import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    for email in state.get("emails", []):
        if email.get("subject") == "Tax Season Reminder: Documents Needed":
            labels = email.get("labels", [])
            has_finance = "label_3" in labels
            is_starred = email.get("isStarred", False)
            star_type = email.get("starType", "")
            is_important = email.get("isImportant", False)

            issues = []
            if not has_finance:
                issues.append(f"'label_3' (Finance) not in labels: {labels}")
            if not is_starred:
                issues.append(f"isStarred is {is_starred}")
            if star_type != "yellow-star":
                issues.append(f"starType is '{star_type}', expected 'yellow-star'")
            if not is_important:
                issues.append(f"isImportant is {is_important}")

            if not issues:
                return True, "Task completed successfully."
            else:
                return False, f"Email 'Tax Season Reminder: Documents Needed' found but: {'; '.join(issues)}."

    return False, "Email with subject 'Tax Season Reminder: Documents Needed' not found."
