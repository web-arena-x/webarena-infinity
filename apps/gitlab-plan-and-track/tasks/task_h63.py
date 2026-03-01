import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # The milestone with "performance optimization" in description is v4.1
    ms_perf = None
    for m in state.get("milestones", []):
        if m.get("title") == "v4.1 - Performance":
            ms_perf = m
            break
    if ms_perf is None:
        return False, "Could not find milestone 'v4.1 - Performance'."

    # These issues were originally in v4.2 - Security Hardening (mentions "security audit")
    expected_titles = [
        "Implement Content Security Policy headers",
        "Upgrade vulnerable dependencies identified in audit",
        "Implement CSRF token rotation",
        "Create automated backup verification system",
        "Add branch protection rules UI",
        "Implement container registry garbage collection",
    ]

    errors = []
    for title in expected_titles:
        issue = None
        for i in state.get("issues", []):
            if i.get("title") == title:
                issue = i
                break
        if issue is None:
            errors.append(f"Could not find issue '{title}'.")
            continue
        if issue.get("milestoneId") != ms_perf["id"]:
            errors.append(
                f"Issue '{title}' has milestoneId '{issue.get('milestoneId')}', "
                f"expected '{ms_perf['id']}'."
            )

    # Verify no open issues remain in the security audit milestone
    ms_sec = None
    for m in state.get("milestones", []):
        if m.get("title") == "v4.2 - Security Hardening":
            ms_sec = m
            break
    if ms_sec is not None:
        remaining = [i for i in state.get("issues", [])
                     if i.get("milestoneId") == ms_sec["id"] and i.get("status") == "open"]
        if remaining:
            errors.append(
                f"{len(remaining)} open issues still in Security Hardening milestone."
            )

    if errors:
        return False, " ".join(errors)

    return True, f"All {len(expected_titles)} issues moved from Security Hardening to Performance milestone."
