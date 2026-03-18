import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Elena's non-created access: add Priya, disable editing."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])
    pres_map = {p["id"]: p for p in presentations}

    # Elena (user_008) has access to but didn't create:
    # pres_002, pres_005, pres_006, pres_007, pres_013, pres_014
    # (She created pres_010)
    elena_access_not_created = [
        "pres_002", "pres_005", "pres_006", "pres_007", "pres_013", "pres_014"
    ]
    priya_id = "user_006"

    errors = []
    for pid in elena_access_not_created:
        if pid not in pres_map:
            errors.append(f"{pid} not found")
            continue
        p = pres_map[pid]
        ss = p.get("shareSettings", {})
        title = p.get("title", pid)

        shared = set(ss.get("sharedWith", []))
        if priya_id not in shared:
            errors.append(f"{pid} ({title}): Priya (user_006) not in sharedWith")

        if ss.get("allowEditing"):
            errors.append(f"{pid} ({title}): allowEditing should be false")

    if errors:
        return False, "; ".join(errors)

    return True, (
        "Priya added and editing disabled on all 6 presentations "
        "Elena has access to but didn't create."
    )
