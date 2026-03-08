import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Add 'Provider-Reviewed' tag to all templates created by the current provider (prov_001)."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    current_provider_id = state.get("currentProvider", {}).get("id", "prov_001")

    errors = []
    modified_count = 0
    unmodified_count = 0

    for tmpl in state.get("visitNoteTemplates", []):
        name = tmpl.get("name", "?")
        creator = tmpl.get("createdBy", "")
        tags = tmpl.get("documentTags", [])

        if creator == current_provider_id:
            if "Provider-Reviewed" not in tags:
                errors.append(f"Template '{name}' by current provider missing 'Provider-Reviewed' tag.")
            else:
                modified_count += 1
        else:
            if "Provider-Reviewed" in tags:
                errors.append(f"Template '{name}' by another provider should NOT have 'Provider-Reviewed' tag.")
            else:
                unmodified_count += 1

    if errors:
        return False, " ".join(errors)
    return True, (
        f"{modified_count} templates by current provider have 'Provider-Reviewed' tag; "
        f"{unmodified_count} templates by other providers left unchanged."
    )
