import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find the template (now renamed)
    tmpl = None
    for t in state.get("matterTemplates", []):
        if t.get("name") == "Personal Injury - General":
            tmpl = t
            break

    if not tmpl:
        # Check if old name still exists
        old = any(
            t.get("name") == "Personal Injury - Auto Accident"
            for t in state.get("matterTemplates", [])
        )
        if old:
            return False, "Template still named 'Personal Injury - Auto Accident', expected 'Personal Injury - General'."
        return False, "Template 'Personal Injury - General' not found."

    errors = []

    if tmpl.get("billingMethod") != "hourly":
        errors.append(
            f"Billing method is '{tmpl.get('billingMethod')}', expected 'hourly'"
        )

    if tmpl.get("isDefault") is not False:
        errors.append(
            f"isDefault is {tmpl.get('isDefault')}, expected False"
        )

    # David Kim is usr_004
    if tmpl.get("responsibleAttorneyId") != "usr_004":
        errors.append(
            f"Responsible attorney is '{tmpl.get('responsibleAttorneyId')}', "
            f"expected 'usr_004' (David Kim)"
        )

    if errors:
        return False, "; ".join(errors)

    return True, "PI template renamed to General, hourly billing, not default, David Kim as attorney."
