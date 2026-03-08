import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    matters = state.get("matters", [])
    users = state.get("firmUsers", [])

    # Find James Chen and Michael Osei user IDs
    chen_id = None
    osei_id = None
    for u in users:
        if u.get("fullName") == "James Chen":
            chen_id = u.get("id")
        elif u.get("fullName") == "Michael Osei":
            osei_id = u.get("id")

    if not chen_id:
        return False, "James Chen not found in firm users."
    if not osei_id:
        return False, "Michael Osei not found in firm users."

    errors = []

    # All of Chen's matters should be Closed
    for m in matters:
        if m.get("responsibleAttorneyId") == chen_id:
            if m.get("status") != "Closed":
                errors.append(
                    f"Chen's matter '{m.get('description')}' has status "
                    f"'{m.get('status')}', expected 'Closed'"
                )

    # All of Osei's matters should be Pending (on hold)
    for m in matters:
        if m.get("responsibleAttorneyId") == osei_id:
            if m.get("status") != "Pending":
                errors.append(
                    f"Osei's matter '{m.get('description')}' has status "
                    f"'{m.get('status')}', expected 'Pending'"
                )

    if errors:
        return False, "; ".join(errors)

    return True, "All Chen matters closed and all Osei matters put on hold."
