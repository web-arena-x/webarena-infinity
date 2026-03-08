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

    # Find provider with highest total bill amount
    best_provider = None
    best_total = -1
    for p in rodriguez.get("medicalProviders", []):
        total = sum(b.get("billAmount", 0) for b in p.get("medicalBills", []))
        if total > best_total:
            best_total = total
            best_provider = p

    if not best_provider:
        return False, "No medical providers with bills found on Rodriguez case."

    # The highest should be NM Hospital (con_018) with $45,000
    records = best_provider.get("medicalRecords", [])
    if not records:
        return False, "Provider with highest bill amount has no medical records."

    first_record = records[0]
    comments = first_record.get("comments", [])

    comment_text = "Flagged for settlement review"
    has_comment = any(c.get("text") == comment_text for c in comments)

    if not has_comment:
        return False, (
            f"Comment '{comment_text}' not found on first record "
            f"'{first_record.get('fileName')}' of highest-billing provider."
        )

    return True, "Comment added to first record of highest-billing provider."
