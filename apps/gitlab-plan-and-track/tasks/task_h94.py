import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # The answer is Enterprise SSO Integration (most recently created open epic with no issues)
    epic = None
    for e in state.get("epics", []):
        if e.get("title") == "Enterprise SSO Integration":
            epic = e
            break
    if epic is None:
        return False, "Could not find epic 'Enterprise SSO Integration'."

    if epic.get("healthStatus") != "needs_attention":
        errors.append(
            f"Epic health is '{epic.get('healthStatus')}', expected 'needs_attention'."
        )

    if epic.get("startDate") != "2026-03-15":
        errors.append(
            f"Epic start date is '{epic.get('startDate')}', expected '2026-03-15'."
        )

    if errors:
        return False, " ".join(errors)

    return True, (
        "Enterprise SSO Integration epic updated with health 'needs_attention' "
        "and start date March 15, 2026."
    )
