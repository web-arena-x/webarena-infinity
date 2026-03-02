import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    themes = state.get("brandingThemes", [])
    gov_theme = None
    for t in themes:
        if t.get("name") == "Government":
            gov_theme = t
            break

    if gov_theme is None:
        return False, "No branding theme named 'Government' found."

    if gov_theme.get("showTaxNumber") is not True:
        return False, f"Government theme showTaxNumber is {gov_theme.get('showTaxNumber')}, expected True."

    if gov_theme.get("showPaymentAdvice") is not False:
        return False, f"Government theme showPaymentAdvice is {gov_theme.get('showPaymentAdvice')}, expected False."

    pt = gov_theme.get("paymentTerms", "")
    if pt != "Net 45 days from invoice date":
        return False, f"Government theme paymentTerms is '{pt}', expected 'Net 45 days from invoice date'."

    tc = gov_theme.get("termsAndConditions", "")
    if tc != "Subject to government procurement regulations.":
        return False, f"Government theme termsAndConditions is '{tc}', expected 'Subject to government procurement regulations.'"

    if gov_theme.get("isDefault") is not True:
        return False, "Government theme is not set as the default."

    # Verify no other theme is also default
    other_defaults = [t.get("name") for t in themes if t.get("isDefault") and t.get("name") != "Government"]
    if other_defaults:
        return False, f"Other themes are also marked as default: {other_defaults}."

    return True, (
        "Branding theme 'Government' created with correct settings and set as default."
    )
