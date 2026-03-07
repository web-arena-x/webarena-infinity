import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    q = next((q for q in state["qaQuestions"] if q["id"] == "qa_05"), None)
    if not q:
        return False, "Question 'qa_05' not found."
    ans = next((a for a in q.get("answers", []) if a["id"] == "ans_07"), None)
    if not ans:
        return False, "Answer 'ans_07' not found."
    if ans["helpful"] <= 89:
        return False, f"Helpful count not increased. Expected > 89, got {ans['helpful']}."
    return True, "Answer marked as helpful successfully."
