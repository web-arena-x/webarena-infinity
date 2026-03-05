#!/usr/bin/env python3
"""
Sanity check for Superhuman real-task verifiers.

For each task, directly constructs the expected end-state (bypassing the agent),
then runs the verifier and asserts it returns True.

Usage:
    python3 sanity_check_real.py                      # All tasks, sequential
    python3 sanity_check_real.py --workers N           # N parallel environments
    python3 sanity_check_real.py --task-id <id>        # Single task (for debugging)
    python3 sanity_check_real.py --port <base>         # Custom base port
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


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def find_email(state, email_id):
    """Find an email by ID string."""
    for e in state["emails"]:
        if e["id"] == email_id:
            return e
    raise ValueError(f"Email not found: {email_id}")


def find_auto_label(state, auto_label_id):
    """Find an auto label by ID."""
    for al in state["autoLabels"]:
        if al["id"] == auto_label_id:
            return al
    raise ValueError(f"Auto label not found: {auto_label_id}")


def find_snippet(state, snippet_id):
    """Find a snippet by ID."""
    for s in state["snippets"]:
        if s["id"] == snippet_id:
            return s
    raise ValueError(f"Snippet not found: {snippet_id}")


def next_label_id(state):
    """Get next label ID and increment counter."""
    lid = state.get("_nextLabelId", 30)
    state["_nextLabelId"] = lid + 1
    return f"label_{lid}"


def next_event_id(state):
    """Get next event ID and increment counter."""
    eid = state.get("_nextEventId", 30)
    state["_nextEventId"] = eid + 1
    return f"cal_{str(eid).zfill(3)}"


# ---------------------------------------------------------------------------
# Solver functions — one per task
# ---------------------------------------------------------------------------

# ---- Easy ----

def solve_task_e1(state):
    """Star Kevin Zhao's partnership inquiry."""
    email = find_email(state, "email_007")
    email["isStarred"] = True


def solve_task_e2(state):
    """Mark the AWS cost anomaly alert as read."""
    email = find_email(state, "email_033")
    email["isRead"] = True


def solve_task_e3(state):
    """Trash Olivia Turner's LinkedIn connection request."""
    email = find_email(state, "email_031")
    email["folder"] = "trash"


def solve_task_e4(state):
    """Remove the star from Marcus Williams' production outage email."""
    email = find_email(state, "email_004")
    email["isStarred"] = False


def solve_task_e5(state):
    """Switch to light mode."""
    state["settings"]["general"]["theme"] = "light"


def solve_task_e6(state):
    """Mark Elena's security audit report as read."""
    email = find_email(state, "email_012")
    email["isRead"] = True


def solve_task_e7(state):
    """Turn off desktop notifications."""
    state["settings"]["general"]["desktopNotifications"] = False


def solve_task_e8(state):
    """Set the undo send timer to 20 seconds."""
    state["settings"]["general"]["undoSendDelay"] = 20


def solve_task_e9(state):
    """Remove the star from Sandra Liu's Series B email."""
    email = find_email(state, "email_002")
    email["isStarred"] = False


def solve_task_e10(state):
    """Mark the Pragmatic Engineer newsletter as read."""
    email = find_email(state, "email_029")
    email["isRead"] = True


def solve_task_e11(state):
    """Switch to compact display density."""
    state["settings"]["general"]["density"] = "compact"


def solve_task_e12(state):
    """Disable keyboard shortcuts."""
    state["settings"]["general"]["keyboardShortcuts"] = False


def solve_task_e13(state):
    """Change the default reply action to Reply."""
    state["settings"]["general"]["defaultReplyAction"] = "reply"


def solve_task_e14(state):
    """Move the developer grant email from trash to inbox."""
    email = find_email(state, "email_104")
    email["folder"] = "inbox"


def solve_task_e15(state):
    """Unblock promos@cheapdeals.biz."""
    state["blockedSenders"] = [
        s for s in state["blockedSenders"]
        if s["email"] != "promos@cheapdeals.biz"
    ]


def solve_task_e16(state):
    """Mark Brian Scott's legal hold notice as read."""
    email = find_email(state, "email_019")
    email["isRead"] = True


def solve_task_e17(state):
    """Star Elena's SOC 2 audit prep email."""
    email = find_email(state, "email_125")
    email["isStarred"] = True


def solve_task_e18(state):
    """Mark the Vercel bandwidth alert as read."""
    email = find_email(state, "email_118")
    email["isRead"] = True


def solve_task_e19(state):
    """Turn on sound notifications."""
    state["settings"]["general"]["soundNotifications"] = True


def solve_task_e20(state):
    """Archive Rachel's LoopWorks renewal warning."""
    email = find_email(state, "email_014")
    email["folder"] = "done"


# ---- Medium ----

def solve_task_m1(state):
    """Apply the Project Alpha label to Jamie's Q2 roadmap email."""
    email = find_email(state, "email_115")
    if "label_1" not in email["labels"]:
        email["labels"].append("label_1")


def solve_task_m2(state):
    """Create a new label called 'Board Prep'."""
    lid = next_label_id(state)
    state["labels"].append({
        "id": lid,
        "name": "Board Prep",
        "color": {"background": "#e8f0fe", "text": "#1a73e8"},
        "isAutoLabel": False,
        "isSystem": False,
    })


def solve_task_m3(state):
    """Remove the Read Later label from the Pragmatic Engineer newsletter."""
    email = find_email(state, "email_029")
    if "label_8" in email["labels"]:
        email["labels"].remove("label_8")


def solve_task_m4(state):
    """Set a reminder on Olivia Turner's Prismatica integration email."""
    email = find_email(state, "email_036")
    email["reminder"] = {"date": "2026-03-03T09:00:00Z", "type": "manual"}


def solve_task_m5(state):
    """Archive Nathan Brooks' introduction email with Yuki Tanaka."""
    email = find_email(state, "email_013")
    email["folder"] = "done"


def solve_task_m6(state):
    """Disable the Newsletters auto label."""
    al = find_auto_label(state, "autolabel_newsletters")
    al["isEnabled"] = False


def solve_task_m7(state):
    """Block the sender of the 'Make $5000/week from home' spam email."""
    email = find_email(state, "email_109")
    sender_email = email["from"]["email"]
    state["blockedSenders"].append({
        "email": sender_email,
        "blockedAt": "2026-03-02T12:00:00Z",
    })


def solve_task_m8(state):
    """Rename the Read Later label to Bookmarks."""
    for label in state["labels"]:
        if label["id"] == "label_8":
            label["name"] = "Bookmarks"
            break


def solve_task_m9(state):
    """Cancel the scheduled weekly check-in email."""
    email = find_email(state, "email_101")
    email["isScheduled"] = False
    email["isDraft"] = True
    email["scheduledTime"] = None


def solve_task_m10(state):
    """Turn off split inbox."""
    state["settings"]["splitInbox"]["enabled"] = False


def solve_task_m11(state):
    """Archive the Figma comment email from Sofia."""
    email = find_email(state, "email_042")
    email["folder"] = "done"


def solve_task_m12(state):
    """Delete the Out of Office snippet."""
    state["snippets"] = [
        s for s in state["snippets"]
        if s["id"] != "snip_006"
    ]


def solve_task_m13(state):
    """Set the default meeting duration to 60 minutes."""
    state["settings"]["calendar"]["defaultMeetingDuration"] = 60


def solve_task_m14(state):
    """Remove the Customer label from Anita Sharma's DevBridge feedback email."""
    email = find_email(state, "email_039")
    if "label_6" in email["labels"]:
        email["labels"].remove("label_6")


def solve_task_m15(state):
    """Enable auto-archive for newsletters."""
    state["settings"]["autoArchive"]["enabled"] = True
    if "autolabel_newsletters" not in state["settings"]["autoArchive"]["autoLabels"]:
        state["settings"]["autoArchive"]["autoLabels"].append("autolabel_newsletters")


def solve_task_m16(state):
    """Change the calendar week start to Monday."""
    state["settings"]["calendar"]["weekStartsOn"] = "monday"


def solve_task_m17(state):
    """Move the v2 API launch go/no-go email from Done back to inbox."""
    email = find_email(state, "email_046")
    email["folder"] = "inbox"


def solve_task_m18(state):
    """Disable the Social auto label."""
    al = find_auto_label(state, "autolabel_social")
    al["isEnabled"] = False


def solve_task_m19(state):
    """Remove the Newsletters split from the inbox."""
    state["splits"] = [
        s for s in state["splits"]
        if s["id"] != "split_newsletters"
    ]
    # Also remove from settings
    splits_list = state["settings"]["splitInbox"].get("splits", [])
    if "split_newsletters" in splits_list:
        splits_list.remove("split_newsletters")


def solve_task_m20(state):
    """Switch the meeting link provider to Zoom."""
    state["settings"]["calendar"]["meetingLinkProvider"] = "zoom"


# ---- Hard ----

def solve_task_h1(state):
    """Archive all unread newsletters in the inbox."""
    # Seed: email_029, email_030, email_122 are inbox, unread, autolabel_newsletters
    for eid in ["email_029", "email_030", "email_122"]:
        email = find_email(state, eid)
        email["folder"] = "done"


def solve_task_h2(state):
    """Create 'Series B' label and apply to Fundraising inbox emails."""
    lid = next_label_id(state)
    state["labels"].append({
        "id": lid,
        "name": "Series B",
        "color": {"background": "#e6f4ea", "text": "#137333"},
        "isAutoLabel": False,
        "isSystem": False,
    })
    # Inbox emails with label_3 (Fundraising): email_002, 023, 026, 119, 120
    for eid in ["email_002", "email_023", "email_026", "email_119", "email_120"]:
        email = find_email(state, eid)
        if lid not in email["labels"]:
            email["labels"].append(lid)


def solve_task_h3(state):
    """Mark all unread calendar emails as read."""
    # Seed: unread inbox calendar split emails: email_021, 024, 026, 027
    for eid in ["email_021", "email_024", "email_026", "email_027"]:
        email = find_email(state, eid)
        email["isRead"] = True


def solve_task_h4(state):
    """Empty the spam folder and unblock spam@fakecorp.com."""
    state["emails"] = [e for e in state["emails"] if e.get("folder") != "spam"]
    state["blockedSenders"] = [
        s for s in state["blockedSenders"]
        if s["email"] != "spam@fakecorp.com"
    ]


def solve_task_h5(state):
    """Light theme, spacious density, no shortcuts, 30s undo send."""
    state["settings"]["general"]["theme"] = "light"
    state["settings"]["general"]["density"] = "spacious"
    state["settings"]["general"]["keyboardShortcuts"] = False
    state["settings"]["general"]["undoSendDelay"] = 30


def solve_task_h6(state):
    """Move all emails labeled Urgent to Done."""
    # Seed inbox emails with label_7: email_004, 009, 012, 014, 019, 125
    for eid in ["email_004", "email_009", "email_012", "email_014", "email_019", "email_125"]:
        email = find_email(state, eid)
        email["folder"] = "done"


def solve_task_h7(state):
    """Delete Partnership label, add Customer to inbox emails that had it."""
    # Inbox emails with label_9 in seed: email_007, email_013, email_041
    for eid in ["email_007", "email_013", "email_041"]:
        email = find_email(state, eid)
        if "label_9" in email["labels"]:
            email["labels"].remove("label_9")
        if "label_6" not in email["labels"]:
            email["labels"].append("label_6")
    # Remove label_9 from all other emails too
    for email in state["emails"]:
        if "label_9" in email.get("labels", []):
            email["labels"].remove("label_9")
    # Delete the label itself
    state["labels"] = [l for l in state["labels"] if l["id"] != "label_9"]


def solve_task_h8(state):
    """Add Urgent label to every unread inbox email with attachments."""
    # Seed: email_001 (unread, attachments, inbox), email_027 (unread, attachments, inbox),
    # email_125 (unread, attachments, inbox — already has label_7)
    for eid in ["email_001", "email_027", "email_125"]:
        email = find_email(state, eid)
        if "label_7" not in email["labels"]:
            email["labels"].append("label_7")


def solve_task_h9(state):
    """Disable every auto label and turn off split inbox."""
    for al in state["autoLabels"]:
        al["isEnabled"] = False
    state["settings"]["splitInbox"]["enabled"] = False


def solve_task_h10(state):
    """Create 'Investor Relations' label and apply to Fundraising inbox emails."""
    lid = next_label_id(state)
    state["labels"].append({
        "id": lid,
        "name": "Investor Relations",
        "color": {"background": "#e0f7fa", "text": "#00695c"},
        "isAutoLabel": False,
        "isSystem": False,
    })
    # Inbox emails with label_3: email_002, 023, 026, 119, 120
    for eid in ["email_002", "email_023", "email_026", "email_119", "email_120"]:
        email = find_email(state, eid)
        if lid not in email["labels"]:
            email["labels"].append(lid)


def solve_task_h11(state):
    """Block the sender of every spam email and mark them all as read."""
    blocked_set = {s["email"] for s in state["blockedSenders"]}
    for email in state["emails"]:
        if email.get("folder") == "spam":
            sender = email["from"]["email"]
            if sender not in blocked_set:
                state["blockedSenders"].append({
                    "email": sender,
                    "blockedAt": "2026-03-02T12:00:00Z",
                })
                blocked_set.add(sender)
            email["isRead"] = True


def solve_task_h12(state):
    """Enable auto-archive for newsletters and receipts, archive newsletter inbox emails."""
    state["settings"]["autoArchive"]["enabled"] = True
    al = state["settings"]["autoArchive"]["autoLabels"]
    for label_id in ["autolabel_newsletters", "autolabel_receipts"]:
        if label_id not in al:
            al.append(label_id)
    # Archive inbox newsletter emails: email_029, 030, 122
    for eid in ["email_029", "email_030", "email_122"]:
        email = find_email(state, eid)
        email["folder"] = "done"


def solve_task_h13(state):
    """Create a calendar event for team lunch on March 9th."""
    eid = next_event_id(state)
    state["calendarEvents"].append({
        "id": eid,
        "title": "Team Lunch",
        "start": "2026-03-09T12:00:00-05:00",
        "end": "2026-03-09T13:00:00-05:00",
        "location": "TechCorp Cafe",
        "description": "Team lunch.",
        "attendees": [],
        "meetingLink": None,
        "calendar": "Work",
        "color": "#4285f4",
        "isAllDay": False,
        "recurrence": None,
    })


def solve_task_h14(state):
    """Star Kevin Zhao's partnership inquiry, add Urgent, set reminder."""
    email = find_email(state, "email_007")
    email["isStarred"] = True
    if "label_7" not in email["labels"]:
        email["labels"].append("label_7")
    email["reminder"] = {"date": "2026-03-03T09:00:00Z", "type": "manual"}


def solve_task_h15(state):
    """Remove all labels from Marcus's weekly team digest and archive it."""
    email = find_email(state, "email_045")
    email["labels"] = []
    email["folder"] = "done"


def solve_task_h16(state):
    """Rename Bug Report Acknowledgment snippet to 'Issue Response', make private."""
    snippet = find_snippet(state, "snip_008")
    snippet["name"] = "Issue Response"
    snippet["isShared"] = False


def solve_task_h17(state):
    """Archive all calendar invite emails in the inbox."""
    # Seed inbox emails with split='calendar': 021-028, 116
    for eid in ["email_021", "email_022", "email_023", "email_024",
                "email_025", "email_026", "email_027", "email_028", "email_116"]:
        email = find_email(state, eid)
        email["folder"] = "done"


def solve_task_h18(state):
    """Delete all emails in the trash and mark every spam email as read."""
    state["emails"] = [e for e in state["emails"] if e.get("folder") != "trash"]
    for email in state["emails"]:
        if email.get("folder") == "spam":
            email["isRead"] = True


def solve_task_h19(state):
    """Unstar outage email, remove all labels, archive it."""
    email = find_email(state, "email_004")
    email["isStarred"] = False
    email["labels"] = []
    email["folder"] = "done"


def solve_task_h20(state):
    """Disable team read statuses/reply indicators, auto-drafts follow-ups, external-only reminders."""
    state["settings"]["readStatuses"]["teamReadStatuses"] = False
    state["settings"]["readStatuses"]["teamReplyIndicators"] = False
    state["settings"]["autoDrafts"]["followUps"] = False
    state["settings"]["reminders"]["autoReminders"] = "external-only"


# ---- Hardening Round 1 ----

def solve_task_h21(state):
    """Archive the email from the customer stuck on data export for two weeks."""
    email = find_email(state, "email_009")
    email["folder"] = "done"


def solve_task_h22(state):
    """Mark v2 API beta feedback as read, add Project Alpha label, set reminder."""
    email = find_email(state, "email_114")
    email["isRead"] = True
    if "label_1" not in email["labels"]:
        email["labels"].append("label_1")
    email["reminder"] = {"date": "2026-03-03T09:00:00Z", "type": "manual"}


def solve_task_h23(state):
    """Mark unread TechCorp teammate emails as read; star those with Engineering label."""
    targets = ["email_001", "email_012", "email_014", "email_024",
               "email_114", "email_115", "email_124", "email_125"]
    star_targets = {"email_012", "email_114", "email_115", "email_125"}
    for eid in targets:
        email = find_email(state, eid)
        email["isRead"] = True
        if eid in star_targets:
            email["isStarred"] = True


def solve_task_h24(state):
    """Delete Hiring Panel calendar event and archive the invite email."""
    state["calendarEvents"] = [
        e for e in state["calendarEvents"] if e["id"] != "cal_016"
    ]
    email = find_email(state, "email_116")
    email["folder"] = "done"


def solve_task_h25(state):
    """Apply Urgent label to Brian Scott's MSA contract redlines email."""
    email = find_email(state, "email_003")
    if "label_7" not in email["labels"]:
        email["labels"].append("label_7")


def solve_task_h26(state):
    """Rename snippet with most sends to include (Top Performer)."""
    # snip_008 has 52 sends — the highest
    snippet = find_snippet(state, "snip_008")
    snippet["name"] = "Bug Report Acknowledgment (Top Performer)"


def solve_task_h27(state):
    """Turn off Personal calendar and delete all Personal calendar events."""
    for cal in state["settings"]["calendar"]["calendars"]:
        if cal["id"] == "cal_personal":
            cal["enabled"] = False
            break
    state["calendarEvents"] = [
        e for e in state["calendarEvents"]
        if e["id"] not in ("cal_005", "cal_013", "cal_015")
    ]


def solve_task_h28(state):
    """Update signature to CTO, set undo send delay to 30."""
    sig = state["settings"]["signatures"]["default"]
    state["settings"]["signatures"]["default"] = sig.replace(
        "VP of Engineering", "CTO"
    )
    state["settings"]["general"]["undoSendDelay"] = 30


def solve_task_h29(state):
    """Remove Read Later label from all emails and delete the label."""
    # Remove label_8 from all emails
    for email in state["emails"]:
        if "label_8" in email.get("labels", []):
            email["labels"].remove("label_8")
    # Delete label_8
    state["labels"] = [l for l in state["labels"] if l["id"] != "label_8"]


def solve_task_h30(state):
    """Add Urgent label to email mentioning competing offer expiring March 20th."""
    email = find_email(state, "email_005")
    if "label_7" not in email["labels"]:
        email["labels"].append("label_7")


def solve_task_h31(state):
    """Star every Fundraising inbox email and enable auto-archive for receipts."""
    for eid in ["email_002", "email_023", "email_026", "email_119", "email_120"]:
        email = find_email(state, eid)
        email["isStarred"] = True
    state["settings"]["autoArchive"]["enabled"] = True
    if "autolabel_receipts" not in state["settings"]["autoArchive"]["autoLabels"]:
        state["settings"]["autoArchive"]["autoLabels"].append("autolabel_receipts")


def solve_task_h32(state):
    """Change event notifications to 30 minutes, default view to day."""
    state["settings"]["calendar"]["eventNotifications"] = "30-minutes"
    state["settings"]["calendar"]["defaultView"] = "day"


def solve_task_h33(state):
    """Cancel the scheduled email to QuantumLeap contact."""
    email = find_email(state, "email_102")
    email["isScheduled"] = False
    email["isDraft"] = True
    email["scheduledTime"] = None


def solve_task_h34(state):
    """Apply Partnership label to TechCrunch feature email, set reminder for deadline."""
    email = find_email(state, "email_010")
    if "label_9" not in email["labels"]:
        email["labels"].append("label_9")
    email["reminder"] = {"date": "2026-03-09T09:00:00Z", "type": "manual"}


def solve_task_h35(state):
    """Create 'Pending Decision' label and apply to inbox emails with reminders."""
    lid = next_label_id(state)
    state["labels"].append({
        "id": lid,
        "name": "Pending Decision",
        "color": {"background": "#fef7e0", "text": "#b06000"},
        "isAutoLabel": False,
        "isSystem": False,
    })
    # Inbox emails with reminders: email_002, 003, 005, 009, 119
    for eid in ["email_002", "email_003", "email_005", "email_009", "email_119"]:
        email = find_email(state, eid)
        if lid not in email["labels"]:
            email["labels"].append(lid)


def solve_task_h36(state):
    """Turn off auto-advance, disable show weekends, set auto-reminder delay to 7."""
    state["settings"]["general"]["autoAdvance"] = False
    state["settings"]["calendar"]["showWeekends"] = False
    state["settings"]["reminders"]["autoReminderDelay"] = 7


def solve_task_h37(state):
    """Archive every unread email in the Other split of the inbox."""
    for eid in ["email_029", "email_030", "email_033", "email_042",
                "email_118", "email_122"]:
        email = find_email(state, eid)
        email["folder"] = "done"


def solve_task_h38(state):
    """Delete Feature Request Response snippet, rename Partnership Proposal, make shared."""
    state["snippets"] = [
        s for s in state["snippets"] if s["id"] != "snip_007"
    ]
    snippet = find_snippet(state, "snip_009")
    snippet["name"] = "Business Proposal"
    snippet["isShared"] = True


def solve_task_h39(state):
    """Move all trash emails to inbox and unblock all blocked senders."""
    for eid in ["email_104", "email_105", "email_106", "email_107", "email_108"]:
        email = find_email(state, eid)
        email["folder"] = "inbox"
    state["blockedSenders"] = []


def solve_task_h40(state):
    """Move SREcon talk acceptance from Done to inbox and apply Engineering label."""
    email = find_email(state, "email_076")
    email["folder"] = "inbox"
    if "label_10" not in email["labels"]:
        email["labels"].append("label_10")


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


# ---------------------------------------------------------------------------
# Server management
# ---------------------------------------------------------------------------
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
    """Start the Superhuman server on the given port."""
    kill_port(port)
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


# ---------------------------------------------------------------------------
# Task runner
# ---------------------------------------------------------------------------
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
    """Reset -> solve -> verify for a single task."""
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


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Superhuman real-task sanity check")
    parser.add_argument("--task-id", type=str, help="Run a single task by ID")
    parser.add_argument("--workers", type=int, default=1, help="Number of parallel workers")
    parser.add_argument("--port", type=int, default=9100, help="Base port for servers")
    args = parser.parse_args()

    tasks = load_tasks()
    if args.task_id:
        tasks = [t for t in tasks if t["id"] == args.task_id]
        if not tasks:
            print(f"Task '{args.task_id}' not found.")
            sys.exit(1)

    print("Generating seed state from JS data...")
    seed_state = generate_seed_state()
    print(f"  {len(seed_state['emails'])} emails, {len(seed_state['labels'])} labels")
    print(f"Running {len(tasks)} task(s)...\n")

    if args.workers <= 1:
        port = find_free_port(args.port)
        results = run_tasks_sequential(tasks, port, seed_state)
    else:
        results = run_tasks_parallel(tasks, args.workers, args.port, seed_state)

    # Sort results by original task order
    task_order = {t["id"]: i for i, t in enumerate(load_tasks())}
    results.sort(key=lambda r: task_order.get(r[0], 999))

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
