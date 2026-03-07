import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    msg = next((m for m in state["messages"] if m["id"] == "msg_06"), None)
    if not msg:
        return False, "Message 'msg_06' not found."
    if not msg.get("isRead"):
        return False, "Message from Stripe is still unread."
    return True, "Stripe message marked as read successfully."
