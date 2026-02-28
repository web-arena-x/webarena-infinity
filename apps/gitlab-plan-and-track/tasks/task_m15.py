import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    epics = state.get("epics", [])
    epic = next((e for e in epics if e.get("title") == "Platform Redesign"), None)
    if epic is None:
        return False, "Could not find epic titled 'Platform Redesign'."

    labels = state.get("labels", [])
    ux_label = next((l for l in labels if l.get("title") == "UX"), None)
    if ux_label is None:
        return False, "Could not find label titled 'UX'."

    needs_discussion_label = next((l for l in labels if l.get("title") == "needs-discussion"), None)
    if needs_discussion_label is None:
        return False, "Could not find label titled 'needs-discussion'."

    epic_labels = epic.get("labels", [])

    if ux_label.get("id") in epic_labels:
        return False, f"Label 'UX' (id: {ux_label.get('id')}) should have been removed from 'Platform Redesign' epic but is still present."

    if needs_discussion_label.get("id") not in epic_labels:
        return False, f"Label 'needs-discussion' (id: {needs_discussion_label.get('id')}) should have been added to 'Platform Redesign' epic but is not present."

    return True, "Label 'UX' removed and 'needs-discussion' added to 'Platform Redesign' epic."
