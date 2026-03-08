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


# ── Hardened tasks (h21–h40) ─────────────────────────────────────────

def solve_task_h21(state):
    """Reply to Raymond Copeland about A1C + add High Risk tag."""
    letter = find_letter(state, "ltr_46")
    letter["isRead"] = True
    letter["readAt"] = TIMESTAMP
    reply = make_letter(
        state, "pat_35", "conv_34",
        "Re: General Question",
        "Hi Raymond, increased thirst and urination can indicate changes in blood sugar control. Please come in for an A1C test so we can evaluate your current levels.",
    )
    state["patientLetters"].append(reply)
    patient = find_patient_by_name(state, "Raymond", "Copeland")
    if "High Risk" not in patient["tags"]:
        patient["tags"].append("High Risk")


def solve_task_h22(state):
    """Change sharing level to 3 for Diabetes Management patients below 3."""
    for patient in state["patients"]:
        if "Diabetes Management" in patient.get("tags", []):
            if patient.get("passportSharingLevel", 2) < 3:
                patient["passportSharingLevel"] = 3


def solve_task_h23(state):
    """Activate virtual visits for the nurse practitioner."""
    for prov in state["providers"]:
        if prov["role"] == "nurse_practitioner":
            prov["virtualVisitActivated"] = True
            prov["virtualVisitInstructions"] = "Please join your visit at https://zoom.us/j/5551234567"
            break


def solve_task_h24(state):
    """Send bulk letter to New Patient tagged patients, no responses."""
    new_patient_ids = [
        p["id"] for p in state["patients"] if "New Patient" in p.get("tags", [])
    ]
    bulk_id = next_bulk_letter_id(state)
    state["bulkLetters"].append({
        "id": bulk_id,
        "description": "Patient portal registration encouragement",
        "subject": "Register for Patient Portal",
        "body": "Dear patient, we encourage you to register for our patient portal.",
        "sentAt": TIMESTAMP,
        "sentBy": "prov_1",
        "targetCount": len(new_patient_ids),
        "allowResponse": False,
    })
    conv_id = next_conversation_id(state)
    for pat_id in new_patient_ids:
        state["patientLetters"].append({
            "id": next_letter_id(state),
            "patientId": pat_id,
            "conversationId": f"{conv_id}_{pat_id}",
            "direction": "to_patient",
            "subject": "Register for Patient Portal",
            "body": "Dear patient, we encourage you to register for our patient portal.",
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


def solve_task_h25(state):
    """Send letters to VIP + Geriatric patients about wellness visits."""
    targets = [
        p for p in state["patients"]
        if "VIP" in p.get("tags", []) and "Geriatric" in p.get("tags", [])
    ]
    for patient in targets:
        conv_id = next_conversation_id(state)
        letter = make_letter(
            state, patient["id"], conv_id,
            "Annual Wellness Visit",
            f"Dear {patient['firstName']}, please schedule your annual wellness visit.",
        )
        state["patientLetters"].append(letter)


def solve_task_h26(state):
    """Reply to Andrew McIntyre + cancel virtual + schedule in-person."""
    reply = make_letter(
        state, "pat_29", "conv_16",
        "Re: General Question",
        "Hi Andrew, let's switch your appointment to in-person so I can do a proper examination.",
    )
    state["patientLetters"].append(reply)
    appt = find_entity(state["appointments"], id="appt_6")
    appt["status"] = "cancelled"
    state["appointments"].append({
        "id": next_appointment_id(state),
        "patientId": "pat_29",
        "providerId": "prov_2",
        "date": "2026-03-07T15:00:00Z",
        "place": "in_person",
        "status": "scheduled",
        "virtualVisitInstructions": None,
        "reason": "GI follow-up",
    })


def solve_task_h27(state):
    """Add All Providers to MRR routing for all providers + add North Beach Office."""
    for prov in state["providers"]:
        pid = prov["id"]
        if pid not in state["messageRouting"]:
            state["messageRouting"][pid] = {}
        routing = state["messageRouting"][pid].get("Medical Records Request", [])
        if "ug_4" not in routing:
            routing.append("ug_4")
        state["messageRouting"][pid]["Medical Records Request"] = routing
    state["practiceSettings"]["practiceLocations"].append({
        "id": next_location_id(state),
        "name": "North Beach Office",
        "address": "2200 Mason Street, San Francisco, CA 94133",
        "posCode": "11",
        "posDescription": "Office",
    })


def solve_task_h28(state):
    """Update Anthony Petrov's EC phone + send Passport invitation."""
    patient = find_patient_by_name(state, "Anthony", "Petrov")
    patient["emergencyContact"]["phone"] = "(510) 555-8888"
    patient["passportStatus"] = "invited"
    patient["invitedAt"] = TIMESTAMP
    patient["invitationCode"] = "9999990"


def solve_task_h29(state):
    """Replace Front Desk with Clinical Team in Okafor's routing."""
    routing = state["messageRouting"]["prov_3"]
    for cat in routing:
        routing[cat] = ["ug_2" if r == "ug_1" else r for r in routing[cat]]


def solve_task_h30(state):
    """Add Clinical Team to all of Dr. Kim's routing categories."""
    for category in MESSAGE_CATEGORIES:
        routing = state["messageRouting"]["prov_4"].get(category, [])
        if "ug_2" not in routing:
            routing.append("ug_2")
        state["messageRouting"]["prov_4"][category] = routing


def solve_task_h31(state):
    """Opt out SMS for Geriatric patients currently opted in."""
    for patient in state["patients"]:
        if "Geriatric" in patient.get("tags", []) and patient.get("smsOptInStatus") == "opted_in":
            patient["smsOptInStatus"] = "opted_out"


def solve_task_h32(state):
    """Cancel the virtual appointment on March 5, 2026."""
    appt = find_entity(state["appointments"], id="appt_14")
    appt["status"] = "cancelled"


def solve_task_h33(state):
    """Update EC phone for earliest registered patient (Howard Blackwell)."""
    patient = find_patient_by_name(state, "Howard", "Blackwell")
    patient["emergencyContact"]["phone"] = "(415) 555-9999"


def solve_task_h34(state):
    """Change PA's notification to 1 week + add to Chen's Referral Request routing."""
    pa = None
    for prov in state["providers"]:
        if prov["role"] == "physician_assistant":
            pa = prov
            break
    pa["notificationTimeframe"] = "1_week"
    routing = state["messageRouting"]["prov_1"]["Referral Request"]
    if pa["id"] not in routing:
        routing.append(pa["id"])


def solve_task_h35(state):
    """Add Clinical Team to Dr. Kim's Billing Question routing."""
    routing = state["messageRouting"]["prov_4"]["Billing Question"]
    if "ug_2" not in routing:
        routing.append("ug_2")


def solve_task_h36(state):
    """Mark all unread inbox messages as read + change Chen's notification to none."""
    for letter in state["patientLetters"]:
        if letter["direction"] == "from_patient" and not letter["isRead"]:
            letter["isRead"] = True
            letter["readAt"] = TIMESTAMP
    provider = find_provider(state, "prov_1")
    provider["notificationTimeframe"] = "none"


def solve_task_h37(state):
    """Add Telehealth Preferred tag to patients with virtual appointments who lack it."""
    virtual_patient_ids = set()
    for appt in state["appointments"]:
        if appt["place"] == "virtual" and appt["status"] == "scheduled":
            virtual_patient_ids.add(appt["patientId"])
    for patient in state["patients"]:
        if patient["id"] in virtual_patient_ids:
            if "Telehealth Preferred" not in patient.get("tags", []):
                patient["tags"].append("Telehealth Preferred")


def solve_task_h38(state):
    """Invite all uninvited patients + change Chen's sharing to 4."""
    for patient in state["patients"]:
        if patient["passportStatus"] == "not_invited":
            patient["passportStatus"] = "invited"
            patient["invitedAt"] = TIMESTAMP
            patient["invitationCode"] = "9999990"
    provider = find_provider(state, "prov_1")
    provider["sharingDefault"] = 4


def solve_task_h39(state):
    """Reply to Priya Sharma, end conversation, add Insurance Pending tag."""
    reply = make_letter(
        state, "pat_32", "conv_13",
        "Re: Medical Records Request",
        "Hi Priya, please visit our front desk to fill out a records release form.",
        conversationState="ended",
    )
    state["patientLetters"].append(reply)
    for l in state["patientLetters"]:
        if l["conversationId"] == "conv_13":
            l["conversationState"] = "ended"
    patient = find_patient_by_name(state, "Priya", "Sharma")
    if "Insurance Pending" not in patient["tags"]:
        patient["tags"].append("Insurance Pending")


def solve_task_h40(state):
    """Change notification to 1 week for providers with 24 hours."""
    for prov in state["providers"]:
        if prov["notificationTimeframe"] == "24_hours":
            prov["notificationTimeframe"] = "1_week"


# ── Hardened tasks (h41–h60) ─────────────────────────────────────────

def solve_task_h41(state):
    """Schedule in-person podiatry follow-up for Patricia O'Brien (vs_2 referral)."""
    state["appointments"].append({
        "id": next_appointment_id(state),
        "patientId": "pat_8",
        "providerId": "prov_1",
        "date": "2026-04-15T14:00:00Z",
        "place": "in_person",
        "status": "scheduled",
        "virtualVisitInstructions": None,
        "reason": "Podiatry referral follow-up",
    })


def solve_task_h42(state):
    """Update Helen Matsumoto's EC phone and sharing level."""
    patient = find_patient_by_name(state, "Helen", "Matsumoto")
    patient["emergencyContact"]["phone"] = "(415) 555-9900"
    patient["passportSharingLevel"] = 4


def solve_task_h43(state):
    """Update Geriatric patients below sharing level 3 to level 3."""
    for patient in state["patients"]:
        if "Geriatric" in patient.get("tags", []):
            if patient.get("passportSharingLevel", 2) < 3:
                patient["passportSharingLevel"] = 3


def solve_task_h44(state):
    """Send no-reply fasting reminder to Warfarin check patient (Robert Washington)."""
    conv_id = next_conversation_id(state)
    letter = make_letter(
        state, "pat_3", conv_id,
        "Warfarin Check Appointment Reminder",
        "Dear Mr. Washington, please fast for 12 hours before your upcoming blood draw and bring your current medication list.",
        doNotAllowResponse=True,
    )
    state["patientLetters"].append(letter)


def solve_task_h45(state):
    """Cancel Howard Blackwell's virtual appt, reschedule in-person same date."""
    appt = find_entity(state["appointments"], id="appt_9")
    appt["status"] = "cancelled"
    state["appointments"].append({
        "id": next_appointment_id(state),
        "patientId": "pat_27",
        "providerId": "prov_4",
        "date": "2026-03-15T14:00:00Z",
        "place": "in_person",
        "status": "scheduled",
        "virtualVisitInstructions": None,
        "reason": "CHF management review",
    })


def solve_task_h46(state):
    """Add Nurses (ug_3) to Prescription Refill routing for all providers."""
    for prov in state["providers"]:
        pid = prov["id"]
        routing = state["messageRouting"][pid].get("Prescription Refill", [])
        if "ug_3" not in routing:
            routing.append("ug_3")
        state["messageRouting"][pid]["Prescription Refill"] = routing


def solve_task_h47(state):
    """Resend Passport invite for Tyler Robinson + add Telehealth Preferred tag."""
    patient = find_patient_by_name(state, "Tyler", "Robinson")
    patient["invitedAt"] = TIMESTAMP
    patient["invitationCode"] = "8888888"
    if "Telehealth Preferred" not in patient["tags"]:
        patient["tags"].append("Telehealth Preferred")


def solve_task_h48(state):
    """Reply to Susan Cho, cancel virtual appt, schedule in-person."""
    reply = make_letter(
        state, "pat_40", "conv_28",
        "Re: Appointment Request",
        "Hi Susan, given the flare-up severity, I'd recommend coming in for an in-person evaluation instead. I've rescheduled your appointment.",
    )
    state["patientLetters"].append(reply)
    appt = find_entity(state["appointments"], id="appt_14")
    appt["status"] = "cancelled"
    state["appointments"].append({
        "id": next_appointment_id(state),
        "patientId": "pat_40",
        "providerId": "prov_3",
        "date": "2026-03-12T15:00:00Z",
        "place": "in_person",
        "status": "scheduled",
        "virtualVisitInstructions": None,
        "reason": "Urticaria flare evaluation",
    })


def solve_task_h49(state):
    """Send letter to older BPH patient (DeLuca), tag younger (Tran)."""
    conv_id = next_conversation_id(state)
    letter = make_letter(
        state, "pat_19", conv_id,
        "Prostate Check-up Reminder",
        "Mr. DeLuca, please schedule your next prostate check-up at your convenience.",
    )
    state["patientLetters"].append(letter)
    patient = find_patient_by_name(state, "Philip", "Tran")
    if "Chronic Care" not in patient["tags"]:
        patient["tags"].append("Chronic Care")


def solve_task_h50(state):
    """Opt Geriatric ACE-intolerant patient into SMS, tag the other High Risk."""
    pat_33 = find_patient_by_name(state, "Douglas", "Fitzgerald")
    pat_33["smsOptInStatus"] = "opted_in"
    pat_14 = find_patient_by_name(state, "Maria", "Gonzalez")
    if "High Risk" not in pat_14["tags"]:
        pat_14["tags"].append("High Risk")


def solve_task_h51(state):
    """Change chat mode + activate virtual for Amanda Wright."""
    state["practiceSettings"]["videoSettings"]["chatMode"] = "everyone_in_waiting_room"
    prov = find_provider(state, "prov_5")
    prov["virtualVisitActivated"] = True
    prov["virtualVisitInstructions"] = "Please join at https://meet.bayareafamilymed.com/wright"


def solve_task_h52(state):
    """Reply to Aisha Patel's ankle swelling message + tag High Risk."""
    reply = make_letter(
        state, "pat_20", "conv_22",
        "Re: General Question",
        "Hi Aisha, some ankle swelling is normal at this stage of pregnancy, but please monitor for any sudden increase or if it's accompanied by headaches or visual changes. Contact us immediately if that happens.",
    )
    state["patientLetters"].append(reply)
    patient = find_patient_by_name(state, "Aisha", "Patel")
    if "High Risk" not in patient["tags"]:
        patient["tags"].append("High Risk")


def solve_task_h53(state):
    """Reply to Catherine Morales, acknowledge rem_6, change sharing to 3."""
    reply = make_letter(
        state, "pat_46", "conv_27",
        "Re: General Question",
        "Hi Catherine, yes please continue taking the Levothyroxine on an empty stomach, 30-60 minutes before breakfast. And yes, Vitamin D is still important - keep taking it.",
    )
    state["patientLetters"].append(reply)
    rem = find_reminder(state, "rem_6")
    rem["acknowledged"] = True
    patient = find_patient_by_name(state, "Catherine", "Morales")
    patient["passportSharingLevel"] = 3


def solve_task_h54(state):
    """Reply to Sophia Nguyen's thyroid check-up request + acknowledge rem_9."""
    reply = make_letter(
        state, "pat_4", "conv_4",
        "Re: Appointment Request",
        "Hi Sophia, I'll arrange your annual thyroid check-up via telehealth. Our front desk will reach out with available times.",
    )
    state["patientLetters"].append(reply)
    rem = find_reminder(state, "rem_9")
    rem["acknowledged"] = True


def solve_task_h55(state):
    """Invite Dr. Torres's uninvited patients, set sharing to 3 for all invited."""
    for patient in state["patients"]:
        if patient["assignedProviderId"] == "prov_2" and patient["passportStatus"] == "not_invited":
            patient["passportStatus"] = "invited"
            patient["invitedAt"] = TIMESTAMP
            patient["invitationCode"] = "9999990"
    for patient in state["patients"]:
        if patient["assignedProviderId"] == "prov_2" and patient["passportStatus"] == "invited":
            patient["passportSharingLevel"] = 3


def solve_task_h56(state):
    """Update William Chang's email and resend Passport invitation."""
    patient = find_patient_by_name(state, "William", "Chang")
    patient["email"] = "william.chang.new@gmail.com"
    patient["invitedAt"] = TIMESTAMP
    patient["invitationCode"] = "8888888"


def solve_task_h57(state):
    """Add Pacific Heights Office, add CPT 99215, change Dr. Kim sharing to 3."""
    state["practiceSettings"]["practiceLocations"].append({
        "id": next_location_id(state),
        "name": "Pacific Heights Office",
        "address": "3500 California Street, San Francisco, CA 94118",
        "posCode": "11",
        "posDescription": "Office",
    })
    state["practiceSettings"]["cptCodes"].append({
        "code": "99215",
        "description": "Office visit, established patient, comprehensive",
    })
    prov = find_provider(state, "prov_4")
    prov["sharingDefault"] = 3


def solve_task_h58(state):
    """Send no-reply letters to both Mental Health tagged patients."""
    for pat_id in ["pat_12", "pat_22"]:
        conv_id = next_conversation_id(state)
        letter = make_letter(
            state, pat_id, conv_id,
            "Therapy Follow-up Appointment",
            "Please schedule your next therapy follow-up appointment at your earliest convenience.",
            doNotAllowResponse=True,
        )
        state["patientLetters"].append(letter)


def solve_task_h59(state):
    """Reply to Kevin Adebayo's billing conversation, end it, add tag."""
    reply = make_letter(
        state, "pat_11", "conv_8",
        "Re: Billing Question",
        "Hi Kevin, the billing issue has been resolved. The charge was adjusted and your insurance has been rebilled correctly.",
        conversationState="ended",
    )
    state["patientLetters"].append(reply)
    for l in state["patientLetters"]:
        if l["conversationId"] == "conv_8":
            l["conversationState"] = "ended"
    patient = find_patient_by_name(state, "Kevin", "Adebayo")
    if "Insurance Pending" not in patient["tags"]:
        patient["tags"].append("Insurance Pending")


def solve_task_h60(state):
    """Add 48-hour providers to Dr. Torres's Referral Request routing."""
    providers_48h = [
        prov["id"] for prov in state["providers"]
        if prov["notificationTimeframe"] == "48_hours"
    ]
    routing = state["messageRouting"]["prov_2"]["Referral Request"]
    for pid in providers_48h:
        if pid not in routing:
            routing.append(pid)


# ── Hardened tasks (h61–h80) ─────────────────────────────────────────

def solve_task_h61(state):
    """Add High Risk tag to all patients with Penicillin allergy who lack it."""
    for patient in state["patients"]:
        allergies = patient.get("clinicalProfile", {}).get("allergies", [])
        has_penicillin = any("penicillin" in a.lower() for a in allergies)
        if has_penicillin and "High Risk" not in patient["tags"]:
            patient["tags"].append("High Risk")


def solve_task_h62(state):
    """Remove Front Desk from Appointment Request, add All Providers to Other for all providers."""
    for prov in state["providers"]:
        pid = prov["id"]
        # Remove ug_1 from Appointment Request
        appt_routing = state["messageRouting"][pid].get("Appointment Request", [])
        state["messageRouting"][pid]["Appointment Request"] = [
            r for r in appt_routing if r != "ug_1"
        ]
        # Add ug_4 to Other
        other_routing = state["messageRouting"][pid].get("Other", [])
        if "ug_4" not in other_routing:
            other_routing.append("ug_4")
        state["messageRouting"][pid]["Other"] = other_routing


def solve_task_h63(state):
    """Reply to Howard Blackwell (BNP improved) and update EC phone."""
    reply = make_letter(
        state, "pat_27", "conv_24",
        "Re: General Question",
        "Mr. Blackwell, your BNP levels have improved and you can resume light activity like gardening. Start slowly and avoid overexertion.",
    )
    state["patientLetters"].append(reply)
    patient = find_patient_by_name(state, "Howard", "Blackwell")
    patient["emergencyContact"]["phone"] = "(650) 555-0001"


def solve_task_h64(state):
    """Chronic Care differentiated: below 3 → upgrade, 3+ → add VIP."""
    for patient in state["patients"]:
        if "Chronic Care" not in patient.get("tags", []):
            continue
        level = patient.get("passportSharingLevel", 2)
        if level < 3:
            patient["passportSharingLevel"] = 3
        else:
            if "VIP" not in patient["tags"]:
                patient["tags"].append("VIP")


def solve_task_h65(state):
    """Schedule appointment for Linda Garcia (withdrawal effects)."""
    state["appointments"].append({
        "id": next_appointment_id(state),
        "patientId": "pat_6",
        "providerId": "prov_3",
        "date": "2026-03-25T09:00:00Z",
        "place": "in_person",
        "status": "scheduled",
        "virtualVisitInstructions": None,
        "reason": "Medication review",
    })


def solve_task_h66(state):
    """Set notification timeframes based on virtual visit activation."""
    for prov in state["providers"]:
        if prov.get("virtualVisitActivated"):
            prov["notificationTimeframe"] = "72_hours"
        else:
            prov["notificationTimeframe"] = "1_week"


def solve_task_h67(state):
    """Reply to Frank DeLuca, end conv_20, acknowledge rem_2."""
    reply = make_letter(
        state, "pat_19", "conv_20",
        "Re: General Question",
        "Mr. DeLuca, we can consider adjusting your Tamsulosin. Let's schedule a follow-up to discuss your symptoms.",
        conversationState="ended",
    )
    state["patientLetters"].append(reply)
    for l in state["patientLetters"]:
        if l["conversationId"] == "conv_20":
            l["conversationState"] = "ended"
    rem = find_reminder(state, "rem_2")
    rem["acknowledged"] = True


def solve_task_h68(state):
    """Remove New Patient tag from registered patients."""
    for patient in state["patients"]:
        if ("New Patient" in patient.get("tags", [])
                and patient.get("passportStatus") == "registered"):
            patient["tags"] = [t for t in patient["tags"] if t != "New Patient"]


def solve_task_h69(state):
    """Send letters to Spanish Speaking patients, upgrade pat_46 sharing level."""
    for pat_id in ["pat_14", "pat_46"]:
        conv_id = next_conversation_id(state)
        letter = make_letter(
            state, pat_id, conv_id,
            "Practice Survey",
            "We'd like to invite you to participate in our upcoming practice survey. Your feedback is valuable to improving our services.",
        )
        state["patientLetters"].append(letter)
    patient = find_patient_by_name(state, "Catherine", "Morales")
    if patient.get("passportSharingLevel", 2) < 3:
        patient["passportSharingLevel"] = 3


def solve_task_h70(state):
    """Reply to Deborah Takahashi about calcium + schedule appointment."""
    reply = make_letter(
        state, "pat_50", "conv_17",
        "Re: Prescription Refill",
        "Hi Deborah, I recommend switching to calcium citrate, which is gentler on the stomach. I'll schedule a follow-up to review your supplements.",
    )
    state["patientLetters"].append(reply)
    state["appointments"].append({
        "id": next_appointment_id(state),
        "patientId": "pat_50",
        "providerId": "prov_1",
        "date": "2026-04-05T10:00:00Z",
        "place": "in_person",
        "status": "scheduled",
        "virtualVisitInstructions": None,
        "reason": "Supplement review",
    })


def solve_task_h71(state):
    """Send bulk letter to NP patients + change NP notification to 48h."""
    np_patient_ids = [
        p["id"] for p in state["patients"] if p["assignedProviderId"] == "prov_3"
    ]
    bulk_id = next_bulk_letter_id(state)
    state["bulkLetters"].append({
        "id": bulk_id,
        "description": "Schedule change notification for NP patients",
        "subject": "Practice Schedule Change",
        "body": "Dear patient, we are writing to inform you about a schedule change at our practice. Please contact us for updated availability.",
        "sentAt": TIMESTAMP,
        "sentBy": "prov_1",
        "targetCount": len(np_patient_ids),
        "allowResponse": True,
    })
    conv_id = next_conversation_id(state)
    for pat_id in np_patient_ids:
        state["patientLetters"].append({
            "id": next_letter_id(state),
            "patientId": pat_id,
            "conversationId": f"{conv_id}_{pat_id}",
            "direction": "to_patient",
            "subject": "Practice Schedule Change",
            "body": "Dear patient, we are writing to inform you about a schedule change at our practice. Please contact us for updated availability.",
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
    prov = find_provider(state, "prov_3")
    prov["notificationTimeframe"] = "48_hours"


def solve_task_h72(state):
    """Update TIA patient (pat_17): sharing level 4, add tags."""
    patient = find_patient_by_name(state, "Thomas", "Nakamura")
    patient["passportSharingLevel"] = 4
    if "Telehealth Preferred" not in patient["tags"]:
        patient["tags"].append("Telehealth Preferred")
    if "Chronic Care" not in patient["tags"]:
        patient["tags"].append("Chronic Care")


def solve_task_h73(state):
    """Send no-reply reminder letters to patients with March 3-5 appointments."""
    target_patient_ids = set()
    for appt in state["appointments"]:
        date = appt.get("date", "")
        if appt["status"] == "scheduled" and (
            date.startswith("2026-03-03") or
            date.startswith("2026-03-04") or
            date.startswith("2026-03-05")
        ):
            target_patient_ids.add(appt["patientId"])

    for pat_id in target_patient_ids:
        conv_id = next_conversation_id(state)
        letter = make_letter(
            state, pat_id, conv_id,
            "Upcoming Appointment Reminder",
            "This is a reminder about your upcoming appointment. Please arrive on time and bring your insurance card and medication list.",
            doNotAllowResponse=True,
        )
        state["patientLetters"].append(letter)


def solve_task_h74(state):
    """Add Clinical Team, remove Front Desk from all Torres routing."""
    routing = state["messageRouting"]["prov_2"]
    for cat in MESSAGE_CATEGORIES:
        cat_routing = routing.get(cat, [])
        # Remove ug_1
        cat_routing = [r for r in cat_routing if r != "ug_1"]
        # Add ug_2
        if "ug_2" not in cat_routing:
            cat_routing.append("ug_2")
        routing[cat] = cat_routing


def solve_task_h75(state):
    """Update Priya Sharma (MRI brain patient): sharing level 3, add High Risk."""
    patient = find_patient_by_name(state, "Priya", "Sharma")
    patient["passportSharingLevel"] = 3
    if "High Risk" not in patient["tags"]:
        patient["tags"].append("High Risk")


def solve_task_h76(state):
    """Upgrade sharing level for appointment reminder patients below 3."""
    appt_reminder_patient_ids = set()
    for rem in state["reminders"]:
        if rem.get("type") == "appointment_reminder":
            appt_reminder_patient_ids.add(rem["patientId"])
    for patient in state["patients"]:
        if patient["id"] in appt_reminder_patient_ids:
            if patient.get("passportSharingLevel", 2) < 3:
                patient["passportSharingLevel"] = 3


def solve_task_h77(state):
    """Activate PA virtual visits + add to Kim's routing."""
    prov = find_provider(state, "prov_5")
    prov["virtualVisitActivated"] = True
    prov["virtualVisitInstructions"] = "Join at https://meet.bayareafamilymed.com/wright"
    routing = state["messageRouting"]["prov_4"]
    if "prov_5" not in routing.get("Test Results", []):
        routing["Test Results"].append("prov_5")
    if "prov_5" not in routing.get("Referral Request", []):
        routing["Referral Request"].append("prov_5")


def solve_task_h78(state):
    """Reply to forgetfulness message (conv_7), add High Risk, set sharing to 4."""
    reply = make_letter(
        state, "pat_10", "conv_7",
        "Re: General Question",
        "Dear Ken, thank you for letting us know. The changes you describe warrant an evaluation. Please bring your mother in for a cognitive assessment.",
    )
    state["patientLetters"].append(reply)
    patient = find_patient_by_name(state, "Helen", "Matsumoto")
    if "High Risk" not in patient["tags"]:
        patient["tags"].append("High Risk")
    patient["passportSharingLevel"] = 4


def solve_task_h79(state):
    """Remove online digital E/M codes, add 99024 and 99050."""
    digital_codes = {"99421", "99422", "99423"}
    state["practiceSettings"]["cptCodes"] = [
        c for c in state["practiceSettings"]["cptCodes"]
        if c["code"] not in digital_codes
    ]
    state["practiceSettings"]["cptCodes"].append({
        "code": "99024",
        "description": "Post-operative follow-up, no charge",
    })
    state["practiceSettings"]["cptCodes"].append({
        "code": "99050",
        "description": "Services after office hours",
    })


def solve_task_h80(state):
    """Send letter to CABG patient, add tag, update EC phone."""
    conv_id = next_conversation_id(state)
    letter = make_letter(
        state, "pat_3", conv_id,
        "Cardiac Rehab Evaluation",
        "Dear Mr. Washington, we'd like to schedule a cardiac rehabilitation evaluation to support your ongoing recovery. Please contact us to arrange a convenient time.",
    )
    state["patientLetters"].append(letter)
    patient = find_patient_by_name(state, "Robert", "Washington")
    if "Telehealth Preferred" not in patient["tags"]:
        patient["tags"].append("Telehealth Preferred")
    patient["emergencyContact"]["phone"] = "(510) 555-9999"


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
    "task_h41": solve_task_h41,
    "task_h42": solve_task_h42,
    "task_h43": solve_task_h43,
    "task_h44": solve_task_h44,
    "task_h45": solve_task_h45,
    "task_h46": solve_task_h46,
    "task_h47": solve_task_h47,
    "task_h48": solve_task_h48,
    "task_h49": solve_task_h49,
    "task_h50": solve_task_h50,
    "task_h51": solve_task_h51,
    "task_h52": solve_task_h52,
    "task_h53": solve_task_h53,
    "task_h54": solve_task_h54,
    "task_h55": solve_task_h55,
    "task_h56": solve_task_h56,
    "task_h57": solve_task_h57,
    "task_h58": solve_task_h58,
    "task_h59": solve_task_h59,
    "task_h60": solve_task_h60,
    "task_h61": solve_task_h61,
    "task_h62": solve_task_h62,
    "task_h63": solve_task_h63,
    "task_h64": solve_task_h64,
    "task_h65": solve_task_h65,
    "task_h66": solve_task_h66,
    "task_h67": solve_task_h67,
    "task_h68": solve_task_h68,
    "task_h69": solve_task_h69,
    "task_h70": solve_task_h70,
    "task_h71": solve_task_h71,
    "task_h72": solve_task_h72,
    "task_h73": solve_task_h73,
    "task_h74": solve_task_h74,
    "task_h75": solve_task_h75,
    "task_h76": solve_task_h76,
    "task_h77": solve_task_h77,
    "task_h78": solve_task_h78,
    "task_h79": solve_task_h79,
    "task_h80": solve_task_h80,
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
