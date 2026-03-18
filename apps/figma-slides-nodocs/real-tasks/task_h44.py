import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Sunset theme: star the draft, archive the published one."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])
    pres_map = {p["id"]: p for p in presentations}

    errors = []

    # pres_018 (Design Workshop Materials) — was draft, sunset theme → star it
    if "pres_018" not in pres_map:
        errors.append("pres_018 not found")
    else:
        p = pres_map["pres_018"]
        if not p.get("starred"):
            errors.append(
                f"pres_018 ({p.get('title')}): sunset-themed draft should be starred, "
                f"got starred=={p.get('starred')}"
            )

    # pres_010 (Marketing Campaign) — was published, sunset theme → archive it
    if "pres_010" not in pres_map:
        errors.append("pres_010 not found")
    else:
        p = pres_map["pres_010"]
        if p.get("status") != "archived":
            errors.append(
                f"pres_010 ({p.get('title')}): sunset-themed published should be archived, "
                f"got status=='{p.get('status')}'"
            )

    if errors:
        return False, "; ".join(errors)

    return True, (
        "Sunset-themed draft (Design Workshop Materials) starred. "
        "Sunset-themed published (Marketing Campaign) archived."
    )
