#!/usr/bin/env python3
"""
Sanity check for Figma Slides function-test tasks.

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

const seed = getSeedData();
process.stdout.write(JSON.stringify(seed));
"""


# ── helpers ──────────────────────────────────────────────────────────

def find_presentation(state, title):
    """Find a presentation by exact title."""
    for p in state["presentations"]:
        if p["title"] == title:
            return p
    raise ValueError(f"Presentation not found: {title!r}")


def find_slides_for_pres(state, pres_id):
    """Get slides for a presentation sorted by order."""
    slides = [s for s in state["slides"] if s["presentationId"] == pres_id]
    return sorted(slides, key=lambda s: s["order"])


def find_comment_by_content(state, pres_title, content_substr):
    """Find a comment by presentation title and content substring."""
    pres = find_presentation(state, pres_title)
    for c in state["comments"]:
        if c["presentationId"] == pres["id"] and content_substr in c["content"]:
            return c
    raise ValueError(f"Comment containing {content_substr!r} not found in {pres_title!r}")


def next_pres_id(state):
    """Get next presentation ID and increment counter."""
    n = state.get("_nextPresentationId", 19)
    state["_nextPresentationId"] = n + 1
    return f"pres_{str(n).zfill(3)}"


def next_slide_id(state):
    """Get next slide ID and increment counter."""
    n = state.get("_nextSlideId", 500)
    state["_nextSlideId"] = n + 1
    return f"slide_{str(n).zfill(5)}"


def next_element_id(state):
    """Get next element ID and increment counter."""
    n = state.get("_nextElementId", 2000)
    state["_nextElementId"] = n + 1
    return f"elem_{str(n).zfill(5)}"


def next_comment_id(state):
    """Get next comment ID and increment counter."""
    n = state.get("_nextCommentId", 41)
    state["_nextCommentId"] = n + 1
    return f"cmt_{str(n).zfill(3)}"


def next_reply_id(state):
    """Get next reply ID and increment counter."""
    n = state.get("_nextReplyId", 25)
    state["_nextReplyId"] = n + 1
    return f"reply_{str(n).zfill(3)}"


def next_template_id(state):
    """Get next template ID and increment counter."""
    n = state.get("_nextTemplateId", 13)
    state["_nextTemplateId"] = n + 1
    return f"tmpl_{str(n).zfill(3)}"


NOW = "2026-03-18T12:00:00Z"


# ── solve functions ──────────────────────────────────────────────────

def _create_presentation(state, title, description="", theme="minimal", tags=None):
    """Helper to create a new presentation with default slide."""
    pid = next_pres_id(state)
    sid = next_slide_id(state)
    eid = next_element_id(state)
    state["presentations"].append({
        "id": pid,
        "title": title,
        "description": description,
        "createdAt": NOW,
        "updatedAt": NOW,
        "createdBy": state["currentUserId"],
        "theme": theme,
        "tags": tags or [],
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
            "content": title,
            "shapeType": None, "fill": None, "stroke": None, "strokeWidth": 0,
            "cornerRadius": 0, "imageUrl": None, "imagePlaceholder": None,
            "style": {"fontFamily": "Inter", "fontSize": 48, "fontWeight": "bold",
                      "color": "#1a1a2e", "textAlign": "center", "italic": False,
                      "underline": False, "lineHeight": 1.2, "letterSpacing": -1,
                      "listType": "none"},
            "animation": {"type": "none", "duration": 300, "delay": 0, "order": 0}
        }]
    })


def solve_task_1(state):
    """Create presentation 'AI Strategy 2026' with description."""
    _create_presentation(state, "AI Strategy 2026", description="Company-wide AI adoption plan")


def solve_task_2(state):
    """Create presentation 'Budget Review Q2' with tags and corporate theme."""
    _create_presentation(state, "Budget Review Q2", theme="corporate", tags=["finance", "quarterly"])


def solve_task_3(state):
    """Delete 'Competitor Analysis Dashboard'."""
    pres = find_presentation(state, "Competitor Analysis Dashboard")
    pid = pres["id"]
    state["presentations"] = [p for p in state["presentations"] if p["id"] != pid]
    state["slides"] = [s for s in state["slides"] if s["presentationId"] != pid]
    state["comments"] = [c for c in state["comments"] if c["presentationId"] != pid]


def solve_task_4(state):
    """Duplicate 'Design Sprint Week 12 Recap'."""
    src = find_presentation(state, "Design Sprint Week 12 Recap")
    new_pid = next_pres_id(state)
    copy = deepcopy(src)
    copy["id"] = new_pid
    copy["title"] = src["title"] + " (Copy)"
    copy["createdAt"] = NOW
    copy["updatedAt"] = NOW
    copy["status"] = "draft"
    copy["starred"] = False
    state["presentations"].append(copy)

    src_slides = find_slides_for_pres(state, src["id"])
    for slide in src_slides:
        new_slide = deepcopy(slide)
        new_slide["id"] = next_slide_id(state)
        new_slide["presentationId"] = new_pid
        for el in new_slide["elements"]:
            el["id"] = next_element_id(state)
        state["slides"].append(new_slide)


def solve_task_5(state):
    """Star 'Engineering Architecture Overview'."""
    pres = find_presentation(state, "Engineering Architecture Overview")
    pres["starred"] = True


def solve_task_6(state):
    """Unstar 'Q1 2026 Product Roadmap'."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    pres["starred"] = False


def solve_task_7(state):
    """Change status of 'Design Workshop Materials' to published."""
    pres = find_presentation(state, "Design Workshop Materials")
    pres["status"] = "published"


def solve_task_8(state):
    """Change status of 'Q4 2025 Revenue Analysis' to archived."""
    pres = find_presentation(state, "Q4 2025 Revenue Analysis")
    pres["status"] = "archived"


def solve_task_9(state):
    """Change visibility of 'Brand Identity Guidelines v2.0' to public."""
    pres = find_presentation(state, "Brand Identity Guidelines v2.0")
    pres["shareSettings"]["visibility"] = "public"


def solve_task_10(state):
    """Disable commenting on 'Annual Company All-Hands 2026'."""
    pres = find_presentation(state, "Annual Company All-Hands 2026")
    pres["shareSettings"]["allowComments"] = False


def solve_task_11(state):
    """Enable editing on 'Q1 2026 Product Roadmap'."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    pres["shareSettings"]["allowEditing"] = True


def solve_task_12(state):
    """Share 'Series B Fundraising Pitch' with Marcus Rivera (user_002)."""
    pres = find_presentation(state, "Series B Fundraising Pitch")
    if "user_002" not in pres["shareSettings"]["sharedWith"]:
        pres["shareSettings"]["sharedWith"].append("user_002")


def solve_task_13(state):
    """Remove Anika Patel from 'Client Proposal — TechVentures Redesign'."""
    pres = find_presentation(state, "Client Proposal \u2014 TechVentures Redesign")
    pres["shareSettings"]["sharedWith"] = [
        u for u in pres["shareSettings"]["sharedWith"] if u != "user_003"
    ]


def solve_task_14(state):
    """Change visibility to team and enable commenting on 'Onboarding Training Module'."""
    pres = find_presentation(state, "Onboarding Training Module")
    pres["shareSettings"]["visibility"] = "team"
    pres["shareSettings"]["allowComments"] = True


def solve_task_15(state):
    """Add a new slide to 'Design Sprint Week 12 Recap'."""
    pres = find_presentation(state, "Design Sprint Week 12 Recap")
    pid = pres["id"]
    slides = find_slides_for_pres(state, pid)
    new_order = len(slides)
    sid = next_slide_id(state)
    state["slides"].append({
        "id": sid,
        "presentationId": pid,
        "order": new_order,
        "layout": "blank",
        "backgroundColor": "#ffffff",
        "transition": {"type": "none", "duration": 500},
        "speakerNotes": "",
        "elements": []
    })
    pres["slideCount"] = new_order + 1


def solve_task_16(state):
    """Delete last slide of 'Team Retrospective — Sprint 47'."""
    pres = find_presentation(state, "Team Retrospective \u2014 Sprint 47")
    pid = pres["id"]
    slides = find_slides_for_pres(state, pid)
    last_slide = slides[-1]
    state["slides"] = [s for s in state["slides"] if s["id"] != last_slide["id"]]
    state["comments"] = [c for c in state["comments"] if c["slideId"] != last_slide["id"]]
    pres["slideCount"] = len(slides) - 1


def solve_task_17(state):
    """Duplicate first slide of 'Q1 2026 Product Roadmap'."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    pid = pres["id"]
    slides = find_slides_for_pres(state, pid)
    first_slide = slides[0]

    # Shift all slides after order 0
    for s in slides:
        if s["order"] > first_slide["order"]:
            s["order"] += 1

    new_slide = deepcopy(first_slide)
    new_slide["id"] = next_slide_id(state)
    new_slide["order"] = first_slide["order"] + 1
    for el in new_slide["elements"]:
        el["id"] = next_element_id(state)
    state["slides"].append(new_slide)
    pres["slideCount"] = len(find_slides_for_pres(state, pid))


def solve_task_18(state):
    """Change layout of 2nd slide (order 1) of pres_001 to two-column."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    slides[1]["layout"] = "two-column"


def solve_task_19(state):
    """Change bg color of first slide of pres_001 to #7B61FF."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    slides[0]["backgroundColor"] = "#7B61FF"


def solve_task_20(state):
    """Update speaker notes of 3rd slide (order 2) of pres_001."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    slides[2]["speakerNotes"] = "Highlight the three major product launches and their specific impact metrics."


def solve_task_21(state):
    """Set transition of 2nd slide (order 1) of pres_001 to dissolve."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    slides[1]["transition"]["type"] = "dissolve"


def solve_task_22(state):
    """Set transition of 6th slide (order 5) of pres_001 to push/800."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    slides[5]["transition"] = {"type": "push", "duration": 800}


def solve_task_23(state):
    """Change title of 3rd slide to 'Q1 Major Launches'."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    slides[2]["elements"][0]["content"] = "Q1 Major Launches"


def solve_task_24(state):
    """Change font family of title on first slide of Q1 Roadmap to Poppins."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    slides[0]["elements"][0]["style"]["fontFamily"] = "Poppins"


def solve_task_25(state):
    """Change font size of title on 3rd slide of pres_001 to 40."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    slides[2]["elements"][0]["style"]["fontSize"] = 40


def solve_task_26(state):
    """Change font weight of subtitle on 1st slide of pres_001 to 600."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    slides[0]["elements"][1]["style"]["fontWeight"] = "600"


def solve_task_27(state):
    """Change text color of title on 9th slide (order 8) of pres_001 to #F24822."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    slides[8]["elements"][0]["style"]["color"] = "#F24822"


def solve_task_28(state):
    """Toggle italic on subtitle of 1st slide of pres_001."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    slides[0]["elements"][1]["style"]["italic"] = True


def solve_task_29(state):
    """Toggle underline on title of 3rd slide of pres_001."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    slides[2]["elements"][0]["style"]["underline"] = True


def solve_task_30(state):
    """Change text alignment of subtitle on 1st slide of pres_001 to left."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    slides[0]["elements"][1]["style"]["textAlign"] = "left"


def solve_task_31(state):
    """Change list type of content element on 3rd slide to numbered."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    slides[2]["elements"][1]["style"]["listType"] = "numbered"


def solve_task_32(state):
    """Lock title element on 2nd slide of pres_001."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    slides[1]["elements"][0]["locked"] = True


def solve_task_33(state):
    """Change letter spacing of title on 3rd slide of pres_001 to 2."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    slides[2]["elements"][0]["style"]["letterSpacing"] = 2


def solve_task_34(state):
    """Change line height of title on first slide of pres_001 to 2.0."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    slides[0]["elements"][0]["style"]["lineHeight"] = 2.0


def solve_task_35(state):
    """Change fill of first rectangle on 4th slide (order 3) to #0D99FF."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    slide = slides[3]
    for el in slide["elements"]:
        if el.get("type") == "shape" and el.get("shapeType") == "rectangle":
            el["fill"] = "#0D99FF"
            break


def solve_task_36(state):
    """Change stroke of line shape on 2nd slide (order 1) to #14AE5C."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    slide = slides[1]
    for el in slide["elements"]:
        if el.get("type") == "shape":
            el["stroke"] = "#14AE5C"
            break


def solve_task_37(state):
    """Change shape type of rectangle on 5th slide (order 4) to circle."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    slide = slides[4]
    for el in slide["elements"]:
        if el.get("type") == "shape" and el.get("shapeType") == "rectangle":
            el["shapeType"] = "circle"
            break


def solve_task_38(state):
    """Set opacity of title on first slide of pres_001 to 0.5."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    slides[0]["elements"][0]["opacity"] = 0.5


def solve_task_39(state):
    """Set rotation of title on first slide of pres_001 to 45."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    slides[0]["elements"][0]["rotation"] = 45


def solve_task_40(state):
    """Delete the line shape (3rd element) from first slide of pres_001."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    slide = slides[0]
    slide["elements"] = [
        el for el in slide["elements"]
        if not (el.get("type") == "shape" and el.get("shapeType") == "line")
    ]


def solve_task_41(state):
    """Add a text element to first slide of pres_001."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    slide = slides[0]
    eid = next_element_id(state)
    slide["elements"].append({
        "id": eid, "type": "text", "x": 100, "y": 100, "width": 200, "height": 60,
        "rotation": 0, "opacity": 1, "locked": False,
        "content": "Text",
        "shapeType": None, "fill": None, "stroke": None, "strokeWidth": 0,
        "cornerRadius": 0, "imageUrl": None, "imagePlaceholder": None,
        "style": {"fontFamily": "Inter", "fontSize": 20, "fontWeight": "normal",
                  "color": "#2c2c2c", "textAlign": "left", "italic": False,
                  "underline": False, "lineHeight": 1.4, "letterSpacing": 0,
                  "listType": "none"},
        "animation": {"type": "none", "duration": 300, "delay": 0, "order": 0}
    })


def solve_task_42(state):
    """Add a rectangle shape to first slide of pres_001."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    slide = slides[0]
    eid = next_element_id(state)
    slide["elements"].append({
        "id": eid, "type": "shape", "x": 100, "y": 100, "width": 200, "height": 200,
        "rotation": 0, "opacity": 1, "locked": False,
        "content": None, "shapeType": "rectangle",
        "fill": "#4A90D9", "stroke": "#333333", "strokeWidth": 2,
        "cornerRadius": 0, "imageUrl": None, "imagePlaceholder": None,
        "style": None,
        "animation": {"type": "none", "duration": 300, "delay": 0, "order": 0}
    })


def solve_task_43(state):
    """Add an image element to first slide of pres_001."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    slide = slides[0]
    eid = next_element_id(state)
    slide["elements"].append({
        "id": eid, "type": "image", "x": 100, "y": 100, "width": 400, "height": 300,
        "rotation": 0, "opacity": 1, "locked": False,
        "content": None, "shapeType": None,
        "fill": None, "stroke": None, "strokeWidth": 0,
        "cornerRadius": 0, "imageUrl": None, "imagePlaceholder": "#e0e0e0",
        "style": None,
        "animation": {"type": "none", "duration": 300, "delay": 0, "order": 0}
    })


def solve_task_44(state):
    """Set animation of title on 3rd slide of pres_001 to fade-in."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    slides[2]["elements"][0]["animation"]["type"] = "fade-in"


def solve_task_45(state):
    """Set animation on title of 9th slide (order 8) to bounce-in/500/200."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    anim = slides[8]["elements"][0]["animation"]
    anim["type"] = "bounce-in"
    anim["duration"] = 500
    anim["delay"] = 200


def solve_task_46(state):
    """Add comment 'Great progress on the roadmap!' to first slide of pres_001."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    slide = slides[0]
    cid = next_comment_id(state)
    state["comments"].append({
        "id": cid,
        "presentationId": pres["id"],
        "slideId": slide["id"],
        "elementId": None,
        "authorId": state["currentUserId"],
        "content": "Great progress on the roadmap!",
        "createdAt": NOW,
        "resolved": False,
        "replies": []
    })


def solve_task_47(state):
    """Reply to the chart visualization comment on pres_001."""
    cmt = find_comment_by_content(state, "Q1 2026 Product Roadmap", "chart visualization")
    rid = next_reply_id(state)
    cmt["replies"].append({
        "id": rid,
        "authorId": state["currentUserId"],
        "content": "I agree, a bar chart would work best for this data.",
        "createdAt": NOW
    })


def solve_task_48(state):
    """Resolve the Canva comment on pres_001."""
    cmt = find_comment_by_content(state, "Q1 2026 Product Roadmap", "Canva")
    cmt["resolved"] = True


def solve_task_49(state):
    """Unresolve the finance comment on pres_003."""
    cmt = find_comment_by_content(state, "Series B Fundraising Pitch", "Finance team confirmed")
    cmt["resolved"] = False


def solve_task_50(state):
    """Delete 'Love the design!' comment from pres_001."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    state["comments"] = [
        c for c in state["comments"]
        if not (c["presentationId"] == pres["id"] and "Love the design" in c["content"])
    ]


def solve_task_51(state):
    """Resolve logo clear space comment on pres_002."""
    cmt = find_comment_by_content(state, "Brand Identity Guidelines v2.0", "logo clear space")
    cmt["resolved"] = True


def solve_task_52(state):
    """Save slide order 8 of pres_001 as template 'Three Cards Layout'."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    slide = slides[8]
    tid = next_template_id(state)
    elements_copy = deepcopy(slide["elements"])
    for el in elements_copy:
        if "id" in el:
            del el["id"]
    state["templates"].append({
        "id": tid,
        "name": "Three Cards Layout",
        "category": "custom",
        "layout": slide["layout"],
        "description": "Custom template saved from slide",
        "previewColor": slide["backgroundColor"] if slide["backgroundColor"] != "#ffffff" else "#7B61FF",
        "elements": elements_copy
    })


def solve_task_53(state):
    """Save slide order 3 of pres_001 as template 'Metrics Dashboard'."""
    pres = find_presentation(state, "Q1 2026 Product Roadmap")
    slides = find_slides_for_pres(state, pres["id"])
    slide = slides[3]
    tid = next_template_id(state)
    elements_copy = deepcopy(slide["elements"])
    for el in elements_copy:
        if "id" in el:
            del el["id"]
    state["templates"].append({
        "id": tid,
        "name": "Metrics Dashboard",
        "category": "custom",
        "layout": slide["layout"],
        "description": "Custom template saved from slide",
        "previewColor": slide["backgroundColor"] if slide["backgroundColor"] != "#ffffff" else "#7B61FF",
        "elements": elements_copy
    })


def solve_task_54(state):
    """Share pres_005 with the creator of pres_002 (user_006)."""
    creator_pres = find_presentation(state, "Brand Identity Guidelines v2.0")
    creator_id = creator_pres["createdBy"]
    target_pres = find_presentation(state, "Engineering Architecture Overview")
    if creator_id not in target_pres["shareSettings"]["sharedWith"]:
        target_pres["shareSettings"]["sharedWith"].append(creator_id)


def solve_task_55(state):
    """Star all draft presentations."""
    for p in state["presentations"]:
        if p["status"] == "draft":
            p["starred"] = True


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
    while port < start + 100:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("", port))
                return port
            except OSError:
                port += 1
    raise RuntimeError(f"No free port found in range {start}-{start+100}")


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
    parser = argparse.ArgumentParser(description="Figma Slides function-task sanity check")
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
