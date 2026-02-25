#!/usr/bin/env python3
"""Regenerate report.html from existing results.json files.

Usage:
    # Specific run directories
    python evaluation/regenerate_report.py apps/gmail/results/gemini_20260225_003422_parallel

    # All results under apps/ (auto-discovers every results.json)
    python evaluation/regenerate_report.py
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from report import generate_report

REPO_ROOT = Path(__file__).resolve().parent.parent


def find_all_run_dirs():
    """Find all directories containing results.json under apps/."""
    return sorted(p.parent for p in REPO_ROOT.glob("apps/**/results.json"))


def main():
    if len(sys.argv) >= 2:
        run_dirs = [Path(a).resolve() for a in sys.argv[1:]]
    else:
        run_dirs = find_all_run_dirs()

    if not run_dirs:
        print("No results.json found.")
        return

    for run_dir in run_dirs:
        results_file = run_dir / "results.json"
        if not results_file.exists():
            print(f"SKIP  {run_dir} (no results.json)")
            continue

        report_file = run_dir / "report.html"
        if report_file.exists():
            print(f"SKIP  {run_dir} (report.html already exists)")
            continue

        with open(results_file) as f:
            aggregate = json.load(f)

        report_path = generate_report(
            results=aggregate["tasks"],
            model=aggregate["model"],
            timestamp=aggregate["timestamp"],
            run_dir=run_dir,
        )
        print(f"  OK  {report_path}")


if __name__ == "__main__":
    main()
