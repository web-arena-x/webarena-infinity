import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    jun_id = next((u["id"] for u in state["users"] if "Jun Nakamura" in u.get("name", "")), None)
    ana_id = next((u["id"] for u in state["users"] if "Ana Garcia" in u.get("name", "")), None)
    if jun_id is None or ana_id is None:
        return False, "Could not find Jun Nakamura or Ana Garcia."

    for issue_id in [1, 2, 46]:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if jun_id in issue.get("assigneeIds", []):
            return False, f"Jun Nakamura (id {jun_id}) still assigned to issue #{issue_id}."
        if ana_id not in issue.get("assigneeIds", []):
            return False, f"Ana Garcia (id {ana_id}) not assigned to issue #{issue_id}."

    return True, "Jun Nakamura replaced by Ana Garcia on issues #1, #2, #46."
