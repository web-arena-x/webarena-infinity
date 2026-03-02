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

    # Check featured product section
    featured_sec = next(
        (s for s in sections if s.get("type") == "featured_product" and s.get("pageId") == "page_home"),
        None
    )
    if featured_sec is None:
        return False, "Featured product section not found on home page."

    titanium = next((p for p in products if "Titanium Watch" in p.get("title", "")), None)
    if titanium is None:
        return False, "Titanium Watch product not found."

    if featured_sec.get("productId") != titanium["id"]:
        actual = next((p for p in products if p.get("id") == featured_sec.get("productId")), {})
        return False, (
            f"Expected featured product to be Titanium Watch, "
            f"but found '{actual.get('title', 'unknown')}'."
        )

    if featured_sec.get("showAcceleratedCheckout") is not False:
        return False, (
            f"Expected accelerated checkout disabled on featured section, "
            f"but got {featured_sec.get('showAcceleratedCheckout')}."
        )

    # Check default product template
    default_tmpl = next(
        (t for t in templates if t.get("themeId") == dawn["id"] and t.get("isDefault") is True),
        None
    )
    if default_tmpl is None:
        return False, "Dawn's default template not found."

    if default_tmpl.get("buyButtonText") != "Shop now":
        return False, (
            f"Expected default template buy button text 'Shop now', "
            f"but got '{default_tmpl.get('buyButtonText')}'."
        )

    if default_tmpl.get("showAcceleratedCheckout") is not False:
        return False, (
            f"Expected accelerated checkout disabled on default template, "
            f"but got {default_tmpl.get('showAcceleratedCheckout')}."
        )

    return True, (
        "Featured product set to Titanium Watch with checkout disabled. "
        "Default template buy button text set to 'Shop now' with checkout disabled."
    )
