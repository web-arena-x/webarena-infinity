import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    email = next(
        (e for e in state["emails"]
         if e["subject"] == "Q1 Product Roadmap Review"
         and e["from"]["email"] == "sarah.chen@techcorp.io"),
        None,
    )
    if not email:
        return False, "Email 'Q1 Product Roadmap Review' not found."

    if email["isImportant"]:
        return False, "Email 'Q1 Product Roadmap Review' is still marked as important."

    if "IMPORTANT" in email["labels"]:
        return False, "Email 'Q1 Product Roadmap Review' still has the IMPORTANT label."

    return True, "Important marker removed from email 'Q1 Product Roadmap Review'."
