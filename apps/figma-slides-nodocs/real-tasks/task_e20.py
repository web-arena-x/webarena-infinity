import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"
    state = resp.json()
    comments = state.get("comments", [])
    match = next(
        (
            c for c in comments
            if "mobile nav redesign" in c.get("content", "").lower()
            and c.get("presentationId") == "pres_008"
        ),
        None,
    )
    if match is None:
        return True, "No comment about 'mobile nav redesign' on pres_008 exists as expected"
    return False, f"Expected comment about 'mobile nav redesign' on pres_008 to be deleted, but found comment id={match.get('id')}"
