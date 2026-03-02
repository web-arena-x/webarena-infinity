import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Draft invoices in seed: INV-0058, INV-0059, INV-0060
    # All should now be awaiting_approval
    draft_numbers = ["INV-0058", "INV-0059", "INV-0060"]
    still_draft = []

    for num in draft_numbers:
        for inv in state.get("invoices", []):
            if inv.get("number") == num:
                if inv.get("status") != "awaiting_approval":
                    still_draft.append(f"{num} (status: {inv.get('status')})")
                break

    if still_draft:
        return False, (
            f"Not all draft invoices were submitted for approval. "
            f"Issues: {', '.join(still_draft)}."
        )

    return True, (
        "All 3 draft invoices (INV-0058, INV-0059, INV-0060) submitted for approval."
    )
