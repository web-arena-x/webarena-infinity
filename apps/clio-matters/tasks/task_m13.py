import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find Robert O'Malley contact
    contacts = state.get("contacts", [])
    omalley = next(
        (c for c in contacts if "O'Malley" in c.get("displayName", "")),
        None
    )
    if omalley is None:
        return False, "Could not find a contact with displayName containing \"O'Malley\"."
    omalley_id = omalley.get("id")

    # Find Real Estate practice area
    practice_areas = state.get("practiceAreas", [])
    real_estate = next(
        (pa for pa in practice_areas if "real estate" in pa.get("name", "").lower()),
        None
    )
    if real_estate is None:
        return False, "Could not find a practice area named 'Real Estate'."
    real_estate_id = real_estate.get("id")

    # Find Rachel Goldstein user
    users = state.get("users", [])
    goldstein = next(
        (u for u in users if "Goldstein" in u.get("name", "")),
        None
    )
    if goldstein is None:
        return False, "Could not find a user with name containing 'Goldstein'."
    goldstein_id = goldstein.get("id")

    # Find a new matter matching all criteria
    matters = state.get("matters", [])
    matching = [
        m for m in matters
        if m.get("clientId") == omalley_id
        and m.get("practiceAreaId") == real_estate_id
        and m.get("billingMethod") == "flat_rate"
        and m.get("responsibleAttorneyId") == goldstein_id
    ]

    if not matching:
        # Provide diagnostic info
        client_matches = [m.get("id") for m in matters if m.get("clientId") == omalley_id]
        return False, (
            f"No matter found with clientId='{omalley_id}' (O'Malley), "
            f"practiceAreaId='{real_estate_id}' (Real Estate), "
            f"billingMethod='flat_rate', and responsibleAttorneyId='{goldstein_id}' (Goldstein). "
            f"Matters with O'Malley as client: {client_matches}."
        )

    return True, "New Real Estate matter exists for Robert O'Malley with flat_rate billing and Rachel Goldstein as responsible attorney."
