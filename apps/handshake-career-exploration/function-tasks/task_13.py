import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    if "job_03" in state["currentUser"]["savedJobIds"]:
        return False, "Job 'job_03' still in savedJobIds."
    return True, "JPMorgan IB Summer Analyst job unsaved successfully."
