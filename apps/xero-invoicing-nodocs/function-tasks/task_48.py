import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    inv83 = next((i for i in state["invoices"] if i["invoiceNumber"] == "INV-0083"), None)
    if inv83:
        return False, "Invoice INV-0083 still exists."
    inv108 = next((i for i in state["invoices"] if i["invoiceNumber"] == "INV-0108"), None)
    if inv108:
        return False, "Invoice INV-0108 still exists."
    if len(state["invoices"]) != 111:
        return False, f"Expected 111 invoices, got {len(state['invoices'])}"
    return True, "Invoices INV-0083 and INV-0108 bulk deleted successfully."
