import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    email = next(
        (e for e in state["emails"] if e["subject"] == "CI/CD Pipeline Migration Plan"),
        None,
    )
    if not email:
        return False, "Email 'CI/CD Pipeline Migration Plan' not found."

    if not email["isSnoozed"]:
        return False, "Email is not snoozed."

    if not email.get("snoozeUntil"):
        return False, "Email snoozeUntil is not set."

    if "2026-03-01" not in email["snoozeUntil"]:
        return False, f"Expected snooze until 2026-03-01, got '{email['snoozeUntil']}'."

    if "INBOX" in email["labels"]:
        return False, "Email is still in the Inbox."

    return True, "Email 'CI/CD Pipeline Migration Plan' snoozed until March 1, 2026."
