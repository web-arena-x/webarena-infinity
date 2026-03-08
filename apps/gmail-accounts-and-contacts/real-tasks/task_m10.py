# Task: Merge EuroDesign duplicate contacts.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    # Check merge_2 is dismissed
    merge_suggestions = state.get("mergeSuggestions", [])
    merge_2 = next((m for m in merge_suggestions if m.get("id") == "merge_2"), None)
    if merge_2 is None:
        errors.append("Merge suggestion 'merge_2' not found")
    elif merge_2.get("dismissed") is not True:
        errors.append(f"Expected merge_2.dismissed to be true, got {merge_2.get('dismissed')}")

    # Check Elena Volkov (contact_37) no longer exists
    contacts = state.get("contacts", [])
    elena = next((c for c in contacts if c.get("id") == "contact_37"), None)
    if elena is not None:
        errors.append("Contact contact_37 (Elena Volkov) should have been removed after merge but still exists")

    # Check Sophie Laurent (contact_15) still exists
    sophie = next((c for c in contacts if c.get("id") == "contact_15"), None)
    if sophie is None:
        errors.append("Contact contact_15 (Sophie Laurent) should still exist after merge but was not found")

    if errors:
        return False, "; ".join(errors)
    return True, "EuroDesign duplicate contacts merged: merge_2 dismissed, Elena Volkov removed, Sophie Laurent retained."
