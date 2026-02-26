import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state.get("settings", {})

    errors = []

    nudges = settings.get("nudges", {})
    suggest_reply = nudges.get("suggestEmailsToReply")
    if suggest_reply is not False:
        errors.append(
            f"settings.nudges.suggestEmailsToReply is {suggest_reply}, expected False"
        )

    default_reply = settings.get("defaultReplyBehavior", "")
    if default_reply != "reply_all":
        errors.append(
            f"settings.defaultReplyBehavior is '{default_reply}', expected 'reply_all'"
        )

    if errors:
        return False, "; ".join(errors)

    return True, "Task completed successfully."
