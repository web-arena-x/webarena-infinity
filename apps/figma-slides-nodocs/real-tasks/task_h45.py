import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Presentation not modified since January: share with Marcus+Anika, set team vis."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])
    pres_map = {p["id"]: p for p in presentations}

    # pres_012 (Q4 2025 Revenue Analysis) was last updated 2026-01-25
    pid = "pres_012"
    if pid not in pres_map:
        return False, f"{pid} not found"

    p = pres_map[pid]
    ss = p.get("shareSettings", {})
    errors = []

    # Check visibility is team
    if ss.get("visibility") != "team":
        errors.append(f"visibility is '{ss.get('visibility')}', expected 'team'")

    # Check Marcus Rivera (user_002) in sharedWith
    shared = set(ss.get("sharedWith", []))
    if "user_002" not in shared:
        errors.append("Marcus Rivera (user_002) not in sharedWith")
    if "user_003" not in shared:
        errors.append("Anika Patel (user_003) not in sharedWith")

    if errors:
        return False, f"pres_012 ({p.get('title')}): " + "; ".join(errors)

    return True, (
        "Q4 2025 Revenue Analysis (oldest update) shared with "
        "Marcus Rivera and Anika Patel, visibility set to team."
    )
