import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    q = next((q for q in state["qaQuestions"] if q["id"] == "qa_06"), None)
    if not q:
        return False, "Question 'qa_06' not found."
    for ans in q.get("answers", []):
        if "mock system design interviews" in ans.get("text", "").lower():
            if ans.get("visibility") == "semi-anonymous":
                return True, "Semi-anonymous answer submitted to qa_06 successfully."
            return False, f"Answer found but visibility is '{ans.get('visibility')}', expected 'semi-anonymous'."
    return False, "Answer about mock system design interviews not found on qa_06."
