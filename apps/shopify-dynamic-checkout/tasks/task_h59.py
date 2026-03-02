import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    themes = state.get("themes", [])

    dawn = next((t for t in themes if t.get("name") == "Dawn"), None)
    taste = next((t for t in themes if t.get("name") == "Taste"), None)
    if dawn is None:
        return False, "Theme 'Dawn' not found."
    if taste is None:
        return False, "Theme 'Taste' not found."

    dawn_colors = dawn.get("settings", {}).get("colors", {})
    taste_colors = taste.get("settings", {}).get("colors", {})

    # Check Dawn secondary colors
    if dawn_colors.get("secondaryBg", "").upper() != "#E8E8E8":
        return False, (
            f"Expected Dawn secondaryBg '#E8E8E8', "
            f"got '{dawn_colors.get('secondaryBg')}'."
        )
    if dawn_colors.get("secondaryText", "").upper() != "#444444":
        return False, (
            f"Expected Dawn secondaryText '#444444', "
            f"got '{dawn_colors.get('secondaryText')}'."
        )

    # Check Taste is published
    if taste.get("role") != "main":
        return False, f"Expected Taste published, got role='{taste.get('role')}'."

    # Check Dawn is no longer main
    if dawn.get("role") == "main":
        return False, "Dawn should no longer be published."

    # Check Taste has same secondary colors
    if taste_colors.get("secondaryBg", "").upper() != "#E8E8E8":
        return False, (
            f"Expected Taste secondaryBg '#E8E8E8', "
            f"got '{taste_colors.get('secondaryBg')}'."
        )
    if taste_colors.get("secondaryText", "").upper() != "#444444":
        return False, (
            f"Expected Taste secondaryText '#444444', "
            f"got '{taste_colors.get('secondaryText')}'."
        )

    return True, (
        "Dawn secondary colors set to #E8E8E8/#444444. "
        "Taste published with same secondary colors applied."
    )
