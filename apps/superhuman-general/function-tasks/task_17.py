import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])
    settings = state.get("settings", {})

    # Find the newsletter email
    email = next(
        (e for e in emails
         if "Today's Briefing" in e.get("subject", "")
         and "AI Startup Funding" in e.get("subject", "")),
        None,
    )
    if email is None:
        return False, "Could not find email 'Today's Briefing: AI Startup Funding Hits Record $12B in Q1'."

    if email.get("isDone") is not True:
        return False, f"Newsletter email is not marked as done. isDone={email.get('isDone')}"

    blocked_senders = settings.get("blockedSenders", [])
    if "newsletter@theinformation.com" not in blocked_senders:
        return False, (
            f"'newsletter@theinformation.com' not found in blockedSenders. "
            f"Current blockedSenders: {blocked_senders}"
        )

    return True, "Unsubscribed from newsletter@theinformation.com and email marked as done."
