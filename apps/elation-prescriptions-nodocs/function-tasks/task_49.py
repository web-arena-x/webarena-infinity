import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})

    favorites = settings.get("favoritesDrugIds", [])
    if "drug_019" in favorites:
        return False, f"drug_019 (Pantoprazole) is still in favoritesDrugIds: {favorites}."

    return True, "Pantoprazole (drug_019) has been removed from favorites."
