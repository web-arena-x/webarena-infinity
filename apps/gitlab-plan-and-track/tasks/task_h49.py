import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Mobile App v2 epic
    mobile_epic = None
    for e in state.get("epics", []):
        if e.get("title") == "Mobile App v2":
            mobile_epic = e
            break
    if mobile_epic is None:
        return False, "Could not find epic 'Mobile App v2'."

    epic_id = mobile_epic["id"]

    # Find Priya Patel
    priya = None
    for u in state.get("users", []):
        if u.get("name") == "Priya Patel":
            priya = u
            break
    if priya is None:
        return False, "Could not find user 'Priya Patel'."

    priya_id = priya["id"]

    # Find design-needed label
    design_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "design-needed":
            design_label = lbl
            break
    if design_label is None:
        return False, "Could not find label 'design-needed'."

    # Find type::task label
    task_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "type::task":
            task_label = lbl
            break
    if task_label is None:
        return False, "Could not find label 'type::task'."

    errors = []

    # Check wireframes issue
    wireframes = None
    for i in state.get("issues", []):
        if i.get("title") == "Mobile app wireframes":
            wireframes = i
            break
    if wireframes is None:
        errors.append("Could not find issue 'Mobile app wireframes'.")
    else:
        if wireframes.get("epicId") != epic_id:
            errors.append("'Mobile app wireframes' not in Mobile App v2 epic.")
        if design_label["id"] not in wireframes.get("labels", []):
            errors.append("'Mobile app wireframes' missing 'design-needed' label.")
        if wireframes.get("weight") != 5:
            errors.append(f"'Mobile app wireframes' weight is {wireframes.get('weight')}, expected 5.")
        if priya_id not in wireframes.get("assignees", []):
            errors.append("'Mobile app wireframes' not assigned to Priya Patel.")

    # Check scaffolding issue
    scaffolding = None
    for i in state.get("issues", []):
        if i.get("title") == "React Native project scaffolding":
            scaffolding = i
            break
    if scaffolding is None:
        errors.append("Could not find issue 'React Native project scaffolding'.")
    else:
        if scaffolding.get("epicId") != epic_id:
            errors.append("'React Native project scaffolding' not in Mobile App v2 epic.")
        if task_label["id"] not in scaffolding.get("labels", []):
            errors.append("'React Native project scaffolding' missing 'type::task' label.")
        if scaffolding.get("weight") != 3:
            errors.append(f"'React Native project scaffolding' weight is {scaffolding.get('weight')}, expected 3.")
        if priya_id not in scaffolding.get("assignees", []):
            errors.append("'React Native project scaffolding' not assigned to Priya Patel.")

    if errors:
        return False, " ".join(errors)

    return True, "Both issues created in Mobile App v2 epic with correct labels, weights, and assignee."
