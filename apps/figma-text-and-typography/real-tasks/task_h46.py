import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Delete the unused style with the second-largest font size."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    text_styles = state.get("textStyles", [])
    errors = []

    # The second-largest unused style is Heading/H3 (24px, ts_004)
    # Unused styles by size: Display(64), H3(24), Body/Large(18), Body/Small(13), Overline(11)
    h3_exists = any(s.get("name") == "Heading/H3" for s in text_styles)
    if h3_exists:
        errors.append("Heading/H3 style should have been deleted (second-largest unused style at 24px).")

    # Make sure used styles are still present
    used_style_names = {"Heading/H1", "Body/Regular", "Heading/H2", "Button/Primary",
                        "Caption/Small", "Code/Inline", "Label/SmallCaps"}
    for name in used_style_names:
        if not any(s.get("name") == name for s in text_styles):
            errors.append(f"Used style '{name}' should not have been deleted.")

    if errors:
        return False, "; ".join(errors)
    return True, "Heading/H3 (second-largest unused style) deleted correctly."
