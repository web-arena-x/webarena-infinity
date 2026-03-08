import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Swap list formats: bulleted→numbered and numbered→bulleted."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    # Feature List was bulleted, should now be numbered
    fl = next((l for l in text_layers if l.get("name") == "Feature List"), None)
    if not fl:
        errors.append("Feature List layer not found.")
    elif fl.get("listStyle") != "numbered":
        errors.append(f"Feature List: expected 'numbered', got '{fl.get('listStyle')}'")

    # Pricing Tiers was numbered, should now be bulleted
    pt = next((l for l in text_layers if l.get("name") == "Pricing Tiers"), None)
    if not pt:
        errors.append("Pricing Tiers layer not found.")
    elif pt.get("listStyle") != "bulleted":
        errors.append(f"Pricing Tiers: expected 'bulleted', got '{pt.get('listStyle')}'")

    # Step Instructions was numbered, should now be bulleted
    si = next((l for l in text_layers if l.get("name") == "Step Instructions"), None)
    if not si:
        errors.append("Step Instructions layer not found.")
    elif si.get("listStyle") != "bulleted":
        errors.append(f"Step Instructions: expected 'bulleted', got '{si.get('listStyle')}'")

    if errors:
        return False, "; ".join(errors)
    return True, "All list formats swapped correctly (bulleted↔numbered)."
