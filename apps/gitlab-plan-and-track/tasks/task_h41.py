import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find v4.2 - Security Hardening milestone
    ms = None
    for m in state.get("milestones", []):
        if m.get("title") == "v4.2 - Security Hardening":
            ms = m
            break
    if ms is None:
        return False, "Could not find milestone 'v4.2 - Security Hardening'."

    ms_id = ms["id"]

    # Get all open issues in this milestone
    issues = [i for i in state.get("issues", [])
              if i.get("milestoneId") == ms_id and i.get("status") == "open"]

    if len(issues) < 3:
        return False, f"Expected at least 3 open issues in Security Hardening milestone, found {len(issues)}."

    errors = []
    for issue in issues:
        title = issue.get("title", "?")
        if not issue.get("confidential"):
            errors.append(f"Issue '{title}' should be confidential.")
        hs = issue.get("healthStatus")
        # We can't know the original confidential state from current state,
        # so just verify every issue is confidential and has at_risk or needs_attention
        if hs not in ("at_risk", "needs_attention"):
            errors.append(f"Issue '{title}' health status is '{hs}', expected 'at_risk' or 'needs_attention'.")

    # Verify the specific breakdown based on seed data:
    # Originally confidential: CSP headers, vulnerable deps, CSRF token rotation -> at_risk
    # Originally not confidential: backup verification, branch protection, container registry -> needs_attention
    confidential_titles = [
        "Implement Content Security Policy headers",
        "Upgrade vulnerable dependencies identified in audit",
        "Implement CSRF token rotation",
    ]
    non_confidential_titles = [
        "Create automated backup verification system",
        "Add branch protection rules UI",
        "Implement container registry garbage collection",
    ]

    for title in confidential_titles:
        issue = None
        for i in issues:
            if i.get("title") == title:
                issue = i
                break
        if issue is None:
            continue
        if issue.get("healthStatus") != "at_risk":
            errors.append(f"Issue '{title}' (originally confidential) should have health 'at_risk', got '{issue.get('healthStatus')}'.")

    for title in non_confidential_titles:
        issue = None
        for i in issues:
            if i.get("title") == title:
                issue = i
                break
        if issue is None:
            continue
        if issue.get("healthStatus") != "needs_attention":
            errors.append(f"Issue '{title}' (originally not confidential) should have health 'needs_attention', got '{issue.get('healthStatus')}'.")
        if not issue.get("confidential"):
            errors.append(f"Issue '{title}' should have been made confidential.")

    if errors:
        return False, " ".join(errors)

    return True, f"All {len(issues)} issues in Security Hardening milestone updated with correct confidential and health status."
