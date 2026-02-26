"""
Task M10: Delete the filter that handles GitHub notifications.
Check that NO filter in state["filters"] has criteria.from containing 'notifications@github.com'.
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    response = requests.get(f"{server_url}/api/state")
    if response.status_code != 200:
        return False, f"Failed to fetch state: HTTP {response.status_code}"

    state = response.json()
    filters = state.get("filters", [])

    for f in filters:
        criteria = f.get("criteria", {})
        from_value = criteria.get("from", "")
        if "notifications@github.com" in from_value:
            return False, (
                f"Filter with criteria.from containing 'notifications@github.com' still exists: {f}"
            )

    return True, "No filter with criteria.from containing 'notifications@github.com' found. GitHub notification filter has been deleted."
