import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"
    state = resp.json()
    presentations = state.get("presentations", [])
    match = next(
        (p for p in presentations if "Competitor Analysis Dashboard" in p.get("title", "")),
        None,
    )
    if match is None:
        return True, "No presentation with title 'Competitor Analysis Dashboard' exists as expected"
    return False, f"Expected 'Competitor Analysis Dashboard' to be deleted, but found presentation with id={match.get('id')}"
