"""Turn off the reply nudge suggestions."""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    response = requests.get(f"{server_url}/api/state")
    if response.status_code != 200:
        return False, f"Failed to fetch state: HTTP {response.status_code}"

    state = response.json()

    suggest_reply = state.get("settings", {}).get("nudges", {}).get("suggestEmailsToReply")
    if suggest_reply is False:
        return True, "Reply nudge suggestions are disabled."
    return False, f"Expected nudges.suggestEmailsToReply to be False, got {suggest_reply!r}."
