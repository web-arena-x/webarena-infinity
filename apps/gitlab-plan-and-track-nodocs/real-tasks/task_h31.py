import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    issue60 = next((i for i in state["issues"] if i["id"] == 60), None)
    if issue60 is None:
        return False, "Issue #60 not found."

    # Should be assigned to Tom Ramirez (id 6) — same as CDN config issue #13
    if 6 not in issue60.get("assigneeIds", []):
        return False, f"Tom Ramirez (id 6) not in assigneeIds for issue #60: {issue60.get('assigneeIds')}."

    # Should have weight 5 — same as CDN config issue #13
    if issue60.get("weight") != 5:
        return False, f"Issue #60 weight is {issue60.get('weight')}, expected 5."

    # Should be in Sprint 7
    sprint7 = next((it for it in state["iterations"] if it.get("title") == "Sprint 7"), None)
    if sprint7 is None:
        return False, "Sprint 7 not found."
    if issue60.get("iterationId") != sprint7["id"]:
        return False, f"Issue #60 iterationId is {issue60.get('iterationId')}, expected {sprint7['id']}."

    # Should have performance label (id 4)
    perf_label = next((l for l in state["labels"] if l["name"] == "performance"), None)
    if perf_label is None:
        return False, "Label 'performance' not found."
    if perf_label["id"] not in issue60.get("labelIds", []):
        return False, f"Issue #60 missing performance label. Labels: {issue60.get('labelIds')}."

    return True, "Issue #60 assigned to Tom Ramirez, weight 5, Sprint 7, with performance label."
