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

    matter_id = matter.get("id")
    damages = state.get("damages", [])
    remaining = [d for d in damages if d.get("matterId") == matter_id]

    if remaining:
        summary = [(d.get("id"), d.get("name"), d.get("amount")) for d in remaining]
        return False, f"Russo v. Lyft still has {len(remaining)} damage(s): {summary}."

    return True, "All damages have been removed from Russo v. Lyft."
