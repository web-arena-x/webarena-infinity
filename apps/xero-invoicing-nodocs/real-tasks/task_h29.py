"""Verify: Change default tax to AU GST (10%) and create AUD draft for CloudBridge."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    state = requests.get(f"{server_url}/api/state", timeout=5).json()
    invoices = state.get("invoices", [])
    settings = state.get("settings", {})

    errors = []

    # Check default tax rate changed to AU GST on Income (tax_7)
    if settings.get("defaultTaxRateId") != "tax_7":
        errors.append(f"defaultTaxRateId is '{settings.get('defaultTaxRateId')}', expected 'tax_7'")

    # Check new AUD draft invoice for CloudBridge (con_21)
    seed_ids = {f"inv_{n}" for n in range(1, 114)}
    new_invoices = [i for i in invoices
                    if i["id"] not in seed_ids
                    and i["contactId"] == "con_21"]

    if not new_invoices:
        errors.append("No new invoice found for CloudBridge Software (con_21)")
    else:
        inv = new_invoices[0]
        if inv.get("status") != "draft":
            errors.append(f"Invoice status is '{inv.get('status')}', expected 'draft'")
        if inv.get("currency") != "AUD":
            errors.append(f"Invoice currency is '{inv.get('currency')}', expected 'AUD'")
        if inv.get("issueDate") != "2026-03-18":
            errors.append(f"Issue date is '{inv.get('issueDate')}', expected '2026-03-18'")
        if inv.get("dueDate") != "2026-06-18":
            errors.append(f"Due date is '{inv.get('dueDate')}', expected '2026-06-18'")

        lis = inv.get("lineItems", [])
        saas = next((l for l in lis if "saas" in l.get("description", "").lower()
                      or "license" in l.get("description", "").lower()), None)
        if not saas:
            errors.append("No line item matching 'SaaS' or 'license' found")
        elif abs(saas["quantity"] - 1) > 0.01 or abs(saas["unitPrice"] - 9600) > 0.01:
            errors.append(f"SaaS line: qty={saas['quantity']} price={saas['unitPrice']}, expected 1 x $9,600")

    if errors:
        return False, "; ".join(errors)
    return True, "Default tax changed to AU GST and new AUD draft created for CloudBridge"
