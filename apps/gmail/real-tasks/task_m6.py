"""
Task M6: Set up a filter for emails from david.kim@financeplus.com that applies the Finance label.
Check that a filter exists in state["filters"] where criteria.from='david.kim@financeplus.com'
AND actions.label='label_3'.
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
        actions = f.get("actions", {})
        if criteria.get("from") == "david.kim@financeplus.com" and actions.get("label") == "label_3":
            return True, "Filter found: from='david.kim@financeplus.com' with action label='label_3' (Finance)."

    return False, (
        f"No filter found with criteria.from='david.kim@financeplus.com' and actions.label='label_3'. "
        f"Current filters: {filters}"
    )
