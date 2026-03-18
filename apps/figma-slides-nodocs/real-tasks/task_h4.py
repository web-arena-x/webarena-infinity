import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    # Elena Voronova (user_008) is in sharedWith of these presentations
    elena_pres_ids = {"pres_002", "pres_005", "pres_007", "pres_010", "pres_013", "pres_014"}
    pres_map = {p["id"]: p for p in presentations}

    missing = []
    wrong_visibility = []

    for pid in elena_pres_ids:
        if pid not in pres_map:
            missing.append(pid)
        else:
            p = pres_map[pid]
            vis = p.get("shareSettings", {}).get("visibility")
            if vis != "organization":
                wrong_visibility.append(f"{pid} ({p.get('title', pid)}) has visibility={vis!r}")

    if missing:
        return False, f"Presentations not found in state: {missing}"
    if wrong_visibility:
        return False, f"Presentations not set to organization visibility: {wrong_visibility}"

    return True, "All 6 presentations Elena has access to have organization visibility."
