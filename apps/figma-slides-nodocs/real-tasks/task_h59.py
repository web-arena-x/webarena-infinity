import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Most-unresolved-comments pres: org vis, enable editing, add Yuki+David."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])
    pres_map = {p["id"]: p for p in presentations}

    # pres_001 has 5 unresolved comments (most in seed data)
    pid = "pres_001"
    if pid not in pres_map:
        return False, f"{pid} not found"

    p = pres_map[pid]
    ss = p.get("shareSettings", {})
    errors = []

    if ss.get("visibility") != "organization":
        errors.append(f"visibility is '{ss.get('visibility')}', expected 'organization'")

    if not ss.get("allowEditing"):
        errors.append("allowEditing should be true")

    shared = set(ss.get("sharedWith", []))
    if "user_005" not in shared:
        errors.append("Yuki Tanaka (user_005) not in sharedWith")
    if "user_007" not in shared:
        errors.append("David Kim (user_007) not in sharedWith")

    if errors:
        return False, f"pres_001 ({p.get('title')}): " + "; ".join(errors)

    return True, (
        "Q1 Product Roadmap (most unresolved comments): "
        "organization visibility, editing enabled, Yuki and David added."
    )
