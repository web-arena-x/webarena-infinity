import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Two proposals: more shared users→archive, fewer→publish+team vis+add Marcus."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])
    pres_map = {p["id"]: p for p in presentations}

    errors = []

    # pres_007 (TechVentures Redesign) — 4 shared users → archive
    if "pres_007" not in pres_map:
        errors.append("pres_007 not found")
    else:
        p = pres_map["pres_007"]
        if p.get("status") != "archived":
            errors.append(
                f"pres_007 ({p.get('title')}): more shared users, "
                f"should be archived, got '{p.get('status')}'"
            )

    # pres_016 (TechStartup.io) — 3 shared users → published, team vis, add Marcus
    if "pres_016" not in pres_map:
        errors.append("pres_016 not found")
    else:
        p = pres_map["pres_016"]
        ss = p.get("shareSettings", {})

        if p.get("status") != "published":
            errors.append(
                f"pres_016 ({p.get('title')}): fewer shared users, "
                f"should be published, got '{p.get('status')}'"
            )
        if ss.get("visibility") != "team":
            errors.append(
                f"pres_016: visibility '{ss.get('visibility')}', expected 'team'"
            )
        if "user_002" not in set(ss.get("sharedWith", [])):
            errors.append("pres_016: Marcus Rivera (user_002) not in sharedWith")

    if errors:
        return False, "; ".join(errors)

    return True, (
        "TechVentures proposal (more shared users) archived. "
        "TechStartup proposal published, team visibility, Marcus added."
    )
