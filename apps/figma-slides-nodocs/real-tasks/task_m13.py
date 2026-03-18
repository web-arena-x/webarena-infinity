import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    pres = next(
        (p for p in presentations if p.get("id") == "pres_009"),
        None,
    )
    if pres is None:
        pres = next(
            (p for p in presentations if "Onboarding Training Module" in p.get("title", "")),
            None,
        )
    if pres is None:
        return False, "Onboarding Training Module (pres_009) not found"

    ss = pres.get("shareSettings", {})
    visibility = ss.get("visibility", "")
    if visibility != "team":
        return False, f"Expected visibility=='team', got '{visibility}'"

    allow_comments = ss.get("allowComments", False)
    if not allow_comments:
        return False, f"Expected allowComments==true, got {allow_comments}"

    allow_editing = ss.get("allowEditing", False)
    if not allow_editing:
        return False, f"Expected allowEditing==true, got {allow_editing}"

    return True, "Onboarding Training Module: visibility set to team, comments and editing enabled"
