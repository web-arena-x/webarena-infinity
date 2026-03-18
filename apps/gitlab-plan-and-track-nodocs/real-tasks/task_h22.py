import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find SAML issues
    saml_issues = [i for i in state["issues"] if "SAML" in i.get("title", "")]
    if len(saml_issues) < 2:
        return False, f"Expected at least 2 SAML issues, found {len(saml_issues)}."

    # Find the v2.0 API Overhaul milestone
    milestone = next((m for m in state["milestones"] if "v2.0" in m.get("title", "")), None)
    if milestone is None:
        return False, "Milestone 'v2.0 — API Overhaul' not found."

    # The SAML issue in v2.0 should be closed
    saml_v2 = next((i for i in saml_issues if i.get("milestoneId") == milestone["id"]), None)
    if saml_v2 is None:
        return False, "No SAML issue found in v2.0 milestone."

    if saml_v2.get("status") != "closed":
        return False, f"SAML issue #{saml_v2['id']} in v2.0 has status '{saml_v2.get('status')}', expected 'closed'."

    return True, f"SAML issue #{saml_v2['id']} in v2.0 milestone is closed."
