import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    patients = state.get("patients", [])
    vitals = state.get("vitals", [])

    if not patients:
        return False, "No patients found in state."
    if not vitals:
        return False, "No vitals found in state."

    errors = []

    for patient in patients:
        patient_id = patient.get("id")
        last_name = patient.get("lastName", "?")

        # Find all vitals for this patient
        patient_vitals = [v for v in vitals if v.get("patientId") == patient_id]

        tags = patient.get("tags", [])
        has_bp_alert = "BP-Alert" in tags

        if not patient_vitals:
            # Patients with no vitals should NOT have the tag
            if has_bp_alert:
                errors.append(
                    f"{last_name} ({patient_id}) has no vitals but has 'BP-Alert' tag"
                )
            continue

        # Find most recent vitals entry by date
        most_recent = max(patient_vitals, key=lambda v: v.get("date", ""))
        systolic = most_recent.get("bloodPressureSystolic")

        if systolic is None:
            # No systolic reading in most recent vitals; should not have tag
            if has_bp_alert:
                errors.append(
                    f"{last_name} ({patient_id}) most recent vitals have no systolic BP "
                    f"but has 'BP-Alert' tag"
                )
            continue

        systolic_val = int(systolic) if isinstance(systolic, (int, float, str)) else 0

        if systolic_val >= 130:
            if not has_bp_alert:
                errors.append(
                    f"{last_name} ({patient_id}) most recent systolic is {systolic_val} (>= 130) "
                    f"but 'BP-Alert' tag is missing. Current tags: {tags}"
                )
        else:
            if has_bp_alert:
                errors.append(
                    f"{last_name} ({patient_id}) most recent systolic is {systolic_val} (< 130) "
                    f"but has 'BP-Alert' tag (over-tagging)"
                )

    if errors:
        return False, f"BP-Alert tagging issues: {'; '.join(errors)}"

    return True, (
        "All patients with most recent systolic BP >= 130 have 'BP-Alert' tag, "
        "and no patients with systolic < 130 or no vitals have the tag."
    )
