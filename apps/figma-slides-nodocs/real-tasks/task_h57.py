import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Duplicate the All-Hands, remove all shared users except Sarah Chen."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    # Find the duplicate by title
    dupes = [p for p in presentations
             if "copy" in p.get("title", "").lower()
             and "all-hands" in p.get("title", "").lower()]

    if not dupes:
        return False, "No duplicate of the All-Hands presentation found."

    errors = []
    dupe = dupes[0]
    shared = set(dupe.get("shareSettings", {}).get("sharedWith", []))

    # Should have only Sarah Chen (user_001)
    if "user_001" not in shared:
        errors.append("Sarah Chen (user_001) not in sharedWith")

    unexpected = shared - {"user_001"}
    if unexpected:
        errors.append(f"Unexpected users still in sharedWith: {unexpected}")

    if errors:
        return False, f"Duplicate '{dupe.get('title')}': " + "; ".join(errors)

    return True, (
        f"All-Hands duplicated as '{dupe.get('title')}'. "
        f"Shared users reduced to Sarah Chen only."
    )
