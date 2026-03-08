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
    comment_text = "Bill verified and approved"

    # Bills that originally had payers:
    # mb_001 (NM_Hospital_Bill.pdf, con_018) and mb_002 (CPTC_Bill_Full.pdf, con_019)
    expected_bills = {"NM_Hospital_Bill.pdf", "CPTC_Bill_Full.pdf"}

    for p in rodriguez.get("medicalProviders", []):
        for b in p.get("medicalBills", []):
            bill_name = b.get("fileName", "")
            if bill_name in expected_bills:
                comments = b.get("comments", [])
                has_comment = any(
                    c.get("text") == comment_text for c in comments
                )
                if not has_comment:
                    errors.append(
                        f"Comment '{comment_text}' not found on {bill_name}"
                    )

    if errors:
        return False, "; ".join(errors)

    return True, "Comment 'Bill verified and approved' added to all bills with payers."
