import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    expected = "mayachen.io"
    actual = state["currentUser"].get("websiteUrl", "")
    if actual == expected:
        return True, "Website URL updated successfully."
    return False, f"Website URL mismatch. Expected: '{expected}', got: '{actual}'."
