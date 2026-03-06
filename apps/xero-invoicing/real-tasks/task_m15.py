import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    quotes = state.get("quotes", [])

    # Find original QU-0025
    original = None
    for q in quotes:
        if q.get("number") == "QU-0025":
            original = q
            break

    if original is None:
        return False, "Original quote QU-0025 not found."

    original_contact = original.get("contactId")

    # Look for a new draft quote with same contactId
    new_draft = None
    for q in quotes:
        if q.get("number") == "QU-0025":
            continue
        if q.get("status") == "draft" and q.get("contactId") == original_contact:
            new_draft = q
            break

    if new_draft is None:
        return False, f"No new draft quote found for contact '{original_contact}' (Fresh Start Catering)."

    return True, f"New draft quote {new_draft.get('number')} created as copy of QU-0025 for Fresh Start Catering."
