import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    other_contacts = state.get("otherContacts", [])

    for oc in other_contacts:
        if oc.get("email") == "noreply@github.com":
            return False, (
                "GitHub notifications entry (noreply@github.com) still exists "
                "in Other Contacts. Expected it to be deleted."
            )

    return True, (
        "GitHub notifications entry (noreply@github.com) has been successfully "
        "deleted from Other Contacts."
    )
