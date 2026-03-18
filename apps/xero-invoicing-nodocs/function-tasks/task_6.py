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

    con = next((c for c in state["contacts"] if c["name"] == "Bright Spark Electrical"), None)
    if not con:
        return False, "Contact 'Bright Spark Electrical' not found."
    if inv["contactId"] != con["id"]:
        return False, "Wrong contact."
    if inv["status"] != "awaiting_payment":
        return False, f"Expected status 'awaiting_payment', got '{inv['status']}'"
    li = next((l for l in inv["lineItems"] if l["description"] == "Electrical inspection"), None)
    if not li:
        return False, "Line item 'Electrical inspection' not found."
    return True, "Approved invoice for Bright Spark Electrical created correctly."
