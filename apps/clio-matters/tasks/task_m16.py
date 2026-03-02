import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    matter = next(
        (m for m in state.get("matters", [])
         if "Doyle" in m.get("description", "") and "scaffolding" in m.get("description", "").lower()),
        None
    )

    if matter is None:
        return False, "Could not find a matter with description containing 'Doyle' and 'scaffolding'."

    relationships = matter.get("relationships", [])
    match = next(
        (r for r in relationships
         if r.get("contactId") == "contact_58"
         and r.get("relationship") == "Insurance Adjuster"),
        None
    )

    if match is None:
        summary = [(r.get("contactId"), r.get("relationship")) for r in relationships]
        return False, (
            f"No relationship with contactId='contact_58' and relationship='Insurance Adjuster' "
            f"found on Doyle scaffolding case. Existing relationships: {summary}."
        )

    return True, "Doyle scaffolding case has State Farm Insurance (contact_58) as Insurance Adjuster."
