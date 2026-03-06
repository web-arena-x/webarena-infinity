import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that all geriatric patients have the 'Chronic Care' tag."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    patients = state.get("patients", [])

    # Geriatric patients (those tagged "Geriatric" in seed data):
    # pat_3, pat_10, pat_19, pat_24, pat_27, pat_33, pat_36, pat_43, pat_47, pat_50
    geriatric_ids = {
        "pat_3", "pat_10", "pat_19", "pat_24", "pat_27",
        "pat_33", "pat_36", "pat_43", "pat_47", "pat_50"
    }

    missing_chronic_care = []
    for pat in patients:
        pid = pat.get("id")
        if pid in geriatric_ids:
            tags = pat.get("tags", [])
            if "Geriatric" not in tags:
                # Patient lost their Geriatric tag - something went wrong
                name = f"{pat.get('firstName', '')} {pat.get('lastName', '')}"
                missing_chronic_care.append(f"{name} ({pid}) - 'Geriatric' tag missing")
            elif "Chronic Care" not in tags:
                name = f"{pat.get('firstName', '')} {pat.get('lastName', '')}"
                missing_chronic_care.append(f"{name} ({pid})")

    if missing_chronic_care:
        return False, (
            f"The following geriatric patients are missing 'Chronic Care' tag: "
            f"{', '.join(missing_chronic_care)}"
        )

    return True, "All geriatric patients now have the 'Chronic Care' tag"
