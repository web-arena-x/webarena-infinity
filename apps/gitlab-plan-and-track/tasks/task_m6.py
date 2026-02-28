import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    issues = state.get("issues", [])
    issue = next((i for i in issues if i.get("title") == "Implement container registry garbage collection"), None)
    if issue is None:
        return False, "Could not find issue titled 'Implement container registry garbage collection'."

    labels = state.get("labels", [])
    breaking_change_label = next((l for l in labels if l.get("title") == "breaking-change"), None)
    if breaking_change_label is None:
        return False, "Could not find label titled 'breaking-change'."

    performance_label = next((l for l in labels if l.get("title") == "performance"), None)
    if performance_label is None:
        return False, "Could not find label titled 'performance'."

    issue_labels = issue.get("labels", [])

    if breaking_change_label.get("id") not in issue_labels:
        return False, f"Label 'breaking-change' (id: {breaking_change_label.get('id')}) is not in issue's labels."

    if performance_label.get("id") not in issue_labels:
        return False, f"Label 'performance' (id: {performance_label.get('id')}) is not in issue's labels."

    return True, "Both 'breaking-change' and 'performance' labels have been added to the container registry garbage collection issue."
