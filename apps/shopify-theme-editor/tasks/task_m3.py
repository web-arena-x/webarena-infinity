import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify heading font is 'Montserrat' and heading font size scale is 130."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    typo = state.get("themeSettings", {}).get("typography", {})

    font = typo.get("headingFont")
    if font != "Montserrat":
        return False, f"Expected headingFont 'Montserrat', got '{font}'."

    scale = typo.get("headingFontSizeScale")
    if scale != 130:
        return False, f"Expected headingFontSizeScale=130, got {scale}."

    return True, "Heading font is 'Montserrat' at 130% scale."
