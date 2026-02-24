#!/usr/bin/env python3
"""Convert the AWS EC2 User Guide PDF to structured markdown files.

Uses pymupdf's TOC to drive chapter/section splitting and applies a
post-processing pipeline to fix PDF extraction artifacts (ligatures,
line wrapping, bullets, headers/footers, etc.).

Output structure:
  apps/user-manuals/aws/ec2/
    01-what-is-amazon-ec2.md
    02-get-started.md
    ...
    05-ec2-instances/
      01-instance-types.md
      ...

Rule: L1 chapters < 50 pages -> single file; >= 50 pages -> subdirectory
      with one file per L2 section.
"""

import os
import re
import sys

import pymupdf

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
PDF_PATH = os.path.join(REPO_ROOT, "apps", "user-manuals", "aws", "ec2-ug.pdf")
OUTPUT_DIR = os.path.join(REPO_ROOT, "apps", "user-manuals", "aws", "ec2")
SOURCE_REF = "apps/user-manuals/aws/ec2-ug.pdf"

# L1 chapters to skip entirely
SKIP_L1_TITLES = {
    "Amazon Elastic Compute Cloud",  # cover
    "Table of Contents",
    "Document history for the Amazon EC2 User Guide",
}

PAGE_THRESHOLD = 50  # L1 chapters >= this many pages get split by L2

# Page header lines to strip (appear at top of every page)
PAGE_HEADERS = [
    "Amazon Elastic Compute Cloud",
    "User Guide",
]

# Ligature replacement map
LIGATURES = {
    "\ufb01": "fi",
    "\ufb00": "ff",
    "\ufb02": "fl",
    "\ufb03": "ffi",
    "\ufb04": "ffl",
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def slugify(title: str) -> str:
    """Convert a title to a filename-friendly slug."""
    s = title.lower()
    # Remove common prefixes like "Amazon" for brevity
    for prefix in ["amazon ", "ec2 "]:
        if s.startswith(prefix):
            s = s[len(prefix):]
    # Replace non-alphanum with hyphens
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    # Collapse repeated hyphens
    s = re.sub(r"-+", "-", s)
    # Truncate to reasonable length
    if len(s) > 60:
        s = s[:60].rstrip("-")
    return s


def fix_ligatures(text: str) -> str:
    for lig, replacement in LIGATURES.items():
        text = text.replace(lig, replacement)
    return text


def fix_smart_quotes(text: str) -> str:
    text = text.replace("\u201c", '"').replace("\u201d", '"')
    text = text.replace("\u2018", "'").replace("\u2019", "'")
    return text


def strip_page_footer(lines: list[str]) -> list[str]:
    """Remove the footer (section title + page number) from the end of page text."""
    # Footer pattern: last non-empty line is a bare number, preceded by a section title
    if len(lines) < 2:
        return lines

    # Find last non-empty lines
    trimmed = list(lines)
    while trimmed and not trimmed[-1].strip():
        trimmed.pop()

    if len(trimmed) < 2:
        return lines

    last = trimmed[-1].strip()
    # Check if last line is a bare page number
    if re.match(r"^\d{1,4}$", last):
        # Remove the page number line and the section title line before it
        # Find these lines in the original list and remove them
        result = list(lines)
        # Remove trailing empties, then the number, then the title
        while result and not result[-1].strip():
            result.pop()
        if result and re.match(r"^\d{1,4}$", result[-1].strip()):
            result.pop()  # remove page number
            # Remove the section title line (one more non-empty line)
            while result and not result[-1].strip():
                result.pop()
            if result:
                result.pop()  # remove section title
        return result

    return lines


def strip_page_headers(lines: list[str]) -> list[str]:
    """Remove standard page header lines from the top."""
    result = []
    header_phase = True
    headers_seen = 0
    for line in lines:
        if header_phase:
            stripped = line.strip()
            if not stripped:
                # Skip blank lines at the very top
                if headers_seen > 0:
                    header_phase = False
                continue
            if stripped in PAGE_HEADERS:
                headers_seen += 1
                continue
            header_phase = False
        result.append(line)
    return result


def extract_page_text(doc, page_num_0indexed: int) -> list[str]:
    """Extract text from a single page, stripping headers and footers."""
    page = doc[page_num_0indexed]
    text = page.get_text("text")
    lines = text.split("\n")
    lines = strip_page_headers(lines)
    lines = strip_page_footer(lines)
    return lines


# ---------------------------------------------------------------------------
# TOC parsing and file planning
# ---------------------------------------------------------------------------


def parse_toc(doc):
    """Parse the PDF TOC into a structured chapter list."""
    toc = doc.get_toc()  # list of (level, title, page_1indexed)
    total_pages = doc.page_count

    # Find all L1 entries
    l1_entries = []
    for i, (level, title, page) in enumerate(toc):
        if level == 1:
            l1_entries.append((i, title, page))

    chapters = []
    chapter_num = 0

    for idx, (toc_idx, title, start_page) in enumerate(l1_entries):
        if title in SKIP_L1_TITLES:
            continue

        # Determine end page
        if idx + 1 < len(l1_entries):
            end_page = l1_entries[idx + 1][2] - 1
        else:
            end_page = total_pages

        page_count = end_page - start_page + 1
        chapter_num += 1

        # Collect L2 sections under this L1
        l2_sections = []
        for j in range(toc_idx + 1, len(toc)):
            if toc[j][0] == 1:
                break
            if toc[j][0] == 2:
                l2_sections.append((j, toc[j][1], toc[j][2]))

        # Collect all sub-TOC entries for this chapter
        sub_toc = []
        for j in range(toc_idx + 1, len(toc)):
            if toc[j][0] == 1:
                break
            sub_toc.append(toc[j])

        chapters.append({
            "num": chapter_num,
            "title": title,
            "start_page": start_page,
            "end_page": end_page,
            "page_count": page_count,
            "split": page_count >= PAGE_THRESHOLD,
            "l2_sections": l2_sections,
            "sub_toc": sub_toc,
            "toc_idx": toc_idx,
        })

    return chapters, toc


def plan_files(chapters, toc):
    """Plan the output files from chapter info.

    Returns list of dicts:
      {path, title, start_page, end_page, toc_entries: [(level, title, page)]}
    """
    files = []

    for ch in chapters:
        num_prefix = f"{ch['num']:02d}"
        ch_slug = slugify(ch["title"])

        if not ch["split"]:
            # Single file for this chapter
            filename = f"{num_prefix}-{ch_slug}.md"
            toc_entries = [(1, ch["title"], ch["start_page"])] + ch["sub_toc"]
            files.append({
                "path": filename,
                "title": ch["title"],
                "start_page": ch["start_page"],
                "end_page": ch["end_page"],
                "toc_entries": toc_entries,
                "is_subdir": False,
            })
        else:
            # Subdirectory with one file per L2
            dir_name = f"{num_prefix}-{ch_slug}"

            if not ch["l2_sections"]:
                # No L2 sections, just make a single file
                filename = os.path.join(dir_name, f"01-{ch_slug}.md")
                toc_entries = [(1, ch["title"], ch["start_page"])] + ch["sub_toc"]
                files.append({
                    "path": filename,
                    "title": ch["title"],
                    "start_page": ch["start_page"],
                    "end_page": ch["end_page"],
                    "toc_entries": toc_entries,
                    "is_subdir": True,
                })
                continue

            for l2_idx, (toc_j, l2_title, l2_start) in enumerate(ch["l2_sections"]):
                # Determine L2 end page
                if l2_idx + 1 < len(ch["l2_sections"]):
                    l2_end = ch["l2_sections"][l2_idx + 1][2] - 1
                else:
                    l2_end = ch["end_page"]

                l2_num = f"{l2_idx + 1:02d}"
                l2_slug = slugify(l2_title)
                filename = os.path.join(dir_name, f"{l2_num}-{l2_slug}.md")

                # Collect TOC entries for this L2 section
                # Include the L2 entry itself (shifted to L1) and all deeper entries
                section_toc = []
                for level, title, page in ch["sub_toc"]:
                    if page < l2_start:
                        continue
                    if page > l2_end:
                        break
                    # Shift levels: L2->L1, L3->L2, etc.
                    section_toc.append((level - 1, title, page))

                files.append({
                    "path": filename,
                    "title": l2_title,
                    "start_page": l2_start,
                    "end_page": l2_end,
                    "toc_entries": section_toc,
                    "is_subdir": True,
                })

            # Handle any content between the L1 heading and the first L2
            first_l2_start = ch["l2_sections"][0][2]
            if ch["start_page"] < first_l2_start:
                # There's preamble content before the first L2
                preamble_toc = [(1, ch["title"], ch["start_page"])]
                for level, title, page in ch["sub_toc"]:
                    if page >= first_l2_start:
                        break
                    preamble_toc.append((level - 1, title, page))

                preamble_file = {
                    "path": os.path.join(dir_name, "00-overview.md"),
                    "title": ch["title"],
                    "start_page": ch["start_page"],
                    "end_page": first_l2_start - 1,
                    "toc_entries": preamble_toc,
                    "is_subdir": True,
                }
                files.insert(len(files) - len(ch["l2_sections"]), preamble_file)

    return files


# ---------------------------------------------------------------------------
# Text extraction and heading insertion
# ---------------------------------------------------------------------------


def extract_section_text(doc, start_page: int, end_page: int) -> str:
    """Extract text for a page range (1-indexed), stripping headers/footers."""
    all_lines = []
    for p in range(start_page - 1, end_page):  # 0-indexed
        page_lines = extract_page_text(doc, p)
        all_lines.extend(page_lines)
        all_lines.append("")  # page break separator
    return "\n".join(all_lines)


def insert_headings(text: str, toc_entries: list[tuple]) -> str:
    """Insert markdown headings based on TOC entries.

    For each TOC entry, find its title in the text and replace
    the first occurrence with a markdown heading.
    """
    if not toc_entries:
        return text

    lines = text.split("\n")

    # Build list of (title_to_find, heading_to_insert) sorted by page desc
    # so we process from bottom to top to avoid offset issues
    insertions = []
    for level, title, page in toc_entries:
        md_level = min(level, 6)  # cap at h6
        heading = f"{'#' * md_level} {title}"
        # Clean title for matching (fix ligatures in the search text too)
        clean_title = fix_ligatures(title)
        insertions.append((clean_title, heading, page))

    # Process each TOC entry: find the title text in lines and replace
    used_lines = set()
    for clean_title, heading, page in insertions:
        best_match = None
        # Search for the title in lines (exact match of stripped line)
        for i, line in enumerate(lines):
            if i in used_lines:
                continue
            stripped = line.strip()
            if not stripped:
                continue
            # Try exact match first
            if fix_ligatures(stripped) == clean_title:
                best_match = i
                break
        if best_match is not None:
            lines[best_match] = heading
            used_lines.add(best_match)
        else:
            # Try partial/fuzzy match: title might be split across lines or
            # have minor differences. Try matching just the start.
            for i, line in enumerate(lines):
                if i in used_lines:
                    continue
                stripped = line.strip()
                if not stripped or len(stripped) < 10:
                    continue
                fixed = fix_ligatures(stripped)
                # Check if the line starts with the title (handles truncation)
                if len(clean_title) > 15 and fixed.startswith(clean_title[:30]):
                    lines[i] = heading
                    used_lines.add(i)
                    break

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Post-processing pipeline
# ---------------------------------------------------------------------------


def fix_bullets(text: str) -> str:
    """Fix bullet point formatting.

    Handles:
    - Inline bullets: '• text' -> '- text'
    - Bullets on a line preceded by blank line, followed by text on the
      same or next line
    """
    # Inline bullets
    text = re.sub(r"^(\s*)• ", r"\1- ", text, flags=re.MULTILINE)
    # Bullet character alone on a line followed by text on next line
    text = re.sub(r"^(\s*)•\s*\n(\s*)(\S)", r"\1- \3", text, flags=re.MULTILINE)
    return text


def fix_numbered_lists(text: str) -> str:
    """Fix numbered lists where the number and text got split across lines."""
    # Pattern: line is just "N." followed by text on next line
    text = re.sub(
        r"^(\s*)(\d+)\.\s*\n\s*(\S)",
        r"\1\2. \3",
        text,
        flags=re.MULTILINE,
    )
    return text


def unwrap_paragraphs(text: str) -> str:
    """Join lines broken at ~85 chars back into paragraphs.

    More aggressive than the generic unwrap_paragraphs.py because PDF
    extraction produces continuation lines at column 0 even within list
    items. We join any non-structural line to the previous line if:
    - The previous line doesn't end with sentence punctuation, OR
    - The current line starts with a lowercase letter (strong continuation signal)
    """
    lines = text.split("\n")
    result = []
    in_code_block = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Track code blocks
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_code_block = not in_code_block
            result.append(line)
            continue

        if in_code_block:
            result.append(line)
            continue

        # Blank line
        if not stripped:
            result.append(line)
            continue

        # Structural line (heading, list, table, etc.)
        if _is_structural(stripped):
            result.append(line)
            continue

        # Non-structural, non-blank line: try to join with previous
        if result:
            prev_idx = len(result) - 1
            while prev_idx >= 0 and not result[prev_idx].strip():
                prev_idx -= 1

            if prev_idx >= 0 and prev_idx == len(result) - 1:
                prev = result[prev_idx]
                prev_stripped = prev.strip()

                if not prev_stripped:
                    result.append(line)
                    continue

                # Join if previous line doesn't end a sentence
                if not _ends_sentence(prev):
                    result[prev_idx] = prev.rstrip() + " " + stripped
                    continue

                # Also join if current line starts lowercase (strong
                # continuation signal from PDF line break)
                if stripped and stripped[0].islower():
                    result[prev_idx] = prev.rstrip() + " " + stripped
                    continue

        result.append(line)

    return "\n".join(result)


def _is_structural(stripped: str) -> bool:
    """Check if a stripped line is structural markdown."""
    if stripped.startswith("#"):
        return True
    if re.match(r"^[-*+] ", stripped):
        return True
    if re.match(r"^\d+[.)] ", stripped):
        return True
    if stripped.startswith("|"):
        return True
    if stripped.startswith(">"):
        return True
    if stripped.startswith("```") or stripped.startswith("~~~"):
        return True
    if re.match(r"^(---+|[*]{3,}|___+)\s*$", stripped):
        return True
    if stripped.startswith("Source:"):
        return True
    if stripped.startswith("!["):
        return True
    return False


def _ends_sentence(line: str) -> bool:
    """Check if line ends with sentence-ending punctuation."""
    s = line.rstrip()
    if not s:
        return True
    if s[-1] in ".!?:)>\"'`]":
        return True
    return False


def normalize_whitespace(text: str) -> str:
    """Strip trailing spaces, collapse excessive blank lines."""
    lines = text.split("\n")
    # Strip trailing whitespace per line
    lines = [line.rstrip() for line in lines]
    # Collapse 3+ blank lines to 2
    result = []
    blank_count = 0
    for line in lines:
        if not line:
            blank_count += 1
            if blank_count <= 2:
                result.append(line)
        else:
            blank_count = 0
            result.append(line)
    return "\n".join(result)


def add_file_header(text: str, title: str) -> str:
    """Add a standard file header."""
    header = f"# {title}\n\nSource: {SOURCE_REF}\n\n---\n\n"
    return header + text


def postprocess(text: str) -> str:
    """Full post-processing pipeline."""
    text = fix_ligatures(text)
    text = fix_smart_quotes(text)
    text = fix_bullets(text)
    text = fix_numbered_lists(text)
    text = unwrap_paragraphs(text)
    text = normalize_whitespace(text)
    return text


# ---------------------------------------------------------------------------
# Main conversion
# ---------------------------------------------------------------------------


def convert(pdf_path: str, output_dir: str):
    """Main conversion entry point."""
    print(f"Opening {pdf_path}...")
    doc = pymupdf.open(pdf_path)
    print(f"  Pages: {doc.page_count}")

    toc = doc.get_toc()
    print(f"  TOC entries: {len(toc)}")

    print("\nParsing chapters...")
    chapters, full_toc = parse_toc(doc)
    for ch in chapters:
        split_marker = " [SPLIT]" if ch["split"] else ""
        print(f"  {ch['num']:2d}. {ch['title']} "
              f"(p{ch['start_page']}-{ch['end_page']}, "
              f"{ch['page_count']} pages, "
              f"{len(ch['l2_sections'])} L2s){split_marker}")

    print("\nPlanning files...")
    file_plan = plan_files(chapters, full_toc)
    print(f"  {len(file_plan)} files planned")

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    print("\nExtracting and converting...")
    total_lines = 0
    total_headings_inserted = 0

    for fi, finfo in enumerate(file_plan):
        filepath = os.path.join(output_dir, finfo["path"])
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        # Extract text
        raw_text = extract_section_text(doc, finfo["start_page"], finfo["end_page"])

        # Insert headings from TOC
        text_with_headings = insert_headings(raw_text, finfo["toc_entries"])

        # Count headings inserted
        heading_count = sum(1 for e in finfo["toc_entries"])
        total_headings_inserted += heading_count

        # Post-process
        processed = postprocess(text_with_headings)

        # Add file header (but remove duplicate top-level heading if present)
        # The first TOC entry becomes the file header's # title, so remove
        # any matching heading from the body to avoid duplication
        body_lines = processed.split("\n")
        if body_lines and body_lines[0].startswith("# "):
            first_heading = body_lines[0].lstrip("# ").strip()
            if first_heading == finfo["title"]:
                body_lines = body_lines[1:]
                # Remove leading blank lines after removed heading
                while body_lines and not body_lines[0].strip():
                    body_lines.pop(0)
                processed = "\n".join(body_lines)

        final = add_file_header(processed, finfo["title"])

        # Ensure file ends with newline
        if not final.endswith("\n"):
            final += "\n"

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(final)

        line_count = final.count("\n")
        total_lines += line_count

        pages = finfo["end_page"] - finfo["start_page"] + 1
        print(f"  [{fi+1:3d}/{len(file_plan)}] {finfo['path']} "
              f"({pages} pages, {line_count} lines, {heading_count} headings)")

    doc.close()

    # Verification
    print("\n" + "=" * 70)
    print("CONVERSION COMPLETE")
    print(f"  Files: {len(file_plan)}")
    print(f"  Total lines: {total_lines}")
    print(f"  Headings inserted: {total_headings_inserted}")

    # Check for remaining ligatures
    remaining_ligatures = 0
    for finfo in file_plan:
        filepath = os.path.join(output_dir, finfo["path"])
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        for lig in LIGATURES:
            count = content.count(lig)
            if count:
                remaining_ligatures += count
                print(f"  WARNING: {finfo['path']} has {count} remaining '{lig}' ligatures")

    if remaining_ligatures == 0:
        print("  Ligatures: CLEAN (0 remaining)")
    else:
        print(f"  Ligatures: {remaining_ligatures} remaining")

    print(f"\nOutput: {output_dir}")


if __name__ == "__main__":
    pdf = sys.argv[1] if len(sys.argv) > 1 else PDF_PATH
    out = sys.argv[2] if len(sys.argv) > 2 else OUTPUT_DIR
    convert(pdf, out)
