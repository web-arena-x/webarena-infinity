import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Analysis-tagged: resolve comments, team vis, add Elena Voronova."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])
    comments = state.get("comments", [])
    pres_map = {p["id"]: p for p in presentations}

    # Tagged 'analysis': pres_012 (Q4 Revenue Analysis), pres_017 (Competitor Analysis)
    analysis_pres = {"pres_012", "pres_017"}
    elena_id = "user_008"

    errors = []
    for pid in analysis_pres:
        if pid not in pres_map:
            errors.append(f"{pid} not found")
            continue
        p = pres_map[pid]
        ss = p.get("shareSettings", {})
        title = p.get("title", pid)

        # Visibility should be team
        if ss.get("visibility") != "team":
            errors.append(f"{pid} ({title}): visibility '{ss.get('visibility')}', expected 'team'")

        # Elena should be in sharedWith
        if elena_id not in set(ss.get("sharedWith", [])):
            errors.append(f"{pid} ({title}): Elena (user_008) not in sharedWith")

        # All comments should be resolved
        pres_comments = [c for c in comments if c.get("presentationId") == pid]
        unresolved = [c for c in pres_comments if not c.get("resolved", False)]
        if unresolved:
            ids = [c.get("id") for c in unresolved]
            errors.append(f"{pid} ({title}): unresolved comments: {ids}")

    if errors:
        return False, "; ".join(errors)

    return True, (
        "Both analysis-tagged presentations: comments resolved, "
        "team visibility, Elena added."
    )
