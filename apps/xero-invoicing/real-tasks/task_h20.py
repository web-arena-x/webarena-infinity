import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Check CN-0011 is deleted
    cn_011 = next((cn for cn in state.get("creditNotes", []) if cn.get("number") == "CN-0011"), None)
    if cn_011 is None:
        # Might have been removed entirely from the list
        pass
    else:
        if cn_011.get("status") != "deleted":
            return False, f"Expected CN-0011 status 'deleted', got '{cn_011.get('status')}'."

    # Find Pacific Freight contact
    contact = next((c for c in state.get("contacts", []) if "Pacific Freight" in c.get("name", "")), None)
    if contact is None:
        return False, "Pacific Freight Lines contact not found."

    pacific_id = contact.get("id")

    # Find a new credit note for Pacific Freight (not CN-0011)
    credit_notes = state.get("creditNotes", [])
    new_cn = next(
        (cn for cn in credit_notes
         if cn.get("contactId") == pacific_id
         and cn.get("number") != "CN-0011"
         and cn.get("status") != "deleted"),
        None
    )

    if new_cn is None:
        return False, "No new credit note found for Pacific Freight Lines."

    # Check total is around $500-550 (with or without GST)
    total = new_cn.get("total", 0)
    if total < 490 or total > 560:
        return False, f"Expected new credit note total ~$500-$550, got ${total}."

    return True, f"CN-0011 deleted and new credit note {new_cn.get('number')} created for Pacific Freight (~${total})."
