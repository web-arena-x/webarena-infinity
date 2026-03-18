import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    pres = next(
        (p for p in presentations if p.get("id") == "pres_003"),
        None,
    )
    if pres is None:
        pres = next(
            (p for p in presentations if "Series B" in p.get("title", "")),
            None,
        )
    if pres is None:
        return False, "Series B Fundraising Pitch (pres_003) not found"

    ss = pres.get("shareSettings", {})
    shared_with = ss.get("sharedWith", [])
    if "user_003" not in shared_with:
        return (
            False,
            f"Expected user_003 (Anika Patel) in sharedWith, got {shared_with}",
        )

    allow_comments = ss.get("allowComments", False)
    if not allow_comments:
        return False, f"Expected allowComments==true, got {allow_comments}"

    return True, "Series B Fundraising Pitch: Anika Patel added and comments enabled"
