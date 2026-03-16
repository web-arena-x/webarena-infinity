"""
Task: Create a text style called 'Body/Compact' with Inter Regular at 13px and a line height of 16px.
Verify: A style named 'Body/Compact' exists with fontFamily='Inter', fontStyle='Regular',
        fontSize=13, lineHeight.value=16, lineHeight.unit='px'.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    text_styles = state.get("textStyles", [])
    if not text_styles:
        return False, "No text styles found in state."

    target = None
    for style in text_styles:
        if style.get("name") == "Body/Compact":
            target = style
            break

    if target is None:
        style_names = [s.get("name", "unnamed") for s in text_styles]
        return False, f"No style named 'Body/Compact' found. Existing styles: {', '.join(style_names)}"

    errors = []

    if target.get("fontFamily") != "Inter":
        errors.append(f"fontFamily is '{target.get('fontFamily')}', expected 'Inter'")

    if target.get("fontStyle") != "Regular":
        errors.append(f"fontStyle is '{target.get('fontStyle')}', expected 'Regular'")

    if target.get("fontSize") != 13:
        errors.append(f"fontSize is {target.get('fontSize')}, expected 13")

    line_height = target.get("lineHeight", {})
    if line_height.get("value") != 16:
        errors.append(f"lineHeight.value is {line_height.get('value')}, expected 16")
    if line_height.get("unit") != "px":
        errors.append(f"lineHeight.unit is '{line_height.get('unit')}', expected 'px'")

    if errors:
        return False, f"Style 'Body/Compact' found but has issues: {'; '.join(errors)}"

    return True, "Style 'Body/Compact' exists with correct properties (Inter Regular 13px, line height 16px)."
