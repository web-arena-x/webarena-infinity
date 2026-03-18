import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    delegates = state.get("delegates", [])

    errors = []

    # James Wu's delegate access should be removed
    for d in delegates:
        if d.get("email") == "james.wu@techcorp.io":
            errors.append("Delegate 'james.wu@techcorp.io' (James Wu) still exists.")
            break

    # Jennifer Walsh should be added as a new delegate
    jennifer = None
    for d in delegates:
        if d.get("email") == "jennifer.walsh@techcorp.io":
            jennifer = d
            break

    if jennifer is None:
        errors.append("Delegate 'jennifer.walsh@techcorp.io' not found.")
    else:
        if jennifer.get("name") != "Jennifer Walsh":
            errors.append(
                f"Expected delegate name='Jennifer Walsh', got '{jennifer.get('name')}'."
            )
        if jennifer.get("status") != "pending":
            errors.append(
                f"Expected delegate status='pending', got '{jennifer.get('status')}'."
            )

    if errors:
        return False, " ".join(errors)

    return True, "James Wu's delegate access removed and Jennifer Walsh added as a pending delegate."
