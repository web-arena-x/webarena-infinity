"""
Task H2: Update the Datadog alerts filter to also archive matching emails and
forward them to priya.sharma@cloudnine.dev instead of nate.patel@devops.tools.
Verify:
  - Filter with id='filter_10' (or criteria.from='alerts@datadog.com') has
    actions.archive=True and actions.forward='priya.sharma@cloudnine.dev'.
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    filters = state.get("filters", [])

    # Find filter by id or criteria.from
    target_filter = None
    for f in filters:
        if f.get("id") == "filter_10":
            target_filter = f
            break
        criteria = f.get("criteria", {})
        if criteria.get("from") == "alerts@datadog.com":
            target_filter = f
            break

    if target_filter is None:
        return False, "Filter for alerts@datadog.com (filter_10) not found."

    actions = target_filter.get("actions", {})
    errors = []

    if actions.get("archive") is not True:
        errors.append(
            f"actions.archive={actions.get('archive')!r}, expected True"
        )

    forward = actions.get("forward", "")
    if forward != "priya.sharma@cloudnine.dev":
        errors.append(
            f"actions.forward={forward!r}, expected 'priya.sharma@cloudnine.dev'"
        )

    if errors:
        return False, "Filter update incomplete: " + "; ".join(errors)

    return True, (
        "Filter for Datadog alerts now archives emails and forwards to "
        "priya.sharma@cloudnine.dev."
    )
