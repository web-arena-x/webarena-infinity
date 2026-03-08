import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Create 'Comprehensive Visit' template with HPI/ROS/PE/Assessment + billing 99215, then configure Urgent Same-Day."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Check template exists
    comp_tmpl = None
    for t in state.get("visitNoteTemplates", []):
        if t.get("name", "").lower() == "comprehensive visit":
            comp_tmpl = t
            break

    if not comp_tmpl:
        return False, "Template 'Comprehensive Visit' not found."

    # Check template content sections
    content = comp_tmpl.get("content", {})
    for section in ["hpi", "ros", "pe", "assessment"]:
        if not content.get(section):
            errors.append(f"Template missing '{section}' section.")

    # Check billing
    billing = comp_tmpl.get("billingItems", [])
    has_99215 = any(b.get("cptCode") == "99215" for b in billing)
    if not has_99215:
        errors.append("Template missing billing code 99215.")

    # Check Urgent Same-Day appointment type
    urgent_apt = None
    for a in state.get("appointmentTypes", []):
        if a.get("name", "").lower() == "urgent same-day":
            urgent_apt = a
            break
    if not urgent_apt:
        errors.append("Urgent Same-Day appointment type not found.")
    else:
        if urgent_apt.get("noteTemplate") != comp_tmpl.get("id"):
            errors.append(
                f"Urgent Same-Day template is '{urgent_apt.get('noteTemplate')}', "
                f"expected '{comp_tmpl.get('id')}' (Comprehensive Visit)."
            )
        if urgent_apt.get("noteFormat") != "hp_single":
            errors.append(
                f"Urgent Same-Day format is '{urgent_apt.get('noteFormat')}', expected 'hp_single'."
            )

    if errors:
        return False, " ".join(errors)
    return True, (
        "Template 'Comprehensive Visit' created with HPI/ROS/PE/Assessment + billing 99215. "
        "Urgent Same-Day uses this template with H&P Single Column format."
    )
