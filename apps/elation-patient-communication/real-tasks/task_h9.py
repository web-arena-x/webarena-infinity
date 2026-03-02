import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    message_routing = state.get("messageRouting", {})
    clinical_team_id = "ug_2"
    category = "Medical Records Request"
    provider_ids = ["prov_1", "prov_2", "prov_3", "prov_4", "prov_5"]

    for prov_id in provider_ids:
        prov_routing = message_routing.get(prov_id, {})
        category_data = prov_routing.get(category)

        if category_data is None:
            return False, (
                f"Category '{category}' not found in routing for {prov_id}."
            )

        recipients = (
            category_data
            if isinstance(category_data, list)
            else category_data.get("recipients", [])
        )

        if clinical_team_id not in recipients:
            return False, (
                f"Clinical Team ({clinical_team_id}) not found in "
                f"'{category}' recipients for {prov_id}."
            )

    return True, "Clinical Team added to Medical Records Request routing for all providers."
