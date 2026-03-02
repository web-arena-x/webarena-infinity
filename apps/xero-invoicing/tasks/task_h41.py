import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # INV-0055 (TechVault Solutions, $41,800) has the largest outstanding balance
    inv = None
    for i in state.get("invoices", []):
        if i.get("number") == "INV-0055":
            inv = i
            break

    if inv is None:
        return False, "Invoice INV-0055 not found."

    status = inv.get("status", "")
    if status != "paid":
        return False, f"INV-0055 status is '{status}', expected 'paid'."

    amount_due = float(inv.get("amountDue", 9999))
    if amount_due > 1.00:
        return False, f"INV-0055 amountDue is ${amount_due:.2f}, expected ~$0."

    return True, (
        "Invoice INV-0055 (TechVault Solutions, $41,800 — largest outstanding balance) fully paid."
    )
