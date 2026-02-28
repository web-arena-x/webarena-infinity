import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    boards = state.get("boards", [])
    board = next((b for b in boards if b.get("name") == "Priority Board"), None)
    if board is None:
        return False, "Could not find a board named 'Priority Board'."

    labels = state.get("labels", [])
    label = next((l for l in labels if l.get("title") == "priority::critical"), None)
    if label is None:
        return False, "Could not find label titled 'priority::critical'."

    board_lists = board.get("lists", [])
    matching_list = next(
        (bl for bl in board_lists if bl.get("type") == "label" and bl.get("labelId") == label.get("id")),
        None
    )

    if matching_list is None:
        return False, f"Board 'Priority Board' does not have a list with type 'label' and labelId matching 'priority::critical' (id: {label.get('id')})."

    return True, "Board 'Priority Board' created with a label list for 'priority::critical'."
