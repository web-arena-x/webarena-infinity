import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    errors = []

    # Sprint Board should be deleted
    for b in state.get("boards", []):
        if b.get("name") == "Sprint Board":
            errors.append("Sprint Board still exists.")
            break

    # Find 'Milestone Tracker' board
    mt_board = None
    for b in state.get("boards", []):
        if b.get("name") == "Milestone Tracker":
            mt_board = b
            break
    if mt_board is None:
        return False, "Could not find board 'Milestone Tracker'. " + " ".join(errors)

    # The three active milestones with earliest start dates:
    # ms_1 (v4.0, 2025-12-01), ms_7 (Q1 2026, 2026-01-01), ms_2 (v4.1, 2026-03-01)
    expected_ms_titles = [
        "v4.0 - Platform Redesign",
        "Q1 2026 Planning",
        "v4.1 - Performance",
    ]
    expected_ms_ids = set()
    for title in expected_ms_titles:
        for m in state.get("milestones", []):
            if m.get("title") == title:
                expected_ms_ids.add(m["id"])
                break

    if len(expected_ms_ids) < 3:
        errors.append("Could not find all 3 expected milestones.")

    # Check board lists contain these milestones
    board_ms_ids = set()
    for lst in mt_board.get("lists", []):
        if lst.get("type") == "milestone":
            board_ms_ids.add(lst.get("milestoneId"))

    for ms_id in expected_ms_ids:
        if ms_id not in board_ms_ids:
            # Find title for error message
            ms_title = ms_id
            for m in state.get("milestones", []):
                if m["id"] == ms_id:
                    ms_title = m["title"]
                    break
            errors.append(f"Board missing milestone list for '{ms_title}'.")

    if errors:
        return False, " ".join(errors)

    return True, "Sprint Board deleted; 'Milestone Tracker' created with 3 earliest-start milestone lists."
