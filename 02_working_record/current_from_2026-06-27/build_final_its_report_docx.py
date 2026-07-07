import re
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[2]
MD_PATH = ROOT / "01_official_internship" / "03_internship_report" / "03_final" / "UTM_ITS_Report_Final.md"
OUT_PATH = ROOT / "01_official_internship" / "03_internship_report" / "03_final" / "UTM_ITS_Report_Final.docx"

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"


def xml_escape(text: str) -> str:
    return escape(text, {"'": "&apos;", '"': "&quot;"})


def emu(inches: float) -> int:
    return int(inches * 914400)


def twips(inches: float) -> int:
    return int(inches * 1440)


def image_size(path: Path):
    data = path.read_bytes()
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return int.from_bytes(data[16:20], "big"), int.from_bytes(data[20:24], "big")
    if data[:2] == b"\xff\xd8":
        i = 2
        while i + 9 < len(data):
            if data[i] != 0xFF:
                i += 1
                continue
            marker = data[i + 1]
            i += 2
            if marker in (0xD8, 0xD9):
                continue
            if i + 2 > len(data):
                break
            length = int.from_bytes(data[i:i + 2], "big")
            if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                h = int.from_bytes(data[i + 3:i + 5], "big")
                w = int.from_bytes(data[i + 5:i + 7], "big")
                return w, h
            i += length
    return 1200, 800


def rpr(size=24, bold=False, italic=False, underline=False):
    parts = [
        "<w:rPr>",
        '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>',
        f'<w:sz w:val="{size}"/>',
        f'<w:szCs w:val="{size}"/>',
    ]
    if bold:
        parts.append("<w:b/><w:bCs/>")
    if italic:
        parts.append("<w:i/><w:iCs/>")
    if underline:
        parts.append('<w:u w:val="single"/>')
    parts.append("</w:rPr>")
    return "".join(parts)


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


def parse_inline(text: str, size=24):
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
        else:
            runs.append((token[1:-1], False, False))
        pos = match.end()
    if pos < len(text):
        runs.append((text[pos:], False, False))
    return "".join(
        f'<w:r>{rpr(size, bold, italic)}<w:t xml:space="preserve">{xml_escape(t)}</w:t></w:r>'
        for t, bold, italic in runs
        if t
    )


def paragraph(text="", style=None, align=None, before=0, after=120, line=360,
              first_line=False, keep_next=False, keep_lines=False, bold=False,
              italic=False, underline=False, size=24, left=0, hanging=0,
              page_break_before=False):
    if bold or italic or underline:
        runs = f'<w:r>{rpr(size, bold, italic, underline)}<w:t xml:space="preserve">{xml_escape(text)}</w:t></w:r>'
    else:
        runs = parse_inline(text, size)
    return (
        "<w:p>"
        + ppr(style, align, before, after, line, first_line, keep_next, keep_lines, page_break_before, left, hanging)
        + runs
        + "</w:p>"
    )


def page_break():
    return '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'


def image_paragraph(rel_id: str, name: str, width_px: int, height_px: int, max_width=5.6, max_height=6.9):
    ratio = height_px / max(width_px, 1)
    width = max_width
    height = width * ratio
    if height > max_height:
        height = max_height
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


def toc_field():
    entries = [
        ("ACKNOWLEDGEMENT", 2, 1),
        ("ABSTRACT", 3, 1),
        ("ABSTRAK", 4, 1),
        ("CHAPTER 1: INTRODUCTION", 6, 1),
        ("CHAPTER 2: SPECIFIC DETAILS ON PROJECTS / TRAINING", 8, 1),
        ("CHAPTER 3: OVERALL INFORMATION OF THE INDUSTRIAL TRAINING", 13, 1),
        ("CHAPTER 4: CONCLUSION", 15, 1),
        ("REFERENCES AND WORK MATERIALS", 17, 1),
        ("APPENDICES", 18, 1),
    ]
    parts = [
        '<w:p><w:r><w:fldChar w:fldCharType="begin"/></w:r>'
        '<w:r><w:instrText xml:space="preserve"> TOC \\o "1-3" \\h \\z \\u </w:instrText></w:r>'
        '<w:r><w:fldChar w:fldCharType="separate"/></w:r></w:p>'
    ]
    for title, page, level in entries:
        style = f"TOC{level}"
        parts.append(
            "<w:p>"
            + ppr(style=style, before=0, after=80, line=300)
            + f'<w:r>{rpr(24)}<w:t xml:space="preserve">{xml_escape(title)}</w:t></w:r>'
            + f'<w:r>{rpr(24)}<w:tab/><w:t>{page}</w:t></w:r>'
            + "</w:p>"
        )
    parts.append('<w:p><w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>')
    return "".join(parts)


def parse_table(lines, start):
    rows = []
    i = start
    while i < len(lines) and lines[i].strip().startswith("|"):
        cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
        if not all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
            rows.append(cells)
        i += 1
    return rows, i


def table_widths(col_count):
    total = 9360
    if col_count == 2:
        return [2500, total - 2500]
    if col_count == 3:
        return [2200, 3900, total - 6100]
    if col_count == 4:
        return [1700, 2700, 2500, total - 6900]
    return [int(total / col_count)] * col_count


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
    for r_idx, row in enumerate(rows):
        tbl.append("<w:tr>")
        if r_idx == 0:
            tbl.append("<w:trPr><w:tblHeader/></w:trPr>")
        for c_idx in range(col_count):
            text = row[c_idx] if c_idx < len(row) else ""
            shading = '<w:shd w:fill="EAF2F8"/>' if r_idx == 0 else ""
            tbl.append("<w:tc>")
            tbl.append(
                f'<w:tcPr><w:tcW w:w="{widths[c_idx]}" w:type="dxa"/>{shading}'
                '<w:vAlign w:val="center"/>'
                '<w:tcMar><w:top w:w="100" w:type="dxa"/><w:left w:w="120" w:type="dxa"/>'
                '<w:bottom w:w="100" w:type="dxa"/><w:right w:w="120" w:type="dxa"/></w:tcMar></w:tcPr>'
            )
            tbl.append(paragraph(text, before=0, after=0, line=276, bold=(r_idx == 0), size=21))
            tbl.append("</w:tc>")
        tbl.append("</w:tr>")
    tbl.append("</w:tbl>")
    tbl.append(paragraph("", before=0, after=120, line=240))
    return "".join(tbl)


def build_body(md_text):
    lines = md_text.splitlines()
    body = []
    image_paths = []
    para_buffer = []
    cover_mode = True

    def flush_para():
        nonlocal para_buffer
        if not para_buffer:
            return
        text = " ".join(x.strip() for x in para_buffer if x.strip())
        para_buffer = []
        if text:
            body.append(paragraph(text, align="both", first_line=True, keep_lines=True))

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            flush_para()
            i += 1
            continue
        if line == "<!-- PAGE BREAK -->":
            flush_para()
            body.append(page_break())
            cover_mode = False
            i += 1
            continue
        if line == "[[TOC]]":
            flush_para()
            body.append(toc_field())
            i += 1
            continue
        if line.startswith("|"):
            flush_para()
            rows, i = parse_table(lines, i)
            if rows:
                body.append(table_xml(rows))
            continue
        img = re.match(r"!\[(.*?)\]\((.*?)\)", line)
        if img:
            flush_para()
            caption, link = img.groups()
            img_path = (MD_PATH.parent / link).resolve()
            if img_path.exists():
                image_paths.append(img_path)
                rid = f"rImg{len(image_paths)}"
                w, h = image_size(img_path)
                if "utm_logo" in str(img_path):
                    body.append(image_paragraph(rid, caption, w, h, max_width=2.4, max_height=1.0))
                elif "li_task" in str(img_path):
                    body.append(image_paragraph(rid, caption, w, h, max_width=2.8, max_height=3.95))
                else:
                    body.append(image_paragraph(rid, caption, w, h, max_width=5.7, max_height=4.3))
            i += 1
            continue
        if line.startswith("*Figure") and line.endswith("*"):
            flush_para()
            body.append(paragraph(line.strip("*"), style="Caption", align="center", italic=True, size=22, keep_lines=True))
            i += 1
            continue
        if line.startswith("# "):
            flush_para()
            title = line[2:].strip()
            if cover_mode:
                if title == "SCSR4114 Internship-Report":
                    body.append(paragraph(title, align="center", underline=True, size=24, before=0, after=420, line=360, keep_next=True))
                else:
                    body.append(paragraph(title, align="center", bold=True, size=28, before=0, after=160, line=360, keep_next=True))
            else:
                body.append(paragraph(title, style="Heading1", align="center", bold=True, size=28, before=0, after=240, line=360, keep_next=True))
            i += 1
            continue
        if line.startswith("## "):
            flush_para()
            body.append(paragraph(line[3:].strip(), style="Heading2", bold=True, size=24, before=180, after=120, line=360, keep_next=True))
            i += 1
            continue
        num = re.match(r"^(\d+)\.\s+(.*)", line)
        if num:
            flush_para()
            body.append(paragraph(f"{num.group(1)}. {num.group(2)}", before=0, after=80, line=360, keep_lines=True, left=720, hanging=360))
            i += 1
            continue
        if cover_mode:
            flush_para()
            if line.startswith("**") and line.endswith("**"):
                body.append(paragraph(line.strip("*"), align="center", bold=True, size=24, before=0, after=140, line=360, keep_next=True))
            else:
                body.append(paragraph(line, align="center", size=24, before=0, after=140, line=360, keep_next=True))
            i += 1
            continue
        para_buffer.append(line)
        i += 1
    flush_para()
    return body, image_paths


def styles_xml():
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="{W_NS}">
  <w:docDefaults>
    <w:rPrDefault><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr></w:rPrDefault>
    <w:pPrDefault><w:pPr><w:spacing w:line="360" w:lineRule="auto"/></w:pPr></w:pPrDefault>
  </w:docDefaults>
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/><w:pPr><w:keepNext/><w:spacing w:before="0" w:after="240" w:line="360" w:lineRule="auto"/><w:jc w:val="center"/><w:outlineLvl w:val="0"/></w:pPr><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/><w:b/><w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/><w:pPr><w:keepNext/><w:spacing w:before="180" w:after="120" w:line="360" w:lineRule="auto"/><w:outlineLvl w:val="1"/></w:pPr><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/><w:b/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Caption"><w:name w:val="Caption"/><w:basedOn w:val="Normal"/><w:qFormat/><w:pPr><w:keepLines/><w:spacing w:before="0" w:after="160" w:line="276" w:lineRule="auto"/><w:jc w:val="center"/></w:pPr><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/><w:i/><w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="TOC1"><w:name w:val="toc 1"/><w:basedOn w:val="Normal"/><w:pPr><w:tabs><w:tab w:val="right" w:leader="dot" w:pos="9350"/></w:tabs><w:spacing w:line="300" w:lineRule="auto"/></w:pPr></w:style>
  <w:style w:type="table" w:styleId="TableGrid"><w:name w:val="Table Grid"/><w:tblPr><w:tblBorders><w:top w:val="single" w:sz="4" w:space="0" w:color="999999"/><w:left w:val="single" w:sz="4" w:space="0" w:color="999999"/><w:bottom w:val="single" w:sz="4" w:space="0" w:color="999999"/><w:right w:val="single" w:sz="4" w:space="0" w:color="999999"/><w:insideH w:val="single" w:sz="4" w:space="0" w:color="BBBBBB"/><w:insideV w:val="single" w:sz="4" w:space="0" w:color="BBBBBB"/></w:tblBorders><w:tblCellMar><w:top w:w="100" w:type="dxa"/><w:left w:w="120" w:type="dxa"/><w:bottom w:w="100" w:type="dxa"/><w:right w:w="120" w:type="dxa"/></w:tblCellMar></w:tblPr></w:style>
</w:styles>"""


def settings_xml():
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:settings xmlns:w="{W_NS}">
  <w:zoom w:percent="100"/>
  <w:updateFields w:val="true"/>
  <w:defaultTabStop w:val="720"/>
</w:settings>"""


def content_types_xml(image_paths):
    defaults = [
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>',
        '<Default Extension="xml" ContentType="application/xml"/>',
    ]
    exts = {p.suffix.lower().lstrip(".") for p in image_paths}
    if "png" in exts:
        defaults.append('<Default Extension="png" ContentType="image/png"/>')
    if "jpeg" in exts or "jpg" in exts:
        defaults.append('<Default Extension="jpeg" ContentType="image/jpeg"/>')
        defaults.append('<Default Extension="jpg" ContentType="image/jpeg"/>')
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  {''.join(defaults)}
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
    for idx, path in enumerate(image_paths, start=1):
        ext = path.suffix.lower().lstrip(".")
        rels.append(f'<Relationship Id="rImg{idx}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/image{idx}.{ext}"/>')
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


def core_xml():
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>UTM Industrial Training Report 2026</dc:title>
  <dc:creator>Sadik Al Mahmud</dc:creator>
  <cp:lastModifiedBy>Codex</cp:lastModifiedBy>
  <dcterms:created xsi:type="dcterms:W3CDTF">2026-07-02T00:00:00Z</dcterms:created>
  <dcterms:modified xsi:type="dcterms:W3CDTF">2026-07-02T00:00:00Z</dcterms:modified>
</cp:coreProperties>"""


def app_xml():
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>Microsoft Word</Application>
</Properties>"""


def build():
    md_text = MD_PATH.read_text(encoding="utf-8")
    body, image_paths = build_body(md_text)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    if OUT_PATH.exists():
        OUT_PATH.unlink()
    with zipfile.ZipFile(OUT_PATH, "w", zipfile.ZIP_DEFLATED) as docx:
        docx.writestr("[Content_Types].xml", content_types_xml(image_paths))
        docx.writestr("_rels/.rels", root_rels_xml())
        docx.writestr("word/document.xml", document_xml(body))
        docx.writestr("word/styles.xml", styles_xml())
        docx.writestr("word/settings.xml", settings_xml())
        docx.writestr("word/footer1.xml", footer_xml())
        docx.writestr("word/_rels/document.xml.rels", doc_rels_xml(image_paths))
        docx.writestr("docProps/core.xml", core_xml())
        docx.writestr("docProps/app.xml", app_xml())
        for idx, image_path in enumerate(image_paths, start=1):
            ext = image_path.suffix.lower().lstrip(".")
            docx.write(image_path, f"word/media/image{idx}.{ext}")
    print(OUT_PATH)
    print(f"images={len(image_paths)}")
    print(f"body_parts={len(body)}")


if __name__ == "__main__":
    build()
