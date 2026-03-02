import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    practice_settings = state.get("practiceSettings", {})
    auto_invite = practice_settings.get("bookingSiteAutoInvite")

    if auto_invite is False:
        return True, "Booking site auto-invite has been disabled."
    else:
        return False, f"bookingSiteAutoInvite is {auto_invite}, expected False."
