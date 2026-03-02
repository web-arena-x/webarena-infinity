import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # TechVault Solutions (con_002) has two invoices:
    #   INV-0043 ($8,756) and INV-0055 ($41,800)
    # The highest total is INV-0055
    inv = None
    for i in state.get("invoices", []):
        if i.get("number") == "INV-0055":
            inv = i
            break

    if inv is None:
        return False, "Invoice INV-0055 not found."

    theme_id = inv.get("brandingThemeId", "")
    if theme_id != "theme_retail":
        return False, (
            f"INV-0055 brandingThemeId is '{theme_id}', expected 'theme_retail' (Retail)."
        )

    title = inv.get("title", "")
    if title != "Q1 2026 Major Project":
        return False, (
            f"INV-0055 title is '{title}', expected 'Q1 2026 Major Project'."
        )

    return True, (
        "INV-0055 (TechVault Solutions, $41,800 — highest total) updated: "
        "branding theme set to Retail, title set to 'Q1 2026 Major Project'."
    )
