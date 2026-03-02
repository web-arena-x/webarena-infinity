import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    sections = state.get("themeSections", [])
    templates = state.get("templates", [])
    products = state.get("products", [])
    themes = state.get("themes", [])

    dawn = next((t for t in themes if t.get("name") == "Dawn"), None)
    if dawn is None:
        return False, "Theme 'Dawn' not found."

    no_checkout = next(
        (t for t in templates if t.get("name") == "Product - No checkout buttons" and t.get("themeId") == dawn["id"]),
        None
    )
    if no_checkout is None:
        return False, "Dawn's 'No checkout buttons' template not found."

    # In seed data, featured product is prod_1 (Classic Cotton T-Shirt)
    # Check it's now on No checkout buttons and in draft
    cotton_tshirt = next((p for p in products if p.get("title") == "Classic Cotton T-Shirt"), None)
    if cotton_tshirt is None:
        return False, "Classic Cotton T-Shirt not found."

    if cotton_tshirt.get("templateId") != no_checkout["id"]:
        return False, (
            f"Expected Classic Cotton T-Shirt on 'No checkout buttons' template, "
            f"but it's on template '{cotton_tshirt.get('templateId')}'."
        )
    if cotton_tshirt.get("status") != "draft":
        return False, (
            f"Expected Classic Cotton T-Shirt status 'draft', "
            f"got '{cotton_tshirt.get('status')}'."
        )

    # Check new featured product is Waxed Canvas Backpack
    backpack = next((p for p in products if p.get("title") == "Waxed Canvas Backpack"), None)
    if backpack is None:
        return False, "Waxed Canvas Backpack not found."

    featured_sec = next(
        (s for s in sections if s.get("type") == "featured_product" and s.get("pageId") == "page_home"),
        None
    )
    if featured_sec is None:
        return False, "Featured product section not found."

    if featured_sec.get("productId") != backpack["id"]:
        return False, (
            f"Expected featured product to be Waxed Canvas Backpack, "
            f"but found productId='{featured_sec.get('productId')}'."
        )

    if featured_sec.get("showAcceleratedCheckout") is not False:
        return False, (
            f"Expected checkout disabled on featured section, "
            f"got {featured_sec.get('showAcceleratedCheckout')}."
        )

    return True, (
        "Classic Cotton T-Shirt moved to 'No checkout buttons' and set to draft. "
        "Waxed Canvas Backpack set as featured product with checkout disabled."
    )
