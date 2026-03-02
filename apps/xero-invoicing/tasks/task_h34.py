import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # rep_003 = Cascade Software Solutions repeating invoice
    ri = None
    for r in state.get("repeatingInvoices", []):
        if r.get("id") == "rep_003":
            ri = r
            break

    if ri is None:
        return False, "Repeating invoice rep_003 (Cascade Software Solutions) not found."

    freq = ri.get("frequency", "")
    if freq != "fortnightly":
        return False, f"rep_003 frequency is '{freq}', expected 'fortnightly'."

    theme_id = ri.get("brandingThemeId", "")
    if theme_id != "theme_professional":
        return False, (
            f"rep_003 brandingThemeId is '{theme_id}', "
            f"expected 'theme_professional' (Professional Services)."
        )

    return True, (
        "Cascade Software Solutions repeating invoice updated: "
        "frequency changed to fortnightly, branding theme set to Professional Services."
    )
