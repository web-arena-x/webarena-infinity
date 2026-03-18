import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"
    state = resp.json()
    comments = state.get("comments", [])
    comment = next(
        (
            c for c in comments
            if "database architecture" in c.get("content", "").lower()
            and c.get("presentationId") == "pres_005"
        ),
        None,
    )
    if comment is None:
        return False, "Comment about 'database architecture' on pres_005 not found"
    resolved = comment.get("resolved")
    if resolved is True:
        return True, f"Comment '{comment.get('id')}' about database architecture diagram is resolved as expected"
    return False, f"Expected comment about 'database architecture' to be resolved, got resolved=={resolved}"
