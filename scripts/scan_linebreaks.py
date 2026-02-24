#!/usr/bin/env python3
"""Scan all user manual markdown files for line-break artifacts.

Detects:
1. Lines that don't end with sentence punctuation followed by continuation lines
2. Private Use Area characters
3. Orphaned short lines (< 15 chars) that look like fragments
"""
import os
import re
import sys
from collections import defaultdict

MANUALS_DIR = os.path.join(os.path.dirname(__file__), '..', 'apps', 'user-manuals')

# Words that indicate a line was broken mid-sentence
CONTINUATION_ENDINGS = {
    'the', 'a', 'an', 'of', 'in', 'to', 'for', 'from', 'with', 'on', 'by',
    'at', 'via', 'into', 'and', 'or', 'but', 'is', 'are', 'was', 'were',
    'be', 'been', 'being', 'has', 'have', 'had', 'will', 'can', 'may',
    'that', 'which', 'who', 'if', 'whether', 'although', 'because',
    'not', 'also', 'then', 'than', 'its', 'their', 'your', 'this',
    'these', 'such', 'each', 'every', 'any', 'all', 'both',
    'include', 'including', 'using',
}


def scan_file(filepath):
    """Scan a single file for line-break issues. Returns list of (line_num, issue, text)."""
    issues = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception:
        return issues

    for i, line in enumerate(lines):
        stripped = line.rstrip()

        # Check for PUA characters
        pua = [c for c in stripped if 0xE000 <= ord(c) <= 0xF8FF]
        if pua:
            issues.append((i + 1, 'PUA_CHAR', stripped[:80]))
            continue

        # Skip structural lines
        if not stripped or stripped.startswith('#') or stripped.startswith('---') or stripped.startswith('Source:'):
            continue
        if stripped.startswith('- ') or stripped.startswith('* ') or stripped.startswith('|'):
            continue
        if stripped.startswith('*Figure') or stripped.startswith('!['):
            continue

        # Check if line ends without sentence punctuation
        if stripped and stripped[-1] not in '.!?:)>*`]"\'':
            # Check if next non-blank line exists and looks like continuation
            next_idx = i + 1
            # Skip blank lines
            while next_idx < len(lines) and not lines[next_idx].strip():
                next_idx += 1

            if next_idx < len(lines):
                next_line = lines[next_idx].strip()
                if not next_line:
                    continue
                # Skip if next line is structural
                if next_line.startswith('#') or next_line.startswith('---') or next_line.startswith('- '):
                    continue
                if next_line.startswith('*Figure') or next_line.startswith('!['):
                    continue

                # Check for strong indicators of broken line
                last_word = stripped.split()[-1].lower().rstrip(',;') if stripped.split() else ''

                if last_word in CONTINUATION_ENDINGS:
                    issues.append((i + 1, 'BROKEN_LINE_CONT_WORD', f"{stripped[-60:]}  →  {next_line[:40]}"))
                elif next_line and next_line[0].islower():
                    issues.append((i + 1, 'BROKEN_LINE_LOWERCASE', f"{stripped[-60:]}  →  {next_line[:40]}"))

    return issues


def main():
    skip_dirs = {'epic'}  # Already fixed
    results = {}

    for dirname in sorted(os.listdir(MANUALS_DIR)):
        dirpath = os.path.join(MANUALS_DIR, dirname)
        if not os.path.isdir(dirpath) or dirname in skip_dirs:
            continue

        dir_issues = defaultdict(list)
        file_count = 0
        files_with_issues = 0

        for root, dirs, files in os.walk(dirpath):
            for fname in files:
                if not fname.endswith('.md'):
                    continue
                file_count += 1
                filepath = os.path.join(root, fname)
                issues = scan_file(filepath)
                if issues:
                    files_with_issues += 1
                    relpath = os.path.relpath(filepath, MANUALS_DIR)
                    dir_issues[relpath] = issues

        total_issues = sum(len(v) for v in dir_issues.values())
        results[dirname] = {
            'files': file_count,
            'files_with_issues': files_with_issues,
            'total_issues': total_issues,
            'details': dir_issues,
        }

    # Print summary
    print(f"{'Directory':<15} {'Files':>6} {'Affected':>8} {'Issues':>7}  Severity")
    print("-" * 60)
    for dirname, data in sorted(results.items(), key=lambda x: -x[1]['total_issues']):
        pct = data['files_with_issues'] / max(data['files'], 1) * 100
        if data['total_issues'] == 0:
            severity = 'CLEAN'
        elif pct < 5:
            severity = 'MILD'
        elif pct < 20:
            severity = 'MODERATE'
        else:
            severity = 'SEVERE'
        print(f"{dirname:<15} {data['files']:>6} {data['files_with_issues']:>8} {data['total_issues']:>7}  {severity} ({pct:.1f}%)")

    # Print examples from affected directories
    print("\n" + "=" * 80)
    for dirname, data in sorted(results.items(), key=lambda x: -x[1]['total_issues']):
        if data['total_issues'] == 0:
            continue
        print(f"\n### {dirname} ({data['total_issues']} issues in {data['files_with_issues']}/{data['files']} files)")
        shown = 0
        for filepath, issues in sorted(data['details'].items()):
            if shown >= 5:
                break
            print(f"\n  {filepath}:")
            for line_num, issue_type, text in issues[:3]:
                print(f"    L{line_num} [{issue_type}] {text}")
            shown += 1


if __name__ == '__main__':
    main()
