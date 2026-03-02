import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    matter = next(
        (m for m in state.get("matters", [])
         if "Patterson" in m.get("description", "") and
         ("bus" in m.get("description", "").lower() or "Metro Transit" in m.get("description", ""))),
        None
    )

    if matter is None:
        return False, "Could not find a matter with description containing 'Patterson' and 'bus' or 'Metro Transit'."

    if matter.get("status") != "closed":
        return False, f"Patterson matter status is '{matter.get('status')}', expected 'closed'."

    if not matter.get("closedDate"):
        return False, "Patterson matter has no closedDate set."

    return True, "Patterson v. Metro Transit matter is closed with a closedDate."
