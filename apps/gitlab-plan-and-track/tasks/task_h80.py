import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # The two open issues with the most time spent:
    # issue_22 (Dark mode): 57600s (16h)
    # issue_7 (GraphQL gateway): 43200s (12h)
    expected_titles = [
        "Add dark mode support for the entire application",
        "Implement GraphQL gateway for v3 API",
    ]

    nd_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "needs-discussion":
            nd_label = lbl
            break
    if nd_label is None:
        return False, "Could not find 'needs-discussion' label."

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
        if issue.get("healthStatus") != "needs_attention":
            errors.append(
                f"Issue '{title}' health is '{issue.get('healthStatus')}', "
                f"expected 'needs_attention'."
            )
        if nd_label["id"] not in issue.get("labels", []):
            errors.append(f"Issue '{title}' missing 'needs-discussion' label.")

    if errors:
        return False, " ".join(errors)

    return True, "Top 2 time-spent issues set to needs_attention with needs-discussion label."
