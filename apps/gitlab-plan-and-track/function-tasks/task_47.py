import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    cadences = state.get("iterationCadences", [])

    target = next((c for c in cadences if c["title"] == "Sprint Cadence"), None)
    if not target:
        return False, "Iteration cadence with title 'Sprint Cadence' not found."

    expected_desc = "Bi-weekly development sprints for the engineering team. Updated for Q2 2026."
    actual_desc = target.get("description", "")
    if actual_desc != expected_desc:
        return False, f"Cadence description is '{actual_desc}', expected '{expected_desc}'."

    return True, "Cadence 'Sprint Cadence' has the updated description ending with 'Updated for Q2 2026.'."
