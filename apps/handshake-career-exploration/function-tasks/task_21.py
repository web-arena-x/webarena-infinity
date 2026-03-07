import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    unread = [m for m in state["messages"] if not m.get("isRead")]
    if unread:
        names = [m["employerName"] for m in unread]
        return False, f"Still {len(unread)} unread messages from: {', '.join(names)}."
    return True, "All messages marked as read successfully."
