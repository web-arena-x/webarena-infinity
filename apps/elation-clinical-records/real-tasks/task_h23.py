import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    templates = state.get("visitNoteTemplates", [])

    if not templates:
        return False, "No visit note templates found in state."

    # Check that the original template still exists
    original_found = False
    new_found = False

    for t in templates:
        name = (t.get("name") or "").strip()
        if "Annual Wellness Visit" in name and t.get("id") == "tmpl_001":
            original_found = True
        if name.lower() == "modified annual wellness":
            new_found = True

    errors = []

    if not original_found:
        template_names = [(t.get("id"), t.get("name")) for t in templates]
        errors.append(
            f"Original template tmpl_001 ('Annual Wellness Visit') not found — "
            f"it may have been renamed instead of duplicated. Templates: {template_names}"
        )

    if not new_found:
        template_names = [t.get("name") for t in templates]
        errors.append(
            f"Template named 'Modified Annual Wellness' not found. "
            f"Current templates: {template_names}"
        )

    if errors:
        return False, "; ".join(errors)

    return True, (
        "Template 'Modified Annual Wellness' exists and original "
        "'Annual Wellness Visit' (tmpl_001) is still present (duplicated, not renamed)."
    )
