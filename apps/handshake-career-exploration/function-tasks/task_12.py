import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    if "job_01" not in state["currentUser"]["savedJobIds"]:
        return False, "Job 'job_01' not in savedJobIds."
    return True, "Google SWE Intern job saved successfully."
