import requests

def verify(server_url):
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    opt = next((o for o in state["optimizations"] if o["title"] == "Minify custom JavaScript files"), None)
    if not opt:
        return False, "Optimization 'Minify custom JavaScript files' not found."
    if opt.get("metric") != "inp":
        return False, f"Expected metric 'inp', got '{opt.get('metric')}'."
    if opt.get("priority") != "high":
        return False, f"Expected priority 'high', got '{opt.get('priority')}'."
    if opt.get("category") != "scripts":
        return False, f"Expected category 'scripts', got '{opt.get('category')}'."
    return True, "Optimization 'Minify custom JavaScript files' created correctly."
