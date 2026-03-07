import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    actual = state["currentUser"]["careerInterests"]["expectedGraduationDate"]
    if actual == "December 2026":
        return True, "Expected graduation date changed to December 2026."
    return False, f"Expected graduation date is '{actual}', expected 'December 2026'."
