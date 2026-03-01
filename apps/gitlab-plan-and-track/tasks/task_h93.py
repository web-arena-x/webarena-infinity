import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # Bug Triage board should be deleted
    for b in state.get("boards", []):
        if b.get("name") == "Bug Triage":
            errors.append("Bug Triage board still exists.")
            break

    # Find Severity Board
    sev_board = None
    for b in state.get("boards", []):
        if b.get("name") == "Severity Board":
            sev_board = b
            break
    if sev_board is None:
        return False, "Could not find board 'Severity Board'. " + " ".join(errors)

    # Find priority labels
    crit_label = high_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "priority::critical":
            crit_label = lbl
        elif lbl.get("title") == "priority::high":
            high_label = lbl
    if crit_label is None:
        errors.append("Could not find 'priority::critical' label.")
    if high_label is None:
        errors.append("Could not find 'priority::high' label.")

    # Check board lists
    board_label_ids = set()
    for lst in sev_board.get("lists", []):
        if lst.get("type") == "label":
            board_label_ids.add(lst.get("labelId"))

    if crit_label and crit_label["id"] not in board_label_ids:
        errors.append("Severity Board missing list for 'priority::critical'.")
    if high_label and high_label["id"] not in board_label_ids:
        errors.append("Severity Board missing list for 'priority::high'.")

    if errors:
        return False, " ".join(errors)

    return True, (
        "Bug Triage board deleted; Severity Board created with "
        "priority::critical and priority::high lists."
    )
