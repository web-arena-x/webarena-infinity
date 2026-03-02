import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    themes = state.get("themes", [])
    templates = state.get("templates", [])

    sense = next((t for t in themes if t.get("name") == "Sense"), None)
    dawn = next((t for t in themes if t.get("name") == "Dawn"), None)
    if sense is None:
        return False, "Theme 'Sense' not found."
    if dawn is None:
        return False, "Theme 'Dawn' not found."

    # Check Sense is published
    if sense.get("role") != "main":
        return False, f"Expected Sense published, got role='{sense.get('role')}'."

    # Check Dawn is no longer main
    if dawn.get("role") == "main":
        return False, "Dawn should no longer be published."

    # Check Sense has Dawn's original button colors (#1A1A1A bg, #FFFFFF text)
    sense_colors = sense.get("settings", {}).get("colors", {})
    if sense_colors.get("accentButtonBg", "").upper() != "#1A1A1A":
        return False, (
            f"Expected Sense button bg '#1A1A1A' (from Dawn), "
            f"got '{sense_colors.get('accentButtonBg')}'."
        )
    if sense_colors.get("accentButtonText", "").upper() != "#FFFFFF":
        return False, (
            f"Expected Sense button text '#FFFFFF' (from Dawn), "
            f"got '{sense_colors.get('accentButtonText')}'."
        )

    # Check Sense heading font is Montserrat
    sense_typo = sense.get("settings", {}).get("typography", {})
    if sense_typo.get("headingFont") != "Montserrat":
        return False, (
            f"Expected Sense heading font 'Montserrat', "
            f"got '{sense_typo.get('headingFont')}'."
        )

    # Check Sense default template has checkout enabled
    sense_default = next(
        (t for t in templates if t.get("themeId") == sense["id"] and t.get("isDefault") is True),
        None
    )
    if sense_default is None:
        return False, "Sense default template not found."
    if sense_default.get("showAcceleratedCheckout") is not True:
        return False, (
            f"Expected Sense default template checkout enabled, "
            f"got {sense_default.get('showAcceleratedCheckout')}."
        )

    return True, (
        "Sense published with Dawn's button colors (#1A1A1A/#FFFFFF), "
        "heading font Montserrat, checkout enabled on default template."
    )
