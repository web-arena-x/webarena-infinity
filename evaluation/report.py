"""Self-contained HTML report generation."""

import base64
import json
from html import escape
from io import BytesIO
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
# Coordinate overlay drawing
# ------------------------------------------------------------------


def _draw_action_overlay(image_bytes: bytes, actions: list[dict]) -> bytes:
    """Draw coordinate markers onto a screenshot image.

    Draws directly onto the image using PIL:
      - click/double_click: crosshair + circle
      - type: crosshair + text label
      - scroll: arrow indicating direction
      - drag: line from source to destination
      - hover: small circle

    Returns the modified image as PNG bytes.
    """
    from PIL import Image, ImageDraw, ImageFont

    img = Image.open(BytesIO(image_bytes)).convert("RGBA")
    # Create a transparent overlay to draw on
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # Try to load a font; fall back to default
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)
    except (OSError, IOError):
        font = ImageFont.load_default()

    # Colors
    CLICK_COLOR = (255, 50, 50, 200)       # red
    TYPE_COLOR = (50, 150, 255, 200)        # blue
    SCROLL_COLOR = (50, 200, 50, 200)       # green
    DRAG_COLOR = (255, 165, 0, 200)         # orange
    HOVER_COLOR = (180, 100, 255, 200)      # purple
    LABEL_BG = (0, 0, 0, 160)              # dark background for text

    for i, action in enumerate(actions):
        kind = action.get("type", "")
        x = action.get("x")
        y = action.get("y")

        if kind in ("click", "double_click") and x is not None and y is not None:
            r = 12 if kind == "double_click" else 8
            # Crosshair
            draw.line([(x - 15, y), (x + 15, y)], fill=CLICK_COLOR, width=2)
            draw.line([(x, y - 15), (x, y + 15)], fill=CLICK_COLOR, width=2)
            # Circle
            draw.ellipse(
                [(x - r, y - r), (x + r, y + r)],
                outline=CLICK_COLOR, width=2,
            )
            # Label
            label = "dblclick" if kind == "double_click" else "click"
            if action.get("button") == "right":
                label = "right-click"
            _draw_label(draw, x + 14, y - 10, label, CLICK_COLOR, LABEL_BG, font)

        elif kind == "type" and x is not None and y is not None:
            # Crosshair at click target
            draw.line([(x - 12, y), (x + 12, y)], fill=TYPE_COLOR, width=2)
            draw.line([(x, y - 12), (x, y + 12)], fill=TYPE_COLOR, width=2)
            draw.ellipse([(x - 6, y - 6), (x + 6, y + 6)], outline=TYPE_COLOR, width=2)
            # Show typed text
            text = action.get("text", "")
            display_text = text[:30] + ("..." if len(text) > 30 else "")
            label = f'type: "{display_text}"'
            _draw_label(draw, x + 10, y - 10, label, TYPE_COLOR, LABEL_BG, font)

        elif kind == "type":
            # Type without coordinates (just keyboard input)
            text = action.get("text", "")
            display_text = text[:30] + ("..." if len(text) > 30 else "")
            label = f'type: "{display_text}"'
            _draw_label(draw, 10, 10 + i * 22, label, TYPE_COLOR, LABEL_BG, font)

        elif kind == "scroll" and x is not None and y is not None:
            direction = action.get("direction", "down")
            amount = action.get("amount", 3)
            # Arrow showing scroll direction
            arrow_len = min(40, amount * 12)
            dx, dy = {"up": (0, -arrow_len), "down": (0, arrow_len),
                       "left": (-arrow_len, 0), "right": (arrow_len, 0)}.get(direction, (0, arrow_len))
            ex, ey = x + dx, y + dy
            draw.line([(x, y), (ex, ey)], fill=SCROLL_COLOR, width=3)
            # Arrowhead
            _draw_arrowhead(draw, x, y, ex, ey, SCROLL_COLOR)
            _draw_label(draw, x + 10, y - 18, f"scroll {direction}", SCROLL_COLOR, LABEL_BG, font)

        elif kind == "drag":
            dx, dy = action.get("dest_x", x), action.get("dest_y", y)
            if x is not None and y is not None and dx is not None and dy is not None:
                # Line from source to destination
                draw.line([(x, y), (dx, dy)], fill=DRAG_COLOR, width=3)
                # Source circle
                draw.ellipse([(x - 6, y - 6), (x + 6, y + 6)], fill=DRAG_COLOR)
                # Arrowhead at destination
                _draw_arrowhead(draw, x, y, dx, dy, DRAG_COLOR)
                _draw_label(draw, x + 10, y - 10, "drag", DRAG_COLOR, LABEL_BG, font)

        elif kind == "hover" and x is not None and y is not None:
            draw.ellipse([(x - 8, y - 8), (x + 8, y + 8)], outline=HOVER_COLOR, width=2)
            _draw_label(draw, x + 10, y - 10, "hover", HOVER_COLOR, LABEL_BG, font)

        elif kind == "key":
            keys = action.get("keys", "")
            _draw_label(draw, 10, 10 + i * 22, f"key: {keys}", TYPE_COLOR, LABEL_BG, font)

    # Composite overlay onto original image
    result = Image.alpha_composite(img, overlay)
    result = result.convert("RGB")

    buf = BytesIO()
    result.save(buf, format="PNG")
    return buf.getvalue()


def _draw_label(draw, x, y, text, color, bg_color, font):
    """Draw a text label with a dark background at (x, y)."""
    bbox = draw.textbbox((x, y), text, font=font)
    pad = 3
    draw.rectangle(
        [bbox[0] - pad, bbox[1] - pad, bbox[2] + pad, bbox[3] + pad],
        fill=bg_color,
    )
    draw.text((x, y), text, fill=color, font=font)


def _draw_arrowhead(draw, x1, y1, x2, y2, color, size=10):
    """Draw a small arrowhead at (x2, y2) pointing away from (x1, y1)."""
    import math
    angle = math.atan2(y2 - y1, x2 - x1)
    a1 = angle + math.pi * 0.8
    a2 = angle - math.pi * 0.8
    points = [
        (x2, y2),
        (x2 + size * math.cos(a1), y2 + size * math.sin(a1)),
        (x2 + size * math.cos(a2), y2 + size * math.sin(a2)),
    ]
    draw.polygon(points, fill=color)


# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------


def _find_task_dir(run_dir: Path, task_id: str) -> Path | None:
    """Locate a task's result directory, supporting both flat and merged layouts."""
    # Flat layout: run_dir/<task_id>/
    candidate = run_dir / task_id
    if candidate.exists():
        return candidate
    # Merged layout: run_dir/success/<task_id>/ or run_dir/fail/<task_id>/
    for sub in ("success", "fail"):
        candidate = run_dir / sub / task_id
        if candidate.exists():
            return candidate
    return None


def _build_details_html(run_dir: Path, r: dict) -> str:
    """Parse history.json and build expandable step-by-step HTML."""
    task_dir = _find_task_dir(run_dir, r["task_id"])
    if task_dir is None:
        return ""
    history_file = task_dir / "history.json"
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
        # If coordinate data is present, draw action overlays on the screenshot
        ss_file = task_dir / "screenshots" / f"step_{i}.png"
        if ss_file.exists():
            image_bytes = ss_file.read_bytes()

            # Draw coordinate overlay if vision agent data is present
            coordinates = step.get("coordinates")
            if coordinates and isinstance(coordinates, list):
                image_bytes = _draw_action_overlay(image_bytes, coordinates)

            b64 = base64.b64encode(image_bytes).decode()
            parts.append(
                f"<br><img class='screenshot' src='data:image/png;base64,{b64}' "
                f"alt='Step {i + 1} screenshot'>"
            )

        parts.append("</div>")
        steps_html.append("".join(parts))

    return "\n".join(steps_html)
