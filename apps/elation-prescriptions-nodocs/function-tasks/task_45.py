import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})

    favorites = settings.get("favoritesDrugIds", [])
    if "drug_001" in favorites:
        return False, f"drug_001 (Atorvastatin) is still in favoritesDrugIds: {favorites}."

    return True, "Atorvastatin (drug_001) has been removed from favorites."
