import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    labels = state.get("labels", [])

    label_names = [l.get("name", "") for l in labels]

    old_name = "Read Later"
    new_name = "Bookmark"

    if old_name in label_names:
        return False, (
            f"Label '{old_name}' still exists. It should have been renamed to '{new_name}'."
        )

    if new_name not in label_names:
        return False, (
            f"Label '{new_name}' not found. Expected '{old_name}' to be renamed to '{new_name}'. "
            f"Existing labels: {label_names}"
        )

    return True, f"Label '{old_name}' successfully renamed to '{new_name}'."
