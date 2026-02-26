"""Edit the Morning Brew filter to also archive matching messages and mark them as read."""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    response = requests.get(f"{server_url}/api/state")
    if response.status_code != 200:
        return False, f"Failed to fetch state: HTTP {response.status_code}"

    state = response.json()
    filters = state.get("filters", [])

    # Find filter_2 by id or by criteria.from
    target_filter = None
    for f in filters:
        if f.get("id") == "filter_2":
            target_filter = f
            break
    if target_filter is None:
        for f in filters:
            criteria = f.get("criteria", {})
            if criteria.get("from") == "crew@morningbrew.com":
                target_filter = f
                break

    if target_filter is None:
        return False, (
            "Could not find filter_2 or a filter with "
            "criteria.from='crew@morningbrew.com'"
        )

    actions = target_filter.get("actions", {})
    errors = []

    if actions.get("archive") is not True:
        errors.append(
            f"actions.archive is {actions.get('archive')}, expected True"
        )

    if actions.get("markRead") is not True:
        errors.append(
            f"actions.markRead is {actions.get('markRead')}, expected True"
        )

    if errors:
        return False, "; ".join(errors)

    return True, (
        "Morning Brew filter (filter_2) now archives and marks as read."
    )
