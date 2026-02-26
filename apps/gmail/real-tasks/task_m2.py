"""
Task M2: Create a new label called 'Urgent' with a red background color.
Check that a label with name='Urgent' exists in state["labels"], type='user', and has a non-null color.
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    response = requests.get(f"{server_url}/api/state")
    if response.status_code != 200:
        return False, f"Failed to fetch state: HTTP {response.status_code}"

    state = response.json()
    labels = state.get("labels", [])

    for label in labels:
        if label.get("name") == "Urgent":
            if label.get("type") != "user":
                return False, f"Label 'Urgent' exists but type is '{label.get('type')}', expected 'user'."
            color = label.get("color")
            if color is None:
                return False, "Label 'Urgent' exists but has no color set."
            return True, f"Label 'Urgent' exists with type='user' and color={color}."

    return False, "No label with name='Urgent' found in state."
