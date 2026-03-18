import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})

    require_allergy = settings.get("requireAllergyReview")
    if require_allergy is not False:
        return False, f"requireAllergyReview is {require_allergy}, expected False."

    return True, "Require allergy review has been disabled (requireAllergyReview is False)."
