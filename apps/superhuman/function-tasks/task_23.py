import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])

    target_subject = "Series B Timeline"
    target_recipient = "nbrooks@acmeventures.com"

    drafts = [e for e in emails if e.get("isDraft") is True]
    if not drafts:
        return False, "No draft emails found in state."

    matching = [
        e for e in drafts
        if target_subject.lower() in e.get("subject", "").lower()
    ]

    if not matching:
        return False, (
            f"No draft email found with subject containing '{target_subject}'. "
            f"Draft subjects: {[e.get('subject') for e in drafts]}"
        )

    for draft in matching:
        to_field = draft.get("to", [])
        # to can be a list of strings or a list of dicts with 'email' key
        recipients = []
        for r in to_field:
            if isinstance(r, str):
                recipients.append(r.lower())
            elif isinstance(r, dict):
                recipients.append(r.get("email", "").lower())
                recipients.append(r.get("address", "").lower())

        if target_recipient.lower() in recipients:
            return True, (
                f"Draft email found with subject '{draft.get('subject')}' "
                f"addressed to '{target_recipient}'."
            )

    return False, (
        f"Draft with subject '{target_subject}' exists but recipient "
        f"'{target_recipient}' not found in 'to' field. "
        f"Found recipients: {[e.get('to') for e in matching]}"
    )
