"""
Task H4: Set up a filter for emails with 'invoice' or 'payment' in the subject
that applies the Invoices label and marks them as read.
Verify: A filter exists where criteria references 'invoice' or 'payment'
(in subject or hasWords) AND actions.label='label_15' AND actions.markRead=True.
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    filters = state.get("filters", [])

    for f in filters:
        criteria = f.get("criteria", {})
        actions = f.get("actions", {})
        subject = (criteria.get("subject") or "").lower()
        has_words = (criteria.get("hasWords") or "").lower()
        combined = subject + " " + has_words

        # Check all conditions together: criteria + actions
        has_keyword = "invoice" in combined or "payment" in combined
        has_label = actions.get("label") == "label_15"
        has_mark_read = actions.get("markRead") is True

        if has_keyword and has_label and has_mark_read:
            return True, (
                "Filter for invoice/payment emails correctly applies Invoices label "
                "and marks as read."
            )

    return False, (
        "No filter found matching all conditions: "
        "criteria with 'invoice'/'payment', actions.label='label_15', "
        "and actions.markRead=True."
    )
