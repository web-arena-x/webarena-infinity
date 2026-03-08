import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify reminder letters sent to all patients with March 3-5 appointments, no responses allowed."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    seed_letter_ids = {f"ltr_{i}" for i in range(1, 48)}

    # Patients with appointments March 3-5, 2026
    target_patients = {
        "pat_20": "Aisha Patel",
        "pat_36": "Martha Reeves-Whitfield",
        "pat_4": "Sophia Nguyen",
        "pat_30": "Janet Okonkwo",
        "pat_1": "James Rodriguez",
        "pat_40": "Susan Cho",
    }

    errors = []
    for pat_id, name in target_patients.items():
        letter_found = False
        for ltr in state.get("patientLetters", []):
            if (ltr.get("id") not in seed_letter_ids
                    and ltr.get("patientId") == pat_id
                    and ltr.get("direction") == "to_patient"
                    and not ltr.get("isDraft", False)):
                # Check doNotAllowResponse
                if not ltr.get("doNotAllowResponse"):
                    errors.append(
                        f"Letter to {name} ({pat_id}) allows responses, expected doNotAllowResponse=true"
                    )
                letter_found = True
                break
        if not letter_found:
            errors.append(f"No reminder letter sent to {name} ({pat_id})")

    if errors:
        return False, "; ".join(errors)
    return True, "Reminder letters sent to all 6 patients with March 3-5 appointments, responses disabled"
