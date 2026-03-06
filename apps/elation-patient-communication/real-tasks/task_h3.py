import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that Passport invitations were sent to all uninvited Dr. Kim patients."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    patients = state.get("patients", [])

    # Dr. Kim (prov_4) uninvited patients:
    # pat_15 (Brian Murphy), pat_23 (Victor Santos), pat_31 (Craig Bennet)
    target_ids = {"pat_15", "pat_23", "pat_31"}
    expected_names = {
        "pat_15": "Brian Murphy",
        "pat_23": "Victor Santos",
        "pat_31": "Craig Bennet"
    }

    not_invited = []
    missing_timestamp = []
    for pat in patients:
        pid = pat.get("id")
        if pid in target_ids:
            status = pat.get("passportStatus")
            if status != "invited":
                not_invited.append(f"{expected_names[pid]} ({pid}) status='{status}'")
            elif pat.get("invitedAt") is None:
                missing_timestamp.append(f"{expected_names[pid]} ({pid})")

    if not_invited:
        return False, (
            f"The following Dr. Kim patients are not invited: {', '.join(not_invited)}"
        )

    if missing_timestamp:
        return False, (
            f"The following patients have 'invited' status but no invitedAt timestamp: "
            f"{', '.join(missing_timestamp)}"
        )

    return True, "All uninvited Dr. Kim patients (Brian Murphy, Victor Santos, Craig Bennet) have been invited to Passport"
