import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    contacts = state.get("contacts", [])

    tom = None
    for contact in contacts:
        if contact.get("firstName") == "Tom" and contact.get("lastName") == "O'Brien":
            tom = contact
            break

    if tom is None:
        return False, (
            "Could not find contact with firstName='Tom' and lastName=\"O'Brien\" "
            "in the contacts list."
        )

    groups = tom.get("groups", [])
    if "grp_4" in groups:
        return False, (
            f"Tom O'Brien still has 'grp_4' (Engineering Team) in their groups array: "
            f"{groups}. Expected 'grp_4' to be removed."
        )

    return True, (
        "Tom O'Brien has been successfully removed from the Engineering Team label "
        "(grp_4 is no longer in their groups array)."
    )
