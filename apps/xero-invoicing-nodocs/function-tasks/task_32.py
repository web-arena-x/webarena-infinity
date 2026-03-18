import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    con = next((c for c in state["contacts"] if c["name"] == "Ridgeway University"), None)
    if not con:
        return False, "Contact 'Ridgeway University' not found."
    if con["phone"] != "+64 9 445 8000":
        return False, f"Expected phone '+64 9 445 8000', got '{con['phone']}'"
    return True, "Ridgeway University phone updated correctly."
