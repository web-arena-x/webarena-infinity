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

    damages = rodriguez.get("damages", [])
    errors = []

    # Check no General category damages remain (except the new consolidated one)
    general_damages = [d for d in damages if d.get("category") == "General"]

    if len(general_damages) != 1:
        errors.append(
            f"Expected exactly 1 General damage (the consolidated entry), "
            f"found {len(general_damages)}"
        )
    elif general_damages:
        d = general_damages[0]
        if "consolidated" not in d.get("description", "").lower():
            errors.append(
                f"General damage description is '{d.get('description')}', "
                f"expected to contain 'consolidated'"
            )
        if d.get("type") != "Pain and Suffering":
            errors.append(
                f"Consolidated damage type is '{d.get('type')}', expected 'Pain and Suffering'"
            )
        if d.get("amount") != 250000:
            errors.append(
                f"Consolidated damage amount is {d.get('amount')}, expected 250000"
            )

    # Verify the original 3 General damages are gone
    old_descriptions = [
        "Pain and suffering from chronic back injury",
        "Emotional distress and PTSD",
        "Loss of quality of life",
    ]
    for old_desc in old_descriptions:
        if any(d.get("description") == old_desc for d in damages):
            errors.append(f"Old General damage '{old_desc}' still exists")

    if errors:
        return False, "; ".join(errors)

    return True, "All original General damages removed; consolidated $250,000 Pain and Suffering entry added."
