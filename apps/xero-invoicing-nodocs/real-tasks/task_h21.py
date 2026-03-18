"""Verify: Delete every draft invoice belonging to a contact in Auckland."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    state = requests.get(f"{server_url}/api/state", timeout=5).json()
    invoices = state.get("invoices", [])
    contacts = state.get("contacts", [])

    auckland_ids = {c["id"] for c in contacts if c.get("billingAddress", {}).get("city") == "Auckland"}

    # Specific drafts that should be deleted: inv_5 (con_5), inv_83 (con_8), inv_108 (con_8)
    expected_deleted = {"inv_5", "inv_83", "inv_108"}
    errors = []

    for inv_id in expected_deleted:
        if any(i["id"] == inv_id for i in invoices):
            errors.append(f"Invoice {inv_id} should have been deleted but still exists")

    # Also verify no remaining drafts for Auckland contacts
    remaining = [i for i in invoices if i["status"] == "draft" and i["contactId"] in auckland_ids]
    if remaining:
        nums = [i["invoiceNumber"] for i in remaining]
        errors.append(f"Remaining draft(s) for Auckland contacts: {', '.join(nums)}")

    if errors:
        return False, "; ".join(errors)
    return True, f"All {len(expected_deleted)} draft invoice(s) for Auckland contacts deleted"
