import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    expected = "linkedin.com/in/maya-chen-stanford"
    actual = state["currentUser"].get("linkedinUrl", "")
    if actual == expected:
        return True, "LinkedIn URL updated successfully."
    return False, f"LinkedIn URL mismatch. Expected: '{expected}', got: '{actual}'."
