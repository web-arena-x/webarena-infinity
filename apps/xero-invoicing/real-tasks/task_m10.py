import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    quotes = state.get("quotes", [])
    qu = None
    for q in quotes:
        if q.get("number") == "QU-0025":
            qu = q
            break

    if qu is None:
        return False, "Quote QU-0025 not found."

    status = qu.get("status", "")
    if status != "sent":
        return False, f"Quote QU-0025 status is '{status}', expected 'sent'."

    sent_at = qu.get("sentAt")
    if sent_at is None:
        return False, "Quote QU-0025 sentAt is None, expected a timestamp."

    return True, "Quote QU-0025 (Fresh Start Catering) has been sent."
