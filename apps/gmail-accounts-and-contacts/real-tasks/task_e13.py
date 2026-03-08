# Task: Link Google Ads.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    services = state.get("linkedServices", [])
    for svc in services:
        if svc.get("name") == "Google Ads":
            if svc.get("isLinked") is True:
                return True, "Google Ads is now linked."
            else:
                return False, f"Google Ads isLinked is {svc.get('isLinked')}, expected true."

    return False, "Linked service 'Google Ads' not found in state."
