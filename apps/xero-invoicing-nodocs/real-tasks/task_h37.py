"""Verify: Delete all draft invoices with empty reference field."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    state = requests.get(f"{server_url}/api/state", timeout=5).json()
    invoices = state.get("invoices", [])

    # In seed state: inv_18, inv_20, inv_42, inv_93 are drafts with empty reference
    expected_deleted = {"inv_18", "inv_20", "inv_42", "inv_93"}
    errors = []

    for inv_id in expected_deleted:
        if any(i["id"] == inv_id for i in invoices):
            inv = next(i for i in invoices if i["id"] == inv_id)
            errors.append(f"Invoice {inv['invoiceNumber']} ({inv_id}) should have been deleted but still exists")

    # Verify no remaining drafts with empty reference
    remaining = [i for i in invoices if i["status"] == "draft" and not i.get("reference")]
    if remaining:
        nums = [i["invoiceNumber"] for i in remaining]
        errors.append(f"Remaining draft(s) with empty reference: {', '.join(nums)}")

    if errors:
        return False, "; ".join(errors)
    return True, f"All {len(expected_deleted)} draft invoice(s) with empty reference deleted"
