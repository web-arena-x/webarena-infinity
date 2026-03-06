import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check formulary information display is disabled
    settings = state.get("settings", {})
    show_formulary_data = settings.get("showFormularyData")

    if show_formulary_data is not False:
        return False, f"settings.showFormularyData is {show_formulary_data}, expected false"

    return True, "Formulary information display disabled successfully"
