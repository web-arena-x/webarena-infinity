import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Presentations with exactly 2 comments: resolve all, star."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])
    comments = state.get("comments", [])
    pres_map = {p["id"]: p for p in presentations}

    # In seed data, presentations with exactly 2 comments:
    # pres_007 (cmt_017, cmt_036), pres_012 (cmt_022, cmt_039),
    # pres_013 (cmt_023, cmt_034), pres_016 (cmt_026, cmt_027)
    two_comment_pres = {"pres_007", "pres_012", "pres_013", "pres_016"}

    errors = []
    for pid in two_comment_pres:
        if pid not in pres_map:
            errors.append(f"{pid} not found")
            continue
        p = pres_map[pid]
        title = p.get("title", pid)

        # Should be starred
        if not p.get("starred"):
            errors.append(f"{pid} ({title}): should be starred")

        # All comments should be resolved
        pres_comments = [c for c in comments if c.get("presentationId") == pid]
        unresolved = [c for c in pres_comments if not c.get("resolved", False)]
        if unresolved:
            ids = [c.get("id") for c in unresolved]
            errors.append(f"{pid} ({title}): unresolved comments: {ids}")

    if errors:
        return False, "; ".join(errors)

    return True, (
        "All 4 presentations with exactly 2 comments: "
        "comments resolved and starred."
    )
