import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []
    matters = state.get("matters", [])

    # Helper to find a matter by description keywords
    def find_matter(keywords):
        for m in matters:
            desc = m.get("description", "").lower()
            if all(kw.lower() in desc for kw in keywords):
                return m
        return None

    # Pending Family Law matters that should now be closed
    pending_checks = [
        (["sato", "adoption"], "Sato Adoption (matter_32)"),
        (["petrovic", "annulment"], "Petrovic Annulment (matter_41)"),
    ]

    for keywords, label in pending_checks:
        matter = find_matter(keywords)
        if matter is None:
            errors.append(f"Could not find matter matching '{label}'.")
            continue

        if matter.get("status") != "closed":
            errors.append(
                f"{label} (id={matter.get('id')}) has status '{matter.get('status')}', expected 'closed'."
            )

    # Open Family Law matters at Consultation that should now be at Filing (stage_2_2)
    filing_stage_id = "stage_2_2"
    consultation_checks = [
        (["stone", "domestic violence"], "Stone v. Stone - Domestic violence (matter_33)"),
        (["baptiste", "contested divorce"], "Baptiste v. Baptiste - Contested divorce (matter_35)"),
        (["sato", "postnuptial"], "Sato Postnuptial (matter_42)"),
    ]

    for keywords, label in consultation_checks:
        matter = find_matter(keywords)
        if matter is None:
            errors.append(f"Could not find matter matching '{label}'.")
            continue

        if matter.get("stageId") != filing_stage_id:
            errors.append(
                f"{label} (id={matter.get('id')}) has stageId '{matter.get('stageId')}', "
                f"expected '{filing_stage_id}' (Filing)."
            )

    if errors:
        return False, (
            "Family Law matter updates incomplete. " + " | ".join(errors)
        )

    return True, (
        "All pending Family Law matters closed (Sato Adoption, Petrovic Annulment) "
        "and all open Family Law matters at Consultation moved to Filing "
        "(Stone v. Stone, Baptiste v. Baptiste, Sato Postnuptial)."
    )
