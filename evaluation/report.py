"""Self-contained HTML report generation."""

import base64
import json
from html import escape
from pathlib import Path


def generate_report(
    results: list[dict],
    model: str,
    timestamp: str,
    run_dir: Path,
) -> str:
    """Write report.html into run_dir and return the path."""
    total = len(results)
    passed = sum(1 for r in results if r["passed"])
    pct = (passed / total * 100) if total else 0

    by_diff: dict[str, dict] = {}
    for r in results:
        d = r.get("difficulty", "")
        if d:
            by_diff.setdefault(d, {"total": 0, "passed": 0})
            by_diff[d]["total"] += 1
            if r["passed"]:
                by_diff[d]["passed"] += 1

    diff_summary_rows = []
    for d in ["easy", "medium", "hard"]:
        if d in by_diff:
            info = by_diff[d]
            p, t = info["passed"], info["total"]
            diff_summary_rows.append(
                f"<tr><td>{d.capitalize()}</td><td>{p}/{t}</td>"
                f"<td>{p / t * 100:.1f}%</td></tr>"
            )

    task_rows = []
    for r in results:
        badge_cls = "pass" if r["passed"] else "fail"
        badge_text = "PASS" if r["passed"] else "FAIL"
        details_html = _build_details_html(run_dir, r)

        task_rows.append(f"""
        <tr>
          <td><code>{escape(r['task_id'])}</code></td>
          <td>{escape(r.get('difficulty', ''))}</td>
          <td><span class="badge {badge_cls}">{badge_text}</span></td>
          <td>{r['steps']}</td>
          <td>{r['elapsed']}s</td>
          <td>{escape(r['verifier_message'])}</td>
        </tr>
        <tr>
          <td colspan="6">
            <details>
              <summary>Details</summary>
              <div class="details-body">
                <p><strong>Instruction:</strong> {escape(r['instruction'])}</p>
                {details_html}
              </div>
            </details>
          </td>
        </tr>""")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Eval Report — {escape(model)} — {escape(timestamp)}</title>
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
         max-width: 1100px; margin: 0 auto; padding: 20px; background: #f8f9fa; }}
  h1, h2 {{ color: #1a1a2e; }}
  .header {{ background: #fff; padding: 20px; border-radius: 8px;
             box-shadow: 0 1px 3px rgba(0,0,0,.1); margin-bottom: 20px; }}
  .header .overall {{ font-size: 2em; font-weight: bold;
                      color: {'#28a745' if pct >= 50 else '#dc3545'}; }}
  table {{ width: 100%; border-collapse: collapse; background: #fff;
           border-radius: 8px; overflow: hidden;
           box-shadow: 0 1px 3px rgba(0,0,0,.1); margin-bottom: 20px; }}
  th, td {{ padding: 10px 14px; text-align: left; border-bottom: 1px solid #eee; }}
  th {{ background: #1a1a2e; color: #fff; }}
  .badge {{ padding: 3px 10px; border-radius: 12px; font-weight: 600;
            font-size: .85em; }}
  .badge.pass {{ background: #d4edda; color: #155724; }}
  .badge.fail {{ background: #f8d7da; color: #721c24; }}
  details {{ cursor: pointer; }}
  .details-body {{ padding: 10px; background: #f1f3f5; border-radius: 4px;
                   margin-top: 6px; font-size: .9em; }}
  .step {{ margin-bottom: 8px; padding: 6px 0; border-bottom: 1px dashed #ddd; }}
  .screenshot {{ max-width: 100%; margin-top: 6px; border: 1px solid #ccc; border-radius: 4px; }}
  code {{ background: #e9ecef; padding: 2px 6px; border-radius: 3px; }}
  .summary-table {{ max-width: 400px; }}
</style>
</head>
<body>
<div class="header">
  <h1>Evaluation Report</h1>
  <p><strong>Model:</strong> {escape(model)} &nbsp;|&nbsp;
     <strong>Date:</strong> {escape(timestamp)} &nbsp;|&nbsp;
     <strong>Tasks:</strong> {total}</p>
  <p class="overall">{passed}/{total} passed ({pct:.1f}%)</p>
</div>

<h2>Summary by Difficulty</h2>
<table class="summary-table">
  <tr><th>Difficulty</th><th>Pass</th><th>Rate</th></tr>
  {''.join(diff_summary_rows)}
</table>

<h2>Task Results</h2>
<table>
  <tr>
    <th>Task</th><th>Difficulty</th><th>Status</th>
    <th>Steps</th><th>Time</th><th>Verifier Message</th>
  </tr>
  {''.join(task_rows)}
</table>
</body>
</html>"""

    report_path = run_dir / "report.html"
    with open(report_path, "w") as f:
        f.write(html)
    return str(report_path)


# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------


def _build_details_html(run_dir: Path, r: dict) -> str:
    """Parse history.json and build expandable step-by-step HTML."""
    history_file = run_dir / r["task_id"] / "history.json"
    if not history_file.exists():
        return ""

    try:
        with open(history_file) as f:
            hist = json.load(f)
    except Exception:
        return "<em>Could not parse history.</em>"

    step_entries = hist if isinstance(hist, list) else hist.get("history", [])
    steps_html: list[str] = []

    for i, step in enumerate(step_entries):
        model_output = step.get("model_output", {}) or {}

        # Thought
        current_state = model_output.get("current_state")
        thought = ""
        if isinstance(current_state, dict):
            thought = escape(str(current_state.get("thought", "")))

        # Actions
        actions = model_output.get("action", []) or []
        if not isinstance(actions, list):
            actions = [actions]
        action_strs = []
        for a in actions:
            if isinstance(a, dict):
                for k, v in a.items():
                    action_strs.append(f"{k}: {escape(str(v))}")

        # Results
        result_entries = step.get("result", []) or []
        if not isinstance(result_entries, list):
            result_entries = [result_entries]
        result_strs = []
        for item in result_entries:
            if isinstance(item, dict):
                if item.get("extracted_content"):
                    result_strs.append(escape(str(item["extracted_content"])))
                if item.get("error"):
                    result_strs.append(f"ERROR: {escape(str(item['error']))}")

        parts = [f"<div class='step'><strong>Step {i + 1}</strong>"]
        if thought:
            parts.append(f"<br><em>Thought:</em> {thought}")
        if action_strs:
            parts.append(f"<br><em>Actions:</em> {'; '.join(action_strs)}")
        if result_strs:
            parts.append(f"<br><em>Result:</em> {'; '.join(result_strs)}")

        # Embed screenshot as base64 inline image
        ss_file = run_dir / r["task_id"] / "screenshots" / f"step_{i}.png"
        if ss_file.exists():
            b64 = base64.b64encode(ss_file.read_bytes()).decode()
            parts.append(
                f"<br><img class='screenshot' src='data:image/png;base64,{b64}' "
                f"alt='Step {i + 1} screenshot'>"
            )

        parts.append("</div>")
        steps_html.append("".join(parts))

    return "\n".join(steps_html)
