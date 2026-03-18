import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    other_contacts = state.get("otherContacts", [])

    errors = []

    for oc in other_contacts:
        if oc.get("email") == "no-reply@zoom.us":
            errors.append("Other contact 'no-reply@zoom.us' (Zoom no-reply) still exists.")
        if oc.get("email") == "meetingbot@calendly.com":
            errors.append("Other contact 'meetingbot@calendly.com' (Calendly meeting bot) still exists.")

    if errors:
        return False, " ".join(errors)

    return True, "Zoom no-reply and Calendly meeting bot entries deleted from Other Contacts."
