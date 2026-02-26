"""Disable Promotions, Updates, and Forums categories, and change inbox type to Important first."""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    response = requests.get(f"{server_url}/api/state")
    if response.status_code != 200:
        return False, f"Failed to fetch state: HTTP {response.status_code}"

    state = response.json()
    settings = state.get("settings", {})

    errors = []

    categories = settings.get("categoriesEnabled", {})
    for cat in ["promotions", "updates", "forums"]:
        if categories.get(cat) is not False:
            errors.append(
                f"categoriesEnabled.{cat} is {categories.get(cat)}, expected False"
            )

    inbox_type = settings.get("inboxType", "")
    if inbox_type != "important_first":
        errors.append(
            f"inboxType is '{inbox_type}', expected 'important_first'"
        )

    if errors:
        return False, "; ".join(errors)

    return True, (
        "Promotions, Updates, and Forums categories are disabled and inbox "
        "type is 'important_first'."
    )
