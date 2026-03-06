import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the Passport invitation has been resent to William Chang."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    patients = state.get("patients", [])
    patient = None
    for pat in patients:
        if pat.get("firstName") == "William" and pat.get("lastName") == "Chang":
            patient = pat
            break

    if patient is None:
        return False, "Patient William Chang not found"

    passport_status = patient.get("passportStatus")
    if passport_status != "invited":
        return False, f"William Chang passportStatus is '{passport_status}', expected 'invited'"

    # The original invitation code was '1746290' and invitedAt was '2026-02-01T09:00:00Z'.
    # After resend, at least one of these should have changed.
    invitation_code = patient.get("invitationCode")
    invited_at = patient.get("invitedAt")

    code_changed = invitation_code != "1746290"
    time_changed = invited_at != "2026-02-01T09:00:00Z"

    if not code_changed and not time_changed:
        return False, (
            f"William Chang's invitation does not appear to have been resent. "
            f"invitationCode is still '1746290' and invitedAt is still '2026-02-01T09:00:00Z'"
        )

    return True, "Passport invitation has been resent to William Chang"
