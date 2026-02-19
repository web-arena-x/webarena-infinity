import requests

def verify(server_url):
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    page = next((p for p in state["pages"] if p["name"] == "FAQ Page"), None)
    if not page:
        return False, "Page 'FAQ Page' not found."
    if page.get("path") != "/pages/faq":
        return False, f"Expected path '/pages/faq', got '{page.get('path')}'."
    if page.get("type") != "page":
        return False, f"Expected type 'page', got '{page.get('type')}'."
    if not page.get("monitored"):
        return False, "Page is not being monitored."
    return True, "Page 'FAQ Page' added with correct settings."
