# Task: Update Sarah Chen company to 'TechCorp Global' and title to 'SVP of Product'.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    contacts = state.get("contacts", [])
    sarah = next(
        (c for c in contacts if c.get("firstName") == "Sarah" and c.get("lastName") == "Chen"),
        None,
    )

    if sarah is None:
        errors.append("Contact Sarah Chen not found")
    else:
        if sarah.get("company") != "TechCorp Global":
            errors.append(f"Expected Sarah Chen's company to be 'TechCorp Global', got '{sarah.get('company')}'")
        if sarah.get("jobTitle") != "SVP of Product":
            errors.append(f"Expected Sarah Chen's jobTitle to be 'SVP of Product', got '{sarah.get('jobTitle')}'")

    if errors:
        return False, "; ".join(errors)
    return True, "Sarah Chen's company updated to 'TechCorp Global' and job title to 'SVP of Product'."
