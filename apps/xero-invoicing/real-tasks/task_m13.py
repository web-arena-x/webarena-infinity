import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    repeating = state.get("repeatingInvoices", [])
    rep = None
    for r in repeating:
        if r.get("id") == "rep_001":
            rep = r
            break

    if rep is None:
        return False, "Repeating invoice rep_001 (Greenfield Organics) not found."

    end_date = rep.get("endDate", "")
    if not end_date:
        return False, "Repeating invoice rep_001 endDate is empty, expected a date in December 2026."

    if "2026-12" not in str(end_date):
        return False, f"Repeating invoice rep_001 endDate is '{end_date}', expected to contain '2026-12'."

    return True, f"Repeating invoice rep_001 end date set to '{end_date}' (December 2026)."
