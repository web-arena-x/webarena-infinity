import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])
    comments = state.get("comments", [])

    # Presentations with at least one unresolved comment (from seed data)
    should_be_starred = {
        "pres_001", "pres_002", "pres_003", "pres_004", "pres_005",
        "pres_006", "pres_007", "pres_008", "pres_009", "pres_010",
        "pres_012", "pres_013", "pres_016", "pres_018"
    }

    # Build a set of pres IDs that actually have unresolved comments in current state
    # (used to cross-check, but the task says "star every presentation with at least one
    # unresolved comment" based on seed knowledge)
    pres_with_unresolved = set()
    for c in comments:
        if not c.get("resolved", False):
            pid = c.get("presentationId") or c.get("presId")
            if pid:
                pres_with_unresolved.add(pid)

    pres_map = {p["id"]: p for p in presentations}
    errors = []

    for pid in should_be_starred:
        if pid not in pres_map:
            errors.append(f"{pid} not found in state")
        elif not pres_map[pid].get("starred", False):
            errors.append(f"{pid} ({pres_map[pid].get('title', pid)}) should be starred but is not")

    if errors:
        return False, f"Presentations with unresolved comments not starred: {errors}"

    return True, "All 14 presentations with unresolved comments are starred."
