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

    errors = []

    # Check each medical bill across all providers
    # Bills that originally had payers: mb_001 (NM Hospital) and mb_002 (Chicago PT)
    for p in rodriguez.get("medicalProviders", []):
        for b in p.get("medicalBills", []):
            bill_name = b.get("fileName", "")
            payers = b.get("payers", [])

            # mb_001: NM_Hospital_Bill.pdf — originally had BCBS payer
            if bill_name == "NM_Hospital_Bill.pdf":
                if len(payers) > 0:
                    errors.append(f"{bill_name} still has {len(payers)} payer(s)")
                expected_balance = b.get("billAmount", 0) - b.get("adjustment", 0)
                actual_balance = b.get("balanceOwed", 0)
                if actual_balance != expected_balance:
                    errors.append(
                        f"{bill_name} balance owed is {actual_balance}, "
                        f"expected {expected_balance} (bill amount - adjustment)"
                    )

            # mb_002: CPTC_Bill_Full.pdf — originally had BCBS payer
            elif bill_name == "CPTC_Bill_Full.pdf":
                if len(payers) > 0:
                    errors.append(f"{bill_name} still has {len(payers)} payer(s)")
                expected_balance = b.get("billAmount", 0) - b.get("adjustment", 0)
                actual_balance = b.get("balanceOwed", 0)
                if actual_balance != expected_balance:
                    errors.append(
                        f"{bill_name} balance owed is {actual_balance}, "
                        f"expected {expected_balance} (bill amount - adjustment)"
                    )

    if errors:
        return False, "; ".join(errors)

    return True, "All payers removed and balances recalculated on Rodriguez medical bills."
