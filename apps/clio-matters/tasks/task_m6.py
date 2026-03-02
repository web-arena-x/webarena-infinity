import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    matter = next(
        (m for m in state.get("matters", [])
         if "Johnson" in m.get("description", "") and "Whole Foods" in m.get("description", "")),
        None
    )

    if matter is None:
        return False, "Could not find a matter with description containing 'Johnson' and 'Whole Foods'."

    permissions = matter.get("permissions", {})
    perm_type = permissions.get("type", "")

    if perm_type not in ("specific", "group"):
        return False, (
            f"Johnson v. Whole Foods permissions type is '{perm_type}', "
            f"expected 'specific' or 'group'."
        )

    group_ids = permissions.get("groupIds", [])
    if "group_1" not in group_ids:
        return False, (
            f"Johnson v. Whole Foods permissions groupIds is {group_ids}, "
            f"expected it to contain 'group_1' (Litigation Team)."
        )

    return True, "Johnson v. Whole Foods permissions restricted to Litigation Team."
