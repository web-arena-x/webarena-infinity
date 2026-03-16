import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Duplicate Page Title as 'Page Subtitle' with Lato Regular 20px, 28px line height, no style, 0.01em spacing."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    # Original Page Title should still exist
    original = next((l for l in text_layers if l.get("id") == "tl_001"), None)
    if not original:
        return False, "Original Page Title layer (tl_001) not found."

    # Find the duplicate by name
    dup = next((l for l in text_layers if l.get("name") == "Page Subtitle" and l.get("id") != "tl_001"), None)
    if not dup:
        return False, "No layer named 'Page Subtitle' found."

    # Content should match original
    if dup.get("content") != original.get("content"):
        errors.append("Page Subtitle content doesn't match Page Title content.")

    if dup.get("fontFamily") != "Lato":
        errors.append(f"Expected fontFamily 'Lato', got '{dup.get('fontFamily')}'.")
    if dup.get("fontStyle") != "Regular":
        errors.append(f"Expected fontStyle 'Regular', got '{dup.get('fontStyle')}'.")
    if dup.get("fontSize") != 20:
        errors.append(f"Expected fontSize 20, got {dup.get('fontSize')}.")

    lh = dup.get("lineHeight", {})
    if lh.get("value") != 28 or lh.get("unit") != "px":
        errors.append(f"Expected lineHeight 28px, got {lh}.")

    if dup.get("textStyleId") is not None:
        errors.append(f"Expected textStyleId null (detached), got '{dup.get('textStyleId')}'.")

    ls = dup.get("letterSpacing", {})
    if ls.get("value") != 0.01 or ls.get("unit") != "em":
        errors.append(f"Expected letterSpacing 0.01em, got {ls}.")

    if errors:
        return False, "; ".join(errors)
    return True, "Page Subtitle duplicated from Page Title with correct Lato Regular 20px properties."
