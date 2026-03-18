import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify marketing alias created+default, Marketing Director added as delegate."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    aliases = state.get("aliases", [])
    delegates = state.get("delegates", [])

    # Check marketing alias exists
    marketing = None
    for a in aliases:
        if a.get("email") == "marketing@techcorp.io":
            marketing = a
            break

    if marketing is None:
        return False, "Alias for marketing@techcorp.io not found."

    # Check alias settings
    errors = []
    if "Marketing" not in (marketing.get("name") or ""):
        errors.append(
            f"alias name should contain 'Marketing', "
            f"got {marketing.get('name')!r}"
        )
    if marketing.get("smtpServer") != "smtp.techcorp.io":
        errors.append(
            f"SMTP server should be 'smtp.techcorp.io', "
            f"got {marketing.get('smtpServer')!r}"
        )
    if str(marketing.get("smtpPort", "")) != "587":
        errors.append(
            f"SMTP port should be '587', got {marketing.get('smtpPort')!r}"
        )
    if marketing.get("smtpUsername") != "marketing@techcorp.io":
        errors.append(
            f"SMTP username should be 'marketing@techcorp.io', "
            f"got {marketing.get('smtpUsername')!r}"
        )
    if not marketing.get("useSSL"):
        errors.append("SSL should be enabled")

    if errors:
        return False, "Alias settings incorrect: " + "; ".join(errors) + "."

    # Check it's the default
    if not marketing.get("isDefault"):
        return False, "marketing@techcorp.io should be the default sending address."

    # No other alias should be default
    for a in aliases:
        if a.get("email") != "marketing@techcorp.io" and a.get("isDefault"):
            return False, (
                f"{a.get('email')} should not be default — "
                f"only marketing@techcorp.io should be."
            )

    # Check Elaine Cho (Marketing Director) added as delegate
    elaine_found = False
    for d in delegates:
        if d.get("email") == "elaine.cho@techcorp.io":
            elaine_found = True
            break

    if not elaine_found:
        return False, (
            "Elaine Cho (elaine.cho@techcorp.io, Marketing Director) "
            "not found in delegates."
        )

    return True, (
        "Marketing alias created with SMTP settings and set as default. "
        "Elaine Cho (Marketing Director) added as delegate."
    )
