import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Find McCarthy pedestrian matter
    matters = state.get("matters", [])
    mccarthy = None
    for m in matters:
        desc = m.get("description", "").lower()
        if "mccarthy" in desc and ("pedestrian" in desc or "crosswalk" in desc):
            mccarthy = m
            break

    if mccarthy is None:
        return False, "Could not find McCarthy pedestrian matter (description containing 'McCarthy' and 'pedestrian' or 'crosswalk')."

    matter_id = mccarthy["id"]

    # Check medical providers
    medical_providers = state.get("medicalProviders", [])
    matter_providers = [mp for mp in medical_providers if mp.get("matterId") == matter_id]

    # Check for UCSF Medical Center - Billing (contact_59)
    has_ucsf = any(mp.get("contactId") == "contact_59" for mp in matter_providers)
    if not has_ucsf:
        provider_contacts = [mp.get("contactId") for mp in matter_providers]
        errors.append(
            f"UCSF Medical Center - Billing (contact_59) not found as medical provider on McCarthy matter. "
            f"Provider contactIds on this matter: {provider_contacts}."
        )

    # Check for Meridian Radiology Associates (contact_66)
    has_meridian = any(mp.get("contactId") == "contact_66" for mp in matter_providers)
    if not has_meridian:
        provider_contacts = [mp.get("contactId") for mp in matter_providers]
        errors.append(
            f"Meridian Radiology Associates (contact_66) not found as medical provider on McCarthy matter. "
            f"Provider contactIds on this matter: {provider_contacts}."
        )

    if errors:
        return False, "Medical providers not added to McCarthy matter correctly. " + " | ".join(errors)

    return True, "UCSF Medical Center and Meridian Radiology Associates added as medical providers on McCarthy matter."
