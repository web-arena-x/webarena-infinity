import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find O'Brien (pat_005)
    patients = state.get("patients", [])
    obrien = None
    for p in patients:
        if p.get("lastName") == "O'Brien":
            obrien = p
            break
    if not obrien:
        return False, "Patient with lastName \"O'Brien\" not found."

    patient_id = obrien.get("id", "pat_005")

    # Check that none of O'Brien's problems have status "Active"
    problems = state.get("problems", [])
    obrien_problems = [pr for pr in problems if pr.get("patientId") == patient_id]

    if not obrien_problems:
        return False, "No problems found for O'Brien."

    still_active = []
    for pr in obrien_problems:
        if pr.get("status") == "Active":
            still_active.append(f"{pr.get('id', '?')} ({pr.get('title', '?')})")

    if still_active:
        return False, (
            f"The following problems for O'Brien are still Active: "
            f"{', '.join(still_active)}"
        )

    # Check tags contain "Stable" and do NOT contain "CHF"
    tags = obrien.get("tags", [])
    errors = []

    if "Stable" not in tags:
        errors.append(f"O'Brien's tags do not include 'Stable'. Current tags: {tags}")

    if "CHF" in tags:
        errors.append(f"O'Brien's tags still contain 'CHF'. Current tags: {tags}")

    if errors:
        return False, "; ".join(errors)

    return True, (
        "All of O'Brien's problems are no longer Active, tags contain 'Stable', "
        "and 'CHF' tag has been removed."
    )
