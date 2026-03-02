#!/usr/bin/env python3
"""
Sanity check for function-tasks verifiers in the Elation Prescriptions app.

For each task, directly constructs the expected end-state (bypassing the UI),
writes it to the server, then runs the verifier and asserts it passes.
"""

import argparse
import importlib.util
import json
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from copy import deepcopy
from pathlib import Path

import requests

APP_DIR = Path(__file__).resolve().parent
TASKS_FILE = APP_DIR / "function-tasks.json"
SEED_LAST_RECONCILED = "2026-01-15T14:30:00Z"


# ──────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────

def get_seed_state():
    """Load seed data by evaluating data.js via Node."""
    data_js = APP_DIR / "js" / "data.js"
    node_script = r"""
    const fs = require('fs');
    const code = fs.readFileSync('%s', 'utf8');
    const fn = new Function(code + `; return {
        SEED_DATA_VERSION, CURRENT_USER, CURRENT_PATIENT,
        PERMANENT_RX_MEDS, PERMANENT_OTC_MEDS, TEMPORARY_MEDS,
        DISCONTINUED_MEDS, CANCELED_SCRIPTS, PHARMACIES,
        REFILL_REQUESTS, CHANGE_REQUESTS, RX_TEMPLATES,
        CUSTOM_SIGS, MEDICATION_DATABASE, DRUG_INTERACTIONS,
        FORMULARY_DATA, SETTINGS, PROVIDERS, DIAGNOSIS_CODES
    }`);
    const data = fn();
    const state = {
        _seedVersion: data.SEED_DATA_VERSION,
        currentUser: data.CURRENT_USER,
        currentPatient: data.CURRENT_PATIENT,
        permanentRxMeds: data.PERMANENT_RX_MEDS,
        permanentOtcMeds: data.PERMANENT_OTC_MEDS,
        temporaryMeds: data.TEMPORARY_MEDS,
        discontinuedMeds: data.DISCONTINUED_MEDS,
        canceledScripts: data.CANCELED_SCRIPTS,
        pharmacies: data.PHARMACIES,
        refillRequests: data.REFILL_REQUESTS,
        changeRequests: data.CHANGE_REQUESTS,
        rxTemplates: data.RX_TEMPLATES,
        customSigs: data.CUSTOM_SIGS,
        medicationDatabase: data.MEDICATION_DATABASE,
        drugInteractions: data.DRUG_INTERACTIONS,
        formularyData: data.FORMULARY_DATA,
        settings: data.SETTINGS,
        providers: data.PROVIDERS,
        diagnosisCodes: data.DIAGNOSIS_CODES,
        _nextPrxId: 100,
        _nextOtcId: 100,
        _nextTmpId: 100,
        _nextDiscId: 100,
        _nextCxlId: 100,
        _nextRrId: 100,
        _nextCrId: 100,
        _nextTplId: 100,
        _nextSigId: 100,
        _nextAlgId: 100
    };
    console.log(JSON.stringify(state));
    """ % str(data_js).replace("\\", "\\\\")

    result = subprocess.run(
        ["node", "-e", node_script],
        capture_output=True, text=True, timeout=10
    )
    if result.returncode != 0:
        raise RuntimeError(f"Node.js error: {result.stderr}")
    return json.loads(result.stdout)


def find_entity(lst, **kwargs):
    """Find first entity matching all key=value pairs."""
    for item in lst:
        if all(item.get(k) == v for k, v in kwargs.items()):
            return item
    return None


def find_entity_containing(lst, field, substring):
    """Find first entity where field contains substring."""
    for item in lst:
        if substring.lower() in item.get(field, "").lower():
            return item
    return None


def remove_entity(lst, **kwargs):
    """Remove and return first entity matching criteria."""
    for i, item in enumerate(lst):
        if all(item.get(k) == v for k, v in kwargs.items()):
            return lst.pop(i)
    raise ValueError(f"Entity not found: {kwargs}")


def load_verifier(verify_path):
    full_path = str(APP_DIR / verify_path)
    spec = importlib.util.spec_from_file_location("verifier", full_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.verify


def load_tasks():
    with open(TASKS_FILE) as f:
        return json.load(f)


NOW_DATE = "2026-03-02"
NOW_ISO = "2026-03-02T12:00:00.000Z"
CURRENT_USER_NAME = "Dr. Sarah Mitchell"
CURRENT_USER_ID = "prov_001"


# ──────────────────────────────────────────────
# Solve functions — one per task
# Each takes seed state (deep copy) and mutates it
# ──────────────────────────────────────────────

def solve_task_1(state):
    """Approve Lisinopril refill request."""
    req = find_entity(state["refillRequests"], medicationName="Lisinopril 10mg tablet", status="pending")
    req["status"] = "approved"
    req["processedDate"] = NOW_ISO
    req["processedBy"] = CURRENT_USER_NAME
    med = find_entity(state["permanentRxMeds"], medicationName="Lisinopril 10mg tablet")
    med["lastPrescribedDate"] = NOW_DATE


def solve_task_2(state):
    """Deny Atorvastatin refill request."""
    req = find_entity(state["refillRequests"], medicationName="Atorvastatin 20mg tablet", status="pending")
    req["status"] = "denied"
    req["processedDate"] = NOW_ISO
    req["processedBy"] = CURRENT_USER_NAME
    req["denyReason"] = "Patient needs lipid panel before renewal"


def solve_task_3(state):
    """Approve Gabapentin refill with modified sig."""
    req = find_entity(state["refillRequests"], medicationName="Gabapentin 300mg capsule", status="pending")
    req["status"] = "approved"
    req["processedDate"] = NOW_ISO
    req["processedBy"] = CURRENT_USER_NAME
    req["modifications"] = {"sig": "Take 1 capsule by mouth twice daily"}
    med = find_entity(state["permanentRxMeds"], medicationName="Gabapentin 300mg capsule")
    med["sig"] = "Take 1 capsule by mouth twice daily"
    med["lastPrescribedDate"] = NOW_DATE


def solve_task_4(state):
    """Approve Omeprazole refill request."""
    req = find_entity(state["refillRequests"], medicationName="Omeprazole 20mg capsule", status="pending")
    req["status"] = "approved"
    req["processedDate"] = NOW_ISO
    req["processedBy"] = CURRENT_USER_NAME
    med = find_entity(state["permanentRxMeds"], medicationName="Omeprazole 20mg capsule")
    med["lastPrescribedDate"] = NOW_DATE


def solve_task_5(state):
    """Deny Sertraline refill request."""
    req = find_entity(state["refillRequests"], medicationName="Sertraline 50mg tablet", status="pending")
    req["status"] = "denied"
    req["processedDate"] = NOW_ISO
    req["processedBy"] = CURRENT_USER_NAME
    req["denyReason"] = "Requires follow-up appointment"


def solve_task_6(state):
    """Approve Metoprolol refill with modified refills."""
    req = find_entity(state["refillRequests"], medicationName="Metoprolol Succinate ER 50mg tablet", status="pending")
    req["status"] = "approved"
    req["processedDate"] = NOW_ISO
    req["processedBy"] = CURRENT_USER_NAME
    req["modifications"] = {"refills": 3}
    med = find_entity(state["permanentRxMeds"], medicationName="Metoprolol Succinate ER 50mg tablet")
    med["refillsRemaining"] = 3
    med["lastPrescribedDate"] = NOW_DATE


def solve_task_7(state):
    """Approve Atorvastatin→Rosuvastatin change request."""
    req = find_entity(state["changeRequests"], originalMedication="Atorvastatin 20mg tablet")
    req["status"] = "approved"
    req["processedDate"] = NOW_ISO
    req["processedBy"] = CURRENT_USER_NAME


def solve_task_8(state):
    """Deny Gabapentin sig clarification change request."""
    req = find_entity(state["changeRequests"], medicationName="Gabapentin 300mg capsule")
    req["status"] = "denied"
    req["processedDate"] = NOW_ISO
    req["processedBy"] = CURRENT_USER_NAME
    req["denyReason"] = "Current sig is correct as written"


def solve_task_9(state):
    """Remove Latex allergy."""
    allergies = state["currentPatient"]["allergies"]
    remove_entity(allergies, allergen="Latex")


def solve_task_10(state):
    """Remove Codeine allergy."""
    allergies = state["currentPatient"]["allergies"]
    remove_entity(allergies, allergen="Codeine")


def solve_task_11(state):
    """Add Ibuprofen drug allergy."""
    state["currentPatient"]["allergies"].append({
        "id": f"alg_{state['_nextAlgId']:03d}",
        "allergen": "Ibuprofen",
        "reaction": "Stomach upset, GI bleeding",
        "severity": "Moderate",
        "type": "drug",
        "onsetDate": NOW_DATE,
        "source": "provider-entered"
    })
    state["_nextAlgId"] += 1


def solve_task_12(state):
    """Add Bee stings environmental allergy."""
    state["currentPatient"]["allergies"].append({
        "id": f"alg_{state['_nextAlgId']:03d}",
        "allergen": "Bee stings",
        "reaction": "Swelling, anaphylaxis",
        "severity": "Severe",
        "type": "environmental",
        "onsetDate": NOW_DATE,
        "source": "provider-entered"
    })
    state["_nextAlgId"] += 1


def solve_task_13(state):
    """Move Montelukast from permanent Rx to temporary."""
    med = remove_entity(state["permanentRxMeds"], medicationName="Montelukast 10mg tablet")
    med["classification"] = "temporary"
    state["temporaryMeds"].append(med)


def solve_task_14(state):
    """Move Amoxicillin from temporary to permanent Rx."""
    med = remove_entity(state["temporaryMeds"], medicationName="Amoxicillin 500mg capsule")
    med["classification"] = "permanent_rx"
    state["permanentRxMeds"].append(med)


def solve_task_15(state):
    """Move Prednisone from temporary to permanent Rx."""
    med = remove_entity(state["temporaryMeds"], medicationName="Prednisone 10mg tablet")
    med["classification"] = "permanent_rx"
    state["permanentRxMeds"].append(med)


def _discontinue_med(state, med_name, source_list_key, reason, details="", send_cancel=False):
    """Helper: discontinue a medication."""
    med = remove_entity(state[source_list_key], medicationName=med_name)
    med["status"] = "discontinued"
    med["classification"] = "discontinued"
    med["discontinuedDate"] = NOW_DATE
    med["discontinuedBy"] = CURRENT_USER_NAME
    med["discontinueReason"] = reason
    med["discontinueDetails"] = details
    if send_cancel and med.get("pharmacyId"):
        cxl_id = f"cxl_{state['_nextCxlId']:03d}"
        state["canceledScripts"].append({
            "id": cxl_id,
            "medicationName": med["medicationName"],
            "ndc": med.get("ndc"),
            "sig": med["sig"],
            "qty": med["qty"],
            "refills": med.get("refills", 0),
            "daysSupply": med.get("daysSupply", 30),
            "status": "canceled",
            "classification": "canceled",
            "prescriberId": med.get("prescriberId"),
            "prescriberName": med.get("prescriberName"),
            "pharmacyId": med["pharmacyId"],
            "pharmacyName": med.get("pharmacyName"),
            "prescribedDate": med.get("lastPrescribedDate"),
            "canceledDate": NOW_DATE,
            "cancelReason": "Medication discontinued: " + reason,
            "diagnosis": med.get("diagnosis", [])
        })
        state["_nextCxlId"] += 1
    state["discontinuedMeds"].append(med)


def solve_task_16(state):
    """Discontinue Omeprazole."""
    _discontinue_med(state, "Omeprazole 20mg capsule", "permanentRxMeds",
                     "I want to discontinue this medication", "Switching to famotidine")


def solve_task_17(state):
    """Discontinue Amlodipine with cancel request."""
    _discontinue_med(state, "Amlodipine 5mg tablet", "permanentRxMeds",
                     "I want to discontinue this medication", send_cancel=True)


def solve_task_18(state):
    """Discontinue Montelukast."""
    _discontinue_med(state, "Montelukast 10mg tablet", "permanentRxMeds",
                     "Patient stopped taking medication")


def solve_task_19(state):
    """Discontinue Ciprofloxacin (temporary)."""
    _discontinue_med(state, "Ciprofloxacin 500mg tablet", "temporaryMeds",
                     "I want to discontinue this medication")


def solve_task_20(state):
    """Discontinue Gabapentin with cancel request."""
    _discontinue_med(state, "Gabapentin 300mg capsule", "permanentRxMeds",
                     "I want to discontinue this medication", send_cancel=True)


def solve_task_21(state):
    """Set drug-to-drug level to major_only."""
    state["settings"]["drugDecisionSupport"]["drugToDrugLevel"] = "major_only"


def solve_task_22(state):
    """Disable drug-to-allergy checking."""
    state["settings"]["drugDecisionSupport"]["drugToAllergyEnabled"] = False


def solve_task_23(state):
    """Set drug-to-drug level to major_moderate."""
    state["settings"]["drugDecisionSupport"]["drugToDrugLevel"] = "major_moderate"


def solve_task_24(state):
    """Disable auto-populate last pharmacy."""
    state["settings"]["autoPopulateLastPharmacy"] = False


def solve_task_25(state):
    """Disable show cost estimates."""
    state["settings"]["showCostEstimates"] = False


def solve_task_26(state):
    """Disable show formulary data."""
    state["settings"]["showFormularyData"] = False


def solve_task_27(state):
    """Change default pharmacy to Walgreens #7892."""
    pharm = find_entity_containing(state["pharmacies"], "name", "Walgreens #7892")
    state["settings"]["defaultPharmacyId"] = pharm["id"]


def solve_task_28(state):
    """Delete Prednisone taper template."""
    remove_entity(state["rxTemplates"], medicationName="Prednisone 10mg tablet (taper)")


def solve_task_29(state):
    """Delete Azithromycin Z-Pack template."""
    remove_entity(state["rxTemplates"], medicationName="Azithromycin 250mg tablet (Z-Pack)")


def solve_task_30(state):
    """Add Levothyroxine template."""
    tpl_id = f"tpl_{state['_nextTplId']:03d}"
    state["rxTemplates"].append({
        "id": tpl_id,
        "medicationName": "Levothyroxine 50mcg tablet",
        "sig": "Take 1 tablet by mouth once daily on empty stomach",
        "qty": 30,
        "unit": "tablets",
        "refills": 5,
        "daysSupply": 30,
        "ndc": None,
        "createdDate": NOW_DATE
    })
    state["_nextTplId"] += 1


def solve_task_31(state):
    """Edit Lisinopril 10mg template sig."""
    tpl = find_entity(state["rxTemplates"], medicationName="Lisinopril 10mg tablet")
    tpl["sig"] = "Take 1 tablet by mouth once daily in the morning"


def solve_task_32(state):
    """Edit Metformin 500mg template qty."""
    tpl = find_entity(state["rxTemplates"], medicationName="Metformin 500mg tablet")
    tpl["qty"] = 90


def solve_task_33(state):
    """Delete injectable sig."""
    remove_entity(state["customSigs"], text="Inject subcutaneously once weekly")


def solve_task_34(state):
    """Add oral custom sig."""
    sig_id = f"sig_{state['_nextSigId']:03d}"
    state["customSigs"].append({
        "id": sig_id,
        "text": "Take 2 capsules by mouth once daily with breakfast",
        "category": "oral"
    })
    state["_nextSigId"] += 1


def solve_task_35(state):
    """Add topical custom sig."""
    sig_id = f"sig_{state['_nextSigId']:03d}"
    state["customSigs"].append({
        "id": sig_id,
        "text": "Apply 1 patch to skin every 72 hours",
        "category": "topical"
    })
    state["_nextSigId"] += 1


def solve_task_36(state):
    """Edit sublingual sig text."""
    sig = find_entity(state["customSigs"], text="Dissolve 1 tablet under the tongue as needed")
    sig["text"] = "Dissolve 1 tablet under the tongue every 5 minutes as needed, max 3 doses"


def solve_task_37(state):
    """Delete ophthalmic sig."""
    remove_entity(state["customSigs"], text="Instill 1 drop in affected eye(s) twice daily")


def _add_prescription(state, med_name, sig, qty, unit, refills, days_supply,
                      classification, pharmacy_name=None, diagnosis=None,
                      daw=False, instructions="", is_controlled=False,
                      schedule_class=None):
    """Helper: add a new prescription to state."""
    pharmacy_id = None
    pharm_name = None
    if pharmacy_name:
        pharm = find_entity_containing(state["pharmacies"], "name", pharmacy_name)
        if pharm:
            pharmacy_id = pharm["id"]
            pharm_name = pharm["name"]

    prx_id = f"prx_{state['_nextPrxId']:03d}"
    med = {
        "id": prx_id,
        "medicationName": med_name,
        "ndc": None,
        "sig": sig,
        "qty": qty,
        "unit": unit,
        "refills": refills,
        "refillsRemaining": refills,
        "daysSupply": days_supply,
        "dispenseAsWritten": daw,
        "status": "active",
        "classification": classification,
        "prescriberId": CURRENT_USER_ID,
        "prescriberName": CURRENT_USER_NAME,
        "pharmacyId": pharmacy_id,
        "pharmacyName": pharm_name,
        "startDate": NOW_DATE,
        "lastPrescribedDate": NOW_DATE,
        "lastFilledDate": None,
        "nextRefillDate": None,
        "diagnosis": diagnosis or [],
        "isControlled": is_controlled,
        "scheduleClass": schedule_class,
        "instructionsToPharmacy": instructions,
        "doNotFillBefore": None
    }
    if classification == "temporary":
        state["temporaryMeds"].append(med)
    elif classification == "permanent_otc":
        state["permanentOtcMeds"].append(med)
    else:
        state["permanentRxMeds"].append(med)
    state["_nextPrxId"] += 1
    return med


def solve_task_38(state):
    """Prescribe Levothyroxine 50mcg as permanent Rx to CVS #4521."""
    _add_prescription(state, "Levothyroxine 50mcg tablet",
                      "Take 1 tablet by mouth once daily on empty stomach",
                      30, "tablets", 5, 30, "permanent_rx", "CVS Pharmacy #4521")


def solve_task_39(state):
    """Prescribe Cyclobenzaprine 10mg as temporary."""
    _add_prescription(state, "Cyclobenzaprine 10mg tablet",
                      "Take 1 tablet by mouth three times daily as needed for muscle spasm",
                      30, "tablets", 0, 10, "temporary")


def solve_task_40(state):
    """Prescribe Famotidine 20mg with DAW."""
    _add_prescription(state, "Famotidine 20mg tablet",
                      "Take 1 tablet by mouth twice daily",
                      60, "tablets", 3, 30, "permanent_rx", "CVS Pharmacy #4521",
                      daw=True)


def solve_task_41(state):
    """Prescribe Albuterol inhaler with diagnosis."""
    _add_prescription(state, "Albuterol 90mcg/actuation inhaler",
                      "Inhale 1-2 puffs every 4-6 hours as needed",
                      1, "inhalers", 2, 30, "permanent_rx", "CVS Pharmacy #4521",
                      diagnosis=[{"code": "J45.20", "description": "Mild intermittent asthma"}])


def solve_task_42(state):
    """Prescribe Doxycycline 100mg as temporary to Walgreens."""
    _add_prescription(state, "Doxycycline 100mg capsule",
                      "Take 1 capsule by mouth twice daily for 14 days",
                      28, "capsules", 0, 14, "temporary", "Walgreens #7892")


def solve_task_43(state):
    """Prescribe Ondansetron 4mg as temporary with instructions."""
    _add_prescription(state, "Ondansetron 4mg tablet",
                      "Take 1 tablet by mouth every 8 hours as needed for nausea",
                      12, "tablets", 0, 4, "temporary",
                      instructions="Patient is post-surgical, urgent fill requested")


def solve_task_44(state):
    """Prescribe Amlodipine 10mg to preferred pharmacy with diagnosis."""
    preferred_id = state["currentPatient"]["preferredPharmacyId"]
    pharm = find_entity(state["pharmacies"], id=preferred_id)
    _add_prescription(state, "Amlodipine 10mg tablet",
                      "Take 1 tablet by mouth once daily",
                      30, "tablets", 3, 30, "permanent_rx", pharm["name"],
                      diagnosis=[{"code": "I10", "description": "Essential hypertension"}])


def solve_task_45(state):
    """Prescribe Escitalopram 10mg to Alto Pharmacy."""
    _add_prescription(state, "Escitalopram 10mg tablet",
                      "Take 1 tablet by mouth once daily in the morning",
                      30, "tablets", 5, 30, "permanent_rx", "Alto Pharmacy")


def _document_med(state, med_name, sig, med_type="otc", qty=0, unit="tablets",
                  days_supply=30, diagnosis=None):
    """Helper: document an existing medication."""
    if med_type == "otc":
        med_id = f"otc_{state['_nextOtcId']:03d}"
        state["_nextOtcId"] += 1
        classification = "permanent_otc"
    else:
        med_id = f"prx_{state['_nextPrxId']:03d}"
        state["_nextPrxId"] += 1
        classification = "permanent_rx"

    med = {
        "id": med_id,
        "medicationName": med_name,
        "ndc": None,
        "sig": sig,
        "qty": qty,
        "unit": unit,
        "refills": 0,
        "refillsRemaining": 0,
        "daysSupply": days_supply,
        "dispenseAsWritten": False,
        "status": "active",
        "classification": classification,
        "prescriberId": None,
        "prescriberName": None,
        "pharmacyId": None,
        "pharmacyName": None,
        "startDate": NOW_DATE,
        "lastPrescribedDate": None,
        "documentedDate": NOW_DATE,
        "diagnosis": diagnosis or [],
        "isControlled": False,
        "scheduleClass": None
    }
    if med_type == "otc":
        state["permanentOtcMeds"].append(med)
    else:
        state["permanentRxMeds"].append(med)
    return med


def solve_task_46(state):
    """Document Glucosamine as OTC."""
    _document_med(state, "Glucosamine 1500mg tablet",
                  "Take 1 tablet by mouth once daily")


def solve_task_47(state):
    """Document Probiotics as OTC."""
    _document_med(state, "Probiotics capsule",
                  "Take 1 capsule by mouth once daily with food")


def solve_task_48(state):
    """Complete reconciliation without changes."""
    state["currentPatient"]["lastReconciledDate"] = NOW_ISO


def solve_task_49(state):
    """Reconcile and discontinue Aspirin 81mg."""
    state["currentPatient"]["lastReconciledDate"] = NOW_ISO
    _discontinue_med(state, "Aspirin 81mg tablet (low-dose)", "permanentOtcMeds",
                     "I want to discontinue this medication")


def solve_task_50(state):
    """Bulk refill Lisinopril and Metformin."""
    lisinopril = find_entity(state["permanentRxMeds"], medicationName="Lisinopril 10mg tablet")
    metformin = find_entity(state["permanentRxMeds"], medicationName="Metformin 500mg tablet")
    for orig in [lisinopril, metformin]:
        _add_prescription(state, orig["medicationName"], orig["sig"],
                          orig["qty"], orig["unit"], orig["refills"],
                          orig["daysSupply"], "permanent_rx",
                          orig.get("pharmacyName"))


def solve_task_51(state):
    """Approve the refill request with urgent notes (Gabapentin)."""
    # Find by notes content, not by ID
    for req in state["refillRequests"]:
        if req.get("notes") and "running low" in req["notes"].lower():
            req["status"] = "approved"
            req["processedDate"] = NOW_ISO
            req["processedBy"] = CURRENT_USER_NAME
            break


def solve_task_52(state):
    """Change default pharmacy to UCSF."""
    pharm = find_entity_containing(state["pharmacies"], "name", "UCSF")
    state["settings"]["defaultPharmacyId"] = pharm["id"]


def solve_task_53(state):
    """Discontinue the only active controlled substance (Alprazolam)."""
    # Find the controlled substance in active lists
    for list_key in ["permanentRxMeds", "permanentOtcMeds", "temporaryMeds"]:
        for med in state[list_key]:
            if med.get("isControlled"):
                _discontinue_med(state, med["medicationName"], list_key,
                                 "I want to discontinue this medication", send_cancel=True)
                return


def solve_task_54(state):
    """Approve the therapeutic substitution change request."""
    for req in state["changeRequests"]:
        if req.get("requestedMedication") != req.get("originalMedication"):
            req["status"] = "approved"
            req["processedDate"] = NOW_ISO
            req["processedBy"] = CURRENT_USER_NAME
            break


def solve_task_55(state):
    """Discontinue Sertraline with cancel request."""
    _discontinue_med(state, "Sertraline 50mg tablet", "permanentRxMeds",
                     "I want to discontinue this medication", send_cancel=True)


def solve_task_56(state):
    """Approve Metoprolol refill with modified sig."""
    req = find_entity(state["refillRequests"],
                      medicationName="Metoprolol Succinate ER 50mg tablet", status="pending")
    req["status"] = "approved"
    req["processedDate"] = NOW_ISO
    req["processedBy"] = CURRENT_USER_NAME
    req["modifications"] = {"sig": "Take 1 tablet by mouth once daily in the morning"}
    med = find_entity(state["permanentRxMeds"],
                      medicationName="Metoprolol Succinate ER 50mg tablet")
    med["sig"] = "Take 1 tablet by mouth once daily in the morning"
    med["lastPrescribedDate"] = NOW_DATE


# Map task IDs to solve functions
SOLVE_MAP = {
    f"task_{i}": globals()[f"solve_task_{i}"]
    for i in range(1, 57)
}


# ──────────────────────────────────────────────
# Runner
# ──────────────────────────────────────────────

def run_single_task(task, server_url, seed_state):
    """Reset → solve → write state → verify. Returns (task_id, passed, message)."""
    task_id = task["id"]

    # 1. Reset
    resp = requests.post(f"{server_url}/api/reset")
    if resp.status_code != 200:
        return task_id, False, f"Reset failed: {resp.status_code}"
    time.sleep(0.3)

    # 2. Clone seed state and apply solve
    state = deepcopy(seed_state)
    solve_fn = SOLVE_MAP.get(task_id)
    if solve_fn is None:
        return task_id, False, f"No solve function for {task_id}"
    try:
        solve_fn(state)
    except Exception as e:
        return task_id, False, f"Solve function error: {e}"

    # 3. Write solved state to server
    resp = requests.put(f"{server_url}/api/state", json=state)
    if resp.status_code != 200:
        return task_id, False, f"PUT state failed: {resp.status_code}"

    # 4. Run verifier
    try:
        verify_fn = load_verifier(task["verify"])
        passed, message = verify_fn(server_url)
    except Exception as e:
        return task_id, False, f"Verifier exception: {e}"

    return task_id, passed, message


def run_worker(tasks, base_port, worker_id, seed_state):
    """Run tasks sequentially on a dedicated server instance."""
    port = base_port + worker_id
    server_url = f"http://localhost:{port}"

    # Start server
    proc = subprocess.Popen(
        [sys.executable, str(APP_DIR / "server.py"), "--port", str(port)],
        cwd=str(APP_DIR),
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    time.sleep(1.5)

    results = []
    try:
        # Seed the server first
        requests.put(f"{server_url}/api/state", json=seed_state)
        time.sleep(0.3)

        for task in tasks:
            tid, passed, msg = run_single_task(task, server_url, seed_state)
            results.append((tid, passed, msg))
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()

    return results


def main():
    parser = argparse.ArgumentParser(description="Sanity check for function-task verifiers")
    parser.add_argument("--task-id", type=str, default=None, help="Run a single task")
    parser.add_argument("--workers", type=int, default=1, help="Parallel workers")
    parser.add_argument("--port", type=int, default=8100, help="Base port")
    args = parser.parse_args()

    print("Loading seed data...")
    seed_state = get_seed_state()

    tasks = load_tasks()
    if args.task_id:
        ids = [s.strip() for s in args.task_id.split(",")]
        tasks = [t for t in tasks if t["id"] in ids]
        if not tasks:
            print(f"Task {args.task_id} not found.")
            sys.exit(1)

    print(f"Running sanity check for {len(tasks)} task(s) with {args.workers} worker(s)...\n")

    all_results = []

    if args.workers == 1:
        all_results = run_worker(tasks, args.port, 0, seed_state)
    else:
        # Partition tasks across workers
        chunks = [[] for _ in range(args.workers)]
        for i, task in enumerate(tasks):
            chunks[i % args.workers].append(task)

        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {
                executor.submit(run_worker, chunk, args.port, wid, seed_state): wid
                for wid, chunk in enumerate(chunks) if chunk
            }
            for future in as_completed(futures):
                all_results.extend(future.result())

    # Sort by task number for consistent output
    def sort_key(r):
        tid = r[0]
        num = int(tid.replace("task_", ""))
        return num
    all_results.sort(key=sort_key)

    # Print results
    passed_count = 0
    failed = []
    for tid, passed, msg in all_results:
        status = "\033[32m  PASS\033[0m" if passed else "\033[31m  FAIL\033[0m"
        print(f"{status}  {tid:12s}  {msg}")
        if passed:
            passed_count += 1
        else:
            failed.append(tid)

    print(f"\n{passed_count}/{len(all_results)} passed")
    if failed:
        print(f"Failed: {', '.join(failed)}")

    sys.exit(0 if not failed else 1)


if __name__ == "__main__":
    main()
