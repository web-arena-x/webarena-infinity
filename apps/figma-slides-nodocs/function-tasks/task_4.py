import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    presentations = state.get("presentations", [])
    original_found = False
    copy_found = False

    for pres in presentations:
        title = pres.get("title", "")
        if title == "Design Sprint Week 12 Recap":
            original_found = True
        if "Design Sprint Week 12 Recap" in title and "(Copy)" in title:
            copy_found = True

    if not original_found:
        return False, "Original presentation 'Design Sprint Week 12 Recap' no longer exists."
    if not copy_found:
        return False, "No duplicate presentation containing 'Design Sprint Week 12 Recap' and '(Copy)' in title found."

    return True, "Original 'Design Sprint Week 12 Recap' exists and a copy with '(Copy)' in the title was found."
