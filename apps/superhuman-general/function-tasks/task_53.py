import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])

    for email in emails:
        if email.get("subject") == "Design Review Feedback":
            # Check sender
            from_addr = email.get("from", {})
            sender_email = from_addr.get("email", "") if isinstance(from_addr, dict) else str(from_addr)
            if sender_email != "alex.morgan@acmecorp.com":
                return False, f"Email 'Design Review Feedback' from '{sender_email}', expected 'alex.morgan@acmecorp.com'."

            # Check recipient
            to_list = email.get("to", [])
            to_emails = [t.get("email", "") if isinstance(t, dict) else str(t) for t in to_list]
            if "marcus.w@designhub.io" not in to_emails:
                return False, f"Email 'Design Review Feedback' to does not include 'marcus.w@designhub.io'. Got: {to_emails}"

            # Check CC
            cc_list = email.get("cc", [])
            cc_emails = [c.get("email", "") if isinstance(c, dict) else str(c) for c in cc_list]
            if "sarah.chen@acmecorp.com" not in cc_emails:
                return False, f"Email 'Design Review Feedback' cc does not include 'sarah.chen@acmecorp.com'. Got: {cc_emails}"

            # Check body
            body = email.get("body", "")
            if "Great work on the new designs" not in body:
                return False, f"Email body does not contain 'Great work on the new designs'. Got: {body!r}"

            # Check not a draft
            if email.get("isDraft") is True:
                return False, "Email 'Design Review Feedback' is still a draft; it should have been sent."

            return True, "Email 'Design Review Feedback' sent correctly with proper to, cc, and body."

    return False, "No email with subject 'Design Review Feedback' found."
