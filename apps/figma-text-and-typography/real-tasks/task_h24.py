import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Duplicate Call to Action, rename to 'Secondary CTA', font DM Sans Regular, remove uppercase."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    # Original Call to Action should still exist
    original = next((l for l in text_layers if l.get("name") == "Call to Action"), None)
    if not original:
        errors.append("Original 'Call to Action' layer not found (should not have been deleted).")

    # Find the duplicate by name
    dup = next((l for l in text_layers if l.get("name") == "Secondary CTA"), None)
    if not dup:
        return False, "Layer 'Secondary CTA' not found. " + "; ".join(errors) if errors else "Layer 'Secondary CTA' not found."

    # Verify duplicate has correct content (same as original)
    if dup.get("content") != "Get Started for Free":
        errors.append(f"Secondary CTA content: expected 'Get Started for Free', got '{dup.get('content')}'")

    if dup.get("fontFamily") != "DM Sans":
        errors.append(f"Secondary CTA fontFamily: expected 'DM Sans', got '{dup.get('fontFamily')}'")

    if dup.get("fontStyle") != "Regular":
        errors.append(f"Secondary CTA fontStyle: expected 'Regular', got '{dup.get('fontStyle')}'")

    if dup.get("letterCase") != "none":
        errors.append(f"Secondary CTA letterCase: expected 'none', got '{dup.get('letterCase')}'")

    # Verify it's a different layer from the original
    if original and dup.get("id") == original.get("id"):
        errors.append("Secondary CTA has the same ID as the original Call to Action.")

    if errors:
        return False, "; ".join(errors)
    return True, "Call to Action duplicated as 'Secondary CTA' with DM Sans Regular and no uppercase."
