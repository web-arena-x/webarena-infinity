# Task: Unlink Google Maps and Chrome.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    linked_services = state.get("linkedServices", [])

    google_maps = next((s for s in linked_services if s.get("name") == "Google Maps"), None)
    if google_maps is None:
        errors.append("Linked service 'Google Maps' not found")
    elif google_maps.get("isLinked") is not False:
        errors.append(f"Expected Google Maps isLinked to be false, got {google_maps.get('isLinked')}")

    chrome = next((s for s in linked_services if s.get("name") == "Chrome"), None)
    if chrome is None:
        errors.append("Linked service 'Chrome' not found")
    elif chrome.get("isLinked") is not False:
        errors.append(f"Expected Chrome isLinked to be false, got {chrome.get('isLinked')}")

    if errors:
        return False, "; ".join(errors)
    return True, "Google Maps and Chrome unlinked successfully."
