import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    aliases = state.get("aliases", [])

    # Find the new notifications alias
    notif_alias = None
    for a in aliases:
        if a.get("email") == "notifications@techcorp.io":
            notif_alias = a
            break

    if notif_alias is None:
        return False, "Alias with email 'notifications@techcorp.io' not found."

    # Verify alias fields
    errors = []
    if notif_alias.get("name") != "TechCorp Notifications":
        errors.append(
            f"Expected alias name 'TechCorp Notifications', got '{notif_alias.get('name')}'."
        )
    if notif_alias.get("smtpServer") != "smtp.techcorp.io":
        errors.append(
            f"Expected smtpServer 'smtp.techcorp.io', got '{notif_alias.get('smtpServer')}'."
        )
    if str(notif_alias.get("smtpPort")) != "587":
        errors.append(
            f"Expected smtpPort '587', got '{notif_alias.get('smtpPort')}'."
        )
    if notif_alias.get("smtpUsername") != "notifications@techcorp.io":
        errors.append(
            f"Expected smtpUsername 'notifications@techcorp.io', "
            f"got '{notif_alias.get('smtpUsername')}'."
        )
    if notif_alias.get("useSSL") is not True:
        errors.append(
            f"Expected useSSL to be True, got '{notif_alias.get('useSSL')}'."
        )
    if notif_alias.get("isDefault") is not True:
        errors.append(
            f"Expected notifications alias isDefault to be True, "
            f"got '{notif_alias.get('isDefault')}'."
        )

    if errors:
        return False, " ".join(errors)

    # Verify the primary alias (sarah.chen@techcorp.io) is no longer default
    primary_alias = None
    for a in aliases:
        if a.get("email") == "sarah.chen@techcorp.io":
            primary_alias = a
            break

    if primary_alias is None:
        return False, "Primary alias sarah.chen@techcorp.io not found."

    if primary_alias.get("isDefault") is True:
        return False, (
            "Primary alias sarah.chen@techcorp.io should no longer be the default "
            "sending address, but isDefault is still True."
        )

    # Verify replyFromSetting is "same"
    reply_from = state.get("replyFromSetting")
    if reply_from != "same":
        return False, (
            f"Expected replyFromSetting to be 'same', got '{reply_from}'."
        )

    return True, (
        "Alias notifications@techcorp.io created correctly with all fields, "
        "set as default sending address, and reply-from set to 'same'."
    )
