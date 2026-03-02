import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state.get("invoiceSettings", {})

    # Check default payment terms changed to end of following month
    due_date = settings.get("defaultDueDate", {})
    due_type = due_date.get("type", "")
    if due_type != "endOfFollowingMonth":
        return False, (
            f"Default due date type is '{due_type}', expected 'endOfFollowingMonth'."
        )

    # Check quote numbering starts from 50
    quote_next = settings.get("quoteNextNumber")
    if quote_next != 50:
        return False, (
            f"Quote next number is {quote_next}, expected 50."
        )

    # Prefix should still be QU-
    quote_prefix = settings.get("quotePrefix", "")
    if quote_prefix != "QU-":
        return False, (
            f"Quote prefix is '{quote_prefix}', expected 'QU-'."
        )

    return True, (
        "Invoice settings updated: default payment terms set to 'end of following month', "
        "quote numbering set to start from QU-0050."
    )
