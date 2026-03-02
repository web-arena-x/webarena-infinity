import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # CloudNine Analytics (con_007) has two invoices:
    #   INV-0047 (due 2026-02-15) — due first
    #   INV-0062 (due 2026-03-06) — due later
    inv = None
    for i in state.get("invoices", []):
        if i.get("number") == "INV-0047":
            inv = i
            break

    if inv is None:
        return False, "Invoice INV-0047 not found."

    status = inv.get("status", "")
    if status != "paid":
        return False, f"INV-0047 status is '{status}', expected 'paid'."

    amount_due = float(inv.get("amountDue", 9999))
    if amount_due > 1.00:
        return False, f"INV-0047 amountDue is ${amount_due:.2f}, expected ~$0."

    return True, (
        "CloudNine Analytics invoice INV-0047 (due 2026-02-15, the earlier due date) fully paid."
    )
