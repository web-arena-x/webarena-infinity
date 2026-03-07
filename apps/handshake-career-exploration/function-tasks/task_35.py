import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    expected = "(650) 555-9999"
    actual = state["currentUser"].get("phone", "")
    if actual == expected:
        return True, "Phone updated successfully."
    return False, f"Phone mismatch. Expected: '{expected}', got: '{actual}'."
