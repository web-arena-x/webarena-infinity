import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Send letter to Deborah Takahashi, upgrade sharing to 4, add Chronic Care."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Check letter sent to pat_50 with subject "Passport Access Update"
    letters = state.get("patientLetters", [])
    letter = next(
        (
            l for l in letters
            if l.get("patientId") == "pat_50"
            and l.get("direction") == "to_patient"
            and l.get("subject") == "Passport Access Update"
        ),
        None,
    )
    if letter is None:
        return False, (
            "No letter found to Deborah Takahashi with subject "
            "'Passport Access Update'."
        )
    if letter.get("isDraft"):
        return False, "Letter to Deborah Takahashi is still a draft."

    # Check sharing level upgraded to 4
    patients = state.get("patients", [])
    pat_50 = next((p for p in patients if p.get("id") == "pat_50"), None)
    if pat_50 is None:
        return False, "Patient pat_50 (Deborah Takahashi) not found."
    if pat_50.get("passportSharingLevel") != 4:
        return False, (
            f"Deborah Takahashi's sharing level is "
            f"{pat_50.get('passportSharingLevel')}, expected 4."
        )

    # Check Chronic Care tag
    if "Chronic Care" not in pat_50.get("tags", []):
        return False, (
            f"Deborah Takahashi's tags are {pat_50.get('tags')}, "
            f"expected 'Chronic Care' to be present."
        )

    return True, (
        "Letter sent, sharing level upgraded to 4, and 'Chronic Care' "
        "tag added for Deborah Takahashi."
    )
