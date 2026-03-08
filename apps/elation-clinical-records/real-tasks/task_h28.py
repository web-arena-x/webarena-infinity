import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that every appointment type with no template has been set to E* Problem-Focused Visit (tmpl_002)."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    appointment_types = state.get("appointmentTypes", [])
    if not appointment_types:
        return False, "No appointmentTypes found in state"

    target_names = ["follow-up", "procedure", "urgent same-day"]
    expected_template = "tmpl_002"
    errors = []

    for name in target_names:
        matched = [at for at in appointment_types if at.get("name", "").lower() == name]
        if not matched:
            errors.append(f"Appointment type '{name}' not found")
            continue
        at = matched[0]
        actual = at.get("noteTemplate", "")
        if actual != expected_template:
            errors.append(
                f"Appointment type '{at.get('name')}' has noteTemplate '{actual}', expected '{expected_template}'"
            )

    if errors:
        return False, "; ".join(errors)
    return True, "All appointment types with no template now have noteTemplate set to tmpl_002"
