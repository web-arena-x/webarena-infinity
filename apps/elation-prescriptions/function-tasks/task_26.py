import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})
    value = settings.get("showFormularyData")

    if value is not False:
        return False, f"showFormularyData is {value}, expected false."

    return True, "showFormularyData successfully set to false."
