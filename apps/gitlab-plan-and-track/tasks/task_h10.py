import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Check Sprint Board does NOT exist
    for board in state.get("boards", []):
        if board.get("name") == "Sprint Board":
            return False, "Board 'Sprint Board' still exists and should have been deleted."

    # Find board "Release Board"
    release_board = None
    for board in state.get("boards", []):
        if board.get("name") == "Release Board":
            release_board = board
            break
    if release_board is None:
        return False, "Could not find board 'Release Board'."

    # Find the three milestones
    v40_milestone = None
    v41_milestone = None
    v42_milestone = None
    for ms in state.get("milestones", []):
        title = ms.get("title", "")
        if "v4.0" in title and "Platform Redesign" in title:
            v40_milestone = ms
        elif "v4.1" in title and "Performance" in title:
            v41_milestone = ms
        elif "v4.2" in title and "Security Hardening" in title:
            v42_milestone = ms

    if v40_milestone is None:
        return False, "Could not find milestone 'v4.0 - Platform Redesign'."
    if v41_milestone is None:
        return False, "Could not find milestone 'v4.1 - Performance'."
    if v42_milestone is None:
        return False, "Could not find milestone 'v4.2 - Security Hardening'."

    expected_milestone_ids = {v40_milestone["id"], v41_milestone["id"], v42_milestone["id"]}

    # Check board has lists for all three milestones
    board_lists = release_board.get("lists", [])
    if len(board_lists) < 3:
        return False, f"Board 'Release Board' has only {len(board_lists)} list(s), expected at least 3."

    # Check each list has type == "milestone" and references the correct milestones
    milestone_list_ids = set()
    for lst in board_lists:
        if lst.get("type") == "milestone":
            ms_id = lst.get("milestoneId")
            if ms_id:
                milestone_list_ids.add(ms_id)

    missing_milestones = expected_milestone_ids - milestone_list_ids
    if missing_milestones:
        # Find which milestone titles are missing
        missing_titles = []
        for ms in state.get("milestones", []):
            if ms["id"] in missing_milestones:
                missing_titles.append(ms.get("title"))
        return False, f"Board 'Release Board' is missing milestone lists for: {missing_titles}"

    return True, "Board 'Sprint Board' deleted and 'Release Board' created with milestone lists for v4.0, v4.1, and v4.2."
