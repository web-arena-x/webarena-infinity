import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Find practice area IDs
    practice_areas = state.get("practiceAreas", [])
    family_law_pa = next(
        (pa for pa in practice_areas if pa.get("id") == "pa_2" or "family law" in pa.get("name", "").lower()),
        None
    )
    criminal_defense_pa = next(
        (pa for pa in practice_areas if pa.get("id") == "pa_3" or "criminal defense" in pa.get("name", "").lower()),
        None
    )

    if family_law_pa is None:
        errors.append("Could not find Family Law practice area.")
    if criminal_defense_pa is None:
        errors.append("Could not find Criminal Defense practice area.")

    if errors:
        return False, " | ".join(errors)

    family_law_id = family_law_pa["id"]
    criminal_defense_id = criminal_defense_pa["id"]

    matters = state.get("matters", [])

    # Check 1: Matter for Jerome Baptiste (contact_62), Family Law, Diana Reyes (user_3), hourly
    baptiste_matter = next(
        (m for m in matters
         if m.get("clientId") == "contact_62"
         and m.get("practiceAreaId") == family_law_id
         and m.get("responsibleAttorneyId") == "user_3"
         and m.get("billingMethod") == "hourly"),
        None
    )
    if baptiste_matter is None:
        # Try broader search to give better error messages
        baptiste_any = [m for m in matters if m.get("clientId") == "contact_62"]
        family_law_any = [m for m in matters if m.get("practiceAreaId") == family_law_id and m.get("clientId") == "contact_62"]
        if not baptiste_any:
            errors.append("No matter found with clientId 'contact_62' (Jerome Baptiste).")
        elif not family_law_any:
            errors.append(
                f"Found matter(s) for Jerome Baptiste but none in Family Law. "
                f"Practice areas: {[m.get('practiceAreaId') for m in baptiste_any]}."
            )
        else:
            details = [
                f"attorney={m.get('responsibleAttorneyId')}, billing={m.get('billingMethod')}"
                for m in family_law_any
            ]
            errors.append(
                f"Found Family Law matter for Baptiste but criteria mismatch. "
                f"Expected attorney=user_3, billing=hourly. Found: {details}."
            )

    # Check 2: Matter for Richard Hernandez (contact_29), Criminal Defense, Robert Jackson (user_8), flat_rate
    hernandez_matter = next(
        (m for m in matters
         if m.get("clientId") == "contact_29"
         and m.get("practiceAreaId") == criminal_defense_id
         and m.get("responsibleAttorneyId") == "user_8"
         and m.get("billingMethod") == "flat_rate"),
        None
    )
    if hernandez_matter is None:
        hernandez_any = [m for m in matters if m.get("clientId") == "contact_29"]
        criminal_any = [m for m in matters if m.get("practiceAreaId") == criminal_defense_id and m.get("clientId") == "contact_29"]
        if not hernandez_any:
            errors.append("No matter found with clientId 'contact_29' (Richard Hernandez).")
        elif not criminal_any:
            errors.append(
                f"Found matter(s) for Richard Hernandez but none in Criminal Defense. "
                f"Practice areas: {[m.get('practiceAreaId') for m in hernandez_any]}."
            )
        else:
            details = [
                f"attorney={m.get('responsibleAttorneyId')}, billing={m.get('billingMethod')}"
                for m in criminal_any
            ]
            errors.append(
                f"Found Criminal Defense matter for Hernandez but criteria mismatch. "
                f"Expected attorney=user_8, billing=flat_rate. Found: {details}."
            )

    if errors:
        return False, "New matters not created correctly. " + " | ".join(errors)

    return True, "Both new matters created: Jerome Baptiste (Family Law, Diana Reyes, hourly) and Richard Hernandez (Criminal Defense, Robert Jackson, flat_rate)."
