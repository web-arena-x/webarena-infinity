import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # Find v4.2 - Security Hardening milestone
    sec_ms = None
    for m in state.get("milestones", []):
        if m.get("title") == "v4.2 - Security Hardening":
            sec_ms = m
            break
    if sec_ms is None:
        return False, "Could not find milestone 'v4.2 - Security Hardening'."

    # Find priority::high label
    high_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "priority::high":
            high_label = lbl
            break
    if high_label is None:
        return False, "Could not find 'priority::high' label."

    # Check both issues
    expected_titles = [
        "Implement two-factor authentication with TOTP",
        "Migrate user authentication from sessions to JWT",
    ]

    for title in expected_titles:
        issue = None
        for i in state.get("issues", []):
            if i.get("title") == title:
                issue = i
                break
        if issue is None:
            errors.append(f"Could not find issue '{title}'.")
            continue
        if issue.get("milestoneId") != sec_ms["id"]:
            errors.append(
                f"Issue '{title}' milestoneId is '{issue.get('milestoneId')}', "
                f"expected '{sec_ms['id']}'."
            )
        if high_label["id"] not in issue.get("labels", []):
            errors.append(f"Issue '{title}' missing 'priority::high' label.")

    if errors:
        return False, " ".join(errors)

    return True, (
        "2FA and JWT migration issues moved to v4.2 - Security Hardening "
        "with priority::high label."
    )
