import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Tag patients with upcoming virtual appointments as 'Telehealth Preferred'
    if not already tagged."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Virtual upcoming appointments in seed data:
    # appt_2: pat_4 (Sophia Nguyen) - already tagged
    # appt_6: pat_29 (Andrew McIntyre) - already tagged
    # appt_9: pat_27 (Howard Blackwell) - NOT tagged
    # appt_13: pat_30 (Janet Okonkwo) - NOT tagged
    # appt_14: pat_40 (Susan Cho) - already tagged
    need_tag = {
        "pat_27": "Howard Blackwell",
        "pat_30": "Janet Okonkwo",
    }

    patients = state.get("patients", [])
    patient_map = {p["id"]: p for p in patients}

    for pid, name in need_tag.items():
        patient = patient_map.get(pid)
        if patient is None:
            return False, f"Patient {name} ({pid}) not found."
        if "Telehealth Preferred" not in patient.get("tags", []):
            return False, (
                f"{name} ({pid}) does not have 'Telehealth Preferred' tag. "
                f"Current tags: {patient.get('tags')}"
            )

    # Also verify already-tagged patients still have the tag
    already_tagged = {
        "pat_4": "Sophia Nguyen",
        "pat_29": "Andrew McIntyre",
        "pat_40": "Susan Cho",
    }
    for pid, name in already_tagged.items():
        patient = patient_map.get(pid)
        if patient and "Telehealth Preferred" not in patient.get("tags", []):
            return False, (
                f"{name} ({pid}) lost their 'Telehealth Preferred' tag."
            )

    return True, (
        "All patients with virtual appointments tagged as "
        "'Telehealth Preferred'."
    )
