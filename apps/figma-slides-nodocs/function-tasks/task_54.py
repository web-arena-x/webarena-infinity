import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    presentations = state.get("presentations", [])

    # Find pres_002 to get its creator
    pres_002 = None
    for p in presentations:
        if p.get("title") == "Brand Identity Guidelines v2.0":
            pres_002 = p
            break

    if not pres_002:
        return False, "Presentation 'Brand Identity Guidelines v2.0' not found."

    creator_id = pres_002.get("createdBy")
    if not creator_id:
        return False, "Could not determine creator of 'Brand Identity Guidelines v2.0'."

    # Find pres_005
    pres_005 = None
    for p in presentations:
        if p.get("title") == "Engineering Architecture Overview":
            pres_005 = p
            break

    if not pres_005:
        return False, "Presentation 'Engineering Architecture Overview' not found."

    share_settings = pres_005.get("shareSettings", {})
    shared_with = share_settings.get("sharedWith", [])

    if creator_id in shared_with:
        return True, f"Presentation 'Engineering Architecture Overview' is shared with '{creator_id}' (creator of 'Brand Identity Guidelines v2.0')."

    return False, f"User '{creator_id}' (creator of 'Brand Identity Guidelines v2.0') is not in sharedWith of 'Engineering Architecture Overview'. Current sharedWith: {shared_with}"
