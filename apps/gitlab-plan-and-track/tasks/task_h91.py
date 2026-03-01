import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # Find epics
    caching_epic = platform_epic = None
    for e in state.get("epics", []):
        if e.get("title") == "Caching Layer Implementation":
            caching_epic = e
        elif e.get("title") == "Platform Redesign":
            platform_epic = e
    if caching_epic is None:
        return False, "Could not find epic 'Caching Layer Implementation'."
    if platform_epic is None:
        return False, "Could not find epic 'Platform Redesign'."

    # Check parent epic changed
    if caching_epic.get("parentEpicId") != platform_epic["id"]:
        errors.append(
            f"Caching Layer parentEpicId is '{caching_epic.get('parentEpicId')}', "
            f"expected '{platform_epic['id']}'."
        )

    # Check open issues in Caching Layer have health needs_attention
    for i in state.get("issues", []):
        if i.get("epicId") == caching_epic["id"] and i.get("status") == "open":
            if i.get("healthStatus") != "needs_attention":
                errors.append(
                    f"Issue '{i.get('title')}' health is '{i.get('healthStatus')}', "
                    f"expected 'needs_attention'."
                )

    if errors:
        return False, " ".join(errors)

    return True, (
        "Caching Layer epic moved under Platform Redesign; "
        "open issues set to needs_attention."
    )
