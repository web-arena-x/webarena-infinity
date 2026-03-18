import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    james_pres = [p for p in presentations if p.get("createdBy") == "user_004"]

    if not james_pres:
        return False, "No presentations found with createdBy=='user_004' (James O'Brien)"

    not_starred = [p for p in james_pres if not p.get("starred", False)]
    if not_starred:
        titles = [p.get("title") for p in not_starred]
        return (
            False,
            f"The following presentations by James O'Brien are not starred: {titles}",
        )

    titles = [p.get("title") for p in james_pres]
    return (
        True,
        f"All {len(james_pres)} presentation(s) by James O'Brien are starred: {titles}",
    )
