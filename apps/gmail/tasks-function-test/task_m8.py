import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    filters = state.get("filters", [])
    if not filters:
        return False, "No filters found in state."

    for f in filters:
        criteria = f.get("criteria", {})
        from_field = criteria.get("from", "")
        if "figma" in from_field.lower():
            actions = f.get("actions", {})
            category = actions.get("category", "")
            if category.lower() == "promotions":
                return True, "Task completed successfully."
            else:
                return False, (
                    f"Found filter with from containing 'figma', but "
                    f"actions.category is '{category}', expected 'promotions'."
                )

    return False, "No filter found with criteria.from containing 'figma'."
