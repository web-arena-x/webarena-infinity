import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    # pres_018 has 5 slides (fewest), pres_014 has 6 (second fewest)
    should_be_starred = {"pres_018", "pres_014"}

    errors = []
    for p in presentations:
        pid = p["id"]
        starred = p.get("starred", False)
        if pid in should_be_starred:
            if not starred:
                errors.append(f"{pid} ({p.get('title', pid)}) should be starred but is not")
        else:
            if starred:
                errors.append(f"{pid} ({p.get('title', pid)}) should NOT be starred but is")

    if errors:
        return False, "; ".join(errors)

    return True, "Only pres_018 and pres_014 are starred; all others are unstarred."
