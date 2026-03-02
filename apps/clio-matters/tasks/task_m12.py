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

    custom_fields = matter.get("customFields", {})

    cf_1 = custom_fields.get("cf_1", "")
    if cf_1 != "SM-2025-PI-4421":
        return False, f"Custom field cf_1 (Court Case Number) is '{cf_1}', expected 'SM-2025-PI-4421'."

    cf_7 = custom_fields.get("cf_7", "")
    if cf_7 != "Hon. Patricia Chen":
        return False, f"Custom field cf_7 (Judge Assigned) is '{cf_7}', expected 'Hon. Patricia Chen'."

    return True, "Doyle scaffolding case has cf_1='SM-2025-PI-4421' and cf_7='Hon. Patricia Chen'."
