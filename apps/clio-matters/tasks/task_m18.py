import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    matter = next(
        (m for m in state.get("matters", [])
         if "Sullivan-Wright" in m.get("description", "")
         and ("surgical error" in m.get("description", "").lower()
              or "appendectomy" in m.get("description", "").lower()
              or "Kaiser" in m.get("description", ""))),
        None
    )

    if matter is None:
        return False, "Could not find a matter with description containing 'Sullivan-Wright' and 'surgical error' or 'Kaiser'."

    matter_id = matter.get("id")
    damages = state.get("damages", [])
    matching = [
        d for d in damages
        if d.get("matterId") == matter_id
        and d.get("type") == "special"
        and abs(d.get("amount", 0) - 200000) < 1
    ]

    if not matching:
        matter_damages = [d for d in damages if d.get("matterId") == matter_id]
        summary = [(d.get("type"), d.get("amount")) for d in matter_damages]
        return False, f"No special damage with amount $200,000 found for Sullivan-Wright case. Existing damages: {summary}."

    return True, "Sullivan-Wright case has a $200,000 special damage entry."
