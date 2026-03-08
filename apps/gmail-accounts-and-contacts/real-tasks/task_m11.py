# Task: Sort by last name and display order last name first.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    settings = state.get("accountSettings", {})
    sort_by = settings.get("contactsSortBy")
    if sort_by != "lastName":
        errors.append(f"Expected contactsSortBy to be 'lastName', got '{sort_by}'")

    display_order = settings.get("contactsDisplayOrder")
    if display_order != "lastFirst":
        errors.append(f"Expected contactsDisplayOrder to be 'lastFirst', got '{display_order}'")

    if errors:
        return False, "; ".join(errors)
    return True, "Contacts sort set to last name and display order set to last name first."
