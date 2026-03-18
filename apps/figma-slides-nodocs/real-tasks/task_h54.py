import requests


def verify(server_url: str) -> tuple[bool, str]:
    """No-comments presentation: publish, team vis, enable comments+editing."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])
    pres_map = {p["id"]: p for p in presentations}

    # pres_017 (Competitor Analysis Dashboard) is the only presentation with no comments
    pid = "pres_017"
    if pid not in pres_map:
        return False, f"{pid} not found"

    p = pres_map[pid]
    ss = p.get("shareSettings", {})
    errors = []

    if p.get("status") != "published":
        errors.append(f"status is '{p.get('status')}', expected 'published'")

    if ss.get("visibility") != "team":
        errors.append(f"visibility is '{ss.get('visibility')}', expected 'team'")

    if not ss.get("allowComments"):
        errors.append("allowComments should be true")

    if not ss.get("allowEditing"):
        errors.append("allowEditing should be true")

    if errors:
        return False, f"pres_017 ({p.get('title')}): " + "; ".join(errors)

    return True, (
        "Competitor Analysis Dashboard (no comments) published, "
        "team visibility, comments and editing enabled."
    )
