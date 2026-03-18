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
            if "buddy program" in c.get("content", "").lower()
            and c.get("presentationId") == "pres_009"
        ),
        None,
    )
    if match is None:
        return True, "No comment about 'buddy program' on pres_009 exists as expected"
    return False, f"Expected comment about 'buddy program' on pres_009 to be deleted, but found comment id={match.get('id')}"
