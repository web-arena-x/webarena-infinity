import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    for contact in contacts:
        if contact.get("firstName") == "Alex" and contact.get("lastName") == "Martinez":
            errors = []
            actual_company = contact.get("company")
            actual_job_title = contact.get("jobTitle")
            if actual_company != "TechCorp Inc":
                errors.append(f"company: expected 'TechCorp Inc', got '{actual_company}'")
            if actual_job_title != "Senior Frontend Engineer":
                errors.append(f"jobTitle: expected 'Senior Frontend Engineer', got '{actual_job_title}'")
            if errors:
                return False, "Alex Martinez found but: " + "; ".join(errors)
            return True, "Alex Martinez's company and jobTitle successfully updated."

    return False, "No contact found with firstName 'Alex' and lastName 'Martinez'."
