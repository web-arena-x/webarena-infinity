import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    patients = state.get("patients", [])
    patient = None
    for p in patients:
        if p.get("id") == "pat_24":
            patient = p
            break

    if patient is None:
        return False, "Patient pat_24 (Nancy Yamamoto) not found."

    tags = patient.get("tags", [])

    if "Geriatric" in tags:
        return False, f"'Geriatric' tag is still present on Nancy Yamamoto. Current tags: {tags}."

    if "Chronic Care" in tags:
        return False, f"'Chronic Care' tag is still present on Nancy Yamamoto. Current tags: {tags}."

    return True, "Tags removed from Nancy Yamamoto's profile."
