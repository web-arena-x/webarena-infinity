import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Sarah's presentations: toggle David Kim in/out of shared users."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])
    pres_map = {p["id"]: p for p in presentations}

    david_id = "user_007"

    # Sarah (user_001) created: pres_001, pres_003, pres_006, pres_007
    # Seed state: pres_001 does NOT have David → should be added
    #             pres_003 does NOT have David → should be added
    #             pres_006 HAS David → should be removed
    #             pres_007 HAS David → should be removed
    expected = {
        "pres_001": True,   # David should now be present
        "pres_003": True,   # David should now be present
        "pres_006": False,  # David should now be absent
        "pres_007": False,  # David should now be absent
    }

    errors = []
    for pid, should_have_david in expected.items():
        if pid not in pres_map:
            errors.append(f"{pid} not found")
            continue
        p = pres_map[pid]
        shared = set(p.get("shareSettings", {}).get("sharedWith", []))
        has_david = david_id in shared
        title = p.get("title", pid)

        if should_have_david and not has_david:
            errors.append(f"{pid} ({title}): David Kim should be present but isn't")
        elif not should_have_david and has_david:
            errors.append(f"{pid} ({title}): David Kim should be removed but is still present")

    if errors:
        return False, "; ".join(errors)

    return True, (
        "David Kim toggled on Sarah's presentations: "
        "added where absent, removed where present."
    )
