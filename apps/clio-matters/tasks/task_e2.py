import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    matter = next(
        (m for m in state.get("matters", [])
         if "Russo" in m.get("description", "") and "Lyft" in m.get("description", "")),
        None
    )

    if matter is None:
        return False, "Could not find a matter with description containing 'Russo' and 'Lyft'."

    if matter.get("status") != "open":
        return False, f"Russo v. Lyft matter status is '{matter.get('status')}', expected 'open'."

    return True, "Russo v. Lyft matter has been reopened with status 'open'."
