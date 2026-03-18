import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    aliases = state.get("aliases", [])

    # Only 1 alias should remain
    if len(aliases) != 1:
        remaining_emails = [a.get("email") for a in aliases]
        return False, (
            f"Expected exactly 1 alias remaining, found {len(aliases)}: "
            f"{', '.join(remaining_emails)}."
        )

    # The remaining alias should be sarah.chen@techcorp.io
    alias = aliases[0]
    if alias.get("email") != "sarah.chen@techcorp.io":
        return False, (
            f"Expected remaining alias to be 'sarah.chen@techcorp.io', "
            f"got '{alias.get('email')}'."
        )

    if alias.get("isPrimary") is not True:
        return False, "Remaining alias should have isPrimary=True."

    if alias.get("isDefault") is not True:
        return False, "Remaining alias should have isDefault=True."

    # Verify replyFromSetting is "default"
    reply_from = state.get("replyFromSetting")
    if reply_from != "default":
        return False, (
            f"Expected replyFromSetting to be 'default', got '{reply_from}'."
        )

    return True, (
        "All non-primary, non-default aliases removed. Only "
        "sarah.chen@techcorp.io remains (primary + default). "
        "Reply-from setting is 'default'."
    )
