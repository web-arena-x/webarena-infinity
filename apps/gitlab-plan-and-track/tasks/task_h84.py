import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # Issue about analyzing slow queries should have a 3-hour timelog
    slow_query_issue = None
    for i in state.get("issues", []):
        if i.get("title") == "Analyze and optimize slow queries from APM logs":
            slow_query_issue = i
            break
    if slow_query_issue is None:
        return False, "Could not find issue 'Analyze and optimize slow queries from APM logs'."

    # Check for timelog with summary 'Index optimization review' and 3h (10800s)
    found_timelog = False
    for tl in state.get("timelogs", []):
        if (
            tl.get("issueId") == slow_query_issue["id"]
            and tl.get("summary") == "Index optimization review"
        ):
            if tl.get("timeSpent") != 10800:
                errors.append(
                    f"Timelog 'Index optimization review' has timeSpent {tl.get('timeSpent')}, "
                    f"expected 10800 (3 hours)."
                )
            found_timelog = True
            break
    if not found_timelog:
        errors.append("No timelog with summary 'Index optimization review' found on slow queries issue.")

    # Issue about keyset pagination should have weight 8
    keyset_issue = None
    for i in state.get("issues", []):
        if i.get("title") == "Optimize issue list query to use keyset pagination":
            keyset_issue = i
            break
    if keyset_issue is None:
        return False, "Could not find issue 'Optimize issue list query to use keyset pagination'."

    if keyset_issue.get("weight") != 8:
        errors.append(
            f"Keyset pagination issue weight is {keyset_issue.get('weight')}, expected 8."
        )

    if errors:
        return False, " ".join(errors)

    return True, (
        "3-hour timelog added to slow queries issue; keyset pagination issue weight set to 8."
    )
