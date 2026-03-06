import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify Dr. Kim's uninvited patients were invited and auto-invite is disabled."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    patients = state.get("patients", [])

    # Dr. Kim (prov_4) uninvited patients: pat_15, pat_23, pat_31
    target_ids = {"pat_15", "pat_23", "pat_31"}
    expected_names = {
        "pat_15": "Brian Murphy",
        "pat_23": "Victor Santos",
        "pat_31": "Craig Bennet"
    }

    not_invited = []
    for pat in patients:
        pid = pat.get("id")
        if pid in target_ids:
            status = pat.get("passportStatus")
            if status != "invited":
                not_invited.append(
                    f"{expected_names[pid]} ({pid}) status='{status}'"
                )

    if not_invited:
        return False, (
            f"The following Dr. Kim patients are not invited: {', '.join(not_invited)}"
        )

    # Check auto-invite is disabled
    practice_settings = state.get("practiceSettings")
    if practice_settings is None:
        return False, "practiceSettings not found in state"

    auto_invite = practice_settings.get("bookingSiteAutoInvite")
    if auto_invite is not False:
        return False, (
            f"bookingSiteAutoInvite is {auto_invite}, expected False"
        )

    return True, (
        "All Dr. Kim's uninvited patients have been invited to Passport "
        "and auto-invite setting is disabled"
    )
