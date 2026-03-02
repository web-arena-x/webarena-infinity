import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    matters = state.get("matters", [])
    patterson = next(
        (m for m in matters
         if "Patterson" in m.get("description", "") and
         "Metro Transit" in m.get("description", "")),
        None
    )

    if patterson is None:
        return False, "Could not find a matter with description containing 'Patterson' and 'Metro Transit'."

    billing = patterson.get("billing", {})
    currency = billing.get("currency")

    if currency is None:
        return False, "Patterson v. Metro Transit matter has no billing.currency set."

    if currency != "GBP":
        return False, (
            f"Patterson v. Metro Transit billing.currency is "
            f"'{currency}', expected 'GBP'."
        )

    return True, "Patterson v. Metro Transit billing currency has been changed to GBP (British Pounds)."
