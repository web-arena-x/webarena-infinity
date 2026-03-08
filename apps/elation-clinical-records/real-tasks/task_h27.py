import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find Henderson (pat_001) — the patient with the most problems
    patients = state.get("patients", [])
    henderson = None
    for p in patients:
        if p.get("lastName") == "Henderson":
            henderson = p
            break
    if not henderson:
        return False, "Patient with lastName 'Henderson' not found."

    patient_id = henderson.get("id", "pat_001")

    # Find all problems for Henderson
    problems = state.get("problems", [])
    henderson_problems = [pr for pr in problems if pr.get("patientId") == patient_id]

    if not henderson_problems:
        return False, "No problems found for Henderson."

    # The controlled problems that should now be Resolved
    controlled_ids = {"prob_002", "prob_006"}

    errors = []

    for prob_id in controlled_ids:
        prob = None
        for pr in henderson_problems:
            if pr.get("id") == prob_id:
                prob = pr
                break

        if not prob:
            errors.append(
                f"Problem {prob_id} not found for Henderson — it may have been deleted "
                f"instead of resolved"
            )
            continue

        status = prob.get("status", "")
        if status != "Resolved":
            errors.append(
                f"{prob_id} ('{prob.get('title', '?')}') has status '{status}', expected 'Resolved'"
            )

    if errors:
        return False, f"Issues with Henderson's controlled problems: {'; '.join(errors)}"

    return True, (
        "Henderson's controlled problems prob_002 (Essential Hypertension) and "
        "prob_006 (Seasonal Allergic Rhinitis) are both resolved and still present."
    )
