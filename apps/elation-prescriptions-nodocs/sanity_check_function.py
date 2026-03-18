#!/usr/bin/env python3
"""
Sanity check for Elation Prescriptions function-test tasks.

For each task, directly applies the expected end-state (bypassing the agent),
then runs the verifier and asserts it passes.

Usage:
    python3 sanity_check_function.py                     # All tasks, sequential
    python3 sanity_check_function.py --workers N          # N parallel environments
    python3 sanity_check_function.py --task-id task_5     # Single task
    python3 sanity_check_function.py --port 9000          # Custom base port
"""
import argparse
import importlib.util
import json
import os
import socket
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from copy import deepcopy
from pathlib import Path

import requests

APP_DIR = Path(__file__).resolve().parent
TASKS_FILE = APP_DIR / "function-tasks.json"

# JS snippet to evaluate data.js and emit the seed state as JSON
_SEED_STATE_JS = """
const fs = require('fs');
const vm = require('vm');
const code = fs.readFileSync(process.argv[1], 'utf8');
vm.runInThisContext(code);

const state = {
    _seedVersion: SEED_DATA_VERSION,
    patients: JSON.parse(JSON.stringify(PATIENTS)),
    currentPatientId: CURRENT_PATIENT_ID,
    providers: JSON.parse(JSON.stringify(PROVIDERS)),
    currentProviderId: CURRENT_USER_PROVIDER_ID,
    pharmacies: JSON.parse(JSON.stringify(PHARMACIES)),
    drugCatalog: JSON.parse(JSON.stringify(DRUG_CATALOG)),
    drugInteractions: JSON.parse(JSON.stringify(DRUG_INTERACTIONS)),
    prescriptions: JSON.parse(JSON.stringify(PRESCRIPTIONS)),
    refillRequests: JSON.parse(JSON.stringify(REFILL_REQUESTS)),
    settings: JSON.parse(JSON.stringify(DEFAULT_SETTINGS)),
    denyReasons: JSON.parse(JSON.stringify(DENY_REASONS)),
    _nextRxId: 31,
    _nextRrId: 13
};
process.stdout.write(JSON.stringify(state));
"""


# ── helpers ──────────────────────────────────────────────────────────

SEED_RX_IDS = {f"rx_{str(i).zfill(3)}" for i in range(1, 31)}


def find_rx(state, rx_id):
    for rx in state["prescriptions"]:
        if rx["id"] == rx_id:
            return rx
    raise ValueError(f"Prescription not found: {rx_id}")


def find_rr(state, rr_id):
    for rr in state["refillRequests"]:
        if rr["id"] == rr_id:
            return rr
    raise ValueError(f"Refill request not found: {rr_id}")


def next_rx_id(state):
    rid = state.get("_nextRxId", 31)
    state["_nextRxId"] = rid + 1
    return f"rx_{str(rid).zfill(3)}"


def provider_display_name(state, provider_id=None):
    pid = provider_id or state["currentProviderId"]
    for p in state["providers"]:
        if p["id"] == pid:
            prefix = "Dr. " if p["title"] in ("MD", "DO") else ""
            suffix = "" if p["title"] in ("MD", "DO") else f", {p['title']}"
            return f"{prefix}{p['firstName']} {p['lastName']}{suffix}"
    return "Unknown"


NOW = "2026-03-18"


# ── solve functions ──────────────────────────────────────────────────

def solve_task_1(state):
    """Create Ibuprofen 400mg prescription for pat_001."""
    rx_id = next_rx_id(state)
    pname = provider_display_name(state)
    state["prescriptions"].append({
        "id": rx_id,
        "patientId": "pat_001",
        "drugId": "drug_043",
        "drugName": "Ibuprofen",
        "brandName": "Motrin",
        "formStrength": "400mg Tablet",
        "dosage": "400mg",
        "frequency": "Twice daily",
        "route": "Oral",
        "quantity": 60,
        "daysSupply": 30,
        "refillsTotal": 2,
        "refillsRemaining": 2,
        "sig": "Take 1 tablet by mouth every 6-8 hours as needed with food",
        "daw": False,
        "pharmacyId": "pharm_001",
        "prescriberId": "prov_001",
        "status": "active",
        "startDate": NOW,
        "endDate": None,
        "priorAuth": False,
        "priorAuthNumber": None,
        "discontinuedReason": None,
        "discontinuedDate": None,
        "fillHistory": [],
        "history": [{"action": "prescribed", "date": NOW, "provider": pname, "note": "New prescription"}]
    })


def solve_task_2(state):
    """Create Omeprazole 20mg with DAW for pat_001."""
    rx_id = next_rx_id(state)
    pname = provider_display_name(state)
    state["prescriptions"].append({
        "id": rx_id,
        "patientId": "pat_001",
        "drugId": "drug_021",
        "drugName": "Omeprazole",
        "brandName": "Prilosec",
        "formStrength": "20mg Capsule, Delayed Release",
        "dosage": "20mg",
        "frequency": "Once daily",
        "route": "Oral",
        "quantity": 30,
        "daysSupply": 30,
        "refillsTotal": 0,
        "refillsRemaining": 0,
        "sig": "Take 1 capsule by mouth once daily before breakfast",
        "daw": True,
        "pharmacyId": "pharm_001",
        "prescriberId": "prov_001",
        "status": "active",
        "startDate": NOW,
        "endDate": None,
        "priorAuth": False,
        "priorAuthNumber": None,
        "discontinuedReason": None,
        "discontinuedDate": None,
        "fillHistory": [],
        "history": [{"action": "prescribed", "date": NOW, "provider": pname, "note": "New prescription"}]
    })


def solve_task_3(state):
    """Create Rosuvastatin 10mg with prior auth for pat_001."""
    rx_id = next_rx_id(state)
    pname = provider_display_name(state)
    state["prescriptions"].append({
        "id": rx_id,
        "patientId": "pat_001",
        "drugId": "drug_003",
        "drugName": "Rosuvastatin",
        "brandName": "Crestor",
        "formStrength": "10mg Tablet",
        "dosage": "10mg",
        "frequency": "Once daily",
        "route": "Oral",
        "quantity": 30,
        "daysSupply": 30,
        "refillsTotal": 2,
        "refillsRemaining": 2,
        "sig": "Take 1 tablet by mouth once daily",
        "daw": False,
        "pharmacyId": "pharm_001",
        "prescriberId": "prov_001",
        "status": "active",
        "startDate": NOW,
        "endDate": None,
        "priorAuth": True,
        "priorAuthNumber": "PA-2026-99999",
        "discontinuedReason": None,
        "discontinuedDate": None,
        "fillHistory": [],
        "history": [{"action": "prescribed", "date": NOW, "provider": pname, "note": "New prescription"}]
    })


def solve_task_4(state):
    """Create Montelukast to Alto Pharmacy for pat_001."""
    rx_id = next_rx_id(state)
    pname = provider_display_name(state)
    state["prescriptions"].append({
        "id": rx_id,
        "patientId": "pat_001",
        "drugId": "drug_051",
        "drugName": "Montelukast",
        "brandName": "Singulair",
        "formStrength": "10mg Tablet",
        "dosage": "10mg",
        "frequency": "Once daily",
        "route": "Oral",
        "quantity": 30,
        "daysSupply": 30,
        "refillsTotal": 5,
        "refillsRemaining": 5,
        "sig": "Take 1 tablet by mouth once daily in the evening",
        "daw": False,
        "pharmacyId": "pharm_007",
        "prescriberId": "prov_001",
        "status": "active",
        "startDate": NOW,
        "endDate": None,
        "priorAuth": False,
        "priorAuthNumber": None,
        "discontinuedReason": None,
        "discontinuedDate": None,
        "fillHistory": [],
        "history": [{"action": "prescribed", "date": NOW, "provider": pname, "note": "New prescription"}]
    })


def solve_task_5(state):
    """Switch to David Kowalski, create Cephalexin 500mg."""
    state["currentPatientId"] = "pat_002"
    rx_id = next_rx_id(state)
    pname = provider_display_name(state)
    state["prescriptions"].append({
        "id": rx_id,
        "patientId": "pat_002",
        "drugId": "drug_027",
        "drugName": "Cephalexin",
        "brandName": "Keflex",
        "formStrength": "500mg Capsule",
        "dosage": "500mg",
        "frequency": "Four times daily",
        "route": "Oral",
        "quantity": 28,
        "daysSupply": 7,
        "refillsTotal": 0,
        "refillsRemaining": 0,
        "sig": "Take 1 capsule by mouth four times daily for 7 days",
        "daw": False,
        "pharmacyId": "pharm_003",
        "prescriberId": "prov_001",
        "status": "active",
        "startDate": NOW,
        "endDate": None,
        "priorAuth": False,
        "priorAuthNumber": None,
        "discontinuedReason": None,
        "discontinuedDate": None,
        "fillHistory": [],
        "history": [{"action": "prescribed", "date": NOW, "provider": pname, "note": "New prescription"}]
    })


def solve_task_6(state):
    """Create Dulaglutide injectable for pat_001."""
    rx_id = next_rx_id(state)
    pname = provider_display_name(state)
    state["prescriptions"].append({
        "id": rx_id,
        "patientId": "pat_001",
        "drugId": "drug_050",
        "drugName": "Dulaglutide",
        "brandName": "Trulicity",
        "formStrength": "1.5mg/0.5mL Solution for Injection",
        "dosage": "1.5mg",
        "frequency": "Once weekly",
        "route": "Subcutaneous",
        "quantity": 4,
        "daysSupply": 28,
        "refillsTotal": 2,
        "refillsRemaining": 2,
        "sig": "Inject 1.5mg subcutaneously once weekly",
        "daw": False,
        "pharmacyId": "pharm_010",
        "prescriberId": "prov_001",
        "status": "active",
        "startDate": NOW,
        "endDate": None,
        "priorAuth": False,
        "priorAuthNumber": None,
        "discontinuedReason": None,
        "discontinuedDate": None,
        "fillHistory": [],
        "history": [{"action": "prescribed", "date": NOW, "provider": pname, "note": "New prescription"}]
    })


def solve_task_7(state):
    """Create Diltiazem 120mg with 5 refills for pat_001."""
    rx_id = next_rx_id(state)
    pname = provider_display_name(state)
    state["prescriptions"].append({
        "id": rx_id,
        "patientId": "pat_001",
        "drugId": "drug_055",
        "drugName": "Diltiazem",
        "brandName": "Cardizem",
        "formStrength": "120mg Capsule, Extended Release",
        "dosage": "120mg",
        "frequency": "Once daily",
        "route": "Oral",
        "quantity": 30,
        "daysSupply": 30,
        "refillsTotal": 5,
        "refillsRemaining": 5,
        "sig": "Take 1 capsule by mouth once daily",
        "daw": False,
        "pharmacyId": "pharm_001",
        "prescriberId": "prov_001",
        "status": "active",
        "startDate": NOW,
        "endDate": None,
        "priorAuth": False,
        "priorAuthNumber": None,
        "discontinuedReason": None,
        "discontinuedDate": None,
        "fillHistory": [],
        "history": [{"action": "prescribed", "date": NOW, "provider": pname, "note": "New prescription"}]
    })


def solve_task_8(state):
    """Create Pregabalin 75mg (Schedule V) for pat_001."""
    rx_id = next_rx_id(state)
    pname = provider_display_name(state)
    state["prescriptions"].append({
        "id": rx_id,
        "patientId": "pat_001",
        "drugId": "drug_037",
        "drugName": "Pregabalin",
        "brandName": "Lyrica",
        "formStrength": "75mg Capsule",
        "dosage": "75mg",
        "frequency": "Twice daily",
        "route": "Oral",
        "quantity": 60,
        "daysSupply": 30,
        "refillsTotal": 1,
        "refillsRemaining": 1,
        "sig": "Take 1 capsule by mouth twice daily",
        "daw": False,
        "pharmacyId": "pharm_001",
        "prescriberId": "prov_001",
        "status": "active",
        "startDate": NOW,
        "endDate": None,
        "priorAuth": False,
        "priorAuthNumber": None,
        "discontinuedReason": None,
        "discontinuedDate": None,
        "fillHistory": [],
        "history": [{"action": "prescribed", "date": NOW, "provider": pname, "note": "New prescription"}]
    })


def solve_task_9(state):
    """Discontinue rx_005 (Pantoprazole) with reason."""
    rx = find_rx(state, "rx_005")
    rx["status"] = "discontinued"
    rx["discontinuedReason"] = "No longer clinically indicated"
    rx["discontinuedDate"] = NOW
    rx["endDate"] = NOW
    rx["history"].append({
        "action": "discontinued", "date": NOW,
        "provider": provider_display_name(state),
        "note": "No longer clinically indicated"
    })


def solve_task_10(state):
    """Place rx_004 (Amlodipine) on hold."""
    rx = find_rx(state, "rx_004")
    rx["status"] = "on-hold"
    rx["history"].append({
        "action": "on-hold", "date": NOW,
        "provider": provider_display_name(state),
        "note": "Hypotension noted, monitoring BP"
    })


def solve_task_11(state):
    """Resume rx_012 (HCTZ) from hold."""
    rx = find_rx(state, "rx_012")
    rx["status"] = "active"
    rx["history"].append({
        "action": "resumed", "date": NOW,
        "provider": provider_display_name(state),
        "note": "Resumed from hold"
    })


def solve_task_12(state):
    """Cancel rx_008 (Albuterol)."""
    rx = find_rx(state, "rx_008")
    rx["status"] = "cancelled"
    rx["endDate"] = NOW
    rx["history"].append({
        "action": "cancelled", "date": NOW,
        "provider": provider_display_name(state),
        "note": "Prescription cancelled"
    })


def solve_task_13(state):
    """Renew rx_001 (Atorvastatin) with 5 refills."""
    rx = find_rx(state, "rx_001")
    rx["refillsRemaining"] = 5
    rx["refillsTotal"] = 5
    rx["status"] = "active"
    rx["history"].append({
        "action": "renewed", "date": NOW,
        "provider": provider_display_name(state),
        "note": "Renewed with 5 refills"
    })


def solve_task_14(state):
    """Renew rx_007 (Gabapentin) with 3 refills."""
    rx = find_rx(state, "rx_007")
    rx["refillsRemaining"] = 3
    rx["refillsTotal"] = 3
    rx["status"] = "active"
    rx["history"].append({
        "action": "renewed", "date": NOW,
        "provider": provider_display_name(state),
        "note": "Renewed with 3 refills"
    })


def solve_task_15(state):
    """Discontinue rx_013 (Sertraline) with reason."""
    rx = find_rx(state, "rx_013")
    rx["status"] = "discontinued"
    rx["discontinuedReason"] = "Patient request - tapering off"
    rx["discontinuedDate"] = NOW
    rx["endDate"] = NOW
    rx["history"].append({
        "action": "discontinued", "date": NOW,
        "provider": provider_display_name(state),
        "note": "Patient request - tapering off"
    })


def solve_task_16(state):
    """Place rx_006 (Levothyroxine) on hold."""
    rx = find_rx(state, "rx_006")
    rx["status"] = "on-hold"
    rx["history"].append({
        "action": "on-hold", "date": NOW,
        "provider": provider_display_name(state),
        "note": "Pending TSH results"
    })


def solve_task_17(state):
    """Cancel rx_002 (Lisinopril)."""
    rx = find_rx(state, "rx_002")
    rx["status"] = "cancelled"
    rx["endDate"] = NOW
    rx["history"].append({
        "action": "cancelled", "date": NOW,
        "provider": provider_display_name(state),
        "note": "Prescription cancelled"
    })


def solve_task_18(state):
    """Switch to William Thornton, discontinue rx_024 (Furosemide)."""
    state["currentPatientId"] = "pat_004"
    rx = find_rx(state, "rx_024")
    rx["status"] = "discontinued"
    rx["discontinuedReason"] = "Resolved peripheral edema"
    rx["discontinuedDate"] = NOW
    rx["endDate"] = NOW
    rx["history"].append({
        "action": "discontinued", "date": NOW,
        "provider": provider_display_name(state),
        "note": "Resolved peripheral edema"
    })


def solve_task_19(state):
    """Modify rx_001 dosage to 40mg."""
    rx = find_rx(state, "rx_001")
    rx["dosage"] = "40mg"
    rx["history"].append({
        "action": "modified", "date": NOW,
        "provider": provider_display_name(state),
        "note": "dosage: 20mg → 40mg"
    })


def solve_task_20(state):
    """Modify rx_007 frequency to Twice daily."""
    rx = find_rx(state, "rx_007")
    old = rx["frequency"]
    rx["frequency"] = "Twice daily"
    rx["history"].append({
        "action": "modified", "date": NOW,
        "provider": provider_display_name(state),
        "note": f"frequency: {old} → Twice daily"
    })


def solve_task_21(state):
    """Modify rx_003 sig."""
    rx = find_rx(state, "rx_003")
    rx["sig"] = "Take 1 tablet by mouth twice daily with meals"
    rx["history"].append({
        "action": "modified", "date": NOW,
        "provider": provider_display_name(state),
        "note": "sig updated"
    })


def solve_task_22(state):
    """Modify rx_004 quantity to 90."""
    rx = find_rx(state, "rx_004")
    rx["quantity"] = 90
    rx["history"].append({
        "action": "modified", "date": NOW,
        "provider": provider_display_name(state),
        "note": "quantity: 30 → 90"
    })


def solve_task_23(state):
    """Modify rx_013 dosage to 100mg."""
    rx = find_rx(state, "rx_013")
    rx["dosage"] = "100mg"
    rx["history"].append({
        "action": "modified", "date": NOW,
        "provider": provider_display_name(state),
        "note": "dosage: 50mg → 100mg"
    })


def solve_task_24(state):
    """Switch to Robert Fitzgerald, modify rx_028 dosage to 25mg."""
    state["currentPatientId"] = "pat_006"
    rx = find_rx(state, "rx_028")
    rx["dosage"] = "25mg"
    rx["history"].append({
        "action": "modified", "date": NOW,
        "provider": provider_display_name(state),
        "note": "dosage: 12.5mg → 25mg"
    })


def solve_task_25(state):
    """Approve refill rr_001 (Atorvastatin for Margaret Chen)."""
    rr = find_rr(state, "rr_001")
    rr["status"] = "approved"
    rr["responseDate"] = f"{NOW}T12:00:00Z"
    rr["respondedBy"] = "prov_001"
    # Side effect: decrement rx_001 refillsRemaining, add fill history
    rx = find_rx(state, "rx_001")
    if rx["refillsRemaining"] > 0:
        rx["refillsRemaining"] -= 1
    rx["fillHistory"].append({
        "fillDate": NOW,
        "pharmacy": rr["pharmacyName"],
        "quantity": rx["quantity"],
        "daysSupply": rx["daysSupply"],
        "fillNumber": len(rx["fillHistory"]) + 1
    })
    rx["history"].append({
        "action": "refill-approved", "date": NOW,
        "provider": "Dr. Mitchell",
        "note": "Refill request approved"
    })


def solve_task_26(state):
    """Deny refill rr_002 (Metformin) with reason."""
    rr = find_rr(state, "rr_002")
    rr["status"] = "denied"
    rr["denyReason"] = "Need lab work before renewal"
    rr["responseDate"] = f"{NOW}T12:00:00Z"
    rr["respondedBy"] = "prov_001"


def solve_task_27(state):
    """Modify and approve refill rr_003 (Pantoprazole)."""
    rr = find_rr(state, "rr_003")
    rr["status"] = "modified"
    rr["responseDate"] = f"{NOW}T12:00:00Z"
    rr["respondedBy"] = "prov_001"
    rr["modifiedDetails"] = "Changed to 20mg from 40mg per clinical review"


def solve_task_28(state):
    """Approve refill rr_005 (Metoprolol for David Kowalski)."""
    rr = find_rr(state, "rr_005")
    rr["status"] = "approved"
    rr["responseDate"] = f"{NOW}T12:00:00Z"
    rr["respondedBy"] = "prov_001"
    rx = find_rx(state, "rx_016")
    if rx["refillsRemaining"] > 0:
        rx["refillsRemaining"] -= 1
    rx["fillHistory"].append({
        "fillDate": NOW,
        "pharmacy": rr["pharmacyName"],
        "quantity": rx["quantity"],
        "daysSupply": rx["daysSupply"],
        "fillNumber": len(rx["fillHistory"]) + 1
    })
    rx["history"].append({
        "action": "refill-approved", "date": NOW,
        "provider": "Dr. Mitchell",
        "note": "Refill request approved"
    })


def solve_task_29(state):
    """Deny refill rr_007 (Valsartan for William Thornton)."""
    rr = find_rr(state, "rr_007")
    rr["status"] = "denied"
    rr["denyReason"] = "Need appointment - overdue for follow-up"
    rr["responseDate"] = f"{NOW}T12:00:00Z"
    rr["respondedBy"] = "prov_001"


def solve_task_30(state):
    """Approve refill rr_010 (Furosemide for William Thornton, urgent)."""
    rr = find_rr(state, "rr_010")
    rr["status"] = "approved"
    rr["responseDate"] = f"{NOW}T12:00:00Z"
    rr["respondedBy"] = "prov_001"
    rx = find_rx(state, "rx_024")
    if rx["refillsRemaining"] > 0:
        rx["refillsRemaining"] -= 1
    rx["fillHistory"].append({
        "fillDate": NOW,
        "pharmacy": rr["pharmacyName"],
        "quantity": rx["quantity"],
        "daysSupply": rx["daysSupply"],
        "fillNumber": len(rx["fillHistory"]) + 1
    })
    rx["history"].append({
        "action": "refill-approved", "date": NOW,
        "provider": "Dr. Mitchell",
        "note": "Refill request approved"
    })


def solve_task_31(state):
    """Deny refill rr_011 (Sertraline for Margaret Chen)."""
    rr = find_rr(state, "rr_011")
    rr["status"] = "denied"
    rr["denyReason"] = "Changed therapy"
    rr["responseDate"] = f"{NOW}T12:00:00Z"
    rr["respondedBy"] = "prov_001"


def solve_task_32(state):
    """Switch to David Kowalski."""
    state["currentPatientId"] = "pat_002"


def solve_task_33(state):
    """Switch to William Thornton."""
    state["currentPatientId"] = "pat_004"


def solve_task_34(state):
    """Switch to Aisha Rahman."""
    state["currentPatientId"] = "pat_003"


def solve_task_35(state):
    """Change default pharmacy to Walgreens (pharm_002)."""
    state["settings"]["defaultPharmacy"] = "pharm_002"


def solve_task_36(state):
    """Change default days supply to 90."""
    state["settings"]["defaultDaysSupply"] = 90


def solve_task_37(state):
    """Change default refills to 3."""
    state["settings"]["defaultRefills"] = 3


def solve_task_38(state):
    """Disable e-prescribing."""
    state["settings"]["eRxEnabled"] = False


def solve_task_39(state):
    """Disable auto-check drug interactions."""
    state["settings"]["autoCheckInteractions"] = False


def solve_task_40(state):
    """Disable require allergy review."""
    state["settings"]["requireAllergyReview"] = False


def solve_task_41(state):
    """Disable require signature."""
    state["settings"]["signatureRequired"] = False


def solve_task_42(state):
    """Change print format to detailed."""
    state["settings"]["printFormat"] = "detailed"


def solve_task_43(state):
    """Change print format to compact."""
    state["settings"]["printFormat"] = "compact"


def solve_task_44(state):
    """Disable show generic first."""
    state["settings"]["showGenericFirst"] = False


def solve_task_45(state):
    """Remove Atorvastatin (drug_001) from favorites."""
    favs = state["settings"]["favoritesDrugIds"]
    if "drug_001" in favs:
        favs.remove("drug_001")


def solve_task_46(state):
    """Remove Azithromycin (drug_028) from favorites."""
    favs = state["settings"]["favoritesDrugIds"]
    if "drug_028" in favs:
        favs.remove("drug_028")


def solve_task_47(state):
    """Add Metoprolol Succinate ER (drug_007) to favorites."""
    state["currentPatientId"] = "pat_002"
    favs = state["settings"]["favoritesDrugIds"]
    if "drug_007" not in favs:
        favs.append("drug_007")


def solve_task_48(state):
    """Add Apixaban (drug_012) to favorites."""
    favs = state["settings"]["favoritesDrugIds"]
    if "drug_012" not in favs:
        favs.append("drug_012")


def solve_task_49(state):
    """Remove Pantoprazole (drug_019) from favorites."""
    favs = state["settings"]["favoritesDrugIds"]
    if "drug_019" in favs:
        favs.remove("drug_019")


def solve_task_50(state):
    """Switch to Aisha Rahman, discontinue rx_021 (Escitalopram)."""
    state["currentPatientId"] = "pat_003"
    rx = find_rx(state, "rx_021")
    rx["status"] = "discontinued"
    rx["discontinuedReason"] = "Course completed, patient doing well"
    rx["discontinuedDate"] = NOW
    rx["endDate"] = NOW
    rx["history"].append({
        "action": "discontinued", "date": NOW,
        "provider": provider_display_name(state),
        "note": "Course completed, patient doing well"
    })


def solve_task_51(state):
    """Switch to William Thornton, renew rx_023 (Insulin Glargine) with 5 refills."""
    state["currentPatientId"] = "pat_004"
    rx = find_rx(state, "rx_023")
    rx["refillsRemaining"] = 5
    rx["refillsTotal"] = 5
    rx["status"] = "active"
    rx["history"].append({
        "action": "renewed", "date": NOW,
        "provider": provider_display_name(state),
        "note": "Renewed with 5 refills"
    })


def solve_task_52(state):
    """Switch to Jessica Morales, place rx_025 (Cephalexin) on hold."""
    state["currentPatientId"] = "pat_005"
    rx = find_rx(state, "rx_025")
    rx["status"] = "on-hold"
    rx["history"].append({
        "action": "on-hold", "date": NOW,
        "provider": provider_display_name(state),
        "note": "GI intolerance reported"
    })


def solve_task_53(state):
    """Change default pharmacy to Express Scripts and days supply to 90."""
    state["settings"]["defaultPharmacy"] = "pharm_008"
    state["settings"]["defaultDaysSupply"] = 90


def solve_task_54(state):
    """Switch to Robert Fitzgerald, modify rx_029 (Spironolactone) quantity to 60."""
    state["currentPatientId"] = "pat_006"
    rx = find_rx(state, "rx_029")
    rx["quantity"] = 60
    rx["history"].append({
        "action": "modified", "date": NOW,
        "provider": provider_display_name(state),
        "note": "quantity: 30 → 60"
    })


def solve_task_55(state):
    """Modify rx_014 (Apixaban) sig."""
    rx = find_rx(state, "rx_014")
    rx["sig"] = "Take 1 tablet by mouth twice daily with food"
    rx["history"].append({
        "action": "modified", "date": NOW,
        "provider": provider_display_name(state),
        "note": "sig updated"
    })


SOLVERS = {
    "task_1": solve_task_1,
    "task_2": solve_task_2,
    "task_3": solve_task_3,
    "task_4": solve_task_4,
    "task_5": solve_task_5,
    "task_6": solve_task_6,
    "task_7": solve_task_7,
    "task_8": solve_task_8,
    "task_9": solve_task_9,
    "task_10": solve_task_10,
    "task_11": solve_task_11,
    "task_12": solve_task_12,
    "task_13": solve_task_13,
    "task_14": solve_task_14,
    "task_15": solve_task_15,
    "task_16": solve_task_16,
    "task_17": solve_task_17,
    "task_18": solve_task_18,
    "task_19": solve_task_19,
    "task_20": solve_task_20,
    "task_21": solve_task_21,
    "task_22": solve_task_22,
    "task_23": solve_task_23,
    "task_24": solve_task_24,
    "task_25": solve_task_25,
    "task_26": solve_task_26,
    "task_27": solve_task_27,
    "task_28": solve_task_28,
    "task_29": solve_task_29,
    "task_30": solve_task_30,
    "task_31": solve_task_31,
    "task_32": solve_task_32,
    "task_33": solve_task_33,
    "task_34": solve_task_34,
    "task_35": solve_task_35,
    "task_36": solve_task_36,
    "task_37": solve_task_37,
    "task_38": solve_task_38,
    "task_39": solve_task_39,
    "task_40": solve_task_40,
    "task_41": solve_task_41,
    "task_42": solve_task_42,
    "task_43": solve_task_43,
    "task_44": solve_task_44,
    "task_45": solve_task_45,
    "task_46": solve_task_46,
    "task_47": solve_task_47,
    "task_48": solve_task_48,
    "task_49": solve_task_49,
    "task_50": solve_task_50,
    "task_51": solve_task_51,
    "task_52": solve_task_52,
    "task_53": solve_task_53,
    "task_54": solve_task_54,
    "task_55": solve_task_55,
}


# ── server management ────────────────────────────────────────────────

def generate_seed_state():
    """Use Node.js to evaluate data.js and produce the seed state JSON."""
    data_js = str(APP_DIR / "js" / "data.js")
    result = subprocess.run(
        ["node", "-e", _SEED_STATE_JS, data_js],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"Failed to generate seed state:\n{result.stderr}")
    return json.loads(result.stdout)


def seed_server(server_url, seed_state):
    """PUT the seed state to the server to establish the baseline."""
    resp = requests.put(
        f"{server_url}/api/state",
        json=seed_state,
        headers={"Content-Type": "application/json"},
    )
    if resp.status_code != 200:
        raise RuntimeError(f"Failed to seed server: HTTP {resp.status_code}")


def find_free_port(start=9000):
    """Find a free port starting from `start`."""
    port = start
    while port < start + 100:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("", port))
                return port
            except OSError:
                port += 1
    raise RuntimeError(f"No free port found in range {start}-{start+100}")


def start_server(port):
    """Start the app server on the given port."""
    proc = subprocess.Popen(
        [sys.executable, "server.py", "--port", str(port)],
        cwd=str(APP_DIR),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    for _ in range(30):
        try:
            requests.get(f"http://localhost:{port}/", timeout=1)
            return proc
        except (requests.ConnectionError, requests.Timeout):
            time.sleep(0.2)
    proc.kill()
    raise RuntimeError(f"Server failed to start on port {port}")


def stop_server(proc):
    """Stop the server process."""
    if proc and proc.poll() is None:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()


# ── task runner ──────────────────────────────────────────────────────

def load_tasks():
    """Load task definitions from function-tasks.json."""
    with open(TASKS_FILE) as f:
        return json.load(f)


def load_verifier(verify_path):
    """Dynamically load a verifier module."""
    full_path = APP_DIR / verify_path
    spec = importlib.util.spec_from_file_location("verifier", str(full_path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.verify


def run_single_task(task, server_url):
    """Reset → solve → verify for a single task."""
    task_id = task["id"]
    solver = SOLVERS.get(task_id)
    if not solver:
        return task_id, False, f"No solver defined for {task_id}"

    try:
        # 1. Reset to seed state
        resp = requests.post(f"{server_url}/api/reset")
        if resp.status_code != 200:
            return task_id, False, f"Reset failed: HTTP {resp.status_code}"

        time.sleep(0.3)

        # 2. Read seed state
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return task_id, False, f"Could not read state after reset: HTTP {resp.status_code}"
        state = resp.json()

        # 3. Apply the solve function
        solver(state)

        # 4. Write solved state back
        resp = requests.put(
            f"{server_url}/api/state",
            json=state,
            headers={"Content-Type": "application/json"},
        )
        if resp.status_code != 200:
            return task_id, False, f"Could not write state: HTTP {resp.status_code}"

        # 5. Run the verifier
        verify_fn = load_verifier(task["verify"])
        passed, message = verify_fn(server_url)
        return task_id, passed, message

    except Exception as e:
        return task_id, False, f"Exception: {e}"


def run_tasks_sequential(tasks, port, seed_state):
    """Run all tasks sequentially on a single server."""
    proc = start_server(port)
    server_url = f"http://localhost:{port}"
    results = []
    try:
        seed_server(server_url, seed_state)
        for task in tasks:
            result = run_single_task(task, server_url)
            results.append(result)
            status = "\033[32m  PASS\033[0m" if result[1] else "\033[31m  FAIL\033[0m"
            print(f"{status}  {result[0]:12s}  {result[2]}")
    finally:
        stop_server(proc)
    return results


def run_tasks_parallel(tasks, workers, base_port, seed_state):
    """Run tasks in parallel across multiple server instances."""
    results = []

    def worker_fn(task, port):
        proc = start_server(port)
        server_url = f"http://localhost:{port}"
        try:
            seed_server(server_url, seed_state)
            return run_single_task(task, server_url)
        finally:
            stop_server(proc)

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {}
        for i, task in enumerate(tasks):
            port = base_port + i
            future = executor.submit(worker_fn, task, port)
            futures[future] = task["id"]

        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            status = "\033[32m  PASS\033[0m" if result[1] else "\033[31m  FAIL\033[0m"
            print(f"{status}  {result[0]:12s}  {result[2]}")

    return results


# ── main ─────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Elation Prescriptions function-task sanity check")
    parser.add_argument("--task-id", type=str, help="Run a single task by ID")
    parser.add_argument("--workers", type=int, default=1, help="Number of parallel workers")
    parser.add_argument("--port", type=int, default=9500, help="Base port for servers")
    args = parser.parse_args()

    tasks = load_tasks()
    if args.task_id:
        tasks = [t for t in tasks if t["id"] == args.task_id]
        if not tasks:
            print(f"Task '{args.task_id}' not found.")
            sys.exit(1)

    print("Generating seed state from JS data...")
    seed_state = generate_seed_state()
    print(f"Running {len(tasks)} task(s)...\n")

    if args.workers <= 1:
        port = find_free_port(args.port)
        results = run_tasks_sequential(tasks, port, seed_state)
    else:
        results = run_tasks_parallel(tasks, args.workers, args.port, seed_state)

    # Summary
    passed = sum(1 for _, p, _ in results if p)
    total = len(results)
    failed = [tid for tid, p, _ in results if not p]

    print(f"\n{passed}/{total} passed")
    if failed:
        print(f"Failed: {', '.join(failed)}")
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
