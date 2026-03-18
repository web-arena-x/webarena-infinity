import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    sarah_pres_ids = {"pres_001", "pres_003", "pres_006", "pres_007"}
    pres_map = {p["id"]: p for p in presentations}

    missing = []
    not_starred = []

    for pid in sarah_pres_ids:
        if pid not in pres_map:
            missing.append(pid)
        elif not pres_map[pid].get("starred", False):
            not_starred.append(pid)

    if missing:
        return False, f"Presentations not found in state: {missing}"
    if not_starred:
        titles = [pres_map[pid].get("title", pid) for pid in not_starred]
        return False, f"Sarah Chen's presentations not starred: {titles}"

    return True, "All 4 of Sarah Chen's presentations are starred."
