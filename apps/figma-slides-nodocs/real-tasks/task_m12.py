import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    pres = next(
        (p for p in presentations if p.get("id") == "pres_008"),
        None,
    )
    if pres is None:
        pres = next(
            (p for p in presentations if "Design Sprint Week 12" in p.get("title", "")),
            None,
        )
    if pres is None:
        return False, "Design Sprint Week 12 Recap (pres_008) not found"

    shared_with = pres.get("shareSettings", {}).get("sharedWith", [])
    missing = []
    if "user_005" not in shared_with:
        missing.append("user_005 (Yuki Tanaka)")
    if "user_007" not in shared_with:
        missing.append("user_007 (David Kim)")

    if missing:
        return (
            False,
            f"Missing from sharedWith: {missing}. Current sharedWith: {shared_with}",
        )

    return True, "Design Sprint Week 12 Recap: David Kim and Yuki Tanaka added to sharedWith"
