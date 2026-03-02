import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    templates = state.get("matterTemplates", [])

    estate_template = next(
        (t for t in templates if t.get("name") == "Estate Planning - Comprehensive"),
        None
    )

    if estate_template is not None:
        return False, "Template 'Estate Planning - Comprehensive' still exists in matterTemplates."

    return True, "Estate Planning - Comprehensive template has been deleted."
