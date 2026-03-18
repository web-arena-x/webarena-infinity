import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    # Find a presentation titled "Team Showcase"
    showcase = None
    for p in presentations:
        if p.get("title", "").strip().lower() == "team showcase":
            showcase = p
            break

    if showcase is None:
        return False, "No presentation titled 'Team Showcase' found."

    errors = []

    # Check theme
    theme = showcase.get("theme")
    if theme != "warm":
        errors.append(f"theme is {theme!r}, expected 'warm'")

    # Check tags contain "team" and "showcase"
    tags = showcase.get("tags", [])
    tags_lower = [t.lower() for t in tags]
    if "team" not in tags_lower:
        errors.append(f"tag 'team' missing from tags: {tags}")
    if "showcase" not in tags_lower:
        errors.append(f"tag 'showcase' missing from tags: {tags}")

    # Check sharedWith contains all editors: user_002, user_003, user_004, user_006, user_008
    # and user_001 (creator)
    required_users = {"user_001", "user_002", "user_003", "user_004", "user_006", "user_008"}
    shared_with = showcase.get("shareSettings", {}).get("sharedWith", [])
    shared_ids = set(shared_with)

    missing_users = required_users - shared_ids
    if missing_users:
        errors.append(f"sharedWith is missing users: {missing_users}")

    if errors:
        return False, f"'Team Showcase' has issues: {'; '.join(errors)}"

    return True, "'Team Showcase' exists with warm theme, correct tags, and all editors in sharedWith."
