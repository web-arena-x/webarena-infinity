import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Archive the unstarred published presentation with the fewest shared users."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])
    pres_map = {p["id"]: p for p in presentations}

    # In seed data, pres_009 (Onboarding Training Module) is published,
    # unstarred, and has only 1 shared user (fewest among unstarred published)
    pid = "pres_009"
    if pid not in pres_map:
        return False, f"{pid} not found"

    p = pres_map[pid]
    if p.get("status") != "archived":
        return False, (
            f"pres_009 ({p.get('title')}): unstarred published with fewest shared "
            f"users (1) should be archived, got status=='{p.get('status')}'"
        )

    return True, (
        "Onboarding Training Module archived "
        "(unstarred published, fewest shared users)."
    )
