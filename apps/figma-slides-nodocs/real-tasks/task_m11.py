import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    pres = next(
        (p for p in presentations if p.get("id") == "pres_016"),
        None,
    )
    if pres is None:
        pres = next(
            (p for p in presentations if "Website Redesign Proposal" in p.get("title", "")),
            None,
        )
    if pres is None:
        return False, "Website Redesign Proposal (pres_016) not found"

    ss = pres.get("shareSettings", {})
    visibility = ss.get("visibility", "")
    if visibility != "team":
        return False, f"Expected visibility=='team', got '{visibility}'"

    shared_with = ss.get("sharedWith", [])
    if "user_008" not in shared_with:
        return (
            False,
            f"Expected user_008 (Elena Voronova) in sharedWith, got {shared_with}",
        )

    return True, "Website Redesign Proposal: visibility set to team and Elena Voronova added to sharedWith"
