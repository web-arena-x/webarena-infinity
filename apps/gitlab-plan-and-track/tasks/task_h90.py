import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # Find the renamed label (was 'blocked', now 'on-hold')
    onhold_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "on-hold":
            onhold_label = lbl
            break
    if onhold_label is None:
        return False, "Could not find label 'on-hold' (renamed from 'blocked')."

    # Verify old label is gone
    for lbl in state.get("labels", []):
        if lbl.get("title") == "blocked":
            errors.append("Old label 'blocked' still exists.")
            break

    # Check color
    if onhold_label.get("color", "").lower() != "#e67e22":
        errors.append(
            f"Label color is '{onhold_label.get('color')}', expected '#e67e22'."
        )

    # Check description
    if onhold_label.get("description") != "Temporarily paused pending external input":
        errors.append(
            f"Label description is '{onhold_label.get('description')}', "
            f"expected 'Temporarily paused pending external input'."
        )

    # Check CSRF token rotation issue has this label
    csrf_issue = None
    for i in state.get("issues", []):
        if i.get("title") == "Implement CSRF token rotation":
            csrf_issue = i
            break
    if csrf_issue is None:
        errors.append("Could not find issue 'Implement CSRF token rotation'.")
    elif onhold_label["id"] not in csrf_issue.get("labels", []):
        errors.append("CSRF token rotation issue missing 'on-hold' label.")

    if errors:
        return False, " ".join(errors)

    return True, (
        "Label renamed to 'on-hold' with color #e67e22 and updated description; "
        "applied to CSRF token rotation issue."
    )
