import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Check numbering scheme
    numbering = state.get("numberingScheme", {})

    prefix = numbering.get("prefix", "")
    if "MLG" not in str(prefix).upper():
        errors.append(
            f"numberingScheme.prefix is '{prefix}', expected to contain 'MLG'."
        )

    separator = numbering.get("separator", "")
    if separator != "/":
        errors.append(
            f"numberingScheme.separator is '{separator}', expected '/'."
        )

    padding = numbering.get("numberPadding")
    if padding is None:
        errors.append("numberingScheme.numberPadding is not set.")
    elif int(padding) != 6:
        errors.append(
            f"numberingScheme.numberPadding is {padding}, expected 6."
        )

    # Check for a matter with clientId matching Andrew Kim (contact_43)
    contacts = state.get("contacts", [])
    andrew_kim = next(
        (c for c in contacts
         if "andrew" in c.get("displayName", "").lower()
         and "kim" in c.get("displayName", "").lower()),
        None
    )

    andrew_id = "contact_43"
    if andrew_kim is not None:
        andrew_id = andrew_kim.get("id", "contact_43")

    andrew_matters = [
        m for m in state.get("matters", [])
        if m.get("clientId") == andrew_id
    ]

    if not andrew_matters:
        errors.append(
            f"No matter found with clientId matching Andrew Kim ({andrew_id})."
        )

    if errors:
        return False, "Numbering scheme and Andrew Kim matter not set up correctly. " + " | ".join(errors)

    return True, (
        f"Numbering scheme updated (prefix='MLG', separator='/', padding=6) "
        f"and matter created for Andrew Kim ({andrew_id})."
    )
