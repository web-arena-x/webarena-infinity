import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    comments = state.get("comments", [])
    target_text = "Love the design! Very clean and professional."

    for c in comments:
        if c.get("presentationId") == "pres_001" and target_text in c.get("content", ""):
            return False, f"Comment '{target_text}' still exists on pres_001."

    return True, f"Comment '{target_text}' has been deleted from pres_001."
