import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    firm_settings = state.get("firmSettings", {})
    default_template_id = firm_settings.get("defaultTemplateId")

    if default_template_id is None:
        return False, "firmSettings.defaultTemplateId is not set in application state."

    if default_template_id != "template_7":
        return False, (
            f"firmSettings.defaultTemplateId is '{default_template_id}', "
            f"expected 'template_7' (Personal Injury - Slip and Fall)."
        )

    return True, "Firm default template has been changed to 'Personal Injury - Slip and Fall' (template_7)."
