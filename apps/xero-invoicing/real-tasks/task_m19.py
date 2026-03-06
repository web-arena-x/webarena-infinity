import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    repeating = state.get("repeatingInvoices", [])
    rep = None
    for r in repeating:
        if r.get("id") == "rep_003":
            rep = r
            break

    if rep is None:
        return False, "Repeating invoice rep_003 (Cascade Software) not found."

    reference = rep.get("reference", "")
    if reference != "CSS-LIC-MONTHLY":
        return False, f"Repeating invoice rep_003 reference is '{reference}', expected 'CSS-LIC-MONTHLY'."

    return True, "Cascade Software repeating invoice reference updated to 'CSS-LIC-MONTHLY'."
