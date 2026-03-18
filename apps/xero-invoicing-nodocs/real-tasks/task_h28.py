"""Verify: Copy the highest-total paid invoice (inv_48, $88,550) as a draft."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    state = requests.get(f"{server_url}/api/state", timeout=5).json()
    invoices = state.get("invoices", [])

    # inv_48 is the highest-total paid invoice for Redwood Property Management (con_23)
    orig = next((i for i in invoices if i["id"] == "inv_48"), None)
    if not orig:
        return False, "Original invoice inv_48 not found"

    # Find a new draft for the same contact
    seed_ids = {f"inv_{n}" for n in range(1, 114)}
    new_drafts = [i for i in invoices
                  if i["id"] not in seed_ids
                  and i["status"] == "draft"
                  and i["contactId"] == "con_23"]

    if not new_drafts:
        return False, "No new draft invoice found for Redwood Property Management (con_23)"

    errors = []
    copy = new_drafts[0]

    # Verify line items match original (4 items)
    orig_descs = sorted([li["description"] for li in orig["lineItems"]])
    copy_descs = sorted([li.get("description", "") for li in copy.get("lineItems", [])])

    if len(copy.get("lineItems", [])) != len(orig["lineItems"]):
        errors.append(f"Copy has {len(copy.get('lineItems', []))} line items, expected {len(orig['lineItems'])}")
    elif orig_descs != copy_descs:
        errors.append(f"Line item descriptions don't match original")

    if errors:
        return False, "; ".join(errors)
    return True, f"Found new draft invoice (id={copy['id']}) copying highest-total paid invoice INV-0048"
