import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Only templates created by the current provider remain. All others deleted."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    current_provider_id = state["currentProvider"]["id"]
    templates = state.get("visitNoteTemplates", [])

    errors = []
    for t in templates:
        if t.get("createdBy") != current_provider_id:
            errors.append(
                f"Template '{t['name']}' (created by {t.get('createdBy')}) "
                f"should have been deleted."
            )

    # Verify the current provider's templates are still there
    # prov_001 templates: E* Annual Wellness Visit, E* Problem-Focused Visit,
    # Telehealth Follow-Up, COVID-19 Vaccine Visit, Pre-Operative Evaluation
    expected_names = {
        "E* Annual Wellness Visit",
        "E* Problem-Focused Visit",
        "Telehealth Follow-Up",
        "COVID-19 Vaccine Visit",
        "Pre-Operative Evaluation",
    }
    remaining_names = {t["name"] for t in templates}
    missing = expected_names - remaining_names
    if missing:
        errors.append(f"Current provider's templates missing: {missing}")

    if errors:
        return False, " ".join(errors)
    return True, (
        f"{len(templates)} templates remain (all by current provider). "
        f"Non-current-provider templates deleted."
    )
