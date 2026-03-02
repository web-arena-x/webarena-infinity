import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Find Personal Injury practice area
    practice_areas = state.get("practiceAreas", [])
    pi_pa = next(
        (pa for pa in practice_areas if pa.get("id") == "pa_1" or "personal injury" in pa.get("name", "").lower()),
        None
    )

    if pi_pa is None:
        return False, "Could not find Personal Injury practice area."

    pi_pa_id = pi_pa["id"]

    # Find all matters with practiceAreaId == PI and stageId == stage_1_3 (Demand)
    # These are the ones that should have been closed
    demand_pi_matters = [
        m for m in state.get("matters", [])
        if m.get("practiceAreaId") == pi_pa_id and m.get("stageId") == "stage_1_3"
    ]

    # Also check matters that were at stage_1_3 but may have been closed (status changed but stage kept)
    # We look for all PI matters and check the known ones
    known_demand_ids = ["matter_1", "matter_6", "matter_13", "matter_24", "matter_114"]
    all_matters = {m.get("id"): m for m in state.get("matters", [])}

    closed_count = 0
    for mid in known_demand_ids:
        matter = all_matters.get(mid)
        if matter is None:
            errors.append(f"Matter {mid} not found in state.")
            continue

        if matter.get("status") != "closed":
            errors.append(
                f"Matter {mid} ('{matter.get('description', '')}') has status "
                f"'{matter.get('status')}', expected 'closed'."
            )
        else:
            closed_count += 1

        if not matter.get("closedDate"):
            errors.append(
                f"Matter {mid} ('{matter.get('description', '')}') has no closedDate set."
            )

    # Also check any other PI matters still sitting at Demand that aren't in our known list
    for m in demand_pi_matters:
        if m.get("id") not in known_demand_ids:
            if m.get("status") != "closed":
                errors.append(
                    f"Additional PI Demand matter {m.get('id')} ('{m.get('description', '')}') "
                    f"has status '{m.get('status')}', expected 'closed'."
                )
            if not m.get("closedDate"):
                errors.append(
                    f"Additional PI Demand matter {m.get('id')} ('{m.get('description', '')}') "
                    f"has no closedDate set."
                )

    if closed_count < 3:
        errors.append(
            f"Only {closed_count} of the known Demand-stage PI matters are closed, expected at least 3."
        )

    if errors:
        return False, "Not all open PI matters at Demand stage were closed. " + " | ".join(errors)

    return True, "All open Personal Injury matters at Demand stage have been closed with closedDate set."
