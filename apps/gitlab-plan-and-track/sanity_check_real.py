#!/usr/bin/env python3
"""
Sanity check for GitLab Plan & Track real-task verifiers.

For each task, directly applies the expected end-state (bypassing the agent),
then runs the verifier and asserts it passes.

Usage:
    python3 sanity_check_real.py                     # All tasks, sequential
    python3 sanity_check_real.py --workers N          # N parallel environments
    python3 sanity_check_real.py --task-id task_e1    # Single task
    python3 sanity_check_real.py --port 9500          # Custom base port
"""
import argparse
import importlib.util
import json
import os
import socket
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from copy import deepcopy
from pathlib import Path

import requests

APP_DIR = Path(__file__).resolve().parent
TASKS_FILE = APP_DIR / "tasks.json"

# JS snippet to evaluate data.js and emit the seed state as JSON
_SEED_STATE_JS = """
const fs = require('fs');
const vm = require('vm');
const code = fs.readFileSync(process.argv[1], 'utf8');
vm.runInThisContext(code);

// Replicate what AppState._loadSeedData() does
const state = {
    users: JSON.parse(JSON.stringify(USERS)),
    issues: JSON.parse(JSON.stringify(ISSUES)),
    labels: JSON.parse(JSON.stringify(LABELS)),
    milestones: JSON.parse(JSON.stringify(MILESTONES)),
    iterations: JSON.parse(JSON.stringify(ITERATIONS)),
    iterationCadences: JSON.parse(JSON.stringify(ITERATION_CADENCES)),
    epics: JSON.parse(JSON.stringify(EPICS)),
    boards: JSON.parse(JSON.stringify(BOARDS)),
    todos: JSON.parse(JSON.stringify(TODOS)),
    timelogs: JSON.parse(JSON.stringify(TIMELOGS)),
    currentUser: JSON.parse(JSON.stringify(CURRENT_USER)),
    _seedVersion: SEED_DATA_VERSION,
    _nextIssueIid: Math.max(...ISSUES.map(i => i.iid)) + 1,
    _nextEpicIid: Math.max(...EPICS.map(e => e.iid)) + 1,
    _nextLabelId: 50,
    _nextMilestoneId: 20,
    _nextIterationId: 20,
    _nextCadenceId: 10,
    _nextBoardId: 10,
    _nextTodoId: 20,
    _nextTimelogId: 30,
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


def find_issue_by_title(state, title):
    """Find an issue by exact title."""
    for i in state["issues"]:
        if i["title"] == title:
            return i
    raise ValueError(f"Issue not found: {title!r}")


def find_label_by_title(state, title):
    """Find a label by exact title."""
    for l in state["labels"]:
        if l["title"] == title:
            return l
    raise ValueError(f"Label not found: {title!r}")


def find_milestone_by_title(state, title):
    """Find a milestone by exact title."""
    for m in state["milestones"]:
        if m["title"] == title:
            return m
    raise ValueError(f"Milestone not found: {title!r}")


def find_epic_by_title(state, title):
    """Find an epic by exact title."""
    for e in state["epics"]:
        if e["title"] == title:
            return e
    raise ValueError(f"Epic not found: {title!r}")


def find_cadence_by_title(state, title):
    """Find a cadence by exact title."""
    for c in state["iterationCadences"]:
        if c["title"] == title:
            return c
    raise ValueError(f"Cadence not found: {title!r}")


def find_iteration_by_title(state, title):
    """Find an iteration by exact title."""
    for i in state["iterations"]:
        if i["title"] == title:
            return i
    raise ValueError(f"Iteration not found: {title!r}")


def find_user_by_name(state, name):
    """Find a user by name."""
    for u in state["users"]:
        if u["name"] == name:
            return u
    raise ValueError(f"User not found: {name!r}")


def find_board_by_name(state, name):
    """Find a board by name."""
    for b in state["boards"]:
        if b["name"] == name:
            return b
    raise ValueError(f"Board not found: {name!r}")


def find_todo_for_issue(state, issue_id, action):
    """Find a todo by target issue and action."""
    for t in state["todos"]:
        if t["targetId"] == issue_id and t["action"] == action:
            return t
    raise ValueError(f"Todo not found: targetId={issue_id!r}, action={action!r}")


def next_issue_id(state):
    iid = state.get("_nextIssueIid", 100)
    state["_nextIssueIid"] = iid + 1
    return iid


def next_epic_iid(state):
    iid = state.get("_nextEpicIid", 20)
    state["_nextEpicIid"] = iid + 1
    return iid


def next_label_id(state):
    lid = state.get("_nextLabelId", 50)
    state["_nextLabelId"] = lid + 1
    return lid


def next_milestone_id(state):
    mid = state.get("_nextMilestoneId", 20)
    state["_nextMilestoneId"] = mid + 1
    return mid


def next_iteration_id(state):
    iid = state.get("_nextIterationId", 20)
    state["_nextIterationId"] = iid + 1
    return iid


def next_cadence_id(state):
    cid = state.get("_nextCadenceId", 10)
    state["_nextCadenceId"] = cid + 1
    return cid


def next_board_id(state):
    bid = state.get("_nextBoardId", 10)
    state["_nextBoardId"] = bid + 1
    return bid


def next_timelog_id(state):
    tid = state.get("_nextTimelogId", 30)
    state["_nextTimelogId"] = tid + 1
    return tid


def next_todo_id(state):
    tid = state.get("_nextTodoId", 20)
    state["_nextTodoId"] = tid + 1
    return tid


NOW = "2026-02-28T12:00:00Z"


# ── Easy solve functions ─────────────────────────────────────────────

def solve_task_e1(state):
    """Close the Safari login page blank screen bug."""
    issue = find_issue_by_title(state, "Login page shows blank screen on Safari 17.2")
    issue["status"] = "closed"
    issue["closedAt"] = NOW
    issue["updatedAt"] = NOW


def solve_task_e2(state):
    """Reopen the Analytics Dashboard epic."""
    epic = find_epic_by_title(state, "Analytics Dashboard")
    epic["status"] = "open"
    epic["updatedAt"] = NOW


def solve_task_e3(state):
    """Mark the todo about upgrading vulnerable dependencies as done."""
    issue = find_issue_by_title(state, "Upgrade vulnerable dependencies identified in audit")
    todo = find_todo_for_issue(state, issue["id"], "assigned")
    todo["status"] = "done"


def solve_task_e4(state):
    """Delete the markdown preview rendering bug."""
    issue = find_issue_by_title(state, "Markdown preview renders incorrectly with nested code blocks")
    issue_id = issue["id"]
    state["issues"] = [i for i in state["issues"] if i["id"] != issue_id]
    state["todos"] = [t for t in state["todos"] if not (t["targetType"] == "issue" and t["targetId"] == issue_id)]
    state["timelogs"] = [t for t in state["timelogs"] if t["issueId"] != issue_id]


def solve_task_e5(state):
    """Set the weight of the 404 error page typo fix to 3."""
    issue = find_issue_by_title(state, "Fix typo in 404 error page message")
    issue["weight"] = 3
    issue["updatedAt"] = NOW


def solve_task_e6(state):
    """Make the API rate limiting issue confidential."""
    issue = find_issue_by_title(state, "Add rate limiting to v3 endpoints")
    issue["confidential"] = True
    issue["updatedAt"] = NOW


def solve_task_e7(state):
    """Remove the 'needs-discussion' label from the real-time collaborative editing issue."""
    issue = find_issue_by_title(state, "Build real-time collaborative editing for issue descriptions")
    label = find_label_by_title(state, "needs-discussion")
    issue["labels"] = [l for l in issue["labels"] if l != label["id"]]
    issue["updatedAt"] = NOW


def solve_task_e8(state):
    """Close the v4.3 - Mobile Optimization milestone."""
    ms = find_milestone_by_title(state, "v4.3 - Mobile Optimization")
    ms["status"] = "closed"


def solve_task_e9(state):
    """Assign Luca Rossi to the retry mechanism for failed API calls issue."""
    issue = find_issue_by_title(state, "Implement retry mechanism for failed API calls")
    user = find_user_by_name(state, "Luca Rossi")
    if user["id"] not in issue["assignees"]:
        issue["assignees"].append(user["id"])
    issue["updatedAt"] = NOW


def solve_task_e10(state):
    """Set a due date of April 30, 2026 for the webhook support issue."""
    issue = find_issue_by_title(state, "Add webhook support for issue state changes")
    issue["dueDate"] = "2026-04-30"
    issue["updatedAt"] = NOW


def solve_task_e11(state):
    """Change the health status of the JavaScript bundle size reduction issue to at risk."""
    issue = find_issue_by_title(state, "Reduce JavaScript bundle size by 40%")
    issue["healthStatus"] = "at_risk"
    issue["updatedAt"] = NOW


def solve_task_e12(state):
    """Mark the todo about the lazy loading for images issue as done."""
    issue = find_issue_by_title(state, "Implement lazy loading for images and avatars")
    todo = find_todo_for_issue(state, issue["id"], "mentioned")
    todo["status"] = "done"


def solve_task_e13(state):
    """Remove Nina Kowalski from the dark mode support issue."""
    issue = find_issue_by_title(state, "Add dark mode support for the entire application")
    user = find_user_by_name(state, "Nina Kowalski")
    issue["assignees"] = [a for a in issue["assignees"] if a != user["id"]]
    issue["updatedAt"] = NOW


def solve_task_e14(state):
    """Rename the 'good-first-issue' label to 'starter-issue'."""
    label = find_label_by_title(state, "good-first-issue")
    label["title"] = "starter-issue"


def solve_task_e15(state):
    """Close the Frontend Modernization epic."""
    epic = find_epic_by_title(state, "Frontend Modernization")
    epic["status"] = "closed"
    epic["updatedAt"] = NOW


def solve_task_e16(state):
    """Delete the Backlog milestone."""
    ms = find_milestone_by_title(state, "Backlog")
    ms_id = ms["id"]
    state["milestones"] = [m for m in state["milestones"] if m["id"] != ms_id]
    for issue in state["issues"]:
        if issue["milestoneId"] == ms_id:
            issue["milestoneId"] = None


def solve_task_e17(state):
    """Unassign Oliver Schmidt from the vulnerable dependencies upgrade issue."""
    issue = find_issue_by_title(state, "Upgrade vulnerable dependencies identified in audit")
    user = find_user_by_name(state, "Oliver Schmidt")
    issue["assignees"] = [a for a in issue["assignees"] if a != user["id"]]
    issue["updatedAt"] = NOW


def solve_task_e18(state):
    """Set the weight of the sidebar tooltip issue to 3."""
    issue = find_issue_by_title(state, "Add tooltip to truncated sidebar labels")
    issue["weight"] = 3
    issue["updatedAt"] = NOW


def solve_task_e19(state):
    """Move the project README update issue to the Q1 2026 Planning milestone."""
    issue = find_issue_by_title(state, "Update project README with new setup instructions")
    ms = find_milestone_by_title(state, "Q1 2026 Planning")
    issue["milestoneId"] = ms["id"]
    issue["updatedAt"] = NOW


def solve_task_e20(state):
    """Restore the snoozed todo about the GraphQL gateway review."""
    issue = find_issue_by_title(state, "Implement GraphQL gateway for v3 API")
    todo = find_todo_for_issue(state, issue["id"], "review_requested")
    todo["status"] = "pending"
    todo["snoozedUntil"] = None


# ── Medium solve functions ───────────────────────────────────────────

def solve_task_m1(state):
    """Create a new milestone called 'v4.4 - Integrations' starting August 1, 2026 and ending September 30, 2026."""
    mid = next_milestone_id(state)
    state["milestones"].append({
        "id": f"ms_{mid}",
        "title": "v4.4 - Integrations",
        "description": "",
        "startDate": "2026-08-01",
        "dueDate": "2026-09-30",
        "status": "active",
        "createdAt": NOW,
    })


def solve_task_m2(state):
    """Add the keyboard shortcuts issue to the Platform Redesign epic and set its iteration to Sprint 27."""
    issue = find_issue_by_title(state, "Implement keyboard shortcuts for common actions")
    epic = find_epic_by_title(state, "Platform Redesign")
    iteration = find_iteration_by_title(state, "Sprint 27")
    issue["epicId"] = epic["id"]
    issue["iterationId"] = iteration["id"]
    issue["updatedAt"] = NOW


def solve_task_m3(state):
    """Create a new issue titled 'Set up monitoring dashboard' assigned to Luca Rossi with the priority::high label."""
    user = find_user_by_name(state, "Luca Rossi")
    label = find_label_by_title(state, "priority::high")
    iid = next_issue_id(state)
    state["issues"].append({
        "id": f"issue_{iid}",
        "iid": iid,
        "title": "Set up monitoring dashboard",
        "description": "",
        "status": "open",
        "assignees": [user["id"]],
        "labels": [label["id"]],
        "milestoneId": None,
        "iterationId": None,
        "epicId": None,
        "weight": None,
        "dueDate": None,
        "startDate": None,
        "healthStatus": None,
        "timeEstimate": 0,
        "timeSpent": 0,
        "confidential": False,
        "authorId": state["currentUser"]["id"],
        "createdAt": NOW,
        "updatedAt": NOW,
        "closedAt": None,
        "taskIds": [],
        "linkedIssueIds": [],
    })


def solve_task_m4(state):
    """Remove all assignees from the dark mode support issue and set its health status to needs attention."""
    issue = find_issue_by_title(state, "Add dark mode support for the entire application")
    issue["assignees"] = []
    issue["healthStatus"] = "needs_attention"
    issue["updatedAt"] = NOW


def solve_task_m5(state):
    """Move the loading skeletons issue to the v4.0 - Platform Redesign milestone and add it to the Frontend Modernization epic."""
    issue = find_issue_by_title(state, "Add loading skeletons to replace spinners")
    ms = find_milestone_by_title(state, "v4.0 - Platform Redesign")
    epic = find_epic_by_title(state, "Frontend Modernization")
    issue["milestoneId"] = ms["id"]
    issue["epicId"] = epic["id"]
    issue["updatedAt"] = NOW


def solve_task_m6(state):
    """Add the 'breaking-change' and 'performance' labels to the container registry garbage collection issue."""
    issue = find_issue_by_title(state, "Implement container registry garbage collection")
    lbl_bc = find_label_by_title(state, "breaking-change")
    lbl_perf = find_label_by_title(state, "performance")
    for lid in [lbl_bc["id"], lbl_perf["id"]]:
        if lid not in issue["labels"]:
            issue["labels"].append(lid)
    issue["updatedAt"] = NOW


def solve_task_m7(state):
    """Disable automatic scheduling and roll-over on the Sprint Cadence."""
    cad = find_cadence_by_title(state, "Sprint Cadence")
    cad["automatic"] = False
    cad["rollOver"] = False


def solve_task_m8(state):
    """Close all open issues assigned to Fatima Al-Rashid."""
    user = find_user_by_name(state, "Fatima Al-Rashid")
    for issue in state["issues"]:
        if user["id"] in issue["assignees"] and issue["status"] == "open":
            issue["status"] = "closed"
            issue["closedAt"] = NOW
            issue["updatedAt"] = NOW


def solve_task_m9(state):
    """Create a new epic called 'CI/CD Pipeline Improvements' and add the Playwright end-to-end testing issue to it."""
    iid = next_epic_iid(state)
    epic_id = f"epic_{iid}"
    state["epics"].append({
        "id": epic_id,
        "iid": iid,
        "title": "CI/CD Pipeline Improvements",
        "description": "",
        "status": "open",
        "startDate": None,
        "dueDate": None,
        "labels": [],
        "healthStatus": None,
        "authorId": state["currentUser"]["id"],
        "confidential": False,
        "parentEpicId": None,
        "createdAt": NOW,
        "updatedAt": NOW,
    })
    issue = find_issue_by_title(state, "Set up end-to-end testing with Playwright")
    issue["epicId"] = epic_id
    issue["updatedAt"] = NOW


def solve_task_m10(state):
    """Set a time estimate of 4 hours on the dropdown menu position bug and assign it to the Backlog milestone."""
    issue = find_issue_by_title(state, "Fix dropdown menu position clipping at viewport edges")
    ms = find_milestone_by_title(state, "Backlog")
    issue["timeEstimate"] = 14400  # 4 hours in seconds
    issue["milestoneId"] = ms["id"]
    issue["updatedAt"] = NOW


def solve_task_m11(state):
    """Move the CSP headers issue to the v4.1 milestone and change its iteration to Sprint 27."""
    issue = find_issue_by_title(state, "Implement Content Security Policy headers")
    ms = find_milestone_by_title(state, "v4.1 - Performance")
    iteration = find_iteration_by_title(state, "Sprint 27")
    issue["milestoneId"] = ms["id"]
    issue["iterationId"] = iteration["id"]
    issue["updatedAt"] = NOW


def solve_task_m12(state):
    """Move all issues in Sprint 26 assigned to David Kim to Sprint 27."""
    user = find_user_by_name(state, "David Kim")
    sprint26 = find_iteration_by_title(state, "Sprint 26")
    sprint27 = find_iteration_by_title(state, "Sprint 27")
    for issue in state["issues"]:
        if issue["iterationId"] == sprint26["id"] and user["id"] in issue["assignees"]:
            issue["iterationId"] = sprint27["id"]
            issue["updatedAt"] = NOW


def solve_task_m13(state):
    """Set a start date of March 15 and due date of April 15, 2026 for the retry mechanism issue."""
    issue = find_issue_by_title(state, "Implement retry mechanism for failed API calls")
    issue["startDate"] = "2026-03-15"
    issue["dueDate"] = "2026-04-15"
    issue["updatedAt"] = NOW


def solve_task_m14(state):
    """Create a new iteration called 'Sprint 29' in the Sprint Cadence starting March 31 and ending April 13, 2026."""
    cad = find_cadence_by_title(state, "Sprint Cadence")
    iid = next_iteration_id(state)
    state["iterations"].append({
        "id": f"iter_{iid}",
        "title": "Sprint 29",
        "cadenceId": cad["id"],
        "startDate": "2026-03-31",
        "dueDate": "2026-04-13",
        "status": "upcoming",
        "createdAt": NOW,
    })


def solve_task_m15(state):
    """Replace the 'UX' label on the Platform Redesign epic with 'needs-discussion'."""
    epic = find_epic_by_title(state, "Platform Redesign")
    lbl_ux = find_label_by_title(state, "UX")
    lbl_nd = find_label_by_title(state, "needs-discussion")
    epic["labels"] = [l for l in epic["labels"] if l != lbl_ux["id"]]
    if lbl_nd["id"] not in epic["labels"]:
        epic["labels"].append(lbl_nd["id"])
    epic["updatedAt"] = NOW


def solve_task_m16(state):
    """Assign Priya Patel and Marcus Johnson to the component library documentation issue."""
    issue = find_issue_by_title(state, "Build component library documentation site")
    priya = find_user_by_name(state, "Priya Patel")
    marcus = find_user_by_name(state, "Marcus Johnson")
    for uid in [priya["id"], marcus["id"]]:
        if uid not in issue["assignees"]:
            issue["assignees"].append(uid)
    issue["updatedAt"] = NOW


def solve_task_m17(state):
    """Create a new board called 'Priority Board' with a list for the priority::critical label."""
    label = find_label_by_title(state, "priority::critical")
    bid = next_board_id(state)
    state["boards"].append({
        "id": f"board_{bid}",
        "name": "Priority Board",
        "lists": [
            {
                "id": f"list_{bid}_1",
                "type": "label",
                "labelId": label["id"],
                "position": 0,
            }
        ],
    })


def solve_task_m18(state):
    """Add the 'performance' label to the JWT authentication migration issue and set its health status to needs attention."""
    issue = find_issue_by_title(state, "Migrate user authentication from sessions to JWT")
    label = find_label_by_title(state, "performance")
    if label["id"] not in issue["labels"]:
        issue["labels"].append(label["id"])
    issue["healthStatus"] = "needs_attention"
    issue["updatedAt"] = NOW


def solve_task_m19(state):
    """Remove Aisha Mohammed from the component library documentation issue and assign Nina Kowalski instead."""
    issue = find_issue_by_title(state, "Build component library documentation site")
    aisha = find_user_by_name(state, "Aisha Mohammed")
    nina = find_user_by_name(state, "Nina Kowalski")
    issue["assignees"] = [a for a in issue["assignees"] if a != aisha["id"]]
    if nina["id"] not in issue["assignees"]:
        issue["assignees"].append(nina["id"])
    issue["updatedAt"] = NOW


def solve_task_m20(state):
    """Rename the 'technical-debt' label to 'tech-debt' and set its description to 'Legacy code requiring refactoring'."""
    label = find_label_by_title(state, "technical-debt")
    label["title"] = "tech-debt"
    label["description"] = "Legacy code requiring refactoring"


# ── Hard solve functions ─────────────────────────────────────────────

def solve_task_h1(state):
    """Create a new epic 'Accessibility Initiative' with the accessibility label, then add all issues with that label to it."""
    lbl = find_label_by_title(state, "accessibility")
    iid = next_epic_iid(state)
    epic_id = f"epic_{iid}"
    state["epics"].append({
        "id": epic_id,
        "iid": iid,
        "title": "Accessibility Initiative",
        "description": "",
        "status": "open",
        "startDate": None,
        "dueDate": None,
        "labels": [lbl["id"]],
        "healthStatus": None,
        "authorId": state["currentUser"]["id"],
        "confidential": False,
        "parentEpicId": None,
        "createdAt": NOW,
        "updatedAt": NOW,
    })
    for issue in state["issues"]:
        if lbl["id"] in issue["labels"]:
            issue["epicId"] = epic_id
            issue["updatedAt"] = NOW


def solve_task_h2(state):
    """Close all open bugs that have priority::low."""
    lbl_bug = find_label_by_title(state, "type::bug")
    lbl_low = find_label_by_title(state, "priority::low")
    for issue in state["issues"]:
        if (issue["status"] == "open"
                and lbl_bug["id"] in issue["labels"]
                and lbl_low["id"] in issue["labels"]):
            issue["status"] = "closed"
            issue["closedAt"] = NOW
            issue["updatedAt"] = NOW


def solve_task_h3(state):
    """Move all issues in Security Hardening that don't have the security label to v4.1."""
    ms_sec = find_milestone_by_title(state, "v4.2 - Security Hardening")
    ms_perf = find_milestone_by_title(state, "v4.1 - Performance")
    lbl_sec = find_label_by_title(state, "security")
    for issue in state["issues"]:
        if issue["milestoneId"] == ms_sec["id"] and lbl_sec["id"] not in issue["labels"]:
            issue["milestoneId"] = ms_perf["id"]
            issue["updatedAt"] = NOW


def solve_task_h4(state):
    """Create Hotfix Cadence with 1-week duration, then create Hotfix 1 iteration."""
    cid = next_cadence_id(state)
    cadence_id = f"cad_{cid}"
    state["iterationCadences"].append({
        "id": cadence_id,
        "title": "Hotfix Cadence",
        "description": "",
        "automatic": False,
        "startDate": "2026-03-03",
        "durationWeeks": 1,
        "upcomingIterations": 1,
        "rollOver": False,
        "active": True,
    })
    iid = next_iteration_id(state)
    state["iterations"].append({
        "id": f"iter_{iid}",
        "title": "Hotfix 1",
        "cadenceId": cadence_id,
        "startDate": "2026-03-03",
        "dueDate": "2026-03-09",
        "status": "upcoming",
        "createdAt": NOW,
    })


def solve_task_h5(state):
    """Reassign all of James O'Brien's open issues to Yuki Tanaka."""
    james = find_user_by_name(state, "James O'Brien")
    yuki = find_user_by_name(state, "Yuki Tanaka")
    for issue in state["issues"]:
        if issue["status"] == "open" and james["id"] in issue["assignees"]:
            issue["assignees"] = [a for a in issue["assignees"] if a != james["id"]]
            if yuki["id"] not in issue["assignees"]:
                issue["assignees"].append(yuki["id"])
            issue["updatedAt"] = NOW


def solve_task_h6(state):
    """Close the v4.0 milestone and move all its open issues to v4.1."""
    ms_v40 = find_milestone_by_title(state, "v4.0 - Platform Redesign")
    ms_v41 = find_milestone_by_title(state, "v4.1 - Performance")
    ms_v40["status"] = "closed"
    for issue in state["issues"]:
        if issue["milestoneId"] == ms_v40["id"] and issue["status"] == "open":
            issue["milestoneId"] = ms_v41["id"]
            issue["updatedAt"] = NOW


def solve_task_h7(state):
    """Remove all labels from the error boundary issue and replace with type::bug and priority::medium."""
    issue = find_issue_by_title(state, "Improve error boundary fallback UI")
    lbl_bug = find_label_by_title(state, "type::bug")
    lbl_med = find_label_by_title(state, "priority::medium")
    issue["labels"] = [lbl_bug["id"], lbl_med["id"]]
    issue["updatedAt"] = NOW


def solve_task_h8(state):
    """Create confidential issue 'Emergency security patch' with priority::critical, security, assigned to James O'Brien and Oliver Schmidt, weight 2, in Security Hardening milestone."""
    lbl_crit = find_label_by_title(state, "priority::critical")
    lbl_sec = find_label_by_title(state, "security")
    james = find_user_by_name(state, "James O'Brien")
    oliver = find_user_by_name(state, "Oliver Schmidt")
    ms = find_milestone_by_title(state, "v4.2 - Security Hardening")
    iid = next_issue_id(state)
    state["issues"].append({
        "id": f"issue_{iid}",
        "iid": iid,
        "title": "Emergency security patch",
        "description": "",
        "status": "open",
        "assignees": [james["id"], oliver["id"]],
        "labels": [lbl_crit["id"], lbl_sec["id"]],
        "milestoneId": ms["id"],
        "iterationId": None,
        "epicId": None,
        "weight": 2,
        "dueDate": None,
        "startDate": None,
        "healthStatus": None,
        "timeEstimate": 0,
        "timeSpent": 0,
        "confidential": True,
        "authorId": state["currentUser"]["id"],
        "createdAt": NOW,
        "updatedAt": NOW,
        "closedAt": None,
        "taskIds": [],
        "linkedIssueIds": [],
    })


def solve_task_h9(state):
    """Move all unassigned open issues to the Backlog milestone and add 'needs-discussion' label."""
    ms = find_milestone_by_title(state, "Backlog")
    lbl = find_label_by_title(state, "needs-discussion")
    for issue in state["issues"]:
        if issue["status"] == "open" and len(issue["assignees"]) == 0:
            issue["milestoneId"] = ms["id"]
            if lbl["id"] not in issue["labels"]:
                issue["labels"].append(lbl["id"])
            issue["updatedAt"] = NOW


def solve_task_h10(state):
    """Delete the Sprint Board and create a new Release Board with lists for v4.0, v4.1, and v4.2 milestones."""
    state["boards"] = [b for b in state["boards"] if b["name"] != "Sprint Board"]
    ms_v40 = find_milestone_by_title(state, "v4.0 - Platform Redesign")
    ms_v41 = find_milestone_by_title(state, "v4.1 - Performance")
    ms_v42 = find_milestone_by_title(state, "v4.2 - Security Hardening")
    bid = next_board_id(state)
    state["boards"].append({
        "id": f"board_{bid}",
        "name": "Release Board",
        "lists": [
            {"id": f"list_{bid}_1", "type": "milestone", "milestoneId": ms_v40["id"], "position": 0},
            {"id": f"list_{bid}_2", "type": "milestone", "milestoneId": ms_v41["id"], "position": 1},
            {"id": f"list_{bid}_3", "type": "milestone", "milestoneId": ms_v42["id"], "position": 2},
        ],
    })


def solve_task_h11(state):
    """Reassign all of Luca Rossi's issues under the Performance Initiative epic tree to Chen Wei."""
    luca = find_user_by_name(state, "Luca Rossi")
    chen = find_user_by_name(state, "Chen Wei")
    perf_epic = find_epic_by_title(state, "Performance Initiative")
    # Collect all epic IDs in the tree (parent + children)
    epic_ids = {perf_epic["id"]}
    for epic in state["epics"]:
        if epic["parentEpicId"] == perf_epic["id"]:
            epic_ids.add(epic["id"])
    for issue in state["issues"]:
        if issue["epicId"] in epic_ids and luca["id"] in issue["assignees"]:
            issue["assignees"] = [a for a in issue["assignees"] if a != luca["id"]]
            if chen["id"] not in issue["assignees"]:
                issue["assignees"].append(chen["id"])
            issue["updatedAt"] = NOW


def solve_task_h12(state):
    """Set weight to 8 and add priority::high to all issues in the Database Optimization epic."""
    epic = find_epic_by_title(state, "Database Optimization")
    lbl_high = find_label_by_title(state, "priority::high")
    for issue in state["issues"]:
        if issue["epicId"] == epic["id"]:
            issue["weight"] = 8
            # Remove existing priority:: labels (scoped)
            issue["labels"] = [l for l in issue["labels"]
                               if not any(lab["title"].startswith("priority::") and lab["id"] == l
                                          for lab in state["labels"])]
            if lbl_high["id"] not in issue["labels"]:
                issue["labels"].append(lbl_high["id"])
            issue["updatedAt"] = NOW


def solve_task_h13(state):
    """Create label 'sprint-goal' with green color, then apply to all open issues in Sprint 26."""
    lid = next_label_id(state)
    label_id = f"lbl_{lid}"
    state["labels"].append({
        "id": label_id,
        "title": "sprint-goal",
        "description": "",
        "color": "#1aaa55",
        "textColor": "#fff",
        "type": "project",
        "scoped": False,
    })
    sprint26 = find_iteration_by_title(state, "Sprint 26")
    for issue in state["issues"]:
        if issue["status"] == "open" and issue["iterationId"] == sprint26["id"]:
            if label_id not in issue["labels"]:
                issue["labels"].append(label_id)
            issue["updatedAt"] = NOW


def solve_task_h14(state):
    """Mark all pending todos as done, then create a new issue 'Review Q1 objectives' assigned to self with priority::medium."""
    for todo in state["todos"]:
        if todo["status"] == "pending":
            todo["status"] = "done"
    lbl = find_label_by_title(state, "priority::medium")
    iid = next_issue_id(state)
    state["issues"].append({
        "id": f"issue_{iid}",
        "iid": iid,
        "title": "Review Q1 objectives",
        "description": "",
        "status": "open",
        "assignees": [state["currentUser"]["id"]],
        "labels": [lbl["id"]],
        "milestoneId": None,
        "iterationId": None,
        "epicId": None,
        "weight": None,
        "dueDate": None,
        "startDate": None,
        "healthStatus": None,
        "timeEstimate": 0,
        "timeSpent": 0,
        "confidential": False,
        "authorId": state["currentUser"]["id"],
        "createdAt": NOW,
        "updatedAt": NOW,
        "closedAt": None,
        "taskIds": [],
        "linkedIssueIds": [],
    })


def solve_task_h15(state):
    """Delete all labels in the 'component' scope."""
    component_ids = {l["id"] for l in state["labels"] if l["title"].startswith("component::")}
    state["labels"] = [l for l in state["labels"] if l["id"] not in component_ids]
    for issue in state["issues"]:
        orig_len = len(issue["labels"])
        issue["labels"] = [l for l in issue["labels"] if l not in component_ids]
        if len(issue["labels"]) != orig_len:
            issue["updatedAt"] = NOW
    for epic in state["epics"]:
        epic["labels"] = [l for l in epic["labels"] if l not in component_ids]


def solve_task_h16(state):
    """Make sure Nina Kowalski is assigned to every issue in the Frontend Modernization epic."""
    nina = find_user_by_name(state, "Nina Kowalski")
    epic = find_epic_by_title(state, "Frontend Modernization")
    for issue in state["issues"]:
        if issue["epicId"] == epic["id"]:
            if nina["id"] not in issue["assignees"]:
                issue["assignees"].append(nina["id"])
                issue["updatedAt"] = NOW


def solve_task_h17(state):
    """Remove 'technical-debt' label from all issues and add 'type::improvement' instead."""
    lbl_td = find_label_by_title(state, "technical-debt")
    lbl_imp = find_label_by_title(state, "type::improvement")
    for issue in state["issues"]:
        if lbl_td["id"] in issue["labels"]:
            issue["labels"] = [l for l in issue["labels"] if l != lbl_td["id"]]
            # type::improvement is scoped, remove existing type:: labels
            issue["labels"] = [l for l in issue["labels"]
                               if not any(lab["title"].startswith("type::") and lab["id"] == l
                                          for lab in state["labels"])]
            if lbl_imp["id"] not in issue["labels"]:
                issue["labels"].append(lbl_imp["id"])
            issue["updatedAt"] = NOW


def solve_task_h18(state):
    """Create milestone 'Bug Bash Week' then move open type::bug issues without a milestone into it."""
    mid = next_milestone_id(state)
    ms_id = f"ms_{mid}"
    state["milestones"].append({
        "id": ms_id,
        "title": "Bug Bash Week",
        "description": "",
        "startDate": "2026-03-10",
        "dueDate": "2026-03-14",
        "status": "active",
        "createdAt": NOW,
    })
    lbl_bug = find_label_by_title(state, "type::bug")
    for issue in state["issues"]:
        if (issue["status"] == "open"
                and lbl_bug["id"] in issue["labels"]
                and issue["milestoneId"] is None):
            issue["milestoneId"] = ms_id
            issue["updatedAt"] = NOW


def solve_task_h19(state):
    """Close the Caching Layer Implementation epic and reassign its issues to Database Optimization."""
    epic_cache = find_epic_by_title(state, "Caching Layer Implementation")
    epic_db = find_epic_by_title(state, "Database Optimization")
    epic_cache["status"] = "closed"
    epic_cache["updatedAt"] = NOW
    for issue in state["issues"]:
        if issue["epicId"] == epic_cache["id"]:
            issue["epicId"] = epic_db["id"]
            issue["updatedAt"] = NOW


def solve_task_h20(state):
    """Delete 'blocked' label, create 'status::blocked' with #b91c1c, apply to user settings migration issue."""
    # Delete old blocked label
    old_lbl = find_label_by_title(state, "blocked")
    old_id = old_lbl["id"]
    state["labels"] = [l for l in state["labels"] if l["id"] != old_id]
    # Remove from all issues and epics
    for issue in state["issues"]:
        issue["labels"] = [l for l in issue["labels"] if l != old_id]
    for epic in state["epics"]:
        epic["labels"] = [l for l in epic["labels"] if l != old_id]

    # Create new scoped label
    lid = next_label_id(state)
    new_label_id = f"lbl_{lid}"
    state["labels"].append({
        "id": new_label_id,
        "title": "status::blocked",
        "description": "",
        "color": "#b91c1c",
        "textColor": "#fff",
        "type": "project",
        "scoped": True,
    })
    # Apply to user settings migration issue
    issue = find_issue_by_title(state, "Migrate user settings page to React")
    if new_label_id not in issue["labels"]:
        issue["labels"].append(new_label_id)
    issue["updatedAt"] = NOW


# ── Hardening Round 1: Easy solve functions ──────────────────────────

def solve_task_e21(state):
    """Snooze the todo about the JavaScript bundle size issue until tomorrow morning."""
    issue = find_issue_by_title(state, "Reduce JavaScript bundle size by 40%")
    todo = find_todo_for_issue(state, issue["id"], "assigned")
    todo["status"] = "snoozed"
    todo["snoozedUntil"] = "2026-03-02T08:00:00Z"


def solve_task_e22(state):
    """Add a time entry of 3 hours to the CSP headers issue with summary 'Security audit review'."""
    issue = find_issue_by_title(state, "Implement Content Security Policy headers")
    tid = next_timelog_id(state)
    state["timelogs"].append({
        "id": f"tl_{tid}",
        "issueId": issue["id"],
        "userId": state["currentUser"]["id"],
        "timeSpent": 10800,
        "summary": "Security audit review",
        "spentAt": NOW,
    })
    issue["timeSpent"] = issue.get("timeSpent", 0) + 10800
    issue["updatedAt"] = NOW


# ── Hardening Round 1: Medium solve functions ────────────────────────

def solve_task_m21(state):
    """Find the open issue with the highest weight and change its health status to 'at risk'."""
    issue = find_issue_by_title(state, "Build real-time collaborative editing for issue descriptions")
    issue["healthStatus"] = "at_risk"
    issue["updatedAt"] = NOW


def solve_task_m22(state):
    """Assign the CSRF token rotation issue to Sprint 26 and replace its priority label with priority::high."""
    issue = find_issue_by_title(state, "Implement CSRF token rotation")
    sprint26 = find_iteration_by_title(state, "Sprint 26")
    lbl_high = find_label_by_title(state, "priority::high")
    issue["iterationId"] = sprint26["id"]
    # Remove existing priority:: scoped labels
    issue["labels"] = [l for l in issue["labels"]
                       if not any(lab["title"].startswith("priority::") and lab["id"] == l
                                  for lab in state["labels"])]
    if lbl_high["id"] not in issue["labels"]:
        issue["labels"].append(lbl_high["id"])
    issue["updatedAt"] = NOW


def solve_task_m23(state):
    """Add Chen Wei and Yuki Tanaka as assignees to the database connection pool issue."""
    issue = find_issue_by_title(state, "Database connection pool exhaustion under load")
    chen = find_user_by_name(state, "Chen Wei")
    yuki = find_user_by_name(state, "Yuki Tanaka")
    for uid in [chen["id"], yuki["id"]]:
        if uid not in issue["assignees"]:
            issue["assignees"].append(uid)
    issue["updatedAt"] = NOW


def solve_task_m24(state):
    """Create a child epic of Security Hardening called 'Compliance Automation' and move the CSRF issue into it."""
    sec_epic = find_epic_by_title(state, "Security Hardening")
    iid = next_epic_iid(state)
    epic_id = f"epic_{iid}"
    state["epics"].append({
        "id": epic_id,
        "iid": iid,
        "title": "Compliance Automation",
        "description": "",
        "status": "open",
        "startDate": None,
        "dueDate": None,
        "labels": [],
        "healthStatus": None,
        "authorId": state["currentUser"]["id"],
        "confidential": False,
        "parentEpicId": sec_epic["id"],
        "createdAt": NOW,
        "updatedAt": NOW,
    })
    issue = find_issue_by_title(state, "Implement CSRF token rotation")
    issue["epicId"] = epic_id
    issue["updatedAt"] = NOW


def solve_task_m25(state):
    """Move the lazy loading images issue to v4.0 and assign it to Sprint 27."""
    issue = find_issue_by_title(state, "Implement lazy loading for images and avatars")
    ms = find_milestone_by_title(state, "v4.0 - Platform Redesign")
    sprint27 = find_iteration_by_title(state, "Sprint 27")
    issue["milestoneId"] = ms["id"]
    issue["iterationId"] = sprint27["id"]
    issue["updatedAt"] = NOW


def solve_task_m26(state):
    """Add a time estimate of 1 day to the file upload bug and log 2 hours."""
    issue = find_issue_by_title(state, "File upload fails silently for files > 50MB")
    issue["timeEstimate"] = 28800  # 1 day = 8h = 28800s
    tid = next_timelog_id(state)
    state["timelogs"].append({
        "id": f"tl_{tid}",
        "issueId": issue["id"],
        "userId": state["currentUser"]["id"],
        "timeSpent": 7200,
        "summary": "Reproducing the issue",
        "spentAt": NOW,
    })
    issue["timeSpent"] = issue.get("timeSpent", 0) + 7200
    issue["updatedAt"] = NOW


def solve_task_m27(state):
    """Change the description and color of the 'testing' label."""
    label = find_label_by_title(state, "testing")
    label["description"] = "Quality assurance and test automation"
    label["color"] = "#0e8a16"
    label["textColor"] = "#fff"


def solve_task_m28(state):
    """Create a new iteration 'Release 4.0 GA' in the Release Cycle cadence."""
    cad = find_cadence_by_title(state, "Release Cycle")
    iid = next_iteration_id(state)
    state["iterations"].append({
        "id": f"iter_{iid}",
        "title": "Release 4.0 GA",
        "cadenceId": cad["id"],
        "startDate": "2026-03-01",
        "dueDate": "2026-03-15",
        "status": "upcoming",
        "createdAt": NOW,
    })


# ── Hardening Round 1: Hard solve functions ──────────────────────────

def solve_task_h21(state):
    """Set health status to 'on track' for every open issue in Sprint 27."""
    sprint27 = find_iteration_by_title(state, "Sprint 27")
    for issue in state["issues"]:
        if issue["iterationId"] == sprint27["id"] and issue["status"] == "open":
            issue["healthStatus"] = "on_track"
            issue["updatedAt"] = NOW


def solve_task_h22(state):
    """Move all open issues with no milestone to the Backlog milestone."""
    ms = find_milestone_by_title(state, "Backlog")
    for issue in state["issues"]:
        if issue["status"] == "open" and issue["milestoneId"] is None:
            issue["milestoneId"] = ms["id"]
            issue["updatedAt"] = NOW


def solve_task_h23(state):
    """Add 'breaking-change' label to every open issue in the API v3 Migration epic."""
    epic = find_epic_by_title(state, "API v3 Migration")
    lbl = find_label_by_title(state, "breaking-change")
    for issue in state["issues"]:
        if issue["epicId"] == epic["id"] and issue["status"] == "open":
            if lbl["id"] not in issue["labels"]:
                issue["labels"].append(lbl["id"])
            issue["updatedAt"] = NOW


def solve_task_h24(state):
    """Create a board 'Component Board' with lists for all 5 component labels."""
    bid = next_board_id(state)
    component_labels = [l for l in state["labels"] if l["title"].startswith("component::")]
    component_labels.sort(key=lambda l: l["title"])
    lists = []
    for i, lbl in enumerate(component_labels):
        lists.append({
            "id": f"list_{bid}_{i + 1}",
            "type": "label",
            "labelId": lbl["id"],
            "position": i,
        })
    state["boards"].append({
        "id": f"board_{bid}",
        "name": "Component Board",
        "lists": lists,
    })


def solve_task_h25(state):
    """For all open issues assigned to David Kim, set health to 'needs attention' and add 'blocked' label."""
    david = find_user_by_name(state, "David Kim")
    lbl = find_label_by_title(state, "blocked")
    for issue in state["issues"]:
        if issue["status"] == "open" and david["id"] in issue["assignees"]:
            issue["healthStatus"] = "needs_attention"
            if lbl["id"] not in issue["labels"]:
                issue["labels"].append(lbl["id"])
            issue["updatedAt"] = NOW


def solve_task_h26(state):
    """Create epic 'Q2 Planning' as child of Platform Redesign, move Sprint 27 issues into it."""
    platform = find_epic_by_title(state, "Platform Redesign")
    sprint27 = find_iteration_by_title(state, "Sprint 27")
    iid = next_epic_iid(state)
    epic_id = f"epic_{iid}"
    state["epics"].append({
        "id": epic_id,
        "iid": iid,
        "title": "Q2 Planning",
        "description": "",
        "status": "open",
        "startDate": None,
        "dueDate": None,
        "labels": [],
        "healthStatus": None,
        "authorId": state["currentUser"]["id"],
        "confidential": False,
        "parentEpicId": platform["id"],
        "createdAt": NOW,
        "updatedAt": NOW,
    })
    for issue in state["issues"]:
        if issue["iterationId"] == sprint27["id"] and issue["status"] == "open":
            issue["epicId"] = epic_id
            issue["updatedAt"] = NOW


def solve_task_h27(state):
    """Restore all done todos to pending and remove snooze from snoozed todos."""
    for todo in state["todos"]:
        if todo["status"] == "done":
            todo["status"] = "pending"
        elif todo["status"] == "snoozed":
            todo["status"] = "pending"
            todo["snoozedUntil"] = None


def solve_task_h28(state):
    """Remove the 'UX' label from all issues and epics."""
    lbl = find_label_by_title(state, "UX")
    ux_id = lbl["id"]
    for issue in state["issues"]:
        if ux_id in issue["labels"]:
            issue["labels"] = [l for l in issue["labels"] if l != ux_id]
            issue["updatedAt"] = NOW
    for epic in state["epics"]:
        if ux_id in epic["labels"]:
            epic["labels"] = [l for l in epic["labels"] if l != ux_id]
            epic["updatedAt"] = NOW


def solve_task_h29(state):
    """Set due date of October 31, 2026 on every open v5.0 issue that has no due date."""
    ms = find_milestone_by_title(state, "v5.0 - Enterprise Edition")
    for issue in state["issues"]:
        if (issue["milestoneId"] == ms["id"]
                and issue["status"] == "open"
                and issue["dueDate"] is None):
            issue["dueDate"] = "2026-10-31"
            issue["updatedAt"] = NOW


def solve_task_h30(state):
    """Close all open v4.0 issues with workflow::in-progress and replace with workflow::done."""
    ms = find_milestone_by_title(state, "v4.0 - Platform Redesign")
    lbl_ip = find_label_by_title(state, "workflow::in-progress")
    lbl_done = find_label_by_title(state, "workflow::done")
    for issue in state["issues"]:
        if (issue["milestoneId"] == ms["id"]
                and issue["status"] == "open"
                and lbl_ip["id"] in issue["labels"]):
            issue["status"] = "closed"
            issue["closedAt"] = NOW
            # Remove workflow::in-progress, add workflow::done (scoped replacement)
            issue["labels"] = [l for l in issue["labels"]
                               if not any(lab["title"].startswith("workflow::") and lab["id"] == l
                                          for lab in state["labels"])]
            if lbl_done["id"] not in issue["labels"]:
                issue["labels"].append(lbl_done["id"])
            issue["updatedAt"] = NOW


# ── Solver registry ──────────────────────────────────────────────────

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
    # Hardening Round 1
    "task_e21": solve_task_e21,
    "task_e22": solve_task_e22,
    "task_m21": solve_task_m21,
    "task_m22": solve_task_m22,
    "task_m23": solve_task_m23,
    "task_m24": solve_task_m24,
    "task_m25": solve_task_m25,
    "task_m26": solve_task_m26,
    "task_m27": solve_task_m27,
    "task_m28": solve_task_m28,
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


def find_free_port(start=9500):
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
    """Start the app server on the given port."""
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
    """Load task definitions from tasks.json."""
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
    parser = argparse.ArgumentParser(description="GitLab Plan & Track real-task sanity check")
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
