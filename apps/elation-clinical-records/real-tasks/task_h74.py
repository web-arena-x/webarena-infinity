import requests
from collections import Counter


def verify(server_url: str) -> tuple[bool, str]:
    """Most-used template duplicated as 'High-Volume Visit', assigned to Follow-Up appointment."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Check 'High-Volume Visit' template exists
    hv_tmpl = None
    for t in state.get("visitNoteTemplates", []):
        if t.get("name") == "High-Volume Visit":
            hv_tmpl = t
            break
    if not hv_tmpl:
        return False, "Template 'High-Volume Visit' not found."

    # The most-used template should be E* Annual Wellness Visit (used by 2 notes)
    # Verify the duplicate has similar content
    orig = None
    for t in state.get("visitNoteTemplates", []):
        if t.get("name") == "E* Annual Wellness Visit":
            orig = t
            break
    if orig:
        orig_content = orig.get("content", {})
        hv_content = hv_tmpl.get("content", {})
        # Check at least the HPI section matches
        if orig_content.get("hpi") and not hv_content.get("hpi"):
            errors.append("'High-Volume Visit' should have HPI content from the original template.")

    # Check Follow-Up appointment uses the duplicate
    followup = None
    for apt in state.get("appointmentTypes", []):
        if apt.get("name") == "Follow-Up":
            followup = apt
            break
    if not followup:
        errors.append("Follow-Up appointment type not found.")
    elif followup.get("noteTemplate") != hv_tmpl["id"]:
        errors.append(
            f"Follow-Up template should be '{hv_tmpl['id']}', "
            f"got '{followup.get('noteTemplate')}'."
        )

    if errors:
        return False, " ".join(errors)
    return True, "'High-Volume Visit' template created and assigned to Follow-Up appointment."
