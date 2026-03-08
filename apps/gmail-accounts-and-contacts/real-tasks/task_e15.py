# Task: Phone visibility to everyone.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    privacy = state.get("accountSettings", {}).get("privacySettings", {})
    show_phone = privacy.get("showPhone")

    if show_phone == "everyone":
        return True, "Phone visibility is now set to everyone."
    else:
        return False, f"showPhone is '{show_phone}', expected 'everyone'."
