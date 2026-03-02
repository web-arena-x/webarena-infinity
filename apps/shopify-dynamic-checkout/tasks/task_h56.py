import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    themes = state.get("themes", [])

    dawn = next((t for t in themes if t.get("name") == "Dawn"), None)
    ride = next((t for t in themes if t.get("name") == "Ride"), None)
    if dawn is None:
        return False, "Theme 'Dawn' not found."
    if ride is None:
        return False, "Theme 'Ride' not found."

    dawn_colors = dawn.get("settings", {}).get("colors", {})
    dawn_typo = dawn.get("settings", {}).get("typography", {})

    # Ride's original primaryBg=#F8FAFC, secondaryBg=#E2E8F0
    ride_colors = ride.get("settings", {}).get("colors", {})

    if dawn_colors.get("primaryBg", "").upper() != ride_colors.get("primaryBg", "").upper():
        return False, (
            f"Expected Dawn primaryBg to match Ride's ('{ride_colors.get('primaryBg')}'), "
            f"got '{dawn_colors.get('primaryBg')}'."
        )

    if dawn_colors.get("secondaryBg", "").upper() != ride_colors.get("secondaryBg", "").upper():
        return False, (
            f"Expected Dawn secondaryBg to match Ride's ('{ride_colors.get('secondaryBg')}'), "
            f"got '{dawn_colors.get('secondaryBg')}'."
        )

    if dawn_typo.get("headingFont") != "Inter":
        return False, (
            f"Expected Dawn heading font 'Inter', got '{dawn_typo.get('headingFont')}'."
        )

    if dawn_typo.get("bodyFont") != "Inter":
        return False, (
            f"Expected Dawn body font 'Inter', got '{dawn_typo.get('bodyFont')}'."
        )

    return True, (
        f"Dawn's primaryBg and secondaryBg match Ride's. "
        f"Dawn's heading and body fonts set to Inter."
    )
