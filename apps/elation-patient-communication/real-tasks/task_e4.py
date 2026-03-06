import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that patient messaging is turned off for the practice."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    practice_settings = state.get("practiceSettings", {})
    allow_messaging = practice_settings.get("allowPatientMessaging")

    if allow_messaging is not False:
        return False, f"practiceSettings.allowPatientMessaging is {allow_messaging}, expected False"

    return True, "Patient messaging for the practice is disabled"
