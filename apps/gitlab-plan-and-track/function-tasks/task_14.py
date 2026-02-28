import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    issues = state.get("issues", [])
    milestones = state.get("milestones", [])

    target = next((i for i in issues if i["title"] == "File upload fails silently for files > 50MB"), None)
    if not target:
        return False, "Issue 'File upload fails silently for files > 50MB' not found."

    security_ms = next((m for m in milestones if m["title"] == "v4.2 - Security Hardening"), None)
    if not security_ms:
        return False, "Milestone 'v4.2 - Security Hardening' not found in state."

    if target.get("milestoneId") != security_ms["id"]:
        return False, f"Issue milestoneId is '{target.get('milestoneId')}', expected '{security_ms['id']}' (v4.2 - Security Hardening)."

    return True, "Issue 'File upload fails silently for files > 50MB' is assigned to milestone 'v4.2 - Security Hardening'."
