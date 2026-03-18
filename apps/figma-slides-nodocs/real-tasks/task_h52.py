import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Anika's fewest-slides pres: star it and share with All-Hands users."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])
    pres_map = {p["id"]: p for p in presentations}

    errors = []

    # Anika (user_003) created pres_004 (16), pres_011 (9), pres_018 (5)
    # Fewest slides: pres_018 (5 slides, Design Workshop Materials)
    pid = "pres_018"
    if pid not in pres_map:
        return False, "pres_018 not found"

    p = pres_map[pid]

    # Should be starred
    if not p.get("starred"):
        errors.append(f"pres_018 ({p.get('title')}): should be starred")

    # All-Hands (pres_006) has all 8 users in sharedWith
    all_hands_users = {
        "user_001", "user_002", "user_003", "user_004",
        "user_005", "user_006", "user_007", "user_008"
    }
    shared = set(p.get("shareSettings", {}).get("sharedWith", []))
    missing = all_hands_users - shared
    if missing:
        errors.append(
            f"pres_018 ({p.get('title')}): missing All-Hands users {missing}"
        )

    if errors:
        return False, "; ".join(errors)

    return True, (
        "Anika's fewest-slides presentation (Design Workshop Materials) "
        "starred and shared with all All-Hands users."
    )
