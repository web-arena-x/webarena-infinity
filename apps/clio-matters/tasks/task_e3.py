import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    matter = next(
        (m for m in state.get("matters", [])
         if "Johnson" in m.get("description", "") and "Whole Foods" in m.get("description", "")),
        None
    )

    if matter is None:
        return False, "Could not find a matter with description containing 'Johnson' and 'Whole Foods'."

    if matter.get("status") != "pending":
        return False, f"Johnson v. Whole Foods matter status is '{matter.get('status')}', expected 'pending'."

    return True, "Johnson v. Whole Foods matter has been marked as pending."
