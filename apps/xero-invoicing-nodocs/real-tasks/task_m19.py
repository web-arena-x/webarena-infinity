import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Create a new contact called Horizon Architecture Studio with specific email and billing address."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    contacts = state.get("contacts", [])
    target = None
    for c in contacts:
        if c.get("name") == "Horizon Architecture Studio":
            target = c
            break

    if target is None:
        return False, "Contact 'Horizon Architecture Studio' not found in state"

    errors = []

    # Check email
    email = target.get("email")
    if email != "hello@horizonarch.co.nz":
        errors.append(f"email is '{email}', expected 'hello@horizonarch.co.nz'")

    # Check billing address
    billing = target.get("billingAddress", {})
    if not billing:
        errors.append("billingAddress is missing or empty")
    else:
        expected = {
            "street": "200 Parnell Road",
            "city": "Auckland",
            "region": "Auckland",
            "postalCode": "1052",
            "country": "New Zealand",
        }
        for field, expected_value in expected.items():
            actual = str(billing.get(field, ""))
            if actual != expected_value:
                errors.append(f"billingAddress.{field} is '{actual}', expected '{expected_value}'")

    if errors:
        return False, "; ".join(errors)

    return True, "Contact 'Horizon Architecture Studio' created with correct email and billing address"
