import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Duplicate the longest-content layer, rename to 'Content Summary', enable truncation (3 lines)."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    # The longest content layer is Body Text (tl_002)
    original = next((l for l in text_layers if l.get("id") == "tl_002"), None)
    if not original:
        return False, "Original Body Text layer (tl_002) not found."

    # Find the duplicate by name
    dupes = [l for l in text_layers if l.get("name") == "Content Summary" and l.get("id") != "tl_002"]
    if not dupes:
        return False, "No layer named 'Content Summary' found."

    dup = dupes[0]

    # Content should match original
    if dup.get("content") != original.get("content"):
        errors.append(f"Duplicate content does not match original Body Text content.")

    # Truncation should be enabled with 3 lines
    trunc = dup.get("truncation", {})
    if not trunc.get("enabled"):
        errors.append("Truncation is not enabled on the duplicate.")
    if trunc.get("maxLines") != 3:
        errors.append(f"Expected maxLines=3, got {trunc.get('maxLines')}.")

    if errors:
        return False, "; ".join(errors)
    return True, "Content Summary layer created with truncation (3 lines) from longest content layer."
