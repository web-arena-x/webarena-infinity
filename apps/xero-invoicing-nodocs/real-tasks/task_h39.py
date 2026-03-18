"""Verify: Update notes on all draft/awaiting-approval invoices with QUO reference."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    state = requests.get(f"{server_url}/api/state", timeout=5).json()
    invoices = state.get("invoices", [])

    # In seed: inv_32 (awaiting_approval, QUO-2026-018), inv_56 (awaiting_approval, QUO-2026-015),
    #          inv_82 (draft, QUO-2026-018)
    target_ids = ["inv_32", "inv_56", "inv_82"]
    expected_notes = "Quote-linked invoice - review before sending"
    errors = []

    for inv_id in target_ids:
        inv = next((i for i in invoices if i["id"] == inv_id), None)
        if not inv:
            errors.append(f"Invoice {inv_id} not found")
            continue
        notes = inv.get("notes", "")
        if notes != expected_notes:
            errors.append(f"Invoice {inv['invoiceNumber']} ({inv_id}) notes is '{notes[:50]}...', expected '{expected_notes}'")

    if errors:
        return False, "; ".join(errors)
    return True, f"Notes updated on {len(target_ids)} QUO-referenced draft/awaiting-approval invoice(s)"
