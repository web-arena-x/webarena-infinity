import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])

    fwd_email = next(
        (e for e in emails
         if e.get("from", {}).get("email") == "alex.morgan@acmecorp.com"
         and "Fwd:" in e.get("subject", "")
         and "Quantum Computing" in e.get("subject", "")
         and any(r.get("email") == "nate.patel@acmecorp.com" for r in e.get("to", []))),
        None,
    )
    if fwd_email is None:
        return False, (
            "Could not find a forwarded email from alex.morgan@acmecorp.com with subject "
            "containing 'Fwd:' and 'Quantum Computing' sent to nate.patel@acmecorp.com."
        )

    return True, "Email 'Quantum Computing Integration Prototype' forwarded to nate.patel@acmecorp.com."
