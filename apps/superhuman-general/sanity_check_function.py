#!/usr/bin/env python3
"""
Sanity check for Superhuman Mail function-test tasks.

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
TASKS_FILE = APP_DIR / "function-tasks.json"

# JS snippet to evaluate data.js and emit the seed state as JSON
_SEED_STATE_JS = """
const fs = require('fs');
const vm = require('vm');
const code = fs.readFileSync(process.argv[1], 'utf8');
vm.runInThisContext(code);

// Replicate what AppState._loadSeedData() does
const state = {
    _seedVersion: SEED_DATA_VERSION,
    emails: JSON.parse(JSON.stringify(EMAILS)),
    contacts: JSON.parse(JSON.stringify(CONTACTS)),
    labels: JSON.parse(JSON.stringify(LABELS)),
    autoLabels: JSON.parse(JSON.stringify(AUTO_LABELS)),
    splits: JSON.parse(JSON.stringify(SPLITS)),
    snippets: JSON.parse(JSON.stringify(SNIPPETS)),
    calendarEvents: JSON.parse(JSON.stringify(CALENDAR_EVENTS)),
    settings: JSON.parse(JSON.stringify(SETTINGS)),
    currentUser: JSON.parse(JSON.stringify(CURRENT_USER)),
    recentOpens: JSON.parse(JSON.stringify(RECENT_OPENS)),
    bookingPages: JSON.parse(JSON.stringify(BOOKING_PAGES)),
    _nextEmailId: Math.max(...EMAILS.map(e => e.id)) + 1,
    _nextLabelId: 30,
    _nextSnippetId: 30,
    _nextEventId: 30,
    _nextAutoLabelId: 20,
    _nextSplitId: 20,
    _nextBookingPageId: 10,
};
process.stdout.write(JSON.stringify(state));
"""


# ── helpers ──────────────────────────────────────────────────────────

def find_entity(entities, **kwargs):
    """Find an entity by attribute match. Raises if not found."""
    for e in entities:
        if all(e.get(k) == v for k, v in kwargs.items()):
            return e
    raise ValueError(f"Entity not found: {kwargs}")


def find_email_by_subject(state, subject):
    """Find an email by subject."""
    for e in state["emails"]:
        if e["subject"] == subject:
            return e
    raise ValueError(f"Email not found: subject={subject!r}")


def find_email_by_subject_and_sender(state, subject, sender_email):
    """Find an email by subject and sender email."""
    for e in state["emails"]:
        if e["subject"] == subject and e["from"]["email"] == sender_email:
            return e
    raise ValueError(f"Email not found: subject={subject!r}, from={sender_email!r}")


def find_label_by_name(state, name):
    """Find a label by name."""
    for l in state["labels"]:
        if l["name"] == name:
            return l
    raise ValueError(f"Label not found: {name!r}")


def find_snippet_by_name(state, name):
    """Find a snippet by name."""
    for s in state["snippets"]:
        if s["name"] == name:
            return s
    raise ValueError(f"Snippet not found: {name!r}")


def find_auto_label_by_name(state, name):
    """Find an auto label by name."""
    for al in state["autoLabels"]:
        if al["name"] == name:
            return al
    raise ValueError(f"Auto label not found: {name!r}")


def find_split_by_name(state, name):
    """Find a split by name."""
    for s in state["splits"]:
        if s["name"] == name:
            return s
    raise ValueError(f"Split not found: {name!r}")


def find_booking_page_by_title(state, title):
    """Find a booking page by title."""
    for bp in state["bookingPages"]:
        if bp["title"] == title:
            return bp
    raise ValueError(f"Booking page not found: {title!r}")


# ── solve functions ──────────────────────────────────────────────────

def solve_task_1(state):
    """Mark email 'Q2 Product Roadmap - Final Review' as read."""
    email = find_email_by_subject(state, "Q2 Product Roadmap - Final Review")
    email["isRead"] = True


def solve_task_2(state):
    """Mark email 'Re: Infrastructure Migration Plan' as unread."""
    email = find_email_by_subject_and_sender(
        state, "Re: Infrastructure Migration Plan", "tom.bradley@acmecorp.com"
    )
    email["isRead"] = False


def solve_task_3(state):
    """Star email 'Partnership Opportunity - FinancePlus x Acme'."""
    email = find_email_by_subject(state, "Partnership Opportunity - FinancePlus x Acme")
    email["isStarred"] = True


def solve_task_4(state):
    """Unstar email 'FY2026 Budget Summary'."""
    email = find_email_by_subject_and_sender(
        state, "FY2026 Budget Summary", "priya.sharma@acmecorp.com"
    )
    email["isStarred"] = False


def solve_task_5(state):
    """Mark email 'Budget Approval Needed - Marketing Campaign' as done."""
    email = find_email_by_subject(state, "Budget Approval Needed - Marketing Campaign")
    email["isDone"] = True
    email["isRead"] = True
    email["remindAt"] = None


def solve_task_6(state):
    """Move email 'Re: Series B Term Sheet Discussion' to Trash."""
    email = find_email_by_subject_and_sender(
        state, "Re: Series B Term Sheet Discussion", "emily.r@venturelabs.co"
    )
    email["isTrashed"] = True
    email["isDone"] = False
    email["remindAt"] = None


def solve_task_7(state):
    """Mark email 'Global Health Initiative - Sponsorship Request' as spam."""
    email = find_email_by_subject(state, "Global Health Initiative - Sponsorship Request")
    email["isSpam"] = True
    email["isDone"] = False
    email["remindAt"] = None


def solve_task_8(state):
    """Set a reminder on 'Quantum Computing Integration Prototype' for March 8."""
    email = find_email_by_subject(state, "Quantum Computing Integration Prototype")
    email["remindAt"] = "2026-03-08T09:00:00.000Z"
    email["isRead"] = True


def solve_task_9(state):
    """Clear the reminder on 'Patent Filing Deadline - April 15'."""
    email = find_email_by_subject_and_sender(
        state, "Patent Filing Deadline - April 15", "james.obrien@legalwise.com"
    )
    email["remindAt"] = None


def solve_task_10(state):
    """Apply the 'Urgent' label to 'Database Performance Report - March'."""
    email = find_email_by_subject_and_sender(
        state, "Database Performance Report - March", "tom.bradley@acmecorp.com"
    )
    urgent_label = find_label_by_name(state, "Urgent")
    if urgent_label["id"] not in email["labels"]:
        email["labels"].append(urgent_label["id"])


def solve_task_11(state):
    """Remove 'Engineering' label from 'Re: Sprint 23 Retrospective Notes'."""
    email = find_email_by_subject_and_sender(
        state, "Re: Sprint 23 Retrospective Notes", "nate.patel@acmecorp.com"
    )
    eng_label = find_label_by_name(state, "Engineering")
    email["labels"] = [l for l in email["labels"] if l != eng_label["id"]]


def solve_task_12(state):
    """Create a new label named 'Design' with blue color."""
    next_id = state.get("_nextLabelId", 30)
    new_label = {
        "id": f"label_{next_id}",
        "name": "Design",
        "type": "user",
        "color": "#2196F3",
    }
    state["labels"].append(new_label)
    state["_nextLabelId"] = next_id + 1


def solve_task_13(state):
    """Delete the 'Receipts' label and remove from all emails."""
    receipts_label = find_label_by_name(state, "Receipts")
    label_id = receipts_label["id"]
    for email in state["emails"]:
        email["labels"] = [l for l in email["labels"] if l != label_id]
    state["labels"] = [l for l in state["labels"] if l["id"] != label_id]


def solve_task_14(state):
    """Send email to sarah.chen@acmecorp.com with subject 'Team Sync'."""
    next_id = state.get("_nextEmailId", 200)
    new_email = {
        "id": next_id,
        "threadId": f"thread_{next_id + 1}",
        "from": {
            "name": state["currentUser"]["name"],
            "email": state["currentUser"]["email"],
        },
        "to": [{"name": "Sarah Chen", "email": "sarah.chen@acmecorp.com"}],
        "cc": [],
        "bcc": [],
        "subject": "Team Sync",
        "snippet": "Let's schedule a sync this week.",
        "body": "Let's schedule a sync this week.",
        "date": "2026-03-07T12:00:00.000Z",
        "isRead": True,
        "isStarred": False,
        "isDone": False,
        "isTrashed": False,
        "isSpam": False,
        "isDraft": False,
        "labels": [],
        "hasAttachments": False,
        "attachments": [],
        "splitCategory": "important",
        "remindAt": None,
        "readReceipt": {"opened": False},
        "autoLabel": None,
        "replyDraftingTeammate": None,
        "threadMessages": None,
    }
    state["emails"].insert(0, new_email)
    state["_nextEmailId"] = next_id + 1


def solve_task_15(state):
    """Reply to 'Partnership Opportunity - FinancePlus x Acme' from David Kim."""
    next_id = state.get("_nextEmailId", 200)
    new_email = {
        "id": next_id,
        "threadId": f"thread_{next_id + 1}",
        "from": {
            "name": state["currentUser"]["name"],
            "email": state["currentUser"]["email"],
        },
        "to": [{"name": "David Kim", "email": "david.kim@financeplus.com"}],
        "cc": [],
        "bcc": [],
        "subject": "Re: Partnership Opportunity - FinancePlus x Acme",
        "snippet": "Let's set up a call next week.",
        "body": "Let's set up a call next week.\n\nBest,\nAlex Morgan\nVP of Product, Acme Corp",
        "date": "2026-03-07T12:00:00.000Z",
        "isRead": True,
        "isStarred": False,
        "isDone": False,
        "isTrashed": False,
        "isSpam": False,
        "isDraft": False,
        "labels": [],
        "hasAttachments": False,
        "attachments": [],
        "splitCategory": "important",
        "remindAt": None,
        "readReceipt": {"opened": False},
        "autoLabel": None,
        "replyDraftingTeammate": None,
        "threadMessages": None,
    }
    state["emails"].insert(0, new_email)
    state["_nextEmailId"] = next_id + 1


def solve_task_16(state):
    """Forward 'Quantum Computing Integration Prototype' to nate.patel@acmecorp.com."""
    next_id = state.get("_nextEmailId", 200)
    original = find_email_by_subject(state, "Quantum Computing Integration Prototype")
    new_email = {
        "id": next_id,
        "threadId": f"thread_{next_id + 1}",
        "from": {
            "name": state["currentUser"]["name"],
            "email": state["currentUser"]["email"],
        },
        "to": [{"name": "Nate Patel", "email": "nate.patel@acmecorp.com"}],
        "cc": [],
        "bcc": [],
        "subject": "Fwd: Quantum Computing Integration Prototype",
        "snippet": original["snippet"][:100],
        "body": f"\n\n---------- Forwarded message ----------\nFrom: {original['from']['name']} <{original['from']['email']}>\nSubject: {original['subject']}\n\n{original.get('body', original['snippet'])}",
        "date": "2026-03-07T12:00:00.000Z",
        "isRead": True,
        "isStarred": False,
        "isDone": False,
        "isTrashed": False,
        "isSpam": False,
        "isDraft": False,
        "labels": [],
        "hasAttachments": False,
        "attachments": [],
        "splitCategory": "important",
        "remindAt": None,
        "readReceipt": {"opened": False},
        "autoLabel": None,
        "replyDraftingTeammate": None,
        "threadMessages": None,
    }
    state["emails"].insert(0, new_email)
    state["_nextEmailId"] = next_id + 1


def solve_task_17(state):
    """Unsubscribe from the sender of 'Today's Briefing: AI Startup Funding...'"""
    email = find_email_by_subject_and_sender(
        state,
        "Today's Briefing: AI Startup Funding Hits Record $12B in Q1",
        "newsletter@theinformation.com",
    )
    email["isDone"] = True
    email["isRead"] = True
    if "blockedSenders" not in state["settings"]:
        state["settings"]["blockedSenders"] = []
    if "newsletter@theinformation.com" not in state["settings"]["blockedSenders"]:
        state["settings"]["blockedSenders"].append("newsletter@theinformation.com")


def solve_task_18(state):
    """Restore trashed email 'Complete Your Survey - Win a $500 Gift Card' to inbox."""
    email = find_email_by_subject(state, "Complete Your Survey - Win a $500 Gift Card")
    email["isTrashed"] = False


def solve_task_19(state):
    """Create snippet 'Project Update', shared, with variables."""
    next_id = state.get("_nextSnippetId", 30)
    new_snippet = {
        "id": f"snip_{next_id}",
        "name": "Project Update",
        "body": "Hi {first_name}, here is the latest update on {project_name}. Let me know if you have questions.",
        "variables": ["first_name", "project_name"],
        "isShared": True,
        "author": state["currentUser"]["name"],
        "authorId": state["currentUser"]["id"],
        "createdAt": "2026-03-07T12:00:00.000Z",
        "metrics": {"sends": 0, "openRate": 0, "responseRate": 0},
    }
    state["snippets"].append(new_snippet)
    state["_nextSnippetId"] = next_id + 1


def solve_task_20(state):
    """Edit snippet 'Meeting Follow-up' → rename to 'Post-Meeting Summary'."""
    snippet = find_snippet_by_name(state, "Meeting Follow-up")
    snippet["name"] = "Post-Meeting Summary"


def solve_task_21(state):
    """Delete snippet 'Decline Politely'."""
    state["snippets"] = [s for s in state["snippets"] if s["name"] != "Decline Politely"]


def solve_task_22(state):
    """Toggle sharing of snippet 'Out of Office' to shared."""
    snippet = find_snippet_by_name(state, "Out of Office")
    snippet["isShared"] = True


def solve_task_23(state):
    """Create calendar event 'Design Workshop' on March 10."""
    next_id = state.get("_nextEventId", 30)
    new_event = {
        "id": f"evt_{next_id}",
        "title": "Design Workshop",
        "date": "2026-03-10",
        "startTime": "10:00",
        "endTime": "12:00",
        "location": "Zoom",
        "description": "",
        "attendees": [],
        "meetingLink": None,
        "isAllDay": False,
        "calendarId": "work",
        "organizer": state["currentUser"]["email"],
        "status": "confirmed",
        "color": "#6C4FF7",
    }
    state["calendarEvents"].append(new_event)
    state["_nextEventId"] = next_id + 1


def solve_task_24(state):
    """Create booking page 'Strategy Session', 60 min, Google Meet."""
    next_id = state.get("_nextBookingPageId", 10)
    new_bp = {
        "id": f"bp_{next_id}",
        "title": "Strategy Session",
        "duration": 60,
        "location": "Google Meet",
        "description": "",
        "availability": {
            "days": ["Mon", "Tue", "Wed", "Thu", "Fri"],
            "startTime": "09:00",
            "endTime": "17:00",
        },
        "link": "https://cal.superhuman.com/alex.morgan/strategy-session",
        "isActive": True,
    }
    state["bookingPages"].append(new_bp)
    state["_nextBookingPageId"] = next_id + 1


def solve_task_25(state):
    """Toggle booking page 'Quick Sync' to active."""
    bp = find_booking_page_by_title(state, "Quick Sync")
    bp["isActive"] = True


def solve_task_26(state):
    """Delete booking page 'Product Demo'."""
    state["bookingPages"] = [
        bp for bp in state["bookingPages"] if bp["title"] != "Product Demo"
    ]


def solve_task_27(state):
    """Change theme to dark."""
    state["settings"]["theme"] = "dark"


def solve_task_28(state):
    """Disable desktop notifications."""
    state["settings"]["notifications"]["desktop"] = False


def solve_task_29(state):
    """Disable sound notifications."""
    state["settings"]["notifications"]["sound"] = False


def solve_task_30(state):
    """Turn off Instant Reply."""
    state["settings"]["instantReply"]["enabled"] = False


def solve_task_31(state):
    """Disable Smart Send."""
    state["settings"]["smartSend"]["enabled"] = False


def solve_task_32(state):
    """Turn off Read Receipts."""
    state["settings"]["readReceipts"]["enabled"] = False


def solve_task_33(state):
    """Disable Team Read Statuses."""
    state["settings"]["readReceipts"]["teamSharing"] = False


def solve_task_34(state):
    """Turn off Auto Reminders."""
    state["settings"]["autoReminders"]["enabled"] = False


def solve_task_35(state):
    """Change Auto Reminder mode to 'external'."""
    state["settings"]["autoReminders"]["mode"] = "external"


def solve_task_36(state):
    """Disable Auto Drafts."""
    state["settings"]["autoDrafts"]["enabled"] = False


def solve_task_37(state):
    """Change Auto Draft type to 'scheduling'."""
    state["settings"]["autoDrafts"]["type"] = "scheduling"


def solve_task_38(state):
    """Change swipe left to 'trash'."""
    state["settings"]["swipeLeft"] = "trash"


def solve_task_39(state):
    """Change swipe right to 'star'."""
    state["settings"]["swipeRight"] = "star"


def solve_task_40(state):
    """Change meeting link provider to 'google-meet'."""
    state["settings"]["meetingLink"]["provider"] = "google-meet"


def solve_task_41(state):
    """Disable auto-add meeting link."""
    state["settings"]["meetingLink"]["autoAdd"] = False


def solve_task_42(state):
    """Disable keyboard shortcuts."""
    state["settings"]["keyboard"]["shortcuts"] = False


def solve_task_43(state):
    """Disable Auto Archive."""
    state["settings"]["autoArchive"]["enabled"] = False


def solve_task_44(state):
    """Disable calendar alerts."""
    state["settings"]["notifications"]["calendarAlerts"] = False


def solve_task_45(state):
    """Change calendar alert timing to 30 minutes."""
    state["settings"]["notifications"]["alertMinutes"] = 30


def solve_task_46(state):
    """Turn off Ask AI."""
    state["settings"]["askAi"]["enabled"] = False


def solve_task_47(state):
    """Change email signature."""
    state["settings"]["signature"] = "Regards,\nAlex Morgan\nVP of Product"


def solve_task_48(state):
    """Create custom Auto Label 'Design Review' with from '@designhub.io'."""
    next_id = state.get("_nextAutoLabelId", 20)
    new_al = {
        "id": f"al_{next_id}",
        "name": "Design Review",
        "type": "custom",
        "enabled": True,
        "criteria": {"from": "@designhub.io"},
    }
    state["autoLabels"].append(new_al)
    state["_nextAutoLabelId"] = next_id + 1


def solve_task_49(state):
    """Disable Auto Label 'Team Update'."""
    al = find_auto_label_by_name(state, "Team Update")
    al["enabled"] = False


def solve_task_50(state):
    """Delete Auto Label 'Support Ticket'."""
    state["autoLabels"] = [
        al for al in state["autoLabels"] if al["name"] != "Support Ticket"
    ]


def solve_task_51(state):
    """Create split 'Investor Updates' based on Auto Label 'Investor'."""
    next_id = state.get("_nextSplitId", 20)
    new_split = {
        "id": f"split_{next_id}",
        "name": "Investor Updates",
        "position": len(state["splits"]),
        "isDefault": False,
        "criteria": {"autoLabel": "Investor"},
    }
    state["splits"].append(new_split)
    state["_nextSplitId"] = next_id + 1


def solve_task_52(state):
    """Delete the 'Feeds' custom split."""
    state["splits"] = [s for s in state["splits"] if s["name"] != "Feeds"]


def solve_task_53(state):
    """Send email to marcus.w@designhub.io with CC sarah.chen@acmecorp.com."""
    next_id = state.get("_nextEmailId", 200)
    new_email = {
        "id": next_id,
        "threadId": f"thread_{next_id + 1}",
        "from": {
            "name": state["currentUser"]["name"],
            "email": state["currentUser"]["email"],
        },
        "to": [{"name": "Marcus Williams", "email": "marcus.w@designhub.io"}],
        "cc": [{"name": "Sarah Chen", "email": "sarah.chen@acmecorp.com"}],
        "bcc": [],
        "subject": "Design Review Feedback",
        "snippet": "Great work on the new designs.",
        "body": "Great work on the new designs.",
        "date": "2026-03-07T12:00:00.000Z",
        "isRead": True,
        "isStarred": False,
        "isDone": False,
        "isTrashed": False,
        "isSpam": False,
        "isDraft": False,
        "labels": [],
        "hasAttachments": False,
        "attachments": [],
        "splitCategory": "important",
        "remindAt": None,
        "readReceipt": {"opened": False},
        "autoLabel": None,
        "replyDraftingTeammate": None,
        "threadMessages": None,
    }
    state["emails"].insert(0, new_email)
    state["_nextEmailId"] = next_id + 1


def solve_task_54(state):
    """Apply both 'Work' and 'Urgent' labels to 'Accessibility Audit Results'."""
    email = find_email_by_subject_and_sender(
        state, "Accessibility Audit Results", "maya.patel@acmecorp.com"
    )
    work_label = find_label_by_name(state, "Work")
    urgent_label = find_label_by_name(state, "Urgent")
    for lid in [work_label["id"], urgent_label["id"]]:
        if lid not in email["labels"]:
            email["labels"].append(lid)


def solve_task_55(state):
    """Clear reminder on 'Re: Payment Terms Discussion' from David Kim."""
    email = find_email_by_subject_and_sender(
        state, "Re: Payment Terms Discussion", "david.kim@financeplus.com"
    )
    email["remindAt"] = None


def solve_task_56(state):
    """Enable Auto Label 'Shipping Update'."""
    al = find_auto_label_by_name(state, "Shipping Update")
    al["enabled"] = True


def solve_task_57(state):
    """Create calendar event 'Lunch Meeting' on March 9."""
    next_id = state.get("_nextEventId", 30)
    new_event = {
        "id": f"evt_{next_id}",
        "title": "Lunch Meeting",
        "date": "2026-03-09",
        "startTime": "12:00",
        "endTime": "13:00",
        "location": "Blue Bottle Coffee",
        "description": "",
        "attendees": ["marcus.w@designhub.io"],
        "meetingLink": None,
        "isAllDay": False,
        "calendarId": "work",
        "organizer": state["currentUser"]["email"],
        "status": "confirmed",
        "color": "#6C4FF7",
    }
    state["calendarEvents"].append(new_event)
    state["_nextEventId"] = next_id + 1


def solve_task_58(state):
    """Change primary timezone to Pacific Time."""
    state["settings"]["timezone"] = "America/Los_Angeles"


def solve_task_59(state):
    """Change secondary timezone to None."""
    state["settings"]["secondaryTimezone"] = ""


def solve_task_60(state):
    """Toggle booking page 'Chat with Alex' to inactive."""
    bp = find_booking_page_by_title(state, "Chat with Alex")
    bp["isActive"] = False


# ── solver registry ──────────────────────────────────────────────────

SOLVERS = {
    f"task_{i}": globals()[f"solve_task_{i}"]
    for i in range(1, 61)
}


# ── infrastructure ──────────────────────────────────────────────────

def generate_seed_state():
    """Evaluate data.js through Node.js to get the seed state as Python dict."""
    data_js_path = APP_DIR / "js" / "data.js"
    result = subprocess.run(
        ["node", "-e", _SEED_STATE_JS, str(data_js_path)],
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
    """Start the Superhuman server on the given port."""
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
    parser = argparse.ArgumentParser(description="Superhuman function-task sanity check")
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
