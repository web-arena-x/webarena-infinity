import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Underline every text layer whose content mentions 'Figma'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    # In seed data, layers with 'Figma' in content:
    # Body Text, Feature List, Copyright Notice, Truncated Preview, Step Instructions
    expected_underlined = {"Body Text", "Feature List", "Copyright Notice", "Truncated Preview", "Step Instructions"}

    for layer in text_layers:
        name = layer.get("name")
        if name in expected_underlined:
            if layer.get("textDecoration") != "underline":
                errors.append(f"{name}: expected textDecoration='underline', got '{layer.get('textDecoration')}'")

    if len(errors) == 0:
        # Also verify we found enough layers
        found = sum(1 for l in text_layers if l.get("name") in expected_underlined)
        if found < 5:
            errors.append(f"Expected 5 layers with 'Figma' in content, found {found}")

    if errors:
        return False, "; ".join(errors)
    return True, "All 5 layers containing 'Figma' are underlined."
