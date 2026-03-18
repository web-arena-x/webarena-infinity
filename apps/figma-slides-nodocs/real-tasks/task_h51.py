import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Merge shared users of Marketing Campaign and Accessibility Audit."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])
    pres_map = {p["id"]: p for p in presentations}

    errors = []

    # Seed sharedWith:
    # Marketing Campaign (pres_010): [user_001, user_002, user_008]
    # Accessibility Audit (pres_011): [user_001, user_003, user_004]
    # Union: {user_001, user_002, user_003, user_004, user_008}
    expected_union = {"user_001", "user_002", "user_003", "user_004", "user_008"}

    for pid, title in [("pres_010", "Marketing Campaign"),
                       ("pres_011", "Accessibility Audit Results")]:
        if pid not in pres_map:
            errors.append(f"{pid} not found")
            continue
        p = pres_map[pid]
        shared = set(p.get("shareSettings", {}).get("sharedWith", []))
        missing = expected_union - shared
        if missing:
            errors.append(
                f"{pid} ({p.get('title')}): missing users {missing}"
            )

    if errors:
        return False, "; ".join(errors)

    return True, (
        "Marketing Campaign and Accessibility Audit Results both have "
        "the combined set of shared users."
    )
