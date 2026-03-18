import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Archive the presentation that has the most comments."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])
    comments = state.get("comments", [])
    pres_map = {p["id"]: p for p in presentations}

    # Count comments per presentation
    from collections import Counter
    comment_counts = Counter(c["presentationId"] for c in comments)

    if not comment_counts:
        return False, "No comments found in state."

    max_count = max(comment_counts.values())
    most_commented = [pid for pid, cnt in comment_counts.items() if cnt == max_count]

    # pres_001 should have the most (6 comments in seed data)
    errors = []
    for pid in most_commented:
        if pid not in pres_map:
            errors.append(f"{pid} not found")
            continue
        p = pres_map[pid]
        if p.get("status") != "archived":
            errors.append(
                f"{pid} ({p.get('title')}) has {max_count} comments (most) "
                f"but status is '{p.get('status')}', expected 'archived'"
            )

    if errors:
        return False, "; ".join(errors)

    return True, (
        f"Presentation with the most comments ({max_count}) is archived."
    )
