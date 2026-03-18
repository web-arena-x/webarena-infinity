import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify support alias default, reply-from same, HR partner as delegate."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    aliases = state.get("aliases", [])
    delegates = state.get("delegates", [])
    reply_from = state.get("replyFromSetting", "")

    # Check support@techcorp.io is default
    support_default = False
    for a in aliases:
        if a.get("email") == "support@techcorp.io":
            if a.get("isDefault"):
                support_default = True
        elif a.get("isDefault"):
            return False, (
                f"Only support@techcorp.io should be default, "
                f"but {a.get('email')} is also marked default."
            )

    if not support_default:
        return False, "support@techcorp.io should be the default sending address."

    # Check reply-from setting
    if reply_from != "same":
        return False, (
            f"Reply-from setting should be 'same', got {reply_from!r}."
        )

    # Check Megan Foster-Kim added as delegate
    megan_found = False
    for d in delegates:
        if d.get("email") == "megan.fosterkim@techcorp.io":
            megan_found = True
            break

    if not megan_found:
        return False, (
            "Megan Foster-Kim (megan.fosterkim@techcorp.io) not found "
            "in delegates."
        )

    return True, (
        "Support alias set as default, reply-from set to 'same', "
        "and HR Business Partner (Megan Foster-Kim) added as delegate."
    )
