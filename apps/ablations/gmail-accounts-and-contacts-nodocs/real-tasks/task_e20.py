import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    contacts = state.get("contacts", [])

    olivia = None
    for contact in contacts:
        if contact.get("firstName") == "Olivia" and contact.get("lastName") == "Grant":
            olivia = contact
            break

    if olivia is None:
        return False, (
            "Could not find contact with firstName='Olivia' and lastName='Grant' "
            "in the contacts list."
        )

    if olivia.get("starred") is True:
        return True, "Olivia Grant has been successfully starred."

    return False, (
        f"Olivia Grant's starred status is {olivia.get('starred')}, "
        f"but expected it to be True."
    )
