# Task: Unlink YouTube.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    services = state.get("linkedServices", [])
    for svc in services:
        if svc.get("name") == "YouTube":
            if svc.get("isLinked") is False:
                return True, "YouTube is now unlinked."
            else:
                return False, f"YouTube isLinked is {svc.get('isLinked')}, expected false."

    return False, "Linked service 'YouTube' not found in state."
