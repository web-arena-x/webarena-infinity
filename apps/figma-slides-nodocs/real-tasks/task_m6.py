import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    match = next(
        (p for p in presentations if p.get("title") == "Design Review Q1"),
        None,
    )
    if match is None:
        return False, "No presentation with title 'Design Review Q1' found"

    theme = match.get("theme", "")
    if theme != "creative":
        return False, f"Expected theme 'creative', got '{theme}'"

    tags = match.get("tags", [])
    required_tags = {"design", "review", "quarterly"}
    missing = required_tags - set(tags)
    if missing:
        return False, f"Missing tags {missing}, found tags: {tags}"

    return True, "Presentation 'Design Review Q1' created with creative theme and required tags"
