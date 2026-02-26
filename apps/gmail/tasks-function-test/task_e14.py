import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state.get("settings", {})
    nudges = settings.get("nudges", {})
    suggest_follow_up = nudges.get("suggestEmailsToFollowUp")

    if suggest_follow_up is False:
        return True, "Task completed successfully."
    else:
        return False, f"Follow-up nudges are not disabled (nudges.suggestEmailsToFollowUp={suggest_follow_up})."
