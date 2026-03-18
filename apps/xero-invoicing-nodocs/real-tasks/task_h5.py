import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Update the company details in settings."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    settings = state.get("settings", {})

    expected = {
        "companyName": "Kiwi Consulting Group",
        "companyEmail": "hello@kiwiconsulting.co.nz",
        "companyPhone": "+64 9 555 0200",
        "companyAddress": "100 Queen Street, Level 10, Auckland 1010, New Zealand",
    }

    errors = []

    for key, expected_value in expected.items():
        actual = settings.get(key)
        if actual != expected_value:
            errors.append(
                f"settings.{key} is '{actual}', expected '{expected_value}'"
            )

    if errors:
        return False, "; ".join(errors)

    return True, "Company details updated correctly in settings"
