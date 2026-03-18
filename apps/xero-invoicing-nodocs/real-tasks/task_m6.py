import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Change Harmony Music Academy's billing address to 100 Willis Street, Wellington, Wellington, 6011, New Zealand."""
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
        if c.get("id") == "con_13" or c.get("name", "").strip().lower() == "harmony music academy":
            target = c
            break

    if target is None:
        return False, "Contact 'Harmony Music Academy' (con_13) not found in state"

    addr = target.get("billingAddress", {})
    if not addr:
        return False, "billingAddress is missing on Harmony Music Academy"

    errors = []

    street = addr.get("street", "").strip()
    if street != "100 Willis Street":
        errors.append(f"Street is '{street}', expected '100 Willis Street'")

    city = addr.get("city", "").strip()
    if city != "Wellington":
        errors.append(f"City is '{city}', expected 'Wellington'")

    region = addr.get("region", "").strip()
    if region != "Wellington":
        errors.append(f"Region is '{region}', expected 'Wellington'")

    postal = addr.get("postalCode", "").strip()
    if postal != "6011":
        errors.append(f"PostalCode is '{postal}', expected '6011'")

    country = addr.get("country", "").strip()
    if country != "New Zealand":
        errors.append(f"Country is '{country}', expected 'New Zealand'")

    if errors:
        return False, "; ".join(errors)

    return True, "Harmony Music Academy billing address updated correctly"
