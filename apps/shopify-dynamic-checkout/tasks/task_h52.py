import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    themes = state.get("themes", [])

    # Find unpublished theme with heading scale 110% (Craft in seed data)
    # After publishing, it becomes main, so we look for the theme with headingScale 110
    target = next(
        (t for t in themes if t.get("settings", {}).get("typography", {}).get("headingScale") == 110),
        None
    )
    if target is None:
        return False, "No theme with heading scale 110% found."

    # Check it's published
    if target.get("role") != "main":
        return False, (
            f"Expected '{target['name']}' (heading scale 110%) to be published, "
            f"but got role='{target.get('role')}'."
        )

    # Check heading font matches body font
    typo = target.get("settings", {}).get("typography", {})
    if typo.get("headingFont") != typo.get("bodyFont"):
        return False, (
            f"Expected '{target['name']}' heading font to match body font '{typo.get('bodyFont')}', "
            f"but heading font is '{typo.get('headingFont')}'."
        )

    # Check Dawn is no longer main
    dawn = next((t for t in themes if t.get("name") == "Dawn"), None)
    if dawn and dawn.get("role") == "main":
        return False, "Dawn should no longer be the published theme."

    return True, (
        f"'{target['name']}' published with heading font changed to '{typo.get('bodyFont')}' "
        f"(matching its body font)."
    )
