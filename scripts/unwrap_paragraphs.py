#!/usr/bin/env python3
"""Unwrap line-wrapped paragraphs in markdown files.

Many scraped docs have paragraphs wrapped at ~80 chars. While valid markdown,
this makes raw files harder to read and process by LLMs. This script joins
wrapped paragraph lines into single lines while preserving all structural
elements (headings, lists, code blocks, tables, frontmatter, etc.).

Handles both column-0 paragraphs and indented continuations within list items.
"""
import os
import re
import sys


def is_structural_at_indent(line):
    """Check if line starts a structural element (at whatever indent level)."""
    stripped = line.lstrip()
    if not stripped:
        return False
    # Heading
    if stripped.startswith('#'):
        return True
    # Unordered list item
    if re.match(r'^[-*+] ', stripped):
        return True
    # Ordered list item
    if re.match(r'^\d+[.\)] ', stripped):
        return True
    # Table row
    if stripped.startswith('|'):
        return True
    # Blockquote
    if stripped.startswith('>'):
        return True
    # Code fence
    if stripped.startswith('```') or stripped.startswith('~~~'):
        return True
    # Horizontal rule
    if re.match(r'^(---+|[*]{3,}|___+)\s*$', stripped):
        return True
    # Hugo/Jekyll shortcode
    if stripped.startswith('{{'):
        return True
    # HTML tag
    if re.match(r'^<[a-zA-Z/!]', stripped):
        return True
    # Image
    if stripped.startswith('!['):
        return True
    # Reference-style link definition
    if re.match(r'^\[.+\]:', stripped):
        return True
    # Source header
    if stripped.startswith('Source:'):
        return True
    return False


def ends_sentence(line):
    """Check if line ends with sentence-ending punctuation."""
    s = line.rstrip()
    if not s:
        return True
    if s[-1] in '.!?:)>':
        return True
    # Ends with closing markup
    if s.endswith('```') or s.endswith('-->'):
        return True
    return False


def get_indent(line):
    """Get the number of leading spaces."""
    return len(line) - len(line.lstrip())


def content_indent_of_list_item(line):
    """For a list item line, return the indent where content starts."""
    stripped = line.lstrip()
    base_indent = get_indent(line)
    # Ordered list: "1. text" or "1) text"
    m = re.match(r'^(\d+[.\)] )', stripped)
    if m:
        return base_indent + len(m.group(1))
    # Unordered list: "- text" or "* text" or "+ text"
    m = re.match(r'^([-*+] )', stripped)
    if m:
        return base_indent + len(m.group(1))
    return base_indent


def unwrap_file(filepath):
    """Unwrap paragraphs in a single markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    lines = text.split('\n')
    result = []
    in_frontmatter = False
    in_code_block = False
    frontmatter_count = 0

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Track YAML frontmatter
        if stripped == '---' and not in_code_block:
            if i == 0 or (frontmatter_count == 0 and not any(l.strip() for l in lines[:i])):
                in_frontmatter = True
                frontmatter_count += 1
                result.append(line)
                continue
            elif in_frontmatter and frontmatter_count == 1:
                in_frontmatter = False
                frontmatter_count += 1
                result.append(line)
                continue

        if in_frontmatter:
            result.append(line)
            continue

        # Track code blocks
        if stripped.startswith('```') or stripped.startswith('~~~'):
            if in_code_block:
                in_code_block = False
            else:
                in_code_block = True
            result.append(line)
            continue

        if in_code_block:
            result.append(line)
            continue

        # Blank line - always output as-is
        if not stripped:
            result.append(line)
            continue

        # Structural line - always output as-is
        if is_structural_at_indent(line):
            result.append(line)
            continue

        # Non-structural, non-blank line.
        # Check if it should be joined with the previous non-blank line.
        if result:
            # Find the previous non-blank line
            prev_idx = len(result) - 1
            while prev_idx >= 0 and not result[prev_idx].strip():
                prev_idx -= 1

            if prev_idx >= 0:
                prev_line = result[prev_idx]
                prev_stripped = prev_line.strip()

                # Never join to a structural line (headings, lists, tables, etc.)
                if is_structural_at_indent(prev_line):
                    # Exception: join indented continuation to list items
                    # only if no blank line between them
                    curr_indent = get_indent(line)
                    if prev_idx == len(result) - 1 and curr_indent > 0:
                        expected_indent = content_indent_of_list_item(prev_line)
                        if curr_indent >= expected_indent and not ends_sentence(prev_line):
                            result[prev_idx] = prev_line.rstrip() + ' ' + stripped
                            continue
                    result.append(line)
                    continue

                # Only join if previous line doesn't end a sentence
                if prev_stripped and not ends_sentence(prev_line):
                    prev_indent = get_indent(prev_line)
                    curr_indent = get_indent(line)

                    # Must have no blank line between (prev is the last result line)
                    if prev_idx != len(result) - 1:
                        result.append(line)
                        continue

                    # Check indent compatibility
                    should_join = False

                    if prev_indent == curr_indent and prev_indent == 0:
                        # Both at column 0
                        should_join = True
                    elif curr_indent > 0 and prev_indent >= 0:
                        # Current line is indented - continuation
                        if curr_indent == prev_indent:
                            should_join = True
                        elif curr_indent > prev_indent:
                            should_join = True

                    if should_join:
                        # Join with previous line
                        result[prev_idx] = prev_line.rstrip() + ' ' + stripped
                        continue

        result.append(line)

    new_text = '\n'.join(result)
    # Clean up double spaces
    new_text = re.sub(r'(?<! )  (?! )', ' ', new_text)
    changed = new_text != text
    return changed, len(lines), len(result), new_text


def process_directory(dirpath, dry_run=False):
    """Process all markdown files in a directory."""
    changed_count = 0
    total_files = 0
    total_lines_saved = 0

    for root, dirs, files in os.walk(dirpath):
        for fname in sorted(files):
            if not fname.endswith('.md'):
                continue
            total_files += 1
            filepath = os.path.join(root, fname)
            try:
                changed, orig_lines, new_lines, new_text = unwrap_file(filepath)
            except Exception as e:
                print(f"  ERROR: {filepath}: {e}")
                continue

            if changed:
                changed_count += 1
                lines_saved = orig_lines - new_lines
                total_lines_saved += lines_saved
                if not dry_run:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_text)

    return total_files, changed_count, total_lines_saved


def main():
    dry_run = '--dry-run' in sys.argv
    specific_dirs = [a for a in sys.argv[1:] if not a.startswith('--')]

    manuals_dir = os.path.join(os.path.dirname(__file__), '..', 'apps', 'user-manuals')

    if specific_dirs:
        dirs_to_process = specific_dirs
    else:
        dirs_to_process = ['zendesk', 'gitlab', 'kubernetes', 'figma',
                           'handshake', 'linear', 'stripe', 'procore',
                           'shopify', 'superhuman', 'clio', 'gmail',
                           'aws', 'buildium', 'quickbooks']

    mode = "DRY RUN" if dry_run else "FIXING"
    print(f"Mode: {mode}")
    print(f"{'Directory':<15} {'Files':>6} {'Changed':>8} {'Lines saved':>12}")
    print("-" * 45)

    for dirname in dirs_to_process:
        dirpath = os.path.join(manuals_dir, dirname)
        if not os.path.isdir(dirpath):
            continue
        total, changed, saved = process_directory(dirpath, dry_run=dry_run)
        print(f"{dirname:<15} {total:>6} {changed:>8} {saved:>12}")

    print(f"\n{'Done!' if not dry_run else 'Dry run complete.'}")


if __name__ == '__main__':
    main()
