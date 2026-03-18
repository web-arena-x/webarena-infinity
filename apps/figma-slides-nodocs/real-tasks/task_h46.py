import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Private-vis presentations: comments→team vis, no comments→delete."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])
    comments = state.get("comments", [])
    pres_map = {p["id"]: p for p in presentations}

    # Count comments per presentation
    comment_pres = set(c["presentationId"] for c in comments)

    errors = []

    # Private presentations with comments should now be team visibility:
    # pres_003, pres_007, pres_012, pres_016
    for pid in ["pres_003", "pres_007", "pres_012", "pres_016"]:
        if pid not in pres_map:
            errors.append(f"{pid} not found")
            continue
        p = pres_map[pid]
        vis = p.get("shareSettings", {}).get("visibility")
        if vis != "team":
            errors.append(
                f"{pid} ({p.get('title')}): had comments and private vis, "
                f"expected team vis, got '{vis}'"
            )

    # pres_017 (no comments, private) should be deleted
    if "pres_017" in pres_map:
        errors.append(
            f"pres_017 ({pres_map['pres_017'].get('title')}) should have been "
            f"deleted (private with no comments), but still exists"
        )

    if errors:
        return False, "; ".join(errors)

    return True, (
        "Private presentations with comments set to team visibility. "
        "Competitor Analysis Dashboard (no comments) deleted."
    )
