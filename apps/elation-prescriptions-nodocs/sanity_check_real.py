#!/usr/bin/env python3
"""
Sanity check for Elation Prescriptions real tasks.

For each task, directly applies the expected end-state (bypassing the agent),
then runs the verifier and asserts it passes.

Usage:
    python3 sanity_check_real.py                     # All tasks, sequential
    python3 sanity_check_real.py --workers N          # N parallel environments
    python3 sanity_check_real.py --task-id task_e1    # Single task
    python3 sanity_check_real.py --port 9600          # Custom base port
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
TASKS_FILE = APP_DIR / "real-tasks.json"

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


def new_rx(state, patient_id, drug_id, drug_name, brand_name, form_strength,
           dosage, frequency, route, quantity, days_supply, refills, sig,
           pharmacy_id, daw=False, prior_auth=False, prior_auth_number=None, note="New prescription"):
    """Helper to create a new prescription in the state."""
    rx_id = next_rx_id(state)
    pname = provider_display_name(state)
    state["prescriptions"].append({
        "id": rx_id,
        "patientId": patient_id,
        "drugId": drug_id,
        "drugName": drug_name,
        "brandName": brand_name,
        "formStrength": form_strength,
        "dosage": dosage,
        "frequency": frequency,
        "route": route,
        "quantity": quantity,
        "daysSupply": days_supply,
        "refillsTotal": refills,
        "refillsRemaining": refills,
        "sig": sig,
        "daw": daw,
        "pharmacyId": pharmacy_id,
        "prescriberId": state["currentProviderId"],
        "status": "active",
        "startDate": NOW,
        "endDate": None,
        "priorAuth": prior_auth,
        "priorAuthNumber": prior_auth_number,
        "discontinuedReason": None,
        "discontinuedDate": None,
        "fillHistory": [],
        "history": [{"action": "prescribed", "date": NOW, "provider": pname, "note": note}]
    })


def discontinue_rx(state, rx_id, reason):
    rx = find_rx(state, rx_id)
    rx["status"] = "discontinued"
    rx["discontinuedReason"] = reason
    rx["discontinuedDate"] = NOW
    rx["endDate"] = NOW
    rx["history"].append({
        "action": "discontinued", "date": NOW,
        "provider": provider_display_name(state), "note": reason
    })


def hold_rx(state, rx_id, reason="Placed on hold"):
    rx = find_rx(state, rx_id)
    rx["status"] = "on-hold"
    rx["history"].append({
        "action": "on-hold", "date": NOW,
        "provider": provider_display_name(state), "note": reason
    })


def cancel_rx(state, rx_id):
    rx = find_rx(state, rx_id)
    rx["status"] = "cancelled"
    rx["endDate"] = NOW
    rx["history"].append({
        "action": "cancelled", "date": NOW,
        "provider": provider_display_name(state), "note": "Prescription cancelled"
    })


def resume_rx(state, rx_id):
    rx = find_rx(state, rx_id)
    rx["status"] = "active"
    rx["history"].append({
        "action": "resumed", "date": NOW,
        "provider": provider_display_name(state), "note": "Resumed from hold"
    })


def renew_rx(state, rx_id, refills):
    rx = find_rx(state, rx_id)
    rx["refillsRemaining"] = refills
    rx["refillsTotal"] = refills
    rx["status"] = "active"
    rx["history"].append({
        "action": "renewed", "date": NOW,
        "provider": provider_display_name(state),
        "note": f"Renewed with {refills} refills"
    })


def modify_rx(state, rx_id, changes):
    rx = find_rx(state, rx_id)
    for key, value in changes.items():
        rx[key] = value
    rx["history"].append({
        "action": "modified", "date": NOW,
        "provider": provider_display_name(state),
        "note": "Modified"
    })


def approve_rr(state, rr_id):
    rr = find_rr(state, rr_id)
    rr["status"] = "approved"
    rr["responseDate"] = f"{NOW}T12:00:00Z"
    rr["respondedBy"] = "prov_001"
    rx = find_rx(state, rr["prescriptionId"])
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
        "provider": "Dr. Mitchell", "note": "Refill request approved"
    })


def deny_rr(state, rr_id, reason):
    rr = find_rr(state, rr_id)
    rr["status"] = "denied"
    rr["denyReason"] = reason
    rr["responseDate"] = f"{NOW}T12:00:00Z"
    rr["respondedBy"] = "prov_001"


def modify_approve_rr(state, rr_id, details):
    rr = find_rr(state, rr_id)
    rr["status"] = "modified"
    rr["responseDate"] = f"{NOW}T12:00:00Z"
    rr["respondedBy"] = "prov_001"
    rr["modifiedDetails"] = details


# ── solve functions: EASY ────────────────────────────────────────────

def solve_task_e1(state):
    """Discontinue rx_005 (Pantoprazole) — acid reflux medication."""
    discontinue_rx(state, "rx_005", "No longer needed")


def solve_task_e2(state):
    """Cancel rx_008 (Flonase)."""
    cancel_rx(state, "rx_008")


def solve_task_e3(state):
    """Resume rx_012 (Hydrochlorothiazide) from hold."""
    resume_rx(state, "rx_012")


def solve_task_e4(state):
    """Approve refill rr_001 (Atorvastatin)."""
    approve_rr(state, "rr_001")


def solve_task_e5(state):
    """Deny refill rr_002 (Metformin) — needs lab work."""
    deny_rr(state, "rr_002", "Need lab work before renewal")


def solve_task_e6(state):
    """Switch to David Kowalski."""
    state["currentPatientId"] = "pat_002"


def solve_task_e7(state):
    """Hold rx_007 (Gabapentin)."""
    hold_rx(state, "rx_007", "Reporting dizziness")


def solve_task_e8(state):
    """Renew rx_013 (Sertraline) with 5 refills."""
    renew_rx(state, "rx_013", 5)


def solve_task_e9(state):
    """Remove Prednisone (drug_045) from favorites."""
    favs = state["settings"]["favoritesDrugIds"]
    if "drug_045" in favs:
        favs.remove("drug_045")


def solve_task_e10(state):
    """Disable allergy review requirement."""
    state["settings"]["requireAllergyReview"] = False


def solve_task_e11(state):
    """Set default pharmacy to Walgreens (pharm_002)."""
    state["settings"]["defaultPharmacy"] = "pharm_002"


def solve_task_e12(state):
    """Set print format to compact."""
    state["settings"]["printFormat"] = "compact"


def solve_task_e13(state):
    """Modify rx_002 (Amlodipine) quantity to 90."""
    modify_rx(state, "rx_002", {"quantity": 90})


def solve_task_e14(state):
    """Switch to Aisha Rahman."""
    state["currentPatientId"] = "pat_003"


def solve_task_e15(state):
    """Approve refill rr_010 (Furosemide, urgent)."""
    approve_rr(state, "rr_010")


def solve_task_e16(state):
    """Discontinue rx_013 (Sertraline) — patient request."""
    discontinue_rx(state, "rx_013", "Patient request")


def solve_task_e17(state):
    """Remove Ibuprofen (drug_043) from favorites."""
    favs = state["settings"]["favoritesDrugIds"]
    if "drug_043" in favs:
        favs.remove("drug_043")


def solve_task_e18(state):
    """Disable e-prescribing."""
    state["settings"]["eRxEnabled"] = False


def solve_task_e19(state):
    """Set default days supply to 90."""
    state["settings"]["defaultDaysSupply"] = 90


def solve_task_e20(state):
    """Deny refill rr_011 (Sertraline) — changed therapy."""
    deny_rr(state, "rr_011", "Changed therapy")


# ── solve functions: MEDIUM ──────────────────────────────────────────

def solve_task_m1(state):
    """Prescribe Ciprofloxacin 500mg for Margaret Chen."""
    new_rx(state, "pat_001", "drug_030", "Ciprofloxacin", "Cipro",
           "500mg Tablet", "500mg", "Twice daily", "Oral", 14, 7, 0,
           "Take 1 tablet by mouth twice daily for 7 days", "pharm_001")


def solve_task_m2(state):
    """Switch to William Thornton, renew insulin with 3 refills."""
    state["currentPatientId"] = "pat_004"
    renew_rx(state, "rx_023", 3)


def solve_task_m3(state):
    """Modify rx_001 (Atorvastatin): dosage to 40mg, quantity to 90."""
    modify_rx(state, "rx_001", {"dosage": "40mg", "quantity": 90})


def solve_task_m4(state):
    """Switch to Jessica Morales, hold rx_025 (Cephalexin)."""
    state["currentPatientId"] = "pat_005"
    hold_rx(state, "rx_025", "GI side effects")


def solve_task_m5(state):
    """Set default pharmacy to UCSF (pharm_004), default refills to 3."""
    state["settings"]["defaultPharmacy"] = "pharm_004"
    state["settings"]["defaultRefills"] = 3


def solve_task_m6(state):
    """Deny refill rr_007 (Valsartan) — overdue for follow-up."""
    deny_rr(state, "rr_007", "Need appointment - overdue for follow-up")


def solve_task_m7(state):
    """Modify and approve refill rr_003 (Pantoprazole)."""
    modify_approve_rr(state, "rr_003", "Reducing dose to 20mg per clinical review")


def solve_task_m8(state):
    """Prescribe Fluconazole 150mg single dose for Margaret."""
    new_rx(state, "pat_001", "drug_032", "Fluconazole", "Diflucan",
           "150mg Tablet", "150mg", "Once daily", "Oral", 1, 1, 0,
           "Take 150mg by mouth as a single dose", "pharm_001")


def solve_task_m9(state):
    """Switch to Robert Fitzgerald, modify rx_028 dosage to 25mg."""
    state["currentPatientId"] = "pat_006"
    modify_rx(state, "rx_028", {"dosage": "25mg"})


def solve_task_m10(state):
    """Renew rx_014 (Apixaban/Eliquis) with 5 refills."""
    renew_rx(state, "rx_014", 5)


def solve_task_m11(state):
    """Set print format to detailed, disable auto-check interactions."""
    state["settings"]["printFormat"] = "detailed"
    state["settings"]["autoCheckInteractions"] = False


def solve_task_m12(state):
    """Prescribe Prednisone 20mg for Margaret — 5-day course."""
    new_rx(state, "pat_001", "drug_045", "Prednisone", "Prednisone",
           "20mg Tablet", "20mg", "Once daily", "Oral", 5, 5, 0,
           "Take 1 tablet by mouth once daily for 5 days", "pharm_001")


def solve_task_m13(state):
    """Switch to David Kowalski, approve refill rr_005 (Metoprolol)."""
    state["currentPatientId"] = "pat_002"
    approve_rr(state, "rr_005")


def solve_task_m14(state):
    """Modify rx_007 sig."""
    modify_rx(state, "rx_007", {"sig": "Take 1 capsule by mouth twice daily with food"})


def solve_task_m15(state):
    """Add Escitalopram (drug_034) to favorites."""
    favs = state["settings"]["favoritesDrugIds"]
    if "drug_034" not in favs:
        favs.append("drug_034")


def solve_task_m16(state):
    """Set default pharmacy to Express Scripts (pharm_008), days supply 90."""
    state["settings"]["defaultPharmacy"] = "pharm_008"
    state["settings"]["defaultDaysSupply"] = 90


def solve_task_m17(state):
    """Switch to David Kowalski, prescribe Valacyclovir 500mg."""
    state["currentPatientId"] = "pat_002"
    new_rx(state, "pat_002", "drug_060", "Valacyclovir", "Valtrex",
           "500mg Tablet", "500mg", "Twice daily", "Oral", 20, 10, 0,
           "Take 1 tablet by mouth twice daily for 10 days", "pharm_003")


def solve_task_m18(state):
    """Modify rx_003 (Metformin) frequency to Once daily."""
    modify_rx(state, "rx_003", {"frequency": "Once daily"})


def solve_task_m19(state):
    """Remove Amoxicillin (drug_025) and Azithromycin (drug_028) from favorites."""
    favs = state["settings"]["favoritesDrugIds"]
    if "drug_025" in favs:
        favs.remove("drug_025")
    if "drug_028" in favs:
        favs.remove("drug_028")


def solve_task_m20(state):
    """Hold rx_030 (Ozempic/Semaglutide)."""
    hold_rx(state, "rx_030", "Prior auth needs renewal")


# ── solve functions: HARD ────────────────────────────────────────────

def solve_task_h1(state):
    """Discontinue Eliquis (rx_014), prescribe Warfarin 5mg with DAW."""
    discontinue_rx(state, "rx_014", "Switching to Warfarin")
    new_rx(state, "pat_001", "drug_011", "Warfarin", "Coumadin",
           "5mg Tablet", "5mg", "Once daily", "Oral", 30, 30, 0,
           "Take 1 tablet by mouth once daily", "pharm_001", daw=True)


def solve_task_h2(state):
    """Start Robert Fitzgerald on Ozempic 0.5mg with prior auth."""
    state["currentPatientId"] = "pat_006"
    new_rx(state, "pat_006", "drug_049", "Semaglutide", "Ozempic",
           "0.5mg/0.5mL Solution for Injection", "0.5mg", "Once weekly",
           "Subcutaneous", 1, 28, 2,
           "Inject 0.5mg subcutaneously once weekly", "pharm_010",
           prior_auth=True, prior_auth_number="PA-2026-55555")


def solve_task_h3(state):
    """William Thornton: approve Furosemide refill, deny Valsartan refill, increase insulin to 30."""
    state["currentPatientId"] = "pat_004"
    approve_rr(state, "rr_010")
    deny_rr(state, "rr_007", "Need appointment - overdue for follow-up")
    modify_rx(state, "rx_023", {"dosage": "30 units"})


def solve_task_h4(state):
    """Prescribe Amoxicillin + Prednisone for Aisha Rahman."""
    state["currentPatientId"] = "pat_003"
    new_rx(state, "pat_003", "drug_025", "Amoxicillin", "Amoxil",
           "500mg Capsule", "500mg", "Three times daily", "Oral", 30, 10, 0,
           "Take 1 capsule by mouth three times daily for 10 days", "pharm_002")
    new_rx(state, "pat_003", "drug_045", "Prednisone", "Prednisone",
           "20mg Tablet", "20mg", "Once daily", "Oral", 5, 5, 0,
           "Take 1 tablet by mouth once daily for 5 days", "pharm_002")


def solve_task_h5(state):
    """Discontinue Pantoprazole 40mg, prescribe Pantoprazole 20mg."""
    discontinue_rx(state, "rx_005", "Stepping down dose")
    new_rx(state, "pat_001", "drug_019", "Pantoprazole", "Protonix",
           "20mg Tablet, Delayed Release", "20mg", "Once daily", "Oral", 30, 30, 2,
           "Take 1 tablet by mouth once daily before breakfast", "pharm_001")


def solve_task_h6(state):
    """Switch to Jessica Morales, discontinue Cephalexin, renew Fluoxetine."""
    state["currentPatientId"] = "pat_005"
    discontinue_rx(state, "rx_025", "Cellulitis resolved")
    renew_rx(state, "rx_026", 5)


def solve_task_h7(state):
    """Multiple settings: Capsule Pharmacy, 90 days, 3 refills, no sig, compact."""
    state["settings"]["defaultPharmacy"] = "pharm_009"
    state["settings"]["defaultDaysSupply"] = 90
    state["settings"]["defaultRefills"] = 3
    state["settings"]["signatureRequired"] = False
    state["settings"]["printFormat"] = "compact"


def solve_task_h8(state):
    """Process Margaret's pending refills: approve Atorvastatin, deny Metformin, deny Sertraline."""
    approve_rr(state, "rr_001")
    deny_rr(state, "rr_002", "Need lab work before renewal")
    deny_rr(state, "rr_011", "Changed therapy")


def solve_task_h9(state):
    """Discontinue Gabapentin, prescribe Pregabalin 75mg."""
    discontinue_rx(state, "rx_007", "Transitioning to Pregabalin")
    new_rx(state, "pat_001", "drug_037", "Pregabalin", "Lyrica",
           "75mg Capsule", "75mg", "Twice daily", "Oral", 60, 30, 1,
           "Take 1 capsule by mouth twice daily", "pharm_001")


def solve_task_h10(state):
    """Switch to Robert Fitzgerald (Metformin allergy), prescribe Sitagliptin."""
    state["currentPatientId"] = "pat_006"
    new_rx(state, "pat_006", "drug_015", "Sitagliptin", "Januvia",
           "100mg Tablet", "100mg", "Once daily", "Oral", 30, 30, 5,
           "Take 1 tablet by mouth once daily", "pharm_004")


def solve_task_h11(state):
    """Renew all active Margaret prescriptions with < 3 refills remaining."""
    renew_rx(state, "rx_001", 5)
    renew_rx(state, "rx_005", 5)
    renew_rx(state, "rx_006", 5)
    renew_rx(state, "rx_008", 5)


def solve_task_h12(state):
    """Prescribe Amlodipine for Aisha Rahman, discontinue Cephalexin for Jessica Morales."""
    state["currentPatientId"] = "pat_003"
    new_rx(state, "pat_003", "drug_005", "Amlodipine", "Norvasc",
           "5mg Tablet", "5mg", "Once daily", "Oral", 30, 30, 5,
           "Take 1 tablet by mouth once daily", "pharm_002")
    state["currentPatientId"] = "pat_005"
    discontinue_rx(state, "rx_025", "Cellulitis resolved")


def solve_task_h13(state):
    """Settings: Costco, 90 days, 3 refills, no allergy review. Prescribe Omeprazole."""
    state["settings"]["defaultPharmacy"] = "pharm_006"
    state["settings"]["defaultDaysSupply"] = 90
    state["settings"]["defaultRefills"] = 3
    state["settings"]["requireAllergyReview"] = False
    new_rx(state, "pat_001", "drug_021", "Omeprazole", "Prilosec",
           "20mg Capsule, Delayed Release", "20mg", "Once daily", "Oral", 30, 30, 2,
           "Take 1 capsule by mouth once daily before breakfast", "pharm_006")


def solve_task_h14(state):
    """Deny Metformin refill, discontinue Metformin, prescribe Metformin ER 500mg."""
    deny_rr(state, "rr_002", "Need lab work before renewal")
    discontinue_rx(state, "rx_003", "Switching to extended release formulation")
    new_rx(state, "pat_001", "drug_014", "Metformin", "Glucophage",
           "500mg Tablet, Extended Release", "500mg", "Once daily", "Oral", 30, 30, 5,
           "Take 1 tablet by mouth once daily with dinner", "pharm_001")


def solve_task_h15(state):
    """Margaret's two prior-auth rxs: hold specialty (Semaglutide), renew other (Apixaban) with 3."""
    hold_rx(state, "rx_030", "Prior auth review")
    renew_rx(state, "rx_014", 3)


def solve_task_h16(state):
    """Robert: hold both cardiologist-prescribed meds (Carvedilol, Spironolactone)."""
    state["currentPatientId"] = "pat_006"
    hold_rx(state, "rx_028", "Admitted for cardiac monitoring")
    hold_rx(state, "rx_029", "Admitted for cardiac monitoring")


def solve_task_h17(state):
    """All pending refills: approve urgent, deny routine."""
    approve_rr(state, "rr_003")
    approve_rr(state, "rr_010")
    deny_rr(state, "rr_001", "Need appointment - overdue for follow-up")
    deny_rr(state, "rr_002", "Need appointment - overdue for follow-up")
    deny_rr(state, "rr_005", "Need appointment - overdue for follow-up")
    deny_rr(state, "rr_007", "Need appointment - overdue for follow-up")
    deny_rr(state, "rr_011", "Need appointment - overdue for follow-up")


def solve_task_h18(state):
    """Nov 2025 rxs: discontinue PCP's (Pantoprazole), double cardiologist's (Apixaban) qty."""
    discontinue_rx(state, "rx_005", "Referred to GI specialist")
    modify_rx(state, "rx_014", {"quantity": 120})


def solve_task_h19(state):
    """Renew Margaret's rxs: 1 remaining -> 5 refills, 2 remaining -> 3 refills."""
    # 1 remaining: rx_005 Pantoprazole
    renew_rx(state, "rx_005", 5)
    # 2 remaining: rx_001 Atorvastatin, rx_006 Albuterol, rx_008 Flonase
    renew_rx(state, "rx_001", 3)
    renew_rx(state, "rx_006", 3)
    renew_rx(state, "rx_008", 3)


def solve_task_h20(state):
    """4-patient SSRI: renew David's 5, increase Aisha's 10mg, discontinue Margaret's, increase Jessica's 40mg."""
    renew_rx(state, "rx_018", 5)
    modify_rx(state, "rx_021", {"dosage": "10mg"})
    discontinue_rx(state, "rx_013", "Switching to SNRI")
    modify_rx(state, "rx_026", {"dosage": "40mg"})


# ── solve functions: HARD (hardening round 1) ──────────────────────

def solve_task_h21(state):
    """ACE-allergy patient: Valsartan 320mg + renew 5."""
    state["currentPatientId"] = "pat_004"
    modify_rx(state, "rx_022", {"dosage": "320mg"})
    renew_rx(state, "rx_022", 5)


def solve_task_h22(state):
    """Find DAW rx (Levothyroxine) and increase to 88mcg."""
    modify_rx(state, "rx_004", {"dosage": "88mcg"})


def solve_task_h23(state):
    """Two Atorvastatin patients: renew lower-dose 5, qty higher-dose 90."""
    renew_rx(state, "rx_001", 5)
    modify_rx(state, "rx_017", {"quantity": 90})


def solve_task_h24(state):
    """Settings for mail-order + prescribe Montelukast."""
    state["settings"]["defaultPharmacy"] = "pharm_007"
    state["settings"]["defaultDaysSupply"] = 90
    state["settings"]["defaultRefills"] = 3
    new_rx(state, "pat_001", "drug_051", "Montelukast", "Singulair",
           "10mg Tablet", "10mg", "Once daily", "Oral", 90, 90, 3,
           "Take 1 tablet by mouth once daily in the evening", "pharm_007")


def solve_task_h25(state):
    """David: deny Metoprolol refill, discontinue, prescribe Carvedilol."""
    state["currentPatientId"] = "pat_002"
    deny_rr(state, "rr_005", "Medication change - switching to Carvedilol")
    discontinue_rx(state, "rx_016", "Inadequate heart rate control, switching to Carvedilol")
    new_rx(state, "pat_002", "drug_057", "Carvedilol", "Coreg",
           "12.5mg Tablet", "12.5mg", "Twice daily", "Oral", 60, 30, 3,
           "Take 1 tablet by mouth twice daily with food", "pharm_003")


def solve_task_h26(state):
    """Find Dr. Reyes's rx (Gabapentin) and increase to 400mg."""
    modify_rx(state, "rx_007", {"dosage": "400mg"})


def solve_task_h27(state):
    """Jessica renew Fluoxetine 6, Robert hold Empagliflozin."""
    state["currentPatientId"] = "pat_005"
    renew_rx(state, "rx_026", 6)
    state["currentPatientId"] = "pat_006"
    hold_rx(state, "rx_027", "Kidney function decline")


def solve_task_h28(state):
    """Differentiated refill processing: approve urgent, modify Metformin, deny Sertraline, leave Atorvastatin."""
    approve_rr(state, "rr_003")
    modify_approve_rr(state, "rr_002", "Reduce to 500mg BID per GI tolerance")
    deny_rr(state, "rr_011", "Changed therapy")
    # rr_001 left pending — no action


def solve_task_h29(state):
    """Hold Family Med rx (Levothyroxine/Okafor), renew Cardiology rx (Apixaban/Tanaka) 6."""
    hold_rx(state, "rx_004", "Provider on leave")
    renew_rx(state, "rx_014", 6)


def solve_task_h30(state):
    """Cross-patient antibiotics: Cipro for Margaret, Amoxicillin for Aisha."""
    new_rx(state, "pat_001", "drug_030", "Ciprofloxacin", "Cipro",
           "500mg Tablet", "500mg", "Twice daily", "Oral", 14, 7, 0,
           "Take 1 tablet by mouth twice daily for 7 days", "pharm_001")
    state["currentPatientId"] = "pat_003"
    new_rx(state, "pat_003", "drug_025", "Amoxicillin", "Amoxil",
           "500mg Capsule", "500mg", "Three times daily", "Oral", 30, 10, 0,
           "Take 1 capsule by mouth three times daily for 10 days", "pharm_002")


def solve_task_h31(state):
    """Favorites cleanup + prescribe Duloxetine 60mg."""
    favs = state["settings"]["favoritesDrugIds"]
    if "drug_043" in favs:
        favs.remove("drug_043")
    if "drug_045" in favs:
        favs.remove("drug_045")
    if "drug_036" not in favs:
        favs.append("drug_036")
    if "drug_035" not in favs:
        favs.append("drug_035")
    new_rx(state, "pat_001", "drug_035", "Duloxetine", "Cymbalta",
           "60mg Capsule, Delayed Release", "60mg", "Once daily", "Oral", 30, 30, 3,
           "Take 1 capsule by mouth once daily", "pharm_001")


def solve_task_h32(state):
    """Two Metformin patients: Margaret 1500mg, David renew 5."""
    modify_rx(state, "rx_003", {"dosage": "1500mg"})
    state["currentPatientId"] = "pat_002"
    renew_rx(state, "rx_019", 5)


def solve_task_h33(state):
    """Resume HCTZ + 50mg, renew Albuterol 4, discontinue Flonase."""
    resume_rx(state, "rx_012")
    modify_rx(state, "rx_012", {"dosage": "50mg"})
    renew_rx(state, "rx_006", 4)
    discontinue_rx(state, "rx_008", "Allergy season over")


def solve_task_h34(state):
    """Interaction-aware macrolide: prescribe Azithromycin (safe choice)."""
    new_rx(state, "pat_001", "drug_028", "Azithromycin", "Zithromax",
           "250mg Tablet", "250mg", "Once daily", "Oral", 6, 5, 0,
           "Take 500mg on day 1, then 250mg once daily for 4 days", "pharm_001")


def solve_task_h35(state):
    """History discovery: increase Amlodipine (CCB) to 10mg."""
    modify_rx(state, "rx_002", {"dosage": "10mg"})


def solve_task_h36(state):
    """Robert: renew Carvedilol 6, Spironolactone 50mg, Empagliflozin 25mg."""
    state["currentPatientId"] = "pat_006"
    renew_rx(state, "rx_028", 6)
    modify_rx(state, "rx_029", {"dosage": "50mg"})
    modify_rx(state, "rx_027", {"dosage": "25mg"})


def solve_task_h37(state):
    """All prior-auth rxs across patients: renew each with 5."""
    renew_rx(state, "rx_014", 5)
    renew_rx(state, "rx_023", 5)
    renew_rx(state, "rx_027", 5)
    renew_rx(state, "rx_030", 5)


def solve_task_h38(state):
    """William: prescribe Amlodipine + hold Insulin."""
    state["currentPatientId"] = "pat_004"
    new_rx(state, "pat_004", "drug_005", "Amlodipine", "Norvasc",
           "5mg Tablet", "5mg", "Once daily", "Oral", 30, 30, 5,
           "Take 1 tablet by mouth once daily", "pharm_005")
    hold_rx(state, "rx_023", "Hypoglycemic episodes")


def solve_task_h39(state):
    """Settings + David Atorvastatin 80mg + switch back to Margaret."""
    state["settings"]["signatureRequired"] = False
    state["settings"]["printFormat"] = "detailed"
    state["currentPatientId"] = "pat_002"
    modify_rx(state, "rx_017", {"dosage": "80mg"})
    state["currentPatientId"] = "pat_001"


def solve_task_h40(state):
    """End-of-day: approve William refill, deny David refill, hold Semaglutide, renew Sertraline 6."""
    approve_rr(state, "rr_010")
    deny_rr(state, "rr_005", "Need appointment - overdue for follow-up")
    hold_rx(state, "rx_030", "Prior auth needs resubmission")
    renew_rx(state, "rx_013", 6)


SOLVERS = {
    "task_e1": solve_task_e1, "task_e2": solve_task_e2, "task_e3": solve_task_e3,
    "task_e4": solve_task_e4, "task_e5": solve_task_e5, "task_e6": solve_task_e6,
    "task_e7": solve_task_e7, "task_e8": solve_task_e8, "task_e9": solve_task_e9,
    "task_e10": solve_task_e10, "task_e11": solve_task_e11, "task_e12": solve_task_e12,
    "task_e13": solve_task_e13, "task_e14": solve_task_e14, "task_e15": solve_task_e15,
    "task_e16": solve_task_e16, "task_e17": solve_task_e17, "task_e18": solve_task_e18,
    "task_e19": solve_task_e19, "task_e20": solve_task_e20,
    "task_m1": solve_task_m1, "task_m2": solve_task_m2, "task_m3": solve_task_m3,
    "task_m4": solve_task_m4, "task_m5": solve_task_m5, "task_m6": solve_task_m6,
    "task_m7": solve_task_m7, "task_m8": solve_task_m8, "task_m9": solve_task_m9,
    "task_m10": solve_task_m10, "task_m11": solve_task_m11, "task_m12": solve_task_m12,
    "task_m13": solve_task_m13, "task_m14": solve_task_m14, "task_m15": solve_task_m15,
    "task_m16": solve_task_m16, "task_m17": solve_task_m17, "task_m18": solve_task_m18,
    "task_m19": solve_task_m19, "task_m20": solve_task_m20,
    "task_h1": solve_task_h1, "task_h2": solve_task_h2, "task_h3": solve_task_h3,
    "task_h4": solve_task_h4, "task_h5": solve_task_h5, "task_h6": solve_task_h6,
    "task_h7": solve_task_h7, "task_h8": solve_task_h8, "task_h9": solve_task_h9,
    "task_h10": solve_task_h10, "task_h11": solve_task_h11, "task_h12": solve_task_h12,
    "task_h13": solve_task_h13, "task_h14": solve_task_h14, "task_h15": solve_task_h15,
    "task_h16": solve_task_h16, "task_h17": solve_task_h17, "task_h18": solve_task_h18,
    "task_h19": solve_task_h19, "task_h20": solve_task_h20,
    "task_h21": solve_task_h21, "task_h22": solve_task_h22, "task_h23": solve_task_h23,
    "task_h24": solve_task_h24, "task_h25": solve_task_h25, "task_h26": solve_task_h26,
    "task_h27": solve_task_h27, "task_h28": solve_task_h28, "task_h29": solve_task_h29,
    "task_h30": solve_task_h30, "task_h31": solve_task_h31, "task_h32": solve_task_h32,
    "task_h33": solve_task_h33, "task_h34": solve_task_h34, "task_h35": solve_task_h35,
    "task_h36": solve_task_h36, "task_h37": solve_task_h37, "task_h38": solve_task_h38,
    "task_h39": solve_task_h39, "task_h40": solve_task_h40,
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


def find_free_port(start=9600):
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
    """Load task definitions from real-tasks.json."""
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
    parser = argparse.ArgumentParser(description="Elation Prescriptions real-task sanity check")
    parser.add_argument("--task-id", type=str, help="Run a single task by ID")
    parser.add_argument("--workers", type=int, default=1, help="Number of parallel workers")
    parser.add_argument("--port", type=int, default=9600, help="Base port for servers")
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
