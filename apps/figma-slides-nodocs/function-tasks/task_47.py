import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    comments = state.get("comments", [])
    target_comment = None
    for c in comments:
        if c.get("presentationId") == "pres_001" and "chart visualization" in c.get("content", "").lower():
            target_comment = c
            break

    if not target_comment:
        return False, "Comment about 'chart visualization' not found on pres_001."

    replies = target_comment.get("replies", [])
    expected_reply = "I agree, a bar chart would work best for this data."

    for r in replies:
        if expected_reply in r.get("content", ""):
            return True, f"Reply '{expected_reply}' found on the chart visualization comment."

    return False, f"No reply containing '{expected_reply}' found on the chart visualization comment. Found {len(replies)} replies."
