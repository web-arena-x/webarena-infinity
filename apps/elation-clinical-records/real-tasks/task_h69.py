import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Highest HR patient gets 'Tachycardia-Screen'. Highest pain patient gets 'Pain-Management'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find highest HR and highest pain across all vitals
    max_hr = None
    max_hr_pid = None
    max_pain = None
    max_pain_pid = None

    for v in state.get("vitals", []):
        hr = v.get("heartRate")
        if hr is not None and (max_hr is None or hr > max_hr):
            max_hr = hr
            max_hr_pid = v["patientId"]

        pain = v.get("painLevel")
        if pain is not None and (max_pain is None or pain > max_pain):
            max_pain = pain
            max_pain_pid = v["patientId"]

    errors = []

    if max_hr_pid:
        hr_patient = next(
            (p for p in state["patients"] if p["id"] == max_hr_pid), None
        )
        if hr_patient and "Tachycardia-Screen" not in hr_patient.get("tags", []):
            errors.append(
                f"{hr_patient['lastName']} (highest HR {max_hr}) "
                f"missing 'Tachycardia-Screen' tag."
            )
    else:
        errors.append("No heart rate data found in vitals.")

    if max_pain_pid:
        pain_patient = next(
            (p for p in state["patients"] if p["id"] == max_pain_pid), None
        )
        if pain_patient and "Pain-Management" not in pain_patient.get("tags", []):
            errors.append(
                f"{pain_patient['lastName']} (highest pain {max_pain}) "
                f"missing 'Pain-Management' tag."
            )
    else:
        errors.append("No pain level data found in vitals.")

    if errors:
        return False, " ".join(errors)
    return True, (
        f"Highest HR ({max_hr}) tagged 'Tachycardia-Screen', "
        f"highest pain ({max_pain}) tagged 'Pain-Management'."
    )
