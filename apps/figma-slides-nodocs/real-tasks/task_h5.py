import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    # Viewers are user_005 (Yuki Tanaka) and user_007 (David Kim)
    viewer_ids = {"user_005", "user_007"}

    violations = []
    for p in presentations:
        shared_with = p.get("shareSettings", {}).get("sharedWith", [])
        shared_ids = set(shared_with)

        found_viewers = viewer_ids & shared_ids
        if found_viewers:
            violations.append(
                f"{p['id']} ({p.get('title', p['id'])}) still has viewers: {found_viewers}"
            )

    if violations:
        return False, f"Viewer IDs still present in sharedWith: {violations}"

    return True, "No viewer (user_005 or user_007) appears in any presentation's sharedWith."
