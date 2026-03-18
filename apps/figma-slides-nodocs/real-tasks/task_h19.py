import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    # Organization-visibility presentations in seed data
    org_pres_ids = {"pres_002", "pres_006", "pres_009", "pres_013"}
    pres_map = {p["id"]: p for p in presentations}

    missing = []
    errors = []

    for pid in org_pres_ids:
        if pid not in pres_map:
            missing.append(pid)
            continue

        p = pres_map[pid]
        title = p.get("title", pid)

        ss = p.get("shareSettings", {})
        allow_comments = ss.get("allowComments")
        allow_editing = ss.get("allowEditing")

        if not allow_comments:
            errors.append(f"{pid} ({title}): allowComments is not true")
        if not allow_editing:
            errors.append(f"{pid} ({title}): allowEditing is not true")

    if missing:
        return False, f"Presentations not found in state: {missing}"
    if errors:
        return False, f"Organization-visibility presentations missing settings: {errors}"

    return True, "All 4 organization-visibility presentations have allowComments and allowEditing enabled."
