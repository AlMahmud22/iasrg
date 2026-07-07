$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$FinalDir = Join-Path $Root "01_official_internship\03_internship_report\03_final"
$MdPath = Join-Path $FinalDir "UTM_ITS_Report_Final.md"
$TargetDocx = Join-Path $FinalDir "Template-Tesis-UTM-v2-PSM-UG-SC-Research-u.docx"
$CleanTemplate = Join-Path $Root "02_working_record\03_cyber_fraud_research_report_2026-04_to_2026-06\research_report_guidelines\Template_Tesis_UTM_PSM_UG_SC_Research.docx"
$AssetDir = Join-Path $FinalDir "assets"

if (-not (Test-Path -LiteralPath $MdPath)) { throw "Missing Markdown source: $MdPath" }
if (-not (Test-Path -LiteralPath $CleanTemplate)) { throw "Missing clean template source: $CleanTemplate" }

Copy-Item -LiteralPath $CleanTemplate -Destination $TargetDocx -Force

function Strip-ChapterHeading([string]$Text) {
    return (($Text -replace '^(?i)CHAPTER\s+\d+\s*:\s*', '').Trim())
}

function Strip-NumberedHeading([string]$Text) {
    return (($Text -replace '^\d+(?:\.\d+)+\s+', '').Trim())
}

function Get-ImageSize([string]$Path) {
    Add-Type -AssemblyName System.Drawing
    $img = [System.Drawing.Image]::FromFile($Path)
    try {
        return @{ Width = $img.Width; Height = $img.Height }
    } finally {
        $img.Dispose()
    }
}

function Set-SelectionStyle([object]$Selection, [string]$StyleName) {
    $Selection.Style = $StyleName
}

function Write-InlineText([object]$Selection, [string]$Text) {
    $pattern = '(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)'
    $matches = [regex]::Matches($Text, $pattern)
    $position = 0

    foreach ($match in $matches) {
        if ($match.Index -gt $position) {
            $Selection.Font.Bold = 0
            $Selection.Font.Italic = 0
            $Selection.TypeText($Text.Substring($position, $match.Index - $position))
        }

        $token = $match.Value
        if ($token.StartsWith("**")) {
            $Selection.Font.Bold = -1
            $Selection.Font.Italic = 0
            $Selection.TypeText($token.Substring(2, $token.Length - 4))
        } elseif ($token.StartsWith("*")) {
            $Selection.Font.Bold = 0
            $Selection.Font.Italic = -1
            $Selection.TypeText($token.Substring(1, $token.Length - 2))
        } else {
            $Selection.Font.Bold = 0
            $Selection.Font.Italic = 0
            $Selection.TypeText($token.Substring(1, $token.Length - 2))
        }
        $position = $match.Index + $match.Length
    }

    if ($position -lt $Text.Length) {
        $Selection.Font.Bold = 0
        $Selection.Font.Italic = 0
        $Selection.TypeText($Text.Substring($position))
    }

    $Selection.Font.Bold = 0
    $Selection.Font.Italic = 0
}

function Add-Paragraph([object]$Selection, [string]$Text, [string]$StyleName, [int]$Alignment = -1) {
    Set-SelectionStyle $Selection $StyleName
    if ($Alignment -ge 0) { $Selection.ParagraphFormat.Alignment = $Alignment }
    $Selection.ParagraphFormat.WidowControl = -1
    $Selection.ParagraphFormat.KeepTogether = -1
    if ($StyleName -match "Caption") {
        $Selection.ParagraphFormat.KeepWithNext = 0
        $Selection.ParagraphFormat.SpaceAfter = 18
    } elseif ($StyleName -match "Heading|TITLE|References|Appendix") {
        $Selection.ParagraphFormat.KeepWithNext = -1
    } else {
        $Selection.ParagraphFormat.KeepWithNext = 0
    }
    Write-InlineText $Selection $Text
    $Selection.TypeParagraph()
}

function Add-PlainParagraph([object]$Selection, [string]$Text, [string]$StyleName, [int]$Alignment = -1) {
    Set-SelectionStyle $Selection $StyleName
    if ($Alignment -ge 0) { $Selection.ParagraphFormat.Alignment = $Alignment }
    $Selection.ParagraphFormat.WidowControl = -1
    $Selection.ParagraphFormat.KeepTogether = -1
    if ($StyleName -match "Caption") {
        $Selection.ParagraphFormat.KeepWithNext = 0
        $Selection.ParagraphFormat.SpaceAfter = 18
    } elseif ($StyleName -match "Heading|TITLE|References|Appendix") {
        $Selection.ParagraphFormat.KeepWithNext = -1
    } else {
        $Selection.ParagraphFormat.KeepWithNext = 0
    }
    $Selection.TypeText($Text)
    $Selection.TypeParagraph()
}

function Add-Image([object]$Selection, [string]$ImagePath, [double]$MaxWidthPt, [double]$MaxHeightPt) {
    Set-SelectionStyle $Selection "Figure Centre"
    $Selection.ParagraphFormat.Alignment = 1
    $shape = $Selection.InlineShapes.AddPicture($ImagePath, $false, $true)
    $shape.LockAspectRatio = -1
    if ($shape.Width -gt $MaxWidthPt) { $shape.Width = $MaxWidthPt }
    if ($shape.Height -gt $MaxHeightPt) { $shape.Height = $MaxHeightPt }
    $shape.Range.ParagraphFormat.Alignment = 1
    $Selection.EndKey(6) | Out-Null
    $Selection.TypeParagraph()
}

function Flush-Buffer([object]$Selection, [System.Collections.Generic.List[string]]$Buffer, [bool]$InCover) {
    if ($Buffer.Count -eq 0) { return }
    $text = (($Buffer | ForEach-Object { $_.Trim() }) -join " ").Trim()
    $Buffer.Clear()
    if ($text.Length -eq 0) { return }

    if ($InCover) {
        Add-Paragraph $Selection $text "COVER AND MAIN FONT" 1
    } elseif ($text -match '^\d+\.\s+') {
        Add-Paragraph $Selection $text "Para 2 lines"
    } else {
        Add-Paragraph $Selection $text "Para 2 lines"
    }
}

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0

try {
    $doc = $word.Documents.Open($TargetDocx)
    $selection = $word.Selection
    if ($doc.ProtectionType -ne -1) {
        try { $doc.Unprotect() } catch { }
    }
    while ($doc.ContentControls.Count -gt 0) {
        $control = $doc.ContentControls.Item(1)
        try { $control.LockContentControl = $false } catch { }
        try { $control.LockContents = $false } catch { }
        $control.Delete($true)
    }
    $selection.WholeStory()
    $selection.Delete() | Out-Null
    $selection.HomeKey(6) | Out-Null

    $lines = Get-Content -LiteralPath $MdPath
    $buffer = New-Object 'System.Collections.Generic.List[string]'
    $inCover = $true

    foreach ($line in $lines) {
        $raw = $line.TrimEnd()
        $trimmed = $raw.Trim()

        if ($trimmed -eq "<!-- PAGE BREAK -->") {
            Flush-Buffer $selection $buffer $inCover
            $selection.InsertBreak(7)
            $inCover = $false
            continue
        }

        if ($trimmed -match '^!\[([^\]]*)\]\(([^)]+)\)$') {
            Flush-Buffer $selection $buffer $inCover
            $assetName = Split-Path -Leaf $Matches[2]
            $imagePath = Join-Path $AssetDir $assetName
            if (-not (Test-Path -LiteralPath $imagePath)) { throw "Missing image asset: $imagePath" }

            if ($inCover) {
                Add-Image $selection $imagePath 135 60
            } elseif ($assetName -eq "li_task_page1.png") {
                Add-Image $selection $imagePath 390 610
            } elseif ($assetName -eq "wazuh_lab_flow.png") {
                Add-Image $selection $imagePath 390 130
            } else {
                Add-Image $selection $imagePath 390 320
            }
            continue
        }

        if ($trimmed -eq "[[TOC]]") {
            Flush-Buffer $selection $buffer $inCover
            $toc = $doc.TablesOfContents.Add(
                $selection.Range,
                $true,
                1,
                3,
                $false,
                "",
                $true,
                $true,
                "TITLE AT PREFACE,1,References,1,Appendix,1",
                $false,
                $true,
                $true
            )
            $toc.Update() | Out-Null
            $selection.SetRange($toc.Range.End, $toc.Range.End) | Out-Null
            $selection.EndKey(6) | Out-Null
            $selection.TypeParagraph()
            continue
        }

        if ($trimmed -match '^(#+)\s+(.+)$') {
            Flush-Buffer $selection $buffer $inCover
            $level = $Matches[1].Length
            $text = $Matches[2].Trim()
            $upper = $text.ToUpperInvariant()

            if ($inCover) {
                Add-Paragraph $selection $text "COVER AND MAIN FONT" 1
            } elseif ($level -eq 1 -and $upper.StartsWith("CHAPTER")) {
                Add-PlainParagraph $selection (Strip-ChapterHeading $text) "Heading 1"
            } elseif ($level -eq 1 -and @("ACKNOWLEDGEMENT", "ABSTRACT", "ABSTRAK", "TABLE OF CONTENTS") -contains $upper) {
                Add-PlainParagraph $selection $upper "TITLE AT PREFACE"
            } elseif ($level -eq 1 -and $upper.StartsWith("REFERENCES")) {
                Add-PlainParagraph $selection $upper "References"
            } elseif ($level -eq 1 -and $upper -eq "APPENDICES") {
                Add-PlainParagraph $selection $upper "TITLE AT PREFACE"
            } elseif ($level -eq 1) {
                Add-PlainParagraph $selection $upper "TITLE AT PREFACE"
            } elseif ($level -eq 2 -and $text.ToLowerInvariant().StartsWith("appendix ")) {
                Add-PlainParagraph $selection $text "Appendix"
            } elseif ($level -eq 2) {
                Add-PlainParagraph $selection (Strip-NumberedHeading $text) "Heading 2"
            } elseif ($level -eq 3) {
                Add-PlainParagraph $selection (Strip-NumberedHeading $text) "Heading 3"
            } else {
                Add-PlainParagraph $selection (Strip-NumberedHeading $text) "Para 2 lines"
            }
            continue
        }

        if ((-not $inCover) -and $trimmed.StartsWith("*") -and $trimmed.EndsWith("*") -and $trimmed.Length -gt 2) {
            Flush-Buffer $selection $buffer $inCover
            $caption = $trimmed.Trim("*").Trim()
            Add-PlainParagraph $selection $caption "Caption for Figure"
            continue
        }

        if ($trimmed.Length -eq 0) {
            Flush-Buffer $selection $buffer $inCover
            continue
        }

        $buffer.Add($raw)
    }

    Flush-Buffer $selection $buffer $inCover

    try {
        $doc.Styles.Item("Hyperlink").Font.Color = 0
        $doc.Styles.Item("Hyperlink").Font.Underline = 0
        $doc.Styles.Item("FollowedHyperlink").Font.Color = 0
        $doc.Styles.Item("FollowedHyperlink").Font.Underline = 0
    } catch { }
    foreach ($field in $doc.Fields) { $field.Update() | Out-Null }
    foreach ($toc in $doc.TablesOfContents) {
        $toc.Update() | Out-Null
        $toc.Range.Font.Color = 0
        $toc.Range.Font.Underline = 0
        foreach ($paragraph in $toc.Range.Paragraphs) {
            $paragraph.Range.Font.Color = 0
            $paragraph.Range.Font.Underline = 0
        }
    }
    $doc.Save()
    $doc.Close()
    Write-Output "Updated template DOCX: $TargetDocx"
} finally {
    $word.Quit()
}
