import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    sprint47_matches = [p for p in presentations if "Sprint 47" in p.get("title", "")]

    if len(sprint47_matches) < 2:
        titles = [p.get("title") for p in sprint47_matches]
        return (
            False,
            f"Expected at least 2 presentations matching 'Sprint 47' (original + duplicate), found {len(sprint47_matches)}: {titles}",
        )

    copy_indicators = ["copy", "Copy", "COPY", "(2)", " 2"]
    duplicate = next(
        (
            p for p in sprint47_matches
            if any(ind in p.get("title", "") for ind in copy_indicators)
        ),
        None,
    )
    if duplicate is None:
        titles = [p.get("title") for p in sprint47_matches]
        return (
            False,
            f"Could not identify a duplicate (copy) among Sprint 47 presentations: {titles}",
        )

    slide_count = duplicate.get("slideCount")
    if slide_count != 6:
        return (
            False,
            f"Expected duplicate slideCount==6, got {slide_count} for '{duplicate.get('title')}'",
        )

    return (
        True,
        f"Team Retrospective — Sprint 47 duplicated: found '{duplicate.get('title')}' with slideCount==6",
    )
