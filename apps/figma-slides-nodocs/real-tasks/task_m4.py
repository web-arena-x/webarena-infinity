import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    pres = next(
        (p for p in presentations if p.get("id") == "pres_011"),
        None,
    )
    if pres is None:
        pres = next(
            (p for p in presentations if "Accessibility Audit" in p.get("title", "")),
            None,
        )
    if pres is None:
        return False, "Accessibility Audit Results (pres_011) not found"

    shared_with = pres.get("shareSettings", {}).get("sharedWith", [])
    if "user_008" not in shared_with:
        return (
            False,
            f"Expected user_008 (Elena Voronova) in sharedWith, got {shared_with}",
        )

    return True, "Accessibility Audit Results: Elena Voronova (user_008) added to sharedWith"
