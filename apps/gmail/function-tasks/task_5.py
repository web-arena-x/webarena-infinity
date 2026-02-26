import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    email = next(
        (e for e in state["emails"] if e["subject"] == "Office Renovation Plans"),
        None,
    )
    if not email:
        return False, "Email 'Office Renovation Plans' not found."

    if not email["isImportant"]:
        return False, "Email 'Office Renovation Plans' is not marked as important."

    if "IMPORTANT" not in email["labels"]:
        return False, "Email 'Office Renovation Plans' does not have the IMPORTANT label."

    return True, "Email 'Office Renovation Plans' is marked as important."
