import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    numbering = state.get("numberingScheme", {})
    padding = numbering.get("numberPadding")

    if padding is None:
        return False, "numberingScheme.numberPadding is not set in application state."

    if padding != 6:
        return False, f"numberingScheme.numberPadding is {padding}, expected 6."

    return True, "Matter number padding has been changed to 6."
