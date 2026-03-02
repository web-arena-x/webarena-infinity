import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    numbering_scheme = state.get("numberingScheme")
    if numbering_scheme is None:
        return False, "No numberingScheme found in application state."

    separator = numbering_scheme.get("separator")
    if separator != ".":
        return False, f"Numbering separator is '{separator}', expected '.'."

    return True, "Numbering scheme separator has been changed to a period."
