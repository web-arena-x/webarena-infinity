import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    emails = state.get("emails", [])
    for email in emails:
        if email.get("isDraft") is True and email.get("subject") == "Code Review Feedback":
            to_list = email.get("to", [])
            for recipient in to_list:
                if isinstance(recipient, dict):
                    addr = recipient.get("email", "").lower()
                elif isinstance(recipient, str):
                    addr = recipient.lower()
                else:
                    continue
                if addr == "priya.sharma@cloudnine.dev":
                    return True, "Task completed successfully."
            # Found draft with right subject but wrong recipient
            return False, (
                f"Found draft with subject 'Code Review Feedback' but 'to' list does "
                f"not contain 'priya.sharma@cloudnine.dev'. Current to: {to_list}"
            )

    return False, (
        "Could not find a draft email with subject 'Code Review Feedback'. "
        "Expected isDraft=True and subject='Code Review Feedback'."
    )
