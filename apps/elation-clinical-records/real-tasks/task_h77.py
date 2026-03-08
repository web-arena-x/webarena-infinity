import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Patients with signed notes billing 99215 get 'High-Complexity-Visit'.
    Template with billing 99215 gets doc tag 'High-Complexity'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Find patients with signed notes containing billing 99215
    pids_with_99215 = set()
    for note in state.get("visitNotes", []):
        if note.get("status") != "signed":
            continue
        for billing in note.get("billingItems", []):
            if billing.get("cptCode") == "99215":
                pids_with_99215.add(note["patientId"])
                break

    for patient in state.get("patients", []):
        pid = patient["id"]
        name = patient.get("lastName", pid)
        tags = patient.get("tags", [])
        should_tag = pid in pids_with_99215

        if should_tag and "High-Complexity-Visit" not in tags:
            errors.append(f"{name} missing 'High-Complexity-Visit' tag.")
        if not should_tag and "High-Complexity-Visit" in tags:
            errors.append(f"{name} should NOT have 'High-Complexity-Visit' tag.")

    # Find template with billing 99215
    for tmpl in state.get("visitNoteTemplates", []):
        has_99215 = any(
            b.get("cptCode") == "99215" for b in tmpl.get("billingItems", [])
        )
        if has_99215:
            doc_tags = tmpl.get("documentTags", [])
            if "High-Complexity" not in doc_tags:
                errors.append(
                    f"Template '{tmpl['name']}' with billing 99215 "
                    f"missing 'High-Complexity' doc tag."
                )

    if errors:
        return False, " ".join(errors)
    return True, "Patients with 99215 notes tagged. Template with 99215 has 'High-Complexity' doc tag."
