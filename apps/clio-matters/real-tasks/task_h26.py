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

    settlement = rodriguez.get("settlement", {})

    # Find Premier Auto recovery (con_015)
    premier_rec = None
    for r in settlement.get("recoveries", []):
        if r.get("sourceContactId") == "con_015":
            premier_rec = r
            break

    if not premier_rec:
        return False, "Premier Auto Dealers recovery (con_015) not found."

    # Find its legal fee
    premier_lf = None
    for lf in settlement.get("legalFees", []):
        if lf.get("recoveryId") == premier_rec.get("id"):
            premier_lf = lf
            break

    if not premier_lf:
        return False, "Legal fee for Premier Auto Dealers recovery not found."

    # Check for referral fee to Carlos Espinoza (con_022) at 5%
    referral_fees = premier_lf.get("referralFees", [])
    espinoza_ref = [rf for rf in referral_fees if rf.get("recipientId") == "con_022"]

    if not espinoza_ref:
        return False, "No referral fee for Carlos Espinoza (con_022) found on Premier Auto legal fee."

    rate = espinoza_ref[0].get("rate", 0)
    if rate != 5:
        return False, f"Referral fee rate is {rate}%, expected 5%."

    return True, "5% referral fee to Carlos Espinoza added on Premier Auto legal fee."
