import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Find Aisha Johnson contact
    contacts = state.get("contacts", [])
    aisha = next(
        (c for c in contacts if "aisha" in c.get("displayName", "").lower() and "johnson" in c.get("displayName", "").lower()),
        None
    )

    aisha_id = "contact_5"
    if aisha is not None:
        aisha_id = aisha.get("id", "contact_5")

    # Find Personal Injury practice area
    practice_areas = state.get("practiceAreas", [])
    pi_pa = next(
        (pa for pa in practice_areas if pa.get("id") == "pa_1" or "personal injury" in pa.get("name", "").lower()),
        None
    )

    if pi_pa is None:
        return False, "Could not find Personal Injury practice area."

    pi_pa_id = pi_pa["id"]

    # Find the NEW matter for Aisha Johnson: PI, contingency, with ~40% fee.
    # Existing Aisha Johnson PI matters (matter_2, matter_20) both have 33.33%.
    # The new matter should have ~40%, so we filter by that.
    aisha_pi_matters = [
        m for m in state.get("matters", [])
        if m.get("clientId") == aisha_id
        and m.get("practiceAreaId") == pi_pa_id
        and m.get("billingMethod") == "contingency"
    ]

    # Find the one with ~40% contingency fee (the new matter)
    new_matter = None
    for m in aisha_pi_matters:
        billing = m.get("billing", {})
        contingency_fee = billing.get("contingencyFee", {})
        percentage = contingency_fee.get("percentage")
        if percentage is not None and abs(float(percentage) - 40) <= 1:
            new_matter = m
            break

    if new_matter is None:
        existing_info = [
            f"{m.get('id')} ({m.get('description', 'N/A')[:50]}, fee={m.get('billing', {}).get('contingencyFee', {}).get('percentage')}%)"
            for m in aisha_pi_matters
        ]
        errors.append(
            f"No new PI matter found for Aisha Johnson with ~40% contingency fee. "
            f"Found Aisha PI matters: {existing_info}"
        )
    else:
        matter_id = new_matter.get("id")

        # Check Marcus Williams as responsible attorney
        resp_attorney = new_matter.get("responsibleAttorneyId", "")
        users = state.get("users", [])
        marcus = next(
            (u for u in users if "marcus" in u.get("name", "").lower() and "williams" in u.get("name", "").lower()),
            None
        )
        marcus_id = marcus.get("id") if marcus else "user_2"
        if resp_attorney != marcus_id:
            errors.append(
                f"Matter {matter_id} responsibleAttorneyId is {resp_attorney}, expected {marcus_id} (Marcus Williams)."
            )

        # Check for a damage entry for this matter with amount close to 15000
        damages = state.get("damages", [])
        matter_damages = [d for d in damages if d.get("matterId") == matter_id]

        damage_found = any(
            abs(float(d.get("amount", 0)) - 15000) < 500
            for d in matter_damages
        )

        if not damage_found:
            damage_amounts = [d.get("amount") for d in matter_damages]
            errors.append(
                f"No damage entry found for matter {matter_id} with amount close to $15,000. "
                f"Found damage amounts: {damage_amounts}."
            )

    if errors:
        return False, "New PI matter for Aisha Johnson not set up correctly. " + " | ".join(errors)

    return True, (
        "New Personal Injury matter created for Aisha Johnson with contingency billing at ~40% "
        "and a damage entry of ~$15,000."
    )
