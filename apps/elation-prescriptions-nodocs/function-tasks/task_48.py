import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})

    favorites = settings.get("favoritesDrugIds", [])
    if "drug_012" not in favorites:
        return False, f"drug_012 (Apixaban) is not in favoritesDrugIds: {favorites}."

    return True, "Apixaban (drug_012) has been added to favorites."
