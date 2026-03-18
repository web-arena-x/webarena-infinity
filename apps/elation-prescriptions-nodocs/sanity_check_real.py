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
    """Switch to David Kowalski, reduce Escitalopram to 5mg, change Metformin ER to twice daily."""
    state["currentPatientId"] = "pat_002"
    modify_rx(state, "rx_018", {"dosage": "5mg"})
    modify_rx(state, "rx_019", {"frequency": "Twice daily"})


def solve_task_h9(state):
    """Prescribe Cyclobenzaprine 10mg, increase Gabapentin dosage to 400mg."""
    new_rx(state, "pat_001", "drug_052", "Cyclobenzaprine", "Flexeril",
           "10mg Tablet", "10mg", "Three times daily", "Oral", 30, 10, 0,
           "Take 1 tablet by mouth three times daily as needed for muscle spasm",
           "pharm_001")
    modify_rx(state, "rx_007", {"dosage": "400mg"})


def solve_task_h10(state):
    """Process Margaret's pending refills: approve Atorvastatin, deny Metformin, deny Sertraline."""
    approve_rr(state, "rr_001")
    deny_rr(state, "rr_002", "Need lab work before renewal")
    deny_rr(state, "rr_011", "Changed therapy")


def solve_task_h11(state):
    """Start Robert Fitzgerald on Dulaglutide, increase Carvedilol to 25mg."""
    state["currentPatientId"] = "pat_006"
    new_rx(state, "pat_006", "drug_050", "Dulaglutide", "Trulicity",
           "0.75mg/0.5mL Solution for Injection", "0.75mg", "Once weekly",
           "Subcutaneous", 4, 28, 2,
           "Inject 0.75mg subcutaneously once weekly", "pharm_004")
    modify_rx(state, "rx_028", {"dosage": "25mg"})


def solve_task_h12(state):
    """Settings: brand first, Alto Pharmacy, remove Pantoprazole + Atorvastatin from favorites."""
    state["settings"]["showGenericFirst"] = False
    state["settings"]["defaultPharmacy"] = "pharm_007"
    favs = state["settings"]["favoritesDrugIds"]
    if "drug_019" in favs:
        favs.remove("drug_019")
    if "drug_001" in favs:
        favs.remove("drug_001")


def solve_task_h13(state):
    """Switch to David Kowalski, prescribe Methylprednisolone dose pack, hold Escitalopram."""
    state["currentPatientId"] = "pat_002"
    new_rx(state, "pat_002", "drug_046", "Methylprednisolone", "Medrol Dosepak",
           "4mg Tablet (21-tablet dose pack)", "4mg", "Once daily", "Oral", 1, 7, 0,
           "Take as directed per dose pack instructions", "pharm_003")
    hold_rx(state, "rx_018", "On steroid therapy")


def solve_task_h14(state):
    """Discontinue Gabapentin, prescribe Pregabalin 75mg."""
    discontinue_rx(state, "rx_007", "Transitioning to Pregabalin")
    new_rx(state, "pat_001", "drug_037", "Pregabalin", "Lyrica",
           "75mg Capsule", "75mg", "Twice daily", "Oral", 60, 30, 1,
           "Take 1 capsule by mouth twice daily", "pharm_001")


def solve_task_h15(state):
    """Switch to William Thornton, renew Valsartan with 5, Insulin with 3 refills."""
    state["currentPatientId"] = "pat_004"
    renew_rx(state, "rx_022", 5)
    renew_rx(state, "rx_023", 3)


def solve_task_h16(state):
    """Switch to Aisha Rahman, prescribe Fluticasone nasal + Montelukast."""
    state["currentPatientId"] = "pat_003"
    new_rx(state, "pat_003", "drug_047", "Fluticasone Propionate Nasal", "Flonase",
           "50mcg/spray Nasal Spray", "50mcg", "Once daily", "Intranasal", 1, 30, 2,
           "Spray 2 sprays in each nostril once daily", "pharm_002")
    new_rx(state, "pat_003", "drug_051", "Montelukast", "Singulair",
           "10mg Tablet", "10mg", "Once daily", "Oral", 30, 30, 5,
           "Take 1 tablet by mouth once daily in the evening", "pharm_002")


def solve_task_h17(state):
    """Modify-approve Pantoprazole refill, discontinue Pantoprazole rx."""
    modify_approve_rr(state, "rr_003", "Stepped down to 20mg per protocol")
    discontinue_rx(state, "rx_005", "Stepped down to 20mg")


def solve_task_h18(state):
    """Switch to David Kowalski, prescribe Advair 250/50, approve Metoprolol refill."""
    state["currentPatientId"] = "pat_002"
    new_rx(state, "pat_002", "drug_023", "Fluticasone/Salmeterol", "Advair Diskus",
           "250/50mcg Dry Powder Inhaler", "250/50mcg", "Twice daily", "Inhalation", 1, 30, 2,
           "Inhale 1 puff twice daily, rinse mouth after use", "pharm_003")
    approve_rr(state, "rr_005")


def solve_task_h19(state):
    """Switch to Robert Fitzgerald, increase Spironolactone to 50mg, Carvedilol qty to 90, prescribe Furosemide 20mg."""
    state["currentPatientId"] = "pat_006"
    modify_rx(state, "rx_029", {"dosage": "50mg"})
    modify_rx(state, "rx_028", {"quantity": 90})
    new_rx(state, "pat_006", "drug_009", "Furosemide", "Lasix",
           "20mg Tablet", "20mg", "Once daily", "Oral", 30, 30, 5,
           "Take 1 tablet by mouth once daily in the morning", "pharm_004")


def solve_task_h20(state):
    """Cancel Albuterol, hold Flonase, renew Atorvastatin with 3 refills."""
    cancel_rx(state, "rx_006")
    hold_rx(state, "rx_008", "Pending seasonal review")
    renew_rx(state, "rx_001", 3)


# ── solve functions: HARDENING ROUND 1 ─────────────────────────────

def solve_task_h21(state):
    """Modify Levothyroxine dosage to 88mcg and update sig."""
    modify_rx(state, "rx_004", {
        "dosage": "88mcg",
        "sig": "Take 1 tablet by mouth once daily on an empty stomach, 60 minutes before breakfast"
    })


def solve_task_h22(state):
    """Switch to Robert Fitzgerald (Metformin allergy), prescribe Sitagliptin."""
    state["currentPatientId"] = "pat_006"
    new_rx(state, "pat_006", "drug_015", "Sitagliptin", "Januvia",
           "100mg Tablet", "100mg", "Once daily", "Oral", 30, 30, 5,
           "Take 1 tablet by mouth once daily", "pharm_004")


def solve_task_h23(state):
    """Renew cardiologist's rx (Apixaban) with 3, increase Amlodipine to 10mg."""
    renew_rx(state, "rx_014", 3)
    modify_rx(state, "rx_002", {"dosage": "10mg"})


def solve_task_h24(state):
    """Renew all active Margaret prescriptions with < 3 refills remaining."""
    renew_rx(state, "rx_001", 5)
    renew_rx(state, "rx_005", 5)
    renew_rx(state, "rx_006", 5)
    renew_rx(state, "rx_008", 5)


def solve_task_h25(state):
    """Increase David's Escitalopram to 20mg, Aisha's to 10mg."""
    modify_rx(state, "rx_018", {"dosage": "20mg"})
    modify_rx(state, "rx_021", {"dosage": "10mg"})


def solve_task_h26(state):
    """Settings: Safeway pharmacy, 5 refills, no sig required. Remove Sertraline + Levothyroxine from favorites."""
    state["settings"]["defaultPharmacy"] = "pharm_012"
    state["settings"]["defaultRefills"] = 5
    state["settings"]["signatureRequired"] = False
    favs = state["settings"]["favoritesDrugIds"]
    if "drug_033" in favs:
        favs.remove("drug_033")
    if "drug_018" in favs:
        favs.remove("drug_018")


def solve_task_h27(state):
    """Resume on-hold diuretic (HCTZ), modify-approve urgent Pantoprazole refill."""
    resume_rx(state, "rx_012")
    modify_approve_rr(state, "rr_003", "Dose verified, approved per protocol")


def solve_task_h28(state):
    """Switch to William Thornton, prescribe Rosuvastatin, approve Furosemide refill."""
    state["currentPatientId"] = "pat_004"
    new_rx(state, "pat_004", "drug_003", "Rosuvastatin", "Crestor",
           "10mg Tablet", "10mg", "Once daily", "Oral", 90, 90, 3,
           "Take 1 tablet by mouth once daily at bedtime", "pharm_005")
    approve_rr(state, "rr_010")


def solve_task_h29(state):
    """Prescribe Azithromycin 250mg for Margaret (avoiding Clarithromycin interaction)."""
    new_rx(state, "pat_001", "drug_028", "Azithromycin", "Zithromax",
           "250mg Tablet", "250mg", "Once daily", "Oral", 6, 5, 0,
           "Take 2 tablets on day 1, then 1 tablet once daily for 4 days", "pharm_001")


def solve_task_h30(state):
    """Prescribe Amlodipine for Aisha Rahman, discontinue Cephalexin for Jessica Morales."""
    state["currentPatientId"] = "pat_003"
    new_rx(state, "pat_003", "drug_005", "Amlodipine", "Norvasc",
           "5mg Tablet", "5mg", "Once daily", "Oral", 30, 30, 5,
           "Take 1 tablet by mouth once daily", "pharm_002")
    state["currentPatientId"] = "pat_005"
    discontinue_rx(state, "rx_025", "Cellulitis resolved")


def solve_task_h31(state):
    """William Thornton: increase insulin dosage to 30 units, renew with 5, increase Furosemide qty to 60."""
    state["currentPatientId"] = "pat_004"
    modify_rx(state, "rx_023", {"dosage": "30 units"})
    renew_rx(state, "rx_023", 5)
    modify_rx(state, "rx_024", {"quantity": 60})


def solve_task_h32(state):
    """3-patient SSRI management: Aisha 10mg, David on-hold, Margaret twice daily."""
    modify_rx(state, "rx_021", {"dosage": "10mg"})
    hold_rx(state, "rx_018", "Patient wants to try discontinuing")
    modify_rx(state, "rx_013", {"frequency": "Twice daily"})


def solve_task_h33(state):
    """Remove NSAID + corticosteroid from favorites, add Clopidogrel + Rosuvastatin, print compact."""
    favs = state["settings"]["favoritesDrugIds"]
    if "drug_043" in favs:
        favs.remove("drug_043")
    if "drug_045" in favs:
        favs.remove("drug_045")
    if "drug_048" not in favs:
        favs.append("drug_048")
    if "drug_003" not in favs:
        favs.append("drug_003")
    state["settings"]["printFormat"] = "compact"


def solve_task_h34(state):
    """Switch to David Kowalski, prescribe Apixaban with DAW and prior auth."""
    state["currentPatientId"] = "pat_002"
    new_rx(state, "pat_002", "drug_012", "Apixaban", "Eliquis",
           "5mg Tablet", "5mg", "Twice daily", "Oral", 60, 30, 5,
           "Take 1 tablet by mouth twice daily", "pharm_003",
           daw=True, prior_auth=True, prior_auth_number="PA-2026-DK-001")


def solve_task_h35(state):
    """Hold Flonase, reduce Metformin to 500mg, approve Atorvastatin refill."""
    hold_rx(state, "rx_008", "Seasonal review")
    modify_rx(state, "rx_003", {"dosage": "500mg"})
    approve_rr(state, "rr_001")


def solve_task_h36(state):
    """Switch to William Thornton (ACE allergy patient), prescribe Amlodipine 10mg."""
    state["currentPatientId"] = "pat_004"
    new_rx(state, "pat_004", "drug_005", "Amlodipine", "Norvasc",
           "10mg Tablet", "10mg", "Once daily", "Oral", 30, 30, 5,
           "Take 1 tablet by mouth once daily", "pharm_005")


def solve_task_h37(state):
    """Settings: Costco, 90 days, 3 refills, no allergy review. Prescribe Omeprazole."""
    state["settings"]["defaultPharmacy"] = "pharm_006"
    state["settings"]["defaultDaysSupply"] = 90
    state["settings"]["defaultRefills"] = 3
    state["settings"]["requireAllergyReview"] = False
    new_rx(state, "pat_001", "drug_021", "Omeprazole", "Prilosec",
           "20mg Capsule, Delayed Release", "20mg", "Once daily", "Oral", 30, 30, 2,
           "Take 1 capsule by mouth once daily before breakfast", "pharm_006")


def solve_task_h38(state):
    """Deny Metformin refill, discontinue Metformin, prescribe Metformin ER 500mg."""
    deny_rr(state, "rr_002", "Need lab work before renewal")
    discontinue_rx(state, "rx_003", "Switching to extended release formulation")
    new_rx(state, "pat_001", "drug_014", "Metformin", "Glucophage",
           "500mg Tablet, Extended Release", "500mg", "Once daily", "Oral", 30, 30, 5,
           "Take 1 tablet by mouth once daily with dinner", "pharm_001")


def solve_task_h39(state):
    """Switch to Robert Fitzgerald: increase Jardiance to 25mg, renew Carvedilol with 5, increase Spironolactone qty."""
    state["currentPatientId"] = "pat_006"
    modify_rx(state, "rx_027", {"dosage": "25mg"})
    renew_rx(state, "rx_028", 5)
    modify_rx(state, "rx_029", {"quantity": 60})


def solve_task_h40(state):
    """Increase Apixaban (blood thinner with PA) quantity to 90, deny Sertraline refill."""
    modify_rx(state, "rx_014", {"quantity": 90})
    deny_rr(state, "rr_011", "Changed therapy")


# ── solve functions: HARDENING ROUND 2 ─────────────────────────────

def solve_task_h41(state):
    """NSAID allergy patient (David): beta blocker 100mg, statin qty 90."""
    state["currentPatientId"] = "pat_002"
    modify_rx(state, "rx_016", {"dosage": "100mg"})
    modify_rx(state, "rx_017", {"quantity": 90})


def solve_task_h42(state):
    """Margaret's two prior-auth rxs: hold specialty (Semaglutide), renew other (Apixaban) with 3."""
    hold_rx(state, "rx_030", "Prior auth review")
    renew_rx(state, "rx_014", 3)


def solve_task_h43(state):
    """Process Margaret's pending refills: approve urgent (rr_003), deny routine (rr_001, rr_002, rr_011)."""
    approve_rr(state, "rr_003")
    deny_rr(state, "rr_001", "Need appointment - overdue for follow-up")
    deny_rr(state, "rr_002", "Need appointment - overdue for follow-up")
    deny_rr(state, "rr_011", "Need appointment - overdue for follow-up")


def solve_task_h44(state):
    """William: approve urgent refill (rr_010), modify-approve routine (rr_007)."""
    state["currentPatientId"] = "pat_004"
    approve_rr(state, "rr_010")
    modify_approve_rr(state, "rr_007", "Dose increase to 320mg per cardiology")


def solve_task_h45(state):
    """NKDA patient (Aisha): Escitalopram dosage to 10mg, quantity to 60."""
    state["currentPatientId"] = "pat_003"
    modify_rx(state, "rx_021", {"dosage": "10mg", "quantity": 60})


def solve_task_h46(state):
    """Margaret's DAW rx (Levothyroxine): quantity 90, days supply 90."""
    modify_rx(state, "rx_004", {"quantity": 90, "daysSupply": 90})


def solve_task_h47(state):
    """Erythromycin allergy patient (Jessica): discontinue antibiotic, increase SSRI to 40mg."""
    state["currentPatientId"] = "pat_005"
    discontinue_rx(state, "rx_025", "Course completed")
    modify_rx(state, "rx_026", {"dosage": "40mg"})


def solve_task_h48(state):
    """Robert: hold both cardiologist-prescribed meds (Carvedilol, Spironolactone)."""
    state["currentPatientId"] = "pat_006"
    hold_rx(state, "rx_028", "Admitted for cardiac monitoring")
    hold_rx(state, "rx_029", "Admitted for cardiac monitoring")


def solve_task_h49(state):
    """Discontinue Dr. Reyes's rx (Gabapentin), renew Dr. Okafor's (Levothyroxine) with 11."""
    discontinue_rx(state, "rx_007", "Adverse effects")
    renew_rx(state, "rx_004", 11)


def solve_task_h50(state):
    """Remove antibiotics from favorites, add Duloxetine+Pregabalin, Amazon Pharmacy, disable eRx."""
    favs = state["settings"]["favoritesDrugIds"]
    if "drug_025" in favs:
        favs.remove("drug_025")
    if "drug_028" in favs:
        favs.remove("drug_028")
    if "drug_035" not in favs:
        favs.append("drug_035")
    if "drug_037" not in favs:
        favs.append("drug_037")
    state["settings"]["defaultPharmacy"] = "pharm_013"
    state["settings"]["eRxEnabled"] = False


def solve_task_h51(state):
    """David's Metoprolol to twice daily, William's Valsartan qty to 60."""
    modify_rx(state, "rx_016", {"frequency": "Twice daily"})
    modify_rx(state, "rx_022", {"quantity": 60})


def solve_task_h52(state):
    """Margaret: resume HCTZ, cancel Albuterol, Metformin to once daily qty 30."""
    resume_rx(state, "rx_012")
    cancel_rx(state, "rx_006")
    modify_rx(state, "rx_003", {"frequency": "Once daily", "quantity": 30})


def solve_task_h53(state):
    """Two Atorvastatin patients: renew lower-dose (Margaret 20mg) with 5, higher-dose (David 40mg) qty 90."""
    renew_rx(state, "rx_001", 5)
    modify_rx(state, "rx_017", {"quantity": 90})


def solve_task_h54(state):
    """Robert: diabetes med (Empagliflozin) 25mg, beta blocker (Carvedilol) once daily, diuretic (Spironolactone) qty 60."""
    state["currentPatientId"] = "pat_006"
    modify_rx(state, "rx_027", {"dosage": "25mg"})
    modify_rx(state, "rx_028", {"frequency": "Once daily"})
    modify_rx(state, "rx_029", {"quantity": 60})


def solve_task_h55(state):
    """Hold Gabapentin + nasal spray, approve Atorvastatin refill."""
    hold_rx(state, "rx_007", "Placed on hold")
    hold_rx(state, "rx_008", "Placed on hold")
    approve_rr(state, "rr_001")


def solve_task_h56(state):
    """Settings: brand first, 5 refills, no sig. Switch to Jessica, renew Fluoxetine with 5."""
    state["settings"]["showGenericFirst"] = False
    state["settings"]["defaultRefills"] = 5
    state["settings"]["signatureRequired"] = False
    state["currentPatientId"] = "pat_005"
    renew_rx(state, "rx_026", 5)


def solve_task_h57(state):
    """Margaret: SSRI (Sertraline) freq twice daily, blood thinner (Apixaban) qty 90, deny Sertraline refill."""
    modify_rx(state, "rx_013", {"frequency": "Twice daily"})
    modify_rx(state, "rx_014", {"quantity": 90})
    deny_rr(state, "rr_011", "Changed therapy")


def solve_task_h58(state):
    """Latex allergy patient (William): renew Valsartan 5, insulin 30 units, Furosemide qty 60."""
    state["currentPatientId"] = "pat_004"
    renew_rx(state, "rx_022", 5)
    modify_rx(state, "rx_023", {"dosage": "30 units"})
    modify_rx(state, "rx_024", {"quantity": 60})


def solve_task_h59(state):
    """Margaret's Pantoprazole: deny urgent refill, hold prescription."""
    deny_rr(state, "rr_003", "Pending GI consult")
    hold_rx(state, "rx_005", "Pending GI consult")


def solve_task_h60(state):
    """Deny Margaret's Metformin refill, hold David's Metformin, increase Robert's Jardiance to 25mg."""
    deny_rr(state, "rr_002", "Need lab work before renewal")
    hold_rx(state, "rx_019", "Pending lab results")
    state["currentPatientId"] = "pat_006"
    modify_rx(state, "rx_027", {"dosage": "25mg"})


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
    "task_h41": solve_task_h41, "task_h42": solve_task_h42, "task_h43": solve_task_h43,
    "task_h44": solve_task_h44, "task_h45": solve_task_h45, "task_h46": solve_task_h46,
    "task_h47": solve_task_h47, "task_h48": solve_task_h48, "task_h49": solve_task_h49,
    "task_h50": solve_task_h50, "task_h51": solve_task_h51, "task_h52": solve_task_h52,
    "task_h53": solve_task_h53, "task_h54": solve_task_h54, "task_h55": solve_task_h55,
    "task_h56": solve_task_h56, "task_h57": solve_task_h57, "task_h58": solve_task_h58,
    "task_h59": solve_task_h59, "task_h60": solve_task_h60,
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
