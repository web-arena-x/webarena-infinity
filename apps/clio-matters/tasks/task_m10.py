import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    matter = next(
        (m for m in state.get("matters", [])
         if "Baptiste" in m.get("description", "")
         and ("contested divorce" in m.get("description", "").lower()
              or "business valuation" in m.get("description", "").lower())),
        None
    )

    if matter is None:
        return False, (
            "Could not find a matter with description containing 'Baptiste' "
            "and 'Contested divorce' or 'business valuation'."
        )

    errors = []

    if matter.get("status") != "closed":
        errors.append(f"Matter status is '{matter.get('status')}', expected 'closed'.")

    if matter.get("stageId") != "stage_2_5":
        errors.append(
            f"Matter stageId is '{matter.get('stageId')}', expected 'stage_2_5' (Trial/Resolution)."
        )

    if errors:
        return False, " ".join(errors)

    return True, "Baptiste contested divorce matter is closed and set to Trial/Resolution stage."
