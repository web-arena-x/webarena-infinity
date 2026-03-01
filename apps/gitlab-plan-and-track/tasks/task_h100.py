import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # Find 'in-review' label
    ir_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "in-review":
            ir_label = lbl
            break
    if ir_label is None:
        return False, "Could not find label 'in-review'."

    if ir_label.get("color", "").lower() != "#7b68ee":
        errors.append(
            f"Label color is '{ir_label.get('color')}', expected '#7b68ee'."
        )

    # Find 'Review Board'
    rv_board = None
    for b in state.get("boards", []):
        if b.get("name") == "Review Board":
            rv_board = b
            break
    if rv_board is None:
        return False, "Could not find board 'Review Board'. " + " ".join(errors)

    # Check board has list for 'in-review' label
    board_has_label = False
    for lst in rv_board.get("lists", []):
        if lst.get("type") == "label" and lst.get("labelId") == ir_label["id"]:
            board_has_label = True
            break
    if not board_has_label:
        errors.append("Review Board missing list for 'in-review' label.")

    # Check issues have the label
    expected_titles = [
        "Implement GraphQL gateway for v3 API",
        "Add dark mode support for the entire application",
    ]
    for title in expected_titles:
        issue = None
        for i in state.get("issues", []):
            if i.get("title") == title:
                issue = i
                break
        if issue is None:
            errors.append(f"Could not find issue '{title}'.")
            continue
        if ir_label["id"] not in issue.get("labels", []):
            errors.append(f"Issue '{title}' missing 'in-review' label.")

    if errors:
        return False, " ".join(errors)

    return True, (
        "Label 'in-review' created; Review Board created with list; "
        "GraphQL gateway and dark mode issues labeled."
    )
