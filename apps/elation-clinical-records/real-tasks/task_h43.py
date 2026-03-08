import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Tag patients with vaccination records as 'Vaccinated', those without as 'No-Vaccines'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Determine which patients have vaccination records
    patients_with_vax = set()
    for v in state.get("vaccinations", []):
        pid = v.get("patientId")
        if pid:
            patients_with_vax.add(pid)

    errors = []
    for patient in state.get("patients", []):
        pid = patient.get("id", "")
        last_name = patient.get("lastName", "?")
        tags = patient.get("tags", [])

        if pid in patients_with_vax:
            if "Vaccinated" not in tags:
                errors.append(f"{last_name} has vaccination records but missing 'Vaccinated' tag.")
        else:
            if "No-Vaccines" not in tags:
                errors.append(f"{last_name} has no vaccination records but missing 'No-Vaccines' tag.")

    if errors:
        return False, " ".join(errors)
    return True, (
        f"All {len(patients_with_vax)} patients with vaccination records have 'Vaccinated' tag; "
        f"all {len(state.get('patients', [])) - len(patients_with_vax)} without have 'No-Vaccines' tag."
    )
