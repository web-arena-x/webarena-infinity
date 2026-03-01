import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    errors = []

    # Check Sprint Board deleted
    for b in state.get("boards", []):
        if b.get("name") == "Sprint Board":
            errors.append("Sprint Board still exists.")
            break

    # Check Bug Triage deleted
    for b in state.get("boards", []):
        if b.get("name") == "Bug Triage":
            errors.append("Bug Triage board still exists.")
            break

    # Find Unified Workflow board
    uw_board = None
    for b in state.get("boards", []):
        if b.get("name") == "Unified Workflow":
            uw_board = b
            break
    if uw_board is None:
        return False, "Could not find board 'Unified Workflow'. " + " ".join(errors)

    # Find workflow labels
    workflow_labels = {}
    for lbl in state.get("labels", []):
        title = lbl.get("title", "")
        if title in ("workflow::ready", "workflow::in-progress", "workflow::review", "workflow::done"):
            workflow_labels[title] = lbl["id"]

    if len(workflow_labels) < 4:
        errors.append("Could not find all 4 workflow labels.")

    # Check board has lists for all 4 workflow labels
    board_label_ids = set()
    for lst in uw_board.get("lists", []):
        if lst.get("type") == "label":
            board_label_ids.add(lst.get("labelId"))

    for title, lid in workflow_labels.items():
        if lid not in board_label_ids:
            errors.append(f"Board missing list for '{title}'.")

    if errors:
        return False, " ".join(errors)

    return True, "Sprint Board and Bug Triage deleted; 'Unified Workflow' board created with all 4 workflow label lists."
