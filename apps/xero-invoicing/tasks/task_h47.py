import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Summit Health Group (con_014) is the only client with both a draft repeating invoice
    # (rep_005) and an overdue regular invoice (INV-0051, due 2026-03-01).
    # The task requires paying off INV-0051.
    inv = None
    for i in state.get("invoices", []):
        if i.get("number") == "INV-0051":
            inv = i
            break

    if inv is None:
        return False, "Invoice INV-0051 not found."

    status = inv.get("status", "")
    if status != "paid":
        return False, f"INV-0051 status is '{status}', expected 'paid'."

    amount_due = float(inv.get("amountDue", 9999))
    if amount_due > 1.00:
        return False, f"INV-0051 amountDue is ${amount_due:.2f}, expected ~$0."

    return True, (
        "INV-0051 (Summit Health Group, $6,060) fully paid. "
        "Summit Health is the client with both a draft repeating invoice and an overdue invoice."
    )
