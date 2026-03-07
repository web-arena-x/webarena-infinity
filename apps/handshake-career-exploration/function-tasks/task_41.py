import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    job_types = state["currentUser"]["careerInterests"]["jobTypes"]
    if "Part-time" not in job_types:
        return True, "Part-time removed from job types."
    return False, f"Part-time still in job types. Current: {job_types}."
