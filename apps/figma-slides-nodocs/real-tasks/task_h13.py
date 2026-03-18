import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    comments = state.get("comments", [])

    # Sarah Chen is user_001; she authored these comments:
    sarah_comment_ids = {
        "cmt_006", "cmt_009", "cmt_010", "cmt_011", "cmt_019",
        "cmt_022", "cmt_025", "cmt_034", "cmt_035", "cmt_038"
    }

    # Check none of Sarah's comments remain
    remaining_sarah = [
        c.get("id", "?") for c in comments
        if c.get("id") in sarah_comment_ids
    ]
    if remaining_sarah:
        return False, f"Sarah Chen's comments still present (should be deleted): {remaining_sarah}"

    # Also check by authorId field in case IDs differ
    sarah_by_author = [
        c.get("id", "?") for c in comments
        if c.get("authorId") == "user_001" or c.get("userId") == "user_001"
        or (c.get("author") or {}).get("id") == "user_001"
    ]
    if sarah_by_author:
        return False, f"Comments authored by user_001 still present: {sarah_by_author}"

    expected_count = 30
    if len(comments) != expected_count:
        return False, (
            f"Expected {expected_count} comments after deleting Sarah's 10, "
            f"found {len(comments)}."
        )

    return True, "All 10 of Sarah Chen's comments deleted; 30 comments remain."
