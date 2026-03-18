import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    other_contacts = state.get("otherContacts", [])

    # Check for any other contact with noreply or no-reply in their email
    noreply_contacts = []
    for oc in other_contacts:
        email = (oc.get("email") or "").lower()
        if "noreply" in email or "no-reply" in email:
            name = f"{oc.get('firstName', '')} {oc.get('lastName', '')}".strip()
            noreply_contacts.append(f"{name} ({oc.get('email')})")

    if noreply_contacts:
        return False, (
            f"The following automated service contacts still exist in other contacts: "
            f"{', '.join(noreply_contacts)}."
        )

    # Verify that other non-noreply contacts still exist
    if len(other_contacts) == 0:
        return False, (
            "All other contacts were deleted. Only noreply/no-reply contacts "
            "should have been removed."
        )

    return True, (
        f"No other contacts with 'noreply' or 'no-reply' in their email remain. "
        f"{len(other_contacts)} other contacts still exist."
    )
