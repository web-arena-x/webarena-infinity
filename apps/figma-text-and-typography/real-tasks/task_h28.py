import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Find layer with smallest font size, duplicate it, set duplicate's size to 24."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    # Copyright Notice (tl_007) has the smallest font size in seed data: 12px
    original = next((l for l in text_layers if l.get("id") == "tl_007"), None)
    if not original:
        return False, "Original Copyright Notice layer (tl_007) not found."

    # Original should be unchanged
    if original.get("fontSize") != 12:
        errors.append(f"Original Copyright Notice fontSize changed: expected 12, got {original.get('fontSize')}")

    # Find the duplicate: a different layer with the same content and fontSize=24
    original_content = original.get("content", "")
    duplicates = [
        l for l in text_layers
        if l.get("id") != "tl_007"
        and l.get("content") == original_content
        and l.get("fontSize") == 24
    ]

    if not duplicates:
        errors.append("No duplicate of Copyright Notice found with fontSize=24.")

    if errors:
        return False, "; ".join(errors)
    return True, "Copyright Notice (smallest font) duplicated with font size set to 24."
