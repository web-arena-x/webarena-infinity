import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify external SMTP aliases deleted, reply-from set to default."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    aliases = state.get("aliases", [])
    reply_from = state.get("replyFromSetting", "")

    # External SMTP aliases that should be deleted:
    # - schen@alumni.stanford.edu (smtp.stanford.edu)
    # - sarah@chen-family.org (mail.chen-family.org)
    external_emails = {
        "schen@alumni.stanford.edu",
        "sarah@chen-family.org",
    }

    still_present = []
    for a in aliases:
        if a.get("email") in external_emails:
            still_present.append(a.get("email"))

    if still_present:
        return False, (
            f"External SMTP aliases should be deleted: "
            f"{', '.join(still_present)}."
        )

    # These should remain:
    # - sarah.chen@techcorp.io (primary, no external SMTP)
    # - support@techcorp.io (SMTP is smtp.techcorp.io — internal)
    expected_remaining = {
        "sarah.chen@techcorp.io",
        "support@techcorp.io",
    }

    remaining_emails = {a.get("email") for a in aliases}
    missing = expected_remaining - remaining_emails

    if missing:
        return False, (
            f"These aliases should still exist (internal SMTP): "
            f"{', '.join(missing)}."
        )

    # Check reply-from setting
    if reply_from != "default":
        return False, (
            f"Reply-from setting should be 'default', got {reply_from!r}."
        )

    return True, (
        "External SMTP aliases deleted (Stanford, chen-family.org). "
        "Internal aliases preserved. Reply-from set to default."
    )
