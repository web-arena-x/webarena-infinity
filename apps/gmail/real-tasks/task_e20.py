"""
Task: Set the maximum page size to 25 conversations.
Verify: state["settings"]["maxPageSize"] == 25.
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    settings = state.get("settings", {})

    max_page_size = settings.get("maxPageSize")
    if max_page_size != 25:
        return False, (
            f"Maximum page size is not 25. "
            f"maxPageSize={max_page_size}"
        )

    return True, "Maximum page size is set to 25."
