import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    match = [s for s in state["textStyles"] if s["name"] == "Heading/Display"]
    if match:
        return False, "Text style 'Heading/Display' still exists."

    return True, "Text style 'Heading/Display' deleted."
