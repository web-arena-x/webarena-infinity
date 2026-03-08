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

    # Find the provider where treatment was previously ongoing (Dr. Reeves, con_021)
    target = None
    for p in rodriguez.get("medicalProviders", []):
        if p.get("contactId") == "con_021":
            target = p
            break

    if not target:
        return False, "Dr. Amanda Reeves provider (con_021) not found on Rodriguez case."

    errors = []

    if target.get("treatmentLastDate") != "2026-02-28":
        errors.append(
            f"Treatment last date is '{target.get('treatmentLastDate')}', "
            f"expected '2026-02-28'"
        )

    if target.get("treatmentComplete") is not True:
        errors.append(
            f"Treatment complete is {target.get('treatmentComplete')}, expected True"
        )

    if errors:
        return False, "; ".join(errors)

    return True, "Dr. Reeves treatment marked complete with last date February 28, 2026."
