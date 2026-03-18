import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify all old app passwords revoked and 3 new ones created."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    app_passwords = state.get("appPasswords", [])

    # Original passwords should be gone
    old_names = {"Thunderbird on MacBook", "Mail on iPhone", "Outlook Desktop"}
    remaining_old = [
        ap["name"] for ap in app_passwords if ap["name"] in old_names
    ]

    if remaining_old:
        return False, (
            f"Old app passwords should be revoked: {', '.join(remaining_old)}."
        )

    # New passwords should exist
    expected_new = {"Work Laptop", "Home Desktop", "Tablet"}
    found_new = {ap["name"] for ap in app_passwords if ap["name"] in expected_new}
    missing = expected_new - found_new

    if missing:
        return False, (
            f"Missing new app passwords: {', '.join(sorted(missing))}."
        )

    # Should have exactly 3 passwords
    if len(app_passwords) != 3:
        return False, (
            f"Expected exactly 3 app passwords, found {len(app_passwords)}."
        )

    return True, (
        "All old app passwords revoked. New passwords created: "
        "Work Laptop, Home Desktop, Tablet."
    )
