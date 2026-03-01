import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Check Bug Triage board is gone
    for b in state.get("boards", []):
        if b.get("name") == "Bug Triage":
            return False, "Board 'Bug Triage' still exists."

    # Find Team Workload board
    board = None
    for b in state.get("boards", []):
        if b.get("name") == "Team Workload":
            board = b
            break
    if board is None:
        return False, "Could not find board 'Team Workload'."

    # Find required labels
    label_map = {}
    for lbl in state.get("labels", []):
        if lbl["title"] in ("workflow::ready", "workflow::in-progress", "workflow::review"):
            label_map[lbl["title"]] = lbl["id"]

    missing = {"workflow::ready", "workflow::in-progress", "workflow::review"} - set(label_map.keys())
    if missing:
        return False, f"Missing labels: {missing}"

    # Check board has lists for all 3 labels
    lists = board.get("lists", [])
    if len(lists) < 3:
        return False, f"Board has {len(lists)} lists, expected at least 3."

    list_label_ids = {lst.get("labelId") for lst in lists if lst.get("type") == "label"}
    errors = []
    for title, lid in label_map.items():
        if lid not in list_label_ids:
            errors.append(f"No list found for label '{title}'.")

    if errors:
        return False, " ".join(errors)

    return True, "Bug Triage deleted. Team Workload board created with workflow::ready, in-progress, and review lists."
