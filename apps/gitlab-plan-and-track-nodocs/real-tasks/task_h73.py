import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # No epic should have any closed issue in its childIssueIds
    closed_ids = {i["id"] for i in state["issues"] if i.get("status") == "closed"}

    for epic in state["epics"]:
        for child_id in epic.get("childIssueIds", []):
            if child_id in closed_ids:
                return False, f"Epic '{epic.get('title')}' still has closed issue #{child_id} in childIssueIds."

    return True, "All closed child issues removed from every epic."
