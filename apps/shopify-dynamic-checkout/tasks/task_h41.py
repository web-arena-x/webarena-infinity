import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    themes = state.get("themes", [])

    # Find the theme that uses DM Sans as body font (Sense)
    source = next((t for t in themes if t.get("settings", {}).get("typography", {}).get("bodyFont") == "DM Sans"), None)
    if source is None:
        return False, "No theme with body font 'DM Sans' found."

    source_typo = source["settings"]["typography"]

    craft = next((t for t in themes if t.get("name") == "Craft"), None)
    if craft is None:
        return False, "Theme 'Craft' not found."

    craft_typo = craft.get("settings", {}).get("typography", {})

    checks = [
        ("headingFont", source_typo["headingFont"]),
        ("bodyFont", source_typo["bodyFont"]),
        ("buttonFont", source_typo["buttonFont"]),
        ("headingScale", source_typo["headingScale"]),
        ("bodyScale", source_typo["bodyScale"]),
    ]

    for key, expected in checks:
        actual = craft_typo.get(key)
        if actual != expected:
            return False, (
                f"Craft's {key} should be '{expected}' (from {source['name']}), "
                f"but got '{actual}'."
            )

    return True, (
        f"Craft's typography now matches {source['name']}: "
        f"heading={source_typo['headingFont']}, body={source_typo['bodyFont']}, "
        f"button={source_typo['buttonFont']}, "
        f"headingScale={source_typo['headingScale']}%, bodyScale={source_typo['bodyScale']}%."
    )
