import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Patients with no vaccinations AND no vitals get 'Needs-Vitals' and 'Needs-Immunization'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    patients_with_vax = {v["patientId"] for v in state.get("vaccinations", [])}
    patients_with_vitals = {v["patientId"] for v in state.get("vitals", [])}

    errors = []
    for patient in state.get("patients", []):
        pid = patient["id"]
        tags = patient.get("tags", [])
        name = patient.get("lastName", pid)
        no_vax = pid not in patients_with_vax
        no_vitals = pid not in patients_with_vitals
        should_tag = no_vax and no_vitals

        if should_tag:
            if "Needs-Vitals" not in tags:
                errors.append(f"{name} missing 'Needs-Vitals' tag.")
            if "Needs-Immunization" not in tags:
                errors.append(f"{name} missing 'Needs-Immunization' tag.")
        else:
            if "Needs-Vitals" in tags:
                errors.append(f"{name} should NOT have 'Needs-Vitals'.")
            if "Needs-Immunization" in tags:
                errors.append(f"{name} should NOT have 'Needs-Immunization'.")

    if errors:
        return False, " ".join(errors)
    return True, "Patients with no vaccinations and no vitals correctly tagged."
