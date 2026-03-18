import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    comments = state.get("comments", [])

    # Originally resolved: cmt_003, cmt_007, cmt_009, cmt_015, cmt_021,
    #                       cmt_024, cmt_025, cmt_031, cmt_035, cmt_039
    originally_resolved = {
        "cmt_003", "cmt_007", "cmt_009", "cmt_015", "cmt_021",
        "cmt_024", "cmt_025", "cmt_031", "cmt_035", "cmt_039"
    }

    comment_ids = {c.get("id") for c in comments}

    # None of the originally resolved comments should still exist
    still_present = originally_resolved & comment_ids
    if still_present:
        return False, f"Resolved comments still present (should be deleted): {still_present}"

    # All remaining comments should have resolved==false
    wrongly_resolved = [c.get("id", "?") for c in comments if c.get("resolved", False)]
    if wrongly_resolved:
        return False, f"Remaining comments have resolved=true (should be false): {wrongly_resolved}"

    expected_remaining = 30
    if len(comments) != expected_remaining:
        return False, (
            f"Expected {expected_remaining} remaining comments after deleting 10 resolved ones, "
            f"found {len(comments)}."
        )

    return True, "All 10 originally-resolved comments deleted; 30 unresolved comments remain."
