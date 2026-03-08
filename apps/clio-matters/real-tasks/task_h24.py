import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find Rodriguez matter
    rodriguez = None
    for m in state.get("matters", []):
        desc = m.get("description") or ""
        if "Rodriguez" in desc and "Premier Auto" in desc:
            rodriguez = m
            break

    if not rodriguez:
        return False, "Rodriguez matter not found."

    # Find the provider that originally had billStatus 'Incomplete' (Advanced Imaging, con_020)
    target_provider = None
    for p in rodriguez.get("medicalProviders", []):
        if p.get("contactId") == "con_020":
            target_provider = p
            break

    if not target_provider:
        return False, "Advanced Imaging Associates provider (con_020) not found on Rodriguez case."

    errors = []

    # Check billStatus is now Received
    if target_provider.get("billStatus") != "Received":
        errors.append(
            f"Bill status is '{target_provider.get('billStatus')}', expected 'Received'"
        )

    # Check new bill exists
    bills = target_provider.get("medicalBills", [])
    final_bill = [b for b in bills if b.get("fileName") == "Final_Invoice.pdf"]
    if not final_bill:
        errors.append("Medical bill 'Final_Invoice.pdf' not found")
    else:
        amt = final_bill[0].get("billAmount", 0)
        if amt != 2800:
            errors.append(f"Final_Invoice.pdf bill amount is {amt}, expected 2800")

    if errors:
        return False, "; ".join(errors)

    return True, "Advanced Imaging bill status updated to Received and Final_Invoice.pdf added for $2,800."
