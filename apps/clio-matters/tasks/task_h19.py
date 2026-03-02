import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Find Brennan hotel slip-and-fall matter
    matters = state.get("matters", [])
    brennan = None
    for m in matters:
        desc = m.get("description", "").lower()
        if "brennan" in desc and ("oceanview" in desc or "hotel" in desc or "slip" in desc):
            brennan = m
            break

    if brennan is None:
        return False, "Could not find Brennan hotel matter (description containing 'Brennan' and 'Oceanview' or 'Hotel' or 'slip')."

    matter_id = brennan["id"]

    # Check damages
    all_damages = state.get("damages", [])
    matter_damages = [d for d in all_damages if d.get("matterId") == matter_id]

    if len(matter_damages) < 3:
        errors.append(
            f"Only {len(matter_damages)} damage(s) found for Brennan matter, expected at least 3."
        )

    # Check for specific damage amounts
    damage_amounts = []
    for d in matter_damages:
        try:
            damage_amounts.append(float(d.get("amount", 0)))
        except (TypeError, ValueError):
            damage_amounts.append(0)

    # Damage close to 8500
    has_8500 = any(abs(a - 8500) < 1500 for a in damage_amounts)
    if not has_8500:
        errors.append(
            f"No damage with amount close to $8,500 found. Damage amounts: {damage_amounts}."
        )

    # Damage close to 12000
    has_12000 = any(abs(a - 12000) < 2000 for a in damage_amounts)
    if not has_12000:
        errors.append(
            f"No damage with amount close to $12,000 found. Damage amounts: {damage_amounts}."
        )

    # Damage close to 45000
    has_45000 = any(abs(a - 45000) < 5000 for a in damage_amounts)
    if not has_45000:
        errors.append(
            f"No damage with amount close to $45,000 found. Damage amounts: {damage_amounts}."
        )

    if errors:
        return False, "Brennan damages not set up correctly. " + " | ".join(errors)

    return True, "Brennan hotel matter has 3 damages: ~$8,500, ~$12,000, and ~$45,000."
