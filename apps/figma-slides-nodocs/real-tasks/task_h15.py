import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    # Viewers: user_005 (Yuki Tanaka), user_007 (David Kim)
    # user_005 created: pres_012, pres_017
    # user_007 created: pres_009
    viewer_created_pres = {"pres_009", "pres_012", "pres_017"}
    pres_map = {p["id"]: p for p in presentations}

    missing = []
    not_archived = []

    for pid in viewer_created_pres:
        if pid not in pres_map:
            missing.append(pid)
        elif pres_map[pid].get("status") != "archived":
            p = pres_map[pid]
            not_archived.append(
                f"{pid} ({p.get('title', pid)}) has status={p.get('status')!r}"
            )

    if missing:
        return False, f"Presentations not found in state: {missing}"
    if not_archived:
        return False, f"Viewer-created presentations not archived: {not_archived}"

    return True, "All 3 presentations created by viewers (pres_009, pres_012, pres_017) are archived."
