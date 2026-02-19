import requests

def verify(server_url):
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    report = next((r for r in state["savedReports"] if r["name"] == "Cart Performance Analysis"), None)
    if not report:
        return False, "Saved report 'Cart Performance Analysis' not found."
    if report.get("metric") != "inp":
        return False, f"Expected metric 'inp', got '{report.get('metric')}'."
    if report.get("reportType") != "by_page_url":
        return False, f"Expected reportType 'by_page_url', got '{report.get('reportType')}'."
    filters = report.get("filters", {})
    if filters.get("deviceType") != "mobile":
        return False, f"Expected device type 'mobile', got '{filters.get('deviceType')}'."
    if filters.get("dateRange") != "last_7_days":
        return False, f"Expected date range 'last_7_days', got '{filters.get('dateRange')}'."
    if filters.get("pageType") != "cart":
        return False, f"Expected page type 'cart', got '{filters.get('pageType')}'."
    return True, "Saved report 'Cart Performance Analysis' created with correct settings."
