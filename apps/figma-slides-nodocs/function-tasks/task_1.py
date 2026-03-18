import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    presentations = state.get("presentations", [])
    for pres in presentations:
        if pres.get("title") == "AI Strategy 2026":
            if pres.get("description") != "Company-wide AI adoption plan":
                return False, f"Presentation 'AI Strategy 2026' found but description is '{pres.get('description')}', expected 'Company-wide AI adoption plan'."
            if pres.get("status") != "draft":
                return False, f"Presentation 'AI Strategy 2026' found but status is '{pres.get('status')}', expected 'draft'."
            return True, "Presentation 'AI Strategy 2026' exists with correct description and draft status."

    return False, "No presentation with title 'AI Strategy 2026' found."
