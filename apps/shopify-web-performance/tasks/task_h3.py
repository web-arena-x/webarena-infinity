import requests

def verify(server_url):
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    # Check new alert
    cart_alert = next((a for a in state["alertRules"] if a["name"] == "Cart INP Alert"), None)
    if not cart_alert:
        return False, "Alert rule 'Cart INP Alert' not found."
    if cart_alert.get("metric") != "inp":
        return False, f"Expected metric 'inp', got '{cart_alert.get('metric')}'."
    if cart_alert.get("threshold") != 250:
        return False, f"Expected threshold 250, got {cart_alert.get('threshold')}."
    if cart_alert.get("pageType") != "cart":
        return False, f"Expected pageType 'cart', got '{cart_alert.get('pageType')}'."
    if cart_alert.get("deviceType") != "mobile":
        return False, f"Expected deviceType 'mobile', got '{cart_alert.get('deviceType')}'."
    if not cart_alert.get("notifyEmail"):
        return False, "Email notifications should be enabled."
    # Check existing alert is now enabled
    cls_alert = next((a for a in state["alertRules"] if a["name"] == "Product Page CLS"), None)
    if not cls_alert:
        return False, "Alert 'Product Page CLS' not found."
    if not cls_alert.get("enabled"):
        return False, "Alert 'Product Page CLS' should be enabled."
    return True, "Cart INP Alert created and Product Page CLS enabled."
