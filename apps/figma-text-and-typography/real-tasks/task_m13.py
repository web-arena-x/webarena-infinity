"""
Task: Change the nudge amount to 2 and the big nudge to 20.
Verify: preferences.nudgeAmount == 2 AND preferences.bigNudgeAmount == 20.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    preferences = state.get("preferences", {})

    nudge_amount = preferences.get("nudgeAmount")
    big_nudge_amount = preferences.get("bigNudgeAmount")

    errors = []
    if nudge_amount != 2:
        errors.append(f"Expected preferences.nudgeAmount == 2, got {nudge_amount}.")
    if big_nudge_amount != 20:
        errors.append(f"Expected preferences.bigNudgeAmount == 20, got {big_nudge_amount}.")

    if errors:
        return False, " ".join(errors)

    return True, "Nudge amount is 2 and big nudge amount is 20."
