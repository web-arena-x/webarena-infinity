import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    labels = state.get("labels", [])

    old_label = next((l for l in labels if l.get("title") == "technical-debt"), None)
    if old_label is not None:
        return False, "Label 'technical-debt' still exists but should have been renamed to 'tech-debt'."

    new_label = next((l for l in labels if l.get("title") == "tech-debt"), None)
    if new_label is None:
        return False, "Could not find a label titled 'tech-debt'."

    if new_label.get("description") != "Legacy code requiring refactoring":
        return False, f"Expected description 'Legacy code requiring refactoring' but got '{new_label.get('description')}'."

    return True, "Label renamed from 'technical-debt' to 'tech-debt' with description 'Legacy code requiring refactoring'."
