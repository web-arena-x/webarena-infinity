import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find the GraphQL gateway issue
    gql_issue = None
    for i in state.get("issues", []):
        if i.get("title") == "Implement GraphQL gateway for v3 API":
            gql_issue = i
            break
    if gql_issue is None:
        return False, "Could not find issue 'Implement GraphQL gateway for v3 API'."

    errors = []

    # Check time estimate is 40 hours (144000 seconds)
    if gql_issue.get("timeEstimate") != 144000:
        errors.append(
            f"Time estimate is {gql_issue.get('timeEstimate')}s, expected 144000s (40h)."
        )

    # Check timelogs: should have exactly one timelog of 16h with the right summary
    issue_timelogs = [t for t in state.get("timelogs", [])
                      if t.get("issueId") == gql_issue["id"]]

    if len(issue_timelogs) != 1:
        errors.append(
            f"Expected exactly 1 timelog, found {len(issue_timelogs)}."
        )
    else:
        tl = issue_timelogs[0]
        if tl.get("timeSpent") != 57600:
            errors.append(
                f"Timelog timeSpent is {tl.get('timeSpent')}s, expected 57600s (16h)."
            )
        if "complete rewrite estimate" not in tl.get("summary", "").lower():
            errors.append(
                f"Timelog summary is '{tl.get('summary')}', expected to contain "
                f"'Complete rewrite estimate'."
            )

    # Check timeSpent on the issue itself
    if gql_issue.get("timeSpent") != 57600:
        errors.append(
            f"Issue timeSpent is {gql_issue.get('timeSpent')}s, expected 57600s (16h)."
        )

    if errors:
        return False, " ".join(errors)

    return True, "GraphQL gateway issue: old timelogs deleted, new 16h entry added, estimate set to 40h."
