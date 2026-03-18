"""Verify: Green Valley Organics — void overdue, approve awaiting, delete drafts."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    state = requests.get(f"{server_url}/api/state", timeout=5).json()
    invoices = state.get("invoices", [])

    errors = []

    # inv_107 should be voided (was overdue)
    inv_107 = next((i for i in invoices if i["id"] == "inv_107"), None)
    if not inv_107:
        errors.append("Invoice inv_107 not found")
    elif inv_107["status"] != "voided":
        errors.append(f"Invoice INV-0107 (inv_107) status is '{inv_107['status']}', expected 'voided'")
    elif not inv_107.get("voidedAt"):
        errors.append("Invoice INV-0107 missing voidedAt timestamp")

    # inv_32 should be approved (was awaiting_approval)
    inv_32 = next((i for i in invoices if i["id"] == "inv_32"), None)
    if not inv_32:
        errors.append("Invoice inv_32 not found")
    elif inv_32["status"] != "awaiting_payment":
        errors.append(f"Invoice INV-0032 (inv_32) status is '{inv_32['status']}', expected 'awaiting_payment'")

    # inv_82 should be deleted (was draft)
    inv_82 = next((i for i in invoices if i["id"] == "inv_82"), None)
    if inv_82:
        errors.append(f"Invoice INV-0082 (inv_82) should have been deleted but still exists with status '{inv_82['status']}'")

    # Verify no overdue/awaiting_approval/draft remain for con_7
    gv_invoices = [i for i in invoices if i["contactId"] == "con_7"]
    bad = [i for i in gv_invoices if i["status"] in ("overdue", "awaiting_approval", "draft")]
    if bad:
        for i in bad:
            errors.append(f"Green Valley invoice {i['invoiceNumber']} still has status '{i['status']}'")

    if errors:
        return False, "; ".join(errors)
    return True, "Green Valley Organics: 1 voided, 1 approved, 1 deleted"
