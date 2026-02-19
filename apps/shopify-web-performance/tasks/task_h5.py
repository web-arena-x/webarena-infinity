import requests

def verify(server_url):
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    # New optimization
    new_opt = next((o for o in state["optimizations"] if o["title"] == "Implement responsive images with srcset"), None)
    if not new_opt:
        return False, "Optimization 'Implement responsive images with srcset' not found."
    if new_opt.get("metric") != "lcp":
        return False, f"Expected metric 'lcp', got '{new_opt.get('metric')}'."
    if new_opt.get("priority") != "critical":
        return False, f"Expected priority 'critical', got '{new_opt.get('priority')}'."
    if new_opt.get("category") != "images":
        return False, f"Expected category 'images', got '{new_opt.get('category')}'."
    if new_opt.get("pageAffected") != "/products/*":
        return False, f"Expected pageAffected '/products/*', got '{new_opt.get('pageAffected')}'."
    if new_opt.get("estimatedImpact") != "400ms LCP improvement":
        return False, f"Expected estimatedImpact '400ms LCP improvement', got '{new_opt.get('estimatedImpact')}'."
    # Existing optimization completed
    existing = next((o for o in state["optimizations"] if o["title"] == "Remove unused Instafeed scripts from product pages"), None)
    if not existing:
        return False, "Optimization 'Remove unused Instafeed scripts from product pages' not found."
    if existing.get("status") != "completed":
        return False, f"Expected status 'completed', got '{existing.get('status')}'."
    return True, "New optimization created and existing optimization marked completed."
