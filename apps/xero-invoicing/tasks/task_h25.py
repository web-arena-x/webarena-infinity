import requests


# Seed invoice IDs — all invoices present at startup
SEED_INVOICE_IDS = {
    "inv_000", "inv_001", "inv_002", "inv_003", "inv_004", "inv_005",
    "inv_006", "inv_007", "inv_008", "inv_009", "inv_010", "inv_011",
    "inv_012", "inv_013", "inv_014", "inv_015", "inv_016", "inv_017",
    "inv_018", "inv_019", "inv_020", "inv_021", "inv_022", "inv_023",
    "inv_024", "inv_025",
}


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # The most expensive paid invoice is INV-0064 ($23,100, Northern Territory Power Corp, con_017)
    # A new draft copy should exist for con_017
    new_inv = None
    for inv in state.get("invoices", []):
        if inv.get("contactId") == "con_017" and inv.get("id") not in SEED_INVOICE_IDS:
            new_inv = inv
            break

    if new_inv is None:
        return False, (
            "No new invoice found for Northern Territory Power Corp (con_017). "
            "The most expensive paid invoice is INV-0064 ($23,100)."
        )

    if new_inv.get("status") != "draft":
        return False, (
            f"New invoice '{new_inv.get('number')}' status is '{new_inv.get('status')}', "
            f"expected 'draft'."
        )

    total = float(new_inv.get("total", 0))
    if abs(total - 23100.00) > 100.00:
        return False, (
            f"New invoice total is ${total:.2f}, expected ~$23,100.00 "
            f"(copy of INV-0064)."
        )

    return True, (
        f"New draft invoice '{new_inv.get('number')}' created as a copy of INV-0064 "
        f"(Northern Territory Power Corp, $23,100)."
    )
