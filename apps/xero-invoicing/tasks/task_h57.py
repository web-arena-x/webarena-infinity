import requests


SEED_REPEAT_IDS = {"rep_001", "rep_002", "rep_003", "rep_004", "rep_005"}


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # New repeating invoice for Vanguard Security Systems (con_023):
    # weekly, Retail template, approved for sending, June 2026 start, December 2026 end,
    # 2 hours dev at ~$185
    new_ri = None
    for ri in state.get("repeatingInvoices", []):
        if ri.get("contactId") == "con_023" and ri.get("id") not in SEED_REPEAT_IDS:
            new_ri = ri
            break

    if new_ri is None:
        return False, (
            "No new repeating invoice found for Vanguard Security Systems (con_023)."
        )

    if new_ri.get("frequency") != "weekly":
        return False, (
            f"Repeating invoice frequency is '{new_ri.get('frequency')}', expected 'weekly'."
        )

    if new_ri.get("brandingThemeId") != "theme_retail":
        return False, (
            f"Repeating invoice branding theme is '{new_ri.get('brandingThemeId')}', "
            f"expected 'theme_retail' (Retail)."
        )

    if new_ri.get("saveAs") != "approved_for_sending":
        return False, (
            f"Repeating invoice saveAs is '{new_ri.get('saveAs')}', "
            f"expected 'approved_for_sending'."
        )

    start = new_ri.get("startDate", "")
    if not start.startswith("2026-06"):
        return False, f"Start date is '{start}', expected to start in June 2026."

    end = new_ri.get("endDate", "")
    if not end.startswith("2026-12"):
        return False, f"End date is '{end}', expected to end in December 2026."

    # Check line item: 2 hours dev at ~$185
    line_items = new_ri.get("lineItems", [])
    found = False
    for li in line_items:
        price = float(li.get("unitPrice", 0))
        qty = li.get("quantity", 0)
        if abs(price - 185.00) < 10.00 and qty == 2:
            found = True
            break

    if not found:
        items = [(li.get("unitPrice"), li.get("quantity")) for li in line_items]
        return False, (
            f"No line item with qty 2 and unitPrice ~$185 (development) found. Items: {items}."
        )

    return True, (
        "Weekly repeating invoice for Vanguard Security Systems created: "
        "Retail template, approved for sending, June-December 2026, 2 hrs development."
    )
