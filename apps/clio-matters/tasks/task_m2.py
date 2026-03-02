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

    matter_id = matter.get("id")
    damages = state.get("damages", [])
    matching = [
        d for d in damages
        if d.get("matterId") == matter_id
        and d.get("type") == "general"
        and abs(d.get("amount", 0) - 50000) < 1
    ]

    if not matching:
        matter_damages = [d for d in damages if d.get("matterId") == matter_id]
        if not matter_damages:
            return False, f"No damages found for matter '{matter_id}' (Johnson v. Whole Foods)."
        summary = [(d.get("type"), d.get("amount")) for d in matter_damages]
        return False, f"No general damage with amount $50,000 found for Johnson v. Whole Foods. Existing damages: {summary}."

    return True, "Johnson v. Whole Foods has a $50,000 general damage entry."
