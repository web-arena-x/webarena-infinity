"""
Sanity check for Figma Slides real tasks.
Verifies that each solve function produces state the verifier accepts.
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
from pathlib import Path

import requests

APP_DIR = Path(__file__).resolve().parent
TASKS_FILE = APP_DIR / "real-tasks.json"
NOW = "2026-03-18T12:00:00Z"

# ─── JavaScript to extract seed state from data.js ───────────────────────────
_SEED_STATE_JS = r"""
const fs = require('fs');
const vm = require('vm');
const src = fs.readFileSync(process.argv[1], 'utf-8');
const ctx = { console, module: { exports: {} }, require };
vm.createContext(ctx);
vm.runInContext(src, ctx);
const seed = ctx.getSeedData();
process.stdout.write(JSON.stringify(seed));
"""


# ═══════════════════════════════════════════════════════════════════════════════
# Helpers
# ═══════════════════════════════════════════════════════════════════════════════

def find_pres(state, title):
    """Find a presentation by title. Raises if not found."""
    for p in state["presentations"]:
        if p["title"] == title:
            return p
    raise ValueError(f"Presentation not found: {title}")


def find_pres_by_id(state, pid):
    for p in state["presentations"]:
        if p["id"] == pid:
            return p
    raise ValueError(f"Presentation ID not found: {pid}")


def find_comment(state, content_substr, pres_id=None):
    """Find a comment by content substring, optionally filtered by presentationId."""
    for c in state["comments"]:
        if content_substr.lower() in c["content"].lower():
            if pres_id is None or c["presentationId"] == pres_id:
                return c
    raise ValueError(f"Comment not found containing '{content_substr}'" +
                     (f" on {pres_id}" if pres_id else ""))


def find_user(state, name):
    for u in state["users"]:
        if u["name"] == name:
            return u
    raise ValueError(f"User not found: {name}")


def next_pres_id(state):
    pid = state["_nextPresentationId"]
    state["_nextPresentationId"] = pid + 1
    return "pres_" + str(pid).zfill(3)


def next_slide_id(state):
    sid = state["_nextSlideId"]
    state["_nextSlideId"] = sid + 1
    return "slide_" + str(sid).zfill(5)


def next_elem_id(state):
    eid = state["_nextElementId"]
    state["_nextElementId"] = eid + 1
    return "elem_" + str(eid).zfill(5)


# ═══════════════════════════════════════════════════════════════════════════════
# Solve functions — EASY
# ═══════════════════════════════════════════════════════════════════════════════

def solve_task_e1(state):
    """Star the User Research Findings presentation."""
    p = find_pres(state, "User Research Findings \u2014 Mobile App")
    p["starred"] = True
    p["updatedAt"] = NOW


def solve_task_e2(state):
    """Archive the Design Sprint Week 12 Recap."""
    p = find_pres(state, "Design Sprint Week 12 Recap")
    p["status"] = "archived"
    p["updatedAt"] = NOW


def solve_task_e3(state):
    """Delete the Competitor Analysis Dashboard."""
    pid = None
    for p in state["presentations"]:
        if p["title"] == "Competitor Analysis Dashboard":
            pid = p["id"]
            break
    state["presentations"] = [p for p in state["presentations"] if p["id"] != pid]
    state["slides"] = [s for s in state["slides"] if s["presentationId"] != pid]
    state["comments"] = [c for c in state["comments"] if c["presentationId"] != pid]


def solve_task_e4(state):
    """Unstar Brand Identity Guidelines v2.0."""
    p = find_pres(state, "Brand Identity Guidelines v2.0")
    p["starred"] = False
    p["updatedAt"] = NOW


def solve_task_e5(state):
    """Change Onboarding Training Module back to draft."""
    p = find_pres(state, "Onboarding Training Module")
    p["status"] = "draft"
    p["updatedAt"] = NOW


def solve_task_e6(state):
    """Resolve the comment about the illustration style guide on Brand Identity Guidelines."""
    c = find_comment(state, "illustration style guide", "pres_002")
    c["resolved"] = True


def solve_task_e7(state):
    """Delete the comment about the buddy program on Onboarding Training Module."""
    state["comments"] = [
        c for c in state["comments"]
        if not ("buddy program" in c["content"].lower() and c["presentationId"] == "pres_009")
    ]


def solve_task_e8(state):
    """Make Q4 2025 Revenue Analysis public."""
    p = find_pres(state, "Q4 2025 Revenue Analysis")
    p["shareSettings"]["visibility"] = "public"
    p["updatedAt"] = NOW


def solve_task_e9(state):
    """Disable comments on Design Workshop Materials."""
    p = find_pres(state, "Design Workshop Materials")
    p["shareSettings"]["allowComments"] = False
    p["updatedAt"] = NOW


def solve_task_e10(state):
    """Star the Accessibility Audit Results."""
    p = find_pres(state, "Accessibility Audit Results")
    p["starred"] = True
    p["updatedAt"] = NOW


def solve_task_e11(state):
    """Publish the Website Redesign Proposal for TechStartup.io."""
    p = find_pres(state, "Website Redesign Proposal \u2014 TechStartup.io")
    p["status"] = "published"
    p["updatedAt"] = NOW


def solve_task_e12(state):
    """Enable editing on Q4 2025 Revenue Analysis."""
    p = find_pres(state, "Q4 2025 Revenue Analysis")
    p["shareSettings"]["allowEditing"] = True
    p["updatedAt"] = NOW


def solve_task_e13(state):
    """Remove David Kim from the TechVentures Redesign proposal."""
    p = find_pres(state, "Client Proposal \u2014 TechVentures Redesign")
    sw = p["shareSettings"]["sharedWith"]
    if "user_007" in sw:
        sw.remove("user_007")
    p["updatedAt"] = NOW


def solve_task_e14(state):
    """Resolve the comment about the database architecture diagram on Engineering Architecture Overview."""
    c = find_comment(state, "database architecture", "pres_005")
    c["resolved"] = True


def solve_task_e15(state):
    """Unstar Annual Company All-Hands 2026."""
    p = find_pres(state, "Annual Company All-Hands 2026")
    p["starred"] = False
    p["updatedAt"] = NOW


def solve_task_e16(state):
    """Unstar Marketing Campaign: Design Without Limits."""
    p = find_pres(state, "Marketing Campaign: Design Without Limits")
    p["starred"] = False
    p["updatedAt"] = NOW


def solve_task_e17(state):
    """Unresolve the revenue numbers comment on All-Hands."""
    c = find_comment(state, "Revenue numbers confirmed", "pres_006")
    c["resolved"] = False


def solve_task_e18(state):
    """Star Product Demo — Enterprise Features."""
    p = find_pres(state, "Product Demo \u2014 Enterprise Features")
    p["starred"] = True
    p["updatedAt"] = NOW


def solve_task_e19(state):
    """Disable editing on Brand Identity Guidelines v2.0."""
    p = find_pres(state, "Brand Identity Guidelines v2.0")
    p["shareSettings"]["allowEditing"] = False
    p["updatedAt"] = NOW


def solve_task_e20(state):
    """Delete the comment about the mobile nav redesign on Design Sprint Week 12 Recap."""
    state["comments"] = [
        c for c in state["comments"]
        if not ("mobile nav redesign" in c["content"].lower() and c["presentationId"] == "pres_008")
    ]


# ═══════════════════════════════════════════════════════════════════════════════
# Solve functions — MEDIUM
# ═══════════════════════════════════════════════════════════════════════════════

def solve_task_m1(state):
    """Create 'Q2 Planning Session' with corporate theme."""
    pid = next_pres_id(state)
    sid = next_slide_id(state)
    eid = next_elem_id(state)
    state["presentations"].append({
        "id": pid,
        "title": "Q2 Planning Session",
        "description": "Quarterly planning for Q2 2026",
        "createdAt": NOW,
        "updatedAt": NOW,
        "createdBy": state["currentUserId"],
        "theme": "corporate",
        "tags": [],
        "starred": False,
        "status": "draft",
        "slideCount": 1,
        "shareSettings": {
            "visibility": "private",
            "allowComments": True,
            "allowEditing": False,
            "shareLink": "",
            "embedLink": "",
            "sharedWith": [state["currentUserId"]]
        }
    })
    state["slides"].append({
        "id": sid,
        "presentationId": pid,
        "order": 0,
        "layout": "title",
        "backgroundColor": "#ffffff",
        "transition": {"type": "none", "duration": 500},
        "speakerNotes": "",
        "elements": [{
            "id": eid, "type": "text", "x": 80, "y": 180, "width": 800, "height": 70,
            "rotation": 0, "opacity": 1, "locked": False,
            "content": "Q2 Planning Session",
            "shapeType": None, "fill": None, "stroke": None, "strokeWidth": 0,
            "cornerRadius": 0, "imageUrl": None, "imagePlaceholder": None,
            "style": {"fontFamily": "Inter", "fontSize": 48, "fontWeight": "bold",
                       "color": "#1a1a2e", "textAlign": "center", "italic": False,
                       "underline": False, "lineHeight": 1.2, "letterSpacing": -1,
                       "listType": "none"},
            "animation": {"type": "none", "duration": 300, "delay": 0, "order": 0}
        }]
    })


def solve_task_m2(state):
    """Share Series B Fundraising Pitch with Anika Patel and enable comments."""
    p = find_pres(state, "Series B Fundraising Pitch")
    ss = p["shareSettings"]
    if "user_003" not in ss["sharedWith"]:
        ss["sharedWith"].append("user_003")
    ss["allowComments"] = True
    p["updatedAt"] = NOW


def solve_task_m3(state):
    """Change Engineering Architecture Overview visibility to organization, disable editing."""
    p = find_pres(state, "Engineering Architecture Overview")
    p["shareSettings"]["visibility"] = "organization"
    p["shareSettings"]["allowEditing"] = False
    p["updatedAt"] = NOW


def solve_task_m4(state):
    """Add Elena Voronova to shared users of Accessibility Audit Results."""
    p = find_pres(state, "Accessibility Audit Results")
    ss = p["shareSettings"]
    if "user_008" not in ss["sharedWith"]:
        ss["sharedWith"].append("user_008")
    p["updatedAt"] = NOW


def solve_task_m5(state):
    """Resolve all unresolved comments on Q1 2026 Product Roadmap."""
    for c in state["comments"]:
        if c["presentationId"] == "pres_001":
            c["resolved"] = True


def solve_task_m6(state):
    """Create 'Design Review Q1' with creative theme and tags."""
    pid = next_pres_id(state)
    sid = next_slide_id(state)
    eid = next_elem_id(state)
    state["presentations"].append({
        "id": pid,
        "title": "Design Review Q1",
        "description": "",
        "createdAt": NOW,
        "updatedAt": NOW,
        "createdBy": state["currentUserId"],
        "theme": "creative",
        "tags": ["design", "review", "quarterly"],
        "starred": False,
        "status": "draft",
        "slideCount": 1,
        "shareSettings": {
            "visibility": "private",
            "allowComments": True,
            "allowEditing": False,
            "shareLink": "",
            "embedLink": "",
            "sharedWith": [state["currentUserId"]]
        }
    })
    state["slides"].append({
        "id": sid, "presentationId": pid, "order": 0, "layout": "title",
        "backgroundColor": "#ffffff",
        "transition": {"type": "none", "duration": 500},
        "speakerNotes": "",
        "elements": [{
            "id": eid, "type": "text", "x": 80, "y": 180, "width": 800, "height": 70,
            "rotation": 0, "opacity": 1, "locked": False,
            "content": "Design Review Q1",
            "shapeType": None, "fill": None, "stroke": None, "strokeWidth": 0,
            "cornerRadius": 0, "imageUrl": None, "imagePlaceholder": None,
            "style": {"fontFamily": "Inter", "fontSize": 48, "fontWeight": "bold",
                       "color": "#1a1a2e", "textAlign": "center", "italic": False,
                       "underline": False, "lineHeight": 1.2, "letterSpacing": -1,
                       "listType": "none"},
            "animation": {"type": "none", "duration": 300, "delay": 0, "order": 0}
        }]
    })


def solve_task_m7(state):
    """Share Product Demo — Enterprise Features with Marcus Rivera and Anika Patel."""
    p = find_pres(state, "Product Demo \u2014 Enterprise Features")
    ss = p["shareSettings"]
    for uid in ["user_002", "user_003"]:
        if uid not in ss["sharedWith"]:
            ss["sharedWith"].append(uid)
    p["updatedAt"] = NOW


def solve_task_m8(state):
    """Change Marketing Campaign visibility to organization, disable editing."""
    p = find_pres(state, "Marketing Campaign: Design Without Limits")
    p["shareSettings"]["visibility"] = "organization"
    p["shareSettings"]["allowEditing"] = False
    p["updatedAt"] = NOW


def solve_task_m9(state):
    """Remove Marcus Rivera from Q1 Product Roadmap, add Yuki Tanaka."""
    p = find_pres(state, "Q1 2026 Product Roadmap")
    sw = p["shareSettings"]["sharedWith"]
    if "user_002" in sw:
        sw.remove("user_002")
    if "user_005" not in sw:
        sw.append("user_005")
    p["updatedAt"] = NOW


def solve_task_m10(state):
    """Duplicate Team Retrospective — Sprint 47."""
    src = find_pres(state, "Team Retrospective \u2014 Sprint 47")
    import copy
    new_pres = copy.deepcopy(src)
    new_id = next_pres_id(state)
    new_pres["id"] = new_id
    new_pres["title"] = src["title"] + " (Copy)"
    new_pres["createdAt"] = NOW
    new_pres["updatedAt"] = NOW
    new_pres["status"] = "draft"
    new_pres["starred"] = False
    state["presentations"].append(new_pres)

    src_slides = [s for s in state["slides"] if s["presentationId"] == src["id"]]
    src_slides.sort(key=lambda s: s["order"])
    for slide in src_slides:
        new_slide = copy.deepcopy(slide)
        new_slide["id"] = next_slide_id(state)
        new_slide["presentationId"] = new_id
        for el in new_slide["elements"]:
            el["id"] = next_elem_id(state)
        state["slides"].append(new_slide)


def solve_task_m11(state):
    """Change Website Redesign Proposal visibility to team, add Elena Voronova."""
    p = find_pres(state, "Website Redesign Proposal \u2014 TechStartup.io")
    p["shareSettings"]["visibility"] = "team"
    ss = p["shareSettings"]
    if "user_008" not in ss["sharedWith"]:
        ss["sharedWith"].append("user_008")
    p["updatedAt"] = NOW


def solve_task_m12(state):
    """Add David Kim and Yuki Tanaka to Design Sprint Week 12 Recap."""
    p = find_pres(state, "Design Sprint Week 12 Recap")
    ss = p["shareSettings"]
    for uid in ["user_005", "user_007"]:
        if uid not in ss["sharedWith"]:
            ss["sharedWith"].append(uid)
    p["updatedAt"] = NOW


def solve_task_m13(state):
    """Set Onboarding Training Module visibility to team, enable comments and editing."""
    p = find_pres(state, "Onboarding Training Module")
    p["shareSettings"]["visibility"] = "team"
    p["shareSettings"]["allowComments"] = True
    p["shareSettings"]["allowEditing"] = True
    p["updatedAt"] = NOW


def solve_task_m14(state):
    """Create 'Investor Update March' with dark theme and tags."""
    pid = next_pres_id(state)
    sid = next_slide_id(state)
    eid = next_elem_id(state)
    state["presentations"].append({
        "id": pid,
        "title": "Investor Update March",
        "description": "",
        "createdAt": NOW,
        "updatedAt": NOW,
        "createdBy": state["currentUserId"],
        "theme": "dark",
        "tags": ["investors", "update"],
        "starred": False,
        "status": "draft",
        "slideCount": 1,
        "shareSettings": {
            "visibility": "private",
            "allowComments": True,
            "allowEditing": False,
            "shareLink": "",
            "embedLink": "",
            "sharedWith": [state["currentUserId"]]
        }
    })
    state["slides"].append({
        "id": sid, "presentationId": pid, "order": 0, "layout": "title",
        "backgroundColor": "#ffffff",
        "transition": {"type": "none", "duration": 500},
        "speakerNotes": "",
        "elements": [{
            "id": eid, "type": "text", "x": 80, "y": 180, "width": 800, "height": 70,
            "rotation": 0, "opacity": 1, "locked": False,
            "content": "Investor Update March",
            "shapeType": None, "fill": None, "stroke": None, "strokeWidth": 0,
            "cornerRadius": 0, "imageUrl": None, "imagePlaceholder": None,
            "style": {"fontFamily": "Inter", "fontSize": 48, "fontWeight": "bold",
                       "color": "#1a1a2e", "textAlign": "center", "italic": False,
                       "underline": False, "lineHeight": 1.2, "letterSpacing": -1,
                       "listType": "none"},
            "animation": {"type": "none", "duration": 300, "delay": 0, "order": 0}
        }]
    })


def solve_task_m15(state):
    """Archive Team Retrospective — Sprint 47 and Design Sprint Week 12 Recap."""
    for title in ["Team Retrospective \u2014 Sprint 47", "Design Sprint Week 12 Recap"]:
        p = find_pres(state, title)
        p["status"] = "archived"
        p["updatedAt"] = NOW


def solve_task_m16(state):
    """Star all presentations created by James O'Brien."""
    for p in state["presentations"]:
        if p["createdBy"] == "user_004":
            p["starred"] = True
            p["updatedAt"] = NOW


def solve_task_m17(state):
    """Share Q4 2025 Revenue Analysis with Priya Sharma-Krishnamurthy, change visibility to team."""
    p = find_pres(state, "Q4 2025 Revenue Analysis")
    ss = p["shareSettings"]
    if "user_006" not in ss["sharedWith"]:
        ss["sharedWith"].append("user_006")
    ss["visibility"] = "team"
    p["updatedAt"] = NOW


def solve_task_m18(state):
    """Enable comments on Series B Fundraising Pitch and Product Demo — Enterprise Features."""
    for title in ["Series B Fundraising Pitch", "Product Demo \u2014 Enterprise Features"]:
        p = find_pres(state, title)
        p["shareSettings"]["allowComments"] = True
        p["updatedAt"] = NOW


def solve_task_m19(state):
    """Delete the two comments on Website Redesign Proposal — TechStartup.io."""
    state["comments"] = [
        c for c in state["comments"]
        if c["presentationId"] != "pres_016"
    ]


def solve_task_m20(state):
    """Resolve the hero visual and KPIs comments on Marketing Campaign."""
    for c in state["comments"]:
        if c["presentationId"] == "pres_010":
            if "hero visual" in c["content"].lower() or "kpi" in c["content"].lower():
                c["resolved"] = True


# ═══════════════════════════════════════════════════════════════════════════════
# Solve functions — HARD
# ═══════════════════════════════════════════════════════════════════════════════

def solve_task_h1(state):
    """Star all of Sarah Chen's presentations that aren't already starred."""
    for p in state["presentations"]:
        if p["createdBy"] == "user_001":
            p["starred"] = True
            p["updatedAt"] = NOW


def solve_task_h2(state):
    """Unstar everything, then star the two presentations with fewest slides."""
    for p in state["presentations"]:
        p["starred"] = False
    # Two with fewest slides: pres_018 (5) and pres_014 (6)
    by_slides = sorted(state["presentations"], key=lambda p: p["slideCount"])
    for p in by_slides[:2]:
        p["starred"] = True
        p["updatedAt"] = NOW


def solve_task_h3(state):
    """Archive all presentations with private share visibility."""
    for p in state["presentations"]:
        if p["shareSettings"]["visibility"] == "private":
            p["status"] = "archived"
            p["updatedAt"] = NOW


def solve_task_h4(state):
    """Set share visibility of every presentation Elena Voronova has access to to organization."""
    elena_pres_ids = {"pres_002", "pres_005", "pres_007", "pres_010", "pres_013", "pres_014"}
    for p in state["presentations"]:
        if p["id"] in elena_pres_ids:
            p["shareSettings"]["visibility"] = "organization"
            p["updatedAt"] = NOW


def solve_task_h5(state):
    """Remove all viewers from shared users of every presentation."""
    viewer_ids = {"user_005", "user_007"}
    for p in state["presentations"]:
        sw = p["shareSettings"]["sharedWith"]
        p["shareSettings"]["sharedWith"] = [u for u in sw if u not in viewer_ids]


def solve_task_h6(state):
    """Create 'Team Showcase' with warm theme, share with all editors."""
    pid = next_pres_id(state)
    sid = next_slide_id(state)
    eid = next_elem_id(state)
    editor_ids = [u["id"] for u in state["users"] if u["role"] == "editor"]
    shared = list(set(["user_001"] + editor_ids))
    state["presentations"].append({
        "id": pid,
        "title": "Team Showcase",
        "description": "",
        "createdAt": NOW,
        "updatedAt": NOW,
        "createdBy": "user_001",
        "theme": "warm",
        "tags": ["team", "showcase"],
        "starred": False,
        "status": "draft",
        "slideCount": 1,
        "shareSettings": {
            "visibility": "private",
            "allowComments": True,
            "allowEditing": False,
            "shareLink": "",
            "embedLink": "",
            "sharedWith": shared
        }
    })
    state["slides"].append({
        "id": sid, "presentationId": pid, "order": 0, "layout": "title",
        "backgroundColor": "#ffffff",
        "transition": {"type": "none", "duration": 500},
        "speakerNotes": "",
        "elements": [{
            "id": eid, "type": "text", "x": 80, "y": 180, "width": 800, "height": 70,
            "rotation": 0, "opacity": 1, "locked": False,
            "content": "Team Showcase",
            "shapeType": None, "fill": None, "stroke": None, "strokeWidth": 0,
            "cornerRadius": 0, "imageUrl": None, "imagePlaceholder": None,
            "style": {"fontFamily": "Inter", "fontSize": 48, "fontWeight": "bold",
                       "color": "#1a1a2e", "textAlign": "center", "italic": False,
                       "underline": False, "lineHeight": 1.2, "letterSpacing": -1,
                       "listType": "none"},
            "animation": {"type": "none", "duration": 300, "delay": 0, "order": 0}
        }]
    })


def solve_task_h7(state):
    """Share Series B Fundraising Pitch with all editors and enable editing."""
    p = find_pres(state, "Series B Fundraising Pitch")
    editor_ids = [u["id"] for u in state["users"] if u["role"] == "editor"]
    ss = p["shareSettings"]
    for uid in editor_ids:
        if uid not in ss["sharedWith"]:
            ss["sharedWith"].append(uid)
    if "user_001" not in ss["sharedWith"]:
        ss["sharedWith"].append("user_001")
    ss["allowEditing"] = True
    p["updatedAt"] = NOW


def solve_task_h8(state):
    """Resolve every unresolved comment across all presentations."""
    for c in state["comments"]:
        c["resolved"] = True


def solve_task_h9(state):
    """Delete all resolved comments across all presentations."""
    state["comments"] = [c for c in state["comments"] if not c["resolved"]]


def solve_task_h10(state):
    """Change share visibility of all team-visible published presentations to organization."""
    for p in state["presentations"]:
        if p["status"] == "published" and p["shareSettings"]["visibility"] == "team":
            p["shareSettings"]["visibility"] = "organization"
            p["updatedAt"] = NOW


def solve_task_h11(state):
    """Share Q4 2025 Revenue Analysis with everyone, set org visibility, enable comments+editing."""
    p = find_pres(state, "Q4 2025 Revenue Analysis")
    all_user_ids = [u["id"] for u in state["users"]]
    p["shareSettings"]["sharedWith"] = all_user_ids
    p["shareSettings"]["visibility"] = "organization"
    p["shareSettings"]["allowComments"] = True
    p["shareSettings"]["allowEditing"] = True
    p["updatedAt"] = NOW


def solve_task_h12(state):
    """Create 'Sprint 48 Planning' with minimal theme, share with Sprint 47 retro members."""
    retro = find_pres(state, "Team Retrospective \u2014 Sprint 47")
    retro_members = list(retro["shareSettings"]["sharedWith"])

    pid = next_pres_id(state)
    sid = next_slide_id(state)
    eid = next_elem_id(state)

    shared = list(set(retro_members + ["user_001"]))
    state["presentations"].append({
        "id": pid,
        "title": "Sprint 48 Planning",
        "description": "",
        "createdAt": NOW,
        "updatedAt": NOW,
        "createdBy": "user_001",
        "theme": "minimal",
        "tags": ["sprint", "agile", "planning"],
        "starred": False,
        "status": "draft",
        "slideCount": 1,
        "shareSettings": {
            "visibility": "private",
            "allowComments": True,
            "allowEditing": False,
            "shareLink": "",
            "embedLink": "",
            "sharedWith": shared
        }
    })
    state["slides"].append({
        "id": sid, "presentationId": pid, "order": 0, "layout": "title",
        "backgroundColor": "#ffffff",
        "transition": {"type": "none", "duration": 500},
        "speakerNotes": "",
        "elements": [{
            "id": eid, "type": "text", "x": 80, "y": 180, "width": 800, "height": 70,
            "rotation": 0, "opacity": 1, "locked": False,
            "content": "Sprint 48 Planning",
            "shapeType": None, "fill": None, "stroke": None, "strokeWidth": 0,
            "cornerRadius": 0, "imageUrl": None, "imagePlaceholder": None,
            "style": {"fontFamily": "Inter", "fontSize": 48, "fontWeight": "bold",
                       "color": "#1a1a2e", "textAlign": "center", "italic": False,
                       "underline": False, "lineHeight": 1.2, "letterSpacing": -1,
                       "listType": "none"},
            "animation": {"type": "none", "duration": 300, "delay": 0, "order": 0}
        }]
    })


def solve_task_h13(state):
    """Delete all comments made by Sarah Chen across all presentations."""
    state["comments"] = [c for c in state["comments"] if c["authorId"] != "user_001"]


def solve_task_h14(state):
    """Star every presentation that has at least one unresolved comment."""
    pres_with_unresolved = set()
    for c in state["comments"]:
        if not c["resolved"]:
            pres_with_unresolved.add(c["presentationId"])
    for p in state["presentations"]:
        if p["id"] in pres_with_unresolved:
            p["starred"] = True
            p["updatedAt"] = NOW


def solve_task_h15(state):
    """Archive all presentations whose creator has a viewer role."""
    viewer_ids = {u["id"] for u in state["users"] if u["role"] == "viewer"}
    for p in state["presentations"]:
        if p["createdBy"] in viewer_ids:
            p["status"] = "archived"
            p["updatedAt"] = NOW


def solve_task_h16(state):
    """Give Q1 Roadmap shared users access to the fundraising pitch, set pitch to team visibility."""
    roadmap = find_pres(state, "Q1 2026 Product Roadmap")
    pitch = find_pres(state, "Series B Fundraising Pitch")
    roadmap_members = roadmap["shareSettings"]["sharedWith"]
    ss = pitch["shareSettings"]
    for uid in roadmap_members:
        if uid not in ss["sharedWith"]:
            ss["sharedWith"].append(uid)
    ss["visibility"] = "team"
    pitch["updatedAt"] = NOW


def solve_task_h17(state):
    """Create 'Design System Audit', share with Mobile Design System Components members."""
    mobile_ds = find_pres(state, "Mobile Design System Components")
    ds_members = list(mobile_ds["shareSettings"]["sharedWith"])

    pid = next_pres_id(state)
    sid = next_slide_id(state)
    eid = next_elem_id(state)

    shared = list(set(ds_members + ["user_001"]))
    state["presentations"].append({
        "id": pid,
        "title": "Design System Audit",
        "description": "",
        "createdAt": NOW,
        "updatedAt": NOW,
        "createdBy": "user_001",
        "theme": "creative",
        "tags": ["design-system", "audit"],
        "starred": False,
        "status": "draft",
        "slideCount": 1,
        "shareSettings": {
            "visibility": "private",
            "allowComments": True,
            "allowEditing": False,
            "shareLink": "",
            "embedLink": "",
            "sharedWith": shared
        }
    })
    state["slides"].append({
        "id": sid, "presentationId": pid, "order": 0, "layout": "title",
        "backgroundColor": "#ffffff",
        "transition": {"type": "none", "duration": 500},
        "speakerNotes": "",
        "elements": [{
            "id": eid, "type": "text", "x": 80, "y": 180, "width": 800, "height": 70,
            "rotation": 0, "opacity": 1, "locked": False,
            "content": "Design System Audit",
            "shapeType": None, "fill": None, "stroke": None, "strokeWidth": 0,
            "cornerRadius": 0, "imageUrl": None, "imagePlaceholder": None,
            "style": {"fontFamily": "Inter", "fontSize": 48, "fontWeight": "bold",
                       "color": "#1a1a2e", "textAlign": "center", "italic": False,
                       "underline": False, "lineHeight": 1.2, "letterSpacing": -1,
                       "listType": "none"},
            "animation": {"type": "none", "duration": 300, "delay": 0, "order": 0}
        }]
    })


def solve_task_h18(state):
    """Remove all shared users from TechVentures Redesign except the creator."""
    p = find_pres(state, "Client Proposal \u2014 TechVentures Redesign")
    p["shareSettings"]["sharedWith"] = [p["createdBy"]]
    p["updatedAt"] = NOW


def solve_task_h19(state):
    """Enable comments and editing on all org-visibility presentations."""
    for p in state["presentations"]:
        if p["shareSettings"]["visibility"] == "organization":
            p["shareSettings"]["allowComments"] = True
            p["shareSettings"]["allowEditing"] = True
            p["updatedAt"] = NOW


def solve_task_h20(state):
    """Delete all comments on User Research Findings and disable comments."""
    state["comments"] = [
        c for c in state["comments"]
        if c["presentationId"] != "pres_004"
    ]
    p = find_pres(state, "User Research Findings \u2014 Mobile App")
    p["shareSettings"]["allowComments"] = False
    p["updatedAt"] = NOW


# ═══════════════════════════════════════════════════════════════════════════════
# Solver registry
# ═══════════════════════════════════════════════════════════════════════════════

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


# ═══════════════════════════════════════════════════════════════════════════════
# Infrastructure
# ═══════════════════════════════════════════════════════════════════════════════

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


def find_free_port(start=9500):
    port = start
    while port < start + 200:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("", port))
                return port
            except OSError:
                port += 1
    raise RuntimeError(f"No free port found in range {start}-{start + 200}")


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


def seed_server(server_url, seed_state):
    resp = requests.put(
        f"{server_url}/api/state",
        json=seed_state,
        headers={"Content-Type": "application/json"},
    )
    if resp.status_code != 200:
        raise RuntimeError(f"Failed to seed server: HTTP {resp.status_code}")


def load_tasks():
    with open(TASKS_FILE) as f:
        return json.load(f)


def load_verifier(verify_path):
    full_path = APP_DIR / verify_path
    spec = importlib.util.spec_from_file_location("verifier", str(full_path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.verify


# ═══════════════════════════════════════════════════════════════════════════════
# Task runner
# ═══════════════════════════════════════════════════════════════════════════════

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
            return task_id, False, f"Could not read state: HTTP {resp.status_code}"
        state = resp.json()

        # 3. Apply solve
        solver(state)

        # 4. Write solved state
        resp = requests.put(
            f"{server_url}/api/state",
            json=state,
            headers={"Content-Type": "application/json"},
        )
        if resp.status_code != 200:
            return task_id, False, f"Could not write state: HTTP {resp.status_code}"

        # 5. Run verifier
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


def main():
    parser = argparse.ArgumentParser(description="Figma Slides real-task sanity check")
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
