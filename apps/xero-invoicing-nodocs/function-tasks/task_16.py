import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    inv = next((i for i in state["invoices"] if i["invoiceNumber"] == "INV-0054"), None)
    if not inv:
        return False, "Invoice INV-0054 not found."
    con = next((c for c in state["contacts"] if c["name"] == "Green Valley Organics"), None)
    if not con:
        return False, "Contact 'Green Valley Organics' not found."
    if inv["contactId"] != con["id"]:
        return False, f"Expected contactId {con['id']}, got {inv['contactId']}"
    return True, "Invoice INV-0054 contact changed to Green Valley Organics."
