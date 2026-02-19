import requests

def verify(server_url):
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    store = state.get("store", {})
    if store.get("name") != "Urban Threads Co.":
        return False, f"Expected store name 'Urban Threads Co.', got '{store.get('name')}'."
    if store.get("domain") != "shop.urbanthreads.com":
        return False, f"Expected domain 'shop.urbanthreads.com', got '{store.get('domain')}'."
    budgets = state.get("performanceBudgets", {})
    cls_budget = budgets.get("cls", {})
    if cls_budget.get("target") != 0.05:
        return False, f"Expected CLS target 0.05, got {cls_budget.get('target')}."
    if cls_budget.get("warning") != 0.15:
        return False, f"Expected CLS warning 0.15, got {cls_budget.get('warning')}."
    return True, "Store settings and CLS budget updated correctly."
