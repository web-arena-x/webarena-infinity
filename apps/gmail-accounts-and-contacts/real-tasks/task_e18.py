# Task: Disable 2FA.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    login = state.get("accountSettings", {}).get("loginSettings", {})
    two_factor = login.get("twoFactorEnabled")

    if two_factor is False:
        return True, "Two-factor authentication is now disabled."
    else:
        return False, f"twoFactorEnabled is {two_factor}, expected false."
