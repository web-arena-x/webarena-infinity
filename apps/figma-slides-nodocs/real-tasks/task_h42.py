import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Team-vis presentations: starred→organization, not starred→private."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])
    pres_map = {p["id"]: p for p in presentations}

    # In seed data, these presentations have team visibility:
    # pres_001 (starred), pres_004, pres_005, pres_008, pres_010 (starred),
    # pres_011, pres_014, pres_015, pres_018
    team_vis_seed = {
        "pres_001": True,   # starred
        "pres_004": False,
        "pres_005": False,
        "pres_008": False,
        "pres_010": True,   # starred
        "pres_011": False,
        "pres_014": False,
        "pres_015": False,
        "pres_018": False,
    }

    errors = []
    for pid, was_starred in team_vis_seed.items():
        if pid not in pres_map:
            errors.append(f"{pid} not found")
            continue
        p = pres_map[pid]
        vis = p.get("shareSettings", {}).get("visibility")
        expected = "organization" if was_starred else "private"
        if vis != expected:
            errors.append(
                f"{pid} ({p.get('title')}): expected visibility '{expected}' "
                f"(was {'starred' if was_starred else 'not starred'}), got '{vis}'"
            )

    if errors:
        return False, "; ".join(errors)

    return True, (
        "All 9 team-visible presentations updated: "
        "starred ones → organization, unstarred → private."
    )
