import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    aliases = state.get("aliases", [])

    for alias in aliases:
        if alias.get("email") == "sarah@chen-family.org":
            return False, (
                "The family email alias (sarah@chen-family.org) still exists "
                "in the aliases list. Expected it to be removed."
            )

    return True, (
        "The family email alias (sarah@chen-family.org) has been successfully removed."
    )
