import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    app_passwords = state.get("appPasswords", [])

    found_thunderbird = False
    found_outlook = False
    for ap in app_passwords:
        name = ap.get("name", "")
        if name == "Thunderbird on MacBook":
            found_thunderbird = True
        if name == "Outlook Desktop":
            found_outlook = True

    errors = []

    if found_thunderbird:
        errors.append("App password 'Thunderbird on MacBook' still exists.")

    if found_outlook:
        errors.append("App password 'Outlook Desktop' still exists.")

    if errors:
        return False, " ".join(errors)

    # Verify that at least 'Mail on iPhone' still remains
    remaining_names = [ap.get("name") for ap in app_passwords]
    if "Mail on iPhone" not in remaining_names:
        return False, (
            "Both Thunderbird and Outlook were removed, but 'Mail on iPhone' is also missing. "
            f"Remaining app passwords: {remaining_names}."
        )

    return True, "App passwords 'Thunderbird on MacBook' and 'Outlook Desktop' have been removed. 'Mail on iPhone' remains."
