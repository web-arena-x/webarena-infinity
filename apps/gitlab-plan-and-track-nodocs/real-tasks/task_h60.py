import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # #48 should be removed from API v3 Migration epic
    api_epic = next((e for e in state["epics"] if "API v3 Migration" in e.get("title", "")), None)
    if api_epic is None:
        return False, "API v3 Migration epic not found."
    if 48 in api_epic.get("childIssueIds", []):
        return False, f"Issue #48 still in API v3 Migration epic childIssueIds: {api_epic.get('childIssueIds')}."

    # New epic 'API Documentation' should exist
    doc_epic = next((e for e in state["epics"] if e.get("title") == "API Documentation"), None)
    if doc_epic is None:
        return False, "Epic 'API Documentation' not found."

    # Should have documentation label (3)
    if 3 not in doc_epic.get("labels", []):
        return False, f"Epic 'API Documentation' missing documentation label (id 3). Labels: {doc_epic.get('labels')}."

    # Should have #43 and #48 as children
    for issue_id in [43, 48]:
        if issue_id not in doc_epic.get("childIssueIds", []):
            return False, f"Issue #{issue_id} not in 'API Documentation' epic childIssueIds: {doc_epic.get('childIssueIds')}."

    return True, "Issue #48 moved from API v3 epic; new 'API Documentation' epic created with #43 and #48."
