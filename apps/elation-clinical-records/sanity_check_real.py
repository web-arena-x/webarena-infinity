#!/usr/bin/env python3
"""
Sanity check for Elation Clinical Records real tasks.

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
import signal
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
_SEED_STATE_JS = r"""
const fs = require('fs');
const vm = require('vm');
const code = fs.readFileSync(process.argv[1], 'utf8');
vm.runInThisContext(code);

const state = {
    currentProvider: JSON.parse(JSON.stringify(CURRENT_PROVIDER)),
    providers: JSON.parse(JSON.stringify(PROVIDERS)),
    patients: JSON.parse(JSON.stringify(PATIENTS)),
    problems: JSON.parse(JSON.stringify(PROBLEMS)),
    vaccinations: JSON.parse(JSON.stringify(VACCINATIONS)),
    vitals: JSON.parse(JSON.stringify(VITALS)),
    visitNotes: JSON.parse(JSON.stringify(VISIT_NOTES)),
    carePlans: JSON.parse(JSON.stringify(CARE_PLANS)),
    visitNoteCategories: JSON.parse(JSON.stringify(VISIT_NOTE_CATEGORIES)),
    visitNoteTemplates: JSON.parse(JSON.stringify(VISIT_NOTE_TEMPLATES)),
    appointmentTypes: JSON.parse(JSON.stringify(APPOINTMENT_TYPES)),
    documentTags: [...DOCUMENT_TAGS],
    providerPreferences: JSON.parse(JSON.stringify(PROVIDER_PREFERENCES)),
    _nextProblemId: 100,
    _nextVaxId: 100,
    _nextVitalId: 100,
    _nextNoteId: 100,
    _nextCarePlanId: 100,
    _nextCategoryId: 100,
    _nextTemplateId: 100,
};
process.stdout.write(JSON.stringify(state));
"""


# ── helpers ──────────────────────────────────────────────────────────

def find_patient(state, **kwargs):
    for p in state["patients"]:
        if all(p.get(k) == v for k, v in kwargs.items()):
            return p
    raise ValueError(f"Patient not found: {kwargs}")


def find_problem(state, patient_id, title):
    for p in state["problems"]:
        if p["patientId"] == patient_id and p["title"] == title:
            return p
    raise ValueError(f"Problem not found: patientId={patient_id}, title={title!r}")


def find_problem_containing(state, patient_id, title_fragment):
    for p in state["problems"]:
        if p["patientId"] == patient_id and title_fragment in p["title"]:
            return p
    raise ValueError(f"Problem containing {title_fragment!r} not found for {patient_id}")


def find_note(state, note_id):
    for n in state["visitNotes"]:
        if n["id"] == note_id:
            return n
    raise ValueError(f"Note not found: {note_id}")


def find_template(state, name):
    for t in state["visitNoteTemplates"]:
        if t["name"] == name:
            return t
    raise ValueError(f"Template not found: {name!r}")


def find_category(state, name):
    for c in state["visitNoteCategories"]:
        if c["name"] == name:
            return c
    raise ValueError(f"Category not found: {name!r}")


def find_appointment_type(state, name):
    for a in state["appointmentTypes"]:
        if a["name"] == name:
            return a
    raise ValueError(f"Appointment type not found: {name!r}")


# ── EASY solve functions ─────────────────────────────────────────────

def solve_task_e1(state):
    """Remove 'Smoker' tag from Marcus Johnson."""
    patient = find_patient(state, lastName="Johnson")
    patient["tags"] = [t for t in patient["tags"] if t != "Smoker"]


def solve_task_e2(state):
    """Mark Nakamura's plantar fasciitis as Active."""
    patient = find_patient(state, lastName="Nakamura")
    prob = find_problem(state, patient["id"], "Plantar Fasciitis, Right Foot")
    prob["status"] = "Active"
    prob["resolvedDate"] = ""


def solve_task_e3(state):
    """Turn off coded assessments."""
    state["providerPreferences"]["codedAssessments"] = False


def solve_task_e4(state):
    """Sign note_012."""
    note = find_note(state, "note_012")
    note["status"] = "signed"
    note["signedAt"] = "2026-03-07T10:00:00Z"


def solve_task_e5(state):
    """Delete Injectable Administration template."""
    state["visitNoteTemplates"] = [
        t for t in state["visitNoteTemplates"]
        if t["name"] != "Injectable Administration"
    ]


def solve_task_e6(state):
    """Add 'Fall-Risk' tag to Helen Zhao."""
    patient = find_patient(state, lastName="Zhao")
    if "Fall-Risk" not in patient["tags"]:
        patient["tags"].append("Fall-Risk")
        patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))


def solve_task_e7(state):
    """Enable show Dx codes in print."""
    state["providerPreferences"]["showDxCodesInPrint"] = True


def solve_task_e8(state):
    """Disable MIPS for Procedure."""
    cat = find_category(state, "Procedure")
    cat["countForMIPS"] = False


def solve_task_e9(state):
    """Remove 'Prenatal' tag from Nakamura."""
    patient = find_patient(state, lastName="Nakamura")
    patient["tags"] = [t for t in patient["tags"] if t != "Prenatal"]


def solve_task_e10(state):
    """Rename Workers Comp to Workers Compensation."""
    cat = find_category(state, "Workers Comp")
    cat["name"] = "Workers Compensation"


def solve_task_e11(state):
    """Resolve Johnson's prediabetes."""
    patient = find_patient(state, lastName="Johnson")
    prob = find_problem(state, patient["id"], "Prediabetes")
    prob["status"] = "Resolved"
    prob["resolvedDate"] = "2026-03-07"


def solve_task_e12(state):
    """Enable MIPS for Vaccination Only."""
    cat = find_category(state, "Vaccination Only")
    cat["countForMIPS"] = True


def solve_task_e13(state):
    """Change default note format to simple."""
    state["providerPreferences"]["defaultNoteFormat"] = "simple"


def solve_task_e14(state):
    """Add '*High-Risk' priority tag to O'Brien."""
    patient = find_patient(state, lastName="O'Brien")
    if "*High-Risk" not in patient["tags"]:
        patient["tags"].append("*High-Risk")
        patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))


def solve_task_e15(state):
    """Remove 'Immunizations-Due' from Washington."""
    patient = find_patient(state, lastName="Washington")
    patient["tags"] = [t for t in patient["tags"] if t != "Immunizations-Due"]


def solve_task_e16(state):
    """Delete Care Plan Review category."""
    state["visitNoteCategories"] = [
        c for c in state["visitNoteCategories"]
        if c["name"] != "Care Plan Review"
    ]


def solve_task_e17(state):
    """Mark Bergstrom's depression as Active."""
    patient = find_patient(state, lastName="Bergstrom")
    prob = find_problem_containing(state, patient["id"], "Major Depressive Disorder")
    prob["status"] = "Active"
    prob["resolvedDate"] = ""


def solve_task_e18(state):
    """Duplicate Diabetes Management template."""
    orig = find_template(state, "Diabetes Management")
    next_id = state.get("_nextTemplateId", 100)
    copy = deepcopy(orig)
    copy["id"] = f"tmpl_{next_id:03d}"
    copy["name"] = orig["name"] + " (Copy)"
    copy["createdAt"] = "2026-03-07T10:00:00Z"
    state["visitNoteTemplates"].append(copy)
    state["_nextTemplateId"] = next_id + 1


def solve_task_e19(state):
    """Rename Telehealth Follow-Up to Virtual Visit Follow-Up."""
    tmpl = find_template(state, "Telehealth Follow-Up")
    tmpl["name"] = "Virtual Visit Follow-Up"


def solve_task_e20(state):
    """Remove 'Pediatric-Parent' from Sharma."""
    patient = find_patient(state, lastName="Sharma")
    patient["tags"] = [t for t in patient["tags"] if t != "Pediatric-Parent"]


# ── MEDIUM solve functions ───────────────────────────────────────────

def solve_task_m1(state):
    """Add Acute Sinusitis (J01.90) to Fitzgerald."""
    patient = find_patient(state, lastName="Fitzgerald")
    next_id = state.get("_nextProblemId", 100)
    existing = [p for p in state["problems"] if p["patientId"] == patient["id"]]
    problem = {
        "id": f"prob_{next_id:03d}",
        "patientId": patient["id"],
        "title": "Acute Sinusitis",
        "icd10": "J01.90",
        "icd9": "",
        "snomed": "",
        "dxDate": "2026-03-07",
        "status": "Active",
        "synopsis": "",
        "resolvedDate": "",
        "sortOrder": len(existing),
    }
    state["problems"].append(problem)
    state["_nextProblemId"] = next_id + 1


def solve_task_m2(state):
    """Record influenza vaccine for Nakamura, IM left deltoid."""
    patient = find_patient(state, lastName="Nakamura")
    next_id = state.get("_nextVaxId", 100)
    vax = {
        "id": f"vax_{next_id:03d}",
        "patientId": patient["id"],
        "vaccineName": "Influenza (IIV4) Preservative Free",
        "cvx": "185",
        "ndc": "",
        "manufacturer": "Sanofi Pasteur",
        "lotNumber": "",
        "expirationDate": "",
        "doseAmount": "",
        "doseUnits": "",
        "seriesNumber": "",
        "method": "Intramuscular",
        "site": "Left Deltoid",
        "givenOn": "2026-03-07T10:00:00Z",
        "orderedBy": state["currentProvider"]["id"],
        "givenBy": state["currentProvider"]["id"],
        "recordType": "New",
        "visDate": "",
        "recall": "",
        "reason": "",
        "notes": "",
        "program": "Not VFC Eligible",
        "fundedBy": "Private",
        "source": "New Immunization",
        "status": "completed",
    }
    state["vaccinations"].append(vax)
    state["_nextVaxId"] = next_id + 1


def solve_task_m3(state):
    """Create visit note for Sharma with Simple Note format."""
    patient = find_patient(state, lastName="Sharma")
    next_id = state.get("_nextNoteId", 100)
    note = {
        "id": f"note_{next_id:03d}",
        "patientId": patient["id"],
        "providerId": state["currentProvider"]["id"],
        "format": "simple",
        "category": state["currentProvider"]["defaultCategory"],
        "templateUsed": "",
        "date": "2026-03-07T10:00:00Z",
        "status": "draft",
        "signedAt": "",
        "reason": "",
        "blocks": [],
        "billingItems": [],
        "documentTags": [],
    }
    state["visitNotes"].append(note)
    state["_nextNoteId"] = next_id + 1


def solve_task_m4(state):
    """Add vitals for Henderson: BP 126/78, HR 72."""
    patient = find_patient(state, lastName="Henderson")
    next_id = state.get("_nextVitalId", 100)
    vital = {
        "id": f"vit_{next_id:03d}",
        "patientId": patient["id"],
        "noteId": "",
        "date": "2026-03-07T10:00:00Z",
        "bloodPressureSystolic": 126,
        "bloodPressureDiastolic": 78,
        "heartRate": 72,
        "respiratoryRate": None,
        "temperature": None,
        "temperatureUnit": "F",
        "oxygenSaturation": None,
        "weight": None,
        "weightUnit": "lbs",
        "height": None,
        "heightUnit": "in",
        "bmi": None,
        "painLevel": None,
    }
    state["vitals"].append(vital)
    state["_nextVitalId"] = next_id + 1


def solve_task_m5(state):
    """Create template 'Chronic Pain Follow-Up' with HPI."""
    next_id = state.get("_nextTemplateId", 100)
    tmpl = {
        "id": f"tmpl_{next_id:03d}",
        "name": "Chronic Pain Follow-Up",
        "createdBy": state["currentProvider"]["id"],
        "content": {
            "hpi": "Patient presents for chronic pain management follow-up.",
        },
        "billingItems": [],
        "pos": "",
        "billingNotes": "",
        "documentTags": [],
        "createdAt": "2026-03-07T10:00:00Z",
    }
    state["visitNoteTemplates"].append(tmpl)
    state["_nextTemplateId"] = next_id + 1


def solve_task_m6(state):
    """Change Telehealth Visit appointment to Follow-Up category."""
    apt = find_appointment_type(state, "Telehealth Visit")
    apt["noteCategory"] = "cat_005"


def solve_task_m7(state):
    """Add category 'Behavioral Health' with MIPS."""
    next_id = state.get("_nextCategoryId", 100)
    max_sort = max(c["sortOrder"] for c in state["visitNoteCategories"])
    cat = {
        "id": f"cat_{next_id:03d}",
        "name": "Behavioral Health",
        "countForMIPS": True,
        "isDefault": False,
        "sortOrder": max_sort + 1,
    }
    state["visitNoteCategories"].append(cat)
    state["_nextCategoryId"] = next_id + 1


def solve_task_m8(state):
    """Record declined influenza for Kowalski."""
    patient = find_patient(state, lastName="Kowalski")
    next_id = state.get("_nextVaxId", 100)
    vax = {
        "id": f"vax_{next_id:03d}",
        "patientId": patient["id"],
        "vaccineName": "Influenza (IIV4) Standard",
        "cvx": "",
        "ndc": "",
        "manufacturer": "",
        "lotNumber": "",
        "expirationDate": "",
        "doseAmount": "",
        "doseUnits": "",
        "seriesNumber": "",
        "method": "",
        "site": "",
        "givenOn": "2026-03-07T00:00:00Z",
        "orderedBy": state["currentProvider"]["id"],
        "givenBy": "",
        "recordType": "Declined",
        "visDate": "",
        "recall": "",
        "reason": "Patient prefers not to vaccinate this season",
        "notes": "",
        "program": "",
        "fundedBy": "",
        "source": "",
        "status": "declined",
    }
    state["vaccinations"].append(vax)
    state["_nextVaxId"] = next_id + 1


def solve_task_m9(state):
    """Update Henderson's diabetes synopsis to note A1C 6.8%."""
    patient = find_patient(state, lastName="Henderson")
    prob = find_problem(state, patient["id"], "Type 2 Diabetes Mellitus")
    prob["synopsis"] = "A1C 6.8% at last check. Well-controlled on current regimen."


def solve_task_m10(state):
    """Set Follow-Up appointment to Hypertension Follow-Up template."""
    apt = find_appointment_type(state, "Follow-Up")
    apt["noteTemplate"] = "tmpl_007"


def solve_task_m11(state):
    """Create note for Zhao with Annual Exam category and E* Annual Wellness template."""
    patient = find_patient(state, lastName="Zhao")
    tmpl = find_template(state, "E* Annual Wellness Visit")
    next_id = state.get("_nextNoteId", 100)
    blocks = []
    for section in ["hpi", "ros", "pe", "assessment"]:
        if tmpl.get("content", {}).get(section):
            blocks.append({"type": section, "content": tmpl["content"][section]})
    note = {
        "id": f"note_{next_id:03d}",
        "patientId": patient["id"],
        "providerId": state["currentProvider"]["id"],
        "format": state["currentProvider"]["defaultNoteFormat"],
        "category": "cat_003",
        "templateUsed": "tmpl_001",
        "date": "2026-03-07T10:00:00Z",
        "status": "draft",
        "signedAt": "",
        "reason": "",
        "blocks": blocks,
        "billingItems": deepcopy(tmpl.get("billingItems", [])),
        "documentTags": list(tmpl.get("documentTags", [])),
    }
    state["visitNotes"].append(note)
    state["_nextNoteId"] = next_id + 1


def solve_task_m12(state):
    """Record Tdap for Rodriguez-Martinez with lot TDP-5590."""
    patient = find_patient(state, lastName="Rodriguez-Martinez")
    next_id = state.get("_nextVaxId", 100)
    vax = {
        "id": f"vax_{next_id:03d}",
        "patientId": patient["id"],
        "vaccineName": "Tdap (Adacel)",
        "cvx": "115",
        "ndc": "",
        "manufacturer": "",
        "lotNumber": "TDP-5590",
        "expirationDate": "",
        "doseAmount": "",
        "doseUnits": "",
        "seriesNumber": "",
        "method": "",
        "site": "",
        "givenOn": "2026-03-07T10:00:00Z",
        "orderedBy": state["currentProvider"]["id"],
        "givenBy": state["currentProvider"]["id"],
        "recordType": "New",
        "visDate": "",
        "recall": "",
        "reason": "",
        "notes": "",
        "program": "Not VFC Eligible",
        "fundedBy": "Private",
        "source": "New Immunization",
        "status": "completed",
    }
    state["vaccinations"].append(vax)
    state["_nextVaxId"] = next_id + 1


def solve_task_m13(state):
    """Add vitals for Johnson: temp 37.2 C."""
    patient = find_patient(state, lastName="Johnson")
    next_id = state.get("_nextVitalId", 100)
    vital = {
        "id": f"vit_{next_id:03d}",
        "patientId": patient["id"],
        "noteId": "",
        "date": "2026-03-07T10:00:00Z",
        "bloodPressureSystolic": None,
        "bloodPressureDiastolic": None,
        "heartRate": None,
        "respiratoryRate": None,
        "temperature": 37.2,
        "temperatureUnit": "C",
        "oxygenSaturation": None,
        "weight": None,
        "weightUnit": "lbs",
        "height": None,
        "heightUnit": "in",
        "bmi": None,
        "painLevel": None,
    }
    state["vitals"].append(vital)
    state["_nextVitalId"] = next_id + 1


def solve_task_m14(state):
    """Update billing notes for Pre-Operative Evaluation template."""
    tmpl = find_template(state, "Pre-Operative Evaluation")
    tmpl["billingNotes"] = (
        "Pre-op clearance - ensure all required labs are completed prior to surgery."
    )


def solve_task_m15(state):
    """Change Johnson's 'Chronic Low Back Pain' title."""
    patient = find_patient(state, lastName="Johnson")
    prob = find_problem(state, patient["id"], "Chronic Low Back Pain")
    prob["title"] = "Chronic Low Back Pain with Lumbar Disc Degeneration"


def solve_task_m16(state):
    """Record Ketorolac injection for Johnson, IM left gluteal."""
    patient = find_patient(state, lastName="Johnson")
    next_id = state.get("_nextVaxId", 100)
    vax = {
        "id": f"vax_{next_id:03d}",
        "patientId": patient["id"],
        "vaccineName": "Ketorolac (Toradol)",
        "cvx": "",
        "ndc": "",
        "manufacturer": "",
        "lotNumber": "",
        "expirationDate": "",
        "doseAmount": "",
        "doseUnits": "",
        "seriesNumber": "",
        "method": "Intramuscular",
        "site": "Left Gluteal",
        "givenOn": "2026-03-07T10:00:00Z",
        "orderedBy": state["currentProvider"]["id"],
        "givenBy": state["currentProvider"]["id"],
        "recordType": "New",
        "visDate": "",
        "recall": "",
        "reason": "",
        "notes": "",
        "program": "",
        "fundedBy": "Private",
        "source": "New Immunization",
        "status": "completed",
        "isInjectable": True,
        "notSendToRegistry": True,
    }
    state["vaccinations"].append(vax)
    state["_nextVaxId"] = next_id + 1


def solve_task_m17(state):
    """Change Office Visit appointment to hp_single format."""
    apt = find_appointment_type(state, "Office Visit")
    apt["noteFormat"] = "hp_single"


def solve_task_m18(state):
    """Add vitals for Rodriguez-Martinez: BP 110/68, SpO2 98."""
    patient = find_patient(state, lastName="Rodriguez-Martinez")
    next_id = state.get("_nextVitalId", 100)
    vital = {
        "id": f"vit_{next_id:03d}",
        "patientId": patient["id"],
        "noteId": "",
        "date": "2026-03-07T10:00:00Z",
        "bloodPressureSystolic": 110,
        "bloodPressureDiastolic": 68,
        "heartRate": None,
        "respiratoryRate": None,
        "temperature": None,
        "temperatureUnit": "F",
        "oxygenSaturation": 98,
        "weight": None,
        "weightUnit": "lbs",
        "height": None,
        "heightUnit": "in",
        "bmi": None,
        "painLevel": None,
    }
    state["vitals"].append(vital)
    state["_nextVitalId"] = next_id + 1


def solve_task_m19(state):
    """Create visit note for Bergstrom with Telehealth category."""
    patient = find_patient(state, lastName="Bergstrom")
    next_id = state.get("_nextNoteId", 100)
    note = {
        "id": f"note_{next_id:03d}",
        "patientId": patient["id"],
        "providerId": state["currentProvider"]["id"],
        "format": state["currentProvider"]["defaultNoteFormat"],
        "category": "cat_002",
        "templateUsed": "",
        "date": "2026-03-07T10:00:00Z",
        "status": "draft",
        "signedAt": "",
        "reason": "",
        "blocks": [],
        "billingItems": [],
        "documentTags": [],
    }
    state["visitNotes"].append(note)
    state["_nextNoteId"] = next_id + 1


def solve_task_m20(state):
    """Add 'Chronic-Pain' tag to Diabetes Management template."""
    tmpl = find_template(state, "Diabetes Management")
    if "Chronic-Pain" not in tmpl["documentTags"]:
        tmpl["documentTags"].append("Chronic-Pain")


# ── HARD solve functions ─────────────────────────────────────────────

def solve_task_h1(state):
    """Mark all Johnson's active problems as controlled."""
    patient = find_patient(state, lastName="Johnson")
    for prob in state["problems"]:
        if prob["patientId"] == patient["id"] and prob["status"] == "Active":
            prob["status"] = "Controlled"


def solve_task_h2(state):
    """Create note for Fitzgerald: pre_op format, cat_009, tmpl_010, signed."""
    patient = find_patient(state, lastName="Fitzgerald")
    tmpl = find_template(state, "Pre-Operative Evaluation")
    next_id = state.get("_nextNoteId", 100)
    blocks = []
    for section in ["hpi", "ros", "pe", "assessment"]:
        if tmpl.get("content", {}).get(section):
            blocks.append({"type": section, "content": tmpl["content"][section]})
    note = {
        "id": f"note_{next_id:03d}",
        "patientId": patient["id"],
        "providerId": state["currentProvider"]["id"],
        "format": "pre_op",
        "category": "cat_009",
        "templateUsed": "tmpl_010",
        "date": "2026-03-07T10:00:00Z",
        "status": "signed",
        "signedAt": "2026-03-07T10:05:00Z",
        "reason": "",
        "blocks": blocks,
        "billingItems": deepcopy(tmpl.get("billingItems", [])),
        "documentTags": list(tmpl.get("documentTags", [])),
    }
    state["visitNotes"].append(note)
    state["_nextNoteId"] = next_id + 1


def solve_task_h3(state):
    """Add Osteopenia (M85.80) to Zhao, mark osteoporosis controlled."""
    patient = find_patient(state, lastName="Zhao")
    # Add new problem
    next_id = state.get("_nextProblemId", 100)
    existing = [p for p in state["problems"] if p["patientId"] == patient["id"]]
    problem = {
        "id": f"prob_{next_id:03d}",
        "patientId": patient["id"],
        "title": "Osteopenia",
        "icd10": "M85.80",
        "icd9": "",
        "snomed": "",
        "dxDate": "2026-03-07",
        "status": "Active",
        "synopsis": "",
        "resolvedDate": "",
        "sortOrder": len(existing),
    }
    state["problems"].append(problem)
    state["_nextProblemId"] = next_id + 1
    # Mark osteoporosis controlled
    osteo = find_problem_containing(state, patient["id"], "Osteoporosis")
    osteo["status"] = "Controlled"


def solve_task_h4(state):
    """Record Henderson's 2nd Shingrix: GSK, IM left deltoid, dose 2, 5-year recall."""
    patient = find_patient(state, lastName="Henderson")
    next_id = state.get("_nextVaxId", 100)
    vax = {
        "id": f"vax_{next_id:03d}",
        "patientId": patient["id"],
        "vaccineName": "Shingrix (Zoster Recombinant)",
        "cvx": "187",
        "ndc": "",
        "manufacturer": "GlaxoSmithKline",
        "lotNumber": "",
        "expirationDate": "",
        "doseAmount": "0.5",
        "doseUnits": "mL",
        "seriesNumber": "2",
        "method": "Intramuscular",
        "site": "Left Deltoid",
        "givenOn": "2026-03-07T10:00:00Z",
        "orderedBy": state["currentProvider"]["id"],
        "givenBy": state["currentProvider"]["id"],
        "recordType": "New",
        "visDate": "",
        "recall": "5 years",
        "reason": "",
        "notes": "",
        "program": "Not VFC Eligible",
        "fundedBy": "Private",
        "source": "New Immunization",
        "status": "completed",
    }
    state["vaccinations"].append(vax)
    state["_nextVaxId"] = next_id + 1


def solve_task_h5(state):
    """Create note for Johnson with assessment block and billing 99214."""
    patient = find_patient(state, lastName="Johnson")
    next_id = state.get("_nextNoteId", 100)
    note = {
        "id": f"note_{next_id:03d}",
        "patientId": patient["id"],
        "providerId": state["currentProvider"]["id"],
        "format": state["currentProvider"]["defaultNoteFormat"],
        "category": state["currentProvider"]["defaultCategory"],
        "templateUsed": "",
        "date": "2026-03-07T10:00:00Z",
        "status": "draft",
        "signedAt": "",
        "reason": "Elevated Blood Pressure",
        "blocks": [
            {
                "type": "assessment",
                "content": "Hypertensive urgency. BP remains elevated despite current regimen.",
                "diagnoses": ["I10"],
            }
        ],
        "billingItems": [
            {"cptCode": "99214", "description": "Office visit, established, moderate complexity"}
        ],
        "documentTags": [],
    }
    state["visitNotes"].append(note)
    state["_nextNoteId"] = next_id + 1


def solve_task_h6(state):
    """Record complete vitals for O'Brien."""
    patient = find_patient(state, lastName="O'Brien")
    next_id = state.get("_nextVitalId", 100)
    vital = {
        "id": f"vit_{next_id:03d}",
        "patientId": patient["id"],
        "noteId": "",
        "date": "2026-03-07T10:00:00Z",
        "bloodPressureSystolic": 138,
        "bloodPressureDiastolic": 86,
        "heartRate": 68,
        "respiratoryRate": 18,
        "temperature": 97.6,
        "temperatureUnit": "F",
        "oxygenSaturation": 93,
        "weight": 190,
        "weightUnit": "lbs",
        "height": None,
        "heightUnit": "in",
        "bmi": None,
        "painLevel": 4,
    }
    state["vitals"].append(vital)
    state["_nextVitalId"] = next_id + 1


def solve_task_h7(state):
    """Remove all tags from Rodriguez-Martinez, add 'Inhaler-Review'."""
    patient = find_patient(state, lastName="Rodriguez-Martinez")
    patient["tags"] = ["Inhaler-Review"]


def solve_task_h8(state):
    """Create category 'Chronic Disease Management' with MIPS, set Follow-Up to use it."""
    next_id = state.get("_nextCategoryId", 100)
    max_sort = max(c["sortOrder"] for c in state["visitNoteCategories"])
    cat_id = f"cat_{next_id:03d}"
    cat = {
        "id": cat_id,
        "name": "Chronic Disease Management",
        "countForMIPS": True,
        "isDefault": False,
        "sortOrder": max_sort + 1,
    }
    state["visitNoteCategories"].append(cat)
    state["_nextCategoryId"] = next_id + 1
    # Update Follow-Up appointment type
    apt = find_appointment_type(state, "Follow-Up")
    apt["noteCategory"] = cat_id


def solve_task_h9(state):
    """Record COVID-19 Moderna for Bergstrom: dose 1, Moderna, IM right deltoid, 3w recall, private."""
    patient = find_patient(state, lastName="Bergstrom")
    next_id = state.get("_nextVaxId", 100)
    vax = {
        "id": f"vax_{next_id:03d}",
        "patientId": patient["id"],
        "vaccineName": "COVID-19 Moderna",
        "cvx": "207",
        "ndc": "",
        "manufacturer": "Moderna",
        "lotNumber": "",
        "expirationDate": "",
        "doseAmount": "",
        "doseUnits": "",
        "seriesNumber": "1",
        "method": "Intramuscular",
        "site": "Right Deltoid",
        "givenOn": "2026-03-07T10:00:00Z",
        "orderedBy": state["currentProvider"]["id"],
        "givenBy": state["currentProvider"]["id"],
        "recordType": "New",
        "visDate": "",
        "recall": "3 weeks",
        "reason": "",
        "notes": "",
        "program": "Not VFC Eligible",
        "fundedBy": "Private",
        "source": "New Immunization",
        "status": "completed",
    }
    state["vaccinations"].append(vax)
    state["_nextVaxId"] = next_id + 1


def solve_task_h10(state):
    """Create note for Henderson with Diabetes Management template, add Care Plan block."""
    patient = find_patient(state, lastName="Henderson")
    tmpl = find_template(state, "Diabetes Management")
    next_id = state.get("_nextNoteId", 100)
    blocks = []
    for section in ["hpi", "ros", "pe", "assessment"]:
        if tmpl.get("content", {}).get(section):
            blocks.append({"type": section, "content": tmpl["content"][section]})
    blocks.append({
        "type": "carePlan",
        "content": "Continue metformin 1000mg BID. Recheck A1C in 3 months.",
    })
    note = {
        "id": f"note_{next_id:03d}",
        "patientId": patient["id"],
        "providerId": state["currentProvider"]["id"],
        "format": state["currentProvider"]["defaultNoteFormat"],
        "category": state["currentProvider"]["defaultCategory"],
        "templateUsed": tmpl["id"],
        "date": "2026-03-07T10:00:00Z",
        "status": "draft",
        "signedAt": "",
        "reason": "",
        "blocks": blocks,
        "billingItems": deepcopy(tmpl.get("billingItems", [])),
        "documentTags": list(tmpl.get("documentTags", [])),
    }
    state["visitNotes"].append(note)
    state["_nextNoteId"] = next_id + 1


def solve_task_h11(state):
    """Complete Kowalski's draft: add PE, ROS blocks, billing 99214, sign."""
    note = find_note(state, "note_012")
    note["blocks"].append({
        "type": "pe",
        "content": "General: Alert, oriented. Lumbar spine tenderness to palpation.",
    })
    note["blocks"].append({
        "type": "ros",
        "content": "Constitutional: Denies fever. Musculoskeletal: Reports low back pain. Psych: Reports anxiety.",
    })
    note["billingItems"].append({
        "cptCode": "99214",
        "description": "Office visit, established, moderate complexity",
    })
    note["status"] = "signed"
    note["signedAt"] = "2026-03-07T10:00:00Z"


def solve_task_h12(state):
    """Add two problems to Sharma: UTI (N39.0) and IDA (D50.9)."""
    patient = find_patient(state, lastName="Sharma")
    existing = [p for p in state["problems"] if p["patientId"] == patient["id"]]

    next_id = state.get("_nextProblemId", 100)
    prob1 = {
        "id": f"prob_{next_id:03d}",
        "patientId": patient["id"],
        "title": "Urinary Tract Infection",
        "icd10": "N39.0",
        "icd9": "",
        "snomed": "",
        "dxDate": "2026-03-07",
        "status": "Active",
        "synopsis": "",
        "resolvedDate": "",
        "sortOrder": len(existing),
    }
    state["problems"].append(prob1)

    prob2 = {
        "id": f"prob_{next_id + 1:03d}",
        "patientId": patient["id"],
        "title": "Iron Deficiency Anemia",
        "icd10": "D50.9",
        "icd9": "",
        "snomed": "",
        "dxDate": "2026-03-07",
        "status": "Active",
        "synopsis": "",
        "resolvedDate": "",
        "sortOrder": len(existing) + 1,
    }
    state["problems"].append(prob2)
    state["_nextProblemId"] = next_id + 2


def solve_task_h13(state):
    """Change default format to simple, create note for Wu."""
    state["providerPreferences"]["defaultNoteFormat"] = "simple"
    patient = find_patient(state, lastName="Wu")
    next_id = state.get("_nextNoteId", 100)
    note = {
        "id": f"note_{next_id:03d}",
        "patientId": patient["id"],
        "providerId": state["currentProvider"]["id"],
        "format": "simple",
        "category": state["currentProvider"]["defaultCategory"],
        "templateUsed": "",
        "date": "2026-03-07T10:00:00Z",
        "status": "draft",
        "signedAt": "",
        "reason": "",
        "blocks": [],
        "billingItems": [],
        "documentTags": [],
    }
    state["visitNotes"].append(note)
    state["_nextNoteId"] = next_id + 1


def solve_task_h14(state):
    """Add 'Flu-Season' to all patients with Dr. Sarah Chen (prov_001) as primary."""
    for patient in state["patients"]:
        if patient["primaryProvider"] == "prov_001":
            if "Flu-Season" not in patient["tags"]:
                patient["tags"].append("Flu-Season")
                patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))


def solve_task_h15(state):
    """Create template 'Geriatric Assessment' with HPI, ROS, PE, billing 99205."""
    next_id = state.get("_nextTemplateId", 100)
    tmpl = {
        "id": f"tmpl_{next_id:03d}",
        "name": "Geriatric Assessment",
        "createdBy": state["currentProvider"]["id"],
        "content": {
            "hpi": "Patient presents for comprehensive geriatric assessment.",
            "ros": "Full review of systems documented.",
            "pe": "Comprehensive examination performed.",
        },
        "billingItems": [
            {"cptCode": "99205", "description": "New patient visit, high complexity"}
        ],
        "pos": "",
        "billingNotes": "",
        "documentTags": [],
        "createdAt": "2026-03-07T10:00:00Z",
    }
    state["visitNoteTemplates"].append(tmpl)
    state["_nextTemplateId"] = next_id + 1


def solve_task_h16(state):
    """Set Urgent Same-Day template to E* Problem-Focused, COVID Vaccine format to non_visit."""
    apt1 = find_appointment_type(state, "Urgent Same-Day")
    apt1["noteTemplate"] = "tmpl_002"
    apt2 = find_appointment_type(state, "COVID Vaccine")
    apt2["noteFormat"] = "non_visit"


def solve_task_h17(state):
    """Remove 'Pediatric' tag from both Washington and Wu."""
    for last_name in ["Washington", "Wu"]:
        patient = find_patient(state, lastName=last_name)
        patient["tags"] = [t for t in patient["tags"] if t != "Pediatric"]


def solve_task_h18(state):
    """Add vitals for Wu: BP 108/68, HR 76, temp 98.6 F, weight 115, height 63, pain 0."""
    patient = find_patient(state, lastName="Wu")
    next_id = state.get("_nextVitalId", 100)
    vital = {
        "id": f"vit_{next_id:03d}",
        "patientId": patient["id"],
        "noteId": "",
        "date": "2026-03-07T10:00:00Z",
        "bloodPressureSystolic": 108,
        "bloodPressureDiastolic": 68,
        "heartRate": 76,
        "respiratoryRate": None,
        "temperature": 98.6,
        "temperatureUnit": "F",
        "oxygenSaturation": None,
        "weight": 115,
        "weightUnit": "lbs",
        "height": 63,
        "heightUnit": "in",
        "bmi": None,
        "painLevel": 0,
    }
    state["vitals"].append(vital)
    state["_nextVitalId"] = next_id + 1


def solve_task_h19(state):
    """Create note for O'Brien with Follow-Up category, HPI and Assessment blocks."""
    patient = find_patient(state, lastName="O'Brien")
    next_id = state.get("_nextNoteId", 100)
    note = {
        "id": f"note_{next_id:03d}",
        "patientId": patient["id"],
        "providerId": state["currentProvider"]["id"],
        "format": state["currentProvider"]["defaultNoteFormat"],
        "category": "cat_005",
        "templateUsed": "",
        "date": "2026-03-07T10:00:00Z",
        "status": "draft",
        "signedAt": "",
        "reason": "",
        "blocks": [
            {
                "type": "hpi",
                "content": "Patient returns for cardiac follow-up. Reports stable symptoms.",
            },
            {
                "type": "assessment",
                "content": "CHF stable. AFib rate controlled. CKD stable.",
                "diagnoses": ["I50.22", "I48.1", "N18.31"],
            },
        ],
        "billingItems": [],
        "documentTags": [],
    }
    state["visitNotes"].append(note)
    state["_nextNoteId"] = next_id + 1


def solve_task_h20(state):
    """Record Hep A for Sharma: Merck, lot HA-7721, SC left upper arm, dose 1, 6mo recall, insurance."""
    patient = find_patient(state, lastName="Sharma")
    next_id = state.get("_nextVaxId", 100)
    vax = {
        "id": f"vax_{next_id:03d}",
        "patientId": patient["id"],
        "vaccineName": "Hepatitis A (Havrix)",
        "cvx": "",
        "ndc": "",
        "manufacturer": "Merck",
        "lotNumber": "HA-7721",
        "expirationDate": "",
        "doseAmount": "",
        "doseUnits": "",
        "seriesNumber": "1",
        "method": "Subcutaneous",
        "site": "Left Upper Arm",
        "givenOn": "2026-03-07T10:00:00Z",
        "orderedBy": state["currentProvider"]["id"],
        "givenBy": state["currentProvider"]["id"],
        "recordType": "New",
        "visDate": "",
        "recall": "6 months",
        "reason": "",
        "notes": "",
        "program": "Not VFC Eligible",
        "fundedBy": "Insurance",
        "source": "New Immunization",
        "status": "completed",
    }
    state["vaccinations"].append(vax)
    state["_nextVaxId"] = next_id + 1


# ── HARDENING ROUND 1 solve functions ────────────────────────────────

def solve_task_h21(state):
    """Add 'BP-Alert' to patients whose most recent vitals have systolic >= 130."""
    # Find most recent vitals per patient
    patient_vitals = {}
    for v in state["vitals"]:
        pid = v["patientId"]
        if pid not in patient_vitals or v["date"] > patient_vitals[pid]["date"]:
            patient_vitals[pid] = v
    for pid, v in patient_vitals.items():
        bp = v.get("bloodPressureSystolic")
        if bp is not None and bp >= 130:
            patient = next(p for p in state["patients"] if p["id"] == pid)
            if "BP-Alert" not in patient["tags"]:
                patient["tags"].append("BP-Alert")
                patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))


def solve_task_h22(state):
    """Create visit note with Telehealth category for patient with declined vax."""
    # Find the patient with a declined vaccination
    declined_pid = None
    for vax in state["vaccinations"]:
        if vax.get("recordType") == "Declined":
            declined_pid = vax["patientId"]
            break
    next_id = state.get("_nextNoteId", 100)
    note = {
        "id": f"note_{next_id:03d}",
        "patientId": declined_pid,
        "providerId": state["currentProvider"]["id"],
        "format": state["currentProvider"]["defaultNoteFormat"],
        "category": "cat_002",
        "templateUsed": "",
        "date": "2026-03-08T10:00:00Z",
        "status": "draft",
        "signedAt": "",
        "reason": "",
        "blocks": [],
        "billingItems": [],
        "documentTags": [],
    }
    state["visitNotes"].append(note)
    state["_nextNoteId"] = next_id + 1


def solve_task_h23(state):
    """Duplicate the template assigned to Annual Exam appointment, rename copy."""
    apt = find_appointment_type(state, "Annual Exam")
    tmpl_id = apt["noteTemplate"]
    orig = next(t for t in state["visitNoteTemplates"] if t["id"] == tmpl_id)
    next_id = state.get("_nextTemplateId", 100)
    copy = deepcopy(orig)
    copy["id"] = f"tmpl_{next_id:03d}"
    copy["name"] = "Modified Annual Wellness"
    copy["createdAt"] = "2026-03-08T10:00:00Z"
    state["visitNoteTemplates"].append(copy)
    state["_nextTemplateId"] = next_id + 1


def solve_task_h24(state):
    """Record historical influenza vaccine for Washington (Patel's patient born 2015)."""
    patient = find_patient(state, lastName="Washington")
    next_id = state.get("_nextVaxId", 100)
    vax = {
        "id": f"vax_{next_id:03d}",
        "patientId": patient["id"],
        "vaccineName": "Influenza (IIV4) Standard",
        "cvx": "185",
        "ndc": "",
        "manufacturer": "",
        "lotNumber": "",
        "expirationDate": "",
        "doseAmount": "",
        "doseUnits": "",
        "seriesNumber": "",
        "method": "Intramuscular",
        "site": "Left Deltoid",
        "givenOn": "2025-01-15T00:00:00Z",
        "orderedBy": "",
        "givenBy": "",
        "recordType": "Historical",
        "visDate": "",
        "recall": "",
        "reason": "",
        "notes": "",
        "program": "",
        "fundedBy": "",
        "source": "Historical",
        "status": "completed",
    }
    state["vaccinations"].append(vax)
    state["_nextVaxId"] = next_id + 1


def solve_task_h25(state):
    """Add Pre-Op Evaluation template's billing code (99215) to Kowalski's draft."""
    note = find_note(state, "note_012")
    note["billingItems"].append({
        "cptCode": "99215",
        "description": "Office visit, established, high complexity",
    })


def solve_task_h26(state):
    """Create 'Geriatric Care' category with MIPS, create note for Zhao with it + template, sign."""
    # Create category
    next_cat_id = state.get("_nextCategoryId", 100)
    max_sort = max(c["sortOrder"] for c in state["visitNoteCategories"])
    cat_id = f"cat_{next_cat_id:03d}"
    cat = {
        "id": cat_id,
        "name": "Geriatric Care",
        "countForMIPS": True,
        "isDefault": False,
        "sortOrder": max_sort + 1,
    }
    state["visitNoteCategories"].append(cat)
    state["_nextCategoryId"] = next_cat_id + 1

    # Create note for Zhao
    patient = find_patient(state, lastName="Zhao")
    tmpl = find_template(state, "E* Annual Wellness Visit")
    next_note_id = state.get("_nextNoteId", 100)
    blocks = []
    for section in ["hpi", "ros", "pe", "assessment"]:
        if tmpl.get("content", {}).get(section):
            blocks.append({"type": section, "content": tmpl["content"][section]})
    note = {
        "id": f"note_{next_note_id:03d}",
        "patientId": patient["id"],
        "providerId": state["currentProvider"]["id"],
        "format": state["currentProvider"]["defaultNoteFormat"],
        "category": cat_id,
        "templateUsed": tmpl["id"],
        "date": "2026-03-08T10:00:00Z",
        "status": "signed",
        "signedAt": "2026-03-08T10:05:00Z",
        "reason": "",
        "blocks": blocks,
        "billingItems": deepcopy(tmpl.get("billingItems", [])),
        "documentTags": list(tmpl.get("documentTags", [])),
    }
    state["visitNotes"].append(note)
    state["_nextNoteId"] = next_note_id + 1


def solve_task_h27(state):
    """Resolve all 'Controlled' problems for Henderson (most problems: 6)."""
    patient = find_patient(state, lastName="Henderson")
    for prob in state["problems"]:
        if prob["patientId"] == patient["id"] and prob["status"] == "Controlled":
            prob["status"] = "Resolved"
            prob["resolvedDate"] = "2026-03-08"


def solve_task_h28(state):
    """Set template to tmpl_002 for all appointment types with no template."""
    for apt in state["appointmentTypes"]:
        if not apt.get("noteTemplate"):
            apt["noteTemplate"] = "tmpl_002"


def solve_task_h29(state):
    """Add 'Multi-Condition' to patients with 4+ active problems."""
    active_counts = {}
    for prob in state["problems"]:
        if prob["status"] == "Active":
            pid = prob["patientId"]
            active_counts[pid] = active_counts.get(pid, 0) + 1
    for patient in state["patients"]:
        if active_counts.get(patient["id"], 0) >= 4:
            if "Multi-Condition" not in patient["tags"]:
                patient["tags"].append("Multi-Condition")
                patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))


def solve_task_h30(state):
    """Change default format to hp_single, create note for Nakamura, add HPI, sign."""
    state["providerPreferences"]["defaultNoteFormat"] = "hp_single"
    patient = find_patient(state, lastName="Nakamura")
    next_id = state.get("_nextNoteId", 100)
    note = {
        "id": f"note_{next_id:03d}",
        "patientId": patient["id"],
        "providerId": state["currentProvider"]["id"],
        "format": "hp_single",
        "category": "cat_005",
        "templateUsed": "",
        "date": "2026-03-08T10:00:00Z",
        "status": "signed",
        "signedAt": "2026-03-08T10:05:00Z",
        "reason": "",
        "blocks": [
            {"type": "hpi", "content": "Follow-up visit for anxiety management."},
        ],
        "billingItems": [],
        "documentTags": [],
    }
    state["visitNotes"].append(note)
    state["_nextNoteId"] = next_id + 1


def solve_task_h31(state):
    """Remove 'Diabetes-Management' from all, add 'Diabetes-Active' where diabetes is Active."""
    # Henderson has tag + active diabetes, Bergstrom has tag + controlled diabetes
    for patient in state["patients"]:
        if "Diabetes-Management" in patient["tags"]:
            patient["tags"] = [t for t in patient["tags"] if t != "Diabetes-Management"]
            # Check if this patient has an active diabetes problem
            has_active_diabetes = any(
                p["patientId"] == patient["id"]
                and p["status"] == "Active"
                and "diabetes" in p["title"].lower()
                for p in state["problems"]
            )
            if has_active_diabetes and "Diabetes-Active" not in patient["tags"]:
                patient["tags"].append("Diabetes-Active")
            patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))


def solve_task_h32(state):
    """Create 'COPD Management' template with HPI + billing 99214, create note for Bergstrom."""
    next_tmpl_id = state.get("_nextTemplateId", 100)
    tmpl_id = f"tmpl_{next_tmpl_id:03d}"
    tmpl = {
        "id": tmpl_id,
        "name": "COPD Management",
        "createdBy": state["currentProvider"]["id"],
        "content": {
            "hpi": "Patient presents for COPD management follow-up.",
        },
        "billingItems": [
            {"cptCode": "99214", "description": "Office visit, established, moderate complexity"}
        ],
        "pos": "",
        "billingNotes": "",
        "documentTags": [],
        "createdAt": "2026-03-08T10:00:00Z",
    }
    state["visitNoteTemplates"].append(tmpl)
    state["_nextTemplateId"] = next_tmpl_id + 1

    # Create note for Bergstrom using template
    patient = find_patient(state, lastName="Bergstrom")
    next_note_id = state.get("_nextNoteId", 100)
    note = {
        "id": f"note_{next_note_id:03d}",
        "patientId": patient["id"],
        "providerId": state["currentProvider"]["id"],
        "format": state["currentProvider"]["defaultNoteFormat"],
        "category": state["currentProvider"]["defaultCategory"],
        "templateUsed": tmpl_id,
        "date": "2026-03-08T10:00:00Z",
        "status": "draft",
        "signedAt": "",
        "reason": "",
        "blocks": [
            {"type": "hpi", "content": tmpl["content"]["hpi"]},
        ],
        "billingItems": deepcopy(tmpl["billingItems"]),
        "documentTags": [],
    }
    state["visitNotes"].append(note)
    state["_nextNoteId"] = next_note_id + 1


def solve_task_h33(state):
    """Add 'Respiratory-Alert' to patients with active problems whose ICD-10 starts with J."""
    target_pids = set()
    for prob in state["problems"]:
        if prob["status"] == "Active" and prob.get("icd10", "").startswith("J"):
            target_pids.add(prob["patientId"])
    for patient in state["patients"]:
        if patient["id"] in target_pids:
            if "Respiratory-Alert" not in patient["tags"]:
                patient["tags"].append("Respiratory-Alert")
                patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))


def solve_task_h34(state):
    """Add 'Care-Coordination' to patients with signed notes tagged 'Chronic-Care'."""
    target_pids = set()
    for note in state["visitNotes"]:
        if note.get("status") == "signed" and "Chronic-Care" in note.get("documentTags", []):
            target_pids.add(note["patientId"])
    for patient in state["patients"]:
        if patient["id"] in target_pids:
            if "Care-Coordination" not in patient["tags"]:
                patient["tags"].append("Care-Coordination")
                patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))


def solve_task_h35(state):
    """Record full vitals for Fitzgerald + create note with template and category."""
    patient = find_patient(state, lastName="Fitzgerald")

    # Add vitals
    next_vit_id = state.get("_nextVitalId", 100)
    vital = {
        "id": f"vit_{next_vit_id:03d}",
        "patientId": patient["id"],
        "noteId": "",
        "date": "2026-03-08T10:00:00Z",
        "bloodPressureSystolic": 122,
        "bloodPressureDiastolic": 76,
        "heartRate": 68,
        "respiratoryRate": None,
        "temperature": 98.4,
        "temperatureUnit": "F",
        "oxygenSaturation": 99,
        "weight": 180,
        "weightUnit": "lbs",
        "height": 72,
        "heightUnit": "in",
        "bmi": None,
        "painLevel": 0,
    }
    state["vitals"].append(vital)
    state["_nextVitalId"] = next_vit_id + 1

    # Create note
    tmpl = find_template(state, "E* Problem-Focused Visit")
    next_note_id = state.get("_nextNoteId", 100)
    blocks = []
    for section in ["hpi", "ros", "pe", "assessment"]:
        if tmpl.get("content", {}).get(section):
            blocks.append({"type": section, "content": tmpl["content"][section]})
    note = {
        "id": f"note_{next_note_id:03d}",
        "patientId": patient["id"],
        "providerId": state["currentProvider"]["id"],
        "format": state["currentProvider"]["defaultNoteFormat"],
        "category": "cat_001",
        "templateUsed": tmpl["id"],
        "date": "2026-03-08T10:00:00Z",
        "status": "draft",
        "signedAt": "",
        "reason": "",
        "blocks": blocks,
        "billingItems": deepcopy(tmpl.get("billingItems", [])),
        "documentTags": list(tmpl.get("documentTags", [])),
    }
    state["visitNotes"].append(note)
    state["_nextNoteId"] = next_note_id + 1


def solve_task_h36(state):
    """Add 'Geriatric-Screening' to O'Brien (oldest Medicare patient)."""
    patient = find_patient(state, lastName="O'Brien")
    if "Geriatric-Screening" not in patient["tags"]:
        patient["tags"].append("Geriatric-Screening")
        patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))


def solve_task_h37(state):
    """Mark all O'Brien's active problems as Controlled, add 'Stable', remove 'CHF'."""
    patient = find_patient(state, lastName="O'Brien")
    for prob in state["problems"]:
        if prob["patientId"] == patient["id"] and prob["status"] == "Active":
            prob["status"] = "Controlled"
    patient["tags"] = [t for t in patient["tags"] if t != "CHF"]
    if "Stable" not in patient["tags"]:
        patient["tags"].append("Stable")
    patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))


def solve_task_h38(state):
    """Configure Procedure: template from Office Visit, category from Follow-Up, format hp_single."""
    office = find_appointment_type(state, "Office Visit")
    followup = find_appointment_type(state, "Follow-Up")
    procedure = find_appointment_type(state, "Procedure")
    procedure["noteTemplate"] = office["noteTemplate"]
    procedure["noteCategory"] = followup["noteCategory"]
    procedure["noteFormat"] = "hp_single"


def solve_task_h39(state):
    """Add Acute Bronchitis (J20.9) to Rodriguez-Martinez, create note with template, sign."""
    patient = find_patient(state, lastName="Rodriguez-Martinez")

    # Add problem
    next_prob_id = state.get("_nextProblemId", 100)
    existing = [p for p in state["problems"] if p["patientId"] == patient["id"]]
    problem = {
        "id": f"prob_{next_prob_id:03d}",
        "patientId": patient["id"],
        "title": "Acute Bronchitis",
        "icd10": "J20.9",
        "icd9": "",
        "snomed": "",
        "dxDate": "2026-03-08",
        "status": "Active",
        "synopsis": "",
        "resolvedDate": "",
        "sortOrder": len(existing),
    }
    state["problems"].append(problem)
    state["_nextProblemId"] = next_prob_id + 1

    # Create note with E* Problem-Focused Visit template
    tmpl = find_template(state, "E* Problem-Focused Visit")
    next_note_id = state.get("_nextNoteId", 100)
    blocks = []
    for section in ["hpi", "ros", "pe", "assessment"]:
        if tmpl.get("content", {}).get(section):
            blocks.append({"type": section, "content": tmpl["content"][section]})
    note = {
        "id": f"note_{next_note_id:03d}",
        "patientId": patient["id"],
        "providerId": state["currentProvider"]["id"],
        "format": state["currentProvider"]["defaultNoteFormat"],
        "category": state["currentProvider"]["defaultCategory"],
        "templateUsed": tmpl["id"],
        "date": "2026-03-08T10:00:00Z",
        "status": "signed",
        "signedAt": "2026-03-08T10:05:00Z",
        "reason": "",
        "blocks": blocks,
        "billingItems": deepcopy(tmpl.get("billingItems", [])),
        "documentTags": list(tmpl.get("documentTags", [])),
    }
    state["visitNotes"].append(note)
    state["_nextNoteId"] = next_note_id + 1


def solve_task_h40(state):
    """Add 'Needs-Visit' to patients with no visit notes."""
    patients_with_notes = {n["patientId"] for n in state["visitNotes"]}
    for patient in state["patients"]:
        if patient["id"] not in patients_with_notes:
            if "Needs-Visit" not in patient["tags"]:
                patient["tags"].append("Needs-Visit")
                patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))


# ── HARDENING ROUND 2 solve functions ────────────────────────────────

def solve_task_h41(state):
    """Find highest BMI patient (Johnson, 33.2), add 'Weight-Management' tag + Obesity problem."""
    # Find patient with highest BMI
    max_bmi = None
    max_pid = None
    for v in state["vitals"]:
        bmi = v.get("bmi")
        if bmi is not None and (max_bmi is None or bmi > max_bmi):
            max_bmi = bmi
            max_pid = v["patientId"]
    patient = next(p for p in state["patients"] if p["id"] == max_pid)
    if "Weight-Management" not in patient["tags"]:
        patient["tags"].append("Weight-Management")
        patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))
    # Add obesity problem
    next_id = state.get("_nextProblemId", 100)
    existing = [p for p in state["problems"] if p["patientId"] == max_pid]
    problem = {
        "id": f"prob_{next_id:03d}",
        "patientId": max_pid,
        "title": "Obesity, unspecified",
        "icd10": "E66.09",
        "icd9": "",
        "snomed": "",
        "dxDate": "2026-03-08",
        "status": "Active",
        "synopsis": "",
        "resolvedDate": "",
        "sortOrder": len(existing),
    }
    state["problems"].append(problem)
    state["_nextProblemId"] = next_id + 1


def solve_task_h42(state):
    """Find patient with Urgent Visit note (Johnson), create signed note with Follow-Up + Hypertension template."""
    # Johnson has note_005 with cat_007 (Urgent Visit)
    patient = find_patient(state, lastName="Johnson")
    tmpl = find_template(state, "Hypertension Follow-Up")
    next_id = state.get("_nextNoteId", 100)
    blocks = []
    for section in ["hpi", "ros", "pe", "assessment"]:
        if tmpl.get("content", {}).get(section):
            blocks.append({"type": section, "content": tmpl["content"][section]})
    note = {
        "id": f"note_{next_id:03d}",
        "patientId": patient["id"],
        "providerId": state["currentProvider"]["id"],
        "format": state["currentProvider"]["defaultNoteFormat"],
        "category": "cat_005",
        "templateUsed": tmpl["id"],
        "date": "2026-03-08T10:00:00Z",
        "status": "signed",
        "signedAt": "2026-03-08T10:05:00Z",
        "reason": "",
        "blocks": blocks,
        "billingItems": deepcopy(tmpl.get("billingItems", [])),
        "documentTags": list(tmpl.get("documentTags", [])),
    }
    state["visitNotes"].append(note)
    state["_nextNoteId"] = next_id + 1


def solve_task_h43(state):
    """Add 'Vaccinated' to patients with vax records, 'No-Vaccines' to those without."""
    patients_with_vax = set()
    for v in state["vaccinations"]:
        patients_with_vax.add(v["patientId"])
    for patient in state["patients"]:
        if patient["id"] in patients_with_vax:
            if "Vaccinated" not in patient["tags"]:
                patient["tags"].append("Vaccinated")
                patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))
        else:
            if "No-Vaccines" not in patient["tags"]:
                patient["tags"].append("No-Vaccines")
                patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))


def solve_task_h44(state):
    """Look up Flu Shot template (tmpl_004), create note for Washington with it + Vaccination Only."""
    apt = find_appointment_type(state, "Flu Shot")
    tmpl_id = apt["noteTemplate"]
    tmpl = next(t for t in state["visitNoteTemplates"] if t["id"] == tmpl_id)
    patient = find_patient(state, lastName="Washington")
    next_id = state.get("_nextNoteId", 100)
    blocks = []
    for section in ["hpi", "ros", "pe", "assessment", "proceduresAdministered"]:
        key = section if section != "proceduresAdministered" else "proceduresAdministered"
        if tmpl.get("content", {}).get(key):
            block_type = "procedures_administered" if key == "proceduresAdministered" else section
            blocks.append({"type": block_type, "content": tmpl["content"][key]})
    note = {
        "id": f"note_{next_id:03d}",
        "patientId": patient["id"],
        "providerId": state["currentProvider"]["id"],
        "format": state["currentProvider"]["defaultNoteFormat"],
        "category": "cat_008",
        "templateUsed": tmpl_id,
        "date": "2026-03-08T10:00:00Z",
        "status": "draft",
        "signedAt": "",
        "reason": "",
        "blocks": blocks,
        "billingItems": deepcopy(tmpl.get("billingItems", [])),
        "documentTags": list(tmpl.get("documentTags", [])),
    }
    state["visitNotes"].append(note)
    state["_nextNoteId"] = next_id + 1


def solve_task_h45(state):
    """Find draft note (note_012), add Social History + Follow Up blocks, billing 99215, sign."""
    note = find_note(state, "note_012")
    note["blocks"].append({
        "type": "social_history",
        "content": "Patient reports stable living situation. Works full-time.",
    })
    note["blocks"].append({
        "type": "follow_up",
        "content": "Follow up in 4 weeks. Continue current treatment plan.",
    })
    note["billingItems"].append({
        "cptCode": "99215",
        "description": "Office visit, established, high complexity",
    })
    note["status"] = "signed"
    note["signedAt"] = "2026-03-08T10:00:00Z"


def solve_task_h46(state):
    """Add 'Active-Plan' to patients with active care plans."""
    patients_with_active_plan = set()
    for cp in state["carePlans"]:
        if cp.get("status", "").lower() == "active":
            patients_with_active_plan.add(cp["patientId"])
    for patient in state["patients"]:
        if patient["id"] in patients_with_active_plan:
            if "Active-Plan" not in patient["tags"]:
                patient["tags"].append("Active-Plan")
                patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))


def solve_task_h47(state):
    """Disable MIPS on default (Office Visit), create 'Quality Metrics' with MIPS, assign to Annual Exam."""
    # Disable MIPS on default category
    cat = find_category(state, "Office Visit")
    cat["countForMIPS"] = False
    # Create Quality Metrics
    next_id = state.get("_nextCategoryId", 100)
    max_sort = max(c["sortOrder"] for c in state["visitNoteCategories"])
    cat_id = f"cat_{next_id:03d}"
    new_cat = {
        "id": cat_id,
        "name": "Quality Metrics",
        "countForMIPS": True,
        "isDefault": False,
        "sortOrder": max_sort + 1,
    }
    state["visitNoteCategories"].append(new_cat)
    state["_nextCategoryId"] = next_id + 1
    # Assign to Annual Exam
    apt = find_appointment_type(state, "Annual Exam")
    apt["noteCategory"] = cat_id


def solve_task_h48(state):
    """Record PCV20 for O'Brien (born 1948, Medicare): Pfizer, IM left deltoid, dose 1, 5yr, Medicare."""
    patient = find_patient(state, lastName="O'Brien")
    next_id = state.get("_nextVaxId", 100)
    vax = {
        "id": f"vax_{next_id:03d}",
        "patientId": patient["id"],
        "vaccineName": "Pneumococcal 20-valent (PCV20)",
        "cvx": "216",
        "ndc": "",
        "manufacturer": "Pfizer",
        "lotNumber": "",
        "expirationDate": "",
        "doseAmount": "0.5",
        "doseUnits": "mL",
        "seriesNumber": "1",
        "method": "Intramuscular",
        "site": "Left Deltoid",
        "givenOn": "2026-03-08T10:00:00Z",
        "orderedBy": state["currentProvider"]["id"],
        "givenBy": state["currentProvider"]["id"],
        "recordType": "New",
        "visDate": "",
        "recall": "5 years",
        "reason": "",
        "notes": "",
        "program": "Not VFC Eligible",
        "fundedBy": "Medicare",
        "source": "New Immunization",
        "status": "completed",
    }
    state["vaccinations"].append(vax)
    state["_nextVaxId"] = next_id + 1


def solve_task_h49(state):
    """Tag Henderson (Active E11.65) with 'DM-Review-Urgent', Bergstrom (Controlled) with 'DM-Review-Routine'."""
    for prob in state["problems"]:
        if prob["icd10"] == "E11.65":
            pid = prob["patientId"]
            patient = next(p for p in state["patients"] if p["id"] == pid)
            if prob["status"] == "Active":
                tag = "DM-Review-Urgent"
            elif prob["status"] == "Controlled":
                tag = "DM-Review-Routine"
            else:
                continue
            if tag not in patient["tags"]:
                patient["tags"].append(tag)
                patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))


def solve_task_h50(state):
    """Create 'Comprehensive Visit' template + billing 99215, configure Urgent Same-Day."""
    next_id = state.get("_nextTemplateId", 100)
    tmpl_id = f"tmpl_{next_id:03d}"
    tmpl = {
        "id": tmpl_id,
        "name": "Comprehensive Visit",
        "createdBy": state["currentProvider"]["id"],
        "content": {
            "hpi": "Patient presents for comprehensive evaluation.",
            "ros": "Full review of systems documented.",
            "pe": "Comprehensive physical examination performed.",
            "assessment": "Assessment and plan documented below.",
        },
        "billingItems": [
            {"cptCode": "99215", "description": "Office visit, established, high complexity"}
        ],
        "pos": "",
        "billingNotes": "",
        "documentTags": [],
        "createdAt": "2026-03-08T10:00:00Z",
    }
    state["visitNoteTemplates"].append(tmpl)
    state["_nextTemplateId"] = next_id + 1
    # Configure Urgent Same-Day
    apt = find_appointment_type(state, "Urgent Same-Day")
    apt["noteTemplate"] = tmpl_id
    apt["noteFormat"] = "hp_single"


def solve_task_h51(state):
    """Find lowest SpO2 patient (Bergstrom, 93), create signed note with Problem-Focused template + blocks."""
    patient = find_patient(state, lastName="Bergstrom")
    tmpl = find_template(state, "E* Problem-Focused Visit")
    next_id = state.get("_nextNoteId", 100)
    blocks = []
    for section in ["hpi", "ros", "pe", "assessment"]:
        if tmpl.get("content", {}).get(section):
            blocks.append({"type": section, "content": tmpl["content"][section]})
    # Ensure HPI and assessment blocks exist
    has_hpi = any(b["type"] == "hpi" for b in blocks)
    has_assessment = any(b["type"] == "assessment" for b in blocks)
    if not has_hpi:
        blocks.insert(0, {"type": "hpi", "content": "Patient presents with respiratory concerns."})
    if not has_assessment:
        blocks.append({"type": "assessment", "content": "Assessment and plan documented."})
    note = {
        "id": f"note_{next_id:03d}",
        "patientId": patient["id"],
        "providerId": state["currentProvider"]["id"],
        "format": state["currentProvider"]["defaultNoteFormat"],
        "category": state["currentProvider"]["defaultCategory"],
        "templateUsed": tmpl["id"],
        "date": "2026-03-08T10:00:00Z",
        "status": "signed",
        "signedAt": "2026-03-08T10:05:00Z",
        "reason": "",
        "blocks": blocks,
        "billingItems": deepcopy(tmpl.get("billingItems", [])),
        "documentTags": list(tmpl.get("documentTags", [])),
    }
    state["visitNotes"].append(note)
    state["_nextNoteId"] = next_id + 1


def solve_task_h52(state):
    """Add 'Provider-Reviewed' tag to all templates created by current provider (prov_001)."""
    current_id = state["currentProvider"]["id"]
    for tmpl in state["visitNoteTemplates"]:
        if tmpl.get("createdBy") == current_id:
            if "Provider-Reviewed" not in tmpl.get("documentTags", []):
                tmpl.setdefault("documentTags", []).append("Provider-Reviewed")


def solve_task_h53(state):
    """Add 'Frequent-Visitor' to patients with 2+ signed notes."""
    signed_counts = {}
    for n in state["visitNotes"]:
        if n.get("status") == "signed":
            pid = n["patientId"]
            signed_counts[pid] = signed_counts.get(pid, 0) + 1
    for patient in state["patients"]:
        if signed_counts.get(patient["id"], 0) >= 2:
            if "Frequent-Visitor" not in patient["tags"]:
                patient["tags"].append("Frequent-Visitor")
                patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))


def solve_task_h54(state):
    """Find patient with most vaccinations (Henderson, 6), create note with Vaccination Only + COVID template."""
    vax_counts = {}
    for v in state["vaccinations"]:
        pid = v["patientId"]
        vax_counts[pid] = vax_counts.get(pid, 0) + 1
    max_pid = max(vax_counts, key=vax_counts.get)
    tmpl = find_template(state, "COVID-19 Vaccine Visit")
    next_id = state.get("_nextNoteId", 100)
    blocks = []
    for section in ["hpi", "ros", "pe", "assessment", "proceduresAdministered"]:
        key = section if section != "proceduresAdministered" else "proceduresAdministered"
        if tmpl.get("content", {}).get(key):
            block_type = "procedures_administered" if key == "proceduresAdministered" else section
            blocks.append({"type": block_type, "content": tmpl["content"][key]})
    note = {
        "id": f"note_{next_id:03d}",
        "patientId": max_pid,
        "providerId": state["currentProvider"]["id"],
        "format": state["currentProvider"]["defaultNoteFormat"],
        "category": "cat_008",
        "templateUsed": tmpl["id"],
        "date": "2026-03-08T10:00:00Z",
        "status": "draft",
        "signedAt": "",
        "reason": "",
        "blocks": blocks,
        "billingItems": deepcopy(tmpl.get("billingItems", [])),
        "documentTags": list(tmpl.get("documentTags", [])),
    }
    state["visitNotes"].append(note)
    state["_nextNoteId"] = next_id + 1


def solve_task_h55(state):
    """Resolve all problems with Controlled status across all patients."""
    for prob in state["problems"]:
        if prob["status"] == "Controlled":
            prob["status"] = "Resolved"
            prob["resolvedDate"] = "2026-03-08"


def solve_task_h56(state):
    """Duplicate template with POS '02' (tmpl_003), rename to 'Virtual Care Standard', assign to Telehealth Visit."""
    orig = next(t for t in state["visitNoteTemplates"] if t.get("pos") == "02")
    next_id = state.get("_nextTemplateId", 100)
    copy = deepcopy(orig)
    copy["id"] = f"tmpl_{next_id:03d}"
    copy["name"] = "Virtual Care Standard"
    copy["createdAt"] = "2026-03-08T10:00:00Z"
    state["visitNoteTemplates"].append(copy)
    state["_nextTemplateId"] = next_id + 1
    # Assign to Telehealth Visit
    apt = find_appointment_type(state, "Telehealth Visit")
    apt["noteTemplate"] = copy["id"]


def solve_task_h57(state):
    """Create 'Mental Health Visit' category, note for Nakamura with it + Telehealth template, blocks, billing, sign."""
    # Create category
    next_cat_id = state.get("_nextCategoryId", 100)
    max_sort = max(c["sortOrder"] for c in state["visitNoteCategories"])
    cat_id = f"cat_{next_cat_id:03d}"
    cat = {
        "id": cat_id,
        "name": "Mental Health Visit",
        "countForMIPS": True,
        "isDefault": False,
        "sortOrder": max_sort + 1,
    }
    state["visitNoteCategories"].append(cat)
    state["_nextCategoryId"] = next_cat_id + 1

    # Create note for Nakamura
    patient = find_patient(state, lastName="Nakamura")
    tmpl = find_template(state, "Telehealth Follow-Up")
    next_note_id = state.get("_nextNoteId", 100)
    blocks = []
    for section in ["hpi", "ros", "pe", "assessment"]:
        if tmpl.get("content", {}).get(section):
            blocks.append({"type": section, "content": tmpl["content"][section]})
    # Ensure HPI block exists
    if not any(b["type"] == "hpi" for b in blocks):
        blocks.insert(0, {"type": "hpi", "content": "Telehealth follow-up for mental health concerns."})
    # Add psychological_status block
    blocks.append({
        "type": "psychological_status",
        "content": "Patient reports ongoing anxiety symptoms. GAD-7 reviewed.",
    })
    note = {
        "id": f"note_{next_note_id:03d}",
        "patientId": patient["id"],
        "providerId": state["currentProvider"]["id"],
        "format": state["currentProvider"]["defaultNoteFormat"],
        "category": cat_id,
        "templateUsed": tmpl["id"],
        "date": "2026-03-08T10:00:00Z",
        "status": "signed",
        "signedAt": "2026-03-08T10:05:00Z",
        "reason": "",
        "blocks": blocks,
        "billingItems": [
            {"cptCode": "99214", "description": "Office visit, established, moderate complexity"}
        ],
        "documentTags": list(tmpl.get("documentTags", [])),
    }
    state["visitNotes"].append(note)
    state["_nextNoteId"] = next_note_id + 1


def solve_task_h58(state):
    """Add 'Flu-Overdue' to patients over 65 with no flu vaccine."""
    from datetime import datetime
    today = datetime(2026, 3, 8)
    patients_with_flu = set()
    for v in state["vaccinations"]:
        name = (v.get("vaccineName") or "").lower()
        if "influenza" in name or "flu" in name:
            patients_with_flu.add(v["patientId"])
    for patient in state["patients"]:
        dob_str = patient.get("dateOfBirth", "")
        if not dob_str:
            continue
        dob = datetime.strptime(dob_str, "%Y-%m-%d")
        age = (today - dob).days // 365
        if age > 65 and patient["id"] not in patients_with_flu:
            if "Flu-Overdue" not in patient["tags"]:
                patient["tags"].append("Flu-Overdue")
                patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))


def solve_task_h59(state):
    """Find template with billing 99395 (tmpl_001), create note for youngest adult (Rodriguez-Martinez)."""
    from datetime import datetime
    today = datetime(2026, 3, 8)
    tmpl = next(
        t for t in state["visitNoteTemplates"]
        if any(b.get("cptCode") == "99395" for b in t.get("billingItems", []))
    )
    # Find youngest adult (18+)
    adults = []
    for p in state["patients"]:
        dob_str = p.get("dateOfBirth", "")
        if not dob_str:
            continue
        dob = datetime.strptime(dob_str, "%Y-%m-%d")
        age = (today - dob).days // 365
        if age >= 18:
            adults.append((p, dob))
    adults.sort(key=lambda x: x[1], reverse=True)
    patient = adults[0][0]

    next_id = state.get("_nextNoteId", 100)
    blocks = []
    for section in ["hpi", "ros", "pe", "assessment"]:
        if tmpl.get("content", {}).get(section):
            blocks.append({"type": section, "content": tmpl["content"][section]})
    note = {
        "id": f"note_{next_id:03d}",
        "patientId": patient["id"],
        "providerId": state["currentProvider"]["id"],
        "format": state["currentProvider"]["defaultNoteFormat"],
        "category": "cat_003",
        "templateUsed": tmpl["id"],
        "date": "2026-03-08T10:00:00Z",
        "status": "draft",
        "signedAt": "",
        "reason": "",
        "blocks": blocks,
        "billingItems": deepcopy(tmpl.get("billingItems", [])),
        "documentTags": list(tmpl.get("documentTags", [])),
    }
    state["visitNotes"].append(note)
    state["_nextNoteId"] = next_id + 1


def solve_task_h60(state):
    """Add 'Recent-Diagnosis' to patients with problems diagnosed 2024+."""
    target_pids = set()
    for prob in state["problems"]:
        dx_date = prob.get("dxDate", "")
        if dx_date and dx_date >= "2024-01-01":
            target_pids.add(prob["patientId"])
    for patient in state["patients"]:
        if patient["id"] in target_pids:
            if "Recent-Diagnosis" not in patient["tags"]:
                patient["tags"].append("Recent-Diagnosis")
                patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))


# ── HARDENING ROUND 3 solve functions ────────────────────────────────

def solve_task_h61(state):
    """Add 'External-Review' to patients with non-current provider AND active problems."""
    current_id = state["currentProvider"]["id"]
    active_pids = set()
    for prob in state["problems"]:
        if prob["status"] == "Active":
            active_pids.add(prob["patientId"])
    for patient in state["patients"]:
        if patient["primaryProvider"] != current_id and patient["id"] in active_pids:
            if "External-Review" not in patient["tags"]:
                patient["tags"].append("External-Review")
                patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))


def solve_task_h62(state):
    """COVID Vaccine template → tags=['COVID-Protocol'], assign to Urgent Same-Day."""
    covid_apt = find_appointment_type(state, "COVID Vaccine")
    tmpl_id = covid_apt["noteTemplate"]
    tmpl = next(t for t in state["visitNoteTemplates"] if t["id"] == tmpl_id)
    tmpl["documentTags"] = ["COVID-Protocol"]
    urgent_apt = find_appointment_type(state, "Urgent Same-Day")
    urgent_apt["noteTemplate"] = tmpl_id


def solve_task_h63(state):
    """Create signed Telehealth notes for all patients sharing Kowalski's anxiety ICD-10."""
    kowalski = find_patient(state, lastName="Kowalski")
    anxiety_icd = None
    for prob in state["problems"]:
        if prob["patientId"] == kowalski["id"] and "anxiety" in prob["title"].lower():
            anxiety_icd = prob["icd10"]
            break
    target_pids = set()
    for prob in state["problems"]:
        if prob["icd10"] == anxiety_icd:
            target_pids.add(prob["patientId"])
    telehealth_cat = find_category(state, "Telehealth")
    for pid in target_pids:
        next_id = state.get("_nextNoteId", 100)
        note = {
            "id": f"note_{next_id:03d}",
            "patientId": pid,
            "providerId": state["currentProvider"]["id"],
            "format": state["currentProvider"]["defaultNoteFormat"],
            "category": telehealth_cat["id"],
            "templateUsed": "",
            "date": "2026-03-08T10:00:00Z",
            "status": "signed",
            "signedAt": "2026-03-08T10:05:00Z",
            "reason": "",
            "blocks": [],
            "billingItems": [],
            "documentTags": [],
        }
        state["visitNotes"].append(note)
        state["_nextNoteId"] = next_id + 1


def solve_task_h64(state):
    """Female with exactly 3 active problems (Nakamura) → historical flu vax + tag."""
    from collections import Counter
    active_counts = Counter()
    for prob in state["problems"]:
        if prob["status"] == "Active":
            active_counts[prob["patientId"]] += 1
    target = None
    for p in state["patients"]:
        sex = (p.get("sexAtBirth") or p.get("gender") or "").lower()
        if sex == "female" and active_counts.get(p["id"], 0) == 3:
            target = p
            break
    if "Flu-Historical" not in target["tags"]:
        target["tags"].append("Flu-Historical")
        target["tags"].sort(key=lambda t: (not t.startswith("*"), t))
    next_id = state.get("_nextVaxId", 100)
    vax = {
        "id": f"vax_{next_id:03d}",
        "patientId": target["id"],
        "vaccineName": "Influenza (IIV4) Standard",
        "cvx": "185",
        "ndc": "",
        "manufacturer": "",
        "lotNumber": "",
        "expirationDate": "",
        "doseAmount": "",
        "doseUnits": "",
        "seriesNumber": "",
        "method": "Intramuscular",
        "site": "Left Deltoid",
        "givenOn": "2025-01-15T00:00:00Z",
        "orderedBy": "",
        "givenBy": "",
        "recordType": "Historical",
        "visDate": "",
        "recall": "",
        "reason": "",
        "notes": "",
        "program": "",
        "fundedBy": "",
        "source": "Historical",
        "status": "completed",
    }
    state["vaccinations"].append(vax)
    state["_nextVaxId"] = next_id + 1


def solve_task_h65(state):
    """Active+Controlled → 'Mixed-Status'. Active only → 'All-Active'."""
    patient_statuses = {}
    for prob in state["problems"]:
        pid = prob["patientId"]
        if pid not in patient_statuses:
            patient_statuses[pid] = set()
        patient_statuses[pid].add(prob["status"])
    for patient in state["patients"]:
        pid = patient["id"]
        statuses = patient_statuses.get(pid, set())
        has_active = "Active" in statuses
        has_controlled = "Controlled" in statuses
        if has_active and has_controlled:
            if "Mixed-Status" not in patient["tags"]:
                patient["tags"].append("Mixed-Status")
                patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))
        elif has_active and not has_controlled:
            if "All-Active" not in patient["tags"]:
                patient["tags"].append("All-Active")
                patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))


def solve_task_h66(state):
    """Create 'Anxiety Management' template, note for Nakamura with it + Telehealth, psych block, sign."""
    next_tmpl_id = state.get("_nextTemplateId", 100)
    tmpl_id = f"tmpl_{next_tmpl_id:03d}"
    tmpl = {
        "id": tmpl_id,
        "name": "Anxiety Management",
        "createdBy": state["currentProvider"]["id"],
        "content": {
            "hpi": "Patient presents for anxiety management follow-up.",
            "assessment": "Anxiety disorder assessment and plan.",
        },
        "billingItems": [
            {"cptCode": "99213", "description": "Office visit, established, low complexity"}
        ],
        "pos": "",
        "billingNotes": "",
        "documentTags": [],
        "createdAt": "2026-03-08T10:00:00Z",
    }
    state["visitNoteTemplates"].append(tmpl)
    state["_nextTemplateId"] = next_tmpl_id + 1

    patient = find_patient(state, lastName="Nakamura")
    telehealth_cat = find_category(state, "Telehealth")
    next_note_id = state.get("_nextNoteId", 100)
    blocks = [
        {"type": "hpi", "content": tmpl["content"]["hpi"]},
        {"type": "assessment", "content": tmpl["content"]["assessment"]},
        {"type": "psychological_status", "content": "Patient reports anxiety symptoms. GAD-7 reviewed."},
    ]
    note = {
        "id": f"note_{next_note_id:03d}",
        "patientId": patient["id"],
        "providerId": state["currentProvider"]["id"],
        "format": state["currentProvider"]["defaultNoteFormat"],
        "category": telehealth_cat["id"],
        "templateUsed": tmpl_id,
        "date": "2026-03-08T10:00:00Z",
        "status": "signed",
        "signedAt": "2026-03-08T10:05:00Z",
        "reason": "",
        "blocks": blocks,
        "billingItems": deepcopy(tmpl["billingItems"]),
        "documentTags": [],
    }
    state["visitNotes"].append(note)
    state["_nextNoteId"] = next_note_id + 1


def solve_task_h67(state):
    """Most recent vax patient (Henderson) → tag + signed Follow-Up note with HTN template."""
    most_recent = max(state["vaccinations"], key=lambda v: v.get("givenOn", ""))
    target_pid = most_recent["patientId"]
    patient = next(p for p in state["patients"] if p["id"] == target_pid)
    if "Recent-Immunization" not in patient["tags"]:
        patient["tags"].append("Recent-Immunization")
        patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))

    tmpl = find_template(state, "Hypertension Follow-Up")
    followup_cat = find_category(state, "Follow-Up")
    next_id = state.get("_nextNoteId", 100)
    blocks = []
    for section in ["hpi", "ros", "pe", "assessment"]:
        if tmpl.get("content", {}).get(section):
            blocks.append({"type": section, "content": tmpl["content"][section]})
    note = {
        "id": f"note_{next_id:03d}",
        "patientId": target_pid,
        "providerId": state["currentProvider"]["id"],
        "format": state["currentProvider"]["defaultNoteFormat"],
        "category": followup_cat["id"],
        "templateUsed": tmpl["id"],
        "date": "2026-03-08T10:00:00Z",
        "status": "signed",
        "signedAt": "2026-03-08T10:05:00Z",
        "reason": "",
        "blocks": blocks,
        "billingItems": deepcopy(tmpl.get("billingItems", [])),
        "documentTags": list(tmpl.get("documentTags", [])),
    }
    state["visitNotes"].append(note)
    state["_nextNoteId"] = next_id + 1


def solve_task_h68(state):
    """Change all complete_hp appointment types to hp_single."""
    for apt in state["appointmentTypes"]:
        if apt["noteFormat"] == "complete_hp":
            apt["noteFormat"] = "hp_single"


def solve_task_h69(state):
    """Highest HR patient → 'Tachycardia-Screen'. Highest pain → 'Pain-Management'."""
    max_hr = max_pain = None
    max_hr_pid = max_pain_pid = None
    for v in state["vitals"]:
        hr = v.get("heartRate")
        if hr is not None and (max_hr is None or hr > max_hr):
            max_hr = hr
            max_hr_pid = v["patientId"]
        pain = v.get("painLevel")
        if pain is not None and (max_pain is None or pain > max_pain):
            max_pain = pain
            max_pain_pid = v["patientId"]
    for patient in state["patients"]:
        if patient["id"] == max_hr_pid and "Tachycardia-Screen" not in patient["tags"]:
            patient["tags"].append("Tachycardia-Screen")
            patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))
        if patient["id"] == max_pain_pid and "Pain-Management" not in patient["tags"]:
            patient["tags"].append("Pain-Management")
            patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))


def solve_task_h70(state):
    """Active ICD-10 'I*' → 'Cardio-Review'. Active ICD-10 'E*' → 'Metabolic-Review'."""
    cardio_pids = set()
    metabolic_pids = set()
    for prob in state["problems"]:
        if prob["status"] != "Active":
            continue
        icd = prob.get("icd10", "")
        if icd.startswith("I"):
            cardio_pids.add(prob["patientId"])
        if icd.startswith("E"):
            metabolic_pids.add(prob["patientId"])
    for patient in state["patients"]:
        pid = patient["id"]
        if pid in cardio_pids and "Cardio-Review" not in patient["tags"]:
            patient["tags"].append("Cardio-Review")
            patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))
        if pid in metabolic_pids and "Metabolic-Review" not in patient["tags"]:
            patient["tags"].append("Metabolic-Review")
            patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))


def solve_task_h71(state):
    """Duplicate Diabetes Management → 'Diabetes Annual Review' + billing 99395. Henderson note."""
    orig = find_template(state, "Diabetes Management")
    next_tmpl_id = state.get("_nextTemplateId", 100)
    dup = deepcopy(orig)
    dup["id"] = f"tmpl_{next_tmpl_id:03d}"
    dup["name"] = "Diabetes Annual Review"
    dup["createdAt"] = "2026-03-08T10:00:00Z"
    dup["billingItems"].append({
        "cptCode": "99395",
        "description": "Preventive visit, established, 40-64 years",
    })
    state["visitNoteTemplates"].append(dup)
    state["_nextTemplateId"] = next_tmpl_id + 1

    patient = find_patient(state, lastName="Henderson")
    annual_cat = find_category(state, "Annual Exam")
    next_note_id = state.get("_nextNoteId", 100)
    blocks = []
    for section in ["hpi", "ros", "pe", "assessment"]:
        if dup.get("content", {}).get(section):
            blocks.append({"type": section, "content": dup["content"][section]})
    note = {
        "id": f"note_{next_note_id:03d}",
        "patientId": patient["id"],
        "providerId": state["currentProvider"]["id"],
        "format": state["currentProvider"]["defaultNoteFormat"],
        "category": annual_cat["id"],
        "templateUsed": dup["id"],
        "date": "2026-03-08T10:00:00Z",
        "status": "draft",
        "signedAt": "",
        "reason": "",
        "blocks": blocks,
        "billingItems": deepcopy(dup.get("billingItems", [])),
        "documentTags": list(dup.get("documentTags", [])),
    }
    state["visitNotes"].append(note)
    state["_nextNoteId"] = next_note_id + 1


def solve_task_h72(state):
    """Patients with no vaccinations AND no vitals → 'Needs-Vitals' + 'Needs-Immunization'."""
    patients_with_vax = {v["patientId"] for v in state["vaccinations"]}
    patients_with_vitals = {v["patientId"] for v in state["vitals"]}
    for patient in state["patients"]:
        pid = patient["id"]
        if pid not in patients_with_vax and pid not in patients_with_vitals:
            for tag in ["Needs-Immunization", "Needs-Vitals"]:
                if tag not in patient["tags"]:
                    patient["tags"].append(tag)
            patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))


def solve_task_h73(state):
    """Default format → pre_op. New 'Pre-Surgical Screening' category. Procedure → new cat + Pre-Op template."""
    state["providerPreferences"]["defaultNoteFormat"] = "pre_op"
    next_cat_id = state.get("_nextCategoryId", 100)
    max_sort = max(c["sortOrder"] for c in state["visitNoteCategories"])
    cat_id = f"cat_{next_cat_id:03d}"
    cat = {
        "id": cat_id,
        "name": "Pre-Surgical Screening",
        "countForMIPS": True,
        "isDefault": False,
        "sortOrder": max_sort + 1,
    }
    state["visitNoteCategories"].append(cat)
    state["_nextCategoryId"] = next_cat_id + 1
    procedure = find_appointment_type(state, "Procedure")
    procedure["noteCategory"] = cat_id
    preop_tmpl = find_template(state, "Pre-Operative Evaluation")
    procedure["noteTemplate"] = preop_tmpl["id"]


def solve_task_h74(state):
    """Most-used template (tmpl_001, 2 notes) → duplicate as 'High-Volume Visit' → assign to Follow-Up."""
    from collections import Counter
    usage = Counter()
    for n in state["visitNotes"]:
        tmpl_used = n.get("templateUsed")
        if tmpl_used:
            usage[tmpl_used] += 1
    most_used_id = usage.most_common(1)[0][0]
    orig = next(t for t in state["visitNoteTemplates"] if t["id"] == most_used_id)
    next_id = state.get("_nextTemplateId", 100)
    dup = deepcopy(orig)
    dup["id"] = f"tmpl_{next_id:03d}"
    dup["name"] = "High-Volume Visit"
    dup["createdAt"] = "2026-03-08T10:00:00Z"
    state["visitNoteTemplates"].append(dup)
    state["_nextTemplateId"] = next_id + 1
    followup = find_appointment_type(state, "Follow-Up")
    followup["noteTemplate"] = dup["id"]


def solve_task_h75(state):
    """Patients with 'Pain' in problem title → 'Pain-Protocol' + visit note each."""
    pain_pids = set()
    for prob in state["problems"]:
        if "pain" in prob.get("title", "").lower():
            pain_pids.add(prob["patientId"])
    pf_tmpl = find_template(state, "E* Problem-Focused Visit")
    ov_cat = find_category(state, "Office Visit")
    for pid in pain_pids:
        patient = next(p for p in state["patients"] if p["id"] == pid)
        if "Pain-Protocol" not in patient["tags"]:
            patient["tags"].append("Pain-Protocol")
            patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))
        next_id = state.get("_nextNoteId", 100)
        blocks = []
        for section in ["hpi", "ros", "pe", "assessment"]:
            if pf_tmpl.get("content", {}).get(section):
                blocks.append({"type": section, "content": pf_tmpl["content"][section]})
        note = {
            "id": f"note_{next_id:03d}",
            "patientId": pid,
            "providerId": state["currentProvider"]["id"],
            "format": state["currentProvider"]["defaultNoteFormat"],
            "category": ov_cat["id"],
            "templateUsed": pf_tmpl["id"],
            "date": "2026-03-08T10:00:00Z",
            "status": "draft",
            "signedAt": "",
            "reason": "",
            "blocks": blocks,
            "billingItems": deepcopy(pf_tmpl.get("billingItems", [])),
            "documentTags": list(pf_tmpl.get("documentTags", [])),
        }
        state["visitNotes"].append(note)
        state["_nextNoteId"] = next_id + 1


def solve_task_h76(state):
    """Delete templates not created by current provider."""
    current_id = state["currentProvider"]["id"]
    state["visitNoteTemplates"] = [
        t for t in state["visitNoteTemplates"]
        if t.get("createdBy") == current_id
    ]


def solve_task_h77(state):
    """Patients with signed notes billing 99215 → 'High-Complexity-Visit'. Template with 99215 → 'High-Complexity' doc tag."""
    for note in state["visitNotes"]:
        if note.get("status") != "signed":
            continue
        has_99215 = any(b.get("cptCode") == "99215" for b in note.get("billingItems", []))
        if has_99215:
            patient = next(p for p in state["patients"] if p["id"] == note["patientId"])
            if "High-Complexity-Visit" not in patient["tags"]:
                patient["tags"].append("High-Complexity-Visit")
                patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))
    for tmpl in state["visitNoteTemplates"]:
        has_99215 = any(b.get("cptCode") == "99215" for b in tmpl.get("billingItems", []))
        if has_99215:
            if "High-Complexity" not in tmpl.get("documentTags", []):
                tmpl.setdefault("documentTags", []).append("High-Complexity")


def solve_task_h78(state):
    """Lowest O2 patient with care plan (O'Brien) → tag + signed Problem-Focused Urgent Visit note."""
    care_plan_pids = {cp["patientId"] for cp in state["carePlans"]}
    min_o2 = None
    min_o2_pid = None
    for v in state["vitals"]:
        o2 = v.get("oxygenSaturation")
        pid = v["patientId"]
        if o2 is not None and pid in care_plan_pids:
            if min_o2 is None or o2 < min_o2:
                min_o2 = o2
                min_o2_pid = pid
    patient = next(p for p in state["patients"] if p["id"] == min_o2_pid)
    if "Respiratory-Priority" not in patient["tags"]:
        patient["tags"].append("Respiratory-Priority")
        patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))
    tmpl = find_template(state, "E* Problem-Focused Visit")
    urgent_cat = find_category(state, "Urgent Visit")
    next_id = state.get("_nextNoteId", 100)
    blocks = []
    for section in ["hpi", "ros", "pe", "assessment"]:
        if tmpl.get("content", {}).get(section):
            blocks.append({"type": section, "content": tmpl["content"][section]})
    has_hpi = any(b["type"] == "hpi" for b in blocks)
    has_assessment = any(b["type"] == "assessment" for b in blocks)
    if not has_hpi:
        blocks.insert(0, {"type": "hpi", "content": "Patient presents with respiratory concerns."})
    if not has_assessment:
        blocks.append({"type": "assessment", "content": "Assessment and plan documented."})
    note = {
        "id": f"note_{next_id:03d}",
        "patientId": min_o2_pid,
        "providerId": state["currentProvider"]["id"],
        "format": state["currentProvider"]["defaultNoteFormat"],
        "category": urgent_cat["id"],
        "templateUsed": tmpl["id"],
        "date": "2026-03-08T10:00:00Z",
        "status": "signed",
        "signedAt": "2026-03-08T10:05:00Z",
        "reason": "",
        "blocks": blocks,
        "billingItems": deepcopy(tmpl.get("billingItems", [])),
        "documentTags": list(tmpl.get("documentTags", [])),
    }
    state["visitNotes"].append(note)
    state["_nextNoteId"] = next_id + 1


def solve_task_h79(state):
    """Create 'Comprehensive Review' cat, 'Full Review' template, configure Annual Exam, Zhao signed note."""
    # Create category
    next_cat_id = state.get("_nextCategoryId", 100)
    max_sort = max(c["sortOrder"] for c in state["visitNoteCategories"])
    cat_id = f"cat_{next_cat_id:03d}"
    cat = {
        "id": cat_id,
        "name": "Comprehensive Review",
        "countForMIPS": True,
        "isDefault": False,
        "sortOrder": max_sort + 1,
    }
    state["visitNoteCategories"].append(cat)
    state["_nextCategoryId"] = next_cat_id + 1

    # Create template
    next_tmpl_id = state.get("_nextTemplateId", 100)
    tmpl_id = f"tmpl_{next_tmpl_id:03d}"
    tmpl = {
        "id": tmpl_id,
        "name": "Full Review",
        "createdBy": state["currentProvider"]["id"],
        "content": {
            "hpi": "Patient presents for comprehensive review.",
            "ros": "Full review of systems documented.",
            "pe": "Comprehensive physical examination performed.",
            "assessment": "Assessment and plan documented below.",
        },
        "billingItems": [
            {"cptCode": "99215", "description": "Office visit, established, high complexity"}
        ],
        "pos": "",
        "billingNotes": "",
        "documentTags": [],
        "createdAt": "2026-03-08T10:00:00Z",
    }
    state["visitNoteTemplates"].append(tmpl)
    state["_nextTemplateId"] = next_tmpl_id + 1

    # Configure Annual Exam
    annual = find_appointment_type(state, "Annual Exam")
    annual["noteTemplate"] = tmpl_id
    annual["noteCategory"] = cat_id

    # Create Zhao note
    zhao = find_patient(state, lastName="Zhao")
    next_note_id = state.get("_nextNoteId", 100)
    blocks = [
        {"type": "hpi", "content": tmpl["content"]["hpi"]},
        {"type": "ros", "content": tmpl["content"]["ros"]},
        {"type": "pe", "content": tmpl["content"]["pe"]},
        {"type": "assessment", "content": tmpl["content"]["assessment"]},
    ]
    note = {
        "id": f"note_{next_note_id:03d}",
        "patientId": zhao["id"],
        "providerId": state["currentProvider"]["id"],
        "format": state["currentProvider"]["defaultNoteFormat"],
        "category": cat_id,
        "templateUsed": tmpl_id,
        "date": "2026-03-08T10:00:00Z",
        "status": "signed",
        "signedAt": "2026-03-08T10:05:00Z",
        "reason": "",
        "blocks": blocks,
        "billingItems": deepcopy(tmpl["billingItems"]),
        "documentTags": [],
    }
    state["visitNotes"].append(note)
    state["_nextNoteId"] = next_note_id + 1


def solve_task_h80(state):
    """Signed notes in >1 cat → 'Multi-Visit-Type'. 1 cat → 'Single-Visit-Type'."""
    from collections import defaultdict
    patient_cats = defaultdict(set)
    for note in state["visitNotes"]:
        if note.get("status") == "signed":
            patient_cats[note["patientId"]].add(note.get("category", ""))
    for patient in state["patients"]:
        pid = patient["id"]
        cats = patient_cats.get(pid, set())
        if len(cats) > 1:
            if "Multi-Visit-Type" not in patient["tags"]:
                patient["tags"].append("Multi-Visit-Type")
                patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))
        elif len(cats) == 1:
            if "Single-Visit-Type" not in patient["tags"]:
                patient["tags"].append("Single-Visit-Type")
                patient["tags"].sort(key=lambda t: (not t.startswith("*"), t))


# ── solver registry ──────────────────────────────────────────────────

SOLVERS = {}
for _prefix, _max in [("e", 20), ("m", 20), ("h", 80)]:
    for _i in range(1, _max + 1):
        _key = f"task_{_prefix}{_i}"
        _fn = f"solve_task_{_prefix}{_i}"
        if _fn in globals():
            SOLVERS[_key] = globals()[_fn]


# ── server management ────────────────────────────────────────────────

def generate_seed_state():
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
    resp = requests.put(
        f"{server_url}/api/state",
        json=seed_state,
        headers={"Content-Type": "application/json"},
    )
    if resp.status_code != 200:
        raise RuntimeError(f"Failed to seed server: HTTP {resp.status_code}")


def find_free_port(start=9600):
    port = start
    while port < start + 200:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("", port))
                return port
            except OSError:
                port += 1
    raise RuntimeError(f"No free port found in range {start}-{start+200}")


def start_server(port):
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
    if proc and proc.poll() is None:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()


# ── task runner ──────────────────────────────────────────────────────

def load_tasks():
    with open(TASKS_FILE) as f:
        return json.load(f)


def load_verifier(verify_path):
    full_path = APP_DIR / verify_path
    spec = importlib.util.spec_from_file_location("verifier", str(full_path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.verify


def run_single_task(task, server_url):
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
    parser = argparse.ArgumentParser(
        description="Elation Clinical Records real-task sanity check"
    )
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
