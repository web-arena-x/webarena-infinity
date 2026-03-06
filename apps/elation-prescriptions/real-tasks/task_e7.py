import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check cost estimates are disabled
    settings = state.get("settings", {})
    show_cost_estimates = settings.get("showCostEstimates")

    if show_cost_estimates is not False:
        return False, f"settings.showCostEstimates is {show_cost_estimates}, expected false"

    return True, "Cost estimates disabled successfully"
