import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])

    reply_email = next(
        (e for e in emails
         if e.get("from", {}).get("email") == "alex.morgan@acmecorp.com"
         and "Re:" in e.get("subject", "")
         and "Partnership Opportunity" in e.get("subject", "")
         and any(r.get("email") == "david.kim@financeplus.com" for r in e.get("to", []))),
        None,
    )
    if reply_email is None:
        return False, (
            "Could not find a reply from alex.morgan@acmecorp.com with subject containing "
            "'Re:' and 'Partnership Opportunity' sent to david.kim@financeplus.com."
        )

    body = reply_email.get("body", "")
    if "call next week" not in body.lower():
        return False, f"Reply body does not contain 'call next week'. Body: {body[:200]}"

    return True, "Reply to 'Partnership Opportunity' sent to david.kim@financeplus.com with correct body."
