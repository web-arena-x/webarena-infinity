import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the auto-invite to Passport after online booking is disabled."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    practice_settings = state.get("practiceSettings", {})
    auto_invite = practice_settings.get("bookingSiteAutoInvite")

    if auto_invite is not False:
        return False, f"practiceSettings.bookingSiteAutoInvite is {auto_invite}, expected False"

    return True, "Auto-invite to Passport after online booking is disabled"
