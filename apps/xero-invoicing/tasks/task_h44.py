import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Retail theme seed state: showTaxNumber=true, showPaymentAdvice=false.
    # After toggling both, expected: showTaxNumber=false, showPaymentAdvice=true.
    theme = None
    for t in state.get("brandingThemes", []):
        if t.get("id") == "theme_retail":
            theme = t
            break

    if theme is None:
        return False, "Retail branding theme not found."

    if theme.get("showTaxNumber") is not False:
        return False, (
            f"Retail theme showTaxNumber is {theme.get('showTaxNumber')}, "
            f"expected False (toggled from True)."
        )

    if theme.get("showPaymentAdvice") is not True:
        return False, (
            f"Retail theme showPaymentAdvice is {theme.get('showPaymentAdvice')}, "
            f"expected True (toggled from False)."
        )

    return True, (
        "Retail branding theme toggled: showTaxNumber=False, showPaymentAdvice=True."
    )
