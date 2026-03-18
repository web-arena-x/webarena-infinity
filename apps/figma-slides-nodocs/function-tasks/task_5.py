import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    presentations = state.get("presentations", [])
    match = [p for p in presentations if p.get("title") == "Engineering Architecture Overview"]
    if not match:
        return False, "No presentation found with title 'Engineering Architecture Overview'."

    pres = match[0]
    if pres.get("starred") is not True:
        return False, f"Expected starred to be true, got {pres.get('starred')}."

    return True, "Presentation 'Engineering Architecture Overview' is now starred."
