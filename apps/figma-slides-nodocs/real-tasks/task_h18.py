import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])
    pres_map = {p["id"]: p for p in presentations}

    if "pres_007" not in pres_map:
        return False, "pres_007 (Client Proposal — TechVentures Redesign) not found in state."

    p = pres_map["pres_007"]

    shared_with = p.get("shareSettings", {}).get("sharedWith", [])
    shared_ids = set(shared_with)

    # Should be exactly [user_001] (the creator)
    if shared_ids != {"user_001"}:
        extra = shared_ids - {"user_001"}
        missing = {"user_001"} - shared_ids
        parts = []
        if extra:
            parts.append(f"unexpected users still present: {extra}")
        if missing:
            parts.append(f"creator user_001 missing from sharedWith")
        return False, f"pres_007 sharedWith is not exactly [user_001]: {'; '.join(parts)} (found {shared_ids})"

    return True, "TechVentures Redesign sharedWith is exactly [user_001] (creator only)."
