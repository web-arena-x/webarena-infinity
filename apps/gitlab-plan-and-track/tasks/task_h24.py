import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find the Component Board
    comp_board = None
    for board in state.get("boards", []):
        if board.get("name") == "Component Board":
            comp_board = board
            break
    if comp_board is None:
        return False, "Could not find board 'Component Board'."

    # Find all component labels
    component_labels = {}
    for lbl in state.get("labels", []):
        title = lbl.get("title", "")
        if title.startswith("component::"):
            component_labels[lbl["id"]] = title

    if len(component_labels) < 5:
        return False, f"Expected at least 5 component labels, found {len(component_labels)}."

    # Check board has lists for all component labels
    board_lists = comp_board.get("lists", [])
    if len(board_lists) < 5:
        return False, f"Board 'Component Board' has {len(board_lists)} lists, expected at least 5."

    # Collect label IDs from board lists
    board_label_ids = set()
    for lst in board_lists:
        if lst.get("type") == "label":
            lid = lst.get("labelId")
            if lid:
                board_label_ids.add(lid)

    missing = set(component_labels.keys()) - board_label_ids
    if missing:
        missing_names = [component_labels[lid] for lid in missing]
        return False, f"Board is missing lists for these component labels: {missing_names}"

    return True, "Board 'Component Board' created with lists for all 5 component labels."
