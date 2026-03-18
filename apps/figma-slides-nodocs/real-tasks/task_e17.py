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
            if "revenue numbers confirmed" in c.get("content", "").lower()
            and c.get("presentationId") == "pres_006"
        ),
        None,
    )
    if comment is None:
        return False, "Comment about 'Revenue numbers confirmed' on pres_006 (All-Hands) not found"
    resolved = comment.get("resolved")
    if resolved is False:
        return True, f"Comment '{comment.get('id')}' (cmt_031) is unresolved as expected"
    return False, f"Expected comment about 'Revenue numbers confirmed' to be unresolved (resolved==false), got resolved=={resolved}"
