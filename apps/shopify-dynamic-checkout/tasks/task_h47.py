import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    products = state.get("products", [])

    # Check Heavyweight Hoodie is active
    hoodie = next((p for p in products if "Heavyweight Hoodie" in p.get("title", "")), None)
    if hoodie is None:
        return False, "Heavyweight Hoodie not found."

    if hoodie.get("status") != "active":
        return False, (
            f"Expected Heavyweight Hoodie to be active, "
            f"but got status='{hoodie.get('status')}'."
        )

    hoodie_vendor = hoodie.get("vendor")

    # Check other Outerwear products from same vendor are archived
    other_outerwear = [
        p for p in products
        if p.get("vendor") == hoodie_vendor
        and p.get("productType") == "Outerwear"
        and p["id"] != hoodie["id"]
    ]

    if not other_outerwear:
        return False, f"No other Outerwear products found from vendor '{hoodie_vendor}'."

    for p in other_outerwear:
        if p.get("status") != "archived":
            return False, (
                f"Expected '{p['title']}' ({hoodie_vendor}, Outerwear) to be archived, "
                f"but got status='{p.get('status')}'."
            )

    return True, (
        f"Heavyweight Hoodie restored to active. "
        f"{len(other_outerwear)} other {hoodie_vendor} Outerwear product(s) archived."
    )
