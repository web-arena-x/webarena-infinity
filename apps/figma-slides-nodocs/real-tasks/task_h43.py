import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Delete comments on James O'Brien's presentations, set private, disable editing."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])
    comments = state.get("comments", [])
    pres_map = {p["id"]: p for p in presentations}

    # James O'Brien (user_004) created: pres_005, pres_015, pres_016
    james_pres_ids = {"pres_005", "pres_015", "pres_016"}

    errors = []

    # No comments should remain on these presentations
    remaining = [c for c in comments if c.get("presentationId") in james_pres_ids]
    if remaining:
        ids = [c.get("id") for c in remaining]
        errors.append(f"Comments still present on James's presentations: {ids}")

    # Each should be private with editing disabled
    for pid in james_pres_ids:
        if pid not in pres_map:
            errors.append(f"{pid} not found")
            continue
        p = pres_map[pid]
        ss = p.get("shareSettings", {})
        title = p.get("title", pid)

        if ss.get("visibility") != "private":
            errors.append(f"{pid} ({title}): visibility is '{ss.get('visibility')}', expected 'private'")
        if ss.get("allowEditing"):
            errors.append(f"{pid} ({title}): allowEditing should be false")

    if errors:
        return False, "; ".join(errors)

    return True, (
        "All comments on James O'Brien's presentations deleted. "
        "All set to private visibility with editing disabled."
    )
