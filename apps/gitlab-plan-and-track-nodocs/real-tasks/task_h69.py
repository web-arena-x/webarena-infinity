import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    board = next((b for b in state["boards"] if b["name"] == "Development Board"), None)
    if board is None:
        return False, "Development Board not found."

    lists = board.get("lists", [])
    label_ids_on_board = {l.get("labelId") for l in lists if l.get("type") == "label"}

    # In Progress (labelId 16) should remain
    if 16 not in label_ids_on_board:
        return False, "In Progress list (labelId 16) missing from board."

    # To Do (15), Review (17), Done (18) should be removed
    for removed_id, name in [(15, "To Do"), (17, "Review"), (18, "Done")]:
        if removed_id in label_ids_on_board:
            return False, f"{name} list (labelId {removed_id}) still on board."

    # Bug (1) and security (5) lists should be added
    if 1 not in label_ids_on_board:
        return False, "Bug list (labelId 1) not found on board."
    if 5 not in label_ids_on_board:
        return False, "Security list (labelId 5) not found on board."

    return True, "Board updated: kept In Progress, removed To Do/Review/Done, added bug/security."
