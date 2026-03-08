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

    # Find bills by provider
    for p in rodriguez.get("medicalProviders", []):
        for b in p.get("medicalBills", []):
            bill_name = b.get("fileName", "")

            # Chicago PT bill (CPTC_Bill_Full.pdf) — balance should be lien
            if bill_name == "CPTC_Bill_Full.pdf":
                if b.get("balanceIsLien") is not True:
                    errors.append(
                        f"CPTC bill balanceIsLien is {b.get('balanceIsLien')}, expected True"
                    )

            # Advanced Imaging bill (AIA_Invoice_Aug.pdf) — remove outstanding
            elif bill_name == "AIA_Invoice_Aug.pdf":
                if b.get("balanceIsOutstanding") is not False:
                    errors.append(
                        f"AIA bill balanceIsOutstanding is {b.get('balanceIsOutstanding')}, "
                        f"expected False"
                    )

            # NM Hospital bill (NM_Hospital_Bill.pdf) — adjustment to $10,000
            elif bill_name == "NM_Hospital_Bill.pdf":
                if b.get("adjustment") != 10000:
                    errors.append(
                        f"NM Hospital bill adjustment is {b.get('adjustment')}, expected 10000"
                    )

    if errors:
        return False, "; ".join(errors)

    return True, "CPTC balance marked as lien, AIA outstanding removed, NM adjustment set to $10,000."
