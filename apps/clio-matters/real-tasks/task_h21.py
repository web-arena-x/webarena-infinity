import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    matters = state.get("matters", [])
    practice_areas = state.get("practiceAreas", [])

    # Find PI practice area id
    pi_id = None
    for pa in practice_areas:
        if pa.get("name") == "Personal Injury":
            pi_id = pa.get("id")
            break

    if not pi_id:
        return False, "Personal Injury practice area not found."

    # Find open PI case with largest total damages
    best_matter = None
    best_total = -1
    for m in matters:
        if m.get("practiceAreaId") == pi_id and m.get("status") == "Open":
            total = sum(d.get("amount", 0) for d in m.get("damages", []))
            if total > best_total:
                best_total = total
                best_matter = m

    if not best_matter:
        return False, "No open PI matter with damages found."

    # The Rodriguez case (mat_001) should be the one with highest damages
    # Check it has a Punitive Damages entry for $100,000
    damages = best_matter.get("damages", [])
    punitive = [d for d in damages
                if d.get("type") == "Punitive Damages" and d.get("amount") == 100000]

    if not punitive:
        return False, (
            f"No Punitive Damages entry for $100,000 found on matter "
            f"'{best_matter.get('description')}' (highest damages: ${best_total:,.0f})."
        )

    d = punitive[0]
    if d.get("category") != "Other":
        return False, f"Punitive Damages category is '{d.get('category')}', expected 'Other'."

    return True, "Punitive Damages of $100,000 added to the PI case with the largest total damages."
