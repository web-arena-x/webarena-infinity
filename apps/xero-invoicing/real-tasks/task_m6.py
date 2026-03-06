import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    themes = state.get("brandingThemes", [])
    found = None
    for t in themes:
        if t.get("name", "").lower() == "corporate executive":
            found = t
            break

    if found is None:
        return False, "Branding theme 'Corporate Executive' not found."

    payment_terms = found.get("paymentTerms", "")
    if "net 14" not in payment_terms.lower():
        return False, f"Theme 'Corporate Executive' paymentTerms is '{payment_terms}', expected to contain 'Net 14 days'."

    return True, "Branding theme 'Corporate Executive' created with payment terms 'Net 14 days'."
