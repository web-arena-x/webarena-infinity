import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    presentations = state.get("presentations", [])
    for pres in presentations:
        if pres.get("title") == "Budget Review Q2":
            tags = pres.get("tags", [])
            if "finance" not in tags:
                return False, f"Presentation 'Budget Review Q2' found but tags {tags} do not contain 'finance'."
            if "quarterly" not in tags:
                return False, f"Presentation 'Budget Review Q2' found but tags {tags} do not contain 'quarterly'."
            if pres.get("theme") != "corporate":
                return False, f"Presentation 'Budget Review Q2' found but theme is '{pres.get('theme')}', expected 'corporate'."
            if pres.get("status") != "draft":
                return False, f"Presentation 'Budget Review Q2' found but status is '{pres.get('status')}', expected 'draft'."
            return True, "Presentation 'Budget Review Q2' exists with correct tags, theme, and draft status."

    return False, "No presentation with title 'Budget Review Q2' found."
