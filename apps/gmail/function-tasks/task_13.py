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

    # label_1 is the "Work" label
    work_label = next((l for l in state["labels"] if l["name"] == "Work"), None)
    if not work_label:
        return False, "Work label not found in state."

    if work_label["id"] in email["labels"]:
        return False, "Email 'Office Renovation Plans' still has the 'Work' label."

    return True, "Work label removed from email 'Office Renovation Plans'."
