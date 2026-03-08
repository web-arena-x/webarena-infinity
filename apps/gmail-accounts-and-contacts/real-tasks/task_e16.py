# Task: Sort by last name.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    sort_by = state.get("accountSettings", {}).get("contactsSortBy")

    if sort_by == "lastName":
        return True, "Contacts are now sorted by last name."
    else:
        return False, f"contactsSortBy is '{sort_by}', expected 'lastName'."
