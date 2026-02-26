import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    # Find the original "API Integration Issue" email (the first one in the thread, which is starred)
    email = next(
        (e for e in state["emails"]
         if e["subject"] == "API Integration Issue"
         and e["from"]["email"] == "priya.sharma@cloudnine.dev"),
        None,
    )
    if not email:
        return False, "Email 'API Integration Issue' from Priya Sharma not found."

    if email["isStarred"]:
        return False, "Email 'API Integration Issue' is still starred."

    return True, "Star removed from email 'API Integration Issue'."
