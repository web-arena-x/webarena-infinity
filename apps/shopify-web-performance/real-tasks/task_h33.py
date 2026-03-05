import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    themes = state.get("themes", [])
    recs = state.get("recommendations", [])
    errors = []

    horizon = next((t for t in themes if t.get("name") == "Horizon - Outdoors"), None)
    if horizon is None:
        return False, "Could not find Horizon - Outdoors theme."

    # Homepage sections should be 8
    home = horizon.get("sectionsPerPage", {}).get("home")
    if home != 8:
        errors.append(f"Horizon homepage sections is {home}, expected 8.")

    # Reduce homepage sections recommendation should be resolved
    rec = next((r for r in recs if r.get("title") == "Reduce homepage sections"), None)
    if rec is None:
        errors.append("Recommendation 'Reduce homepage sections' not found.")
    elif rec.get("status") != "resolved":
        errors.append(f"Recommendation status is '{rec.get('status')}', expected 'resolved'.")

    if errors:
        return False, " ".join(errors)
    return True, "Homepage sections reduced to 8 and homepage sections recommendation resolved."
