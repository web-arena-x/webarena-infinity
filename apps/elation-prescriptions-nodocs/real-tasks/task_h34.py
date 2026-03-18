import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Interaction-aware macrolide: prescribe Azithromycin (not Clarithromycin)."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []
    seed_ids = {f"rx_{str(i).zfill(3)}" for i in range(1, 31)}

    # Should have Azithromycin for Margaret
    azithro = [
        rx for rx in state["prescriptions"]
        if rx["id"] not in seed_ids
        and rx.get("patientId") == "pat_001"
        and "azithromycin" in rx.get("drugName", "").lower()
    ]
    if not azithro:
        errors.append("No new Azithromycin prescription found for Margaret (pat_001).")
    else:
        new_rx = azithro[0]
        if "250mg" not in new_rx.get("formStrength", "").lower().replace(" ", ""):
            errors.append(f"Expected formStrength containing '250mg', got '{new_rx.get('formStrength')}'.")
        if new_rx.get("frequency") != "Once daily":
            errors.append(f"Expected frequency 'Once daily', got '{new_rx.get('frequency')}'.")
        if new_rx.get("quantity") != 6:
            errors.append(f"Expected quantity 6, got {new_rx.get('quantity')}.")
        if new_rx.get("refillsTotal") != 0:
            errors.append(f"Expected refillsTotal 0, got {new_rx.get('refillsTotal')}.")
        if new_rx.get("pharmacyId") != "pharm_001":
            errors.append(f"Expected pharmacyId 'pharm_001' (CVS), got '{new_rx.get('pharmacyId')}'.")

    # Should NOT have Clarithromycin
    clarithro = [
        rx for rx in state["prescriptions"]
        if rx["id"] not in seed_ids
        and rx.get("patientId") == "pat_001"
        and "clarithromycin" in rx.get("drugName", "").lower()
    ]
    if clarithro:
        errors.append("Clarithromycin was prescribed but has a major interaction with the patient's statin.")

    if errors:
        return False, " ".join(errors)
    return True, "Azithromycin prescribed correctly (safe macrolide choice given statin interaction)."
