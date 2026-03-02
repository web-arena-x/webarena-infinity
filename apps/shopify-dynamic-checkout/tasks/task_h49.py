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
    ride_colors = ride.get("settings", {}).get("colors", {})

    # After swap: Dawn should have Ride's original values, Ride should have Dawn's original
    # Dawn original: bg=#1A1A1A, text=#FFFFFF
    # Ride original: bg=#0F172A, text=#F8FAFC

    # Dawn should now have Ride's original values
    if dawn_colors.get("accentButtonBg", "").upper() != "#0F172A":
        return False, (
            f"Expected Dawn's button bg '#0F172A' (from Ride), "
            f"got '{dawn_colors.get('accentButtonBg')}'."
        )
    if dawn_colors.get("accentButtonText", "").upper() != "#F8FAFC":
        return False, (
            f"Expected Dawn's button text '#F8FAFC' (from Ride), "
            f"got '{dawn_colors.get('accentButtonText')}'."
        )

    # Ride should now have Dawn's original values
    if ride_colors.get("accentButtonBg", "").upper() != "#1A1A1A":
        return False, (
            f"Expected Ride's button bg '#1A1A1A' (from Dawn), "
            f"got '{ride_colors.get('accentButtonBg')}'."
        )
    if ride_colors.get("accentButtonText", "").upper() != "#FFFFFF":
        return False, (
            f"Expected Ride's button text '#FFFFFF' (from Dawn), "
            f"got '{ride_colors.get('accentButtonText')}'."
        )

    return True, (
        "Button colors swapped: Dawn now has #0F172A/#F8FAFC (from Ride), "
        "Ride now has #1A1A1A/#FFFFFF (from Dawn)."
    )
