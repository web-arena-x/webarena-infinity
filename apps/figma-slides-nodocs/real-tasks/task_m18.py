import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    pres_003 = next(
        (p for p in presentations if p.get("id") == "pres_003"),
        None,
    )
    if pres_003 is None:
        pres_003 = next(
            (p for p in presentations if "Series B" in p.get("title", "")),
            None,
        )
    if pres_003 is None:
        return False, "Series B Fundraising Pitch (pres_003) not found"

    pres_015 = next(
        (p for p in presentations if p.get("id") == "pres_015"),
        None,
    )
    if pres_015 is None:
        pres_015 = next(
            (p for p in presentations if "Product Demo" in p.get("title", "") and "Enterprise" in p.get("title", "")),
            None,
        )
    if pres_015 is None:
        return False, "Product Demo — Enterprise Features (pres_015) not found"

    errors = []
    if not pres_003.get("shareSettings", {}).get("allowComments", False):
        errors.append(
            f"Series B Fundraising Pitch: expected allowComments==true, got {pres_003.get('shareSettings', {}).get('allowComments')}"
        )
    if not pres_015.get("shareSettings", {}).get("allowComments", False):
        errors.append(
            f"Product Demo — Enterprise Features: expected allowComments==true, got {pres_015.get('shareSettings', {}).get('allowComments')}"
        )

    if errors:
        return False, "; ".join(errors)

    return True, "Comments enabled on both Series B Fundraising Pitch and Product Demo — Enterprise Features"
