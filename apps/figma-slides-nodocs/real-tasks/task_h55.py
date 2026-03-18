import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Presentations with both resolved+unresolved comments: delete resolved, star."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])
    comments = state.get("comments", [])
    pres_map = {p["id"]: p for p in presentations}

    # Seed presentations with both resolved and unresolved comments:
    # pres_001: resolved [cmt_003], unresolved [cmt_001,002,004,005,029]
    # pres_002: resolved [cmt_007], unresolved [cmt_006,008,030]
    # pres_003: resolved [cmt_009,035], unresolved [cmt_010]
    # pres_006: resolved [cmt_015,031], unresolved [cmt_014,016,032]
    # pres_012: resolved [cmt_039], unresolved [cmt_022]
    mixed_pres = {"pres_001", "pres_002", "pres_003", "pres_006", "pres_012"}

    # Resolved comments that should be deleted
    deleted_ids = {"cmt_003", "cmt_007", "cmt_009", "cmt_035", "cmt_015", "cmt_031", "cmt_039"}

    errors = []

    # Check no deleted comments remain
    remaining_deleted = [c for c in comments if c.get("id") in deleted_ids]
    if remaining_deleted:
        ids = [c.get("id") for c in remaining_deleted]
        errors.append(f"Resolved comments that should be deleted still present: {ids}")

    # Check each mixed presentation is starred
    for pid in mixed_pres:
        if pid not in pres_map:
            errors.append(f"{pid} not found")
            continue
        p = pres_map[pid]
        if not p.get("starred"):
            errors.append(f"{pid} ({p.get('title')}): should be starred")

    # Remaining comments on these presentations should all be unresolved
    for c in comments:
        if c.get("presentationId") in mixed_pres and c.get("resolved"):
            errors.append(
                f"{c.get('id')} on {c.get('presentationId')}: "
                f"should not be resolved (only unresolved should remain)"
            )

    if errors:
        return False, "; ".join(errors)

    return True, (
        "Resolved comments deleted from 5 presentations with mixed comment states. "
        "All 5 starred."
    )
