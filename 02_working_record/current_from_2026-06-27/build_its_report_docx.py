import os
import re
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[2]
MD_PATH = ROOT / "01_official_internship" / "03_internship_report" / "01_mapping_outline" / "its_report_2026.md"
OUT_PATH = ROOT / "01_official_internship" / "03_internship_report" / "02_drafts" / "ITS_Report_2026_Draft.docx"

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"


def xml_escape(text: str) -> str:
    return escape(text, {"'": "&apos;", '"': "&quot;"})


def rel_path_from_md(link: str) -> Path:
    return (MD_PATH.parent / link).resolve()


def png_size(path: Path):
    with path.open("rb") as f:
        header = f.read(24)
    if header[:8] != b"\x89PNG\r\n\x1a\n":
        return 1200, 800
    width = int.from_bytes(header[16:20], "big")
    height = int.from_bytes(header[20:24], "big")
    return width, height


def emu(inches: float) -> int:
    return int(inches * 914400)


def twips(inches: float) -> int:
    return int(inches * 1440)


def rpr(size=24, bold=False, italic=False):
    parts = [
        '<w:rPr>',
        '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>',
        f'<w:sz w:val="{size}"/>',
        f'<w:szCs w:val="{size}"/>',
    ]
    if bold:
        parts.append("<w:b/>")
        parts.append("<w:bCs/>")
    if italic:
        parts.append("<w:i/>")
        parts.append("<w:iCs/>")
    parts.append("</w:rPr>")
    return "".join(parts)


def parse_inline(text: str, default_size=24):
    runs = []
    pattern = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)")
    pos = 0
    for match in pattern.finditer(text):
        if match.start() > pos:
            runs.append((text[pos:match.start()], False, False))
        token = match.group(0)
        if token.startswith("**"):
            runs.append((token[2:-2], True, False))
        elif token.startswith("*"):
            runs.append((token[1:-1], False, True))
        elif token.startswith("`"):
            runs.append((token[1:-1], False, False))
        pos = match.end()
    if pos < len(text):
        runs.append((text[pos:], False, False))
    return "".join(
        f'<w:r>{rpr(default_size, bold, italic)}<w:t xml:space="preserve">{xml_escape(t)}</w:t></w:r>'
        for t, bold, italic in runs
        if t
    )


def ppr(style=None, align=None, before=0, after=120, line=360, first_line=False,
        keep_next=False, keep_lines=False, page_break_before=False, left=0, hanging=0):
    parts = ["<w:pPr>"]
    if style:
        parts.append(f'<w:pStyle w:val="{style}"/>')
    if keep_next:
        parts.append("<w:keepNext/>")
    if keep_lines:
        parts.append("<w:keepLines/>")
    if page_break_before:
        parts.append("<w:pageBreakBefore/>")
    if align:
        parts.append(f'<w:jc w:val="{align}"/>')
    parts.append(f'<w:spacing w:before="{before}" w:after="{after}" w:line="{line}" w:lineRule="auto"/>')
    if first_line:
        parts.append('<w:ind w:firstLine="720"/>')
    elif left or hanging:
        hanging_attr = f' w:hanging="{hanging}"' if hanging else ""
        parts.append(f'<w:ind w:left="{left}"{hanging_attr}/>')
    parts.append("</w:pPr>")
    return "".join(parts)


def paragraph(text="", style=None, align=None, before=0, after=120, line=360, first_line=False,
              keep_next=False, keep_lines=False, page_break_before=False, bold=False, italic=False,
              size=24, left=0, hanging=0):
    if bold or italic:
        runs = f'<w:r>{rpr(size, bold, italic)}<w:t xml:space="preserve">{xml_escape(text)}</w:t></w:r>'
    else:
        runs = parse_inline(text, size)
    return (
        "<w:p>"
        + ppr(style, align, before, after, line, first_line, keep_next, keep_lines, page_break_before, left, hanging)
        + runs
        + "</w:p>"
    )


def empty_paragraph():
    return "<w:p/>"


def page_break():
    return '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'


def image_paragraph(rel_id: str, name: str, width_px: int, height_px: int, max_width=5.4):
    ratio = height_px / max(width_px, 1)
    width = max_width
    height = width * ratio
    if height > 6.4:
        height = 6.4
        width = height / ratio
    cx = emu(width)
    cy = emu(height)
    safe_name = xml_escape(name)
    return f"""
<w:p>
  {ppr(align="center", before=120, after=60, line=240, keep_next=True, keep_lines=True)}
  <w:r>
    {rpr(22)}
    <w:drawing>
      <wp:inline xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" distT="0" distB="0" distL="0" distR="0">
        <wp:extent cx="{cx}" cy="{cy}"/>
        <wp:docPr id="1" name="{safe_name}"/>
        <a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
          <a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">
            <pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">
              <pic:nvPicPr>
                <pic:cNvPr id="0" name="{safe_name}"/>
                <pic:cNvPicPr/>
              </pic:nvPicPr>
              <pic:blipFill>
                <a:blip r:embed="{rel_id}"/>
                <a:stretch><a:fillRect/></a:stretch>
              </pic:blipFill>
              <pic:spPr>
                <a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>
                <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
              </pic:spPr>
            </pic:pic>
          </a:graphicData>
        </a:graphic>
      </wp:inline>
    </w:drawing>
  </w:r>
</w:p>
""".strip()


def table_xml(rows):
    col_count = max(len(row) for row in rows)
    widths = table_widths(col_count)
    tbl = [
        "<w:tbl>",
        "<w:tblPr>",
        '<w:tblStyle w:val="TableGrid"/>',
        '<w:tblW w:w="0" w:type="auto"/>',
        '<w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0" w:firstColumn="0" w:lastColumn="0" w:noHBand="0" w:noVBand="1"/>',
        "</w:tblPr>",
        "<w:tblGrid>",
    ]
    for width in widths:
        tbl.append(f'<w:gridCol w:w="{width}"/>')
    tbl.append("</w:tblGrid>")
    for i, row in enumerate(rows):
        tbl.append("<w:tr>")
        if i == 0:
            tbl.append("<w:trPr><w:tblHeader/></w:trPr>")
        for j in range(col_count):
            text = row[j].strip() if j < len(row) else ""
            shading = '<w:shd w:fill="D9EAF7"/>' if i == 0 else ""
            tbl.append("<w:tc>")
            tbl.append(f'<w:tcPr><w:tcW w:w="{widths[j]}" w:type="dxa"/>{shading}<w:vAlign w:val="center"/><w:tcMar><w:top w:w="80" w:type="dxa"/><w:left w:w="100" w:type="dxa"/><w:bottom w:w="80" w:type="dxa"/><w:right w:w="100" w:type="dxa"/></w:tcMar></w:tcPr>')
            align = "center" if (j == 0 and col_count > 2) or len(text) < 18 else None
            tbl.append(paragraph(text, align=align, before=0, after=0, line=276, bold=(i == 0), size=21))
            tbl.append("</w:tc>")
        tbl.append("</w:tr>")
    tbl.append("</w:tbl>")
    tbl.append(paragraph("", before=0, after=120, line=240))
    return "".join(tbl)


def table_widths(col_count):
    total = 9360
    if col_count == 2:
        return [2600, total - 2600]
    if col_count == 3:
        return [2200, 4300, total - 6500]
    if col_count == 4:
        return [2000, 2200, 2700, total - 6900]
    if col_count == 5:
        return [1300, 2100, 2200, 1900, total - 7500]
    return [int(total / col_count)] * col_count


def parse_table(lines, start):
    rows = []
    i = start
    while i < len(lines) and lines[i].strip().startswith("|"):
        raw = lines[i].strip()
        cells = [c.strip() for c in raw.strip("|").split("|")]
        if not all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
            rows.append(cells)
        i += 1
    return rows, i


def styles_xml():
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="{W_NS}">
  <w:docDefaults>
    <w:rPrDefault><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr></w:rPrDefault>
    <w:pPrDefault><w:pPr><w:spacing w:line="360" w:lineRule="auto"/></w:pPr></w:pPrDefault>
  </w:docDefaults>
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/><w:pPr><w:keepNext/><w:spacing w:before="0" w:after="240" w:line="360" w:lineRule="auto"/><w:jc w:val="center"/></w:pPr><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/><w:b/><w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/><w:pPr><w:keepNext/><w:spacing w:before="180" w:after="120" w:line="360" w:lineRule="auto"/></w:pPr><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/><w:b/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Caption"><w:name w:val="Caption"/><w:basedOn w:val="Normal"/><w:qFormat/><w:pPr><w:keepNext/><w:keepLines/><w:spacing w:before="0" w:after="160" w:line="276" w:lineRule="auto"/><w:jc w:val="center"/></w:pPr><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/><w:i/><w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr></w:style>
  <w:style w:type="table" w:styleId="TableGrid"><w:name w:val="Table Grid"/><w:basedOn w:val="TableNormal"/><w:uiPriority w:val="59"/><w:tblPr><w:tblBorders><w:top w:val="single" w:sz="4" w:space="0" w:color="999999"/><w:left w:val="single" w:sz="4" w:space="0" w:color="999999"/><w:bottom w:val="single" w:sz="4" w:space="0" w:color="999999"/><w:right w:val="single" w:sz="4" w:space="0" w:color="999999"/><w:insideH w:val="single" w:sz="4" w:space="0" w:color="BBBBBB"/><w:insideV w:val="single" w:sz="4" w:space="0" w:color="BBBBBB"/></w:tblBorders><w:tblCellMar><w:top w:w="80" w:type="dxa"/><w:left w:w="100" w:type="dxa"/><w:bottom w:w="80" w:type="dxa"/><w:right w:w="100" w:type="dxa"/></w:tblCellMar></w:tblPr></w:style>
</w:styles>"""


def settings_xml():
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:settings xmlns:w="{W_NS}">
  <w:zoom w:percent="100"/>
  <w:defaultTabStop w:val="720"/>
  <w:compat/>
</w:settings>"""


def content_types_xml(image_count):
    image_defaults = '<Default Extension="png" ContentType="image/png"/>'
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  {image_defaults}
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
  <Override PartName="/word/settings.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"/>
  <Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>"""


def root_rels_xml():
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>"""


def doc_rels_xml(image_paths):
    rels = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">',
        '<Relationship Id="rFooter1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>',
    ]
    for idx, _ in enumerate(image_paths, start=1):
        rels.append(f'<Relationship Id="rImg{idx}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/image{idx}.png"/>')
    rels.append("</Relationships>")
    return "".join(rels)


def footer_xml():
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:ftr xmlns:w="{W_NS}" xmlns:r="{R_NS}">
  <w:p>
    <w:pPr><w:jc w:val="center"/></w:pPr>
    <w:r>{rpr(20)}<w:fldChar w:fldCharType="begin"/></w:r>
    <w:r>{rpr(20)}<w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>
    <w:r>{rpr(20)}<w:fldChar w:fldCharType="separate"/></w:r>
    <w:r>{rpr(20)}<w:t>1</w:t></w:r>
    <w:r>{rpr(20)}<w:fldChar w:fldCharType="end"/></w:r>
  </w:p>
</w:ftr>"""


def core_xml():
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>Industrial Training Report 2026</dc:title>
  <dc:creator>Sadik Al Mahmud</dc:creator>
  <cp:lastModifiedBy>Codex</cp:lastModifiedBy>
  <dcterms:created xsi:type="dcterms:W3CDTF">2026-06-28T00:00:00Z</dcterms:created>
  <dcterms:modified xsi:type="dcterms:W3CDTF">2026-06-28T00:00:00Z</dcterms:modified>
</cp:coreProperties>"""


def app_xml():
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>Microsoft Word</Application>
</Properties>"""


def build_body(md_text):
    lines = md_text.splitlines()
    body = []
    image_paths = []
    i = 0
    cover_mode = True
    paragraph_buffer = []

    def flush_para():
        nonlocal paragraph_buffer
        if not paragraph_buffer:
            return
        text = " ".join(x.strip() for x in paragraph_buffer if x.strip())
        paragraph_buffer = []
        if text:
            body.append(paragraph(text, align="both", first_line=True, keep_lines=True))

    while i < len(lines):
        raw = lines[i]
        line = raw.strip()

        if line in ("<div align=\"center\">", "</div>"):
            i += 1
            continue

        if line == "<!-- PAGE BREAK -->":
            flush_para()
            body.append(page_break())
            cover_mode = False
            i += 1
            continue

        if not line:
            flush_para()
            i += 1
            continue

        if line.startswith("|"):
            flush_para()
            rows, nxt = parse_table(lines, i)
            if rows:
                body.append(table_xml(rows))
            i = nxt
            continue

        img_match = re.match(r"!\[(.*?)\]\((.*?)\)", line)
        if img_match:
            flush_para()
            caption = img_match.group(1)
            link = img_match.group(2)
            image_path = rel_path_from_md(link)
            if image_path.exists():
                image_paths.append(image_path)
                rel_id = f"rImg{len(image_paths)}"
                w, h = png_size(image_path)
                body.append(image_paragraph(rel_id, caption, w, h))
            i += 1
            continue

        if line.startswith("*Figure") and line.endswith("*"):
            flush_para()
            body.append(paragraph(line.strip("*"), style="Caption", align="center", italic=True, size=22, keep_next=True, keep_lines=True))
            i += 1
            continue

        if line.startswith("# "):
            flush_para()
            title = line[2:].strip()
            if title == "LIST OF FIGURES" and body and not body[-1].startswith('<w:p><w:r><w:br'):
                body.append(page_break())
            if title == "INDUSTRIAL TRAINING REPORT":
                body.append(paragraph(title, align="center", bold=True, size=28, before=0, after=240, line=360, keep_next=True))
            elif title.startswith("CHAPTER "):
                body.append(paragraph(title, style="Heading1", align="center", bold=True, size=28, before=0, after=240, line=360, keep_next=True, page_break_before=False))
            else:
                body.append(paragraph(title, align="center", bold=True, size=28, before=0, after=240, line=360, keep_next=True))
            i += 1
            continue

        if line.startswith("## "):
            flush_para()
            body.append(paragraph(line[3:].strip(), style="Heading2", bold=True, size=24, before=180, after=120, line=360, keep_next=True))
            i += 1
            continue

        num_match = re.match(r"^(\d+)\.\s+(.*)", line)
        bullet_match = re.match(r"^-\s+(.*)", line)
        if num_match:
            flush_para()
            body.append(paragraph(f"{num_match.group(1)}. {num_match.group(2)}", before=0, after=80, line=360, keep_lines=True, left=720, hanging=360))
            i += 1
            continue
        if bullet_match:
            flush_para()
            body.append(paragraph(f"- {bullet_match.group(1)}", before=0, after=80, line=360, keep_lines=True, left=720, hanging=360))
            i += 1
            continue

        if cover_mode and line.startswith("**") and line.endswith("**"):
            flush_para()
            text = line.strip("*")
            size = 26 if text in ("UNIVERSITI TEKNOLOGI MALAYSIA", "INDUSTRIAL TRAINING REPORT") else 24
            body.append(paragraph(text, align="center", bold=True, size=size, before=0, after=160, line=360, keep_next=True))
            i += 1
            continue

        if cover_mode:
            flush_para()
            body.append(paragraph(line, align="center", size=24, before=0, after=160, line=360, keep_next=True))
            i += 1
            continue

        if line.startswith("`") and line.endswith("`"):
            flush_para()
            body.append(paragraph(line.strip("`"), align="center", size=22, before=0, after=120, line=300, keep_lines=True))
            i += 1
            continue

        paragraph_buffer.append(line)
        i += 1

    flush_para()
    return body, image_paths


def document_xml(body_parts):
    sect = f"""
<w:sectPr>
  <w:footerReference w:type="default" r:id="rFooter1"/>
  <w:pgSz w:w="11906" w:h="16838"/>
  <w:pgMar w:top="{twips(1.0)}" w:right="{twips(1.0)}" w:bottom="{twips(1.0)}" w:left="{twips(1.5)}" w:header="720" w:footer="720" w:gutter="0"/>
  <w:cols w:space="720"/>
  <w:docGrid w:linePitch="360"/>
</w:sectPr>
""".strip()
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="{W_NS}" xmlns:r="{R_NS}" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">
  <w:body>
    {''.join(body_parts)}
    {sect}
  </w:body>
</w:document>"""


def build():
    md_text = MD_PATH.read_text(encoding="utf-8")
    body, image_paths = build_body(md_text)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    if OUT_PATH.exists():
        OUT_PATH.unlink()
    with zipfile.ZipFile(OUT_PATH, "w", zipfile.ZIP_DEFLATED) as docx:
        docx.writestr("[Content_Types].xml", content_types_xml(len(image_paths)))
        docx.writestr("_rels/.rels", root_rels_xml())
        docx.writestr("word/document.xml", document_xml(body))
        docx.writestr("word/styles.xml", styles_xml())
        docx.writestr("word/settings.xml", settings_xml())
        docx.writestr("word/footer1.xml", footer_xml())
        docx.writestr("word/_rels/document.xml.rels", doc_rels_xml(image_paths))
        docx.writestr("docProps/core.xml", core_xml())
        docx.writestr("docProps/app.xml", app_xml())
        for idx, image_path in enumerate(image_paths, start=1):
            docx.write(image_path, f"word/media/image{idx}.png")
    print(OUT_PATH)
    print(f"images={len(image_paths)}")
    print(f"body_parts={len(body)}")


if __name__ == "__main__":
    build()
