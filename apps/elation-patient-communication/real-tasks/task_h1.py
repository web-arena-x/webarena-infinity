import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that all of Dr. Chen's diabetes patients are tagged as 'High Risk'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    patients = state.get("patients", [])

    # Dr. Chen's patients with diabetes-related conditions:
    # pat_1 (James Rodriguez): Type 2 Diabetes Mellitus
    # pat_8 (Patricia O'Brien): Type 2 Diabetes
    # pat_30 (Janet Okonkwo): Type 1 Diabetes
    # pat_36 (Martha Reeves-Whitfield): Type 2 Diabetes
    diabetes_patient_ids = {"pat_1", "pat_8", "pat_30", "pat_36"}

    missing = []
    for pat in patients:
        pid = pat.get("id")
        if pid in diabetes_patient_ids:
            tags = pat.get("tags", [])
            if "High Risk" not in tags:
                name = f"{pat.get('firstName', '')} {pat.get('lastName', '')}"
                missing.append(f"{name} ({pid})")

    if missing:
        return False, (
            f"The following Dr. Chen diabetes patients are missing 'High Risk' tag: "
            f"{', '.join(missing)}"
        )

    return True, "All of Dr. Chen's diabetes patients are tagged as 'High Risk'"
