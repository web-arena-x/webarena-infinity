import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    numbering = state.get("numberingScheme", {})

    errors = []

    separator = numbering.get("separator")
    if separator != "/":
        errors.append(f"Numbering separator is '{separator}', expected '/'.")

    padding = numbering.get("numberPadding")
    if padding != 6:
        errors.append(f"Numbering numberPadding is {padding}, expected 6.")

    if errors:
        return False, " ".join(errors)

    return True, "Numbering scheme updated to slash separator with 6-digit padding."
