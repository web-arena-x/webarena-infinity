import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    templates = state.get("matterTemplates", [])

    criminal_template = next(
        (t for t in templates if t.get("name") == "Criminal Defense - Misdemeanor"),
        None
    )
    if criminal_template is None:
        return False, "Could not find template named 'Criminal Defense - Misdemeanor'."

    if criminal_template.get("isDefault") is not True:
        return False, f"Criminal Defense - Misdemeanor template isDefault is {criminal_template.get('isDefault')}, expected True."

    pi_template = next(
        (t for t in templates if t.get("name") == "Personal Injury - Auto Accident"),
        None
    )
    if pi_template is not None and pi_template.get("isDefault") is not False:
        return False, f"Personal Injury - Auto Accident template isDefault is {pi_template.get('isDefault')}, expected False."

    return True, "Criminal Defense - Misdemeanor is now the default template."
