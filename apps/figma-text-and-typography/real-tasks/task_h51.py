import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Delete Heading/H1 style and apply Heading/H3 to layers that were using it."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    text_styles = state.get("textStyles", [])
    errors = []

    # Heading/H1 should be deleted
    if any(s.get("name") == "Heading/H1" for s in text_styles):
        errors.append("Heading/H1 style should have been deleted.")

    # Heading/H3 should still exist
    h3 = next((s for s in text_styles if s.get("name") == "Heading/H3"), None)
    if not h3:
        return False, "Heading/H3 style not found."

    # Page Title (was using H1) should now have H3 applied
    page_title = next((l for l in text_layers if l.get("name") == "Page Title"), None)
    if not page_title:
        return False, "Page Title layer not found."

    if page_title.get("textStyleId") != h3["id"]:
        errors.append(f"Page Title: expected textStyleId '{h3['id']}', got '{page_title.get('textStyleId')}'.")

    if page_title.get("fontFamily") != h3["fontFamily"]:
        errors.append(f"Page Title: expected fontFamily '{h3['fontFamily']}', got '{page_title.get('fontFamily')}'.")

    if page_title.get("fontStyle") != h3["fontStyle"]:
        errors.append(f"Page Title: expected fontStyle '{h3['fontStyle']}', got '{page_title.get('fontStyle')}'.")

    if page_title.get("fontSize") != h3["fontSize"]:
        errors.append(f"Page Title: expected fontSize {h3['fontSize']}, got {page_title.get('fontSize')}.")

    if errors:
        return False, "; ".join(errors)
    return True, "Heading/H1 deleted and Heading/H3 applied to Page Title."
