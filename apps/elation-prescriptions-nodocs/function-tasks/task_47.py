import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})

    favorites = settings.get("favoritesDrugIds", [])
    if "drug_007" not in favorites:
        return False, f"drug_007 (Metoprolol Succinate ER) is not in favoritesDrugIds: {favorites}."

    return True, "Metoprolol Succinate ER (drug_007) has been added to favorites."
