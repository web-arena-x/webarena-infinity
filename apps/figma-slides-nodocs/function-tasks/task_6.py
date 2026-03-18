import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    presentations = state.get("presentations", [])
    match = [p for p in presentations if p.get("title") == "Q1 2026 Product Roadmap"]
    if not match:
        return False, "No presentation found with title 'Q1 2026 Product Roadmap'."

    pres = match[0]
    if pres.get("starred") is not False:
        return False, f"Expected starred to be false, got {pres.get('starred')}."

    return True, "Presentation 'Q1 2026 Product Roadmap' is now unstarred."
