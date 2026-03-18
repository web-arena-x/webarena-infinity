import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    pres = next(
        (p for p in presentations if p.get("id") == "pres_001"),
        None,
    )
    if pres is None:
        pres = next(
            (p for p in presentations if "Q1 2026 Product Roadmap" in p.get("title", "")),
            None,
        )
    if pres is None:
        return False, "Q1 2026 Product Roadmap (pres_001) not found"

    shared_with = pres.get("shareSettings", {}).get("sharedWith", [])

    if "user_002" in shared_with:
        return (
            False,
            f"Expected user_002 (Marcus Rivera) removed from sharedWith, but still present: {shared_with}",
        )

    if "user_005" not in shared_with:
        return (
            False,
            f"Expected user_005 (Yuki Tanaka) in sharedWith, got {shared_with}",
        )

    return True, "Q1 Product Roadmap: Marcus Rivera removed and Yuki Tanaka added to sharedWith"
