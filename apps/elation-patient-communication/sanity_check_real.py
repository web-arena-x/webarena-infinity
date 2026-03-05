#!/usr/bin/env python3
"""
Sanity check for Elation Patient Communication real-task verifiers.

For each task, directly applies the expected end-state (bypassing the agent),
then runs the verifier and asserts it passes.

Usage:
    python3 sanity_check_real.py                     # All tasks, sequential
    python3 sanity_check_real.py --workers N          # N parallel environments
    python3 sanity_check_real.py --task-id task_e5    # Single task
    python3 sanity_check_real.py --port 9000          # Custom base port
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
_SEED_STATE_JS = """
const fs = require('fs');
const vm = require('vm');
const code = fs.readFileSync(process.argv[1], 'utf8');
vm.runInThisContext(code);

// Replicate what AppState._loadSeedData() does
const state = {
    _seedVersion: SEED_DATA_VERSION,
    currentUser: JSON.parse(JSON.stringify(CURRENT_USER)),
    providers: JSON.parse(JSON.stringify(PROVIDERS)),
    userGroups: JSON.parse(JSON.stringify(USER_GROUPS)),
    patients: JSON.parse(JSON.stringify(PATIENTS)),
    patientLetters: JSON.parse(JSON.stringify(PATIENT_LETTERS)),
    appointments: JSON.parse(JSON.stringify(APPOINTMENTS)),
    reminders: JSON.parse(JSON.stringify(REMINDERS)),
    bulkLetters: JSON.parse(JSON.stringify(BULK_LETTERS)),
    visitSummaries: JSON.parse(JSON.stringify(VISIT_SUMMARIES)),
    practiceSettings: JSON.parse(JSON.stringify(PRACTICE_SETTINGS)),
    messageRouting: JSON.parse(JSON.stringify(MESSAGE_ROUTING)),
    messageCategories: [...MESSAGE_CATEGORIES],
    patientTags: [...PATIENT_TAGS],
    sharingLevels: JSON.parse(JSON.stringify(SHARING_LEVELS)),
    notificationTimeframes: JSON.parse(JSON.stringify(NOTIFICATION_TIMEFRAMES)),
    _nextPatientId: INITIAL_COUNTERS._nextPatientId,
    _nextLetterId: INITIAL_COUNTERS._nextLetterId,
    _nextConversationId: INITIAL_COUNTERS._nextConversationId,
    _nextAppointmentId: INITIAL_COUNTERS._nextAppointmentId,
    _nextReminderId: INITIAL_COUNTERS._nextReminderId,
    _nextBulkLetterId: INITIAL_COUNTERS._nextBulkLetterId,
    _nextVisitSummaryId: INITIAL_COUNTERS._nextVisitSummaryId,
    _nextLocationId: INITIAL_COUNTERS._nextLocationId,
    _nextCptCodeId: INITIAL_COUNTERS._nextCptCodeId,
};
process.stdout.write(JSON.stringify(state));
"""


# ── helpers ──────────────────────────────────────────────────────────

def find_entity(entities, **kwargs):
    for e in entities:
        if all(e.get(k) == v for k, v in kwargs.items()):
            return e
    raise ValueError(f"Entity not found: {kwargs}")


def find_patient_by_name(state, first, last):
    return find_entity(state["patients"], firstName=first, lastName=last)


def find_provider(state, provider_id):
    return find_entity(state["providers"], id=provider_id)


def find_letter(state, letter_id):
    return find_entity(state["patientLetters"], id=letter_id)


def find_reminder(state, reminder_id):
    return find_entity(state["reminders"], id=reminder_id)


def find_appointment(state, appt_id):
    return find_entity(state["appointments"], id=appt_id)


def next_letter_id(state):
    lid = state["_nextLetterId"]
    state["_nextLetterId"] = lid + 1
    return f"ltr_{lid}"


def next_conversation_id(state):
    cid = state["_nextConversationId"]
    state["_nextConversationId"] = cid + 1
    return f"conv_{cid}"


def next_appointment_id(state):
    aid = state["_nextAppointmentId"]
    state["_nextAppointmentId"] = aid + 1
    return f"appt_{aid}"


def next_bulk_letter_id(state):
    bid = state["_nextBulkLetterId"]
    state["_nextBulkLetterId"] = bid + 1
    return f"bulk_{bid}"


def next_location_id(state):
    lid = state["_nextLocationId"]
    state["_nextLocationId"] = lid + 1
    return f"loc_{lid}"


TIMESTAMP = "2026-03-02T12:00:00Z"

MESSAGE_CATEGORIES = [
    "General Question", "Prescription Refill", "Appointment Request",
    "Test Results", "Billing Question", "Referral Request",
    "Medical Records Request", "Other",
]


# ── solve functions ──────────────────────────────────────────────────

# ---- Easy ----

def solve_task_e1(state):
    """Mark Emily Thompson's dizziness message as read."""
    letter = find_letter(state, "ltr_4")
    letter["isRead"] = True
    letter["readAt"] = TIMESTAMP


def solve_task_e2(state):
    """Acknowledge Aisha Patel's appointment reminder."""
    reminder = find_reminder(state, "rem_4")
    reminder["acknowledged"] = True


def solve_task_e3(state):
    """Tag James Rodriguez as VIP."""
    patient = find_entity(state["patients"], id="pat_1")
    if "VIP" not in patient["tags"]:
        patient["tags"].append("VIP")


def solve_task_e4(state):
    """Remove 'New Patient' tag from Emily Thompson."""
    patient = find_entity(state["patients"], id="pat_2")
    patient["tags"] = [t for t in patient["tags"] if t != "New Patient"]


def solve_task_e5(state):
    """Cancel Sophia Nguyen's telehealth appointment."""
    appt = find_appointment(state, "appt_2")
    appt["status"] = "cancelled"


def solve_task_e6(state):
    """End conversation with Howard Blackwell about pacemaker."""
    for letter in state["patientLetters"]:
        if letter["conversationId"] == "conv_24":
            letter["conversationState"] = "ended"


def solve_task_e7(state):
    """Delete the draft letter to Martha Reeves-Whitfield."""
    state["patientLetters"] = [l for l in state["patientLetters"] if l["id"] != "ltr_35"]


def solve_task_e8(state):
    """Turn off booking site auto-invite."""
    state["practiceSettings"]["bookingSiteAutoInvite"] = False


def solve_task_e9(state):
    """Disable waiting room audio notification."""
    state["practiceSettings"]["videoSettings"]["waitingRoomAudioNotification"] = False


def solve_task_e10(state):
    """Remove CPT code 99423."""
    state["practiceSettings"]["cptCodes"] = [
        c for c in state["practiceSettings"]["cptCodes"]
        if c["code"] != "99423"
    ]


def solve_task_e11(state):
    """Mark Priya Sharma's medical records message as read."""
    letter = find_letter(state, "ltr_19")
    letter["isRead"] = True
    letter["readAt"] = TIMESTAMP


def solve_task_e12(state):
    """Acknowledge Marcus Johnson's Passport reminder."""
    reminder = find_reminder(state, "rem_7")
    reminder["acknowledged"] = True


def solve_task_e13(state):
    """Add 'High Risk' tag to Janet Okonkwo."""
    patient = find_entity(state["patients"], id="pat_30")
    if "High Risk" not in patient["tags"]:
        patient["tags"].append("High Risk")


def solve_task_e14(state):
    """Remove East Bay Clinic location."""
    state["practiceSettings"]["practiceLocations"] = [
        loc for loc in state["practiceSettings"]["practiceLocations"]
        if loc["name"] != "East Bay Clinic"
    ]


def solve_task_e15(state):
    """Deactivate telehealth for Dr. Kim."""
    provider = find_provider(state, "prov_4")
    provider["virtualVisitActivated"] = False


def solve_task_e16(state):
    """Change notification timeframe to 72 hours."""
    provider = find_provider(state, "prov_1")
    provider["notificationTimeframe"] = "72_hours"


def solve_task_e17(state):
    """Disable patient messaging."""
    state["practiceSettings"]["allowPatientMessaging"] = False


def solve_task_e18(state):
    """Mark Andrew McIntyre's acid reflux message as read."""
    letter = find_letter(state, "ltr_23")
    letter["isRead"] = True
    letter["readAt"] = TIMESTAMP


def solve_task_e19(state):
    """Set sharing default to level 4."""
    provider = find_provider(state, "prov_1")
    provider["sharingDefault"] = 4


def solve_task_e20(state):
    """Acknowledge Martha Reeves-Whitfield's appointment reminder."""
    reminder = find_reminder(state, "rem_5")
    reminder["acknowledged"] = True


# ---- Medium ----

def solve_task_m1(state):
    """Invite Anthony Petrov to Passport."""
    patient = find_entity(state["patients"], id="pat_9")
    patient["passportStatus"] = "invited"
    patient["invitedAt"] = TIMESTAMP
    patient["invitationCode"] = "9999999"


def solve_task_m2(state):
    """Reply to James Rodriguez about Lisinopril."""
    state["patientLetters"].append({
        "id": next_letter_id(state),
        "patientId": "pat_1",
        "conversationId": "conv_1",
        "direction": "to_patient",
        "subject": "Re: Prescription Refill",
        "body": "Yes, I will also send a refill for your Lisinopril along with your Metformin.",
        "category": None,
        "senderId": "prov_1",
        "senderType": "provider",
        "attachments": [],
        "postDate": None,
        "sentAt": TIMESTAMP,
        "readAt": None,
        "isRead": False,
        "isDraft": False,
        "conversationState": "open",
        "doNotAllowResponse": False,
        "unreadAlertTimeframe": "none",
        "printHeader": "default",
    })


def solve_task_m3(state):
    """Schedule in-person appointment for Emily Thompson."""
    state["appointments"].append({
        "id": next_appointment_id(state),
        "patientId": "pat_2",
        "providerId": "prov_1",
        "date": "2026-03-15T14:00:00Z",
        "place": "in_person",
        "status": "scheduled",
        "virtualVisitInstructions": None,
        "reason": "Annual physical",
    })


def solve_task_m4(state):
    """Upgrade Helen Matsumoto's sharing to level 4."""
    patient = find_entity(state["patients"], id="pat_10")
    patient["passportSharingLevel"] = 4


def solve_task_m5(state):
    """Add South Bay Clinic location."""
    state["practiceSettings"]["practiceLocations"].append({
        "id": next_location_id(state),
        "name": "South Bay Clinic",
        "address": "850 Stevens Creek Blvd, San Jose, CA 95128",
        "posCode": "11",
        "posDescription": "Office",
    })


def solve_task_m6(state):
    """Add CPT code 99215."""
    state["practiceSettings"]["cptCodes"].append({
        "code": "99215",
        "description": "Office visit, established patient, high complexity",
    })


def solve_task_m7(state):
    """Send the draft to Martha Reeves-Whitfield."""
    letter = find_letter(state, "ltr_35")
    letter["isDraft"] = False
    letter["sentAt"] = TIMESTAMP


def solve_task_m8(state):
    """Enable telehealth for Jessica Okafor."""
    provider = find_provider(state, "prov_3")
    provider["virtualVisitActivated"] = True
    provider["virtualVisitInstructions"] = (
        "Join your virtual visit at https://zoom.us/j/1234567890. "
        "Please have your insurance card ready."
    )


def solve_task_m9(state):
    """Tag Raymond Copeland with Chronic Care and Diabetes Management."""
    patient = find_entity(state["patients"], id="pat_35")
    for tag in ["Chronic Care", "Diabetes Management"]:
        if tag not in patient["tags"]:
            patient["tags"].append(tag)


def solve_task_m10(state):
    """Add Clinical Team to Torres Prescription Refill routing."""
    routing = state["messageRouting"]["prov_2"]["Prescription Refill"]
    if "ug_2" not in routing:
        routing.append("ug_2")


def solve_task_m11(state):
    """Send letter to David Park about flu vaccine."""
    conv_id = next_conversation_id(state)
    state["patientLetters"].append({
        "id": next_letter_id(state),
        "patientId": "pat_7",
        "conversationId": conv_id,
        "direction": "to_patient",
        "subject": "Annual Flu Vaccine Reminder",
        "body": "Hi David, it's time to schedule your annual flu shot.",
        "category": None,
        "senderId": "prov_1",
        "senderType": "provider",
        "attachments": [],
        "postDate": None,
        "sentAt": TIMESTAMP,
        "readAt": None,
        "isRead": False,
        "isDraft": False,
        "conversationState": "open",
        "doNotAllowResponse": False,
        "unreadAlertTimeframe": "none",
        "printHeader": "default",
    })


def solve_task_m12(state):
    """Invite Brian Murphy to Passport with sharing level 3."""
    patient = find_entity(state["patients"], id="pat_15")
    patient["passportStatus"] = "invited"
    patient["passportSharingLevel"] = 3
    patient["invitedAt"] = TIMESTAMP
    patient["invitationCode"] = "9999998"


def solve_task_m13(state):
    """Cancel Rachel Steinberg's appointment."""
    appt = find_appointment(state, "appt_10")
    appt["status"] = "cancelled"


def solve_task_m14(state):
    """Change chat mode to host_only and disable screen sharing."""
    state["practiceSettings"]["videoSettings"]["chatMode"] = "host_only"
    state["practiceSettings"]["videoSettings"]["screenSharingPatients"] = False


def solve_task_m15(state):
    """Disable Patricia O'Brien's Passport."""
    patient = find_entity(state["patients"], id="pat_8")
    patient["passportAccountDisabled"] = True
    patient["passportStatus"] = "not_invited"


def solve_task_m16(state):
    """Read Janet Okonkwo's message and tag her as high risk."""
    letter = find_letter(state, "ltr_20")
    letter["isRead"] = True
    letter["readAt"] = TIMESTAMP
    patient = find_entity(state["patients"], id="pat_30")
    if "High Risk" not in patient["tags"]:
        patient["tags"].append("High Risk")


def solve_task_m17(state):
    """End Kevin Adebayo billing conversation."""
    for letter in state["patientLetters"]:
        if letter["conversationId"] == "conv_8":
            letter["conversationState"] = "ended"


def solve_task_m18(state):
    """Schedule virtual appointment for Andrew McIntyre."""
    state["appointments"].append({
        "id": next_appointment_id(state),
        "patientId": "pat_29",
        "providerId": "prov_2",
        "date": "2026-03-20T15:00:00Z",
        "place": "virtual",
        "status": "scheduled",
        "virtualVisitInstructions": "Join at https://zoom.us/j/7261048395?pwd=def456",
        "reason": "Acid reflux follow-up",
    })


def solve_task_m19(state):
    """Remove Geriatric and Chronic Care tags from Nancy Yamamoto."""
    patient = find_entity(state["patients"], id="pat_24")
    patient["tags"] = [t for t in patient["tags"] if t not in ("Geriatric", "Chronic Care")]


def solve_task_m20(state):
    """Update Dr. Kim's sharing to level 3 and notification to 24 hours."""
    provider = find_provider(state, "prov_4")
    provider["sharingDefault"] = 3
    provider["notificationTimeframe"] = "24_hours"


# ---- Hard ----

def solve_task_h1(state):
    """Invite all Dr. Kim's uninvited patients to Passport."""
    # Dr. Kim = prov_4, uninvited: pat_15, pat_23, pat_31
    for pid, code in [("pat_15", "9999991"), ("pat_23", "9999992"), ("pat_31", "9999993")]:
        patient = find_entity(state["patients"], id=pid)
        patient["passportStatus"] = "invited"
        patient["invitedAt"] = TIMESTAMP
        patient["invitationCode"] = code


def solve_task_h2(state):
    """Mark all unread patient messages as read."""
    for letter in state["patientLetters"]:
        if letter["direction"] == "from_patient" and not letter.get("isDraft", False):
            if not letter["isRead"]:
                letter["isRead"] = True
                letter["readAt"] = TIMESTAMP


def solve_task_h3(state):
    """Acknowledge all pending reminders."""
    for reminder in state["reminders"]:
        reminder["acknowledged"] = True


def solve_task_h4(state):
    """Cancel all virtual March appointments."""
    for appt_id in ["appt_2", "appt_6", "appt_9", "appt_13", "appt_14"]:
        appt = find_appointment(state, appt_id)
        appt["status"] = "cancelled"


def solve_task_h5(state):
    """Read messages from Janet/Christine and end their conversations."""
    find_letter(state, "ltr_20")["isRead"] = True
    find_letter(state, "ltr_20")["readAt"] = TIMESTAMP
    find_letter(state, "ltr_29")["isRead"] = True
    find_letter(state, "ltr_29")["readAt"] = TIMESTAMP
    for letter in state["patientLetters"]:
        if letter["conversationId"] in ("conv_14", "conv_21"):
            letter["conversationState"] = "ended"


def solve_task_h6(state):
    """Add Clinical Team to all routing categories for Dr. Chen."""
    for category in MESSAGE_CATEGORIES:
        routing = state["messageRouting"]["prov_1"].get(category, [])
        if "ug_2" not in routing:
            routing.append("ug_2")
        state["messageRouting"]["prov_1"][category] = routing


def solve_task_h7(state):
    """Remove telephone E/M codes (99441, 99442, 99443)."""
    codes_to_remove = {"99441", "99442", "99443"}
    state["practiceSettings"]["cptCodes"] = [
        c for c in state["practiceSettings"]["cptCodes"]
        if c["code"] not in codes_to_remove
    ]


def solve_task_h8(state):
    """Send bulk letter to Diabetes Management patients."""
    target_ids = ["pat_1", "pat_11", "pat_30", "pat_35"]
    bulk_id = next_bulk_letter_id(state)
    state["bulkLetters"].append({
        "id": bulk_id,
        "description": "A1C screening outreach",
        "subject": "Annual A1C Screening Reminder",
        "body": "Please schedule your annual A1C screening at your earliest convenience.",
        "sentAt": TIMESTAMP,
        "sentBy": "prov_1",
        "targetCount": len(target_ids),
        "allowResponse": False,
    })
    conv_id = next_conversation_id(state)
    for pat_id in target_ids:
        state["patientLetters"].append({
            "id": next_letter_id(state),
            "patientId": pat_id,
            "conversationId": f"{conv_id}_{pat_id}",
            "direction": "to_patient",
            "subject": "Annual A1C Screening Reminder",
            "body": "Please schedule your annual A1C screening at your earliest convenience.",
            "category": None,
            "senderId": "prov_1",
            "senderType": "provider",
            "attachments": [],
            "postDate": None,
            "sentAt": TIMESTAMP,
            "readAt": None,
            "isRead": False,
            "isDraft": False,
            "conversationState": "ended",
            "doNotAllowResponse": True,
            "unreadAlertTimeframe": "none",
            "printHeader": "default",
        })


def solve_task_h9(state):
    """Add Clinical Team to Medical Records Request routing for all providers."""
    for prov_id in ["prov_1", "prov_2", "prov_3", "prov_4", "prov_5"]:
        routing = state["messageRouting"].get(prov_id, {})
        cat_routing = routing.get("Medical Records Request", [])
        if "ug_2" not in cat_routing:
            cat_routing.append("ug_2")
        routing["Medical Records Request"] = cat_routing
        state["messageRouting"][prov_id] = routing


def solve_task_h10(state):
    """Enable telehealth for Jessica Okafor and Amanda Wright."""
    prov3 = find_provider(state, "prov_3")
    prov3["virtualVisitActivated"] = True
    prov3["virtualVisitInstructions"] = "Join your telehealth visit: https://zoom.us/j/okafor123"
    prov5 = find_provider(state, "prov_5")
    prov5["virtualVisitActivated"] = True
    prov5["virtualVisitInstructions"] = "Join your telehealth visit: https://zoom.us/j/wright456"


def solve_task_h11(state):
    """Reply to both unread appointment requests (Sophia Nguyen and Susan Cho)."""
    # Reply to conv_4 (Sophia Nguyen)
    state["patientLetters"].append({
        "id": next_letter_id(state),
        "patientId": "pat_4",
        "conversationId": "conv_4",
        "direction": "to_patient",
        "subject": "Re: Appointment Request",
        "body": "Your appointment request has been received and will be scheduled.",
        "category": None,
        "senderId": "prov_1",
        "senderType": "provider",
        "attachments": [],
        "postDate": None,
        "sentAt": TIMESTAMP,
        "readAt": None,
        "isRead": False,
        "isDraft": False,
        "conversationState": "open",
        "doNotAllowResponse": False,
        "unreadAlertTimeframe": "none",
        "printHeader": "default",
    })
    # Reply to conv_28 (Susan Cho)
    state["patientLetters"].append({
        "id": next_letter_id(state),
        "patientId": "pat_40",
        "conversationId": "conv_28",
        "direction": "to_patient",
        "subject": "Re: Appointment Request",
        "body": "Your appointment request has been received and will be scheduled.",
        "category": None,
        "senderId": "prov_1",
        "senderType": "provider",
        "attachments": [],
        "postDate": None,
        "sentAt": TIMESTAMP,
        "readAt": None,
        "isRead": False,
        "isDraft": False,
        "conversationState": "open",
        "doNotAllowResponse": False,
        "unreadAlertTimeframe": "none",
        "printHeader": "default",
    })


def solve_task_h12(state):
    """End all open conversations with Dr. Torres's patients."""
    # Open conversations: conv_16 (Andrew McIntyre), conv_26 (Russell Keane)
    for letter in state["patientLetters"]:
        if letter["conversationId"] in ("conv_16", "conv_26"):
            letter["conversationState"] = "ended"


def solve_task_h13(state):
    """Tag Victor Santos and Craig Bennet as Insurance Pending, invite to Passport."""
    for pid, code in [("pat_23", "9999994"), ("pat_31", "9999995")]:
        patient = find_entity(state["patients"], id=pid)
        if "Insurance Pending" not in patient["tags"]:
            patient["tags"].append("Insurance Pending")
        patient["passportStatus"] = "invited"
        patient["invitedAt"] = TIMESTAMP
        patient["invitationCode"] = code


def solve_task_h14(state):
    """Remove 99421-99423, add 99458."""
    codes_to_remove = {"99421", "99422", "99423"}
    state["practiceSettings"]["cptCodes"] = [
        c for c in state["practiceSettings"]["cptCodes"]
        if c["code"] not in codes_to_remove
    ]
    state["practiceSettings"]["cptCodes"].append({
        "code": "99458",
        "description": "Prolonged telehealth service, 15 min",
    })


def solve_task_h15(state):
    """Mark all unread messages from Dr. Chen's patients as read."""
    # Unread from prov_1 patients: ltr_4,6,10,15,19,20,24,29,47
    prov1_unread = {"ltr_4", "ltr_6", "ltr_10", "ltr_15", "ltr_19",
                    "ltr_20", "ltr_24", "ltr_29", "ltr_47"}
    for letter in state["patientLetters"]:
        if letter["id"] in prov1_unread:
            letter["isRead"] = True
            letter["readAt"] = TIMESTAMP


def solve_task_h16(state):
    """Upgrade Helen Matsumoto sharing to 4 and send notification letter."""
    patient = find_entity(state["patients"], id="pat_10")
    patient["passportSharingLevel"] = 4
    conv_id = next_conversation_id(state)
    state["patientLetters"].append({
        "id": next_letter_id(state),
        "patientId": "pat_10",
        "conversationId": conv_id,
        "direction": "to_patient",
        "subject": "Updated Passport Sharing Level",
        "body": "Your Passport sharing level has been updated to the most comprehensive level.",
        "category": None,
        "senderId": "prov_1",
        "senderType": "provider",
        "attachments": [],
        "postDate": None,
        "sentAt": TIMESTAMP,
        "readAt": None,
        "isRead": False,
        "isDraft": False,
        "conversationState": "open",
        "doNotAllowResponse": False,
        "unreadAlertTimeframe": "none",
        "printHeader": "default",
    })


def solve_task_h17(state):
    """Disable Robert Washington's Passport and remove all tags."""
    patient = find_entity(state["patients"], id="pat_3")
    patient["passportAccountDisabled"] = True
    patient["passportStatus"] = "not_invited"
    patient["tags"] = []


def solve_task_h18(state):
    """Schedule two appointments: Emily Thompson and Priya Sharma."""
    state["appointments"].append({
        "id": next_appointment_id(state),
        "patientId": "pat_2",
        "providerId": "prov_1",
        "date": "2026-03-15T14:00:00Z",
        "place": "in_person",
        "status": "scheduled",
        "virtualVisitInstructions": None,
        "reason": "Annual physical",
    })
    state["appointments"].append({
        "id": next_appointment_id(state),
        "patientId": "pat_32",
        "providerId": "prov_1",
        "date": "2026-03-18T10:00:00Z",
        "place": "in_person",
        "status": "scheduled",
        "virtualVisitInstructions": None,
        "reason": "Migraine follow-up",
    })


def solve_task_h19(state):
    """Remove Telehealth location, add West SF Urgent Care."""
    state["practiceSettings"]["practiceLocations"] = [
        loc for loc in state["practiceSettings"]["practiceLocations"]
        if loc["name"] != "Telehealth"
    ]
    state["practiceSettings"]["practiceLocations"].append({
        "id": next_location_id(state),
        "name": "West SF Urgent Care",
        "address": "2100 Geary Blvd, San Francisco, CA 94115",
        "posCode": "20",
        "posDescription": "Urgent Care Facility",
    })


def solve_task_h20(state):
    """Resend invitations to all invited-but-not-registered patients."""
    invited_not_registered = {
        "pat_5": "8888881",
        "pat_13": "8888882",
        "pat_21": "8888883",
        "pat_28": "8888884",
        "pat_39": "8888885",
        "pat_48": "8888886",
    }
    for pid, new_code in invited_not_registered.items():
        patient = find_entity(state["patients"], id=pid)
        patient["invitedAt"] = TIMESTAMP
        patient["invitationCode"] = new_code


# ---- Hardening Round 1 (h21-h40) ----

def solve_task_h21(state):
    """Reply to Raymond Copeland about thirst/urination, schedule virtual appt."""
    state["patientLetters"].append({
        "id": next_letter_id(state),
        "patientId": "pat_35",
        "conversationId": "conv_34",
        "direction": "to_patient",
        "subject": "Re: General Question",
        "body": "Raymond, your symptoms of increased thirst and urination may indicate a change in blood sugar control. Please come in for fasting blood work so we can evaluate.",
        "category": None,
        "senderId": "prov_1",
        "senderType": "provider",
        "attachments": [],
        "postDate": None,
        "sentAt": TIMESTAMP,
        "readAt": None,
        "isRead": False,
        "isDraft": False,
        "conversationState": "open",
        "doNotAllowResponse": False,
        "unreadAlertTimeframe": "none",
        "printHeader": "default",
    })
    state["appointments"].append({
        "id": next_appointment_id(state),
        "patientId": "pat_35",
        "providerId": "prov_4",
        "date": "2026-03-25T11:00:00Z",
        "place": "virtual",
        "status": "scheduled",
        "virtualVisitInstructions": "Join at https://zoom.us/j/5029384716?pwd=ghi789",
        "reason": "Blood sugar evaluation",
    })


def solve_task_h22(state):
    """Read Helen Matsumoto's message, add High Risk tag, reply."""
    letter = find_letter(state, "ltr_10")
    letter["isRead"] = True
    letter["readAt"] = TIMESTAMP
    patient = find_entity(state["patients"], id="pat_10")
    if "High Risk" not in patient["tags"]:
        patient["tags"].append("High Risk")
    state["patientLetters"].append({
        "id": next_letter_id(state),
        "patientId": "pat_10",
        "conversationId": "conv_7",
        "direction": "to_patient",
        "subject": "Re: General Question",
        "body": "Dear Ken, thank you for letting us know. Increased forgetfulness can occur with Alzheimer's progression. We'll evaluate her at the upcoming appointment.",
        "category": None,
        "senderId": "prov_1",
        "senderType": "provider",
        "attachments": [],
        "postDate": None,
        "sentAt": TIMESTAMP,
        "readAt": None,
        "isRead": False,
        "isDraft": False,
        "conversationState": "open",
        "doNotAllowResponse": False,
        "unreadAlertTimeframe": "none",
        "printHeader": "default",
    })


def solve_task_h23(state):
    """Reply to Diane Foster-Hutchinson's referral request, tag as VIP."""
    state["patientLetters"].append({
        "id": next_letter_id(state),
        "patientId": "pat_16",
        "conversationId": "conv_10",
        "direction": "to_patient",
        "subject": "Re: Referral Request",
        "body": "Hi Diane, I'll find a new allergist for you in the SF area who specializes in bee venom allergy testing.",
        "category": None,
        "senderId": "prov_1",
        "senderType": "provider",
        "attachments": [],
        "postDate": None,
        "sentAt": TIMESTAMP,
        "readAt": None,
        "isRead": False,
        "isDraft": False,
        "conversationState": "open",
        "doNotAllowResponse": False,
        "unreadAlertTimeframe": "none",
        "printHeader": "default",
    })
    patient = find_entity(state["patients"], id="pat_16")
    if "VIP" not in patient["tags"]:
        patient["tags"].append("VIP")


def solve_task_h24(state):
    """Cancel Janet's virtual appt, schedule in-person, reply to message."""
    appt = find_appointment(state, "appt_13")
    appt["status"] = "cancelled"
    state["appointments"].append({
        "id": next_appointment_id(state),
        "patientId": "pat_30",
        "providerId": "prov_1",
        "date": "2026-03-10T09:00:00Z",
        "place": "in_person",
        "status": "scheduled",
        "virtualVisitInstructions": None,
        "reason": "Urgent diabetes management",
    })
    state["patientLetters"].append({
        "id": next_letter_id(state),
        "patientId": "pat_30",
        "conversationId": "conv_14",
        "direction": "to_patient",
        "subject": "Re: General Question",
        "body": "Janet, your blood sugar readings are concerning. I've cancelled your virtual visit and rescheduled you for an in-person appointment on March 10.",
        "category": None,
        "senderId": "prov_1",
        "senderType": "provider",
        "attachments": [],
        "postDate": None,
        "sentAt": TIMESTAMP,
        "readAt": None,
        "isRead": False,
        "isDraft": False,
        "conversationState": "open",
        "doNotAllowResponse": False,
        "unreadAlertTimeframe": "none",
        "printHeader": "default",
    })


def solve_task_h25(state):
    """Cancel all Dr. Chen in-person upcoming appointments, keep virtual."""
    for appt_id in ["appt_1", "appt_4", "appt_7", "appt_11", "appt_12"]:
        appt = find_appointment(state, appt_id)
        appt["status"] = "cancelled"


def solve_task_h26(state):
    """Add Front Desk to Dr. Torres categories where he's sole recipient."""
    sole_categories = [
        "Prescription Refill", "Test Results", "Referral Request", "Other",
    ]
    for cat in sole_categories:
        routing = state["messageRouting"]["prov_2"].get(cat, [])
        if "ug_1" not in routing:
            routing.append("ug_1")
        state["messageRouting"]["prov_2"][cat] = routing


def solve_task_h27(state):
    """Send letter to Deborah Takahashi, upgrade sharing to 4, add Chronic Care."""
    conv_id = next_conversation_id(state)
    state["patientLetters"].append({
        "id": next_letter_id(state),
        "patientId": "pat_50",
        "conversationId": conv_id,
        "direction": "to_patient",
        "subject": "Passport Access Update",
        "body": "Dear Mrs. Takahashi, we're upgrading your Passport access to the most comprehensive level.",
        "category": None,
        "senderId": "prov_1",
        "senderType": "provider",
        "attachments": [],
        "postDate": None,
        "sentAt": TIMESTAMP,
        "readAt": None,
        "isRead": False,
        "isDraft": False,
        "conversationState": "open",
        "doNotAllowResponse": False,
        "unreadAlertTimeframe": "none",
        "printHeader": "default",
    })
    patient = find_entity(state["patients"], id="pat_50")
    patient["passportSharingLevel"] = 4
    if "Chronic Care" not in patient["tags"]:
        patient["tags"].append("Chronic Care")


def solve_task_h28(state):
    """Cancel Howard Blackwell's virtual appt, schedule in-person."""
    appt = find_appointment(state, "appt_9")
    appt["status"] = "cancelled"
    state["appointments"].append({
        "id": next_appointment_id(state),
        "patientId": "pat_27",
        "providerId": "prov_4",
        "date": "2026-03-22T14:00:00Z",
        "place": "in_person",
        "status": "scheduled",
        "virtualVisitInstructions": None,
        "reason": "CHF management review",
    })


def solve_task_h29(state):
    """Apply Dr. Chen's routing to all other providers."""
    import copy
    chen_routing = state["messageRouting"]["prov_1"]
    for prov_id in ["prov_2", "prov_3", "prov_4", "prov_5"]:
        state["messageRouting"][prov_id] = copy.deepcopy(chen_routing)


def solve_task_h30(state):
    """Reply to Priya Sharma's records request, sign off conversation."""
    state["patientLetters"].append({
        "id": next_letter_id(state),
        "patientId": "pat_32",
        "conversationId": "conv_13",
        "direction": "to_patient",
        "subject": "Re: Medical Records Request",
        "body": "Hi Priya, please fill out the records release form. Processing takes 5-7 business days.",
        "category": None,
        "senderId": "prov_1",
        "senderType": "provider",
        "attachments": [],
        "postDate": None,
        "sentAt": TIMESTAMP,
        "readAt": None,
        "isRead": False,
        "isDraft": False,
        "conversationState": "ended",
        "doNotAllowResponse": False,
        "unreadAlertTimeframe": "none",
        "printHeader": "default",
    })
    for letter in state["patientLetters"]:
        if letter["conversationId"] == "conv_13":
            letter["conversationState"] = "ended"


def solve_task_h31(state):
    """Remove 'New Patient' tag from all patients."""
    for pid in ["pat_2", "pat_5", "pat_9", "pat_31", "pat_42"]:
        patient = find_entity(state["patients"], id=pid)
        patient["tags"] = [t for t in patient["tags"] if t != "New Patient"]


def solve_task_h32(state):
    """Reply to Maria Gonzalez conversation, acknowledge rem_1."""
    state["patientLetters"].append({
        "id": next_letter_id(state),
        "patientId": "pat_14",
        "conversationId": "conv_9",
        "direction": "to_patient",
        "subject": "Re: General Question",
        "body": "Maria, great job on the daily walks! We'll discuss diet and Metformin at your upcoming appointment.",
        "category": None,
        "senderId": "prov_1",
        "senderType": "provider",
        "attachments": [],
        "postDate": None,
        "sentAt": TIMESTAMP,
        "readAt": None,
        "isRead": False,
        "isDraft": False,
        "conversationState": "open",
        "doNotAllowResponse": False,
        "unreadAlertTimeframe": "none",
        "printHeader": "default",
    })
    reminder = find_reminder(state, "rem_1")
    reminder["acknowledged"] = True


def solve_task_h33(state):
    """Send no-reply letter to Christine Lee, acknowledge rem_6."""
    conv_id = next_conversation_id(state)
    state["patientLetters"].append({
        "id": next_letter_id(state),
        "patientId": "pat_22",
        "conversationId": conv_id,
        "direction": "to_patient",
        "subject": "Sleep Concerns Follow-up",
        "body": "Christine, please start keeping a sleep diary for the next 2 weeks.",
        "category": None,
        "senderId": "prov_1",
        "senderType": "provider",
        "attachments": [],
        "postDate": None,
        "sentAt": TIMESTAMP,
        "readAt": None,
        "isRead": False,
        "isDraft": False,
        "conversationState": "open",
        "doNotAllowResponse": True,
        "unreadAlertTimeframe": "none",
        "printHeader": "default",
    })
    reminder = find_reminder(state, "rem_6")
    reminder["acknowledged"] = True


def solve_task_h34(state):
    """Tag virtual-appointment patients as 'Telehealth Preferred'."""
    for pid in ["pat_27", "pat_30"]:
        patient = find_entity(state["patients"], id=pid)
        if "Telehealth Preferred" not in patient["tags"]:
            patient["tags"].append("Telehealth Preferred")


def solve_task_h35(state):
    """Update Dr. Chen telehealth instructions and video chat mode."""
    provider = find_provider(state, "prov_1")
    provider["virtualVisitInstructions"] = (
        "Join your virtual visit at https://zoom.us/j/newlink123. "
        "Please ensure your camera is working."
    )
    state["practiceSettings"]["videoSettings"]["chatMode"] = "everyone_in_waiting_room"


def solve_task_h36(state):
    """Read both appt requests, reply to Susan Cho, schedule virtual appt."""
    find_letter(state, "ltr_6")["isRead"] = True
    find_letter(state, "ltr_6")["readAt"] = TIMESTAMP
    find_letter(state, "ltr_39")["isRead"] = True
    find_letter(state, "ltr_39")["readAt"] = TIMESTAMP
    state["patientLetters"].append({
        "id": next_letter_id(state),
        "patientId": "pat_40",
        "conversationId": "conv_28",
        "direction": "to_patient",
        "subject": "Re: Appointment Request",
        "body": "Susan, I'll schedule a telehealth visit to evaluate your urticaria flare.",
        "category": None,
        "senderId": "prov_1",
        "senderType": "provider",
        "attachments": [],
        "postDate": None,
        "sentAt": TIMESTAMP,
        "readAt": None,
        "isRead": False,
        "isDraft": False,
        "conversationState": "open",
        "doNotAllowResponse": False,
        "unreadAlertTimeframe": "none",
        "printHeader": "default",
    })
    state["appointments"].append({
        "id": next_appointment_id(state),
        "patientId": "pat_40",
        "providerId": "prov_3",
        "date": "2026-03-14T10:00:00Z",
        "place": "virtual",
        "status": "scheduled",
        "virtualVisitInstructions": "Join at https://zoom.us/j/3948271605?pwd=jkl012",
        "reason": "Urticaria evaluation",
    })


def solve_task_h37(state):
    """Enable telehealth for Amanda Wright, schedule virtual appt for Sophia."""
    provider = find_provider(state, "prov_5")
    provider["virtualVisitActivated"] = True
    provider["virtualVisitInstructions"] = "Join at https://zoom.us/j/wright789"
    state["appointments"].append({
        "id": next_appointment_id(state),
        "patientId": "pat_4",
        "providerId": "prov_5",
        "date": "2026-03-20T15:00:00Z",
        "place": "virtual",
        "status": "scheduled",
        "virtualVisitInstructions": "Join at https://zoom.us/j/wright789",
        "reason": "Thyroid follow-up",
    })


def solve_task_h38(state):
    """Invite all uninvited patients to Passport."""
    uninvited = [
        ("pat_9", "9999961"),
        ("pat_15", "9999962"),
        ("pat_23", "9999963"),
        ("pat_31", "9999964"),
        ("pat_37", "9999965"),
        ("pat_42", "9999966"),
    ]
    for pid, code in uninvited:
        patient = find_entity(state["patients"], id=pid)
        patient["passportStatus"] = "invited"
        patient["invitedAt"] = TIMESTAMP
        patient["invitationCode"] = code


def solve_task_h39(state):
    """Read, reply, sign off conversations for Christine Lee & Diane F-H."""
    find_letter(state, "ltr_29")["isRead"] = True
    find_letter(state, "ltr_29")["readAt"] = TIMESTAMP
    find_letter(state, "ltr_15")["isRead"] = True
    find_letter(state, "ltr_15")["readAt"] = TIMESTAMP
    state["patientLetters"].append({
        "id": next_letter_id(state),
        "patientId": "pat_22",
        "conversationId": "conv_21",
        "direction": "to_patient",
        "subject": "Re: General Question",
        "body": "Christine, let's try adjusting your Trazodone dose. I'll also refer you to our sleep specialist.",
        "category": None,
        "senderId": "prov_1",
        "senderType": "provider",
        "attachments": [],
        "postDate": None,
        "sentAt": TIMESTAMP,
        "readAt": None,
        "isRead": False,
        "isDraft": False,
        "conversationState": "ended",
        "doNotAllowResponse": False,
        "unreadAlertTimeframe": "none",
        "printHeader": "default",
    })
    state["patientLetters"].append({
        "id": next_letter_id(state),
        "patientId": "pat_16",
        "conversationId": "conv_10",
        "direction": "to_patient",
        "subject": "Re: Referral Request",
        "body": "Diane, I'll find a new allergist who specializes in venom allergy testing.",
        "category": None,
        "senderId": "prov_1",
        "senderType": "provider",
        "attachments": [],
        "postDate": None,
        "sentAt": TIMESTAMP,
        "readAt": None,
        "isRead": False,
        "isDraft": False,
        "conversationState": "ended",
        "doNotAllowResponse": False,
        "unreadAlertTimeframe": "none",
        "printHeader": "default",
    })
    for letter in state["patientLetters"]:
        if letter["conversationId"] in ("conv_21", "conv_10"):
            letter["conversationState"] = "ended"


def solve_task_h40(state):
    """Add two CPT codes and Fremont Clinic location."""
    state["practiceSettings"]["cptCodes"].append({
        "code": "99458",
        "description": "Prolonged telehealth service, 15 min",
    })
    state["practiceSettings"]["cptCodes"].append({
        "code": "99459",
        "description": "Prolonged telehealth service, additional 15 min",
    })
    state["practiceSettings"]["practiceLocations"].append({
        "id": next_location_id(state),
        "name": "Fremont Clinic",
        "address": "39500 Paseo Padre Pkwy, Fremont, CA 94538",
        "posCode": "11",
        "posDescription": "Office",
    })


SOLVERS = {
    "task_e1": solve_task_e1,
    "task_e2": solve_task_e2,
    "task_e3": solve_task_e3,
    "task_e4": solve_task_e4,
    "task_e5": solve_task_e5,
    "task_e6": solve_task_e6,
    "task_e7": solve_task_e7,
    "task_e8": solve_task_e8,
    "task_e9": solve_task_e9,
    "task_e10": solve_task_e10,
    "task_e11": solve_task_e11,
    "task_e12": solve_task_e12,
    "task_e13": solve_task_e13,
    "task_e14": solve_task_e14,
    "task_e15": solve_task_e15,
    "task_e16": solve_task_e16,
    "task_e17": solve_task_e17,
    "task_e18": solve_task_e18,
    "task_e19": solve_task_e19,
    "task_e20": solve_task_e20,
    "task_m1": solve_task_m1,
    "task_m2": solve_task_m2,
    "task_m3": solve_task_m3,
    "task_m4": solve_task_m4,
    "task_m5": solve_task_m5,
    "task_m6": solve_task_m6,
    "task_m7": solve_task_m7,
    "task_m8": solve_task_m8,
    "task_m9": solve_task_m9,
    "task_m10": solve_task_m10,
    "task_m11": solve_task_m11,
    "task_m12": solve_task_m12,
    "task_m13": solve_task_m13,
    "task_m14": solve_task_m14,
    "task_m15": solve_task_m15,
    "task_m16": solve_task_m16,
    "task_m17": solve_task_m17,
    "task_m18": solve_task_m18,
    "task_m19": solve_task_m19,
    "task_m20": solve_task_m20,
    "task_h1": solve_task_h1,
    "task_h2": solve_task_h2,
    "task_h3": solve_task_h3,
    "task_h4": solve_task_h4,
    "task_h5": solve_task_h5,
    "task_h6": solve_task_h6,
    "task_h7": solve_task_h7,
    "task_h8": solve_task_h8,
    "task_h9": solve_task_h9,
    "task_h10": solve_task_h10,
    "task_h11": solve_task_h11,
    "task_h12": solve_task_h12,
    "task_h13": solve_task_h13,
    "task_h14": solve_task_h14,
    "task_h15": solve_task_h15,
    "task_h16": solve_task_h16,
    "task_h17": solve_task_h17,
    "task_h18": solve_task_h18,
    "task_h19": solve_task_h19,
    "task_h20": solve_task_h20,
    "task_h21": solve_task_h21,
    "task_h22": solve_task_h22,
    "task_h23": solve_task_h23,
    "task_h24": solve_task_h24,
    "task_h25": solve_task_h25,
    "task_h26": solve_task_h26,
    "task_h27": solve_task_h27,
    "task_h28": solve_task_h28,
    "task_h29": solve_task_h29,
    "task_h30": solve_task_h30,
    "task_h31": solve_task_h31,
    "task_h32": solve_task_h32,
    "task_h33": solve_task_h33,
    "task_h34": solve_task_h34,
    "task_h35": solve_task_h35,
    "task_h36": solve_task_h36,
    "task_h37": solve_task_h37,
    "task_h38": solve_task_h38,
    "task_h39": solve_task_h39,
    "task_h40": solve_task_h40,
}


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


def find_free_port(start=9500):
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
    parser = argparse.ArgumentParser(description="Elation Patient Communication real-task sanity check")
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
