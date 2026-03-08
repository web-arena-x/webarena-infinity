# Task: Switch 2FA to SMS.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    login = state.get("accountSettings", {}).get("loginSettings", {})
    method = login.get("twoFactorMethod")

    if method == "sms":
        return True, "Two-factor authentication method is now SMS."
    else:
        return False, f"twoFactorMethod is '{method}', expected 'sms'."
