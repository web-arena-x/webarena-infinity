#!/usr/bin/env python3
"""Sanity check for real-task verifiers.

For each task, directly constructs the expected end-state (bypassing the agent),
then runs the verifier and asserts it returns True.
"""

import argparse
import copy
import importlib.util
import json
import os
import signal
import socket
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

APP_DIR = os.path.dirname(os.path.abspath(__file__))
TASKS_FILE = os.path.join(APP_DIR, "real-tasks.json")
NUM_TASKS = 100


# ─── Helpers ──────────────────────────────────────────────────────────────────

def find_entity(collection, **kwargs):
    """Find a single entity by attribute match."""
    for item in collection:
        if all(item.get(k) == v for k, v in kwargs.items()):
            return item
    key_desc = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
    raise ValueError(f"Entity not found: {key_desc}")


def find_entity_by(collection, key, predicate):
    """Find entity where predicate(entity[key]) is True."""
    for item in collection:
        if predicate(item.get(key, "")):
            return item
    raise ValueError(f"No entity matched predicate on '{key}'")


def find_issue(state, issue_id):
    return find_entity(state["issues"], id=issue_id)


def find_label(state, name):
    return find_entity(state["labels"], name=name)


def find_milestone(state, title):
    return find_entity(state["milestones"], title=title)


def find_milestone_containing(state, substring):
    return find_entity_by(state["milestones"], "title", lambda t: substring in t)


def find_iteration(state, title):
    return find_entity(state["iterations"], title=title)


def find_epic(state, title):
    return find_entity(state["epics"], title=title)


def find_epic_containing(state, substring):
    return find_entity_by(state["epics"], "title", lambda t: substring in t)


def find_board(state, name):
    return find_entity(state["boards"], name=name)


def get_next_id(state, entity):
    nid = state["_nextId"][entity]
    state["_nextId"][entity] = nid + 1
    return nid


# ─── Seed State ───────────────────────────────────────────────────────────────

def generate_seed_state():
    """Extract seed state from data.js using Node."""
    js_code = r"""
    const fs = require('fs');
    const src = fs.readFileSync('%s/js/data.js', 'utf8');
    const fn = new Function(src + '; return SeedData;');
    const seed = fn();
    const state = {
        _seedVersion: seed.SEED_DATA_VERSION,
        users: JSON.parse(JSON.stringify(seed.users)),
        currentUserId: seed.currentUserId,
        labels: JSON.parse(JSON.stringify(seed.labels)),
        milestones: JSON.parse(JSON.stringify(seed.milestones)),
        iterationCadences: JSON.parse(JSON.stringify(seed.iterationCadences)),
        iterations: JSON.parse(JSON.stringify(seed.iterations)),
        epics: JSON.parse(JSON.stringify(seed.epics)),
        issueTemplates: JSON.parse(JSON.stringify(seed.issueTemplates)),
        issues: JSON.parse(JSON.stringify(seed.issues)),
        comments: JSON.parse(JSON.stringify(seed.comments)),
        activityLog: JSON.parse(JSON.stringify(seed.activityLog)),
        boards: JSON.parse(JSON.stringify(seed.boards)),
        notifications: JSON.parse(JSON.stringify(seed.notifications)),
        notificationSettings: JSON.parse(JSON.stringify(seed.notificationSettings)),
        project: JSON.parse(JSON.stringify(seed.project)),
        _nextId: JSON.parse(JSON.stringify(seed._nextId)),
    };
    process.stdout.write(JSON.stringify(state));
    """.replace('%s', APP_DIR.replace('\\', '\\\\'))

    result = subprocess.run(
        ["node", "-e", js_code],
        capture_output=True, text=True, timeout=10,
    )
    if result.returncode != 0:
        print(f"Node stderr: {result.stderr}", file=sys.stderr)
        raise RuntimeError("Failed to generate seed state from data.js")
    return json.loads(result.stdout)


# ─── Solver Functions — Easy ─────────────────────────────────────────────────

def solve_task_e1(state):
    """Close issue #33 'Memory leak in WebSocket connection handler'."""
    issue = find_issue(state, 33)
    issue["status"] = "closed"
    issue["closedAt"] = "2026-03-18T00:00:00Z"


def solve_task_e2(state):
    """Reopen issue #89 'Fix data loss on concurrent issue edits'."""
    issue = find_issue(state, 89)
    issue["status"] = "open"
    issue["closedAt"] = None


def solve_task_e3(state):
    """Set issue #14 priority to critical (swap high→critical)."""
    issue = find_issue(state, 14)
    issue["labelIds"] = [l for l in issue["labelIds"] if l != 12]
    if 11 not in issue["labelIds"]:
        issue["labelIds"].append(11)


def solve_task_e4(state):
    """Mark issue #57 as not confidential."""
    issue = find_issue(state, 57)
    issue["confidential"] = False


def solve_task_e5(state):
    """Remove Emily Okonkwo (id 8) from issue #22."""
    issue = find_issue(state, 22)
    issue["assigneeIds"] = [a for a in issue["assigneeIds"] if a != 8]


def solve_task_e6(state):
    """Set weight of issue #9 to 8."""
    issue = find_issue(state, 9)
    issue["weight"] = 8


def solve_task_e7(state):
    """Clear due date on issue #28."""
    issue = find_issue(state, 28)
    issue["dueDate"] = None


def solve_task_e8(state):
    """Add documentation label (id 3) to issue #43."""
    issue = find_issue(state, 43)
    if 3 not in issue["labelIds"]:
        issue["labelIds"].append(3)


def solve_task_e9(state):
    """Close epic 'Performance Optimization Phase 2'."""
    epic = find_epic(state, "Performance Optimization Phase 2")
    epic["status"] = "closed"


def solve_task_e10(state):
    """Reopen milestone 'v1.1 — Stability'."""
    ms = find_milestone_containing(state, "v1.1")
    ms["status"] = "active"


def solve_task_e11(state):
    """Delete the 'breaking-change' label."""
    label = find_label(state, "breaking-change")
    label_id = label["id"]
    state["labels"] = [l for l in state["labels"] if l["id"] != label_id]
    for issue in state["issues"]:
        issue["labelIds"] = [l for l in issue["labelIds"] if l != label_id]
    for epic in state["epics"]:
        epic["labels"] = [l for l in epic["labels"] if l != label_id]
    for board in state["boards"]:
        board["lists"] = [l for l in board["lists"] if l.get("labelId") != label_id]


def solve_task_e12(state):
    """Set notification level to 'watch'."""
    state["notificationSettings"]["level"] = "watch"


def solve_task_e13(state):
    """Mark all notifications as read."""
    for n in state["notifications"]:
        n["read"] = True


def solve_task_e14(state):
    """Assign Marek Kowalski (id 2) to issue #111."""
    issue = find_issue(state, 111)
    if 2 not in issue["assigneeIds"]:
        issue["assigneeIds"].append(2)


def solve_task_e15(state):
    """Remove bug label (id 1) from issue #104."""
    issue = find_issue(state, 104)
    issue["labelIds"] = [l for l in issue["labelIds"] if l != 1]


def solve_task_e16(state):
    """Move issue #55 to v2.1 Integrations milestone (id 4)."""
    issue = find_issue(state, 55)
    issue["milestoneId"] = 4


def solve_task_e17(state):
    """Set time estimate for issue #23 to 40h (144000s)."""
    issue = find_issue(state, 23)
    issue["timeEstimate"] = 144000


def solve_task_e18(state):
    """Close epic 'Accessibility Compliance (WCAG 2.1 AA)'."""
    epic = find_epic_containing(state, "Accessibility Compliance")
    epic["status"] = "closed"


def solve_task_e19(state):
    """Remove the Review list (labelId 17) from Development Board."""
    board = find_board(state, "Development Board")
    board["lists"] = [l for l in board["lists"] if l.get("labelId") != 17]
    for i, lst in enumerate(board["lists"]):
        lst["position"] = i


def solve_task_e20(state):
    """Set due date of issue #20 to 2026-05-15."""
    issue = find_issue(state, 20)
    issue["dueDate"] = "2026-05-15"


# ─── Solver Functions — Medium ───────────────────────────────────────────────

def solve_task_m1(state):
    """Create issue 'Implement GraphQL subscriptions for real-time updates'."""
    nid = get_next_id(state, "issues")
    state["issues"].append({
        "id": nid,
        "title": "Implement GraphQL subscriptions for real-time updates",
        "description": "",
        "type": "issue",
        "status": "open",
        "authorId": state["currentUserId"],
        "assigneeIds": [7],  # Li Wei
        "labelIds": [7, 2],  # backend, feature
        "milestoneId": 4,    # v2.1 — Integrations
        "iterationId": None,
        "weight": 8,
        "dueDate": None,
        "confidential": False,
        "timeEstimate": 0,
        "timeSpent": 0,
        "createdAt": "2026-03-18T00:00:00Z",
        "updatedAt": "2026-03-18T00:00:00Z",
        "closedAt": None,
        "relatedIssues": [],
    })


def solve_task_m2(state):
    """Move issue #29 from Backlog to v2.0, set priority to high."""
    issue = find_issue(state, 29)
    issue["milestoneId"] = 3  # v2.0 — API Overhaul
    issue["labelIds"] = [l for l in issue["labelIds"] if l != 13]  # remove medium
    if 12 not in issue["labelIds"]:
        issue["labelIds"].append(12)  # add high


def solve_task_m3(state):
    """Create milestone 'v2.2 — Performance'."""
    nid = get_next_id(state, "milestones")
    state["milestones"].append({
        "id": nid,
        "title": "v2.2 \u2014 Performance",
        "description": "Performance improvements and optimizations",
        "startDate": "2026-07-01",
        "dueDate": "2026-08-31",
        "status": "active",
    })


def solve_task_m4(state):
    """Create epic 'Dark Mode Support'."""
    nid = get_next_id(state, "epics")
    state["epics"].append({
        "id": nid,
        "title": "Dark Mode Support",
        "description": "Implement dark mode across all application pages",
        "status": "open",
        "startDate": None,
        "dueDate": None,
        "labels": [8, 6],  # frontend, UX
        "authorId": state["currentUserId"],
        "confidential": False,
        "childIssueIds": [],
        "childEpicIds": [],
        "createdAt": "2026-03-18T00:00:00Z",
        "updatedAt": "2026-03-18T00:00:00Z",
    })


def solve_task_m5(state):
    """Add issues #94 and #115 to Notification System Revamp epic."""
    epic = find_epic(state, "Notification System Revamp")
    for iid in [94, 115]:
        if iid not in epic["childIssueIds"]:
            epic["childIssueIds"].append(iid)


def solve_task_m6(state):
    """Create label 'regression' (#c0392b) and add to issue #35."""
    nid = get_next_id(state, "labels")
    state["labels"].append({
        "id": nid,
        "name": "regression",
        "description": "",
        "color": "#c0392b",
        "textColor": "#fff",
        "scoped": False,
    })
    issue = find_issue(state, 35)
    if nid not in issue["labelIds"]:
        issue["labelIds"].append(nid)


def solve_task_m7(state):
    """Assign David Kim (11) to issue #60, set iteration to Sprint 7 (id 7)."""
    issue = find_issue(state, 60)
    if 11 not in issue["assigneeIds"]:
        issue["assigneeIds"].append(11)
    issue["iterationId"] = 7


def solve_task_m8(state):
    """Create iteration 'Design Cycle 6' in Design Cycles cadence."""
    nid = get_next_id(state, "iterations")
    state["iterations"].append({
        "id": nid,
        "cadenceId": 2,  # Design Cycles
        "title": "Design Cycle 6",
        "startDate": "2026-06-15",
        "endDate": "2026-07-05",
        "status": "upcoming",
    })


def solve_task_m9(state):
    """Add blocks relationship from #14 to #49."""
    issue14 = find_issue(state, 14)
    issue49 = find_issue(state, 49)
    if not any(r["issueId"] == 49 for r in issue14["relatedIssues"]):
        issue14["relatedIssues"].append({"issueId": 49, "type": "blocks"})
    if not any(r["issueId"] == 14 for r in issue49["relatedIssues"]):
        issue49["relatedIssues"].append({"issueId": 14, "type": "is_blocked_by"})


def solve_task_m10(state):
    """Remove In Progress list (labelId 16), add performance list (labelId 4)."""
    board = find_board(state, "Development Board")
    board["lists"] = [l for l in board["lists"] if l.get("labelId") != 16]
    nid = get_next_id(state, "boardLists")
    closed_idx = next((i for i, l in enumerate(board["lists"]) if l["type"] == "closed"), len(board["lists"]))
    board["lists"].insert(closed_idx, {
        "id": nid,
        "type": "label",
        "title": "performance",
        "position": closed_idx,
        "labelId": 4,
    })
    for i, lst in enumerate(board["lists"]):
        lst["position"] = i


def solve_task_m11(state):
    """Close issues #57, #58, #59."""
    for issue_id in [57, 58, 59]:
        issue = find_issue(state, issue_id)
        issue["status"] = "closed"
        issue["closedAt"] = "2026-03-18T00:00:00Z"


def solve_task_m12(state):
    """Update security label color and description."""
    label = find_label(state, "security")
    label["color"] = "#8e44ad"
    label["textColor"] = "#fff"
    label["description"] = "Security vulnerabilities and hardening"


def solve_task_m13(state):
    """Add David Kim (11) to issue #42, change priority to high."""
    issue = find_issue(state, 42)
    if 11 not in issue["assigneeIds"]:
        issue["assigneeIds"].append(11)
    issue["labelIds"] = [l for l in issue["labelIds"] if l != 13]  # remove medium
    if 12 not in issue["labelIds"]:
        issue["labelIds"].append(12)  # add high


def solve_task_m14(state):
    """Set issue #2 time estimate to 60h, time spent to 10h."""
    issue = find_issue(state, 2)
    issue["timeEstimate"] = 216000  # 60h
    issue["timeSpent"] = 36000     # 10h


def solve_task_m15(state):
    """Move issue #34 to v2.1, assign Priya Sharma (5)."""
    issue = find_issue(state, 34)
    issue["milestoneId"] = 4
    if 5 not in issue["assigneeIds"]:
        issue["assigneeIds"].append(5)


def solve_task_m16(state):
    """Create confidential epic 'Security Vulnerability Assessment'."""
    nid = get_next_id(state, "epics")
    state["epics"].append({
        "id": nid,
        "title": "Security Vulnerability Assessment",
        "description": "",
        "status": "open",
        "startDate": None,
        "dueDate": None,
        "labels": [5, 11],  # security, priority::critical
        "authorId": state["currentUserId"],
        "confidential": True,
        "childIssueIds": [],
        "childEpicIds": [],
        "createdAt": "2026-03-18T00:00:00Z",
        "updatedAt": "2026-03-18T00:00:00Z",
    })


def solve_task_m17(state):
    """Add issue #74 to CI/CD epic, change milestone to v2.1."""
    epic = find_epic_containing(state, "CI/CD Pipeline")
    if 74 not in epic["childIssueIds"]:
        epic["childIssueIds"].append(74)
    issue = find_issue(state, 74)
    issue["milestoneId"] = 4


def solve_task_m18(state):
    """Update Backlog milestone description and start date."""
    ms = find_milestone(state, "Backlog")
    ms["description"] = "Items not yet scheduled for a release"
    ms["startDate"] = "2026-01-01"


def solve_task_m19(state):
    """Swap #48 out of API v3 Migration epic, add #121."""
    epic = find_epic_containing(state, "API v3 Migration")
    epic["childIssueIds"] = [i for i in epic["childIssueIds"] if i != 48]
    if 121 not in epic["childIssueIds"]:
        epic["childIssueIds"].append(121)


def solve_task_m20(state):
    """Close issue #78, add related_to link between #78 and #31."""
    issue78 = find_issue(state, 78)
    issue78["status"] = "closed"
    issue78["closedAt"] = "2026-03-18T00:00:00Z"
    issue31 = find_issue(state, 31)
    if not any(r["issueId"] == 31 for r in issue78["relatedIssues"]):
        issue78["relatedIssues"].append({"issueId": 31, "type": "related_to"})
    if not any(r["issueId"] == 78 for r in issue31["relatedIssues"]):
        issue31["relatedIssues"].append({"issueId": 78, "type": "related_to"})


# ─── Solver Functions — Hard ─────────────────────────────────────────────────

def solve_task_h1(state):
    """Create task 'API v3 rate limiting documentation' matching issue #9's assignee/milestone."""
    # Issue #9: assigneeIds [7], milestoneId 3
    nid = get_next_id(state, "issues")
    state["issues"].append({
        "id": nid,
        "title": "API v3 rate limiting documentation",
        "description": "",
        "type": "task",
        "status": "open",
        "authorId": state["currentUserId"],
        "assigneeIds": [7],  # Li Wei (same as #9)
        "labelIds": [3],     # documentation
        "milestoneId": 3,    # v2.0 (same as #9)
        "iterationId": None,
        "weight": None,
        "dueDate": None,
        "confidential": False,
        "timeEstimate": 0,
        "timeSpent": 0,
        "createdAt": "2026-03-18T00:00:00Z",
        "updatedAt": "2026-03-18T00:00:00Z",
        "closedAt": None,
        "relatedIssues": [],
    })


def solve_task_h2(state):
    """Close all open low-priority issues in v2.0 (#10, #48)."""
    for issue_id in [10, 48]:
        issue = find_issue(state, issue_id)
        issue["status"] = "closed"
        issue["closedAt"] = "2026-03-18T00:00:00Z"


def solve_task_h3(state):
    """Assign David Kim (11) to #60, #61, #62 and set iteration to Sprint 7."""
    for issue_id in [60, 61, 62]:
        issue = find_issue(state, issue_id)
        if 11 not in issue["assigneeIds"]:
            issue["assigneeIds"].append(11)
        issue["iterationId"] = 7


def solve_task_h4(state):
    """Reassign Tom's v2.1 issues to Ana Garcia."""
    for issue_id in [19, 20, 21, 42, 50, 53]:
        issue = find_issue(state, issue_id)
        issue["assigneeIds"] = [a for a in issue["assigneeIds"] if a != 6]
        if 3 not in issue["assigneeIds"]:
            issue["assigneeIds"].append(3)


def solve_task_h5(state):
    """Create 'Critical Fixes' milestone and move critical issues to it."""
    nid = get_next_id(state, "milestones")
    state["milestones"].append({
        "id": nid,
        "title": "Critical Fixes",
        "description": "",
        "startDate": None,
        "dueDate": "2026-04-01",
        "status": "active",
    })
    for issue_id in [11, 33, 41]:
        issue = find_issue(state, issue_id)
        issue["milestoneId"] = nid


def solve_task_h6(state):
    """Replace all label-based board lists with bug/feature/performance."""
    board = find_board(state, "Development Board")
    # Remove all label-based lists
    board["lists"] = [l for l in board["lists"] if l["type"] != "label"]
    # Add new label lists before the closed list
    closed_idx = next((i for i, l in enumerate(board["lists"]) if l["type"] == "closed"), len(board["lists"]))
    new_labels = [
        (1, "bug"),
        (2, "feature"),
        (4, "performance"),
    ]
    for offset, (label_id, title) in enumerate(new_labels):
        nid = get_next_id(state, "boardLists")
        board["lists"].insert(closed_idx + offset, {
            "id": nid,
            "type": "label",
            "title": title,
            "position": closed_idx + offset,
            "labelId": label_id,
        })
    for i, lst in enumerate(board["lists"]):
        lst["position"] = i


def solve_task_h7(state):
    """Close CI/CD Pipeline Modernization epic and all child issues."""
    for issue_id in [19, 20, 21, 53, 54]:
        issue = find_issue(state, issue_id)
        issue["status"] = "closed"
        issue["closedAt"] = "2026-03-18T00:00:00Z"
    epic = find_epic_containing(state, "CI/CD Pipeline Modernization")
    epic["status"] = "closed"


def solve_task_h8(state):
    """Move #47 from API v3 Migration to Perf Opt epic, change milestone and priority."""
    epic2 = find_epic_containing(state, "API v3 Migration")
    epic2["childIssueIds"] = [i for i in epic2["childIssueIds"] if i != 47]
    epic3 = find_epic(state, "Performance Optimization Phase 2")
    if 47 not in epic3["childIssueIds"]:
        epic3["childIssueIds"].append(47)
    issue = find_issue(state, 47)
    issue["milestoneId"] = 4  # v2.1
    issue["labelIds"] = [l for l in issue["labelIds"] if l != 13]  # remove medium
    if 12 not in issue["labelIds"]:
        issue["labelIds"].append(12)  # add high


def solve_task_h9(state):
    """Set Sprint 7 for Emily's open bugs without iteration (#37,#67,#72,#110,#120)."""
    for issue_id in [37, 67, 72, 110, 120]:
        issue = find_issue(state, issue_id)
        issue["iterationId"] = 7


def solve_task_h10(state):
    """Close Priya's performance issues (#11, #12, #14, #49)."""
    for issue_id in [11, 12, 14, 49]:
        issue = find_issue(state, issue_id)
        issue["status"] = "closed"
        issue["closedAt"] = "2026-03-18T00:00:00Z"


def solve_task_h11(state):
    """Create issue 'Update Redis client library to v5' matching #12's assignees/weight/milestone."""
    # Issue #12: assigneeIds [5,11], weight 13, milestoneId 3
    nid = get_next_id(state, "issues")
    state["issues"].append({
        "id": nid,
        "title": "Update Redis client library to v5",
        "description": "",
        "type": "issue",
        "status": "open",
        "authorId": state["currentUserId"],
        "assigneeIds": [5, 11],  # same as #12
        "labelIds": [7, 10, 13],  # backend, tech-debt, priority::medium
        "milestoneId": 3,         # same as #12
        "iterationId": None,
        "weight": 13,             # same as #12
        "dueDate": None,
        "confidential": False,
        "timeEstimate": 0,
        "timeSpent": 0,
        "createdAt": "2026-03-18T00:00:00Z",
        "updatedAt": "2026-03-18T00:00:00Z",
        "closedAt": None,
        "relatedIssues": [],
    })


def solve_task_h12(state):
    """Create 'blocked' label and add to migration issues #7, #8, #47."""
    nid = get_next_id(state, "labels")
    state["labels"].append({
        "id": nid,
        "name": "blocked",
        "description": "",
        "color": "#e74c3c",
        "textColor": "#fff",
        "scoped": False,
    })
    for issue_id in [7, 8, 47]:
        issue = find_issue(state, issue_id)
        if nid not in issue["labelIds"]:
            issue["labelIds"].append(nid)


def solve_task_h13(state):
    """Add blocks from #20 to #21, set both to high priority."""
    issue20 = find_issue(state, 20)
    issue21 = find_issue(state, 21)
    # Add relationship
    if not any(r["issueId"] == 21 for r in issue20["relatedIssues"]):
        issue20["relatedIssues"].append({"issueId": 21, "type": "blocks"})
    if not any(r["issueId"] == 20 for r in issue21["relatedIssues"]):
        issue21["relatedIssues"].append({"issueId": 20, "type": "is_blocked_by"})
    # Set #20 priority to high (swap medium→high)
    issue20["labelIds"] = [l for l in issue20["labelIds"] if l != 13]
    if 12 not in issue20["labelIds"]:
        issue20["labelIds"].append(12)
    # #21 already has priority::high (12)


def solve_task_h14(state):
    """Create epic 'Platform Stability' and add critical issues as children."""
    nid = get_next_id(state, "epics")
    state["epics"].append({
        "id": nid,
        "title": "Platform Stability",
        "description": "",
        "status": "open",
        "startDate": None,
        "dueDate": None,
        "labels": [4, 12],  # performance, priority::high
        "authorId": state["currentUserId"],
        "confidential": False,
        "childIssueIds": [11, 33, 41],
        "childEpicIds": [],
        "createdAt": "2026-03-18T00:00:00Z",
        "updatedAt": "2026-03-18T00:00:00Z",
    })


def solve_task_h15(state):
    """Assign Marek Kowalski (2) to unassigned security issues in v3.0 (#57,#58,#59)."""
    for issue_id in [57, 58, 59]:
        issue = find_issue(state, issue_id)
        if 2 not in issue["assigneeIds"]:
            issue["assigneeIds"].append(2)


def solve_task_h16(state):
    """Move v1.1 issues to v1.0, delete v1.1 milestone."""
    ms_v11 = find_milestone_containing(state, "v1.1")
    ms_v10 = find_milestone_containing(state, "v1.0")
    v11_id = ms_v11["id"]
    v10_id = ms_v10["id"]
    for issue in state["issues"]:
        if issue["milestoneId"] == v11_id:
            issue["milestoneId"] = v10_id
    state["milestones"] = [m for m in state["milestones"] if m["id"] != v11_id]


def solve_task_h17(state):
    """Create epic 'Q2 Bug Fixes' with v2.0 bug issues as children."""
    nid = get_next_id(state, "epics")
    state["epics"].append({
        "id": nid,
        "title": "Q2 Bug Fixes",
        "description": "",
        "status": "open",
        "startDate": None,
        "dueDate": None,
        "labels": [1, 12],  # bug, priority::high
        "authorId": state["currentUserId"],
        "confidential": False,
        "childIssueIds": [28, 31, 33, 35, 41, 78, 101, 104],
        "childEpicIds": [],
        "createdAt": "2026-03-18T00:00:00Z",
        "updatedAt": "2026-03-18T00:00:00Z",
    })


def solve_task_h18(state):
    """Add 4h time spent to Li Wei's issues with no time logged (#32,#45,#125,#129)."""
    for issue_id in [32, 45, 125, 129]:
        issue = find_issue(state, issue_id)
        issue["timeSpent"] = issue["timeSpent"] + 14400


def solve_task_h19(state):
    """Set Enterprise SSO epic and children #57,#58,#59 to not confidential."""
    epic = find_epic_containing(state, "Enterprise SSO")
    epic["confidential"] = False
    for issue_id in [57, 58, 59]:
        issue = find_issue(state, issue_id)
        issue["confidential"] = False


def solve_task_h20(state):
    """Close Notification System Revamp epic, move children to Search epic."""
    epic_notif = find_epic(state, "Notification System Revamp")
    epic_notif["status"] = "closed"
    children_to_move = [63, 64, 65]
    epic_notif["childIssueIds"] = [i for i in epic_notif["childIssueIds"] if i not in children_to_move]
    epic_search = find_epic_containing(state, "Search Infrastructure Upgrade")
    for iid in children_to_move:
        if iid not in epic_search["childIssueIds"]:
            epic_search["childIssueIds"].append(iid)


# ─── Solver Functions — Hard (Hardening Round 1) ────────────────────────────

def solve_task_h21(state):
    """v2.0: no priority → high; critical → Sprint 7."""
    priority_labels = {11, 12, 13, 14}
    for issue in state["issues"]:
        if issue["status"] != "open" or issue["milestoneId"] != 3:
            continue
        has_priority = any(l in priority_labels for l in issue["labelIds"])
        if not has_priority:
            # Add priority::high
            if 12 not in issue["labelIds"]:
                issue["labelIds"].append(12)
        if 11 in issue["labelIds"]:
            # Critical → Sprint 7
            issue["iterationId"] = 7


def solve_task_h22(state):
    """Assign highest-weight member (Jun Nakamura, id 4) to Search epic unassigned children."""
    for issue_id in [60, 61, 62]:
        issue = find_issue(state, issue_id)
        if 4 not in issue["assigneeIds"]:
            issue["assigneeIds"].append(4)


def solve_task_h23(state):
    """Close open breaking-change issues in v2.0 (#7, #8, #10, #47)."""
    for issue_id in [7, 8, 10, 47]:
        issue = find_issue(state, issue_id)
        issue["status"] = "closed"
        issue["closedAt"] = "2026-03-18T00:00:00Z"


def solve_task_h24(state):
    """Move Emily's issues from Mobile Responsive to Accessibility epic, set priority high."""
    moved = [15, 16, 17, 51]
    epic4 = find_epic(state, "Mobile Responsive Redesign")
    epic4["childIssueIds"] = [i for i in epic4["childIssueIds"] if i not in moved]
    epic6 = find_epic_containing(state, "Accessibility Compliance")
    for iid in moved:
        if iid not in epic6["childIssueIds"]:
            epic6["childIssueIds"].append(iid)
    for iid in moved:
        issue = find_issue(state, iid)
        issue["labelIds"] = [l for l in issue["labelIds"] if l not in (11, 12, 13, 14)]
        if 12 not in issue["labelIds"]:
            issue["labelIds"].append(12)


def solve_task_h25(state):
    """Close Tom's devops issues in v2.1 (#19, #20, #21, #42, #50, #53)."""
    for issue_id in [19, 20, 21, 42, 50, 53]:
        issue = find_issue(state, issue_id)
        issue["status"] = "closed"
        issue["closedAt"] = "2026-03-18T00:00:00Z"


def solve_task_h26(state):
    """Add blocks from #2 (Auth SAML) to #57 (SSO SAML)."""
    issue2 = find_issue(state, 2)
    issue57 = find_issue(state, 57)
    if not any(r["issueId"] == 57 for r in issue2["relatedIssues"]):
        issue2["relatedIssues"].append({"issueId": 57, "type": "blocks"})
    if not any(r["issueId"] == 2 for r in issue57["relatedIssues"]):
        issue57["relatedIssues"].append({"issueId": 2, "type": "is_blocked_by"})


def solve_task_h27(state):
    """Remove To Do/Done lists, add bug/security lists on Development Board."""
    board = find_board(state, "Development Board")
    board["lists"] = [l for l in board["lists"] if l.get("labelId") not in (15, 18)]
    closed_idx = next((i for i, l in enumerate(board["lists"]) if l["type"] == "closed"), len(board["lists"]))
    for offset, (label_id, title) in enumerate([(1, "bug"), (5, "security")]):
        nid = get_next_id(state, "boardLists")
        board["lists"].insert(closed_idx + offset, {
            "id": nid,
            "type": "label",
            "title": title,
            "position": closed_idx + offset,
            "labelId": label_id,
        })
    for i, lst in enumerate(board["lists"]):
        lst["position"] = i


def solve_task_h28(state):
    """Add documentation label and 8h time spent to #6 (blocker of migration tasks)."""
    issue = find_issue(state, 6)
    if 3 not in issue["labelIds"]:
        issue["labelIds"].append(3)
    issue["timeSpent"] = issue["timeSpent"] + 28800


def solve_task_h29(state):
    """Create 'Frontend Bug Fixes' epic with all open bug+frontend issues as children."""
    children = [i["id"] for i in state["issues"]
                if i["status"] == "open" and 1 in i["labelIds"] and 8 in i["labelIds"]]
    nid = get_next_id(state, "epics")
    state["epics"].append({
        "id": nid,
        "title": "Frontend Bug Fixes",
        "description": "",
        "status": "open",
        "startDate": None,
        "dueDate": None,
        "labels": [1, 8],
        "authorId": state["currentUserId"],
        "confidential": False,
        "childIssueIds": children,
        "childEpicIds": [],
        "createdAt": "2026-03-18T00:00:00Z",
        "updatedAt": "2026-03-18T00:00:00Z",
    })


def solve_task_h30(state):
    """Set #23 weight to 13, add blocks from #23 to #96."""
    issue23 = find_issue(state, 23)
    issue23["weight"] = 13
    issue96 = find_issue(state, 96)
    if not any(r["issueId"] == 96 for r in issue23["relatedIssues"]):
        issue23["relatedIssues"].append({"issueId": 96, "type": "blocks"})
    if not any(r["issueId"] == 23 for r in issue96["relatedIssues"]):
        issue96["relatedIssues"].append({"issueId": 23, "type": "is_blocked_by"})


def solve_task_h31(state):
    """Remove closed children from Auth epic, add Notification epic children."""
    epic1 = find_epic(state, "User Authentication Overhaul")
    epic1["childIssueIds"] = [i for i in epic1["childIssueIds"] if i not in (4, 5)]
    for iid in [63, 64, 65]:
        if iid not in epic1["childIssueIds"]:
            epic1["childIssueIds"].append(iid)


def solve_task_h32(state):
    """Assign Ana Garcia (3) and Sprint 8 to unassigned backend v2.1 issues."""
    for issue_id in [60, 61, 63, 64, 80, 111]:
        issue = find_issue(state, issue_id)
        if 3 not in issue["assigneeIds"]:
            issue["assigneeIds"].append(3)
        issue["iterationId"] = 8


def solve_task_h33(state):
    """Set weight 13 and priority::critical for Jun+Emily co-assigned issues."""
    for issue_id in [15, 23, 30]:
        issue = find_issue(state, issue_id)
        issue["weight"] = 13
        issue["labelIds"] = [l for l in issue["labelIds"] if l not in (11, 12, 13, 14)]
        if 11 not in issue["labelIds"]:
            issue["labelIds"].append(11)


def solve_task_h34(state):
    """Create Sprint 9, move devops issues from Sprint 8."""
    nid = get_next_id(state, "iterations")
    state["iterations"].append({
        "id": nid,
        "cadenceId": 1,
        "title": "Sprint 9",
        "startDate": "2026-04-28",
        "endDate": "2026-05-11",
        "status": "upcoming",
    })
    for issue_id in [20, 21, 42, 53]:
        issue = find_issue(state, issue_id)
        issue["iterationId"] = nid


def solve_task_h35(state):
    """Create 'overdue-risk' label, apply to v2.0 issues due before 2026-03-25."""
    nid = get_next_id(state, "labels")
    state["labels"].append({
        "id": nid,
        "name": "overdue-risk",
        "description": "",
        "color": "#e74c3c",
        "textColor": "#fff",
        "scoped": False,
    })
    for issue in state["issues"]:
        if (issue["status"] == "open" and issue["milestoneId"] == 3
                and issue["dueDate"] and issue["dueDate"] < "2026-03-25"):
            if nid not in issue["labelIds"]:
                issue["labelIds"].append(nid)


def solve_task_h36(state):
    """Create 'Security Hardening' milestone, move confidential issues."""
    nid = get_next_id(state, "milestones")
    state["milestones"].append({
        "id": nid,
        "title": "Security Hardening",
        "description": "",
        "startDate": None,
        "dueDate": "2026-06-30",
        "status": "active",
    })
    for issue in state["issues"]:
        if issue["status"] == "open" and issue["confidential"]:
            issue["milestoneId"] = nid


def solve_task_h37(state):
    """Create task 'Security audit for CI pipeline' based on #53, add to CI/CD epic."""
    nid = get_next_id(state, "issues")
    state["issues"].append({
        "id": nid,
        "title": "Security audit for CI pipeline",
        "description": "",
        "type": "task",
        "status": "open",
        "authorId": state["currentUserId"],
        "assigneeIds": [6],  # Tom Ramirez (same as #53)
        "labelIds": [5, 9],  # security, devops
        "milestoneId": 4,    # v2.1 (same as #53)
        "iterationId": None,
        "weight": None,
        "dueDate": None,
        "confidential": False,
        "timeEstimate": 0,
        "timeSpent": 0,
        "createdAt": "2026-03-18T00:00:00Z",
        "updatedAt": "2026-03-18T00:00:00Z",
        "closedAt": None,
        "relatedIssues": [],
    })
    epic = find_epic_containing(state, "CI/CD Pipeline")
    if nid not in epic["childIssueIds"]:
        epic["childIssueIds"].append(nid)


def solve_task_h38(state):
    """Add blocks from #12 to #60, ensure both have priority::high."""
    issue12 = find_issue(state, 12)
    issue60 = find_issue(state, 60)
    if not any(r["issueId"] == 60 for r in issue12["relatedIssues"]):
        issue12["relatedIssues"].append({"issueId": 60, "type": "blocks"})
    if not any(r["issueId"] == 12 for r in issue60["relatedIssues"]):
        issue60["relatedIssues"].append({"issueId": 12, "type": "is_blocked_by"})
    # #12: swap medium→high
    issue12["labelIds"] = [l for l in issue12["labelIds"] if l not in (11, 13, 14)]
    if 12 not in issue12["labelIds"]:
        issue12["labelIds"].append(12)
    # #60 already has priority::high (12)


def solve_task_h39(state):
    """Set weight 13 for v2.0 open issues with weight=8 and exactly 1 assignee."""
    for issue in state["issues"]:
        if (issue["status"] == "open" and issue["milestoneId"] == 3
                and issue["weight"] == 8 and len(issue["assigneeIds"]) == 1):
            issue["weight"] = 13


def solve_task_h40(state):
    """Create confidential 'Compliance Audit' epic, add v3.0 security children, set critical."""
    nid = get_next_id(state, "epics")
    children = [46, 57, 58, 59]
    state["epics"].append({
        "id": nid,
        "title": "Compliance Audit",
        "description": "",
        "status": "open",
        "startDate": None,
        "dueDate": None,
        "labels": [5, 11],
        "authorId": state["currentUserId"],
        "confidential": True,
        "childIssueIds": children,
        "childEpicIds": [],
        "createdAt": "2026-03-18T00:00:00Z",
        "updatedAt": "2026-03-18T00:00:00Z",
    })
    for issue_id in children:
        issue = find_issue(state, issue_id)
        issue["labelIds"] = [l for l in issue["labelIds"] if l not in (12, 13, 14)]
        if 11 not in issue["labelIds"]:
            issue["labelIds"].append(11)


# ─── Solver Functions — Hard (Hardening Round 2) ────────────────────────────

def solve_task_h41(state):
    """Create milestone 'Emergency Fixes', move Sprint 6 critical issues into it."""
    nid = get_next_id(state, "milestones")
    state["milestones"].append({
        "id": nid,
        "title": "Emergency Fixes",
        "description": "",
        "startDate": None,
        "dueDate": "2026-04-15",
        "status": "active",
    })
    for issue_id in [11, 33, 41]:
        issue = find_issue(state, issue_id)
        issue["milestoneId"] = nid


def solve_task_h42(state):
    """Create 'Backlog Bug Sweep' epic with bug+frontend Backlog children, close them."""
    children = [i["id"] for i in state["issues"]
                if i["status"] == "open" and i["milestoneId"] == 6
                and 1 in i["labelIds"] and 8 in i["labelIds"]]
    nid = get_next_id(state, "epics")
    state["epics"].append({
        "id": nid,
        "title": "Backlog Bug Sweep",
        "description": "",
        "status": "open",
        "startDate": None,
        "dueDate": None,
        "labels": [1],
        "authorId": state["currentUserId"],
        "confidential": False,
        "childIssueIds": children,
        "childEpicIds": [],
        "createdAt": "2026-03-18T00:00:00Z",
        "updatedAt": "2026-03-18T00:00:00Z",
    })
    for issue_id in children:
        issue = find_issue(state, issue_id)
        issue["status"] = "closed"
        issue["closedAt"] = "2026-03-18T00:00:00Z"


def solve_task_h43(state):
    """Blocks from #77 to #102 (shared author quick-action issues), both priority::high."""
    issue77 = find_issue(state, 77)
    issue102 = find_issue(state, 102)
    if not any(r["issueId"] == 102 for r in issue77["relatedIssues"]):
        issue77["relatedIssues"].append({"issueId": 102, "type": "blocks"})
    if not any(r["issueId"] == 77 for r in issue102["relatedIssues"]):
        issue102["relatedIssues"].append({"issueId": 77, "type": "is_blocked_by"})
    # #77: priority low (14) → high (12)
    issue77["labelIds"] = [l for l in issue77["labelIds"] if l not in (11, 13, 14)]
    if 12 not in issue77["labelIds"]:
        issue77["labelIds"].append(12)
    # #102: priority medium (13) → high (12)
    issue102["labelIds"] = [l for l in issue102["labelIds"] if l not in (11, 13, 14)]
    if 12 not in issue102["labelIds"]:
        issue102["labelIds"].append(12)


def solve_task_h44(state):
    """Remove closed children from Accessibility epic; medium→high for #22, #55."""
    epic = find_epic_containing(state, "Accessibility Compliance")
    epic["childIssueIds"] = [i for i in epic["childIssueIds"] if i not in (24, 56)]
    for issue_id in [22, 55]:
        issue = find_issue(state, issue_id)
        issue["labelIds"] = [l for l in issue["labelIds"] if l != 13]
        if 12 not in issue["labelIds"]:
            issue["labelIds"].append(12)


def solve_task_h45(state):
    """Create 'needs-triage' label, add board list, apply to #41 and #35."""
    nid = get_next_id(state, "labels")
    state["labels"].append({
        "id": nid,
        "name": "needs-triage",
        "description": "",
        "color": "#9b59b6",
        "textColor": "#fff",
        "scoped": False,
    })
    board = find_board(state, "Development Board")
    closed_idx = next((i for i, l in enumerate(board["lists"]) if l["type"] == "closed"), len(board["lists"]))
    list_id = get_next_id(state, "boardLists")
    board["lists"].insert(closed_idx, {
        "id": list_id,
        "type": "label",
        "title": "needs-triage",
        "position": closed_idx,
        "labelId": nid,
    })
    for i, lst in enumerate(board["lists"]):
        lst["position"] = i
    for issue_id in [41, 35]:
        issue = find_issue(state, issue_id)
        if nid not in issue["labelIds"]:
            issue["labelIds"].append(nid)


def solve_task_h46(state):
    """Create 'Document session management best practices' issue referencing #4."""
    nid = get_next_id(state, "issues")
    state["issues"].append({
        "id": nid,
        "title": "Document session management best practices",
        "description": "",
        "type": "issue",
        "status": "open",
        "authorId": state["currentUserId"],
        "assigneeIds": [4],       # Jun Nakamura (same as #4)
        "labelIds": [3],          # documentation
        "milestoneId": 3,         # v2.0 (same as #4)
        "iterationId": None,
        "weight": None,
        "dueDate": None,
        "confidential": False,
        "timeEstimate": 0,
        "timeSpent": 0,
        "createdAt": "2026-03-18T00:00:00Z",
        "updatedAt": "2026-03-18T00:00:00Z",
        "closedAt": None,
        "relatedIssues": [{"issueId": 4, "type": "related_to"}],
    })
    issue4 = find_issue(state, 4)
    if not any(r["issueId"] == nid for r in issue4["relatedIssues"]):
        issue4["relatedIssues"].append({"issueId": nid, "type": "related_to"})


def solve_task_h47(state):
    """Close Priya's performance issues with weight>=8 (#11,#12,#49), log 8h each."""
    for issue_id in [11, 12, 49]:
        issue = find_issue(state, issue_id)
        issue["status"] = "closed"
        issue["closedAt"] = "2026-03-18T00:00:00Z"
        issue["timeSpent"] = issue["timeSpent"] + 28800


def solve_task_h48(state):
    """Find blocker of #2 (#1), log 20h, change priority high→critical."""
    issue1 = find_issue(state, 1)
    issue1["timeSpent"] = issue1["timeSpent"] + 72000
    issue1["labelIds"] = [l for l in issue1["labelIds"] if l != 12]
    if 11 not in issue1["labelIds"]:
        issue1["labelIds"].append(11)


def solve_task_h49(state):
    """Update Backlog description, close issues with weight ≤ 1."""
    backlog = find_milestone(state, "Backlog")
    backlog["description"] = "Deferred work \u2014 not scheduled for active development"
    for issue_id in [72, 120, 127, 129]:
        issue = find_issue(state, issue_id)
        issue["status"] = "closed"
        issue["closedAt"] = "2026-03-18T00:00:00Z"


def solve_task_h50(state):
    """Create 'release-blocker' label + 'v2.0.1 — Hotfix' milestone, apply to #33/#41."""
    label_id = get_next_id(state, "labels")
    state["labels"].append({
        "id": label_id,
        "name": "release-blocker",
        "description": "",
        "color": "#cc0000",
        "textColor": "#fff",
        "scoped": False,
    })
    ms_id = get_next_id(state, "milestones")
    state["milestones"].append({
        "id": ms_id,
        "title": "v2.0.1 \u2014 Hotfix",
        "description": "",
        "startDate": None,
        "dueDate": "2026-04-10",
        "status": "active",
    })
    for issue_id in [33, 41]:
        issue = find_issue(state, issue_id)
        if label_id not in issue["labelIds"]:
            issue["labelIds"].append(label_id)
        issue["milestoneId"] = ms_id


def solve_task_h51(state):
    """Emily's bugs without iteration → Design Cycle 5, priority medium."""
    for issue_id in [37, 67, 72, 110, 120]:
        issue = find_issue(state, issue_id)
        issue["iterationId"] = 13  # Design Cycle 5
        issue["labelIds"] = [l for l in issue["labelIds"] if l not in (11, 12, 14)]
        if 13 not in issue["labelIds"]:
            issue["labelIds"].append(13)


def solve_task_h52(state):
    """Move CI/CD high-priority children (#19,#21,#53) to Search epic, Sprint 7."""
    moved = [19, 21, 53]
    cicd = find_epic_containing(state, "CI/CD Pipeline")
    cicd["childIssueIds"] = [i for i in cicd["childIssueIds"] if i not in moved]
    search = find_epic_containing(state, "Search Infrastructure")
    for iid in moved:
        if iid not in search["childIssueIds"]:
            search["childIssueIds"].append(iid)
    for iid in moved:
        issue = find_issue(state, iid)
        issue["iterationId"] = 7


def solve_task_h53(state):
    """Close Backlog milestone, move feature+backend issues to v2.1."""
    backlog = find_milestone(state, "Backlog")
    backlog["status"] = "closed"
    for issue_id in [68, 105, 112]:
        issue = find_issue(state, issue_id)
        issue["milestoneId"] = 4


def solve_task_h54(state):
    """Set weight 13 for v2.0 critical issues (#11,#33,#41) — discovered via #12's relation."""
    for issue_id in [11, 33, 41]:
        issue = find_issue(state, issue_id)
        issue["weight"] = 13


def solve_task_h55(state):
    """Log 8h time spent on Tom's v2.1 issues."""
    for issue_id in [19, 20, 21, 42, 50, 53]:
        issue = find_issue(state, issue_id)
        issue["timeSpent"] = issue["timeSpent"] + 28800


def solve_task_h56(state):
    """Swap tech-debt→performance on devops+tech-debt issues (#42,#54), weight=8."""
    for issue_id in [42, 54]:
        issue = find_issue(state, issue_id)
        issue["labelIds"] = [l for l in issue["labelIds"] if l != 10]
        if 4 not in issue["labelIds"]:
            issue["labelIds"].append(4)
        issue["weight"] = 8


def solve_task_h57(state):
    """#46: non-confidential, milestone→v2.0, assign David Kim, blocks #2."""
    issue46 = find_issue(state, 46)
    issue46["confidential"] = False
    issue46["milestoneId"] = 3
    if 11 not in issue46["assigneeIds"]:
        issue46["assigneeIds"].append(11)
    if not any(r["issueId"] == 2 for r in issue46["relatedIssues"]):
        issue46["relatedIssues"].append({"issueId": 2, "type": "blocks"})
    issue2 = find_issue(state, 2)
    if not any(r["issueId"] == 46 for r in issue2["relatedIssues"]):
        issue2["relatedIssues"].append({"issueId": 46, "type": "is_blocked_by"})


def solve_task_h58(state):
    """Close API v3 Migration epic + children, remove breaking-change labels."""
    epic = find_epic(state, "API v3 Migration")
    epic["status"] = "closed"
    for issue_id in [7, 8, 9, 10, 47, 48]:
        issue = find_issue(state, issue_id)
        issue["status"] = "closed"
        issue["closedAt"] = "2026-03-18T00:00:00Z"
        issue["labelIds"] = [l for l in issue["labelIds"] if l != 20]


def solve_task_h59(state):
    """Relationship chain #22→#55→#23, all priority::high."""
    issue22 = find_issue(state, 22)
    issue55 = find_issue(state, 55)
    issue23 = find_issue(state, 23)
    # #22 blocks #55
    if not any(r["issueId"] == 55 for r in issue22["relatedIssues"]):
        issue22["relatedIssues"].append({"issueId": 55, "type": "blocks"})
    if not any(r["issueId"] == 22 for r in issue55["relatedIssues"]):
        issue55["relatedIssues"].append({"issueId": 22, "type": "is_blocked_by"})
    # #55 blocks #23
    if not any(r["issueId"] == 23 for r in issue55["relatedIssues"]):
        issue55["relatedIssues"].append({"issueId": 23, "type": "blocks"})
    if not any(r["issueId"] == 55 for r in issue23["relatedIssues"]):
        issue23["relatedIssues"].append({"issueId": 55, "type": "is_blocked_by"})
    # All three → priority::high (12)
    for issue in [issue22, issue55, issue23]:
        issue["labelIds"] = [l for l in issue["labelIds"] if l not in (11, 13, 14)]
        if 12 not in issue["labelIds"]:
            issue["labelIds"].append(12)


def solve_task_h60(state):
    """Remove #48 from API v3 epic, create 'API Documentation' epic with #43 and #48."""
    api_epic = find_epic(state, "API v3 Migration")
    api_epic["childIssueIds"] = [i for i in api_epic["childIssueIds"] if i != 48]
    nid = get_next_id(state, "epics")
    state["epics"].append({
        "id": nid,
        "title": "API Documentation",
        "description": "",
        "status": "open",
        "startDate": None,
        "dueDate": None,
        "labels": [3],  # documentation
        "authorId": state["currentUserId"],
        "confidential": False,
        "childIssueIds": [43, 48],
        "childEpicIds": [],
        "createdAt": "2026-03-18T00:00:00Z",
        "updatedAt": "2026-03-18T00:00:00Z",
    })


# ─── Solver Registry ──────────────────────────────────────────────────────────

SOLVERS = {}
for _difficulty, _prefix, _count in [("easy", "e", 20), ("medium", "m", 20), ("hard", "h", 60)]:
    for _i in range(1, _count + 1):
        _task_id = f"task_{_prefix}{_i}"
        _fn_name = f"solve_task_{_prefix}{_i}"
        SOLVERS[_task_id] = globals()[_fn_name]


# ─── Server Management ───────────────────────────────────────────────────────

def find_free_port(start=9200):
    for port in range(start, start + 200):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("", port))
                return port
            except OSError:
                continue
    raise RuntimeError(f"No free port found starting from {start}")


def kill_port(port):
    """Kill any process on the given port."""
    try:
        result = subprocess.run(
            ["lsof", "-ti", f":{port}"], capture_output=True, text=True
        )
        if result.stdout.strip():
            for pid in result.stdout.strip().split("\n"):
                try:
                    os.kill(int(pid), signal.SIGKILL)
                except (ProcessLookupError, ValueError):
                    pass
            time.sleep(0.3)
    except FileNotFoundError:
        pass


def start_server(port, seed_state):
    """Start the app server and PUT seed state."""
    import requests

    kill_port(port)
    proc = subprocess.Popen(
        [sys.executable, "server.py", "--port", str(port)],
        cwd=APP_DIR,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    # Wait for server
    url = f"http://localhost:{port}"
    for _ in range(30):
        try:
            requests.get(f"{url}/index.html", timeout=1)
            break
        except Exception:
            time.sleep(0.2)
    else:
        proc.kill()
        raise RuntimeError(f"Server on port {port} did not start")

    # PUT seed state
    resp = requests.put(
        f"{url}/api/state",
        json=seed_state,
        headers={"Content-Type": "application/json"},
        timeout=5,
    )
    if resp.status_code != 200:
        proc.kill()
        raise RuntimeError(f"Failed to PUT seed state: {resp.status_code}")

    return proc, url


def stop_server(proc):
    if proc:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()


# ─── Task Execution ──────────────────────────────────────────────────────────

def load_verifier(verify_path):
    """Dynamically load a verifier module."""
    full_path = os.path.join(APP_DIR, verify_path)
    spec = importlib.util.spec_from_file_location("verifier", full_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.verify


def run_single_task(task, port, seed_state):
    """Reset → solve → verify for a single task."""
    import requests

    task_id = task["id"]
    solver = SOLVERS.get(task_id)
    if not solver:
        return task_id, False, f"No solver for {task_id}"

    url = f"http://localhost:{port}"

    # Reset
    resp = requests.post(f"{url}/api/reset", timeout=5)
    if resp.status_code != 200:
        return task_id, False, f"Reset failed: {resp.status_code}"

    # Re-PUT seed state (reset clears it)
    resp = requests.put(
        f"{url}/api/state",
        json=seed_state,
        headers={"Content-Type": "application/json"},
        timeout=5,
    )

    # Read current state, apply solver
    resp = requests.get(f"{url}/api/state", timeout=5)
    state = resp.json()
    try:
        solver(state)
    except Exception as e:
        return task_id, False, f"Solver error: {e}"

    # Write solved state
    resp = requests.put(
        f"{url}/api/state",
        json=state,
        headers={"Content-Type": "application/json"},
        timeout=5,
    )

    # Run verifier
    try:
        verifier = load_verifier(task["verify"])
        passed, msg = verifier(url)
        return task_id, passed, msg
    except Exception as e:
        return task_id, False, f"Verifier error: {e}"


def run_tasks_sequential(tasks, port, seed_state):
    """Run tasks sequentially on a single server."""
    proc, url = start_server(port, seed_state)
    results = []
    try:
        for task in tasks:
            result = run_single_task(task, port, seed_state)
            results.append(result)
    finally:
        stop_server(proc)
    return results


def run_tasks_parallel(tasks, workers, base_port, seed_state):
    """Run tasks in parallel across multiple servers."""
    results = []

    def worker_fn(worker_tasks, port):
        proc, url = start_server(port, seed_state)
        worker_results = []
        try:
            for task in worker_tasks:
                result = run_single_task(task, port, seed_state)
                worker_results.append(result)
        finally:
            stop_server(proc)
        return worker_results

    # Partition tasks across workers
    partitions = [[] for _ in range(workers)]
    for i, task in enumerate(tasks):
        partitions[i % workers].append(task)

    ports = [find_free_port(base_port + i * 10) for i in range(workers)]

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(worker_fn, partitions[i], ports[i]): i
            for i in range(workers)
            if partitions[i]
        }
        for future in as_completed(futures):
            results.extend(future.result())

    return results


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Real task sanity check")
    parser.add_argument("--task-id", help="Run a single task")
    parser.add_argument("--workers", type=int, default=1, help="Parallel workers")
    parser.add_argument("--port", type=int, default=9200, help="Base port")
    args = parser.parse_args()

    # Load tasks
    with open(TASKS_FILE) as f:
        all_tasks = json.load(f)

    if args.task_id:
        tasks = [t for t in all_tasks if t["id"] == args.task_id]
        if not tasks:
            print(f"Task '{args.task_id}' not found.")
            sys.exit(1)
    else:
        tasks = all_tasks

    # Generate seed state
    print("Generating seed state from data.js...")
    seed_state = generate_seed_state()
    print(f"Seed state loaded: {len(seed_state['issues'])} issues, {len(seed_state['labels'])} labels")

    # Run
    if args.workers > 1 and len(tasks) > 1:
        results = run_tasks_parallel(tasks, args.workers, args.port, seed_state)
    else:
        port = find_free_port(args.port)
        results = run_tasks_sequential(tasks, port, seed_state)

    # Sort by task id for display
    def sort_key(r):
        tid = r[0]  # e.g., "task_e1", "task_m10", "task_h20"
        prefix = tid.split("_")[1][0]  # 'e', 'm', 'h'
        num = int(tid.split("_")[1][1:])
        order = {"e": 0, "m": 1, "h": 2}
        return (order.get(prefix, 3), num)

    results.sort(key=sort_key)

    # Print results
    passed = 0
    failed = []
    for task_id, success, msg in results:
        icon = "\033[32m  PASS\033[0m" if success else "\033[31m  FAIL\033[0m"
        print(f"{icon}  {task_id:12s} {msg}")
        if success:
            passed += 1
        else:
            failed.append(task_id)

    print(f"\n{passed}/{len(results)} passed")
    if failed:
        print(f"Failed: {', '.join(failed)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
