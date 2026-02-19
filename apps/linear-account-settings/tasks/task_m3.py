import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the user's email was changed to 'jordan@nextera-labs.com'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    cu = state.get("currentUser", {})
    email = cu.get("email", "")

    if email != "jordan@nextera-labs.com":
        return False, f"Expected email 'jordan@nextera-labs.com', got '{email}'."

    # Verify sync to workspaceMembers
    members = state.get("workspaceMembers", [])
    member = next((m for m in members if m["id"] == cu["id"]), None)
    if member and member.get("email") != "jordan@nextera-labs.com":
        return False, f"Email not synced to workspaceMembers: got '{member.get('email')}'."

    return True, "Email successfully changed to 'jordan@nextera-labs.com'."
