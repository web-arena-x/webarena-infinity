import requests

def verify(server_url):
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    report = next((r for r in state["savedReports"] if r["name"] == "Mobile CLS Trends"), None)
    if not report:
        return False, "Saved report 'Mobile CLS Trends' not found."
    if report.get("metric") != "cls":
        return False, f"Expected metric 'cls', got '{report.get('metric')}'."
    if report.get("reportType") != "over_time":
        return False, f"Expected reportType 'over_time', got '{report.get('reportType')}'."
    filters = report.get("filters", {})
    if filters.get("deviceType") != "mobile":
        return False, f"Expected device type 'mobile', got '{filters.get('deviceType')}'."
    if filters.get("dateRange") != "last_30_days":
        return False, f"Expected date range 'last_30_days', got '{filters.get('dateRange')}'."
    return True, "Saved report 'Mobile CLS Trends' created correctly."
