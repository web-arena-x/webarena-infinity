import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Only female patient with exactly 3 active problems gets historical flu vaccine + 'Flu-Historical' tag."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Count active problems per patient
    active_counts = {}
    for prob in state.get("problems", []):
        if prob.get("status") == "Active":
            pid = prob["patientId"]
            active_counts[pid] = active_counts.get(pid, 0) + 1

    # Find female patient with exactly 3 active problems
    target = None
    for p in state.get("patients", []):
        sex = (p.get("sexAtBirth") or p.get("gender") or "").lower()
        if sex == "female" and active_counts.get(p["id"], 0) == 3:
            target = p
            break
    if not target:
        return False, "No female patient with exactly 3 active problems found."

    errors = []

    # Check tag
    if "Flu-Historical" not in target.get("tags", []):
        errors.append(f"{target['lastName']} missing 'Flu-Historical' tag.")

    # Check historical influenza vaccine
    flu_vax = [
        v for v in state.get("vaccinations", [])
        if v["patientId"] == target["id"]
        and "influenza" in (v.get("vaccineName") or "").lower()
        and (v.get("recordType") or "").lower() == "historical"
    ]
    if not flu_vax:
        errors.append(f"{target['lastName']} missing historical influenza vaccine.")

    if errors:
        return False, " ".join(errors)
    return True, f"{target['lastName']} has 'Flu-Historical' tag and historical influenza vaccine."
