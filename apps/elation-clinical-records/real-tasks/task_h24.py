import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find Washington (pat_008) — Dr. Patel's patient born in 2015
    patients = state.get("patients", [])
    washington = None
    for p in patients:
        if p.get("lastName") == "Washington":
            washington = p
            break
    if not washington:
        return False, "Patient with lastName 'Washington' not found."

    patient_id = washington.get("id", "pat_008")

    # Verify DOB contains 2015
    dob = washington.get("dateOfBirth", "")
    if "2015" not in str(dob):
        return False, (
            f"Washington's DOB is '{dob}', expected a 2015 birth year. "
            f"May not be the correct patient."
        )

    # Find vaccinations for Washington
    vaccinations = state.get("vaccinations", [])
    existing_vax_ids = {"vax_008", "vax_009", "vax_010", "vax_011"}

    washington_new_vax = [
        v for v in vaccinations
        if v.get("patientId") == patient_id and v.get("id") not in existing_vax_ids
    ]

    if not washington_new_vax:
        return False, (
            "No new vaccination found for Washington (existing vax_008 through vax_011 excluded)."
        )

    # Look for an influenza vaccine with recordType "Historical"
    for vax in washington_new_vax:
        vax_name = (vax.get("vaccineName") or "").lower()
        record_type = vax.get("recordType", "")

        if "influenza" in vax_name and record_type == "Historical":
            return True, (
                f"Historical influenza vaccination found for Washington "
                f"(id={vax.get('id')}, vaccineName='{vax.get('vaccineName')}', "
                f"recordType='{record_type}')."
            )

    # Diagnostics
    details = []
    for vax in washington_new_vax:
        details.append(
            f"id={vax.get('id')}: vaccineName='{vax.get('vaccineName')}', "
            f"recordType='{vax.get('recordType')}'"
        )

    return False, (
        f"Found {len(washington_new_vax)} new vaccination(s) for Washington but none match "
        f"influenza + Historical. Details: {'; '.join(details)}"
    )
