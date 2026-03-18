import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    comments = state.get("comments", [])

    if not comments:
        return False, "No comments found in state — expected 40 comments to exist."

    unresolved = [c for c in comments if not c.get("resolved", False)]
    if unresolved:
        unresolved_ids = [c.get("id", "?") for c in unresolved]
        return False, f"{len(unresolved)} comment(s) still unresolved: {unresolved_ids}"

    return True, f"All {len(comments)} comments are resolved."
