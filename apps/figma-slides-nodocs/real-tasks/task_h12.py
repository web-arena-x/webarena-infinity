import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    # Find "Sprint 48 Planning"
    sprint48 = None
    for p in presentations:
        if p.get("title", "").strip().lower() == "sprint 48 planning":
            sprint48 = p
            break

    if sprint48 is None:
        return False, "No presentation titled 'Sprint 48 Planning' found."

    errors = []

    # Check theme
    theme = sprint48.get("theme")
    if theme != "minimal":
        errors.append(f"theme is {theme!r}, expected 'minimal'")

    # Check tags contain sprint, agile, planning
    tags = sprint48.get("tags", [])
    tags_lower = [t.lower() for t in tags]
    for required_tag in ["sprint", "agile", "planning"]:
        if required_tag not in tags_lower:
            errors.append(f"tag '{required_tag}' missing from tags: {tags}")

    # pres_014 (Sprint 47 retro) sharedWith=[user_001, user_002, user_003, user_004, user_008]
    required_users = {"user_001", "user_002", "user_003", "user_004", "user_008"}
    shared_with = sprint48.get("shareSettings", {}).get("sharedWith", [])
    shared_ids = set(shared_with)

    missing_users = required_users - shared_ids
    if missing_users:
        errors.append(f"sharedWith missing users from Sprint 47 retro: {missing_users}")

    if errors:
        return False, f"'Sprint 48 Planning' has issues: {'; '.join(errors)}"

    return True, "'Sprint 48 Planning' exists with minimal theme, correct tags, and Sprint 47 retro members in sharedWith."
