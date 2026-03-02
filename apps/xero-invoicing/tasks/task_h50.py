import requests


SEED_INVOICE_IDS = {
    "inv_000", "inv_001", "inv_002", "inv_003", "inv_004", "inv_005",
    "inv_006", "inv_007", "inv_008", "inv_009", "inv_010", "inv_011",
    "inv_012", "inv_013", "inv_014", "inv_015", "inv_016", "inv_017",
    "inv_018", "inv_019", "inv_020", "inv_021", "inv_022", "inv_023",
    "inv_024", "inv_025",
}

SEED_THEME_IDS = {"theme_standard", "theme_professional", "theme_simple", "theme_retail"}


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Check for 'Consulting' branding theme
    consulting_theme = None
    for t in state.get("brandingThemes", []):
        if t.get("name") == "Consulting":
            consulting_theme = t
            break

    if consulting_theme is None:
        return False, "No branding theme named 'Consulting' found."

    if consulting_theme.get("paymentTerms") != "Net 21 days":
        return False, (
            f"Consulting theme paymentTerms is '{consulting_theme.get('paymentTerms')}', "
            f"expected 'Net 21 days'."
        )

    if consulting_theme.get("showTaxNumber") is not True:
        return False, (
            f"Consulting theme showTaxNumber is {consulting_theme.get('showTaxNumber')}, "
            f"expected True."
        )

    # Check for new invoice for Wellington & Partners (con_016) using this theme
    new_inv = None
    for inv in state.get("invoices", []):
        if (inv.get("contactId") == "con_016"
                and inv.get("id") not in SEED_INVOICE_IDS):
            new_inv = inv
            break

    if new_inv is None:
        return False, (
            "No new invoice found for Wellington & Partners Accounting (con_016)."
        )

    if new_inv.get("currency") != "NZD":
        return False, (
            f"New invoice currency is '{new_inv.get('currency')}', expected 'NZD'."
        )

    if new_inv.get("brandingThemeId") != consulting_theme.get("id"):
        return False, (
            f"New invoice branding theme is '{new_inv.get('brandingThemeId')}', "
            f"expected '{consulting_theme.get('id')}' (Consulting)."
        )

    # Check line item: 4 hours of consulting at ~$250
    line_items = new_inv.get("lineItems", [])
    found = False
    for li in line_items:
        price = float(li.get("unitPrice", 0))
        qty = li.get("quantity", 0)
        if abs(price - 250.00) < 10.00 and qty == 4:
            found = True
            break

    if not found:
        items = [(li.get("unitPrice"), li.get("quantity")) for li in line_items]
        return False, (
            f"No line item with qty 4 and unitPrice ~$250 (consulting) found. Items: {items}."
        )

    return True, (
        f"Branding theme 'Consulting' created. New invoice '{new_inv.get('number')}' "
        f"for Wellington & Partners in NZD with 4 hours consulting using the Consulting theme."
    )
