import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    delegates = state.get("delegates", [])
    errors = []

    # Check total delegate count is exactly 2
    if len(delegates) != 2:
        errors.append(
            f"Expected exactly 2 delegates, found {len(delegates)}."
        )

    # Check that old delegates are gone
    old_emails = [
        "james.wu@techcorp.io",
        "priya.sharma@techcorp.io",
        "alex.martinez@techcorp.io",
    ]
    for old_email in old_emails:
        for d in delegates:
            if d.get("email") == old_email:
                errors.append(
                    f"Old delegate {old_email} still exists and should have been removed."
                )

    # Check that Jennifer Walsh exists with correct details
    jennifer = None
    for d in delegates:
        if d.get("email") == "jennifer.walsh@techcorp.io":
            jennifer = d
            break

    if jennifer is None:
        errors.append("Delegate jennifer.walsh@techcorp.io not found.")
    else:
        if jennifer.get("name") != "Jennifer Walsh":
            errors.append(
                f"Jennifer Walsh delegate name is '{jennifer.get('name')}', "
                f"expected 'Jennifer Walsh'."
            )
        if jennifer.get("status") != "pending":
            errors.append(
                f"Jennifer Walsh delegate status is '{jennifer.get('status')}', "
                f"expected 'pending'."
            )

    # Check that David Park exists with correct details
    david = None
    for d in delegates:
        if d.get("email") == "david.park@techcorp.io":
            david = d
            break

    if david is None:
        errors.append("Delegate david.park@techcorp.io not found.")
    else:
        if david.get("name") != "David Park":
            errors.append(
                f"David Park delegate name is '{david.get('name')}', "
                f"expected 'David Park'."
            )
        if david.get("status") != "pending":
            errors.append(
                f"David Park delegate status is '{david.get('status')}', "
                f"expected 'pending'."
            )

    if errors:
        return False, " ".join(errors)

    return True, (
        "Delegation cleaned up: old delegates removed, Jennifer Walsh and "
        "David Park added as pending delegates."
    )
