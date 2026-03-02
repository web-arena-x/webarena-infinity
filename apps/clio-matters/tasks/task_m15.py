import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    matter = next(
        (m for m in state.get("matters", [])
         if "Blackwell" in m.get("description", "")
         and ("Divorce" in m.get("description", "")
              or "divorce" in m.get("description", "").lower()
              or "dissolution" in m.get("description", "").lower())),
        None
    )

    if matter is None:
        return False, "Could not find a matter with description containing 'Blackwell' and 'Divorce' or 'dissolution'."

    # Check blockedUsers contains user_5 (Priya Sharma)
    blocked_users = matter.get("blockedUsers", [])
    if "user_5" not in blocked_users:
        return False, f"Blackwell divorce matter blockedUsers does not contain 'user_5' (Priya Sharma). Current blockedUsers: {blocked_users}."

    # Check permissions type is restricted (specific or similar)
    permissions = matter.get("permissions", {})
    perm_type = permissions.get("type", "")
    if perm_type not in ("specific", "restricted", "group"):
        return False, f"Blackwell divorce matter permissions.type is '{perm_type}', expected 'specific' (or similar restricted type)."

    # Check permissions.groupIds contains group_2 (Family Law Division)
    group_ids = permissions.get("groupIds", [])
    if "group_2" not in group_ids:
        return False, f"Blackwell divorce matter permissions.groupIds does not contain 'group_2' (Family Law Division). Current groupIds: {group_ids}."

    return True, "Blackwell divorce matter has user_5 blocked, restricted permissions, and Family Law Division (group_2) access."
