import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the user's pronouns were updated to 'he/him'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    cu = state.get("currentUser", {})
    pronouns = cu.get("pronouns", "")

    if pronouns != "he/him":
        return False, f"Expected pronouns 'he/him', got '{pronouns}'."

    return True, "User's pronouns successfully updated to 'he/him'."
