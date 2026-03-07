import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    for q in state["qaQuestions"]:
        if "best tech companies for new grad software engineers" in q.get("question", "").lower():
            if q.get("authorName") == "Maya Chen" and q.get("status") == "pending":
                return True, "Question submitted successfully."
            return False, f"Question found but author is '{q.get('authorName')}' or status is '{q.get('status')}'."
    return False, "Question about best tech companies not found."
