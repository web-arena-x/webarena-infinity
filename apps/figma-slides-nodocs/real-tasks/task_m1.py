import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    match = next(
        (p for p in presentations if p.get("title") == "Q2 Planning Session"),
        None,
    )
    if match is None:
        return False, "No presentation with title 'Q2 Planning Session' found"

    desc = match.get("description", "")
    if desc != "Quarterly planning for Q2 2026":
        return (
            False,
            f"Expected description 'Quarterly planning for Q2 2026', got '{desc}'",
        )

    theme = match.get("theme", "")
    if theme != "corporate":
        return False, f"Expected theme 'corporate', got '{theme}'"

    return True, "Presentation 'Q2 Planning Session' created with correct description and corporate theme"
