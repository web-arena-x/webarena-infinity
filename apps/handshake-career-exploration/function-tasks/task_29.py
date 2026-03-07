import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    q = next((q for q in state["qaQuestions"] if q["id"] == "qa_10"), None)
    if not q:
        return False, "Question 'qa_10' not found."
    for ans in q.get("answers", []):
        if "bulge bracket banks" in ans.get("text", "").lower():
            if ans.get("visibility") == "full":
                return True, "Fully visible answer submitted to qa_10 successfully."
            return False, f"Answer found but visibility is '{ans.get('visibility')}', expected 'full'."
    return False, "Answer about bulge bracket banks not found on qa_10."
