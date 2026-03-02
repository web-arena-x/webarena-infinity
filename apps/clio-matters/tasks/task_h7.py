import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Find Criminal Defense practice area
    practice_areas = state.get("practiceAreas", [])
    cd_pa = next(
        (pa for pa in practice_areas
         if pa.get("id") == "pa_3" or "criminal defense" in pa.get("name", "").lower()),
        None
    )

    if cd_pa is None:
        return False, "Could not find Criminal Defense practice area."

    cd_pa_id = cd_pa.get("id")

    # Identify the Pre-Trial stage (stage_3_2)
    pre_trial_stage_id = "stage_3_2"
    stages = cd_pa.get("stages", [])
    pre_trial_stage = next(
        (s for s in stages if s.get("id") == pre_trial_stage_id or "pre-trial" in s.get("name", "").lower() or "pretrial" in s.get("name", "").lower()),
        None
    )

    if pre_trial_stage is not None:
        pre_trial_stage_id = pre_trial_stage.get("id")

    # Known matters that were at Arraignment (stage_3_1)
    known_arraignment_ids = ["matter_48", "matter_51", "matter_120"]
    matters_by_id = {m.get("id"): m for m in state.get("matters", [])}

    moved_count = 0
    for mid in known_arraignment_ids:
        matter = matters_by_id.get(mid)
        if matter is None:
            errors.append(f"Matter {mid} not found in state.")
            continue

        if matter.get("stageId") != pre_trial_stage_id:
            errors.append(
                f"Matter {mid} ('{matter.get('description', '')}') has stageId "
                f"'{matter.get('stageId')}', expected '{pre_trial_stage_id}' (Pre-Trial)."
            )
        else:
            moved_count += 1

    # Also check if any other CD matters are still at Arraignment
    arraignment_stage_id = "stage_3_1"
    remaining_at_arraignment = [
        m for m in state.get("matters", [])
        if m.get("practiceAreaId") == cd_pa_id and m.get("stageId") == arraignment_stage_id
    ]

    if remaining_at_arraignment:
        remaining_descs = [
            f"{m.get('id')} ('{m.get('description', '')}')" for m in remaining_at_arraignment
        ]
        errors.append(
            f"{len(remaining_at_arraignment)} Criminal Defense matter(s) still at Arraignment: "
            f"{', '.join(remaining_descs)}."
        )

    if moved_count < 2:
        errors.append(
            f"Only {moved_count} of the known Arraignment matters moved to Pre-Trial, expected at least 2."
        )

    if errors:
        return False, (
            "Not all Criminal Defense matters moved from Arraignment to Pre-Trial. "
            + " | ".join(errors)
        )

    return True, (
        f"All Criminal Defense matters at Arraignment have been moved to Pre-Trial. "
        f"{moved_count} known matters confirmed at Pre-Trial stage."
    )
