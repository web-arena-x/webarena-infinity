import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})

    print_format = settings.get("printFormat")
    if print_format != "compact":
        return False, f"printFormat is '{print_format}', expected 'compact'."

    return True, "Print format changed to 'compact'."
