import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find the board
    board = None
    for b in state.get("boards", []):
        if b.get("name") == "Security Overview":
            board = b
            break
    if board is None:
        return False, "Could not find board 'Security Overview'."

    # Find required labels
    label_map = {}
    for lbl in state.get("labels", []):
        if lbl["title"] in ("priority::critical", "priority::high", "security"):
            label_map[lbl["title"]] = lbl["id"]

    missing_labels = {"priority::critical", "priority::high", "security"} - set(label_map.keys())
    if missing_labels:
        return False, f"Missing labels in state: {missing_labels}"

    # Check board has 3 lists with correct labels
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

    return True, "Board 'Security Overview' created with lists for priority::critical, priority::high, and security."
