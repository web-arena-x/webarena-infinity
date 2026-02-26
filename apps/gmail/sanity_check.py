#!/usr/bin/env python3
"""
Sanity check for Gmail real-task verifiers.

For each task, directly constructs the expected end-state (bypassing the agent),
then runs the verifier and asserts it returns True. This confirms that verifiers
correctly recognize a solved task.

Usage:
    python3 sanity_check.py                      # All tasks, sequential
    python3 sanity_check.py --workers N           # N parallel environments
    python3 sanity_check.py --task-id <id>        # Single task (for debugging)
    python3 sanity_check.py --port <base>         # Custom base port
"""

import argparse
import copy
import importlib.util
import json
import os
import signal
import subprocess
import sys
import time

import requests

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
APP_DIR = os.path.dirname(os.path.abspath(__file__))
TASKS_FILE = os.path.join(APP_DIR, "real-tasks.json")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def find_email(state, email_id):
    """Find an email by ID."""
    return next(e for e in state["emails"] if e["id"] == email_id)


def find_label_by_id(state, label_id):
    """Find a label by its ID."""
    return next(l for l in state["labels"] if l["id"] == label_id)


def find_filter_by_id(state, filter_id):
    """Find a filter by its ID."""
    return next(f for f in state["filters"] if f["id"] == filter_id)


# ---------------------------------------------------------------------------
# Seed state loader (evaluates data.js via Node)
# ---------------------------------------------------------------------------
_NODE_SCRIPT = r"""
const fs = require('fs');
const path = require('path');

const appDir = process.argv[1];
const dataCode = fs.readFileSync(path.join(appDir, 'js', 'data.js'), 'utf-8');

// data.js uses const — wrap in a function so the declarations are local
const fn = new Function(dataCode + `
    return {
        SEED_DATA_VERSION, CURRENT_USER, CONTACTS, LABELS,
        EMAILS, FILTERS, SETTINGS, BLOCKED_SENDERS
    };
`);
const data = fn();

const state = {
    emails: JSON.parse(JSON.stringify(data.EMAILS)),
    labels: JSON.parse(JSON.stringify(data.LABELS)),
    filters: JSON.parse(JSON.stringify(data.FILTERS)),
    settings: JSON.parse(JSON.stringify(data.SETTINGS)),
    contacts: JSON.parse(JSON.stringify(data.CONTACTS)),
    blockedSenders: JSON.parse(JSON.stringify(data.BLOCKED_SENDERS)),
    currentUser: JSON.parse(JSON.stringify(data.CURRENT_USER)),
    _nextEmailId: 200,
    _nextLabelId: 30,
    _nextFilterId: 20,
    _seedDataVersion: data.SEED_DATA_VERSION,
};

// Recalculate label counts (mirrors AppState._recalculateLabelCounts)
for (const label of state.labels) {
    const matches = state.emails.filter(e => {
        if (e.isTrashed || e.isSpam || e.isDraft) return false;
        return e.labels.includes(label.id);
    });
    label.messageCount = matches.length;
    label.unreadCount = matches.filter(e => !e.isRead).length;
}

process.stdout.write(JSON.stringify(state));
"""


def load_seed_state():
    """Evaluate data.js via Node and return the seed state dict."""
    result = subprocess.run(
        ["node", "-e", _NODE_SCRIPT, APP_DIR],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"ERROR: Failed to load seed data via Node:\n{result.stderr}", file=sys.stderr)
        sys.exit(1)
    return json.loads(result.stdout)


# ---------------------------------------------------------------------------
# Server management
# ---------------------------------------------------------------------------
def kill_port(port):
    """Kill any process listening on the given port."""
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
    """Start server.py on the given port, returning the Popen object."""
    kill_port(port)
    proc = subprocess.Popen(
        [sys.executable, "server.py", "--port", str(port)],
        cwd=APP_DIR,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return proc


def wait_for_server(port, timeout=10):
    """Poll until the server responds, return True if ready."""
    url = f"http://localhost:{port}/api/state"
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            r = requests.get(url, timeout=1)
            # 404 is expected (no state yet), but means the server is up
            if r.status_code in (200, 404):
                return True
        except requests.ConnectionError:
            pass
        time.sleep(0.2)
    return False


def stop_server(proc):
    """Stop the server process."""
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
def load_verifier(task_id):
    """Dynamically load a verifier module and return its verify function."""
    path = os.path.join(APP_DIR, "real-tasks", f"{task_id}.py")
    spec = importlib.util.spec_from_file_location(task_id, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.verify


# ---------------------------------------------------------------------------
# Solver functions — one per task
# ---------------------------------------------------------------------------

# ---- Easy ----

def solve_task_e1(state):
    """Star Sarah Chen's Q1 product roadmap email."""
    email = find_email(state, 1)
    email["isStarred"] = True
    email["starType"] = "yellow-star"


def solve_task_e2(state):
    """Mark Sophie Laurent's conference invitation as read."""
    email = find_email(state, 14)
    email["isRead"] = True


def solve_task_e3(state):
    """Trash Tom Bradley's property listing email."""
    email = find_email(state, 15)
    email["isTrashed"] = True
    if "INBOX" in email["labels"]:
        email["labels"].remove("INBOX")


def solve_task_e4(state):
    """Archive Carlos Mendez's shipping update."""
    email = find_email(state, 19)
    email["isArchived"] = True
    if "INBOX" in email["labels"]:
        email["labels"].remove("INBOX")


def solve_task_e5(state):
    """Turn off conversation view."""
    state["settings"]["conversationView"] = False


def solve_task_e6(state):
    """Switch to dark mode."""
    state["settings"]["theme"] = "dark"


def solve_task_e7(state):
    """Remove importance from Jennifer Wu's collaboration proposal."""
    email = find_email(state, 20)
    email["isImportant"] = False
    if "IMPORTANT" in email["labels"]:
        email["labels"].remove("IMPORTANT")


def solve_task_e8(state):
    """Remove star from Emily Rodriguez's partnership email."""
    email = find_email(state, 7)
    email["isStarred"] = False
    email["starType"] = None


def solve_task_e9(state):
    """Change undo send timer to 30 seconds."""
    state["settings"]["undoSendDelay"] = 30


def solve_task_e10(state):
    """Mark Priya's API integration email as read."""
    email = find_email(state, 2)
    email["isRead"] = True


def solve_task_e11(state):
    """Trash Ana Gutierrez's volunteer event email."""
    email = find_email(state, 12)
    email["isTrashed"] = True
    if "INBOX" in email["labels"]:
        email["labels"].remove("INBOX")


def solve_task_e12(state):
    """Turn off hover actions."""
    state["settings"]["hoverActions"] = False


def solve_task_e13(state):
    """Unmark Crypto Gains email as spam, move to inbox."""
    email = find_email(state, 93)
    email["isSpam"] = False
    if "INBOX" not in email["labels"]:
        email["labels"].append("INBOX")


def solve_task_e14(state):
    """Set default reply to reply all."""
    state["settings"]["defaultReplyBehavior"] = "reply-all"


def solve_task_e15(state):
    """Mark Design System Update as important."""
    email = find_email(state, 6)
    email["isImportant"] = True
    if "IMPORTANT" not in email["labels"]:
        email["labels"].append("IMPORTANT")


def solve_task_e16(state):
    """Unstar James O'Brien's contract review email."""
    email = find_email(state, 11)
    email["isStarred"] = False
    email["starType"] = None


def solve_task_e17(state):
    """Switch to compact density."""
    state["settings"]["density"] = "compact"


def solve_task_e18(state):
    """Turn off keyboard shortcuts."""
    state["settings"]["keyboardShortcutsEnabled"] = False


def solve_task_e19(state):
    """Unblock annoying@daily-deals.biz."""
    state["blockedSenders"] = [
        s for s in state["blockedSenders"]
        if s["email"] != "annoying@daily-deals.biz"
    ]


def solve_task_e20(state):
    """Set max page size to 25."""
    state["settings"]["maxPageSize"] = 25


# ---- Medium ----

def solve_task_m1(state):
    """Add Clients label to David Kim's tax season reminder."""
    email = find_email(state, 28)
    if "label_11" not in email["labels"]:
        email["labels"].append("label_11")


def solve_task_m2(state):
    """Create label 'Urgent' with red color."""
    lid = state["_nextLabelId"]
    state["_nextLabelId"] = lid + 1
    state["labels"].append({
        "id": f"label_{lid}",
        "name": "Urgent",
        "type": "user",
        "color": {"background": "#cc3333", "text": "#fff"},
        "visible": True,
        "parentId": None,
        "messageCount": 0,
        "unreadCount": 0,
    })


def solve_task_m3(state):
    """Move VC meetup email to Social category."""
    email = find_email(state, 30)
    email["labels"] = [l for l in email["labels"] if not l.startswith("CATEGORY_")]
    email["labels"].append("CATEGORY_SOCIAL")
    email["category"] = "social"


def solve_task_m4(state):
    """Snooze CI/CD Pipeline email until tomorrow."""
    email = find_email(state, 9)
    email["isSnoozed"] = True
    email["snoozeUntil"] = "2026-02-27T08:00:00.000Z"
    if "INBOX" in email["labels"]:
        email["labels"].remove("INBOX")


def solve_task_m5(state):
    """Remove Action Required label from contract review."""
    email = find_email(state, 11)
    if "label_17" in email["labels"]:
        email["labels"].remove("label_17")


def solve_task_m6(state):
    """Create filter for david.kim@financeplus.com -> Finance label."""
    fid = state["_nextFilterId"]
    state["_nextFilterId"] = fid + 1
    state["filters"].append({
        "id": f"filter_{fid}",
        "criteria": {
            "from": "david.kim@financeplus.com",
            "to": "", "subject": "", "hasWords": "", "doesntHave": "",
            "hasAttachment": False, "size": None, "sizeUnit": "MB",
            "sizeComparison": "greater",
        },
        "actions": {
            "label": "label_3", "archive": False, "markRead": False,
            "star": False, "forward": None, "delete": False,
            "neverSpam": False, "alwaysImportant": False,
            "neverImportant": False, "category": None,
        },
        "enabled": True,
        "createdAt": "2026-02-26T00:00:00Z",
    })


def solve_task_m7(state):
    """Block prince.of.lagos@hotmail.com."""
    state["blockedSenders"].append({
        "email": "prince.of.lagos@hotmail.com",
        "blockedAt": "2026-02-26T00:00:00Z",
    })


def solve_task_m8(state):
    """Disable Social category."""
    state["settings"]["categoriesEnabled"]["social"] = False


def solve_task_m9(state):
    """Rename Reference label to Resources."""
    label = find_label_by_id(state, "label_19")
    label["name"] = "Resources"


def solve_task_m10(state):
    """Delete GitHub notification filter."""
    state["filters"] = [
        f for f in state["filters"]
        if f.get("criteria", {}).get("from") != "notifications@github.com"
    ]


def solve_task_m11(state):
    """Turn off Send and Archive."""
    state["settings"]["sendAndArchive"] = False


def solve_task_m12(state):
    """Disable Forums category."""
    state["settings"]["categoriesEnabled"]["forums"] = False


def solve_task_m13(state):
    """Archive latest Morning Brew newsletter."""
    email = find_email(state, 77)
    email["isArchived"] = True
    if "INBOX" in email["labels"]:
        email["labels"].remove("INBOX")


def solve_task_m14(state):
    """Add Projects label to office renovation email."""
    email = find_email(state, 17)
    if "label_9" not in email["labels"]:
        email["labels"].append("label_9")


def solve_task_m15(state):
    """Switch inbox type to Important first."""
    state["settings"]["inboxType"] = "important-first"


def solve_task_m16(state):
    """Empty spam folder."""
    state["emails"] = [e for e in state["emails"] if not e.get("isSpam")]


def solve_task_m17(state):
    """Move archived sprint planning notes back to inbox."""
    email = find_email(state, 85)
    email["isArchived"] = False
    if "INBOX" not in email["labels"]:
        email["labels"].append("INBOX")


def solve_task_m18(state):
    """Turn off reply nudge suggestions."""
    state["settings"]["nudges"]["suggestEmailsToReply"] = False


def solve_task_m19(state):
    """Set auto-advance to older."""
    state["settings"]["autoAdvance"] = "older"


def solve_task_m20(state):
    """Change button labels to text."""
    state["settings"]["buttonLabels"] = "text"


# ---- Hard ----

def solve_task_h1(state):
    """Create 'Q1 Priority' nested under Work, apply to email 1."""
    lid = state["_nextLabelId"]
    state["_nextLabelId"] = lid + 1
    new_id = f"label_{lid}"
    state["labels"].append({
        "id": new_id,
        "name": "Q1 Priority",
        "type": "user",
        "color": {"background": "#2962ff", "text": "#fff"},
        "visible": True,
        "parentId": "label_1",
        "messageCount": 0,
        "unreadCount": 0,
    })
    email = find_email(state, 1)
    email["labels"].append(new_id)


def solve_task_h2(state):
    """Update Datadog alerts filter to archive and forward to priya."""
    filt = find_filter_by_id(state, "filter_10")
    filt["actions"]["archive"] = True
    filt["actions"]["forward"] = "priya.sharma@cloudnine.dev"


def solve_task_h3(state):
    """Archive all unread social emails."""
    for eid in [31, 33, 37, 43]:
        email = find_email(state, eid)
        email["isArchived"] = True
        if "INBOX" in email["labels"]:
            email["labels"].remove("INBOX")


def solve_task_h4(state):
    """Create filter for invoice/payment -> Invoices label + mark read."""
    fid = state["_nextFilterId"]
    state["_nextFilterId"] = fid + 1
    state["filters"].append({
        "id": f"filter_{fid}",
        "criteria": {
            "from": "", "to": "", "subject": "invoice",
            "hasWords": "payment", "doesntHave": "",
            "hasAttachment": False, "size": None, "sizeUnit": "MB",
            "sizeComparison": "greater",
        },
        "actions": {
            "label": "label_15", "archive": False, "markRead": True,
            "star": False, "forward": None, "delete": False,
            "neverSpam": False, "alwaysImportant": False,
            "neverImportant": False, "category": None,
        },
        "enabled": True,
        "createdAt": "2026-02-26T00:00:00Z",
    })


def solve_task_h5(state):
    """Trash Amazon, Nike, REI promo emails."""
    for eid in [44, 52, 55]:
        email = find_email(state, eid)
        email["isTrashed"] = True
        if "INBOX" in email["labels"]:
            email["labels"].remove("INBOX")


def solve_task_h6(state):
    """Change United Airlines star to green, move to Primary, add Action Required."""
    email = find_email(state, 49)
    email["isStarred"] = True
    email["starType"] = "green-star"
    email["labels"] = [l for l in email["labels"] if not l.startswith("CATEGORY_")]
    email["labels"].append("CATEGORY_PRIMARY")
    email["category"] = "primary"
    if "label_17" not in email["labels"]:
        email["labels"].append("label_17")


def solve_task_h7(state):
    """Create 'Taxes' under Finance, apply to emails 28 and 122."""
    lid = state["_nextLabelId"]
    state["_nextLabelId"] = lid + 1
    new_id = f"label_{lid}"
    state["labels"].append({
        "id": new_id,
        "name": "Taxes",
        "type": "user",
        "color": {"background": "#fff9c4", "text": "#f57f17"},
        "visible": True,
        "parentId": "label_3",
        "messageCount": 0,
        "unreadCount": 0,
    })
    for eid in [28, 122]:
        email = find_email(state, eid)
        email["labels"].append(new_id)


def solve_task_h8(state):
    """Multiple settings changes."""
    state["settings"]["theme"] = "dark"
    state["settings"]["density"] = "compact"
    state["settings"]["hoverActions"] = False
    state["settings"]["dynamicEmail"] = False
    state["settings"]["undoSendDelay"] = 20


def solve_task_h9(state):
    """Configure multiple inbox sections."""
    sections = state["settings"]["multipleInboxSections"]
    sections[0]["query"] = "is:important"
    sections[0]["name"] = "Priority"
    sections[1]["query"] = "label:Action Required"
    sections[1]["name"] = "Action Items"


def solve_task_h10(state):
    """Remove user labels from email 29, add Waiting For Reply."""
    email = find_email(state, 29)
    email["labels"] = [l for l in email["labels"] if l not in ("label_1", "label_9")]
    if "label_18" not in email["labels"]:
        email["labels"].append("label_18")


def solve_task_h11(state):
    """Trash unread primary emails with attachments."""
    for eid in [1, 6, 9, 26]:
        email = find_email(state, eid)
        email["isTrashed"] = True
        if "INBOX" in email["labels"]:
            email["labels"].remove("INBOX")


def solve_task_h12(state):
    """Mark email 6 as read, star with blue, add Projects label."""
    email = find_email(state, 6)
    email["isRead"] = True
    email["isStarred"] = True
    email["starType"] = "blue-star"
    if "label_9" not in email["labels"]:
        email["labels"].append("label_9")


def solve_task_h13(state):
    """Create 'Conferences' under Work, apply to emails 14 and 46."""
    lid = state["_nextLabelId"]
    state["_nextLabelId"] = lid + 1
    new_id = f"label_{lid}"
    state["labels"].append({
        "id": new_id,
        "name": "Conferences",
        "type": "user",
        "color": {"background": "#c8e6c9", "text": "#2e7d32"},
        "visible": True,
        "parentId": "label_1",
        "messageCount": 0,
        "unreadCount": 0,
    })
    for eid in [14, 46]:
        email = find_email(state, eid)
        email["labels"].append(new_id)


def solve_task_h14(state):
    """Disable Promotions, Updates, Forums + set inbox to Important first."""
    state["settings"]["categoriesEnabled"]["promotions"] = False
    state["settings"]["categoriesEnabled"]["updates"] = False
    state["settings"]["categoriesEnabled"]["forums"] = False
    state["settings"]["inboxType"] = "important-first"


def solve_task_h15(state):
    """Edit Morning Brew filter to archive + mark read."""
    filt = find_filter_by_id(state, "filter_2")
    filt["actions"]["archive"] = True
    filt["actions"]["markRead"] = True


def solve_task_h16(state):
    """Create filter for attachments > 5MB -> Reference + archive."""
    fid = state["_nextFilterId"]
    state["_nextFilterId"] = fid + 1
    state["filters"].append({
        "id": f"filter_{fid}",
        "criteria": {
            "from": "", "to": "", "subject": "", "hasWords": "",
            "doesntHave": "", "hasAttachment": True,
            "size": 5, "sizeUnit": "MB", "sizeComparison": "greater",
        },
        "actions": {
            "label": "label_19", "archive": True, "markRead": False,
            "star": False, "forward": None, "delete": False,
            "neverSpam": False, "alwaysImportant": False,
            "neverImportant": False, "category": None,
        },
        "enabled": True,
        "createdAt": "2026-02-26T00:00:00Z",
    })


def solve_task_h17(state):
    """Archive all Newsletters-labeled emails in inbox."""
    for email in state["emails"]:
        if "label_6" in email.get("labels", []) and "INBOX" in email.get("labels", []):
            email["isArchived"] = True
            email["labels"].remove("INBOX")


def solve_task_h18(state):
    """Unsnooze mortgage email, add Action Required label."""
    email = find_email(state, 83)
    email["isSnoozed"] = False
    email["snoozeUntil"] = None
    if "INBOX" not in email["labels"]:
        email["labels"].append("INBOX")
    if "label_17" not in email["labels"]:
        email["labels"].append("label_17")


def solve_task_h19(state):
    """Empty trash, then unmark all spam."""
    state["emails"] = [e for e in state["emails"] if not e.get("isTrashed")]
    for email in state["emails"]:
        if email.get("isSpam"):
            email["isSpam"] = False
            if "INBOX" not in email.get("labels", []):
                email["labels"].append("INBOX")


def solve_task_h20(state):
    """Delete Receipts label, add Finance label to affected emails."""
    receipt_email_ids = [19, 22, 67, 69, 88]
    for email in state["emails"]:
        if email["id"] in receipt_email_ids:
            if "label_3" not in email["labels"]:
                email["labels"].append("label_3")
            if "label_5" in email["labels"]:
                email["labels"].remove("label_5")
    state["labels"] = [l for l in state["labels"] if l["id"] != "label_5"]


# ---------------------------------------------------------------------------
# Solver registry
# ---------------------------------------------------------------------------
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


# ---------------------------------------------------------------------------
# Test execution
# ---------------------------------------------------------------------------
def run_tasks(task_ids, port, seed_state):
    """Start a server on *port*, run each task, return list of (task_id, passed, msg)."""
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
                results.append((tid, False, f"Failed to seed server state: HTTP {r.status_code}"))
            return results

        for tid in task_ids:
            try:
                # Reset to seed
                requests.post(f"{base}/api/reset", timeout=5)

                # Fetch clean seed state
                resp = requests.get(f"{base}/api/state", timeout=5)
                state = resp.json()

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


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Gmail real-task sanity check")
    parser.add_argument("--workers", type=int, default=1, help="Parallel server workers")
    parser.add_argument("--task-id", type=str, default=None, help="Run a single task")
    parser.add_argument("--port", type=int, default=9100, help="Base port")
    args = parser.parse_args()

    # Load task list
    with open(TASKS_FILE) as f:
        tasks = json.load(f)
    all_task_ids = [t["id"] for t in tasks]

    # Determine which tasks to run
    if args.task_id:
        if args.task_id not in SOLVERS:
            print(f"Unknown task: {args.task_id}")
            print(f"Available: {', '.join(sorted(SOLVERS.keys()))}")
            sys.exit(1)
        task_ids = [args.task_id]
    else:
        task_ids = all_task_ids

    # Load seed state once
    print("Loading seed state from data.js...")
    seed_state = load_seed_state()
    print(f"  {len(seed_state['emails'])} emails, {len(seed_state['labels'])} labels, "
          f"{len(seed_state['filters'])} filters")
    print()

    # Run tasks
    all_results = []
    if args.workers <= 1:
        all_results = run_tasks(task_ids, args.port, seed_state)
    else:
        import concurrent.futures
        # Partition tasks across workers
        chunks = [[] for _ in range(args.workers)]
        for i, tid in enumerate(task_ids):
            chunks[i % args.workers].append(tid)

        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {}
            for i, chunk in enumerate(chunks):
                if chunk:
                    port = args.port + i
                    futures[executor.submit(run_tasks, chunk, port, copy.deepcopy(seed_state))] = chunk
            for future in concurrent.futures.as_completed(futures):
                all_results.extend(future.result())

    # Sort results by task ID
    order = {tid: i for i, tid in enumerate(all_task_ids)}
    all_results.sort(key=lambda r: order.get(r[0], 999))

    # Print results
    passed = 0
    failed = []
    for tid, ok, msg in all_results:
        status = "\033[32m  PASS\033[0m" if ok else "\033[31m  FAIL\033[0m"
        print(f"{status}  {tid:12s}  {msg}")
        if ok:
            passed += 1
        else:
            failed.append(tid)

    print()
    print(f"{passed}/{len(all_results)} passed")
    if failed:
        print(f"Failed: {', '.join(failed)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
