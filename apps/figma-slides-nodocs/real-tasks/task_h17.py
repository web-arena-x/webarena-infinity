import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    # Find "Design System Audit"
    audit_pres = None
    for p in presentations:
        if p.get("title", "").strip().lower() == "design system audit":
            audit_pres = p
            break

    if audit_pres is None:
        return False, "No presentation titled 'Design System Audit' found."

    errors = []

    # Check theme
    theme = audit_pres.get("theme")
    if theme != "creative":
        errors.append(f"theme is {theme!r}, expected 'creative'")

    # Check tags contain "design-system" and "audit"
    tags = audit_pres.get("tags", [])
    tags_lower = [t.lower() for t in tags]
    for required_tag in ["design-system", "audit"]:
        if required_tag not in tags_lower:
            errors.append(f"tag '{required_tag}' missing from tags: {tags}")

    # pres_013 (Mobile Design System Components) sharedWith:
    # [user_001, user_002, user_003, user_004, user_006, user_008]
    required_users = {"user_001", "user_002", "user_003", "user_004", "user_006", "user_008"}
    shared_with = audit_pres.get("shareSettings", {}).get("sharedWith", [])
    shared_ids = set(shared_with)

    missing_users = required_users - shared_ids
    if missing_users:
        errors.append(
            f"sharedWith missing users from Mobile Design System Components: {missing_users}"
        )

    if errors:
        return False, f"'Design System Audit' has issues: {'; '.join(errors)}"

    return True, "'Design System Audit' exists with creative theme, correct tags, and Mobile Design System members in sharedWith."
