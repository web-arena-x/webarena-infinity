import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    providers = state.get("providers", [])
    for provider in providers:
        if provider.get("id") == "prov_1":
            timeframe = provider.get("notificationTimeframe")
            if timeframe == "72_hours":
                return True, "Notification timeframe updated to 72 hours."
            else:
                return False, (
                    f"Provider prov_1 found but notificationTimeframe is "
                    f"'{timeframe}', expected '72_hours'."
                )

    return False, "Provider with id 'prov_1' not found in providers."
