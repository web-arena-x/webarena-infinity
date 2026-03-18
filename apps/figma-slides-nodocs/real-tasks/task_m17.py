import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    pres = next(
        (p for p in presentations if p.get("id") == "pres_012"),
        None,
    )
    if pres is None:
        pres = next(
            (p for p in presentations if "Q4 2025 Revenue Analysis" in p.get("title", "")),
            None,
        )
    if pres is None:
        return False, "Q4 2025 Revenue Analysis (pres_012) not found"

    ss = pres.get("shareSettings", {})
    shared_with = ss.get("sharedWith", [])
    if "user_006" not in shared_with:
        return (
            False,
            f"Expected user_006 (Priya Sharma-Krishnamurthy) in sharedWith, got {shared_with}",
        )

    visibility = ss.get("visibility", "")
    if visibility != "team":
        return False, f"Expected visibility=='team', got '{visibility}'"

    return True, "Q4 2025 Revenue Analysis: Priya Sharma-Krishnamurthy added and visibility set to team"
