import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    job_functions = state["currentUser"]["careerInterests"]["jobFunctions"]
    if "Marketing" in job_functions:
        return True, "Marketing added to job functions."
    return False, f"Marketing not in job functions. Current: {job_functions}."
