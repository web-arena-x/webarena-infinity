import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Check no label named "performance" exists
    for lbl in state.get("labels", []):
        if lbl.get("title") == "performance":
            return False, "Label 'performance' still exists (should be renamed to 'perf')."

    # Find the renamed label
    perf_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "perf":
            perf_label = lbl
            break
    if perf_label is None:
        return False, "Could not find label 'perf'."

    errors = []

    # Check color
    if perf_label.get("color") != "#0284c7":
        errors.append(f"Label color is '{perf_label.get('color')}', expected '#0284c7'.")

    # Check description
    if perf_label.get("description") != "Performance optimization work":
        errors.append(f"Label description is '{perf_label.get('description')}', expected 'Performance optimization work'.")

    if errors:
        return False, " ".join(errors)

    return True, "Label renamed to 'perf' with color #0284c7 and updated description."
