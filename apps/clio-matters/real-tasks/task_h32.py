import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Check practice area exists
    cl_pa = None
    for pa in state.get("practiceAreas", []):
        if pa.get("name") == "Civil Litigation":
            cl_pa = pa
            break

    if not cl_pa:
        return False, "Practice area 'Civil Litigation' not found."

    # Check stages
    stages = state.get("matterStages", {}).get(cl_pa["id"], [])
    stage_names = [s.get("name") for s in stages]

    if "Pre-Trial" not in stage_names:
        errors.append("Stage 'Pre-Trial' not found under Civil Litigation")
    if "Trial" not in stage_names:
        errors.append("Stage 'Trial' not found under Civil Litigation")

    # Check template
    cl_tmpl = None
    for t in state.get("matterTemplates", []):
        if t.get("name") == "Civil Litigation - Standard":
            cl_tmpl = t
            break

    if not cl_tmpl:
        errors.append("Template 'Civil Litigation - Standard' not found")
    else:
        if cl_tmpl.get("practiceAreaId") != cl_pa["id"]:
            errors.append(
                f"Template practiceAreaId is '{cl_tmpl.get('practiceAreaId')}', "
                f"expected '{cl_pa['id']}'"
            )
        if cl_tmpl.get("billingMethod") != "hourly":
            errors.append(
                f"Template billing method is '{cl_tmpl.get('billingMethod')}', expected 'hourly'"
            )

    if errors:
        return False, "; ".join(errors)

    return True, "Civil Litigation PA with Pre-Trial/Trial stages and Standard template created."
