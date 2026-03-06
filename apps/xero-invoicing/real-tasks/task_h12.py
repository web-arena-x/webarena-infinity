import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    invoices = state.get("invoices", [])

    # Check INV-0058, INV-0059, INV-0060 are all voided
    draft_numbers = ["INV-0058", "INV-0059", "INV-0060"]
    for num in draft_numbers:
        inv = next((i for i in invoices if i.get("number") == num), None)
        if inv is None:
            return False, f"Invoice {num} not found."
        if inv.get("status") != "voided":
            return False, f"Expected {num} status 'voided', got '{inv.get('status')}'."

    # Also check no invoice has status 'draft'
    drafts = [i.get("number") for i in invoices if i.get("status") == "draft"]
    if drafts:
        return False, f"Found invoices still in draft status: {', '.join(drafts)}."

    return True, "All draft invoices (INV-0058, INV-0059, INV-0060) have been voided."
