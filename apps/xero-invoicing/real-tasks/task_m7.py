import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    invoices = state.get("invoices", [])
    inv = None
    for i in invoices:
        if i.get("number") == "INV-0058":
            inv = i
            break

    if inv is None:
        return False, "Invoice INV-0058 not found."

    reference = inv.get("reference", "")
    if reference != "MRW-MARCH-2026":
        return False, f"Invoice INV-0058 reference is '{reference}', expected 'MRW-MARCH-2026'."

    return True, "Invoice INV-0058 reference updated to 'MRW-MARCH-2026'."
