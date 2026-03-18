import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    inv = next((i for i in state["invoices"] if i["invoiceNumber"] == "INV-0033"), None)
    if not inv:
        return False, "Invoice INV-0033 not found."
    con = next((c for c in state["contacts"] if c["id"] == inv["contactId"]), None)
    if not con:
        return False, "Contact for INV-0033 not found."
    if con["phone"] != "+64 9 307 3300":
        return False, f"Expected phone '+64 9 307 3300', got '{con['phone']}'"
    return True, "Phone updated for contact associated with INV-0033."
