import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    presentations = state.get("presentations", [])
    draft_presentations = [p for p in presentations if p.get("status") == "draft"]

    if not draft_presentations:
        return False, "No presentations with status 'draft' found in state."

    unstarred = []
    for p in draft_presentations:
        if p.get("starred") is not True:
            unstarred.append(f"{p.get('id')} ({p.get('title')})")

    if unstarred:
        return False, f"The following draft presentations are not starred: {', '.join(unstarred)}"

    draft_ids = [f"{p.get('id')} ({p.get('title')})" for p in draft_presentations]
    return True, f"All draft presentations are starred: {', '.join(draft_ids)}"
