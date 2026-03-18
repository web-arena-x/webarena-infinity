import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Create 'Cross-Team Status Update', share with All-Hands commenters."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    # Find the new presentation
    match = [p for p in presentations if p.get("title") == "Cross-Team Status Update"]
    if not match:
        return False, "No presentation titled 'Cross-Team Status Update' found."

    p = match[0]
    ss = p.get("shareSettings", {})
    errors = []

    # Check theme
    if p.get("theme") != "minimal":
        errors.append(f"theme is '{p.get('theme')}', expected 'minimal'")

    # Check tags
    tags = set(p.get("tags", []))
    for t in ["status", "update"]:
        if t not in tags:
            errors.append(f"missing tag '{t}'")

    # Commenters on All-Hands (pres_006):
    # cmt_014 (user_008), cmt_015 (user_007), cmt_016 (user_003),
    # cmt_031 (user_005), cmt_032 (user_004)
    expected_users = {"user_003", "user_004", "user_005", "user_007", "user_008"}
    shared = set(ss.get("sharedWith", []))

    missing = expected_users - shared
    if missing:
        errors.append(f"sharedWith missing All-Hands commenters: {missing}")

    if errors:
        return False, "; ".join(errors)

    return True, (
        "'Cross-Team Status Update' created with minimal theme, "
        "tags status+update, shared with all All-Hands commenters."
    )
