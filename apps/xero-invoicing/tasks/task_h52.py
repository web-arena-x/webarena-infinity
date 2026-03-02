import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # INV-0056 (Horizon Media) and INV-0057 (Stellar Education) were awaiting approval.
    # Both should now be approved (awaiting_payment) and sent.
    expected = {
        "INV-0056": "Horizon Media & Advertising",
        "INV-0057": "Stellar Education Services",
    }

    for inv_num, contact_name in expected.items():
        inv = None
        for i in state.get("invoices", []):
            if i.get("number") == inv_num:
                inv = i
                break

        if inv is None:
            return False, f"Invoice {inv_num} not found."

        if inv.get("status") != "awaiting_payment":
            return False, (
                f"{inv_num} ({contact_name}) status is '{inv.get('status')}', "
                f"expected 'awaiting_payment' (approved)."
            )

        if not inv.get("sentAt"):
            return False, (
                f"{inv_num} ({contact_name}) has not been sent (sentAt is empty)."
            )

    return True, (
        "Both awaiting-approval invoices (INV-0056, INV-0057) approved and sent."
    )
