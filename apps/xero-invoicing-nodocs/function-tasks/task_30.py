import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    con = next((c for c in state["contacts"] if c["name"] == "Wellington Design Studio"), None)
    if not con:
        return False, "Contact 'Wellington Design Studio' not found."
    if con["email"] != "hello@wellingtondesign.co.nz":
        return False, f"Expected email 'hello@wellingtondesign.co.nz', got '{con['email']}'"
    if con["phone"] != "+64 4 555 1234":
        return False, f"Expected phone '+64 4 555 1234', got '{con['phone']}'"
    return True, "Contact 'Wellington Design Studio' created correctly."
