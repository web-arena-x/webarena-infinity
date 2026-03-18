import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Share Revenue Analysis with Roadmap users, resolve all Revenue comments."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])
    comments = state.get("comments", [])
    pres_map = {p["id"]: p for p in presentations}

    errors = []

    # Check Revenue Analysis (pres_012)
    if "pres_012" not in pres_map:
        return False, "pres_012 (Q4 2025 Revenue Analysis) not found"

    revenue = pres_map["pres_012"]
    shared = set(revenue.get("shareSettings", {}).get("sharedWith", []))

    # Q1 Product Roadmap (pres_001) sharedWith in seed: user_002, user_003, user_004
    for uid in ["user_002", "user_003", "user_004"]:
        if uid not in shared:
            errors.append(f"Revenue Analysis missing Roadmap user {uid}")

    # All comments on Revenue Analysis should be resolved
    revenue_comments = [c for c in comments if c.get("presentationId") == "pres_012"]
    unresolved = [c for c in revenue_comments if not c.get("resolved", False)]
    if unresolved:
        ids = [c.get("id") for c in unresolved]
        errors.append(f"Unresolved comments on Revenue Analysis: {ids}")

    if errors:
        return False, "; ".join(errors)

    return True, (
        "Revenue Analysis shared with all Roadmap users. "
        "All Revenue Analysis comments resolved."
    )
