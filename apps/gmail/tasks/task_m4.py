import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    filters = state.get("filters", [])
    for f in filters:
        criteria = f.get("criteria", {})
        if criteria.get("from") == "sarah.chen@techcorp.io":
            return False, f"Filter with criteria.from='sarah.chen@techcorp.io' still exists (filter id={f.get('id')})."

    return True, "Task completed successfully."
