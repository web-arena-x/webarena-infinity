#!/usr/bin/env python3
"""
Sanity check for Elation Patient Communication real tasks.

For each task, directly applies the expected end-state (bypassing the agent),
then runs the verifier and asserts it passes.

Usage:
    python3 sanity_check_real.py                     # All tasks, sequential
    python3 sanity_check_real.py --workers N          # N parallel environments
    python3 sanity_check_real.py --task-id task_e1    # Single task
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


def find_provider_by_name(state, first, last):
    return find_entity(state["providers"], firstName=first, lastName=last)


def find_letter(state, letter_id):
    return find_entity(state["patientLetters"], id=letter_id)


def find_reminder(state, reminder_id):
    return find_entity(state["reminders"], id=reminder_id)


def find_location_by_name(state, name):
    for loc in state["practiceSettings"]["practiceLocations"]:
        if loc["name"] == name:
            return loc
    raise ValueError(f"Location not found: {name!r}")


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


def make_letter(state, patient_id, conversation_id, subject, body, **overrides):
    letter = {
        "id": next_letter_id(state),
        "patientId": patient_id,
        "conversationId": conversation_id,
        "direction": "to_patient",
        "subject": subject,
        "body": body,
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
    }
    letter.update(overrides)
    return letter


TIMESTAMP = "2026-03-02T12:00:00Z"

MESSAGE_CATEGORIES = [
    "General Question", "Prescription Refill", "Appointment Request",
    "Test Results", "Billing Question", "Referral Request",
    "Medical Records Request", "Other",
]


# ── solve functions ──────────────────────────────────────────────────

# ── Easy tasks ───────────────────────────────────────────────────────

def solve_task_e1(state):
    """Mark Janet Okonkwo's blood sugar message as read."""
    letter = find_letter(state, "ltr_20")
    letter["isRead"] = True
    letter["readAt"] = TIMESTAMP


def solve_task_e2(state):
    """Acknowledge James Rodriguez's appointment reminder."""
    reminder = find_reminder(state, "rem_10")
    reminder["acknowledged"] = True


def solve_task_e3(state):
    """Cancel Sophia Nguyen's thyroid check-up appointment."""
    appt = find_entity(state["appointments"], id="appt_2")
    appt["status"] = "cancelled"


def solve_task_e4(state):
    """Turn off patient messaging."""
    state["practiceSettings"]["allowPatientMessaging"] = False


def solve_task_e5(state):
    """Add VIP tag to David Park."""
    patient = find_patient_by_name(state, "David", "Park")
    if "VIP" not in patient["tags"]:
        patient["tags"].append("VIP")


def solve_task_e6(state):
    """Remove 'New Patient' tag from Emily Thompson."""
    patient = find_patient_by_name(state, "Emily", "Thompson")
    patient["tags"] = [t for t in patient["tags"] if t != "New Patient"]


def solve_task_e7(state):
    """Deactivate virtual visits for Dr. Torres."""
    provider = find_provider(state, "prov_2")
    provider["virtualVisitActivated"] = False


def solve_task_e8(state):
    """Delete the draft letter to Martha Reeves-Whitfield."""
    state["patientLetters"] = [l for l in state["patientLetters"] if l["id"] != "ltr_35"]


def solve_task_e9(state):
    """Change Dr. Chen's notification timeframe to 72 hours."""
    provider = find_provider(state, "prov_1")
    provider["notificationTimeframe"] = "72_hours"


def solve_task_e10(state):
    """Disable booking site auto-invite."""
    state["practiceSettings"]["bookingSiteAutoInvite"] = False


def solve_task_e11(state):
    """Acknowledge Marcus Johnson's passport invitation reminder."""
    reminder = find_reminder(state, "rem_7")
    reminder["acknowledged"] = True


def solve_task_e12(state):
    """Remove East Bay Clinic."""
    state["practiceSettings"]["practiceLocations"] = [
        loc for loc in state["practiceSettings"]["practiceLocations"]
        if loc["name"] != "East Bay Clinic"
    ]


def solve_task_e13(state):
    """Remove CPT code 99201."""
    state["practiceSettings"]["cptCodes"] = [
        c for c in state["practiceSettings"]["cptCodes"]
        if c["code"] != "99201"
    ]


def solve_task_e14(state):
    """Turn off screen sharing for patients."""
    state["practiceSettings"]["videoSettings"]["screenSharingPatients"] = False


def solve_task_e15(state):
    """Cancel Dennis Volkov's blood pressure appointment."""
    appt = find_entity(state["appointments"], id="appt_15")
    appt["status"] = "cancelled"


def solve_task_e16(state):
    """Change video chat mode to host only."""
    state["practiceSettings"]["videoSettings"]["chatMode"] = "host_only"


def solve_task_e17(state):
    """Send the draft letter to Martha Reeves-Whitfield."""
    letter = find_letter(state, "ltr_35")
    letter["isDraft"] = False
    letter["sentAt"] = TIMESTAMP


def solve_task_e18(state):
    """Acknowledge Maria Gonzalez's unread alert reminder."""
    reminder = find_reminder(state, "rem_1")
    reminder["acknowledged"] = True


def solve_task_e19(state):
    """Disable waiting room audio notification."""
    state["practiceSettings"]["videoSettings"]["waitingRoomAudioNotification"] = False


def solve_task_e20(state):
    """Change Dr. Chen's sharing default to 3."""
    provider = find_provider(state, "prov_1")
    provider["sharingDefault"] = 3


# ── Medium tasks ─────────────────────────────────────────────────────

def solve_task_m1(state):
    """Send Passport invitation to Anthony Petrov."""
    patient = find_patient_by_name(state, "Anthony", "Petrov")
    patient["passportStatus"] = "invited"
    patient["invitedAt"] = TIMESTAMP
    patient["invitationCode"] = "9999999"


def solve_task_m2(state):
    """End conversation with Aisha Patel (conv_22)."""
    for letter in state["patientLetters"]:
        if letter["conversationId"] == "conv_22":
            letter["conversationState"] = "ended"


def solve_task_m3(state):
    """Add South Bay Clinic location."""
    state["practiceSettings"]["practiceLocations"].append({
        "id": next_location_id(state),
        "name": "South Bay Clinic",
        "address": "789 Stevens Creek Blvd, San Jose, CA 95128",
        "posCode": "11",
        "posDescription": "Office",
    })


def solve_task_m4(state):
    """Add Nurses to Dr. Kim's Prescription Refill routing."""
    routing = state["messageRouting"]["prov_4"]["Prescription Refill"]
    if "ug_3" not in routing:
        routing.append("ug_3")


def solve_task_m5(state):
    """Resend Passport invitation to William Chang."""
    patient = find_patient_by_name(state, "William", "Chang")
    patient["invitedAt"] = TIMESTAMP
    patient["invitationCode"] = "8888888"


def solve_task_m6(state):
    """Update Brian Murphy's email."""
    patient = find_patient_by_name(state, "Brian", "Murphy")
    patient["email"] = "brian.murphy@gmail.com"


def solve_task_m7(state):
    """Activate virtual visits for Jessica Okafor."""
    provider = find_provider(state, "prov_3")
    provider["virtualVisitActivated"] = True
    provider["virtualVisitInstructions"] = "Join your telehealth visit at https://zoom.us/j/1234567890. Please test your camera and microphone beforehand."


def solve_task_m8(state):
    """Add CPT code 99205."""
    state["practiceSettings"]["cptCodes"].append({
        "code": "99205",
        "description": "Office visit, new patient, high complexity",
    })


def solve_task_m9(state):
    """Schedule in-person appointment for Emily Thompson."""
    patient = find_patient_by_name(state, "Emily", "Thompson")
    state["appointments"].append({
        "id": next_appointment_id(state),
        "patientId": patient["id"],
        "providerId": "prov_1",
        "date": "2026-03-15T10:00:00Z",
        "place": "in_person",
        "status": "scheduled",
        "virtualVisitInstructions": None,
        "reason": "General check-up",
    })


def solve_task_m10(state):
    """Remove Front Desk from Dr. Torres's General Question routing."""
    routing = state["messageRouting"]["prov_2"]
    routing["General Question"] = [r for r in routing["General Question"] if r != "ug_1"]


def solve_task_m11(state):
    """Rename Main Office to SF Main Office."""
    loc = find_location_by_name(state, "Main Office")
    loc["name"] = "SF Main Office"


def solve_task_m12(state):
    """Disable Stephanie Rivera's Passport."""
    patient = find_patient_by_name(state, "Stephanie", "Rivera")
    patient["passportAccountDisabled"] = True
    patient["passportStatus"] = "not_invited"


def solve_task_m13(state):
    """Change Helen Matsumoto's sharing level to 1."""
    patient = find_patient_by_name(state, "Helen", "Matsumoto")
    patient["passportSharingLevel"] = 1


def solve_task_m14(state):
    """Add Clinical Team to Dr. Chen's Test Results routing."""
    routing = state["messageRouting"]["prov_1"]["Test Results"]
    if "ug_2" not in routing:
        routing.append("ug_2")


def solve_task_m15(state):
    """Send letter to David Park about spirometry, no reply allowed."""
    conv_id = next_conversation_id(state)
    letter = make_letter(
        state, "pat_7", conv_id,
        "Spirometry Test Scheduling",
        "Hi David, please schedule your next spirometry test at your earliest convenience.",
        doNotAllowResponse=True,
    )
    state["patientLetters"].append(letter)


def solve_task_m16(state):
    """Schedule virtual appointment for Andrew McIntyre."""
    patient = find_patient_by_name(state, "Andrew", "McIntyre")
    state["appointments"].append({
        "id": next_appointment_id(state),
        "patientId": patient["id"],
        "providerId": "prov_2",
        "date": "2026-03-20T15:00:00Z",
        "place": "virtual",
        "status": "scheduled",
        "virtualVisitInstructions": "Join at https://zoom.us/j/7261048395?pwd=def456",
        "reason": "GI follow-up",
    })


def solve_task_m17(state):
    """Opt David Park out of SMS."""
    patient = find_patient_by_name(state, "David", "Park")
    patient["smsOptInStatus"] = "opted_out"


def solve_task_m18(state):
    """Add emergency contact for Kevin Adebayo."""
    patient = find_patient_by_name(state, "Kevin", "Adebayo")
    patient["emergencyContact"] = {
        "name": "Grace Adebayo",
        "phone": "(650) 555-1122",
        "relationship": "Wife",
    }


def solve_task_m19(state):
    """End Maria Gonzalez's lab results conversation (conv_9)."""
    for letter in state["patientLetters"]:
        if letter["conversationId"] == "conv_9":
            letter["conversationState"] = "ended"


def solve_task_m20(state):
    """Change James Rodriguez's sharing level to 4."""
    patient = find_patient_by_name(state, "James", "Rodriguez")
    patient["passportSharingLevel"] = 4


# ── Hard tasks ───────────────────────────────────────────────────────

def solve_task_h1(state):
    """Tag Dr. Chen's diabetes patients as High Risk."""
    for patient in state["patients"]:
        if patient["assignedProviderId"] != "prov_1":
            continue
        profile = patient.get("clinicalProfile", {})
        problems = profile.get("problemList", [])
        has_diabetes = any("diabetes" in p.lower() for p in problems)
        if has_diabetes and "High Risk" not in patient["tags"]:
            patient["tags"].append("High Risk")


def solve_task_h2(state):
    """Reply to Christine Lee and end conversation."""
    letter = make_letter(
        state, "pat_22", "conv_21",
        "Re: General Question",
        "Hi Christine, I understand the insomnia is affecting you. Let's try increasing your Trazodone to 100mg at bedtime. If that doesn't help after a week, we can explore other options.",
        conversationState="ended",
    )
    state["patientLetters"].append(letter)
    for l in state["patientLetters"]:
        if l["conversationId"] == "conv_21":
            l["conversationState"] = "ended"


def solve_task_h3(state):
    """Send Passport invitations to Dr. Kim's uninvited patients."""
    for patient in state["patients"]:
        if patient["assignedProviderId"] == "prov_4" and patient["passportStatus"] == "not_invited":
            patient["passportStatus"] = "invited"
            patient["invitedAt"] = TIMESTAMP
            patient["invitationCode"] = "9999990"


def solve_task_h4(state):
    """Route Billing Question to Front Desk for all providers."""
    for prov in state["providers"]:
        pid = prov["id"]
        if pid not in state["messageRouting"]:
            state["messageRouting"][pid] = {}
        routing = state["messageRouting"][pid].get("Billing Question", [])
        if "ug_1" not in routing:
            routing.append("ug_1")
        state["messageRouting"][pid]["Billing Question"] = routing


def solve_task_h5(state):
    """Read Raymond Copeland's message and reply."""
    letter = find_letter(state, "ltr_46")
    letter["isRead"] = True
    letter["readAt"] = TIMESTAMP
    reply = make_letter(
        state, "pat_35", "conv_34",
        "Re: General Question",
        "Hi Raymond, increased thirst and urination can indicate your blood sugar needs better control. Please come in for an updated A1C test. In the meantime, continue your current medications and monitor your blood sugar closely.",
    )
    state["patientLetters"].append(reply)


def solve_task_h6(state):
    """Send message to Helen Matsumoto about cognitive assessment."""
    # Reply to conv_7 (Ken wrote on behalf of Helen)
    reply = make_letter(
        state, "pat_10", "conv_7",
        "Re: General Question",
        "Dear Ken, thank you for reaching out about your mother. The increased forgetfulness and difficulty recognizing family members warrants an evaluation. Her cognitive assessment follow-up is scheduled for March 6th. Please bring her in at 11 AM.",
    )
    state["patientLetters"].append(reply)


def solve_task_h7(state):
    """Cancel all virtual March 2026 appointments and deactivate Dr. Kim's virtual visits."""
    for appt in state["appointments"]:
        if (appt["place"] == "virtual"
            and appt["status"] == "scheduled"
            and appt["date"].startswith("2026-03")):
            appt["status"] = "cancelled"
    provider = find_provider(state, "prov_4")
    provider["virtualVisitActivated"] = False


def solve_task_h8(state):
    """Reply to Barbara Andersen and mark all unread inbox messages as read."""
    # Mark ltr_47 as read
    ltr_47 = find_letter(state, "ltr_47")
    ltr_47["isRead"] = True
    ltr_47["readAt"] = TIMESTAMP
    # Reply
    reply = make_letter(
        state, "pat_38", "conv_35",
        "Re: Test Results",
        "Hi Barbara, your lab results are in. Your B12 level has improved to normal range and your iron is trending up. Continue your current supplements and we'll recheck in 3 months.",
    )
    state["patientLetters"].append(reply)
    # Mark all remaining unread from-patient messages as read
    unread_ids = ["ltr_4", "ltr_6", "ltr_10", "ltr_15", "ltr_19", "ltr_20",
                  "ltr_23", "ltr_24", "ltr_29", "ltr_39", "ltr_46"]
    for l in state["patientLetters"]:
        if l["id"] in unread_ids and not l["isRead"]:
            l["isRead"] = True
            l["readAt"] = TIMESTAMP


def solve_task_h9(state):
    """Acknowledge all unacknowledged reminders."""
    for reminder in state["reminders"]:
        reminder["acknowledged"] = True


def solve_task_h10(state):
    """Add Clinical Team to all Dr. Chen's message routing categories."""
    for category in MESSAGE_CATEGORIES:
        routing = state["messageRouting"]["prov_1"].get(category, [])
        if "ug_2" not in routing:
            routing.append("ug_2")
        state["messageRouting"]["prov_1"][category] = routing


def solve_task_h11(state):
    """Add Chronic Care tag to geriatric patients who lack it."""
    for patient in state["patients"]:
        if "Geriatric" in patient["tags"] and "Chronic Care" not in patient["tags"]:
            patient["tags"].append("Chronic Care")


def solve_task_h12(state):
    """Reply to all unread patient messages."""
    unread_convs = {
        "conv_2": "pat_2",
        "conv_4": "pat_4",
        "conv_7": "pat_10",
        "conv_10": "pat_16",
        "conv_13": "pat_32",
        "conv_14": "pat_30",
        "conv_16": "pat_29",
        "conv_17": "pat_50",
        "conv_21": "pat_22",
        "conv_28": "pat_40",
        "conv_34": "pat_35",
        "conv_35": "pat_38",
    }
    for conv_id, pat_id in unread_convs.items():
        # Get the original subject from the conversation
        orig = None
        for l in state["patientLetters"]:
            if l["conversationId"] == conv_id:
                orig = l
                break
        subject = f"Re: {orig['subject']}" if orig else "Re: Your Message"
        reply = make_letter(
            state, pat_id, conv_id,
            subject,
            "Thank you for your message. I will review your concern and get back to you shortly.",
        )
        state["patientLetters"].append(reply)


def solve_task_h13(state):
    """End open conversations inactive before Feb 25, 2026."""
    # Identify open conversations with last activity before 2026-02-25
    cutoff = "2026-02-25T00:00:00Z"
    conversations = {}
    for l in state["patientLetters"]:
        cid = l["conversationId"]
        if cid not in conversations:
            conversations[cid] = {"letters": [], "all_ended": True, "max_date": ""}
        conversations[cid]["letters"].append(l)
        if l.get("conversationState") != "ended":
            conversations[cid]["all_ended"] = False
        sent = l.get("sentAt") or ""
        if sent > conversations[cid]["max_date"]:
            conversations[cid]["max_date"] = sent

    for cid, info in conversations.items():
        if info["all_ended"]:
            continue
        if info["max_date"] and info["max_date"] < cutoff:
            for l in info["letters"]:
                l["conversationState"] = "ended"


def solve_task_h14(state):
    """Change Dr. Torres's notification to none and remove from Dr. Chen's General Question routing."""
    provider = find_provider(state, "prov_2")
    provider["notificationTimeframe"] = "none"
    routing = state["messageRouting"]["prov_1"]["General Question"]
    state["messageRouting"]["prov_1"]["General Question"] = [
        r for r in routing if r != "prov_2"
    ]


def solve_task_h15(state):
    """Reply to Diane Foster-Hutchinson's referral request and end conversation."""
    reply = make_letter(
        state, "pat_16", "conv_10",
        "Re: Referral Request",
        "Hi Diane, I've prepared a referral to Dr. Lisa Park, an excellent allergist in SF who specializes in venom allergies. Her office will contact you to schedule an appointment.",
        conversationState="ended",
    )
    state["patientLetters"].append(reply)
    for l in state["patientLetters"]:
        if l["conversationId"] == "conv_10":
            l["conversationState"] = "ended"


def solve_task_h16(state):
    """Send bulk letter to all Geriatric patients about wellness visit."""
    geriatric_ids = [
        p["id"] for p in state["patients"] if "Geriatric" in p["tags"]
    ]
    bulk_id = next_bulk_letter_id(state)
    state["bulkLetters"].append({
        "id": bulk_id,
        "description": "Annual Wellness Visit Reminder for Geriatric Patients",
        "subject": "Schedule Your Annual Wellness Visit",
        "body": "Dear patient, please schedule your annual wellness visit at your earliest convenience. Regular check-ups are important for maintaining your health.",
        "sentAt": TIMESTAMP,
        "sentBy": "prov_1",
        "targetCount": len(geriatric_ids),
        "allowResponse": True,
    })
    conv_id = next_conversation_id(state)
    for pat_id in geriatric_ids:
        state["patientLetters"].append({
            "id": next_letter_id(state),
            "patientId": pat_id,
            "conversationId": f"{conv_id}_{pat_id}",
            "direction": "to_patient",
            "subject": "Schedule Your Annual Wellness Visit",
            "body": "Dear patient, please schedule your annual wellness visit at your earliest convenience. Regular check-ups are important for maintaining your health.",
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
    """Reply to Howard Blackwell about gardening and schedule virtual follow-up."""
    reply = make_letter(
        state, "pat_27", "conv_24",
        "Re: General Question",
        "Mr. Blackwell, light gardening should be fine this spring. Start slowly and avoid heavy lifting. Stop if you feel short of breath or have any chest discomfort.",
    )
    state["patientLetters"].append(reply)
    state["appointments"].append({
        "id": next_appointment_id(state),
        "patientId": "pat_27",
        "providerId": "prov_4",
        "date": "2026-04-01T14:00:00Z",
        "place": "virtual",
        "status": "scheduled",
        "virtualVisitInstructions": "Join at https://zoom.us/j/5029384716?pwd=ghi789",
        "reason": "CHF follow-up",
    })


def solve_task_h18(state):
    """Invite Dr. Kim's uninvited patients to Passport and disable auto-invite."""
    for patient in state["patients"]:
        if patient["assignedProviderId"] == "prov_4" and patient["passportStatus"] == "not_invited":
            patient["passportStatus"] = "invited"
            patient["invitedAt"] = TIMESTAMP
            patient["invitationCode"] = "9999990"
    state["practiceSettings"]["bookingSiteAutoInvite"] = False


def solve_task_h19(state):
    """Add Insurance Pending tag and send Passport invitations to Megan Burke and Craig Bennet."""
    for name in [("Megan", "Burke"), ("Craig", "Bennet")]:
        patient = find_patient_by_name(state, name[0], name[1])
        if "Insurance Pending" not in patient["tags"]:
            patient["tags"].append("Insurance Pending")
        patient["passportStatus"] = "invited"
        patient["invitedAt"] = TIMESTAMP
        patient["invitationCode"] = "9999990"


def solve_task_h20(state):
    """Remove telephone E/M CPT codes and add 99205."""
    telephone_codes = {"99441", "99442", "99443"}
    state["practiceSettings"]["cptCodes"] = [
        c for c in state["practiceSettings"]["cptCodes"]
        if c["code"] not in telephone_codes
    ]
    state["practiceSettings"]["cptCodes"].append({
        "code": "99205",
        "description": "Office visit, new patient, high complexity",
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


def find_free_port(start=9000):
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
        resp = requests.post(f"{server_url}/api/reset")
        if resp.status_code != 200:
            return task_id, False, f"Reset failed: HTTP {resp.status_code}"

        time.sleep(0.3)

        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return task_id, False, f"Could not read state after reset: HTTP {resp.status_code}"
        state = resp.json()

        solver(state)

        resp = requests.put(
            f"{server_url}/api/state",
            json=state,
            headers={"Content-Type": "application/json"},
        )
        if resp.status_code != 200:
            return task_id, False, f"Could not write state: HTTP {resp.status_code}"

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
