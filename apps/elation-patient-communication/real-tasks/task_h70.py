import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify reply to Deborah Takahashi about calcium and new appointment scheduled."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    seed_letter_ids = {f"ltr_{i}" for i in range(1, 48)}
    seed_appt_ids = {f"appt_{i}" for i in range(1, 21)}
    errors = []

    # Check for reply in conv_17
    has_reply = False
    for ltr in state.get("patientLetters", []):
        if (ltr.get("conversationId") == "conv_17"
                and ltr.get("direction") == "to_patient"
                and ltr.get("id") not in seed_letter_ids
                and not ltr.get("isDraft", False)):
            has_reply = True
            break

    if not has_reply:
        errors.append("No new reply in conv_17 (Deborah Takahashi's calcium supplement question)")

    # Check for new appointment
    appt_found = False
    for appt in state.get("appointments", []):
        if appt.get("id") in seed_appt_ids:
            continue
        if (appt.get("patientId") == "pat_50"
                and appt.get("providerId") == "prov_1"
                and appt.get("place") == "in_person"
                and appt.get("status") == "scheduled"
                and "2026-04-05" in appt.get("date", "")):
            appt_found = True
            break

    if not appt_found:
        errors.append(
            "No in-person appointment found for pat_50 (Deborah Takahashi) "
            "with prov_1 (Dr. Chen) on April 5, 2026"
        )

    if errors:
        return False, "; ".join(errors)
    return True, "Reply sent about calcium and appointment scheduled for Deborah Takahashi"
