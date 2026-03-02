#!/usr/bin/env python3
"""
Sanity check for Clio Matters real-task verifiers.

For each task, directly constructs the expected end-state (bypassing the agent),
then runs the verifier and asserts it returns True. This confirms that verifiers
correctly recognize a solved task.

Usage:
    python3 sanity_check_real.py                      # All tasks, sequential
    python3 sanity_check_real.py --workers N           # N parallel environments
    python3 sanity_check_real.py --task-id task_e1     # Single task
    python3 sanity_check_real.py --port 9500           # Custom base port
"""
import argparse
import importlib.util
import json
import os
import signal
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from copy import deepcopy
from pathlib import Path

import requests

APP_DIR = Path(__file__).resolve().parent
TASKS_FILE = APP_DIR / "tasks.json"

NOW = "2026-03-02T12:00:00Z"
TODAY = "2026-03-02"

# ---------------------------------------------------------------------------
# Seed state loader (evaluates data.js via Node)
# ---------------------------------------------------------------------------
_SEED_STATE_JS = r"""
const fs = require('fs');
const vm = require('vm');
const code = fs.readFileSync(process.argv[1], 'utf8');
vm.runInThisContext(code);

function _maxIdNum(items) {
    return Math.max(...items.map(item => {
        const parts = String(item.id).split('_');
        return parseInt(parts[parts.length - 1], 10);
    }).filter(n => !isNaN(n)));
}

const state = {
    _seedVersion: SEED_DATA_VERSION,
    currentUser: JSON.parse(JSON.stringify(CURRENT_USER)),
    users: JSON.parse(JSON.stringify(USERS)),
    groups: JSON.parse(JSON.stringify(GROUPS)),
    contacts: JSON.parse(JSON.stringify(CONTACTS)),
    practiceAreas: JSON.parse(JSON.stringify(PRACTICE_AREAS)),
    customFieldDefinitions: JSON.parse(JSON.stringify(CUSTOM_FIELD_DEFINITIONS)),
    matterTemplates: JSON.parse(JSON.stringify(MATTER_TEMPLATES)),
    numberingScheme: JSON.parse(JSON.stringify(NUMBERING_SCHEME)),
    matters: JSON.parse(JSON.stringify(MATTERS)),
    damages: JSON.parse(JSON.stringify(DAMAGES)),
    medicalProviders: JSON.parse(JSON.stringify(MEDICAL_PROVIDERS)),
    medicalRecords: JSON.parse(JSON.stringify(MEDICAL_RECORDS)),
    medicalBills: JSON.parse(JSON.stringify(MEDICAL_BILLS)),
    settlements: JSON.parse(JSON.stringify(SETTLEMENTS)),
    timeEntries: JSON.parse(JSON.stringify(TIME_ENTRIES)),
    expenses: JSON.parse(JSON.stringify(EXPENSES)),
    activityLog: JSON.parse(JSON.stringify(ACTIVITY_LOG)),
    notificationSettings: JSON.parse(JSON.stringify(NOTIFICATION_SETTINGS)),
    firmSettings: JSON.parse(JSON.stringify(FIRM_SETTINGS)),
    deletedMatters: JSON.parse(JSON.stringify(DELETED_MATTERS)),
    expenseCategories: JSON.parse(JSON.stringify(EXPENSE_CATEGORIES)),
    currencies: JSON.parse(JSON.stringify(CURRENCIES)),
    relationshipTypes: JSON.parse(JSON.stringify(RELATIONSHIP_TYPES)),
    _nextMatterId: MATTERS.length > 0 ? _maxIdNum(MATTERS) + 1 : 121,
    _nextContactId: CONTACTS.length > 0 ? _maxIdNum(CONTACTS) + 1 : 61,
    _nextDamageId: DAMAGES.length > 0 ? _maxIdNum(DAMAGES) + 1 : 31,
    _nextMedicalProviderId: MEDICAL_PROVIDERS.length > 0 ? _maxIdNum(MEDICAL_PROVIDERS) + 1 : 9,
    _nextMedicalRecordId: MEDICAL_RECORDS.length > 0 ? _maxIdNum(MEDICAL_RECORDS) + 1 : 16,
    _nextMedicalBillId: MEDICAL_BILLS.length > 0 ? _maxIdNum(MEDICAL_BILLS) + 1 : 16,
    _nextTimeEntryId: TIME_ENTRIES.length > 0 ? _maxIdNum(TIME_ENTRIES) + 1 : 201,
    _nextExpenseId: EXPENSES.length > 0 ? _maxIdNum(EXPENSES) + 1 : 81,
    _nextLogId: ACTIVITY_LOG.length > 0 ? _maxIdNum(ACTIVITY_LOG) + 1 : 151,
    _nextFolderId: 500,
};
process.stdout.write(JSON.stringify(state));
"""


def generate_seed_state():
    data_js = str(APP_DIR / "js" / "data.js")
    result = subprocess.run(
        ["node", "-e", _SEED_STATE_JS, data_js],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print(f"ERROR: Failed to generate seed state:\n{result.stderr}", file=sys.stderr)
        sys.exit(1)
    return json.loads(result.stdout)


# ---------------------------------------------------------------------------
# Lookup helpers
# ---------------------------------------------------------------------------
def find_matter_by_desc(state, *keywords):
    """Find a matter whose description contains all keywords (case-insensitive)."""
    for m in state["matters"]:
        desc = (m.get("description") or "").lower()
        if all(kw.lower() in desc for kw in keywords):
            return m
    raise ValueError(f"Matter not found with keywords: {keywords}")


def find_matter_by_number(state, number):
    for m in state["matters"]:
        if m["number"] == number:
            return m
    raise ValueError(f"Matter not found: number={number!r}")


def find_matter_by_id(state, matter_id):
    for m in state["matters"]:
        if m["id"] == matter_id:
            return m
    raise ValueError(f"Matter not found: id={matter_id!r}")


def find_practice_area(state, name):
    for pa in state["practiceAreas"]:
        if pa["name"] == name:
            return pa
    raise ValueError(f"Practice area not found: {name!r}")


def find_template(state, name):
    for t in state["matterTemplates"]:
        if t["name"] == name:
            return t
    raise ValueError(f"Template not found: {name!r}")


def find_contact_by_name(state, name):
    for c in state["contacts"]:
        if name.lower() in (c.get("displayName") or "").lower():
            return c
    raise ValueError(f"Contact not found: {name!r}")


def find_user_by_name(state, name):
    for u in state["users"]:
        if name.lower() in u["name"].lower():
            return u
    raise ValueError(f"User not found: {name!r}")


def ensure_settlement(state, matter_id):
    if matter_id not in state["settlements"]:
        state["settlements"][matter_id] = {
            "recoveries": [],
            "legalFees": [],
            "nonMedicalLiens": [],
            "outstandingBalances": [],
        }
    return state["settlements"][matter_id]


def next_matter_id(state):
    mid = state.get("_nextMatterId", 121)
    state["_nextMatterId"] = mid + 1
    return mid


def next_damage_id(state):
    did = state.get("_nextDamageId", 39)
    state["_nextDamageId"] = did + 1
    return did


def next_provider_id(state):
    pid = state.get("_nextMedicalProviderId", 13)
    state["_nextMedicalProviderId"] = pid + 1
    return pid


# ---------------------------------------------------------------------------
# Solve functions — one per task
# ---------------------------------------------------------------------------

# ---- Easy ----

def solve_task_e1(state):
    """Close the Patterson bus accident case."""
    m = find_matter_by_desc(state, "Patterson", "Metro Transit")
    m["status"] = "closed"
    m["closedDate"] = TODAY


def solve_task_e2(state):
    """Reopen the Russo v. Lyft rideshare accident matter."""
    m = find_matter_by_desc(state, "Russo", "Lyft")
    m["status"] = "open"
    m["closedDate"] = None


def solve_task_e3(state):
    """Mark the Johnson v. Whole Foods case as pending."""
    m = find_matter_by_desc(state, "Johnson", "Whole Foods")
    m["status"] = "pending"
    m["pendingDate"] = TODAY


def solve_task_e4(state):
    """Turn off budget threshold notifications."""
    state["notificationSettings"]["budget_threshold"] = False


def solve_task_e5(state):
    """Change the matter numbering separator to a period."""
    state["numberingScheme"]["separator"] = "."


def solve_task_e6(state):
    """Set Criminal Defense - Misdemeanor template as default."""
    for t in state["matterTemplates"]:
        t["isDefault"] = (t["name"] == "Criminal Defense - Misdemeanor")


def solve_task_e7(state):
    """Delete the Estate Planning - Comprehensive template."""
    state["matterTemplates"] = [
        t for t in state["matterTemplates"]
        if t["name"] != "Estate Planning - Comprehensive"
    ]


def solve_task_e8(state):
    """Rename Corporate/Business to Business Law."""
    pa = find_practice_area(state, "Corporate/Business")
    pa["name"] = "Business Law"


def solve_task_e9(state):
    """Move Dimitriou dog bite matter to Investigation stage."""
    m = find_matter_by_desc(state, "Dimitriou", "dog bite")
    m["stageId"] = "stage_1_2"


def solve_task_e10(state):
    """Disable matter deletion notifications."""
    state["notificationSettings"]["matter_deletions"] = False


def solve_task_e11(state):
    """Change number padding to 6."""
    state["numberingScheme"]["numberPadding"] = 6


def solve_task_e12(state):
    """Delete the Closing stage from Real Estate."""
    pa = find_practice_area(state, "Real Estate")
    pa["stages"] = [s for s in pa["stages"] if s["name"] != "Closing"]
    for i, s in enumerate(pa["stages"]):
        s["order"] = i


def solve_task_e13(state):
    """Delete the Mills motorcycle collision matter."""
    m = find_matter_by_desc(state, "Mills", "Motorcycle")
    idx = next(i for i, x in enumerate(state["matters"]) if x["id"] == m["id"])
    matter = state["matters"].pop(idx)
    matter["deletedDate"] = NOW
    state["deletedMatters"].append(matter)


def solve_task_e14(state):
    """Recover the Smith consultation from recovery bin."""
    idx = None
    for i, dm in enumerate(state["deletedMatters"]):
        if "Smith Consultation" in dm.get("description", ""):
            idx = i
            break
    if idx is not None:
        matter = state["deletedMatters"].pop(idx)
        matter["status"] = "open"
        state["matters"].append(matter)


def solve_task_e15(state):
    """Add Appeals stage to Criminal Defense."""
    pa = find_practice_area(state, "Criminal Defense")
    pa["stages"].append({
        "id": f"stage_3_{len(pa['stages']) + 1}",
        "name": "Appeals",
        "order": len(pa["stages"]),
    })


def solve_task_e16(state):
    """Change firm default template to PI - Slip and Fall."""
    state["firmSettings"]["defaultTemplateId"] = "template_7"


def solve_task_e17(state):
    """Switch deduction order on Washington case to fees first."""
    m = find_matter_by_desc(state, "Washington", "Pacific Steel")
    if m.get("personalInjury") is None:
        m["personalInjury"] = {}
    m["personalInjury"]["deductionOrder"] = "fees_first"


def solve_task_e18(state):
    """Change Patterson case currency to British Pounds."""
    m = find_matter_by_desc(state, "Patterson", "Metro Transit")
    m["billing"]["currency"] = "GBP"


def solve_task_e19(state):
    """Reassign DeLuca felony DUI to Robert Jackson."""
    m = find_matter_by_desc(state, "DeLuca", "Felony DUI")
    m["responsibleAttorneyId"] = "user_8"


def solve_task_e20(state):
    """Rename Intake stage under Personal Injury to Case Intake."""
    pa = find_practice_area(state, "Personal Injury")
    for s in pa["stages"]:
        if s["id"] == "stage_1_1":
            s["name"] = "Case Intake"


# ---- Medium ----

def solve_task_m1(state):
    """Create Civil Rights practice area with 3 stages."""
    max_num = max(
        int(pa["id"].split("_")[1])
        for pa in state["practiceAreas"]
    )
    pa_id = f"pa_{max_num + 1}"
    state["practiceAreas"].append({
        "id": pa_id,
        "name": "Civil Rights",
        "stages": [
            {"id": f"stage_{max_num + 1}_1", "name": "Investigation", "order": 0},
            {"id": f"stage_{max_num + 1}_2", "name": "Filing", "order": 1},
            {"id": f"stage_{max_num + 1}_3", "name": "Resolution", "order": 2},
        ],
        "color": "#6366f1",
        "createdDate": NOW,
    })


def solve_task_m2(state):
    """Add $50,000 general damage to Johnson v. Whole Foods."""
    m = find_matter_by_desc(state, "Johnson", "Whole Foods")
    did = next_damage_id(state)
    state["damages"].append({
        "id": f"dmg_{did}",
        "matterId": m["id"],
        "name": "Pain and suffering",
        "amount": 50000,
        "type": "general",
        "date": None,
        "notes": "",
        "createdDate": NOW,
        "updatedDate": NOW,
    })


def solve_task_m3(state):
    """Change McCarthy responsible attorney to Marcus Williams and move to Litigation."""
    m = find_matter_by_desc(state, "McCarthy", "pedestrian")
    m["responsibleAttorneyId"] = "user_2"
    m["stageId"] = "stage_1_4"


def solve_task_m4(state):
    """Create Immigration - Work Visa template."""
    max_num = max(
        int(t["id"].split("_")[1])
        for t in state["matterTemplates"]
    )
    state["matterTemplates"].append({
        "id": f"template_{max_num + 1}",
        "name": "Immigration - Work Visa",
        "isDefault": False,
        "description": "Template for immigration work visa matters",
        "practiceAreaId": "pa_8",
        "billable": True,
        "billingMethod": "hourly",
        "deductionOrder": None,
        "customFields": {},
        "documentFolders": [],
        "createdDate": NOW,
    })


def solve_task_m5(state):
    """Add $250,000 recovery to Patterson settlement."""
    m = find_matter_by_desc(state, "Patterson", "Metro Transit")
    settlement = ensure_settlement(state, m["id"])
    next_id = len(settlement["recoveries"]) + 1
    settlement["recoveries"].append({
        "id": f"rec_{next_id}",
        "amount": 250000,
        "sourceContactId": "contact_58",
        "sourceName": "State Farm Insurance - Liens",
    })


def solve_task_m6(state):
    """Restrict Johnson v. Whole Foods permissions to Litigation Team."""
    m = find_matter_by_desc(state, "Johnson", "Whole Foods")
    m["permissions"] = {
        "type": "specific",
        "userIds": [],
        "groupIds": ["group_1"],
    }


def solve_task_m7(state):
    """Update numbering to slash separator and 6-digit padding."""
    state["numberingScheme"]["separator"] = "/"
    state["numberingScheme"]["numberPadding"] = 6


def solve_task_m8(state):
    """Add $15,000 non-medical lien from CalComp to Patterson settlement."""
    m = find_matter_by_desc(state, "Patterson", "Metro Transit")
    settlement = ensure_settlement(state, m["id"])
    next_id = len(settlement["nonMedicalLiens"]) + 1
    settlement["nonMedicalLiens"].append({
        "id": f"nml_{next_id}",
        "holderContactId": "contact_42",
        "description": "CalComp Workers Compensation lien",
        "amount": 15000,
        "reduction": 0,
    })


def solve_task_m9(state):
    """Add Dr. Michael Reeves Chiropractic as medical provider on Johnson case."""
    m = find_matter_by_desc(state, "Johnson", "Whole Foods")
    pid = next_provider_id(state)
    state["medicalProviders"].append({
        "id": f"mp_{pid}",
        "matterId": m["id"],
        "contactId": "contact_60",
        "description": "Post-surgical pain management",
        "firstTreatmentDate": None,
        "lastTreatmentDate": None,
        "treatmentComplete": False,
        "recordRequestDate": None,
        "recordFollowUpDate": None,
        "recordStatus": "not_requested",
        "billRequestDate": None,
        "billFollowUpDate": None,
        "billStatus": "not_requested",
    })


def solve_task_m10(state):
    """Close Baptiste contested divorce and set stage to Trial/Resolution."""
    m = find_matter_by_desc(state, "Baptiste", "Contested divorce")
    m["status"] = "closed"
    m["closedDate"] = TODAY
    m["stageId"] = "stage_2_5"


def solve_task_m11(state):
    """Remove all damages from Russo v. Lyft."""
    m = find_matter_by_desc(state, "Russo", "Lyft")
    state["damages"] = [d for d in state["damages"] if d["matterId"] != m["id"]]


def solve_task_m12(state):
    """Set custom fields on Doyle scaffolding case."""
    m = find_matter_by_desc(state, "Doyle", "scaffolding")
    m["customFields"]["cf_1"] = "SM-2025-PI-4421"
    m["customFields"]["cf_7"] = "Hon. Patricia Chen"


def solve_task_m13(state):
    """Create new Real Estate matter for Robert O'Malley."""
    mid = next_matter_id(state)
    number = str(mid).zfill(5)
    state["matters"].append({
        "id": f"matter_{mid}",
        "number": number,
        "displayNumber": f"{number}-OMalley",
        "description": "O'Malley Rental Property Dispute",
        "status": "open",
        "billingMethod": "flat_rate",
        "clientId": "contact_6",
        "responsibleAttorneyId": "user_13",
        "originatingAttorneyId": None,
        "responsibleStaffId": None,
        "clientReferenceNumber": "",
        "location": "",
        "practiceAreaId": "pa_4",
        "stageId": None,
        "openDate": TODAY,
        "pendingDate": None,
        "closedDate": None,
        "createdDate": NOW,
        "templateId": None,
        "permissions": {"type": "everyone", "userIds": [], "groupIds": []},
        "blockedUsers": [],
        "relationships": [],
        "customFields": {},
        "billing": {
            "billable": True, "method": "flat_rate", "currency": "USD",
            "rates": [], "budget": 0, "budgetUsed": 0, "trustBalance": 0,
            "minimumTrust": 0, "contingencyFee": None, "flatRate": None,
        },
        "personalInjury": None,
        "notifications": [],
        "documentFolders": [],
        "reports": {"useFirmSettings": True, "originatingPct": 50, "responsiblePct": 50},
        "deleted": False, "deletedAt": None,
    })


def solve_task_m14(state):
    """Add 33.33% contingency legal fee to Okafor burn case settlement."""
    m = find_matter_by_desc(state, "Okafor", "burn")
    settlement = ensure_settlement(state, m["id"])
    next_id = len(settlement["legalFees"]) + 1
    settlement["legalFees"].append({
        "id": f"lf_{next_id}",
        "recoveryId": None,
        "recipientId": "user_2",
        "rate": 33.33,
        "percentage": 33.33,
        "flatAmount": 0,
        "discount": 0,
        "referralFees": [],
    })


def solve_task_m15(state):
    """Block Priya Sharma from Blackwell divorce and restrict to Family Law Division."""
    m = find_matter_by_desc(state, "Blackwell", "Divorce", "High-asset")
    if "user_5" not in m.get("blockedUsers", []):
        m.setdefault("blockedUsers", []).append("user_5")
    m["permissions"] = {
        "type": "specific",
        "userIds": [],
        "groupIds": ["group_2"],
    }


def solve_task_m16(state):
    """Add State Farm Insurance as Insurance Adjuster on Doyle case."""
    m = find_matter_by_desc(state, "Doyle", "scaffolding")
    m.setdefault("relationships", []).append({
        "contactId": "contact_58",
        "relationship": "Insurance Adjuster",
        "billRecipient": False,
    })


def solve_task_m17(state):
    """Change Vertex Series B currency to GBP and budget to 100000."""
    m = find_matter_by_desc(state, "Vertex", "Series B")
    m["billing"]["currency"] = "GBP"
    m["billing"]["budget"] = 100000


def solve_task_m18(state):
    """Add $200,000 special damage to Sullivan-Wright case."""
    m = find_matter_by_desc(state, "Sullivan-Wright")
    did = next_damage_id(state)
    state["damages"].append({
        "id": f"dmg_{did}",
        "matterId": m["id"],
        "name": "Lost future earnings",
        "amount": 200000,
        "type": "special",
        "date": None,
        "notes": "",
        "createdDate": NOW,
        "updatedDate": NOW,
    })


def solve_task_m19(state):
    """Delete Plea Negotiation from Criminal Defense, rename Pre-Trial."""
    pa = find_practice_area(state, "Criminal Defense")
    pa["stages"] = [s for s in pa["stages"] if s["name"] != "Plea Negotiation"]
    for s in pa["stages"]:
        if s["name"] == "Pre-Trial":
            s["name"] = "Pre-Trial/Plea"
    for i, s in enumerate(pa["stages"]):
        s["order"] = i
    # Clear stageId for matters that were at the deleted stage
    for m in state["matters"]:
        if m["practiceAreaId"] == pa["id"] and m["stageId"] == "stage_3_3":
            m["stageId"] = None


def solve_task_m20(state):
    """Add $5,000 outstanding balance to Patterson settlement."""
    m = find_matter_by_desc(state, "Patterson", "Metro Transit")
    settlement = ensure_settlement(state, m["id"])
    next_id = len(settlement["outstandingBalances"]) + 1
    settlement["outstandingBalances"].append({
        "id": f"ob_{next_id}",
        "responsibility": "client",
        "holderContactId": "contact_57",
        "description": "Pacific Physical Therapy Center balance",
        "balanceOwing": 5000,
        "originalAmount": 5000,
        "reduction": 0,
    })


# ---- Hard ----

def solve_task_h1(state):
    """Close all open PI matters in the Demand stage."""
    for m in state["matters"]:
        if (m["practiceAreaId"] == "pa_1"
                and m["stageId"] == "stage_1_3"
                and m["status"] == "open"):
            m["status"] = "closed"
            m["closedDate"] = TODAY


def solve_task_h2(state):
    """Create new PI matter for Aisha Johnson with 40% contingency and $15,000 damage."""
    mid = next_matter_id(state)
    number = str(mid).zfill(5)
    matter_id = f"matter_{mid}"
    state["matters"].append({
        "id": matter_id,
        "number": number,
        "displayNumber": f"{number}-Johnson",
        "description": "Johnson v. Restaurant - Slip and fall at restaurant",
        "status": "open",
        "billingMethod": "contingency",
        "clientId": "contact_5",
        "responsibleAttorneyId": "user_2",
        "originatingAttorneyId": None,
        "responsibleStaffId": None,
        "clientReferenceNumber": "",
        "location": "",
        "practiceAreaId": "pa_1",
        "stageId": None,
        "openDate": TODAY,
        "pendingDate": None,
        "closedDate": None,
        "createdDate": NOW,
        "templateId": None,
        "permissions": {"type": "everyone", "userIds": [], "groupIds": []},
        "blockedUsers": [],
        "relationships": [],
        "customFields": {},
        "billing": {
            "billable": True, "method": "contingency", "currency": "USD",
            "rates": [], "budget": 0, "budgetUsed": 0, "trustBalance": 0,
            "minimumTrust": 0,
            "contingencyFee": {"userId": "user_2", "percentage": 40},
            "flatRate": None,
        },
        "personalInjury": {"deductionOrder": "fees_first"},
        "notifications": [],
        "documentFolders": [],
        "reports": {"useFirmSettings": True, "originatingPct": 50, "responsiblePct": 50},
        "deleted": False, "deletedAt": None,
    })
    did = next_damage_id(state)
    state["damages"].append({
        "id": f"dmg_{did}",
        "matterId": matter_id,
        "name": "Emergency room visit",
        "amount": 15000,
        "type": "special",
        "date": None,
        "notes": "",
        "createdDate": NOW,
        "updatedDate": NOW,
    })


def solve_task_h3(state):
    """Find PI matter with highest budget, change attorney to Diana Reyes."""
    pi_matters = [m for m in state["matters"] if m["practiceAreaId"] == "pa_1"]
    best = max(pi_matters, key=lambda m: m.get("billing", {}).get("budget", 0))
    best["responsibleAttorneyId"] = "user_3"


def solve_task_h4(state):
    """Set up Johnson v. Whole Foods settlement."""
    m = find_matter_by_desc(state, "Johnson", "Whole Foods")
    settlement = ensure_settlement(state, m["id"])
    settlement["recoveries"].append({
        "id": f"rec_{len(settlement['recoveries']) + 1}",
        "amount": 208650,
        "sourceContactId": None,
        "sourceName": "Hartford Insurance",
    })
    settlement["legalFees"].append({
        "id": f"lf_{len(settlement['legalFees']) + 1}",
        "recoveryId": None,
        "recipientId": "user_2",
        "rate": 33.33,
        "percentage": 33.33,
        "flatAmount": 0,
        "discount": 0,
        "referralFees": [],
    })
    settlement["nonMedicalLiens"].append({
        "id": f"nml_{len(settlement['nonMedicalLiens']) + 1}",
        "holderContactId": "contact_59",
        "description": "UCSF Medical Center lien",
        "amount": 14500,
        "reduction": 0,
    })


def solve_task_h5(state):
    """Create Appellate Law PA with 4 stages and template."""
    max_num = max(int(pa["id"].split("_")[1]) for pa in state["practiceAreas"])
    pa_id = f"pa_{max_num + 1}"
    state["practiceAreas"].append({
        "id": pa_id,
        "name": "Appellate Law",
        "stages": [
            {"id": f"stage_{max_num + 1}_1", "name": "Notice of Appeal", "order": 0},
            {"id": f"stage_{max_num + 1}_2", "name": "Briefing", "order": 1},
            {"id": f"stage_{max_num + 1}_3", "name": "Oral Argument", "order": 2},
            {"id": f"stage_{max_num + 1}_4", "name": "Decision", "order": 3},
        ],
        "color": "#6366f1",
        "createdDate": NOW,
    })
    max_t = max(int(t["id"].split("_")[1]) for t in state["matterTemplates"])
    state["matterTemplates"].append({
        "id": f"template_{max_t + 1}",
        "name": "Appellate Practice - Standard",
        "isDefault": False,
        "description": "Template for appellate matters",
        "practiceAreaId": pa_id,
        "billable": True,
        "billingMethod": "hourly",
        "deductionOrder": None,
        "customFields": {},
        "documentFolders": [],
        "createdDate": NOW,
    })


def solve_task_h6(state):
    """Transfer all Priya Sharma's matters to Kevin Nakamura."""
    for m in state["matters"]:
        if m["responsibleAttorneyId"] == "user_5":
            m["responsibleAttorneyId"] = "user_6"


def solve_task_h7(state):
    """Move all CD matters at Arraignment to Pre-Trial."""
    for m in state["matters"]:
        if m["practiceAreaId"] == "pa_3" and m["stageId"] == "stage_3_1":
            m["stageId"] = "stage_3_2"


def solve_task_h8(state):
    """Update numbering and create matter for Andrew Kim."""
    state["numberingScheme"]["prefix"] = "MLG"
    state["numberingScheme"]["separator"] = "/"
    state["numberingScheme"]["numberPadding"] = 6
    mid = next_matter_id(state)
    number = str(mid).zfill(6)
    state["matters"].append({
        "id": f"matter_{mid}",
        "number": number,
        "displayNumber": f"MLG/{number}-Kim",
        "description": "Kim Startup Formation",
        "status": "open",
        "billingMethod": "hourly",
        "clientId": "contact_43",
        "responsibleAttorneyId": "user_1",
        "originatingAttorneyId": None,
        "responsibleStaffId": None,
        "clientReferenceNumber": "",
        "location": "",
        "practiceAreaId": "pa_5",
        "stageId": None,
        "openDate": TODAY,
        "pendingDate": None,
        "closedDate": None,
        "createdDate": NOW,
        "templateId": None,
        "permissions": {"type": "everyone", "userIds": [], "groupIds": []},
        "blockedUsers": [],
        "relationships": [],
        "customFields": {},
        "billing": {
            "billable": True, "method": "hourly", "currency": "USD",
            "rates": [], "budget": 0, "budgetUsed": 0, "trustBalance": 0,
            "minimumTrust": 0, "contingencyFee": None, "flatRate": None,
        },
        "personalInjury": None,
        "notifications": [],
        "documentFolders": [],
        "reports": {"useFirmSettings": True, "originatingPct": 50, "responsiblePct": 50},
        "deleted": False, "deletedAt": None,
    })


def solve_task_h9(state):
    """Okafor burn case: add damage, legal fee, outstanding balance."""
    m = find_matter_by_desc(state, "Okafor", "burn")
    did = next_damage_id(state)
    state["damages"].append({
        "id": f"dmg_{did}",
        "matterId": m["id"],
        "name": "Future reconstructive surgery",
        "amount": 35000,
        "type": "special",
        "date": None,
        "notes": "",
        "createdDate": NOW,
        "updatedDate": NOW,
    })
    settlement = ensure_settlement(state, m["id"])
    settlement["legalFees"].append({
        "id": f"lf_{len(settlement['legalFees']) + 1}",
        "recoveryId": None,
        "recipientId": "user_2",
        "rate": 40,
        "percentage": 40,
        "flatAmount": 0,
        "discount": 0,
        "referralFees": [],
    })
    settlement["outstandingBalances"].append({
        "id": f"ob_{len(settlement['outstandingBalances']) + 1}",
        "responsibility": "client",
        "holderContactId": None,
        "description": "Outstanding balance",
        "balanceOwing": 8000,
        "originalAmount": 8000,
        "reduction": 0,
    })


def solve_task_h10(state):
    """Close pending FL matters, move open FL consultation to Filing."""
    for m in state["matters"]:
        if m["practiceAreaId"] == "pa_2" and m["status"] == "pending":
            m["status"] = "closed"
            m["closedDate"] = TODAY
    for m in state["matters"]:
        if (m["practiceAreaId"] == "pa_2"
                and m["status"] == "open"
                and m["stageId"] == "stage_2_1"):
            m["stageId"] = "stage_2_2"


def solve_task_h11(state):
    """Set up McCarthy pedestrian settlement."""
    m = find_matter_by_desc(state, "McCarthy", "pedestrian")
    settlement = ensure_settlement(state, m["id"])
    settlement["recoveries"].append({
        "id": f"rec_{len(settlement['recoveries']) + 1}",
        "amount": 150000,
        "sourceContactId": None,
        "sourceName": "City of San Francisco",
    })
    settlement["legalFees"].append({
        "id": f"lf_{len(settlement['legalFees']) + 1}",
        "recoveryId": None,
        "recipientId": "user_8",
        "rate": 33.33,
        "percentage": 33.33,
        "flatAmount": 0,
        "discount": 0,
        "referralFees": [],
    })
    settlement["outstandingBalances"].append({
        "id": f"ob_{len(settlement['outstandingBalances']) + 1}",
        "responsibility": "client",
        "holderContactId": "contact_56",
        "description": "Bay Area Orthopedic Associates",
        "balanceOwing": 25000,
        "originalAmount": 25000,
        "reduction": 0,
    })


def solve_task_h12(state):
    """Reassign Robert Jackson's open PI matters to Marcus Williams."""
    for m in state["matters"]:
        if (m["practiceAreaId"] == "pa_1"
                and m["status"] == "open"
                and m["responsibleAttorneyId"] == "user_8"):
            m["responsibleAttorneyId"] = "user_2"


def solve_task_h13(state):
    """Create two new matters: FL for Baptiste, CD for Hernandez."""
    mid1 = next_matter_id(state)
    number1 = str(mid1).zfill(5)
    state["matters"].append({
        "id": f"matter_{mid1}",
        "number": number1,
        "displayNumber": f"{number1}-Baptiste",
        "description": "Baptiste Family Law Matter",
        "status": "open",
        "billingMethod": "hourly",
        "clientId": "contact_62",
        "responsibleAttorneyId": "user_3",
        "originatingAttorneyId": None,
        "responsibleStaffId": None,
        "clientReferenceNumber": "",
        "location": "",
        "practiceAreaId": "pa_2",
        "stageId": None,
        "openDate": TODAY,
        "pendingDate": None,
        "closedDate": None,
        "createdDate": NOW,
        "templateId": None,
        "permissions": {"type": "everyone", "userIds": [], "groupIds": []},
        "blockedUsers": [],
        "relationships": [],
        "customFields": {},
        "billing": {
            "billable": True, "method": "hourly", "currency": "USD",
            "rates": [], "budget": 0, "budgetUsed": 0, "trustBalance": 0,
            "minimumTrust": 0, "contingencyFee": None, "flatRate": None,
        },
        "personalInjury": None,
        "notifications": [],
        "documentFolders": [],
        "reports": {"useFirmSettings": True, "originatingPct": 50, "responsiblePct": 50},
        "deleted": False, "deletedAt": None,
    })
    mid2 = next_matter_id(state)
    number2 = str(mid2).zfill(5)
    state["matters"].append({
        "id": f"matter_{mid2}",
        "number": number2,
        "displayNumber": f"{number2}-Hernandez",
        "description": "People v. Hernandez - Criminal Defense",
        "status": "open",
        "billingMethod": "flat_rate",
        "clientId": "contact_29",
        "responsibleAttorneyId": "user_8",
        "originatingAttorneyId": None,
        "responsibleStaffId": None,
        "clientReferenceNumber": "",
        "location": "",
        "practiceAreaId": "pa_3",
        "stageId": None,
        "openDate": TODAY,
        "pendingDate": None,
        "closedDate": None,
        "createdDate": NOW,
        "templateId": None,
        "permissions": {"type": "everyone", "userIds": [], "groupIds": []},
        "blockedUsers": [],
        "relationships": [],
        "customFields": {},
        "billing": {
            "billable": True, "method": "flat_rate", "currency": "USD",
            "rates": [], "budget": 0, "budgetUsed": 0, "trustBalance": 0,
            "minimumTrust": 0, "contingencyFee": None, "flatRate": None,
        },
        "personalInjury": None,
        "notifications": [],
        "documentFolders": [],
        "reports": {"useFirmSettings": True, "originatingPct": 50, "responsiblePct": 50},
        "deleted": False, "deletedAt": None,
    })


def solve_task_h14(state):
    """DeLuca arraignment case: flat rate $15,000, move to Pre-Trial."""
    m = find_matter_by_desc(state, "DeLuca", "Felony DUI")
    m["billingMethod"] = "flat_rate"
    m["billing"]["method"] = "flat_rate"
    m["billing"]["flatRate"] = {"amount": 15000, "userId": m["responsibleAttorneyId"]}
    m["stageId"] = "stage_3_2"


def solve_task_h15(state):
    """Add UCSF Medical Center and Meridian Radiology as providers on McCarthy case."""
    m = find_matter_by_desc(state, "McCarthy", "pedestrian")
    pid1 = next_provider_id(state)
    state["medicalProviders"].append({
        "id": f"mp_{pid1}",
        "matterId": m["id"],
        "contactId": "contact_59",
        "description": "UCSF Medical Center treatment",
        "firstTreatmentDate": None,
        "lastTreatmentDate": None,
        "treatmentComplete": False,
        "recordRequestDate": None,
        "recordFollowUpDate": None,
        "recordStatus": "not_requested",
        "billRequestDate": None,
        "billFollowUpDate": None,
        "billStatus": "not_requested",
    })
    pid2 = next_provider_id(state)
    state["medicalProviders"].append({
        "id": f"mp_{pid2}",
        "matterId": m["id"],
        "contactId": "contact_66",
        "description": "Meridian Radiology Associates imaging",
        "firstTreatmentDate": None,
        "lastTreatmentDate": None,
        "treatmentComplete": False,
        "recordRequestDate": None,
        "recordFollowUpDate": None,
        "recordStatus": "not_requested",
        "billRequestDate": None,
        "billFollowUpDate": None,
        "billStatus": "not_requested",
    })


def solve_task_h16(state):
    """Delete PI - Slip and Fall template, create PI - Premises Liability."""
    state["matterTemplates"] = [
        t for t in state["matterTemplates"]
        if t["name"] != "Personal Injury - Slip and Fall"
    ]
    max_num = max(
        int(t["id"].split("_")[1])
        for t in state["matterTemplates"]
    )
    state["matterTemplates"].append({
        "id": f"template_{max_num + 1}",
        "name": "Personal Injury - Premises Liability",
        "isDefault": False,
        "description": "Template for premises liability cases",
        "practiceAreaId": "pa_1",
        "billable": True,
        "billingMethod": "contingency",
        "deductionOrder": "fees_first",
        "customFields": {},
        "documentFolders": [],
        "createdDate": NOW,
    })


def solve_task_h17(state):
    """Washington case: 35% contingency, $120K recovery, Settlement/Trial stage."""
    m = find_matter_by_desc(state, "Washington", "Pacific Steel")
    m["billing"]["contingencyFee"]["percentage"] = 35
    settlement = ensure_settlement(state, m["id"])
    settlement["recoveries"].append({
        "id": f"rec_{len(settlement['recoveries']) + 1}",
        "amount": 120000,
        "sourceContactId": "contact_42",
        "sourceName": "CalComp Workers Compensation",
    })
    m["stageId"] = "stage_1_5"


def solve_task_h18(state):
    """Create Appellate Practice PA with 3 stages, move Hernandez armed robbery."""
    max_num = max(int(pa["id"].split("_")[1]) for pa in state["practiceAreas"])
    pa_id = f"pa_{max_num + 1}"
    state["practiceAreas"].append({
        "id": pa_id,
        "name": "Appellate Practice",
        "stages": [
            {"id": f"stage_{max_num + 1}_1", "name": "Notice of Appeal", "order": 0},
            {"id": f"stage_{max_num + 1}_2", "name": "Brief Writing", "order": 1},
            {"id": f"stage_{max_num + 1}_3", "name": "Oral Argument", "order": 2},
        ],
        "color": "#6366f1",
        "createdDate": NOW,
    })
    m = find_matter_by_desc(state, "Hernandez", "armed robbery")
    m["practiceAreaId"] = pa_id


def solve_task_h19(state):
    """Add 3 damages to Brennan hotel slip-and-fall."""
    m = find_matter_by_desc(state, "Brennan", "Oceanview")
    for name, amount, dtype in [
        ("Emergency room visit", 8500, "special"),
        ("Wrist surgery", 12000, "special"),
        ("Pain and suffering", 45000, "general"),
    ]:
        did = next_damage_id(state)
        state["damages"].append({
            "id": f"dmg_{did}",
            "matterId": m["id"],
            "name": name,
            "amount": amount,
            "type": dtype,
            "date": None,
            "notes": "",
            "createdDate": NOW,
            "updatedDate": NOW,
        })


def solve_task_h20(state):
    """Set up Fitzgerald medical malpractice settlement."""
    m = find_matter_by_desc(state, "Fitzgerald", "Misdiagnosis")
    settlement = ensure_settlement(state, m["id"])
    settlement["recoveries"].append({
        "id": f"rec_{len(settlement['recoveries']) + 1}",
        "amount": 375000,
        "sourceContactId": None,
        "sourceName": "Settlement",
    })
    settlement["legalFees"].append({
        "id": f"lf_{len(settlement['legalFees']) + 1}",
        "recoveryId": None,
        "recipientId": "user_8",
        "rate": 40,
        "percentage": 40,
        "flatAmount": 0,
        "discount": 0,
        "referralFees": [],
    })
    settlement["nonMedicalLiens"].append({
        "id": f"nml_{len(settlement['nonMedicalLiens']) + 1}",
        "holderContactId": None,
        "description": "Health insurance subrogation lien",
        "amount": 20000,
        "reduction": 0,
    })
    settlement["outstandingBalances"].append({
        "id": f"ob_{len(settlement['outstandingBalances']) + 1}",
        "responsibility": "client",
        "holderContactId": None,
        "description": "Follow-up care balance",
        "balanceOwing": 5000,
        "originalAmount": 5000,
        "reduction": 0,
    })


# ---------------------------------------------------------------------------
# SOLVERS dispatch map
# ---------------------------------------------------------------------------
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
}


# ---------------------------------------------------------------------------
# Server management
# ---------------------------------------------------------------------------
def kill_port(port):
    try:
        result = subprocess.run(
            ["lsof", "-ti", f":{port}"],
            capture_output=True, text=True,
        )
        for pid in result.stdout.strip().split("\n"):
            if pid:
                os.kill(int(pid), signal.SIGKILL)
    except Exception:
        pass


def start_server(port):
    kill_port(port)
    proc = subprocess.Popen(
        [sys.executable, "server.py", "--port", str(port)],
        cwd=str(APP_DIR),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return proc


def wait_for_server(port, timeout=10):
    url = f"http://localhost:{port}/api/state"
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            r = requests.get(url, timeout=1)
            if r.status_code in (200, 404):
                return True
        except requests.ConnectionError:
            pass
        time.sleep(0.2)
    return False


def stop_server(proc):
    if proc and proc.poll() is None:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait()


# ---------------------------------------------------------------------------
# Verifier loader
# ---------------------------------------------------------------------------
def load_verifier(task):
    path = str(APP_DIR / task["verify"])
    spec = importlib.util.spec_from_file_location(task["id"], path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.verify


# ---------------------------------------------------------------------------
# Task runner
# ---------------------------------------------------------------------------
def run_single_task(task, server_url, seed_state):
    task_id = task["id"]
    solver = SOLVERS.get(task_id)
    if not solver:
        return task_id, False, f"No solver for {task_id}"

    # 1. Reset via POST /api/reset
    try:
        requests.post(f"{server_url}/api/reset", timeout=5)
        time.sleep(0.3)
    except Exception as e:
        return task_id, False, f"Reset failed: {e}"

    # 2. Seed the server
    state = deepcopy(seed_state)
    try:
        requests.put(
            f"{server_url}/api/state",
            json=state,
            headers={"Content-Type": "application/json"},
            timeout=5,
        )
    except Exception as e:
        return task_id, False, f"Seed failed: {e}"

    # 3. Apply solve
    try:
        solver(state)
    except Exception as e:
        return task_id, False, f"Solve error: {e}"

    # 4. Push solved state
    try:
        requests.put(
            f"{server_url}/api/state",
            json=state,
            headers={"Content-Type": "application/json"},
            timeout=5,
        )
    except Exception as e:
        return task_id, False, f"Push state failed: {e}"

    # 5. Run verifier
    try:
        verify_fn = load_verifier(task)
        passed, message = verify_fn(server_url)
    except Exception as e:
        return task_id, False, f"Verifier exception: {e}"

    return task_id, passed, message


def run_tasks_sequential(tasks, port, seed_state):
    proc = start_server(port)
    if not wait_for_server(port):
        stop_server(proc)
        print(f"FATAL: Server on port {port} did not start.", file=sys.stderr)
        sys.exit(1)

    server_url = f"http://localhost:{port}"

    # Seed initial state so server has _seed_state
    requests.put(
        f"{server_url}/api/state",
        json=seed_state,
        headers={"Content-Type": "application/json"},
        timeout=5,
    )

    results = []
    for task in tasks:
        tid, passed, msg = run_single_task(task, server_url, seed_state)
        status = "\033[92m  PASS\033[0m" if passed else "\033[91m  FAIL\033[0m"
        print(f"{status}  {tid:12s}  {msg}")
        results.append((tid, passed, msg))

    stop_server(proc)
    return results


def run_tasks_parallel(tasks, workers, base_port, seed_state):
    results = []

    def worker_fn(worker_tasks, port):
        proc = start_server(port)
        if not wait_for_server(port):
            stop_server(proc)
            return [(t["id"], False, "Server failed to start") for t in worker_tasks]

        server_url = f"http://localhost:{port}"
        requests.put(
            f"{server_url}/api/state",
            json=seed_state,
            headers={"Content-Type": "application/json"},
            timeout=5,
        )

        worker_results = []
        for task in worker_tasks:
            tid, passed, msg = run_single_task(task, server_url, seed_state)
            worker_results.append((tid, passed, msg))
        stop_server(proc)
        return worker_results

    # Partition tasks across workers
    partitions = [[] for _ in range(workers)]
    for i, task in enumerate(tasks):
        partitions[i % workers].append(task)

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {}
        for w, partition in enumerate(partitions):
            if partition:
                f = executor.submit(worker_fn, partition, base_port + w)
                futures[f] = w

        for f in as_completed(futures):
            for tid, passed, msg in f.result():
                status = "\033[92m  PASS\033[0m" if passed else "\033[91m  FAIL\033[0m"
                print(f"{status}  {tid:12s}  {msg}")
                results.append((tid, passed, msg))

    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Sanity check for Clio Matters real tasks")
    parser.add_argument("--task-id", help="Run a single task by ID")
    parser.add_argument("--workers", type=int, default=1, help="Number of parallel workers")
    parser.add_argument("--port", type=int, default=9500, help="Base port for servers")
    args = parser.parse_args()

    # Load tasks
    with open(TASKS_FILE) as f:
        tasks = json.load(f)

    if args.task_id:
        tasks = [t for t in tasks if t["id"] == args.task_id]
        if not tasks:
            print(f"ERROR: Task {args.task_id!r} not found.", file=sys.stderr)
            sys.exit(1)

    # Generate seed state
    print("Generating seed state from data.js...")
    seed_state = generate_seed_state()
    print(f"Seed state loaded: {len(seed_state['matters'])} matters, "
          f"{len(seed_state['damages'])} damages, "
          f"{len(seed_state['medicalProviders'])} providers\n")

    # Run tasks
    if args.workers > 1 and len(tasks) > 1:
        results = run_tasks_parallel(tasks, args.workers, args.port, seed_state)
    else:
        results = run_tasks_sequential(tasks, args.port, seed_state)

    # Summary
    passed = sum(1 for _, p, _ in results if p)
    total = len(results)
    failed = [(tid, msg) for tid, p, msg in results if not p]

    print(f"\n{passed}/{total} passed")
    if failed:
        print("Failed:")
        for tid, msg in failed:
            print(f"  {tid}: {msg}")
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
