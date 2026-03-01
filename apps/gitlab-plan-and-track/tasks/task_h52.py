import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Check board exists
    perf_board = None
    for b in state.get("boards", []):
        if b.get("name") == "Performance Tracker":
            perf_board = b
            break
    if perf_board is None:
        return False, "Could not find board 'Performance Tracker'."

    # Check board lists
    lbl_crit = None
    lbl_high = None
    lbl_med = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "priority::critical":
            lbl_crit = lbl
        elif lbl.get("title") == "priority::high":
            lbl_high = lbl
        elif lbl.get("title") == "priority::medium":
            lbl_med = lbl

    if not all([lbl_crit, lbl_high, lbl_med]):
        return False, "Could not find one or more priority labels."

    errors = []

    board_label_ids = set()
    for lst in perf_board.get("lists", []):
        if lst.get("type") == "label":
            board_label_ids.add(lst.get("labelId"))

    for expected_lbl, name in [(lbl_crit, "priority::critical"), (lbl_high, "priority::high"), (lbl_med, "priority::medium")]:
        if expected_lbl["id"] not in board_label_ids:
            errors.append(f"Board missing list for '{name}'.")

    # Find v4.1 milestone
    ms_v41 = None
    for m in state.get("milestones", []):
        if m.get("title") == "v4.1 - Performance":
            ms_v41 = m
            break
    if ms_v41 is None:
        return False, "Could not find milestone 'v4.1 - Performance'."

    # Find performance label
    perf_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "performance":
            perf_label = lbl
            break
    if perf_label is None:
        return False, "Could not find label 'performance'."

    perf_id = perf_label["id"]
    high_id = lbl_high["id"]

    # Check all open issues in v4.1 with performance label have priority::high
    perf_issues = [i for i in state.get("issues", [])
                   if i.get("milestoneId") == ms_v41["id"]
                   and i.get("status") == "open"
                   and perf_id in i.get("labels", [])]

    if len(perf_issues) < 3:
        errors.append(f"Expected at least 3 performance issues in v4.1, found {len(perf_issues)}.")

    for issue in perf_issues:
        if high_id not in issue.get("labels", []):
            errors.append(f"Issue '{issue.get('title')}' missing 'priority::high' label.")

    if errors:
        return False, " ".join(errors)

    return True, f"Board 'Performance Tracker' created and priority::high applied to {len(perf_issues)} performance issues."
