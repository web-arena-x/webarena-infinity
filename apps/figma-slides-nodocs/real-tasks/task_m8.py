import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    pres = next(
        (p for p in presentations if p.get("id") == "pres_010"),
        None,
    )
    if pres is None:
        pres = next(
            (p for p in presentations if "Marketing Campaign" in p.get("title", "")),
            None,
        )
    if pres is None:
        return False, "Marketing Campaign presentation (pres_010) not found"

    ss = pres.get("shareSettings", {})
    visibility = ss.get("visibility", "")
    if visibility != "organization":
        return False, f"Expected visibility=='organization', got '{visibility}'"

    allow_editing = ss.get("allowEditing", True)
    if allow_editing:
        return False, f"Expected allowEditing==false, got {allow_editing}"

    return True, "Marketing Campaign: visibility set to organization and editing disabled"
