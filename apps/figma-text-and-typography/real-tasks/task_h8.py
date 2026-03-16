"""
Task: Create a new text layer saying 'Subscribe to our newsletter', set it to Poppins Bold
      at 16px, center-aligned, and uppercase.
Verify: A layer exists with content='Subscribe to our newsletter', fontFamily='Poppins',
        fontStyle='Bold', fontSize=16, horizontalAlign='center', letterCase='uppercase'.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    text_layers = state.get("textLayers", [])
    if not text_layers:
        return False, "No text layers found in state."

    # Find layer with matching content
    target = None
    for layer in text_layers:
        if layer.get("content") == "Subscribe to our newsletter":
            target = layer
            break

    if target is None:
        return False, "No layer with content 'Subscribe to our newsletter' found."

    errors = []

    if target.get("fontFamily") != "Poppins":
        errors.append(f"fontFamily is '{target.get('fontFamily')}', expected 'Poppins'")

    if target.get("fontStyle") != "Bold":
        errors.append(f"fontStyle is '{target.get('fontStyle')}', expected 'Bold'")

    if target.get("fontSize") != 16:
        errors.append(f"fontSize is {target.get('fontSize')}, expected 16")

    if target.get("horizontalAlign") != "center":
        errors.append(f"horizontalAlign is '{target.get('horizontalAlign')}', expected 'center'")

    if target.get("letterCase") != "uppercase":
        errors.append(f"letterCase is '{target.get('letterCase')}', expected 'uppercase'")

    if errors:
        return False, f"Layer found but has issues: {'; '.join(errors)}"

    return True, "Layer 'Subscribe to our newsletter' exists with Poppins Bold 16px, center-aligned, uppercase."
