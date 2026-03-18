import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Create a new contact called Southern Cross Logistics with specified details."""
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
        if c.get("name", "").strip().lower() == "southern cross logistics":
            target = c
            break

    if target is None:
        return False, "Contact 'Southern Cross Logistics' not found in state"

    errors = []

    email = target.get("email", "")
    if email.strip().lower() != "logistics@southerncross.co.nz":
        errors.append(f"Email is '{email}', expected 'logistics@southerncross.co.nz'")

    phone = target.get("phone", "")
    # Normalize phone for comparison: strip spaces and dashes
    phone_normalized = phone.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
    expected_phone_normalized = "+6493001234"
    if phone_normalized != expected_phone_normalized:
        errors.append(f"Phone is '{phone}', expected '+64 9 300 1234'")

    addr = target.get("billingAddress", {})
    if not addr:
        errors.append("billingAddress is missing")
    else:
        street = addr.get("street", "").strip()
        if street != "10 Customs Street":
            errors.append(f"Street is '{street}', expected '10 Customs Street'")

        city = addr.get("city", "").strip()
        if city != "Auckland":
            errors.append(f"City is '{city}', expected 'Auckland'")

        region = addr.get("region", "").strip()
        if region != "Auckland":
            errors.append(f"Region is '{region}', expected 'Auckland'")

        postal = addr.get("postalCode", "").strip()
        if postal != "1010":
            errors.append(f"PostalCode is '{postal}', expected '1010'")

        country = addr.get("country", "").strip()
        if country != "New Zealand":
            errors.append(f"Country is '{country}', expected 'New Zealand'")

    if errors:
        return False, "; ".join(errors)

    return True, "Contact 'Southern Cross Logistics' created with correct details"
