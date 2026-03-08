import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find Foster matter
    foster = None
    for m in state.get("matters", []):
        if "Foster" in (m.get("description") or ""):
            foster = m
            break

    if not foster:
        return False, "Foster slip-and-fall matter not found."

    settlement = foster.get("settlement", {})
    errors = []

    # Check recovery from State Farm (con_023) for $100,000
    recoveries = settlement.get("recoveries", [])
    sf_rec = None
    for r in recoveries:
        if r.get("sourceContactId") == "con_023":
            sf_rec = r
            break

    if not sf_rec:
        errors.append("No recovery from State Farm Insurance (con_023) found")
    else:
        if sf_rec.get("amount") != 100000:
            errors.append(
                f"State Farm recovery amount is {sf_rec.get('amount')}, expected 100000"
            )

    # Check legal fee for that recovery
    if sf_rec:
        legal_fees = settlement.get("legalFees", [])
        sf_lf = None
        for lf in legal_fees:
            if lf.get("recoveryId") == sf_rec.get("id"):
                sf_lf = lf
                break

        if not sf_lf:
            errors.append("No legal fee entry found for the State Farm recovery")
        else:
            # Michael Osei is usr_006
            if sf_lf.get("recipientId") != "usr_006":
                errors.append(
                    f"Legal fee recipient is '{sf_lf.get('recipientId')}', "
                    f"expected 'usr_006' (Michael Osei)"
                )
            if sf_lf.get("rate") != 40:
                errors.append(
                    f"Legal fee rate is {sf_lf.get('rate')}%, expected 40%"
                )
            if sf_lf.get("discount") != 10:
                errors.append(
                    f"Legal fee discount is {sf_lf.get('discount')}%, expected 10%"
                )

    if errors:
        return False, "; ".join(errors)

    return True, "State Farm recovery ($100k) and legal fee (Osei, 40%, 10% discount) added to Foster case."
