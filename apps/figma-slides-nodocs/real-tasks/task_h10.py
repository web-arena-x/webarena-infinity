import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    # Published presentations with team visibility in seed data
    # (pres_018 is team but draft — should NOT be changed)
    target_pres_ids = {
        "pres_001", "pres_004", "pres_005", "pres_008",
        "pres_010", "pres_011", "pres_014", "pres_015"
    }
    pres_map = {p["id"]: p for p in presentations}

    missing = []
    wrong_visibility = []

    for pid in target_pres_ids:
        if pid not in pres_map:
            missing.append(pid)
        else:
            p = pres_map[pid]
            vis = p.get("shareSettings", {}).get("visibility")
            if vis != "organization":
                wrong_visibility.append(
                    f"{pid} ({p.get('title', pid)}) has visibility={vis!r}"
                )

    if missing:
        return False, f"Presentations not found in state: {missing}"
    if wrong_visibility:
        return False, f"Published team presentations not updated to organization: {wrong_visibility}"

    # pres_018 (draft, team) should NOT have been changed to organization
    if "pres_018" in pres_map:
        p018 = pres_map["pres_018"]
        vis018 = p018.get("shareSettings", {}).get("visibility")
        if vis018 == "organization":
            return False, (
                "pres_018 (Design Workshop Materials) is a draft and should NOT have been "
                "changed to organization visibility."
            )

    return True, "All 8 published team-visibility presentations updated to organization visibility."
