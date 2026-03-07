import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    expected = "Aspiring product manager and engineer. Passionate about building AI products that make a difference."
    actual = state["currentUser"].get("bio", "")
    if actual == expected:
        return True, "Bio updated successfully."
    return False, f"Bio mismatch. Expected: '{expected}', got: '{actual}'."
