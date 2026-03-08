import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find Rodriguez matter
    rodriguez = None
    for m in state.get("matters", []):
        desc = m.get("description") or ""
        if "Rodriguez" in desc and "Premier Auto" in desc:
            rodriguez = m
            break

    if not rodriguez:
        return False, "Rodriguez matter not found."

    # Find Advanced Imaging provider (con_020) - the diagnostic imaging provider
    target = None
    for p in rodriguez.get("medicalProviders", []):
        if p.get("contactId") == "con_020":
            target = p
            break

    if not target:
        return False, "Advanced Imaging Associates provider (con_020) not found on Rodriguez case."

    actual = target.get("recordStatus")
    if actual != "Complete":
        return False, f"Record status for diagnostic imaging provider is '{actual}', expected 'Complete'."

    # Ensure the other providers were NOT changed to Complete
    errors = []
    for p in rodriguez.get("medicalProviders", []):
        if p.get("contactId") in ("con_019", "con_021"):
            if p.get("recordStatus") == "Complete" and p.get("contactId") == "con_019":
                # Chicago PT was already 'Received' in seed data; if it's now 'Complete' that's wrong
                errors.append(
                    f"Rehabilitation provider (con_019) record status was changed to 'Complete' — "
                    f"only the diagnostic imaging provider should have been updated"
                )

    if errors:
        return False, "; ".join(errors)

    return True, "Record status set to 'Complete' for diagnostic imaging provider (Advanced Imaging)."
