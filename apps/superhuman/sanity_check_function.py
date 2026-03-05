#!/usr/bin/env python3
"""
Sanity check for Superhuman function-test tasks.

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

const state = {
    version: SEED_DATA_VERSION,
    currentUser: JSON.parse(JSON.stringify(CURRENT_USER)),
    contacts: JSON.parse(JSON.stringify(CONTACTS)),
    labels: JSON.parse(JSON.stringify(LABELS)),
    autoLabels: JSON.parse(JSON.stringify(AUTO_LABELS)),
    splits: JSON.parse(JSON.stringify(SPLITS)),
    folders: JSON.parse(JSON.stringify(FOLDERS)),
    snippets: JSON.parse(JSON.stringify(SNIPPETS)),
    calendarEvents: JSON.parse(JSON.stringify(CALENDAR_EVENTS)),
    emails: JSON.parse(JSON.stringify(EMAILS)),
    settings: JSON.parse(JSON.stringify(SETTINGS)),
    blockedSenders: JSON.parse(JSON.stringify(BLOCKED_SENDERS)),
    recentOpens: JSON.parse(JSON.stringify(RECENT_OPENS)),
    folderCounts: {},
    _nextEmailId: 200,
    _nextLabelId: 30,
    _nextSnippetId: 20,
    _nextEventId: 30
};
process.stdout.write(JSON.stringify(state));
"""


# ── helpers ──────────────────────────────────────────────────────────

def find_email_by_subject(state, subject_fragment):
    """Find an email by subject substring match. Raises if not found."""
    for e in state["emails"]:
        if subject_fragment in e["subject"]:
            return e
    raise ValueError(f"Email not found with subject containing: {subject_fragment!r}")


def find_email_by_id(state, email_id):
    """Find an email by ID. Raises if not found."""
    for e in state["emails"]:
        if e["id"] == email_id:
            return e
    raise ValueError(f"Email not found with id: {email_id!r}")


def find_label_by_name(state, name):
    """Find a label by name."""
    for l in state["labels"]:
        if l["name"] == name:
            return l
    raise ValueError(f"Label not found: {name!r}")


def find_auto_label_by_name(state, name):
    """Find an auto-label by name."""
    for al in state["autoLabels"]:
        if al["name"] == name:
            return al
    raise ValueError(f"Auto-label not found: {name!r}")


def find_snippet_by_name(state, name):
    """Find a snippet by name."""
    for s in state["snippets"]:
        if s["name"] == name:
            return s
    raise ValueError(f"Snippet not found: {name!r}")


def find_event_by_title(state, title_fragment):
    """Find a calendar event by title substring."""
    for e in state["calendarEvents"]:
        if title_fragment in e["title"]:
            return e
    raise ValueError(f"Event not found with title containing: {title_fragment!r}")


def next_email_id(state):
    """Get next email ID and increment counter."""
    eid = state.get("_nextEmailId", 200)
    state["_nextEmailId"] = eid + 1
    return f"email_{str(eid).zfill(3)}"


def next_label_id(state):
    """Get next label ID and increment counter."""
    lid = state.get("_nextLabelId", 30)
    state["_nextLabelId"] = lid + 1
    return f"label_{lid}"


def next_snippet_id(state):
    """Get next snippet ID and increment counter."""
    sid = state.get("_nextSnippetId", 20)
    state["_nextSnippetId"] = sid + 1
    return f"snippet_{str(sid).zfill(2)}"


def next_event_id(state):
    """Get next event ID and increment counter."""
    eid = state.get("_nextEventId", 30)
    state["_nextEventId"] = eid + 1
    return f"event_{str(eid).zfill(2)}"


# ── solve functions ──────────────────────────────────────────────────

def solve_task_1(state):
    """Mark email 'Project Alpha — Q1 Scope Finalization' as read."""
    email = find_email_by_subject(state, "Project Alpha")
    email["isRead"] = True


def solve_task_2(state):
    """Mark email 'Q1 OKR mid-quarter check-in — Engineering' as unread."""
    email = find_email_by_subject(state, "Q1 OKR mid-quarter check-in")
    email["isRead"] = False


def solve_task_3(state):
    """Star the email 'Partnership inquiry: QuantumLeap AI'."""
    email = find_email_by_subject(state, "Partnership inquiry: QuantumLeap AI")
    email["isStarred"] = True


def solve_task_4(state):
    """Unstar the email 'Urgent: Production outage'."""
    email = find_email_by_subject(state, "Urgent: Production outage")
    email["isStarred"] = False


def solve_task_5(state):
    """Archive email 'Fwd: TechCrunch' (mark done)."""
    email = find_email_by_subject(state, "TechCrunch")
    email["folder"] = "done"
    email["isRead"] = True
    email["reminder"] = None


def solve_task_6(state):
    """Trash email 'Vercel usage alert'."""
    email = find_email_by_subject(state, "Vercel usage alert")
    email["folder"] = "trash"
    email["reminder"] = None


def solve_task_7(state):
    """Move 'Unsubscribe confirmation — CRO Weekly' from trash to inbox."""
    email = find_email_by_subject(state, "Unsubscribe confirmation")
    email["folder"] = "inbox"


def solve_task_8(state):
    """Move 'Make $5000/week' from spam to inbox."""
    email = find_email_by_subject(state, "Make $5000/week")
    email["folder"] = "inbox"


def solve_task_9(state):
    """Move 'Reminder: TechCorp domain' to spam."""
    email = find_email_by_subject(state, "TechCorp domain techcorp.io renews")
    email["folder"] = "spam"
    email["reminder"] = None


def solve_task_10(state):
    """Permanently delete 'URGENT: Claim your $10,000 developer grant now!'."""
    state["emails"] = [
        e for e in state["emails"]
        if "Claim your $10,000 developer grant" not in e["subject"]
    ]


def solve_task_11(state):
    """Add 'Engineering' label to 'Re: Board deck'."""
    email = find_email_by_subject(state, "Re: Board deck")
    if "label_10" not in email["labels"]:
        email["labels"].append("label_10")


def solve_task_12(state):
    """Remove 'Urgent' label from 'Urgent: Production outage'."""
    email = find_email_by_subject(state, "Urgent: Production outage")
    email["labels"] = [l for l in email["labels"] if l != "label_7"]


def solve_task_13(state):
    """Add 'Project Alpha' and 'Q1 Planning' labels to 'Re: Re: v2 API beta feedback'."""
    email = find_email_by_subject(state, "v2 API beta feedback")
    if "label_1" not in email["labels"]:
        email["labels"].append("label_1")
    if "label_2" not in email["labels"]:
        email["labels"].append("label_2")


def solve_task_14(state):
    """Remove all labels from 'Customer complaint — data export'."""
    email = find_email_by_subject(state, "Customer complaint")
    email["labels"] = []


def solve_task_15(state):
    """Set reminder on 'SolarPeak integration' for March 10, 2026."""
    email = find_email_by_subject(state, "SolarPeak integration")
    email["reminder"] = {"date": "2026-03-10T09:00:00Z", "type": "manual"}


def solve_task_16(state):
    """Clear reminder from 'Re: Series B prep — data room checklist'."""
    email = find_email_by_subject(state, "Re: Series B prep")
    email["reminder"] = None


def solve_task_17(state):
    """Move 'LoopWorks — export issue resolved' from done to inbox."""
    email = find_email_by_subject(state, "LoopWorks")
    # Find the one in done folder
    for e in state["emails"]:
        if "LoopWorks" in e["subject"] and "export issue resolved" in e["subject"]:
            e["folder"] = "inbox"
            return
    raise ValueError("LoopWorks email not found")


def solve_task_18(state):
    """Move 'Old expense report Q3 2025' from trash to done."""
    email = find_email_by_subject(state, "Old expense report Q3 2025")
    email["folder"] = "done"


def solve_task_19(state):
    """Unsubscribe from sender of 'Engineering Manager spotlight': block + archive."""
    email = find_email_by_subject(state, "Engineering Manager spotlight")
    sender_email = email["from"]["email"]
    # Block the sender
    if not any(b["email"] == sender_email for b in state["blockedSenders"]):
        state["blockedSenders"].append({
            "email": sender_email,
            "blockedAt": "2026-03-02T12:00:00Z"
        })
    # Archive all emails from this sender in inbox
    for e in state["emails"]:
        if e["from"]["email"] == sender_email and e["folder"] == "inbox":
            e["folder"] = "done"


def solve_task_20(state):
    """Get Me To Zero — archive all inbox emails."""
    for email in state["emails"]:
        if email["folder"] == "inbox" and not email.get("isDraft") and not email.get("isScheduled"):
            email["folder"] = "done"
            email["isRead"] = True


def solve_task_21(state):
    """Get Me To Zero — preserving starred emails."""
    for email in state["emails"]:
        if email["folder"] == "inbox" and not email.get("isDraft") and not email.get("isScheduled"):
            if not email["isStarred"]:
                email["folder"] = "done"
                email["isRead"] = True


def solve_task_22(state):
    """Send new email to jamie.chen@techcorp.io with subject 'Team Sync Follow-up'."""
    eid = next_email_id(state)
    new_email = {
        "id": eid,
        "threadId": eid,
        "subject": "Team Sync Follow-up",
        "from": {"name": state["currentUser"]["name"], "email": state["currentUser"]["email"]},
        "to": [{"name": "Jamie Chen", "email": "jamie.chen@techcorp.io"}],
        "cc": [],
        "bcc": [],
        "body": "<p>Thanks for the update on the Q2 roadmap.</p>",
        "snippet": "Thanks for the update on the Q2 roadmap.",
        "date": "2026-03-02T12:00:00Z",
        "isRead": True,
        "isStarred": False,
        "folder": "sent",
        "split": "important",
        "labels": [],
        "autoLabels": [],
        "hasAttachments": False,
        "attachments": [],
        "readStatus": {"enabled": True, "opens": []},
        "reminder": None,
        "isDraft": False,
        "isScheduled": False,
        "scheduledTime": None,
        "threadMessages": []
    }
    state["emails"].append(new_email)


def solve_task_23(state):
    """Save draft to nbrooks@acmeventures.com with subject 'Series B Timeline'."""
    eid = next_email_id(state)
    new_draft = {
        "id": eid,
        "threadId": eid,
        "subject": "Series B Timeline",
        "from": {"name": state["currentUser"]["name"], "email": state["currentUser"]["email"]},
        "to": [{"name": "Nathan Brooks", "email": "nbrooks@acmeventures.com"}],
        "cc": [],
        "bcc": [],
        "body": "<p>Nathan, here is the updated timeline for Series B.</p>",
        "snippet": "Nathan, here is the updated timeline for Series B.",
        "date": "2026-03-02T12:00:00Z",
        "isRead": True,
        "isStarred": False,
        "folder": "drafts",
        "split": "important",
        "labels": [],
        "autoLabels": [],
        "hasAttachments": False,
        "attachments": [],
        "readStatus": {"enabled": False, "opens": []},
        "reminder": None,
        "isDraft": True,
        "isScheduled": False,
        "scheduledTime": None,
        "threadMessages": []
    }
    state["emails"].append(new_draft)


def solve_task_24(state):
    """Cancel scheduled email 'TechCorp + FusionLabs — KubeCon Europe proposal'."""
    email = find_email_by_id(state, "email_103")
    email["isDraft"] = True
    email["isScheduled"] = False
    email["scheduledTime"] = None
    email["folder"] = "drafts"


def solve_task_25(state):
    """Create label 'Design System' with blue color."""
    lid = next_label_id(state)
    state["labels"].append({
        "id": lid,
        "name": "Design System",
        "color": {"background": "#e8f0fe", "text": "#1a73e8"},
        "isSystem": False,
        "isAutoLabel": False
    })


def solve_task_26(state):
    """Rename label 'Read Later' to 'Bookmark'."""
    label = find_label_by_name(state, "Read Later")
    label["name"] = "Bookmark"


def solve_task_27(state):
    """Change 'Customer' label color to orange."""
    label = find_label_by_name(state, "Customer")
    label["color"] = {"background": "#fff3e0", "text": "#e65100"}


def solve_task_28(state):
    """Delete 'Partnership' label and remove from all emails."""
    label_id = "label_9"
    state["labels"] = [l for l in state["labels"] if l["id"] != label_id]
    for email in state["emails"]:
        email["labels"] = [l for l in email["labels"] if l != label_id]


def solve_task_29(state):
    """Create label 'Infrastructure' with teal color."""
    lid = next_label_id(state)
    state["labels"].append({
        "id": lid,
        "name": "Infrastructure",
        "color": {"background": "#e0f2f1", "text": "#00695c"},
        "isSystem": False,
        "isAutoLabel": False
    })


def solve_task_30(state):
    """Change theme to light."""
    state["settings"]["general"]["theme"] = "light"


def solve_task_31(state):
    """Change density to compact."""
    state["settings"]["general"]["density"] = "compact"


def solve_task_32(state):
    """Disable keyboard shortcuts."""
    state["settings"]["general"]["keyboardShortcuts"] = False


def solve_task_33(state):
    """Enable sound notifications."""
    state["settings"]["general"]["soundNotifications"] = True


def solve_task_34(state):
    """Disable desktop notifications."""
    state["settings"]["general"]["desktopNotifications"] = False


def solve_task_35(state):
    """Disable auto-advance."""
    state["settings"]["general"]["autoAdvance"] = False


def solve_task_36(state):
    """Change undo-send delay to 30."""
    state["settings"]["general"]["undoSendDelay"] = 30


def solve_task_37(state):
    """Change default reply action to reply."""
    state["settings"]["general"]["defaultReplyAction"] = "reply"


def solve_task_38(state):
    """Change density to spacious."""
    state["settings"]["general"]["density"] = "spacious"


def solve_task_39(state):
    """Disable split inbox."""
    state["settings"]["splitInbox"]["enabled"] = False


def solve_task_40(state):
    """Remove News split."""
    state["splits"] = [s for s in state["splits"] if s["id"] != "split_newsletters"]
    state["settings"]["splitInbox"]["splits"] = [
        sid for sid in state["settings"]["splitInbox"]["splits"]
        if sid != "split_newsletters"
    ]


def solve_task_41(state):
    """Change reminder default time to 14:00."""
    state["settings"]["reminders"]["defaultTime"] = "14:00"


def solve_task_42(state):
    """Change auto-reminders to external-only."""
    state["settings"]["reminders"]["autoReminders"] = "external-only"


def solve_task_43(state):
    """Change auto-reminder delay to 5."""
    state["settings"]["reminders"]["autoReminderDelay"] = 5


def solve_task_44(state):
    """Disable read statuses."""
    state["settings"]["readStatuses"]["enabled"] = False


def solve_task_45(state):
    """Disable team read statuses."""
    state["settings"]["readStatuses"]["teamReadStatuses"] = False


def solve_task_46(state):
    """Disable team reply indicators."""
    state["settings"]["readStatuses"]["teamReplyIndicators"] = False


def solve_task_47(state):
    """Disable follow-up auto-drafts."""
    state["settings"]["autoDrafts"]["followUps"] = False


def solve_task_48(state):
    """Disable scheduling auto-drafts."""
    state["settings"]["autoDrafts"]["scheduling"] = False


def solve_task_49(state):
    """Change calendar default view to day."""
    state["settings"]["calendar"]["defaultView"] = "day"


def solve_task_50(state):
    """Change week starts on to monday."""
    state["settings"]["calendar"]["weekStartsOn"] = "monday"


def solve_task_51(state):
    """Disable show weekends."""
    state["settings"]["calendar"]["showWeekends"] = False


def solve_task_52(state):
    """Change default meeting duration to 60."""
    state["settings"]["calendar"]["defaultMeetingDuration"] = 60


def solve_task_53(state):
    """Change event notifications to 30-minutes."""
    state["settings"]["calendar"]["eventNotifications"] = "30-minutes"


def solve_task_54(state):
    """Enable auto-archive with Newsletters and Receipts."""
    state["settings"]["autoArchive"]["enabled"] = True
    state["settings"]["autoArchive"]["autoLabels"] = [
        "autolabel_newsletters", "autolabel_receipts"
    ]


def solve_task_55(state):
    """Update signature to include CTO."""
    state["settings"]["signatures"]["default"] = (
        "<p>Best regards,<br>Alex Morgan<br>"
        "VP of Engineering & CTO, TechCorp<br>"
        "alex.morgan@techcorp.io</p>"
    )


def solve_task_56(state):
    """Disable Newsletters auto-label."""
    al = find_auto_label_by_name(state, "Newsletters")
    al["isEnabled"] = False


def solve_task_57(state):
    """Enable Finance auto-label."""
    al = find_auto_label_by_name(state, "Finance")
    al["isEnabled"] = True


def solve_task_58(state):
    """Create snippet 'Quick Acknowledgment'."""
    sid = next_snippet_id(state)
    state["snippets"].append({
        "id": sid,
        "name": "Quick Acknowledgment",
        "body": "<p>Thanks for your email. I will review and get back to you shortly.</p>",
        "variables": [],
        "placeholders": [],
        "isShared": False,
        "author": state["currentUser"]["name"],
        "metrics": {"sends": 0, "openRate": 0, "responseRate": 0},
        "createdAt": "2026-03-02T12:00:00Z",
        "updatedAt": "2026-03-02T12:00:00Z"
    })


def solve_task_59(state):
    """Delete snippet 'Out of Office'."""
    state["snippets"] = [
        s for s in state["snippets"] if s["name"] != "Out of Office"
    ]


def solve_task_60(state):
    """Rename snippet 'Meeting Follow-Up' to 'Post-Meeting Summary'."""
    snip = find_snippet_by_name(state, "Meeting Follow-Up")
    snip["name"] = "Post-Meeting Summary"


def solve_task_61(state):
    """Delete calendar event 'Company Holiday — No Meetings'."""
    state["calendarEvents"] = [
        e for e in state["calendarEvents"]
        if "Company Holiday" not in e["title"]
    ]


def solve_task_62(state):
    """Create calendar event 'Q2 Planning Session'."""
    eid = next_event_id(state)
    state["calendarEvents"].append({
        "id": eid,
        "title": "Q2 Planning Session",
        "start": "2026-03-20T10:00:00-05:00",
        "end": "2026-03-20T12:00:00-05:00",
        "location": "",
        "description": "",
        "attendees": [],
        "meetingLink": None,
        "calendar": "Work",
        "color": "#4285f4",
        "isAllDay": False,
        "recurrence": None
    })


def solve_task_63(state):
    """Block sender 'alerts@domainrenewal-notice.info'."""
    target = "alerts@domainrenewal-notice.info"
    if not any(b["email"] == target for b in state["blockedSenders"]):
        state["blockedSenders"].append({
            "email": target,
            "blockedAt": "2026-03-02T12:00:00Z"
        })


def solve_task_64(state):
    """Unblock sender 'promos@cheapdeals.biz'."""
    state["blockedSenders"] = [
        b for b in state["blockedSenders"]
        if b["email"] != "promos@cheapdeals.biz"
    ]


def solve_task_65(state):
    """Change meeting link provider to zoom."""
    state["settings"]["calendar"]["meetingLinkProvider"] = "zoom"


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
    "task_56": solve_task_56,
    "task_57": solve_task_57,
    "task_58": solve_task_58,
    "task_59": solve_task_59,
    "task_60": solve_task_60,
    "task_61": solve_task_61,
    "task_62": solve_task_62,
    "task_63": solve_task_63,
    "task_64": solve_task_64,
    "task_65": solve_task_65,
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
    while port < start + 200:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("", port))
                return port
            except OSError:
                port += 1
    raise RuntimeError(f"No free port found in range {start}-{start+200}")


def start_server(port):
    """Start the Superhuman server on the given port."""
    proc = subprocess.Popen(
        [sys.executable, "server.py", "--port", str(port)],
        cwd=str(APP_DIR),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    # Wait for server to be ready
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

        # Wait briefly for reset to settle
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
        # Seed the server with initial state so GET /api/state works
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
