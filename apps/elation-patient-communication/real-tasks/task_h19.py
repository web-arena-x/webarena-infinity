import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify Megan Burke and Craig Bennet have 'Insurance Pending' tag and Passport invitations."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    patients = state.get("patients", [])

    target_patients = {
        "pat_42": "Megan Burke",
        "pat_31": "Craig Bennet"
    }

    errors = []
    for pat in patients:
        pid = pat.get("id")
        if pid in target_patients:
            name = target_patients[pid]
            tags = pat.get("tags", [])

            # Check Insurance Pending tag
            if "Insurance Pending" not in tags:
                errors.append(f"{name} ({pid}) missing 'Insurance Pending' tag (current tags: {tags})")

            # Check Passport invitation
            status = pat.get("passportStatus")
            if status != "invited":
                errors.append(f"{name} ({pid}) passportStatus is '{status}', expected 'invited'")
            elif pat.get("invitedAt") is None:
                errors.append(f"{name} ({pid}) invitedAt is None, expected a timestamp")

    if errors:
        return False, "; ".join(errors)

    return True, (
        "Megan Burke and Craig Bennet both have 'Insurance Pending' tag "
        "and Passport invitations sent"
    )
