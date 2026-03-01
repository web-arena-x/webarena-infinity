import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # Find the GraphQL gateway issue
    gql_issue = None
    for i in state.get("issues", []):
        if i.get("title") == "Implement GraphQL gateway for v3 API":
            gql_issue = i
            break
    if gql_issue is None:
        return False, "Could not find issue 'Implement GraphQL gateway for v3 API'."

    # Check that the snoozed todo about this issue is now pending
    gql_todo = None
    for t in state.get("todos", []):
        if t.get("targetId") == gql_issue["id"] and t.get("action") == "review_requested":
            gql_todo = t
            break
    if gql_todo is None:
        errors.append("Could not find the review_requested todo for GraphQL gateway.")
    elif gql_todo.get("status") != "pending":
        errors.append(
            f"GraphQL gateway todo status is '{gql_todo.get('status')}', expected 'pending'."
        )

    # Check for the new timelog
    found_timelog = False
    for tl in state.get("timelogs", []):
        if (
            tl.get("issueId") == gql_issue["id"]
            and tl.get("summary") == "Schema optimization review"
        ):
            if tl.get("timeSpent") != 7200:
                errors.append(
                    f"Timelog timeSpent is {tl.get('timeSpent')}, expected 7200 (2 hours)."
                )
            found_timelog = True
            break
    if not found_timelog:
        errors.append("No timelog with summary 'Schema optimization review' found on GraphQL gateway issue.")

    if errors:
        return False, " ".join(errors)

    return True, (
        "GraphQL gateway todo restored to pending; "
        "2-hour timelog added with summary 'Schema optimization review'."
    )
