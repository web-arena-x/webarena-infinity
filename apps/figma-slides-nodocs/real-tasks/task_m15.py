import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    pres_014 = next(
        (p for p in presentations if p.get("id") == "pres_014"),
        None,
    )
    if pres_014 is None:
        pres_014 = next(
            (p for p in presentations if "Team Retrospective" in p.get("title", "") and "Sprint 47" in p.get("title", "")),
            None,
        )
    if pres_014 is None:
        return False, "Team Retrospective — Sprint 47 (pres_014) not found"

    pres_008 = next(
        (p for p in presentations if p.get("id") == "pres_008"),
        None,
    )
    if pres_008 is None:
        pres_008 = next(
            (p for p in presentations if "Design Sprint Week 12" in p.get("title", "")),
            None,
        )
    if pres_008 is None:
        return False, "Design Sprint Week 12 Recap (pres_008) not found"

    errors = []
    status_014 = pres_014.get("status", "")
    if status_014 != "archived":
        errors.append(
            f"Team Retrospective Sprint 47: expected status=='archived', got '{status_014}'"
        )

    status_008 = pres_008.get("status", "")
    if status_008 != "archived":
        errors.append(
            f"Design Sprint Week 12 Recap: expected status=='archived', got '{status_008}'"
        )

    if errors:
        return False, "; ".join(errors)

    return True, "Both Team Retrospective — Sprint 47 and Design Sprint Week 12 Recap are archived"
