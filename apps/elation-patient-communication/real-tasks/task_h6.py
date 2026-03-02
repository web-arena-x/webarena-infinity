import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    message_routing = state.get("messageRouting", {})
    prov_1_routing = message_routing.get("prov_1", {})

    categories = [
        "General Question",
        "Prescription Refill",
        "Appointment Request",
        "Test Results",
        "Billing Question",
        "Referral Request",
        "Medical Records Request",
        "Other",
    ]

    clinical_team_id = "ug_2"

    for category in categories:
        category_data = prov_1_routing.get(category)
        if category_data is None:
            return False, (
                f"Category '{category}' not found in Dr. Chen's message routing."
            )

        recipients = category_data if isinstance(category_data, list) else category_data.get("recipients", [])

        if clinical_team_id not in recipients:
            return False, (
                f"Clinical Team ({clinical_team_id}) not found in recipients "
                f"for category '{category}' in Dr. Chen's routing."
            )

    return True, "Clinical Team added to all message routing categories for Dr. Chen."
