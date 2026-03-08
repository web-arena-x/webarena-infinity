import requests


def verify(server_url: str) -> tuple[bool, str]:
    """COVID Vaccine template tags replaced with 'COVID-Protocol', same template assigned to Urgent Same-Day."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Find COVID Vaccine appointment type
    covid_apt = None
    for apt in state.get("appointmentTypes", []):
        if apt.get("name") == "COVID Vaccine":
            covid_apt = apt
            break
    if not covid_apt:
        return False, "COVID Vaccine appointment type not found."

    tmpl_id = covid_apt.get("noteTemplate")
    if not tmpl_id:
        return False, "COVID Vaccine appointment has no template assigned."

    # Find the template
    tmpl = None
    for t in state.get("visitNoteTemplates", []):
        if t["id"] == tmpl_id:
            tmpl = t
            break
    if not tmpl:
        return False, f"Template {tmpl_id} not found."

    # Check tags replaced
    doc_tags = tmpl.get("documentTags", [])
    if doc_tags != ["COVID-Protocol"]:
        errors.append(
            f"Template '{tmpl['name']}' tags should be ['COVID-Protocol'], "
            f"got {doc_tags}."
        )

    # Check Urgent Same-Day uses the same template
    urgent_apt = None
    for apt in state.get("appointmentTypes", []):
        if apt.get("name") == "Urgent Same-Day":
            urgent_apt = apt
            break
    if not urgent_apt:
        errors.append("Urgent Same-Day appointment type not found.")
    elif urgent_apt.get("noteTemplate") != tmpl_id:
        errors.append(
            f"Urgent Same-Day template should be '{tmpl_id}', "
            f"got '{urgent_apt.get('noteTemplate')}'."
        )

    if errors:
        return False, " ".join(errors)
    return True, (
        f"Template '{tmpl['name']}' tags updated to ['COVID-Protocol'] "
        f"and assigned to Urgent Same-Day."
    )
