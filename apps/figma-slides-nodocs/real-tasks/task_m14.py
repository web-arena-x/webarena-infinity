import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    match = next(
        (p for p in presentations if p.get("title") == "Investor Update March"),
        None,
    )
    if match is None:
        return False, "No presentation with title 'Investor Update March' found"

    theme = match.get("theme", "")
    if theme != "dark":
        return False, f"Expected theme 'dark', got '{theme}'"

    tags = match.get("tags", [])
    required_tags = {"investors", "update"}
    missing = required_tags - set(tags)
    if missing:
        return False, f"Missing tags {missing}, found tags: {tags}"

    return True, "Presentation 'Investor Update March' created with dark theme and required tags"
