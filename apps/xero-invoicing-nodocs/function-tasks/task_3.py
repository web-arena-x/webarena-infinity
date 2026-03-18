import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    original_ids = {f"inv_{i}" for i in range(1, 114)}
    new_invs = [i for i in state["invoices"] if i["id"] not in original_ids]
    if not new_invs:
        return False, "No new invoice found."
    inv = new_invs[0]

    con = next((c for c in state["contacts"] if c["name"] == "Coastal Cafe Group"), None)
    if not con:
        return False, "Contact 'Coastal Cafe Group' not found."
    if inv["contactId"] != con["id"]:
        return False, "Wrong contact."
    if inv["reference"] != "PO-CAFE-2026":
        return False, f"Expected reference 'PO-CAFE-2026', got '{inv['reference']}'"
    if inv["notes"] != "Payment due within 14 days.":
        return False, f"Wrong notes: '{inv['notes']}'"
    return True, "Draft invoice for Coastal Cafe Group created with correct reference and notes."
