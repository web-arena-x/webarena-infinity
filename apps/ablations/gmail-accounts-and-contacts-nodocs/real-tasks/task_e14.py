import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    aliases = state.get("aliases", [])

    support_alias = None
    primary_alias = None

    for alias in aliases:
        if alias.get("email") == "support@techcorp.io":
            support_alias = alias
        if alias.get("email") == "sarah.chen@techcorp.io":
            primary_alias = alias

    if support_alias is None:
        return False, (
            "Could not find alias with email 'support@techcorp.io' in the aliases list."
        )

    if primary_alias is None:
        return False, (
            "Could not find alias with email 'sarah.chen@techcorp.io' in the aliases list."
        )

    if not support_alias.get("isDefault"):
        return False, (
            "The support@techcorp.io alias is not set as the default sending address. "
            f"isDefault is {support_alias.get('isDefault')}."
        )

    if primary_alias.get("isDefault"):
        return False, (
            "The previous default alias sarah.chen@techcorp.io still has isDefault=True. "
            "Expected it to be False after changing the default."
        )

    return True, (
        "The support@techcorp.io alias is now the default sending address "
        "and sarah.chen@techcorp.io is no longer the default."
    )
