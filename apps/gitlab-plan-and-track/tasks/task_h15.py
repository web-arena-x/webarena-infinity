import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Check that no label with title starting with "component::" exists
    component_labels_remaining = []
    for lbl in state.get("labels", []):
        if lbl.get("title", "").startswith("component::"):
            component_labels_remaining.append(lbl.get("title"))

    if component_labels_remaining:
        return False, f"The following component:: labels still exist: {component_labels_remaining}"

    # Track which label IDs were component labels (they should not appear in issues)
    # We know the original component label titles from seed data
    original_component_titles = [
        "component::frontend",
        "component::backend",
        "component::api",
        "component::database",
        "component::infrastructure",
    ]

    # Also verify that no issue has any label ID that corresponds to a component label
    # Since the labels are deleted, we check that no issue references any component:: label ID
    # We build a set of all remaining label IDs
    remaining_label_ids = {lbl["id"] for lbl in state.get("labels", [])}

    # Check a few known issues that had component labels to ensure they no longer have them
    # Issues with component labels in seed data (by title):
    issues_to_check = [
        "Implement responsive sidebar navigation",    # had component::frontend
        "Optimize slow database queries in project search",  # had component::database
        "Build API rate limiting and throttling",     # had component::api
    ]

    issues_by_title = {}
    for issue in state.get("issues", []):
        if issue.get("title") in issues_to_check:
            issues_by_title[issue.get("title")] = issue

    errors = []
    for title, issue in issues_by_title.items():
        for label_id in issue.get("labels", []):
            if label_id not in remaining_label_ids:
                # This label ID was deleted (good), but it's still referenced in the issue
                # Actually this means the label was deleted but not cleaned from issues
                # Let's check if any label in remaining set is component::
                pass  # already checked above

    # The main check: no component:: labels in the labels array
    if component_labels_remaining:
        return False, f"Component labels still exist: {component_labels_remaining}"

    # Check issues don't still reference deleted component label IDs
    # We need to check if any issue references a label that no longer exists in state["labels"]
    all_label_ids = {lbl["id"] for lbl in state.get("labels", [])}
    issues_with_orphan_labels = []
    for issue in state.get("issues", []):
        for label_id in issue.get("labels", []):
            if label_id not in all_label_ids:
                # This issue has a reference to a deleted label
                issues_with_orphan_labels.append(issue.get("title", issue.get("id")))
                break

    if issues_with_orphan_labels:
        return False, f"Issues still reference deleted component:: label IDs: {issues_with_orphan_labels[:5]}"

    return True, "All 'component::' labels deleted and removed from all issues."
