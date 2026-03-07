import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    appt = next((a for a in state["appointments"] if a["id"] == "appt_01"), None)
    if not appt:
        return False, "Appointment 'appt_01' not found."
    for comment in appt.get("comments", []):
        if "cover letter" in comment.get("text", "").lower():
            return True, "Comment about cover letter added to appointment."
    return False, "No comment containing 'cover letter' found on appointment."
