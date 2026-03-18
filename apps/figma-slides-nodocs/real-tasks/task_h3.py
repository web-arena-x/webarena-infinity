import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    private_pres_ids = {"pres_003", "pres_007", "pres_012", "pres_016", "pres_017"}
    pres_map = {p["id"]: p for p in presentations}

    missing = []
    not_archived = []

    for pid in private_pres_ids:
        if pid not in pres_map:
            missing.append(pid)
        elif pres_map[pid].get("status") != "archived":
            not_archived.append(f"{pid} ({pres_map[pid].get('title', pid)}) has status={pres_map[pid].get('status')}")

    if missing:
        return False, f"Presentations not found in state: {missing}"
    if not_archived:
        return False, f"Private presentations not archived: {not_archived}"

    return True, "All 5 private-visibility presentations are archived."
