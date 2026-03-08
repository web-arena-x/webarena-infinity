import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Find patient with highest BMI → add tag 'Weight-Management' + problem 'Obesity, unspecified' E66.09."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Determine which patient has the highest recorded BMI
    # From seed data: Johnson (pat_003) has BMI 33.2 (highest)
    vitals = state.get("vitals", [])
    max_bmi = None
    max_bmi_pid = None
    for v in vitals:
        bmi = v.get("bmi")
        if bmi is not None and (max_bmi is None or bmi > max_bmi):
            max_bmi = bmi
            max_bmi_pid = v.get("patientId")

    if max_bmi_pid is None:
        return False, "No vitals with BMI found."

    # Find that patient
    patient = None
    for p in state.get("patients", []):
        if p.get("id") == max_bmi_pid:
            patient = p
            break
    if not patient:
        return False, f"Patient {max_bmi_pid} not found."

    last_name = patient.get("lastName", "?")
    errors = []

    # Check tag
    tags = patient.get("tags", [])
    if "Weight-Management" not in tags:
        errors.append(f"{last_name} is missing 'Weight-Management' tag.")

    # Check new problem
    problems = state.get("problems", [])
    patient_problems = [pr for pr in problems if pr.get("patientId") == max_bmi_pid]
    obesity_prob = None
    for pr in patient_problems:
        icd = pr.get("icd10", "")
        if icd == "E66.09":
            obesity_prob = pr
            break
    if not obesity_prob:
        errors.append(f"{last_name} has no problem with ICD-10 code E66.09.")
    else:
        title = obesity_prob.get("title", "")
        if "obesity" not in title.lower():
            errors.append(f"Problem with E66.09 has unexpected title: '{title}'.")

    if errors:
        return False, " ".join(errors)
    return True, f"{last_name} (highest BMI {max_bmi}) has 'Weight-Management' tag and Obesity problem (E66.09)."
