import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    matter = next(
        (m for m in state.get("matters", [])
         if "Johnson" in m.get("description", "") and "Whole Foods" in m.get("description", "")),
        None
    )

    if matter is None:
        return False, "Could not find a matter with description containing 'Johnson' and 'Whole Foods'."

    matter_id = matter.get("id")
    providers = state.get("medicalProviders", [])
    matching = [
        p for p in providers
        if p.get("matterId") == matter_id and p.get("contactId") == "contact_60"
    ]

    if not matching:
        matter_providers = [
            (p.get("contactId"), p.get("description", ""))
            for p in providers if p.get("matterId") == matter_id
        ]
        return False, (
            f"No medical provider with contactId 'contact_60' (Dr. Michael Reeves Chiropractic) "
            f"found for Johnson v. Whole Foods. Existing providers for this matter: {matter_providers}."
        )

    return True, "Dr. Michael Reeves Chiropractic added as medical provider on Johnson v. Whole Foods."
