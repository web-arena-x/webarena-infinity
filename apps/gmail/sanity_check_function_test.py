#!/usr/bin/env python3
"""
Verifier sanity check for function tests -- for each task, directly apply the
expected state changes via the API, run the verifier, and assert it passes.

Usage:
    python3 sanity_check_function_test.py                  # Run all 50 tasks sequentially
    python3 sanity_check_function_test.py --workers 4       # Run with 4 parallel server workers
    python3 sanity_check_function_test.py --task-id task_e1 # Run a single task
    python3 sanity_check_function_test.py --port 9000       # Custom base port
"""

import argparse
import copy
import importlib.util
import json
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone

import requests

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TASKS_DIR = os.path.join(SCRIPT_DIR, "tasks-function-test")

# -- Helper: find email by id ------------------------------------------------

def find_email(state, email_id):
    return next(e for e in state["emails"] if e["id"] == email_id)

# -- Seed state construction via Node ----------------------------------------

def get_seed_state():
    """Evaluate js/data.js through Node and return the seed state dict."""
    data_js_path = os.path.join(SCRIPT_DIR, "js", "data.js")
    with open(data_js_path) as f:
        js_code = f.read()

    js_code += """
console.log(JSON.stringify({
    _seedVersion: SEED_DATA_VERSION,
    emails: EMAILS,
    labels: LABELS,
    filters: FILTERS,
    settings: SETTINGS,
    contacts: CONTACTS,
    blockedSenders: BLOCKED_SENDERS,
    currentUser: CURRENT_USER,
    _nextEmailId: Math.max(...EMAILS.map(e => e.id)) + 1,
    _nextLabelId: 30,
    _nextFilterId: 20
}));
"""
    result = subprocess.run(
        ["node", "-"],
        input=js_code,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"Failed to evaluate seed data: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    return json.loads(result.stdout.strip())

# -- Per-task solve functions ------------------------------------------------
# Each function mutates the state dict to match what the verifier expects.

def solve_task_e1(state):
    """Mark email 'Monthly Financial Report - January 2026' (id=5) as unread."""
    email = find_email(state, 5)
    email["isRead"] = False

def solve_task_e2(state):
    """Move 'You have inherited $5,000,000' (id=89) from Trash to Inbox."""
    email = find_email(state, 89)
    email["isTrashed"] = False
    if "INBOX" not in email["labels"]:
        email["labels"].append("INBOX")

def solve_task_e3(state):
    """Block email address 'carlos.m@logisticspro.net'."""
    state["blockedSenders"].append({
        "email": "carlos.m@logisticspro.net",
        "blockedAt": datetime.now(timezone.utc).isoformat(),
    })

def solve_task_e4(state):
    """Remove importance from 'Contract Review: Vendor Agreement' (id=11)."""
    email = find_email(state, 11)
    email["isImportant"] = False
    if "IMPORTANT" in email["labels"]:
        email["labels"].remove("IMPORTANT")

def solve_task_e5(state):
    """Permanently delete spam email 'Claim your $500 Amazon Gift Card' (id=97)."""
    state["emails"] = [e for e in state["emails"] if e["id"] != 97]

def solve_task_e6(state):
    """Mute 'Quarterly Team Dinner' (id=18)."""
    email = find_email(state, 18)
    email["isMuted"] = True

def solve_task_e7(state):
    """Move archived 'Meeting notes: Sprint planning' (id=85) back to Inbox."""
    email = find_email(state, 85)
    email["isArchived"] = False
    if "INBOX" not in email["labels"]:
        email["labels"].append("INBOX")

def solve_task_e8(state):
    """Disable hover actions."""
    state["settings"]["hoverActions"] = False

def solve_task_e9(state):
    """Turn off dynamic email."""
    state["settings"]["dynamicEmail"] = False

def solve_task_e10(state):
    """Change auto-advance to 'list'."""
    state["settings"]["autoAdvance"] = "list"

def solve_task_e11(state):
    """Change button labels to 'text'."""
    state["settings"]["buttonLabels"] = "text"

def solve_task_e12(state):
    """Disable Send & Archive."""
    state["settings"]["sendAndArchive"] = False

def solve_task_e13(state):
    """Mark LinkedIn 'Sarah Chen endorsed you for Cloud Architecture' (id=31) as read."""
    email = find_email(state, 31)
    email["isRead"] = True

def solve_task_e14(state):
    """Turn off follow-up nudges."""
    state["settings"]["nudges"]["suggestEmailsToFollowUp"] = False

def solve_task_e15(state):
    """Permanently delete trashed 'Congratulations! You won $10,000!' (id=90)."""
    state["emails"] = [e for e in state["emails"] if e["id"] != 90]

def solve_task_m1(state):
    """Change Work label color to green."""
    for label in state["labels"]:
        if label["id"] == "label_1":
            label["color"] = {"background": "#2a8547", "text": "#fff"}
            break

def solve_task_m2(state):
    """Create filter: subject contains 'invoice', auto-archive."""
    next_filter_id = state.get("_nextFilterId", 20)
    state["filters"].append({
        "id": f"filter_{next_filter_id}",
        "criteria": {
            "from": "",
            "to": "",
            "subject": "invoice",
            "hasWords": "",
            "doesntHave": "",
            "hasAttachment": False,
            "size": None,
            "sizeUnit": "MB",
            "sizeComparison": "greater",
        },
        "actions": {
            "label": None,
            "archive": True,
            "markRead": False,
            "star": False,
            "forward": None,
            "delete": False,
            "neverSpam": False,
            "alwaysImportant": False,
            "neverImportant": False,
            "category": None,
        },
        "enabled": True,
        "createdAt": datetime.now(timezone.utc).isoformat(),
    })
    state["_nextFilterId"] = next_filter_id + 1

def solve_task_m3(state):
    """Disable Forums and Updates category tabs."""
    state["settings"]["categoriesEnabled"]["forums"] = False
    state["settings"]["categoriesEnabled"]["updates"] = False

def solve_task_m4(state):
    """Apply 'Meetings' (label_10) to 'Strategy Workshop Follow-up' (id=23)."""
    email = find_email(state, 23)
    if "label_10" not in email["labels"]:
        email["labels"].append("label_10")

def solve_task_m5(state):
    """Hide the 'Reference' label (label_19)."""
    for label in state["labels"]:
        if label["id"] == "label_19":
            label["visible"] = False
            break

def solve_task_m6(state):
    """Set Multiple Inboxes position to 'above'."""
    state["settings"]["multipleInboxPosition"] = "above"

def solve_task_m7(state):
    """Snooze 'Re: Collaboration Proposal' (id=20) until tomorrow."""
    email = find_email(state, 20)
    email["isSnoozed"] = True
    tomorrow = datetime.now(timezone.utc) + timedelta(days=1)
    email["snoozeUntil"] = tomorrow.replace(hour=8, minute=0, second=0, microsecond=0).isoformat()
    if "INBOX" in email["labels"]:
        email["labels"].remove("INBOX")

def solve_task_m8(state):
    """Create filter: from figma, categorize as promotions."""
    next_filter_id = state.get("_nextFilterId", 20)
    state["filters"].append({
        "id": f"filter_{next_filter_id}",
        "criteria": {
            "from": "newsletter@figma.com",
            "to": "",
            "subject": "",
            "hasWords": "",
            "doesntHave": "",
            "hasAttachment": False,
            "size": None,
            "sizeUnit": "MB",
            "sizeComparison": "greater",
        },
        "actions": {
            "label": None,
            "archive": False,
            "markRead": False,
            "star": False,
            "forward": None,
            "delete": False,
            "neverSpam": False,
            "alwaysImportant": False,
            "neverImportant": False,
            "category": "promotions",
        },
        "enabled": True,
        "createdAt": datetime.now(timezone.utc).isoformat(),
    })
    state["_nextFilterId"] = next_filter_id + 1

def solve_task_m9(state):
    """Star 'Your tweet got 250 likes' (id=32) and mark important."""
    email = find_email(state, 32)
    email["isStarred"] = True
    email["starType"] = "yellow-star"
    email["isImportant"] = True
    if "IMPORTANT" not in email["labels"]:
        email["labels"].append("IMPORTANT")

def solve_task_m10(state):
    """Move 'Sarah Chen endorsed you for Cloud Architecture' (id=31) from Social to Primary."""
    email = find_email(state, 31)
    email["category"] = "primary"
    if "CATEGORY_SOCIAL" in email["labels"]:
        email["labels"].remove("CATEGORY_SOCIAL")
    if "CATEGORY_PRIMARY" not in email["labels"]:
        email["labels"].append("CATEGORY_PRIMARY")

def solve_task_m11(state):
    """Discard draft 'Re: Conference Talk Proposal' (id=98)."""
    state["emails"] = [e for e in state["emails"] if e["id"] != 98]

def solve_task_m12(state):
    """Apply 'Education' (label_8) and 'Reference' (label_19) to 'Lab Tour Invitation' (id=107)."""
    email = find_email(state, 107)
    if "label_8" not in email["labels"]:
        email["labels"].append("label_8")
    if "label_19" not in email["labels"]:
        email["labels"].append("label_19")

def solve_task_m13(state):
    """Delete all spam emails permanently."""
    state["emails"] = [e for e in state["emails"] if not e.get("isSpam", False)]

def solve_task_m14(state):
    """Compose draft to priya.sharma@cloudnine.dev with subject 'Code Review Feedback'."""
    next_id = state.get("_nextEmailId", 131)
    state["emails"].append({
        "id": next_id,
        "threadId": "thread_" + str(next_id),
        "from": {
            "name": "Alex Johnson",
            "email": "alex.johnson@gmail.com",
        },
        "to": [{"name": "Priya Sharma", "email": "priya.sharma@cloudnine.dev"}],
        "cc": [],
        "bcc": [],
        "subject": "Code Review Feedback",
        "snippet": "",
        "body": "",
        "date": datetime.now(timezone.utc).isoformat(),
        "isRead": True,
        "isStarred": False,
        "starType": None,
        "isImportant": False,
        "labels": ["DRAFT"],
        "category": "primary",
        "hasAttachments": False,
        "attachments": [],
        "isSnoozed": False,
        "snoozeUntil": None,
        "isTrashed": False,
        "isSpam": False,
        "isArchived": False,
        "isDraft": True,
        "isSent": False,
        "isMuted": False,
    })
    state["_nextEmailId"] = next_id + 1

def solve_task_m15(state):
    """Change theme to 'soft' and density to 'comfortable'."""
    state["settings"]["theme"] = "soft"
    state["settings"]["density"] = "comfortable"

def solve_task_m16(state):
    """Update filter for morningbrew to also mark as read."""
    for f in state["filters"]:
        if f["id"] == "filter_2":
            f["actions"]["markRead"] = True
            break

def solve_task_m17(state):
    """Create label 'Taxes' under Finance (label_3)."""
    next_label_id = state.get("_nextLabelId", 30)
    state["labels"].append({
        "id": f"label_{next_label_id}",
        "name": "Taxes",
        "type": "user",
        "color": None,
        "visible": True,
        "parentId": "label_3",
        "messageCount": 0,
        "unreadCount": 0,
    })
    state["_nextLabelId"] = next_label_id + 1

def solve_task_m18(state):
    """Turn off reply nudges and set default reply to 'reply_all'."""
    state["settings"]["nudges"]["suggestEmailsToReply"] = False
    state["settings"]["defaultReplyBehavior"] = "reply_all"

def solve_task_m19(state):
    """Unsnooze 'Investor Deck Review' (id=82) back to Inbox."""
    email = find_email(state, 82)
    email["isSnoozed"] = False
    email["snoozeUntil"] = None
    if "INBOX" not in email["labels"]:
        email["labels"].append("INBOX")

def solve_task_m20(state):
    """Send email to robert.singh@university.edu with subject 'Guest Lecture Confirmation'."""
    next_id = state.get("_nextEmailId", 131)
    state["emails"].append({
        "id": next_id,
        "threadId": "thread_" + str(next_id),
        "from": {
            "name": "Alex Johnson",
            "email": "alex.johnson@gmail.com",
        },
        "to": [{"name": "Robert Singh", "email": "robert.singh@university.edu"}],
        "cc": [],
        "bcc": [],
        "subject": "Guest Lecture Confirmation",
        "snippet": "Hi Robert, I would be happy to give the guest lecture...",
        "body": "Hi Robert, I would be happy to give the guest lecture on March 20th. Please send me the details. Thanks, Alex",
        "date": datetime.now(timezone.utc).isoformat(),
        "isRead": True,
        "isStarred": False,
        "starType": None,
        "isImportant": False,
        "labels": ["SENT"],
        "category": "primary",
        "hasAttachments": False,
        "attachments": [],
        "isSnoozed": False,
        "snoozeUntil": None,
        "isTrashed": False,
        "isSpam": False,
        "isArchived": False,
        "isDraft": False,
        "isSent": True,
        "isMuted": False,
    })
    state["_nextEmailId"] = next_id + 1

def solve_task_h1(state):
    """Create filter: from coursera, subject certificate, apply Education, mark read, archive."""
    next_filter_id = state.get("_nextFilterId", 20)
    state["filters"].append({
        "id": f"filter_{next_filter_id}",
        "criteria": {
            "from": "no-reply@coursera.org",
            "to": "",
            "subject": "certificate",
            "hasWords": "",
            "doesntHave": "",
            "hasAttachment": False,
            "size": None,
            "sizeUnit": "MB",
            "sizeComparison": "greater",
        },
        "actions": {
            "label": "label_8",
            "archive": True,
            "markRead": True,
            "star": False,
            "forward": None,
            "delete": False,
            "neverSpam": False,
            "alwaysImportant": False,
            "neverImportant": False,
            "category": None,
        },
        "enabled": True,
        "createdAt": datetime.now(timezone.utc).isoformat(),
    })
    state["_nextFilterId"] = next_filter_id + 1

def solve_task_h2(state):
    """Send email to jennifer.wu CC kevin.zhao, subject 'Collaboration Meeting'."""
    next_id = state.get("_nextEmailId", 131)
    state["emails"].append({
        "id": next_id,
        "threadId": "thread_" + str(next_id),
        "from": {
            "name": "Alex Johnson",
            "email": "alex.johnson@gmail.com",
        },
        "to": [{"name": "Jennifer Wu", "email": "jennifer.wu@biomedresearch.com"}],
        "cc": [{"name": "Kevin Zhao", "email": "kevin.zhao@quantumlab.tech"}],
        "bcc": [],
        "subject": "Collaboration Meeting",
        "snippet": "Hi Jennifer and Kevin, I would like to schedule a meeting...",
        "body": "Hi Jennifer and Kevin, I would like to schedule a meeting to discuss the research collaboration. How does next Tuesday at 3pm work? Best, Alex",
        "date": datetime.now(timezone.utc).isoformat(),
        "isRead": True,
        "isStarred": False,
        "starType": None,
        "isImportant": False,
        "labels": ["SENT"],
        "category": "primary",
        "hasAttachments": False,
        "attachments": [],
        "isSnoozed": False,
        "snoozeUntil": None,
        "isTrashed": False,
        "isSpam": False,
        "isArchived": False,
        "isDraft": False,
        "isSent": True,
        "isMuted": False,
    })
    state["_nextEmailId"] = next_id + 1

def solve_task_h3(state):
    """Empty Trash: remove all trashed emails."""
    state["emails"] = [e for e in state["emails"] if not e.get("isTrashed", False)]

def solve_task_h4(state):
    """Archive all unread Social emails."""
    for email in state["emails"]:
        if (email.get("category") == "social"
                and not email.get("isRead", True)
                and "INBOX" in email.get("labels", [])):
            email["labels"].remove("INBOX")
            email["isArchived"] = True

def solve_task_h5(state):
    """Create 'Cloud' label under Work with blue color, apply to email id=2."""
    next_label_id = state.get("_nextLabelId", 30)
    label_id = f"label_{next_label_id}"
    state["labels"].append({
        "id": label_id,
        "name": "Cloud",
        "type": "user",
        "color": {"background": "#2962ff", "text": "#fff"},
        "visible": True,
        "parentId": "label_1",
        "messageCount": 0,
        "unreadCount": 0,
    })
    email = find_email(state, 2)
    if label_id not in email["labels"]:
        email["labels"].append(label_id)
    state["_nextLabelId"] = next_label_id + 1

def solve_task_h6(state):
    """Forward 'Research Paper: Quantum Error Correction' to sarah.chen@techcorp.io."""
    next_id = state.get("_nextEmailId", 131)
    state["emails"].append({
        "id": next_id,
        "threadId": "thread_" + str(next_id),
        "from": {
            "name": "Alex Johnson",
            "email": "alex.johnson@gmail.com",
        },
        "to": [{"name": "Sarah Chen", "email": "sarah.chen@techcorp.io"}],
        "cc": [],
        "bcc": [],
        "subject": "Fwd: Research Paper: Quantum Error Correction",
        "snippet": "---------- Forwarded message ----------",
        "body": "---------- Forwarded message ----------\nFrom: Kevin Zhao\nSubject: Research Paper: Quantum Error Correction\n\nOur team just published a new paper on quantum error correction codes.",
        "date": datetime.now(timezone.utc).isoformat(),
        "isRead": True,
        "isStarred": False,
        "starType": None,
        "isImportant": False,
        "labels": ["SENT"],
        "category": "primary",
        "hasAttachments": False,
        "attachments": [],
        "isSnoozed": False,
        "snoozeUntil": None,
        "isTrashed": False,
        "isSpam": False,
        "isArchived": False,
        "isDraft": False,
        "isSent": True,
        "isMuted": False,
    })
    state["_nextEmailId"] = next_id + 1

def solve_task_h7(state):
    """Configure Multiple Inboxes second section and position."""
    state["settings"]["multipleInboxSections"][1]["query"] = "is:important"
    state["settings"]["multipleInboxSections"][1]["name"] = "Priority Items"
    state["settings"]["multipleInboxPosition"] = "above"

def solve_task_h8(state):
    """Create 'DevReports' label with orange color, apply to emails id=58 and id=68."""
    next_label_id = state.get("_nextLabelId", 30)
    label_id = f"label_{next_label_id}"
    state["labels"].append({
        "id": label_id,
        "name": "DevReports",
        "type": "user",
        "color": {"background": "#e37400", "text": "#fff"},
        "visible": True,
        "parentId": None,
        "messageCount": 0,
        "unreadCount": 0,
    })
    for eid in [58, 68]:
        email = find_email(state, eid)
        if label_id not in email["labels"]:
            email["labels"].append(label_id)
    state["_nextLabelId"] = next_label_id + 1

def solve_task_h9(state):
    """Disable keyboard shortcuts, importance markers, hover actions; set density to compact."""
    state["settings"]["keyboardShortcutsEnabled"] = False
    state["settings"]["importanceMarkers"] = False
    state["settings"]["hoverActions"] = False
    state["settings"]["density"] = "compact"

def solve_task_h10(state):
    """Star 'Re: Collaboration Proposal' (id=20), apply Clients (label_11), mark read."""
    email = find_email(state, 20)
    email["isStarred"] = True
    email["starType"] = "yellow-star"
    if "label_11" not in email["labels"]:
        email["labels"].append("label_11")
    email["isRead"] = True

def solve_task_h11(state):
    """Move Amazon email (id=44) from Promotions to Primary, apply Action Required (label_17)."""
    email = find_email(state, 44)
    email["category"] = "primary"
    if "CATEGORY_PROMOTIONS" in email["labels"]:
        email["labels"].remove("CATEGORY_PROMOTIONS")
    if "CATEGORY_PRIMARY" not in email["labels"]:
        email["labels"].append("CATEGORY_PRIMARY")
    if "label_17" not in email["labels"]:
        email["labels"].append("label_17")

def solve_task_h12(state):
    """Snooze 'CI/CD Pipeline Migration Plan' (id=9) until next week, remove Action Required."""
    email = find_email(state, 9)
    email["isSnoozed"] = True
    next_week = datetime.now(timezone.utc) + timedelta(days=7)
    email["snoozeUntil"] = next_week.replace(hour=8, minute=0, second=0, microsecond=0).isoformat()
    if "label_17" in email["labels"]:
        email["labels"].remove("label_17")
    if "INBOX" in email["labels"]:
        email["labels"].remove("INBOX")

def solve_task_h13(state):
    """Move spam 'Lose 30 pounds in 30 days!' (id=94) to Inbox, apply Health (label_7)."""
    email = find_email(state, 94)
    email["isSpam"] = False
    if "INBOX" not in email["labels"]:
        email["labels"].append("INBOX")
    if "label_7" not in email["labels"]:
        email["labels"].append("label_7")

def solve_task_h14(state):
    """Create 'Review Needed' label with purple color, apply to emails id=105, 26, 9."""
    next_label_id = state.get("_nextLabelId", 30)
    label_id = f"label_{next_label_id}"
    state["labels"].append({
        "id": label_id,
        "name": "Review Needed",
        "type": "user",
        "color": {"background": "#7e57c2", "text": "#fff"},
        "visible": True,
        "parentId": None,
        "messageCount": 0,
        "unreadCount": 0,
    })
    for eid in [105, 26, 9]:
        email = find_email(state, eid)
        if label_id not in email["labels"]:
            email["labels"].append(label_id)
    state["_nextLabelId"] = next_label_id + 1

def solve_task_h15(state):
    """Delete HR label (label_12), remove from emails, rename Clients (label_11) to Partners."""
    state["labels"] = [l for l in state["labels"] if l["id"] != "label_12"]
    for email in state["emails"]:
        if "label_12" in email.get("labels", []):
            email["labels"].remove("label_12")
    for label in state["labels"]:
        if label["id"] == "label_11":
            label["name"] = "Partners"
            break


SOLVERS = {
    "task_e1": solve_task_e1, "task_e2": solve_task_e2,
    "task_e3": solve_task_e3, "task_e4": solve_task_e4,
    "task_e5": solve_task_e5, "task_e6": solve_task_e6,
    "task_e7": solve_task_e7, "task_e8": solve_task_e8,
    "task_e9": solve_task_e9, "task_e10": solve_task_e10,
    "task_e11": solve_task_e11, "task_e12": solve_task_e12,
    "task_e13": solve_task_e13, "task_e14": solve_task_e14,
    "task_e15": solve_task_e15,
    "task_m1": solve_task_m1, "task_m2": solve_task_m2,
    "task_m3": solve_task_m3, "task_m4": solve_task_m4,
    "task_m5": solve_task_m5, "task_m6": solve_task_m6,
    "task_m7": solve_task_m7, "task_m8": solve_task_m8,
    "task_m9": solve_task_m9, "task_m10": solve_task_m10,
    "task_m11": solve_task_m11, "task_m12": solve_task_m12,
    "task_m13": solve_task_m13, "task_m14": solve_task_m14,
    "task_m15": solve_task_m15, "task_m16": solve_task_m16,
    "task_m17": solve_task_m17, "task_m18": solve_task_m18,
    "task_m19": solve_task_m19, "task_m20": solve_task_m20,
    "task_h1": solve_task_h1, "task_h2": solve_task_h2,
    "task_h3": solve_task_h3, "task_h4": solve_task_h4,
    "task_h5": solve_task_h5, "task_h6": solve_task_h6,
    "task_h7": solve_task_h7, "task_h8": solve_task_h8,
    "task_h9": solve_task_h9, "task_h10": solve_task_h10,
    "task_h11": solve_task_h11, "task_h12": solve_task_h12,
    "task_h13": solve_task_h13, "task_h14": solve_task_h14,
    "task_h15": solve_task_h15,
}

# -- Server lifecycle --------------------------------------------------------

def start_server(port):
    return subprocess.Popen(
        [sys.executable, "server.py", "--port", str(port)],
        cwd=SCRIPT_DIR,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

def wait_for_server(port, timeout=10):
    url = f"http://localhost:{port}/"
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            r = requests.get(url, timeout=2)
            if r.status_code == 200:
                return True
        except requests.ConnectionError:
            pass
        time.sleep(0.3)
    return False

def stop_server(proc):
    if proc.poll() is not None:
        return
    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait()

# -- Verifier loading --------------------------------------------------------

def load_verifier(task_id):
    path = os.path.join(TASKS_DIR, f"{task_id}.py")
    spec = importlib.util.spec_from_file_location(task_id, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.verify

# -- Worker: run a batch of tasks on one server ------------------------------

def run_tasks(task_ids, port, seed_state):
    """Start a server on *port*, run each task, return list of (task_id, passed, message)."""
    results = []
    proc = start_server(port)
    try:
        if not wait_for_server(port):
            for tid in task_ids:
                results.append((tid, False, "Server failed to start"))
            return results

        base = f"http://localhost:{port}"

        # First PUT sets _seed_state on the server
        r = requests.put(f"{base}/api/state", json=seed_state, timeout=5)
        if r.status_code != 200:
            for tid in task_ids:
                results.append((tid, False, "Failed to seed server state"))
            return results

        for tid in task_ids:
            try:
                # Reset to seed
                requests.post(f"{base}/api/reset", timeout=5)

                # Fetch clean seed state
                state = requests.get(f"{base}/api/state", timeout=5).json()

                # Apply expected changes
                SOLVERS[tid](state)

                # Push solved state
                requests.put(f"{base}/api/state", json=state, timeout=5)

                # Run the verifier
                verify = load_verifier(tid)
                passed, message = verify(base)
                results.append((tid, passed, message))
            except Exception as e:
                results.append((tid, False, f"Error: {e}"))
    finally:
        stop_server(proc)
    return results

# -- Main --------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Function test verifier sanity check")
    parser.add_argument("--workers", type=int, default=1,
                        help="Number of parallel server workers (default: 1)")
    parser.add_argument("--task-id", type=str,
                        help="Run a single task (e.g. task_e1)")
    parser.add_argument("--port", type=int, default=19000,
                        help="Base port for servers (default: 19000)")
    args = parser.parse_args()

    # Determine which tasks to run
    if args.task_id:
        task_ids = [args.task_id]
    else:
        with open(os.path.join(SCRIPT_DIR, "tasks-function-test.json")) as f:
            task_ids = [t["id"] for t in json.load(f)]

    for tid in task_ids:
        if tid not in SOLVERS:
            print(f"Unknown task: {tid}", file=sys.stderr)
            sys.exit(1)

    # Build seed state from js/data.js
    print("Loading seed state via Node...")
    seed_state = get_seed_state()
    print(f"Seed loaded: {len(seed_state['emails'])} emails, "
          f"{len(seed_state['labels'])} labels, "
          f"{len(seed_state['filters'])} filters")

    num_workers = min(args.workers, len(task_ids))
    all_results = []

    if num_workers <= 1:
        # Sequential -- single server
        all_results = run_tasks(task_ids, args.port, seed_state)
    else:
        # Parallel -- one server per worker, tasks round-robin partitioned
        chunks = [[] for _ in range(num_workers)]
        for i, tid in enumerate(task_ids):
            chunks[i % num_workers].append(tid)

        with ThreadPoolExecutor(max_workers=num_workers) as pool:
            futures = {
                pool.submit(run_tasks, chunk, args.port + i, seed_state): i
                for i, chunk in enumerate(chunks) if chunk
            }
            for f in as_completed(futures):
                all_results.extend(f.result())

    # Sort by original task order
    order = {tid: i for i, tid in enumerate(task_ids)}
    all_results.sort(key=lambda r: order.get(r[0], 999))

    # Print results
    print()
    passed_count = 0
    failed = []
    for tid, passed, message in all_results:
        status = "PASS" if passed else "FAIL"
        if passed:
            passed_count += 1
        else:
            failed.append(tid)
        print(f"  {status}  {tid:12s}  {message}")

    total = len(all_results)
    print(f"\n{passed_count}/{total} passed")
    if failed:
        print(f"Failed: {', '.join(failed)}")
        sys.exit(1)
    else:
        print("All verifiers passed!")

if __name__ == "__main__":
    main()
