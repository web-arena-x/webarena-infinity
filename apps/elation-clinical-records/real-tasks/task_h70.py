import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Active ICD-10 'I*' → 'Cardio-Review'. Active ICD-10 'E*' → 'Metabolic-Review'. Both possible."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Determine who should get each tag based on active problems
    cardio_pids = set()
    metabolic_pids = set()
    for prob in state.get("problems", []):
        if prob.get("status") != "Active":
            continue
        icd = prob.get("icd10", "")
        if icd.startswith("I"):
            cardio_pids.add(prob["patientId"])
        if icd.startswith("E"):
            metabolic_pids.add(prob["patientId"])

    errors = []
    for patient in state.get("patients", []):
        pid = patient["id"]
        tags = patient.get("tags", [])
        name = patient.get("lastName", pid)

        should_cardio = pid in cardio_pids
        should_metabolic = pid in metabolic_pids

        if should_cardio and "Cardio-Review" not in tags:
            errors.append(f"{name} should have 'Cardio-Review'.")
        if not should_cardio and "Cardio-Review" in tags:
            errors.append(f"{name} should NOT have 'Cardio-Review'.")
        if should_metabolic and "Metabolic-Review" not in tags:
            errors.append(f"{name} should have 'Metabolic-Review'.")
        if not should_metabolic and "Metabolic-Review" in tags:
            errors.append(f"{name} should NOT have 'Metabolic-Review'.")

    if errors:
        return False, " ".join(errors)
    return True, (
        f"Cardio-Review on {len(cardio_pids)} patients, "
        f"Metabolic-Review on {len(metabolic_pids)} patients."
    )
