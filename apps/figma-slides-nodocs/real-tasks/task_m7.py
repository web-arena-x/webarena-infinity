import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    pres = next(
        (p for p in presentations if p.get("id") == "pres_015"),
        None,
    )
    if pres is None:
        pres = next(
            (p for p in presentations if "Product Demo" in p.get("title", "") and "Enterprise" in p.get("title", "")),
            None,
        )
    if pres is None:
        return False, "Product Demo — Enterprise Features (pres_015) not found"

    shared_with = pres.get("shareSettings", {}).get("sharedWith", [])
    missing = []
    if "user_002" not in shared_with:
        missing.append("user_002 (Marcus Rivera)")
    if "user_003" not in shared_with:
        missing.append("user_003 (Anika Patel)")

    if missing:
        return (
            False,
            f"Missing from sharedWith: {missing}. Current sharedWith: {shared_with}",
        )

    return True, "Product Demo — Enterprise Features: Marcus Rivera and Anika Patel added to sharedWith"
