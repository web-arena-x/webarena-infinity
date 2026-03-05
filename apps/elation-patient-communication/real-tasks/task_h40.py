import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Add two CPT codes and a new practice location."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state.get("practiceSettings", {})

    # Check CPT code 99458
    cpt_codes = settings.get("cptCodes", [])
    code_99458 = next(
        (c for c in cpt_codes if c.get("code") == "99458"),
        None,
    )
    if code_99458 is None:
        return False, "CPT code '99458' not found."
    if "telehealth" not in code_99458.get("description", "").lower():
        return False, (
            f"CPT 99458 description '{code_99458.get('description')}' "
            f"does not mention telehealth."
        )

    # Check CPT code 99459
    code_99459 = next(
        (c for c in cpt_codes if c.get("code") == "99459"),
        None,
    )
    if code_99459 is None:
        return False, "CPT code '99459' not found."
    if "telehealth" not in code_99459.get("description", "").lower():
        return False, (
            f"CPT 99459 description '{code_99459.get('description')}' "
            f"does not mention telehealth."
        )

    # Check Fremont Clinic location
    locations = settings.get("practiceLocations", [])
    fremont = next(
        (loc for loc in locations if "Fremont" in (loc.get("name") or "")),
        None,
    )
    if fremont is None:
        return False, "Practice location 'Fremont Clinic' not found."
    if fremont.get("posCode") != "11":
        return False, (
            f"Fremont Clinic POS code is '{fremont.get('posCode')}', "
            f"expected '11'."
        )

    return True, (
        "CPT codes 99458 and 99459 added, and Fremont Clinic location created."
    )
