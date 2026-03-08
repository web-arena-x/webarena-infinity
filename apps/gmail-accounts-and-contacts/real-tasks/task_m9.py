# Task: Update Tom Bradley's email to 'tom@newrealty.com' and job title to 'Senior Agent'.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    contacts = state.get("contacts", [])
    tom = next(
        (c for c in contacts if c.get("firstName") == "Tom" and c.get("lastName") == "Bradley"),
        None,
    )

    if tom is None:
        errors.append("Contact Tom Bradley not found")
    else:
        if tom.get("email") != "tom@newrealty.com":
            errors.append(f"Expected Tom Bradley's email to be 'tom@newrealty.com', got '{tom.get('email')}'")
        if tom.get("jobTitle") != "Senior Agent":
            errors.append(f"Expected Tom Bradley's jobTitle to be 'Senior Agent', got '{tom.get('jobTitle')}'")

    if errors:
        return False, "; ".join(errors)
    return True, "Tom Bradley's email updated to 'tom@newrealty.com' and job title to 'Senior Agent'."
