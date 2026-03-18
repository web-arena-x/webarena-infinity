import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    contacts = state.get("contacts", [])
    kevin = None
    for c in contacts:
        if c.get("firstName") == "Kevin" and c.get("lastName") == "Chen":
            kevin = c
            break

    if kevin is None:
        return False, "Contact Kevin Chen not found in contacts list."

    errors = []

    if kevin.get("company") != "Google":
        errors.append(
            f"Expected company='Google', got '{kevin.get('company')}'."
        )

    if kevin.get("jobTitle") != "Senior Product Manager":
        errors.append(
            f"Expected jobTitle='Senior Product Manager', got '{kevin.get('jobTitle')}'."
        )

    if errors:
        return False, " ".join(errors)

    return True, "Kevin Chen's company is Google and job title is Senior Product Manager."
