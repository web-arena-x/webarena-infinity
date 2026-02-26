import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    filters = state.get("filters", [])
    if not filters:
        return False, "No filters found in state."

    matching_filters = []
    for f in filters:
        criteria = f.get("criteria", {})
        subject = criteria.get("subject", "")
        if "invoice" in subject.lower():
            actions = f.get("actions", {})
            if actions.get("archive") is True:
                matching_filters.append(f)

    if matching_filters:
        return True, "Task completed successfully."

    # Provide diagnostic info
    invoice_filters = []
    for f in filters:
        criteria = f.get("criteria", {})
        subject = criteria.get("subject", "")
        if "invoice" in subject.lower():
            invoice_filters.append(f)

    if invoice_filters:
        actions_info = [f.get("actions", {}) for f in invoice_filters]
        return False, (
            f"Found filter(s) with subject containing 'invoice', but none have "
            f"archive=True. Filter actions: {actions_info}"
        )

    return False, "No filter found with criteria.subject containing 'invoice'."
