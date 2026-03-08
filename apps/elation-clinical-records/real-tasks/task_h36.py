import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find O'Brien (pat_005) — the oldest Medicare patient (DOB 1948-06-30)
    patients = state.get("patients", [])
    obrien = None
    for p in patients:
        if p.get("lastName") == "O'Brien":
            obrien = p
            break
    if not obrien:
        return False, "Patient with lastName \"O'Brien\" not found."

    tags = obrien.get("tags", [])
    if "Geriatric-Screening" in tags:
        return True, "O'Brien (oldest Medicare patient) has 'Geriatric-Screening' tag."

    return False, (
        f"O'Brien's tags do not include 'Geriatric-Screening'. "
        f"Current tags: {tags}"
    )
