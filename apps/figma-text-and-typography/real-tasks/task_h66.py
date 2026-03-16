import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Feature List duplicated as 'Benefits List' with Poppins Medium and numbered list."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    # Original should still exist
    original = next((l for l in text_layers if l.get("name") == "Feature List"), None)
    if not original:
        return False, "Original Feature List layer not found."

    # Find the duplicate
    dup = next((l for l in text_layers if l.get("name") == "Benefits List"), None)
    if not dup:
        return False, "Benefits List layer not found."

    # Content should match original
    if dup.get("content") != original.get("content"):
        errors.append("Benefits List content doesn't match Feature List content.")

    if dup.get("fontFamily") != "Poppins":
        errors.append(f"Expected fontFamily 'Poppins', got '{dup.get('fontFamily')}'.")
    if dup.get("fontStyle") != "Medium":
        errors.append(f"Expected fontStyle 'Medium', got '{dup.get('fontStyle')}'.")
    if dup.get("listStyle") != "numbered":
        errors.append(f"Expected listStyle 'numbered', got '{dup.get('listStyle')}'.")

    if errors:
        return False, "; ".join(errors)
    return True, "Feature List duplicated as Benefits List with Poppins Medium numbered list."
