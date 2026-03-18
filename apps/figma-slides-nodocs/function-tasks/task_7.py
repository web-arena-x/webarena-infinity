import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    presentations = state.get("presentations", [])
    for pres in presentations:
        if pres.get("title") == "Design Workshop Materials":
            if pres.get("status") == "published":
                return True, "Presentation 'Design Workshop Materials' status is 'published'."
            else:
                return False, f"Presentation 'Design Workshop Materials' has status='{pres.get('status')}', expected 'published'."

    return False, "No presentation with title 'Design Workshop Materials' found."
