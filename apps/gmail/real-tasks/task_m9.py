"""
Task M9: Rename the Reference label to Resources.
Find label with id='label_19', check name='Resources'.
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    response = requests.get(f"{server_url}/api/state")
    if response.status_code != 200:
        return False, f"Failed to fetch state: HTTP {response.status_code}"

    state = response.json()
    labels = state.get("labels", [])

    for label in labels:
        if label.get("id") == "label_19":
            name = label.get("name")
            if name == "Resources":
                return True, "Label label_19 has been renamed to 'Resources'."
            else:
                return False, f"Label label_19 has name='{name}', expected 'Resources'."

    return False, "Label with id='label_19' not found in state."
