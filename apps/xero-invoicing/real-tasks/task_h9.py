import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    invoices = state.get("invoices", [])

    # Check INV-0048 (Pacific Freight, $4,180)
    inv_048 = next((inv for inv in invoices if inv.get("number") == "INV-0048"), None)
    if inv_048 is None:
        return False, "Invoice INV-0048 not found."

    if inv_048.get("status") != "paid":
        return False, f"Expected INV-0048 status 'paid', got '{inv_048.get('status')}'."

    if abs(inv_048.get("amountDue", 9999)) > 0.01:
        return False, f"Expected INV-0048 amountDue=0, got {inv_048.get('amountDue')}."

    # Check INV-0054 (Sapphire Bay Resort, $2,178)
    inv_054 = next((inv for inv in invoices if inv.get("number") == "INV-0054"), None)
    if inv_054 is None:
        return False, "Invoice INV-0054 not found."

    if inv_054.get("status") != "paid":
        return False, f"Expected INV-0054 status 'paid', got '{inv_054.get('status')}'."

    if abs(inv_054.get("amountDue", 9999)) > 0.01:
        return False, f"Expected INV-0054 amountDue=0, got {inv_054.get('amountDue')}."

    return True, "Both INV-0048 (Pacific Freight) and INV-0054 (Sapphire Bay Resort) fully paid."
