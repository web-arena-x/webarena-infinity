import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    practice_settings = state.get("practiceSettings", {})
    allow_messaging = practice_settings.get("allowPatientMessaging")

    if allow_messaging is False:
        return True, "Patient messaging has been disabled."
    else:
        return False, f"allowPatientMessaging is {allow_messaging}, expected False."
