import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})
    value = settings.get("showCostEstimates")

    if value is not False:
        return False, f"showCostEstimates is {value}, expected false."

    return True, "showCostEstimates successfully set to false."
