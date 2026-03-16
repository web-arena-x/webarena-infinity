#!/usr/bin/env python3
"""
Sanity check for Figma Text & Typography real-task verifiers.

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

NOW = "2026-03-08T00:00:00Z"

# JS snippet to evaluate data.js and emit the seed state as JSON
_SEED_STATE_JS = """
const fs = require('fs');
const vm = require('vm');
const code = fs.readFileSync(process.argv[1], 'utf8');
vm.runInThisContext(code);

const state = {
    _seedVersion: SEED_DATA_VERSION,
    textLayers: JSON.parse(JSON.stringify(TEXT_LAYERS)),
    textStyles: JSON.parse(JSON.stringify(TEXT_STYLES)),
    fontFamilies: JSON.parse(JSON.stringify(FONT_FAMILIES)),
    preferences: JSON.parse(JSON.stringify(PREFERENCES)),
    fileInfo: JSON.parse(JSON.stringify(FILE_INFO)),
    currentUser: JSON.parse(JSON.stringify(CURRENT_USER)),
    _nextTextLayerId: 100,
    _nextTextStyleId: 100,
    _nextLinkId: 100,
};
process.stdout.write(JSON.stringify(state));
"""


# -- helpers ----------------------------------------------------------------

def find_layer(state, name):
    """Find a text layer by name. Raises if not found."""
    for l in state["textLayers"]:
        if l["name"] == name:
            return l
    raise ValueError(f"Text layer not found: {name!r}")


def find_style(state, name):
    """Find a text style by name. Raises if not found."""
    for s in state["textStyles"]:
        if s["name"] == name:
            return s
    raise ValueError(f"Text style not found: {name!r}")


def apply_style_to_layer(layer, style):
    """Copy all style properties to a layer (mirrors AppState.applyTextStyle)."""
    layer["textStyleId"] = style["id"]
    layer["fontFamily"] = style["fontFamily"]
    layer["fontStyle"] = style["fontStyle"]
    layer["fontSize"] = style["fontSize"]
    layer["lineHeight"] = deepcopy(style["lineHeight"])
    layer["letterSpacing"] = deepcopy(style["letterSpacing"])
    layer["paragraphSpacing"] = style["paragraphSpacing"]
    layer["paragraphIndent"] = style["paragraphIndent"]
    layer["textDecoration"] = style["textDecoration"]
    layer["letterCase"] = style["letterCase"]
    layer["listStyle"] = style["listStyle"]
    layer["openTypeFeatures"] = deepcopy(style["openTypeFeatures"])


def propagate_style_to_layers(state, style):
    """Update all layers using a given style (mirrors AppState.updateTextStyle)."""
    for layer in state["textLayers"]:
        if layer.get("textStyleId") == style["id"]:
            layer["fontFamily"] = style["fontFamily"]
            layer["fontStyle"] = style["fontStyle"]
            layer["fontSize"] = style["fontSize"]
            layer["lineHeight"] = deepcopy(style["lineHeight"])
            layer["letterSpacing"] = deepcopy(style["letterSpacing"])
            layer["paragraphSpacing"] = style["paragraphSpacing"]
            layer["paragraphIndent"] = style["paragraphIndent"]
            layer["textDecoration"] = style["textDecoration"]
            layer["letterCase"] = style["letterCase"]
            layer["listStyle"] = style["listStyle"]
            layer["openTypeFeatures"] = deepcopy(style["openTypeFeatures"])


# -- solve functions (easy) -------------------------------------------------

def solve_task_e1(state):
    """Hide the Copyright Notice text layer."""
    find_layer(state, "Copyright Notice")["visible"] = False


def solve_task_e2(state):
    """Lock the Page Title layer."""
    find_layer(state, "Page Title")["locked"] = True


def solve_task_e3(state):
    """Center-align the Section Header."""
    find_layer(state, "Section Header")["horizontalAlign"] = "center"


def solve_task_e4(state):
    """Turn off smart quotes."""
    state["preferences"]["smartQuotes"] = False


def solve_task_e5(state):
    """Remove the strikethrough from the deleted text."""
    find_layer(state, "Strikethrough Example")["textDecoration"] = "none"


def solve_task_e6(state):
    """Change the spelling language to French."""
    state["preferences"]["spellingLanguage"] = "French"


def solve_task_e7(state):
    """Switch the Pricing Tiers to a bulleted list."""
    find_layer(state, "Pricing Tiers")["listStyle"] = "bulleted"


def solve_task_e8(state):
    """Underline the Page Title."""
    find_layer(state, "Page Title")["textDecoration"] = "underline"


def solve_task_e9(state):
    """Disable snap to grid."""
    state["preferences"]["snapToGrid"] = False


def solve_task_e10(state):
    """Remove the uppercase formatting from the Call to Action button text."""
    find_layer(state, "Call to Action")["letterCase"] = "none"


def solve_task_e11(state):
    """Turn off font preview in the settings."""
    state["preferences"]["showFontPreview"] = False


def solve_task_e12(state):
    """Turn off vertical trim on the Release Notes Header."""
    find_layer(state, "Release Notes Header")["verticalTrim"] = False


def solve_task_e13(state):
    """Delete the Strikethrough Example layer."""
    state["textLayers"] = [l for l in state["textLayers"] if l["name"] != "Strikethrough Example"]


def solve_task_e14(state):
    """Change the default font size to 14."""
    state["preferences"]["defaultFontSize"] = 14


def solve_task_e15(state):
    """Detach the style from the Section Header."""
    find_layer(state, "Section Header")["textStyleId"] = None


def solve_task_e16(state):
    """Switch the Arabic Welcome text direction to left-to-right."""
    find_layer(state, "Arabic Welcome")["textDirection"] = "ltr"


def solve_task_e17(state):
    """Disable truncation on the Truncated Preview."""
    find_layer(state, "Truncated Preview")["truncation"] = {"enabled": False, "maxLines": None}


def solve_task_e18(state):
    """Disable smart symbols."""
    state["preferences"]["smartSymbols"] = False


def solve_task_e19(state):
    """Set the nudge amount to 4 pixels."""
    state["preferences"]["nudgeAmount"] = 4


def solve_task_e20(state):
    """Convert the Step Instructions to a bulleted list."""
    find_layer(state, "Step Instructions")["listStyle"] = "bulleted"


# -- solve functions (medium) -----------------------------------------------

def solve_task_m1(state):
    """Rename Body Text to 'Introduction' and justify-align it."""
    layer = find_layer(state, "Body Text")
    layer["name"] = "Introduction"
    layer["horizontalAlign"] = "justify"


def solve_task_m2(state):
    """Switch the Page Title font to Montserrat Bold."""
    layer = find_layer(state, "Page Title")
    layer["fontFamily"] = "Montserrat"
    layer["fontStyle"] = "Bold"
    # Montserrat is variable: wght (100-900, default 400), ital (0-1, default 0)
    layer["variableAxes"] = {"wght": 400, "ital": 0}


def solve_task_m3(state):
    """Make the Feature List numbered and increase its list spacing to 8."""
    layer = find_layer(state, "Feature List")
    layer["listStyle"] = "numbered"
    layer["listSpacing"] = 8


def solve_task_m4(state):
    """Create a new text layer with the text 'Terms and Conditions'."""
    next_id = state.get("_nextTextLayerId", 100)
    prefs = state["preferences"]
    layer = {
        "id": f"tl_{str(next_id).zfill(3)}",
        "name": "Terms and Conditions",
        "content": "Terms and Conditions",
        "fontFamily": prefs["defaultFontFamily"],
        "fontStyle": prefs["defaultFontStyle"],
        "fontSize": prefs["defaultFontSize"],
        "lineHeight": deepcopy(prefs["defaultLineHeight"]),
        "letterSpacing": deepcopy(prefs["defaultLetterSpacing"]),
        "paragraphSpacing": 0,
        "paragraphIndent": 0,
        "horizontalAlign": prefs["defaultHorizontalAlign"],
        "verticalAlign": "top",
        "textDecoration": "none",
        "letterCase": "none",
        "textDirection": prefs["defaultTextDirection"],
        "resizing": "auto-width",
        "truncation": {"enabled": False, "maxLines": None},
        "listStyle": "none",
        "listSpacing": 0,
        "hangingPunctuation": False,
        "hangingList": False,
        "verticalTrim": False,
        "links": [],
        "openTypeFeatures": {"liga": True, "kern": True},
        "textStyleId": None,
        "variableAxes": {},
        "width": None,
        "height": None,
        "x": 40,
        "y": 40 + len(state["textLayers"]) * 40,
        "locked": False,
        "visible": True,
        "createdAt": NOW,
        "updatedAt": NOW,
    }
    state["textLayers"].append(layer)
    state["_nextTextLayerId"] = next_id + 1


def solve_task_m5(state):
    """Switch the Code Sample font to Fira Code."""
    layer = find_layer(state, "Code Sample")
    layer["fontFamily"] = "Fira Code"
    # Fira Code is variable: wght (300-700, default 400)
    layer["variableAxes"] = {"wght": 400}


def solve_task_m6(state):
    """Set the Body Text paragraph spacing to 24 and indent to 20."""
    layer = find_layer(state, "Body Text")
    layer["paragraphSpacing"] = 24
    layer["paragraphIndent"] = 20


def solve_task_m7(state):
    """Change the default font to Roboto and the default size to 14."""
    state["preferences"]["defaultFontFamily"] = "Roboto"
    state["preferences"]["defaultFontSize"] = 14


def solve_task_m8(state):
    """Apply the Heading/H3 style to the Release Notes Header."""
    layer = find_layer(state, "Release Notes Header")
    style = find_style(state, "Heading/H3")
    apply_style_to_layer(layer, style)


def solve_task_m9(state):
    """Increase the truncation limit on the Truncated Preview to 5 lines."""
    find_layer(state, "Truncated Preview")["truncation"] = {"enabled": True, "maxLines": 5}


def solve_task_m10(state):
    """Switch the Indented Quote font to Georgia and turn off its hanging punctuation."""
    layer = find_layer(state, "Indented Quote")
    layer["fontFamily"] = "Georgia"
    layer["hangingPunctuation"] = False
    # Georgia is not variable
    layer["variableAxes"] = {}


def solve_task_m11(state):
    """Delete the Heading/Display text style."""
    style = find_style(state, "Heading/Display")
    style_id = style["id"]
    state["textStyles"] = [s for s in state["textStyles"] if s["id"] != style_id]
    for layer in state["textLayers"]:
        if layer.get("textStyleId") == style_id:
            layer["textStyleId"] = None


def solve_task_m12(state):
    """Set the Variable Font Demo weight to 700."""
    find_layer(state, "Variable Font Demo")["variableAxes"]["wght"] = 700


def solve_task_m13(state):
    """Change the nudge amount to 2 and the big nudge to 20."""
    state["preferences"]["nudgeAmount"] = 2
    state["preferences"]["bigNudgeAmount"] = 20


def solve_task_m14(state):
    """Enable truncation on the Body Text and limit it to 4 lines."""
    find_layer(state, "Body Text")["truncation"] = {"enabled": True, "maxLines": 4}


def solve_task_m15(state):
    """Switch the Call to Action to auto-width resizing."""
    layer = find_layer(state, "Call to Action")
    layer["resizing"] = "auto-width"
    layer["width"] = None
    layer["height"] = None


def solve_task_m16(state):
    """Add a link covering the full Japanese Heading text pointing to https://figma.com/japan."""
    layer = find_layer(state, "Japanese Heading")
    next_link_id = state.get("_nextLinkId", 100)
    link_id = f"lnk_{str(next_link_id).zfill(3)}"
    content_len = len(layer["content"])
    layer["links"].append({
        "id": link_id,
        "startIndex": 0,
        "endIndex": content_len,
        "url": "https://figma.com/japan",
    })
    state["_nextLinkId"] = next_link_id + 1


def solve_task_m17(state):
    """Reduce the Section Header font size to 28 and widen its letter spacing to 0.05 em."""
    layer = find_layer(state, "Section Header")
    layer["fontSize"] = 28
    layer["letterSpacing"] = {"value": 0.05, "unit": "em"}


def solve_task_m18(state):
    """Set the default alignment to center and the default text direction to RTL."""
    state["preferences"]["defaultHorizontalAlign"] = "center"
    state["preferences"]["defaultTextDirection"] = "rtl"


def solve_task_m19(state):
    """Enable Stylistic Set 1 on the Page Title."""
    find_layer(state, "Page Title")["openTypeFeatures"]["ss01"] = True


def solve_task_m20(state):
    """Change the Small Caps Header to uppercase and increase its size to 16."""
    layer = find_layer(state, "Small Caps Header")
    layer["letterCase"] = "uppercase"
    layer["fontSize"] = 16


# -- solve functions (hard) -------------------------------------------------

def solve_task_h1(state):
    """Switch all text layers currently using Inter to Roboto."""
    for layer in state["textLayers"]:
        if layer["fontFamily"] == "Inter":
            layer["fontFamily"] = "Roboto"
            # Roboto is variable: wght (100-900, default 400), wdth (75-100, default 100)
            layer["variableAxes"] = {"wght": 400, "wdth": 100}


def solve_task_h2(state):
    """Hide all the right-to-left text layers."""
    for layer in state["textLayers"]:
        if layer["textDirection"] == "rtl":
            layer["visible"] = False


def solve_task_h3(state):
    """Detach the text style from every layer that has one applied."""
    for layer in state["textLayers"]:
        if layer.get("textStyleId"):
            layer["textStyleId"] = None


def solve_task_h4(state):
    """Create a text style called 'Body/Compact' with Inter Regular at 13px and 16px line height."""
    next_id = state.get("_nextTextStyleId", 100)
    style = {
        "id": f"ts_{str(next_id).zfill(3)}",
        "name": "Body/Compact",
        "fontFamily": "Inter",
        "fontStyle": "Regular",
        "fontSize": 13,
        "lineHeight": {"value": 16, "unit": "px"},
        "letterSpacing": {"value": 0, "unit": "em"},
        "paragraphSpacing": 0,
        "paragraphIndent": 0,
        "textDecoration": "none",
        "letterCase": "none",
        "listStyle": "none",
        "openTypeFeatures": {"liga": True, "kern": True},
        "description": "",
        "createdAt": NOW,
        "updatedAt": NOW,
    }
    state["textStyles"].append(style)
    state["_nextTextStyleId"] = next_id + 1


def solve_task_h5(state):
    """Update the Body/Regular style to use a font size of 18."""
    style = find_style(state, "Body/Regular")
    style["fontSize"] = 18
    propagate_style_to_layers(state, style)


def solve_task_h6(state):
    """Lock all layers that have links in them."""
    for layer in state["textLayers"]:
        if layer.get("links") and len(layer["links"]) > 0:
            layer["locked"] = True


def solve_task_h7(state):
    """Remove all list formatting from every layer."""
    for layer in state["textLayers"]:
        layer["listStyle"] = "none"


def solve_task_h8(state):
    """Create a new text layer with specific properties."""
    next_id = state.get("_nextTextLayerId", 100)
    layer = {
        "id": f"tl_{str(next_id).zfill(3)}",
        "name": "Subscribe to our newsl",
        "content": "Subscribe to our newsletter",
        "fontFamily": "Poppins",
        "fontStyle": "Bold",
        "fontSize": 16,
        "lineHeight": deepcopy(state["preferences"]["defaultLineHeight"]),
        "letterSpacing": deepcopy(state["preferences"]["defaultLetterSpacing"]),
        "paragraphSpacing": 0,
        "paragraphIndent": 0,
        "horizontalAlign": "center",
        "verticalAlign": "top",
        "textDecoration": "none",
        "letterCase": "uppercase",
        "textDirection": state["preferences"]["defaultTextDirection"],
        "resizing": "auto-width",
        "truncation": {"enabled": False, "maxLines": None},
        "listStyle": "none",
        "listSpacing": 0,
        "hangingPunctuation": False,
        "hangingList": False,
        "verticalTrim": False,
        "links": [],
        "openTypeFeatures": {"liga": True, "kern": True},
        "textStyleId": None,
        "variableAxes": {},
        "width": None,
        "height": None,
        "x": 40,
        "y": 40 + len(state["textLayers"]) * 40,
        "locked": False,
        "visible": True,
        "createdAt": NOW,
        "updatedAt": NOW,
    }
    state["textLayers"].append(layer)
    state["_nextTextLayerId"] = next_id + 1


def solve_task_h9(state):
    """Change the Heading/H2 style to use Playfair Display Bold."""
    style = find_style(state, "Heading/H2")
    style["fontFamily"] = "Playfair Display"
    style["fontStyle"] = "Bold"
    propagate_style_to_layers(state, style)


def solve_task_h10(state):
    """Remove all links from the Copyright Notice."""
    find_layer(state, "Copyright Notice")["links"] = []


def solve_task_h11(state):
    """Enable vertical trim on both the Page Title and Section Header."""
    find_layer(state, "Page Title")["verticalTrim"] = True
    find_layer(state, "Section Header")["verticalTrim"] = True


def solve_task_h12(state):
    """Reduce the Caption/Small style's font size to 11 pixels."""
    style = find_style(state, "Caption/Small")
    style["fontSize"] = 11
    propagate_style_to_layers(state, style)


def solve_task_h13(state):
    """Rename Call to Action to 'CTA Button', DM Sans Bold, auto-height."""
    layer = find_layer(state, "Call to Action")
    layer["name"] = "CTA Button"
    layer["fontFamily"] = "DM Sans"
    layer["fontStyle"] = "Bold"
    layer["resizing"] = "auto-height"
    # DM Sans is variable: wght (100-1000, default 400), opsz (9-40, default 14)
    layer["variableAxes"] = {"wght": 400, "opsz": 14}
    # auto-height keeps width, sets height to null
    layer["height"] = None


def solve_task_h14(state):
    """Disable contextual alternates on all layers that currently have them enabled."""
    for layer in state["textLayers"]:
        features = layer.get("openTypeFeatures", {})
        if features.get("calt") is True:
            features["calt"] = False


def solve_task_h15(state):
    """Apply the Label/Overline style to the Small Caps Header."""
    layer = find_layer(state, "Small Caps Header")
    style = find_style(state, "Label/Overline")
    apply_style_to_layer(layer, style)


def solve_task_h16(state):
    """Delete both the Body/Small and Body/Large text styles."""
    names_to_delete = {"Body/Small", "Body/Large"}
    ids_to_delete = {s["id"] for s in state["textStyles"] if s["name"] in names_to_delete}
    state["textStyles"] = [s for s in state["textStyles"] if s["id"] not in ids_to_delete]
    for layer in state["textLayers"]:
        if layer.get("textStyleId") in ids_to_delete:
            layer["textStyleId"] = None


def solve_task_h17(state):
    """Add 12 pixels of paragraph spacing to every layer that uses a list format."""
    for layer in state["textLayers"]:
        if layer.get("listStyle") not in (None, "none"):
            layer["paragraphSpacing"] = 12


def solve_task_h18(state):
    """Create Heading/H4 style and apply to Release Notes Header."""
    next_id = state.get("_nextTextStyleId", 100)
    style = {
        "id": f"ts_{str(next_id).zfill(3)}",
        "name": "Heading/H4",
        "fontFamily": "Inter",
        "fontStyle": "Semi Bold",
        "fontSize": 20,
        "lineHeight": {"value": 28, "unit": "px"},
        "letterSpacing": {"value": -0.01, "unit": "em"},
        "paragraphSpacing": 0,
        "paragraphIndent": 0,
        "textDecoration": "none",
        "letterCase": "none",
        "listStyle": "none",
        "openTypeFeatures": {"liga": True, "kern": True},
        "description": "",
        "createdAt": NOW,
        "updatedAt": NOW,
    }
    state["textStyles"].append(style)
    state["_nextTextStyleId"] = next_id + 1

    layer = find_layer(state, "Release Notes Header")
    apply_style_to_layer(layer, style)


def solve_task_h19(state):
    """Change all auto-width layers to auto-height with a width of 400."""
    for layer in state["textLayers"]:
        if layer["resizing"] == "auto-width":
            layer["resizing"] = "auto-height"
            layer["width"] = 400
            layer["height"] = None


def solve_task_h20(state):
    """Turn off all OpenType features except standard ligatures and kerning on Code Sample."""
    layer = find_layer(state, "Code Sample")
    features = layer.get("openTypeFeatures", {})
    for key in list(features.keys()):
        if key not in ("liga", "kern"):
            features[key] = False
    # Ensure liga and kern are True
    features["liga"] = True
    features["kern"] = True


# -- solve functions (hardening round 1) -----------------------------------

def solve_task_h21(state):
    """Create 'Quote/Block' style with Playfair Display Regular 18px/28px, apply to Indented Quote."""
    next_id = state.get("_nextTextStyleId", 100)
    style = {
        "id": f"ts_{str(next_id).zfill(3)}",
        "name": "Quote/Block",
        "fontFamily": "Playfair Display",
        "fontStyle": "Regular",
        "fontSize": 18,
        "lineHeight": {"value": 28, "unit": "px"},
        "letterSpacing": {"value": 0, "unit": "em"},
        "paragraphSpacing": 0,
        "paragraphIndent": 0,
        "textDecoration": "none",
        "letterCase": "none",
        "listStyle": "none",
        "openTypeFeatures": {"liga": True, "kern": True},
        "description": "",
        "createdAt": NOW,
        "updatedAt": NOW,
    }
    state["textStyles"].append(style)
    state["_nextTextStyleId"] = next_id + 1

    layer = find_layer(state, "Indented Quote")
    apply_style_to_layer(layer, style)


def solve_task_h22(state):
    """Swap list formats: bulleted→numbered, numbered→bulleted."""
    for layer in state["textLayers"]:
        if layer["listStyle"] == "bulleted":
            layer["listStyle"] = "numbered"
        elif layer["listStyle"] == "numbered":
            layer["listStyle"] = "bulleted"


def solve_task_h23(state):
    """Lock the text layer with the most hyperlinks."""
    # Copyright Notice has 2 links (most)
    find_layer(state, "Copyright Notice")["locked"] = True


def solve_task_h24(state):
    """Duplicate Call to Action, rename to 'Secondary CTA', DM Sans Regular, remove uppercase."""
    original = find_layer(state, "Call to Action")
    next_id = state.get("_nextTextLayerId", 100)
    dup = deepcopy(original)
    dup["id"] = f"tl_{str(next_id).zfill(3)}"
    dup["name"] = "Secondary CTA"
    dup["fontFamily"] = "DM Sans"
    dup["fontStyle"] = "Regular"
    dup["letterCase"] = "none"
    # DM Sans is variable: wght (100-1000, default 400), opsz (9-40, default 14)
    dup["variableAxes"] = {"wght": 400, "opsz": 14}
    dup["y"] = original["y"] + 40
    dup["createdAt"] = NOW
    dup["updatedAt"] = NOW
    state["textLayers"].append(dup)
    state["_nextTextLayerId"] = next_id + 1


def solve_task_h25(state):
    """Add paragraph indent of 24 to every layer with paragraph spacing > 0."""
    for layer in state["textLayers"]:
        if layer.get("paragraphSpacing", 0) > 0:
            layer["paragraphIndent"] = 24


def solve_task_h26(state):
    """Enable fractions on both Montserrat layers."""
    for layer in state["textLayers"]:
        if layer["fontFamily"] == "Montserrat":
            layer["openTypeFeatures"]["frac"] = True


def solve_task_h27(state):
    """Switch all auto-height layers to fixed with height=200, keep widths."""
    for layer in state["textLayers"]:
        if layer["resizing"] == "auto-height":
            layer["resizing"] = "fixed"
            layer["height"] = 200
            # width is already set for auto-height layers


def solve_task_h28(state):
    """Find layer with smallest font size, duplicate it, set duplicate's size to 24."""
    smallest = min(state["textLayers"], key=lambda l: l["fontSize"])
    next_id = state.get("_nextTextLayerId", 100)
    dup = deepcopy(smallest)
    dup["id"] = f"tl_{str(next_id).zfill(3)}"
    dup["name"] = f"{smallest['name']} (copy)"
    dup["fontSize"] = 24
    dup["y"] = smallest["y"] + 40
    dup["createdAt"] = NOW
    dup["updatedAt"] = NOW
    state["textLayers"].append(dup)
    state["_nextTextLayerId"] = next_id + 1


def solve_task_h29(state):
    """Turn on vertical trim for every layer with a text style applied."""
    for layer in state["textLayers"]:
        if layer.get("textStyleId"):
            layer["verticalTrim"] = True


def solve_task_h30(state):
    """Delete every text style not used by any layer."""
    used_ids = {l.get("textStyleId") for l in state["textLayers"] if l.get("textStyleId")}
    state["textStyles"] = [s for s in state["textStyles"] if s["id"] in used_ids]


def solve_task_h31(state):
    """Underline every layer whose content mentions 'Figma'."""
    for layer in state["textLayers"]:
        if "Figma" in layer.get("content", ""):
            layer["textDecoration"] = "underline"


def solve_task_h32(state):
    """Apply Body/Regular to Strikethrough Example, then set decoration to underline."""
    layer = find_layer(state, "Strikethrough Example")
    style = find_style(state, "Body/Regular")
    apply_style_to_layer(layer, style)
    layer["textDecoration"] = "underline"


def solve_task_h33(state):
    """Change letter case of the only Playfair Display layer to capitalize."""
    find_layer(state, "Indented Quote")["letterCase"] = "capitalize"


def solve_task_h34(state):
    """Swap center-aligned and right-aligned layers."""
    for layer in state["textLayers"]:
        if layer["horizontalAlign"] == "center":
            layer["horizontalAlign"] = "right"
        elif layer["horizontalAlign"] == "right":
            layer["horizontalAlign"] = "center"


def solve_task_h35(state):
    """Set defaults to Playfair Display/24, then create 'Hero Title' layer."""
    state["preferences"]["defaultFontFamily"] = "Playfair Display"
    state["preferences"]["defaultFontSize"] = 24
    next_id = state.get("_nextTextLayerId", 100)
    prefs = state["preferences"]
    layer = {
        "id": f"tl_{str(next_id).zfill(3)}",
        "name": "Hero Title",
        "content": "Hero Title",
        "fontFamily": "Playfair Display",
        "fontStyle": prefs["defaultFontStyle"],
        "fontSize": 24,
        "lineHeight": deepcopy(prefs["defaultLineHeight"]),
        "letterSpacing": deepcopy(prefs["defaultLetterSpacing"]),
        "paragraphSpacing": 0,
        "paragraphIndent": 0,
        "horizontalAlign": prefs["defaultHorizontalAlign"],
        "verticalAlign": "top",
        "textDecoration": "none",
        "letterCase": "none",
        "textDirection": prefs["defaultTextDirection"],
        "resizing": "auto-width",
        "truncation": {"enabled": False, "maxLines": None},
        "listStyle": "none",
        "listSpacing": 0,
        "hangingPunctuation": False,
        "hangingList": False,
        "verticalTrim": False,
        "links": [],
        "openTypeFeatures": {"liga": True, "kern": True},
        "textStyleId": None,
        "variableAxes": {},
        "width": None,
        "height": None,
        "x": 40,
        "y": 40 + len(state["textLayers"]) * 40,
        "locked": False,
        "visible": True,
        "createdAt": NOW,
        "updatedAt": NOW,
    }
    state["textLayers"].append(layer)
    state["_nextTextLayerId"] = next_id + 1


def solve_task_h36(state):
    """Enable oldstyle figures on every Inter layer."""
    for layer in state["textLayers"]:
        if layer["fontFamily"] == "Inter":
            layer["openTypeFeatures"]["onum"] = True


def solve_task_h37(state):
    """Remove all links from every auto-width layer."""
    for layer in state["textLayers"]:
        if layer["resizing"] == "auto-width":
            layer["links"] = []


def solve_task_h38(state):
    """Create 'Navigation Menu' layer: Montserrat Medium 14px, small-caps, smcp."""
    next_id = state.get("_nextTextLayerId", 100)
    prefs = state["preferences"]
    layer = {
        "id": f"tl_{str(next_id).zfill(3)}",
        "name": "Navigation Menu",
        "content": "Navigation Menu",
        "fontFamily": "Montserrat",
        "fontStyle": "Medium",
        "fontSize": 14,
        "lineHeight": deepcopy(prefs["defaultLineHeight"]),
        "letterSpacing": deepcopy(prefs["defaultLetterSpacing"]),
        "paragraphSpacing": 0,
        "paragraphIndent": 0,
        "horizontalAlign": prefs["defaultHorizontalAlign"],
        "verticalAlign": "top",
        "textDecoration": "none",
        "letterCase": "small-caps",
        "textDirection": prefs["defaultTextDirection"],
        "resizing": "auto-width",
        "truncation": {"enabled": False, "maxLines": None},
        "listStyle": "none",
        "listSpacing": 0,
        "hangingPunctuation": False,
        "hangingList": False,
        "verticalTrim": False,
        "links": [],
        "openTypeFeatures": {"liga": True, "kern": True, "smcp": True},
        "textStyleId": None,
        "variableAxes": {},
        "width": None,
        "height": None,
        "x": 40,
        "y": 40 + len(state["textLayers"]) * 40,
        "locked": False,
        "visible": True,
        "createdAt": NOW,
        "updatedAt": NOW,
    }
    state["textLayers"].append(layer)
    state["_nextTextLayerId"] = next_id + 1


def solve_task_h39(state):
    """Disable vertical trim and hanging punctuation on layers that have them."""
    for layer in state["textLayers"]:
        if layer.get("verticalTrim") is True:
            layer["verticalTrim"] = False
        if layer.get("hangingPunctuation") is True:
            layer["hangingPunctuation"] = False


def solve_task_h40(state):
    """Rename the DM Sans layer to 'New Features', change font to Open Sans Bold."""
    layer = find_layer(state, "Release Notes Header")
    layer["name"] = "New Features"
    layer["fontFamily"] = "Open Sans"
    layer["fontStyle"] = "Bold"
    # Open Sans is variable: wght (300-800, default 400)
    layer["variableAxes"] = {"wght": 400}


# -- solve functions (hardening round 2) -----------------------------------

def solve_task_h41(state):
    """Duplicate the longest-content layer, rename to 'Content Summary', enable truncation (3 lines)."""
    longest = max(state["textLayers"], key=lambda l: len(l.get("content", "")))
    next_id = state.get("_nextTextLayerId", 100)
    dup = deepcopy(longest)
    dup["id"] = f"tl_{str(next_id).zfill(3)}"
    dup["name"] = "Content Summary"
    dup["truncation"] = {"enabled": True, "maxLines": 3}
    dup["y"] = longest["y"] + 40
    dup["createdAt"] = NOW
    dup["updatedAt"] = NOW
    state["textLayers"].append(dup)
    state["_nextTextLayerId"] = next_id + 1


def solve_task_h42(state):
    """Apply the style with the widest letter spacing to Variable Font Demo."""
    style = find_style(state, "Label/SmallCaps")
    layer = find_layer(state, "Variable Font Demo")
    apply_style_to_layer(layer, style)


def solve_task_h43(state):
    """Set spelling language to Arabic (bold RTL layer's script), hide that layer."""
    state["preferences"]["spellingLanguage"] = "Arabic"
    find_layer(state, "Arabic Welcome")["visible"] = False


def solve_task_h44(state):
    """Enable oldstyle figures and lining figures on Indented Quote (Spiekermann layer)."""
    layer = find_layer(state, "Indented Quote")
    layer["openTypeFeatures"]["onum"] = True
    layer["openTypeFeatures"]["lnum"] = True


def solve_task_h45(state):
    """Montserrat disambiguation: smaller -> Inter Semi Bold, larger -> Playfair Display Bold."""
    small_caps = find_layer(state, "Small Caps Header")
    small_caps["fontFamily"] = "Inter"
    small_caps["fontStyle"] = "Semi Bold"
    small_caps["variableAxes"] = {"wght": 400, "slnt": 0}

    section = find_layer(state, "Section Header")
    section["fontFamily"] = "Playfair Display"
    section["fontStyle"] = "Bold"
    section["variableAxes"] = {"wght": 400}


def solve_task_h46(state):
    """Delete the unused style with the second-largest font size (Heading/H3, 24px)."""
    used_ids = {l.get("textStyleId") for l in state["textLayers"] if l.get("textStyleId")}
    unused = [s for s in state["textStyles"] if s["id"] not in used_ids]
    unused.sort(key=lambda s: s["fontSize"], reverse=True)
    target = unused[1]
    state["textStyles"] = [s for s in state["textStyles"] if s["id"] != target["id"]]


def solve_task_h47(state):
    """Serif layers -> capitalize, monospace layers -> lowercase."""
    cat_map = {f["name"]: f.get("category", "") for f in state["fontFamilies"]}
    for layer in state["textLayers"]:
        cat = cat_map.get(layer["fontFamily"], "")
        if cat == "serif":
            layer["letterCase"] = "capitalize"
        elif cat == "monospace":
            layer["letterCase"] = "lowercase"


def solve_task_h48(state):
    """Lock center/right-aligned layers, hide strikethrough layers."""
    for layer in state["textLayers"]:
        if layer["horizontalAlign"] in ("center", "right"):
            layer["locked"] = True
        if layer["textDecoration"] == "strikethrough":
            layer["visible"] = False


def solve_task_h49(state):
    """Styled layers: left-aligned -> center, center-aligned -> right."""
    for layer in state["textLayers"]:
        if layer.get("textStyleId"):
            if layer["horizontalAlign"] == "left":
                layer["horizontalAlign"] = "center"
            elif layer["horizontalAlign"] == "center":
                layer["horizontalAlign"] = "right"


def solve_task_h50(state):
    """Change %-based line heights to 24px."""
    for layer in state["textLayers"]:
        lh = layer.get("lineHeight", {})
        if lh.get("unit") == "%":
            layer["lineHeight"] = {"value": 24, "unit": "px"}


def solve_task_h51(state):
    """Delete Heading/H1 and apply Heading/H3 to layers that had H1."""
    h1 = find_style(state, "Heading/H1")
    h3 = find_style(state, "Heading/H3")
    h1_id = h1["id"]
    for layer in state["textLayers"]:
        if layer.get("textStyleId") == h1_id:
            apply_style_to_layer(layer, h3)
    state["textStyles"] = [s for s in state["textStyles"] if s["id"] != h1_id]


def solve_task_h52(state):
    """Create Code/Block style from Code Sample properties, apply to Code Sample."""
    layer = find_layer(state, "Code Sample")
    next_id = state.get("_nextTextStyleId", 100)
    style = {
        "id": f"ts_{str(next_id).zfill(3)}",
        "name": "Code/Block",
        "fontFamily": layer["fontFamily"],
        "fontStyle": layer["fontStyle"],
        "fontSize": layer["fontSize"],
        "lineHeight": deepcopy(layer["lineHeight"]),
        "letterSpacing": deepcopy(layer["letterSpacing"]),
        "paragraphSpacing": layer["paragraphSpacing"],
        "paragraphIndent": layer["paragraphIndent"],
        "textDecoration": layer["textDecoration"],
        "letterCase": layer["letterCase"],
        "listStyle": layer["listStyle"],
        "openTypeFeatures": deepcopy(layer["openTypeFeatures"]),
        "description": "",
        "createdAt": NOW,
        "updatedAt": NOW,
    }
    state["textStyles"].append(style)
    state["_nextTextStyleId"] = next_id + 1
    apply_style_to_layer(layer, style)


def solve_task_h53(state):
    """Layers with custom weight axis below 500 -> increase to 500."""
    for layer in state["textLayers"]:
        axes = layer.get("variableAxes", {})
        if "wght" in axes and axes["wght"] < 500:
            axes["wght"] = 500


def solve_task_h54(state):
    """Update Body/Regular to 15px/22px line height, then detach from all layers."""
    style = find_style(state, "Body/Regular")
    style["fontSize"] = 15
    style["lineHeight"] = {"value": 22, "unit": "px"}
    propagate_style_to_layers(state, style)
    for layer in state["textLayers"]:
        if layer.get("textStyleId") == style["id"]:
            layer["textStyleId"] = None


def solve_task_h55(state):
    """Create Serif/Quote style from the only serif layer (Indented Quote), apply it."""
    layer = find_layer(state, "Indented Quote")
    next_id = state.get("_nextTextStyleId", 100)
    style = {
        "id": f"ts_{str(next_id).zfill(3)}",
        "name": "Serif/Quote",
        "fontFamily": layer["fontFamily"],
        "fontStyle": layer["fontStyle"],
        "fontSize": layer["fontSize"],
        "lineHeight": deepcopy(layer["lineHeight"]),
        "letterSpacing": deepcopy(layer["letterSpacing"]),
        "paragraphSpacing": layer["paragraphSpacing"],
        "paragraphIndent": layer["paragraphIndent"],
        "textDecoration": layer["textDecoration"],
        "letterCase": layer["letterCase"],
        "listStyle": layer["listStyle"],
        "openTypeFeatures": deepcopy(layer["openTypeFeatures"]),
        "description": "",
        "createdAt": NOW,
        "updatedAt": NOW,
    }
    state["textStyles"].append(style)
    state["_nextTextStyleId"] = next_id + 1
    apply_style_to_layer(layer, style)


def solve_task_h56(state):
    """Create 'Table of Contents' layer with numbered list, Open Sans Medium 15px, hanging list."""
    next_id = state.get("_nextTextLayerId", 100)
    prefs = state["preferences"]
    layer = {
        "id": f"tl_{str(next_id).zfill(3)}",
        "name": "Table of Contents",
        "content": "Table of Contents",
        "fontFamily": "Open Sans",
        "fontStyle": "Medium",
        "fontSize": 15,
        "lineHeight": {"value": 22, "unit": "px"},
        "letterSpacing": deepcopy(prefs["defaultLetterSpacing"]),
        "paragraphSpacing": 0,
        "paragraphIndent": 0,
        "horizontalAlign": prefs["defaultHorizontalAlign"],
        "verticalAlign": "top",
        "textDecoration": "none",
        "letterCase": "none",
        "textDirection": prefs["defaultTextDirection"],
        "resizing": "auto-width",
        "truncation": {"enabled": False, "maxLines": None},
        "listStyle": "numbered",
        "listSpacing": 8,
        "hangingPunctuation": False,
        "hangingList": True,
        "verticalTrim": False,
        "links": [],
        "openTypeFeatures": {"liga": True, "kern": True},
        "textStyleId": None,
        "variableAxes": {},
        "width": None,
        "height": None,
        "x": 40,
        "y": 40 + len(state["textLayers"]) * 40,
        "locked": False,
        "visible": True,
        "createdAt": NOW,
        "updatedAt": NOW,
    }
    state["textLayers"].append(layer)
    state["_nextTextLayerId"] = next_id + 1


def solve_task_h57(state):
    """Variable Font Demo: set weight to max (900), slant to min (-10)."""
    layer = find_layer(state, "Variable Font Demo")
    layer["variableAxes"]["wght"] = 900
    layer["variableAxes"]["slnt"] = -10


def solve_task_h58(state):
    """Apply Body/Regular to all layers with fontSize 14."""
    style = find_style(state, "Body/Regular")
    for layer in state["textLayers"]:
        if layer["fontSize"] == 14:
            apply_style_to_layer(layer, style)


def solve_task_h59(state):
    """Duplicate Page Title as 'Page Subtitle', Lato Regular 20px, 28px lh, no style, 0.01em spacing."""
    original = find_layer(state, "Page Title")
    next_id = state.get("_nextTextLayerId", 100)
    dup = deepcopy(original)
    dup["id"] = f"tl_{str(next_id).zfill(3)}"
    dup["name"] = "Page Subtitle"
    dup["fontFamily"] = "Lato"
    dup["fontStyle"] = "Regular"
    dup["fontSize"] = 20
    dup["lineHeight"] = {"value": 28, "unit": "px"}
    dup["textStyleId"] = None
    dup["letterSpacing"] = {"value": 0.01, "unit": "em"}
    dup["variableAxes"] = {}
    dup["y"] = original["y"] + 40
    dup["createdAt"] = NOW
    dup["updatedAt"] = NOW
    state["textLayers"].append(dup)
    state["_nextTextLayerId"] = next_id + 1


def solve_task_h60(state):
    """Add underline decoration to every layer that has at least one link."""
    for layer in state["textLayers"]:
        if layer.get("links") and len(layer["links"]) > 0:
            layer["textDecoration"] = "underline"


# -- solve functions (hardening round 3) -----------------------------------

def solve_task_h61(state):
    """Set letter spacing 0.02em and line height 22px on every 14px layer."""
    for layer in state["textLayers"]:
        if layer["fontSize"] == 14:
            layer["letterSpacing"] = {"value": 0.02, "unit": "em"}
            layer["lineHeight"] = {"value": 22, "unit": "px"}


def solve_task_h62(state):
    """Halve Heading/Display font size, switch to Crimson Text Bold, apply to Japanese Heading."""
    style = find_style(state, "Heading/Display")
    style["fontSize"] = 32  # 64 / 2
    style["fontFamily"] = "Crimson Text"
    style["fontStyle"] = "Bold"
    layer = find_layer(state, "Japanese Heading")
    apply_style_to_layer(layer, style)


def solve_task_h63(state):
    """Lock every layer whose font family starts with 'Noto'."""
    for layer in state["textLayers"]:
        if layer["fontFamily"].startswith("Noto"):
            layer["locked"] = True


def solve_task_h64(state):
    """Clamp font sizes to 14-32 range."""
    for layer in state["textLayers"]:
        if layer["fontSize"] < 14:
            layer["fontSize"] = 14
        elif layer["fontSize"] > 32:
            layer["fontSize"] = 32


def solve_task_h65(state):
    """Update Heading/H2: Playfair Display Semi Bold 28px/36px, enable onum. Propagate."""
    style = find_style(state, "Heading/H2")
    style["fontFamily"] = "Playfair Display"
    style["fontStyle"] = "Semi Bold"
    style["fontSize"] = 28
    style["lineHeight"] = {"value": 36, "unit": "px"}
    style["openTypeFeatures"]["onum"] = True
    propagate_style_to_layers(state, style)


def solve_task_h66(state):
    """Duplicate the 14px bulleted list layer as 'Benefits List', Poppins Medium, numbered."""
    original = find_layer(state, "Feature List")
    next_id = state.get("_nextTextLayerId", 100)
    dup = deepcopy(original)
    dup["id"] = f"tl_{str(next_id).zfill(3)}"
    dup["name"] = "Benefits List"
    dup["fontFamily"] = "Poppins"
    dup["fontStyle"] = "Medium"
    dup["listStyle"] = "numbered"
    dup["variableAxes"] = {}
    dup["y"] = original["y"] + 40
    dup["createdAt"] = NOW
    dup["updatedAt"] = NOW
    state["textLayers"].append(dup)
    state["_nextTextLayerId"] = next_id + 1


def solve_task_h67(state):
    """On Indented Quote: disable ss01, enable onum+smcp, set paragraph indent to 40."""
    layer = find_layer(state, "Indented Quote")
    layer["openTypeFeatures"]["ss01"] = False
    layer["openTypeFeatures"]["onum"] = True
    layer["openTypeFeatures"]["smcp"] = True
    layer["paragraphIndent"] = 40


def solve_task_h68(state):
    """Set default font to match the layer with widest letter spacing (Small Caps Header)."""
    # Small Caps Header has letterSpacing 0.1em (widest), uses Montserrat 14px
    state["preferences"]["defaultFontFamily"] = "Montserrat"
    state["preferences"]["defaultFontSize"] = 14


def solve_task_h69(state):
    """Add link on first 10 chars to figma.com/list and set list spacing 10 on all list layers."""
    next_link_id = state.get("_nextLinkId", 100)
    for layer in state["textLayers"]:
        if layer.get("listStyle") not in (None, "none"):
            link_id = f"lnk_{str(next_link_id).zfill(3)}"
            layer["links"].append({
                "id": link_id,
                "startIndex": 0,
                "endIndex": 10,
                "url": "https://figma.com/list",
            })
            next_link_id += 1
            layer["listSpacing"] = 10
    state["_nextLinkId"] = next_link_id


def solve_task_h70(state):
    """Create 'Sidebar Navigation' layer: Space Grotesk Bold 13px, uppercase, 0.08em, zero."""
    next_id = state.get("_nextTextLayerId", 100)
    prefs = state["preferences"]
    layer = {
        "id": f"tl_{str(next_id).zfill(3)}",
        "name": "Sidebar Navigation",
        "content": "Sidebar Navigation",
        "fontFamily": "Space Grotesk",
        "fontStyle": "Bold",
        "fontSize": 13,
        "lineHeight": {"value": 18, "unit": "px"},
        "letterSpacing": {"value": 0.08, "unit": "em"},
        "paragraphSpacing": 0,
        "paragraphIndent": 0,
        "horizontalAlign": prefs["defaultHorizontalAlign"],
        "verticalAlign": "top",
        "textDecoration": "none",
        "letterCase": "uppercase",
        "textDirection": prefs["defaultTextDirection"],
        "resizing": "auto-width",
        "truncation": {"enabled": False, "maxLines": None},
        "listStyle": "none",
        "listSpacing": 0,
        "hangingPunctuation": False,
        "hangingList": False,
        "verticalTrim": False,
        "links": [],
        "openTypeFeatures": {"liga": True, "kern": True, "zero": True},
        "textStyleId": None,
        "variableAxes": {},
        "width": None,
        "height": None,
        "x": 40,
        "y": 40 + len(state["textLayers"]) * 40,
        "locked": False,
        "visible": True,
        "createdAt": NOW,
        "updatedAt": NOW,
    }
    state["textLayers"].append(layer)
    state["_nextTextLayerId"] = next_id + 1


def solve_task_h71(state):
    """Find layer with hanging punctuation + indent, change to Merriweather Regular, spacing 16."""
    layer = find_layer(state, "Indented Quote")
    layer["fontFamily"] = "Merriweather"
    layer["fontStyle"] = "Regular"
    layer["variableAxes"] = {}
    layer["paragraphSpacing"] = 16


def solve_task_h72(state):
    """Code Sample: Fira Code Medium 15px/24px, enable ss01+zero, detach style."""
    layer = find_layer(state, "Code Sample")
    layer["fontFamily"] = "Fira Code"
    layer["fontStyle"] = "Medium"
    layer["fontSize"] = 15
    layer["lineHeight"] = {"value": 24, "unit": "px"}
    layer["openTypeFeatures"]["ss01"] = True
    layer["openTypeFeatures"]["zero"] = True
    layer["textStyleId"] = None
    # Fira Code is variable: wght (300-700, default 400)
    layer["variableAxes"] = {"wght": 400}


def solve_task_h73(state):
    """Apply Caption/Small to Release Notes Header (second-largest font size), enable truncation 2."""
    layer = find_layer(state, "Release Notes Header")
    style = find_style(state, "Caption/Small")
    apply_style_to_layer(layer, style)
    layer["truncation"] = {"enabled": True, "maxLines": 2}


def solve_task_h74(state):
    """Set spelling language Japanese, big nudge 50, default alignment right."""
    state["preferences"]["spellingLanguage"] = "Japanese"
    state["preferences"]["bigNudgeAmount"] = 50
    state["preferences"]["defaultHorizontalAlign"] = "right"


def solve_task_h75(state):
    """Hide the larger RTL layer (Arabic Welcome), lock the smaller (Hebrew Body)."""
    find_layer(state, "Arabic Welcome")["visible"] = False
    find_layer(state, "Hebrew Body")["locked"] = True


def solve_task_h76(state):
    """Create 'Learn More' layer: Crimson Text Semi Bold 16px, underline, center, full link."""
    next_id = state.get("_nextTextLayerId", 100)
    next_link_id = state.get("_nextLinkId", 100)
    prefs = state["preferences"]
    content = "Learn More"
    layer = {
        "id": f"tl_{str(next_id).zfill(3)}",
        "name": "Learn More",
        "content": content,
        "fontFamily": "Crimson Text",
        "fontStyle": "Semi Bold",
        "fontSize": 16,
        "lineHeight": deepcopy(prefs["defaultLineHeight"]),
        "letterSpacing": deepcopy(prefs["defaultLetterSpacing"]),
        "paragraphSpacing": 0,
        "paragraphIndent": 0,
        "horizontalAlign": "center",
        "verticalAlign": "top",
        "textDecoration": "underline",
        "letterCase": "none",
        "textDirection": prefs["defaultTextDirection"],
        "resizing": "auto-width",
        "truncation": {"enabled": False, "maxLines": None},
        "listStyle": "none",
        "listSpacing": 0,
        "hangingPunctuation": False,
        "hangingList": False,
        "verticalTrim": False,
        "links": [{
            "id": f"lnk_{str(next_link_id).zfill(3)}",
            "startIndex": 0,
            "endIndex": len(content),
            "url": "https://figma.com/learn",
        }],
        "openTypeFeatures": {"liga": True, "kern": True},
        "textStyleId": None,
        "variableAxes": {},
        "width": None,
        "height": None,
        "x": 40,
        "y": 40 + len(state["textLayers"]) * 40,
        "locked": False,
        "visible": True,
        "createdAt": NOW,
        "updatedAt": NOW,
    }
    state["textLayers"].append(layer)
    state["_nextTextLayerId"] = next_id + 1
    state["_nextLinkId"] = next_link_id + 1


def solve_task_h77(state):
    """Body Text: Lato Regular, 24px lh, detach style, indent 16, auto-width."""
    layer = find_layer(state, "Body Text")
    layer["fontFamily"] = "Lato"
    layer["fontStyle"] = "Regular"
    layer["lineHeight"] = {"value": 24, "unit": "px"}
    layer["textStyleId"] = None
    layer["paragraphIndent"] = 16
    layer["resizing"] = "auto-width"
    layer["width"] = None
    layer["height"] = None
    layer["variableAxes"] = {}


def solve_task_h78(state):
    """Create Heading/Hero style (Playfair Display Bold 56px/64px, -0.03em, ss01), apply to Page Title."""
    next_id = state.get("_nextTextStyleId", 100)
    style = {
        "id": f"ts_{str(next_id).zfill(3)}",
        "name": "Heading/Hero",
        "fontFamily": "Playfair Display",
        "fontStyle": "Bold",
        "fontSize": 56,
        "lineHeight": {"value": 64, "unit": "px"},
        "letterSpacing": {"value": -0.03, "unit": "em"},
        "paragraphSpacing": 0,
        "paragraphIndent": 0,
        "textDecoration": "none",
        "letterCase": "none",
        "listStyle": "none",
        "openTypeFeatures": {"liga": True, "kern": True, "ss01": True},
        "description": "",
        "createdAt": NOW,
        "updatedAt": NOW,
    }
    state["textStyles"].append(style)
    state["_nextTextStyleId"] = next_id + 1

    layer = find_layer(state, "Page Title")
    apply_style_to_layer(layer, style)


def solve_task_h79(state):
    """Variable Font Demo: Source Code Pro, weight 700, ss01+zero, 0.05em, center."""
    layer = find_layer(state, "Variable Font Demo")
    layer["fontFamily"] = "Source Code Pro"
    # Source Code Pro is variable: wght (200-900, default 400)
    layer["variableAxes"] = {"wght": 700}
    layer["openTypeFeatures"]["ss01"] = True
    layer["openTypeFeatures"]["zero"] = True
    layer["letterSpacing"] = {"value": 0.05, "unit": "em"}
    layer["horizontalAlign"] = "center"


def solve_task_h80(state):
    """Center-aligned -> justify+hangingPunctuation, right-aligned -> left+LTR."""
    for layer in state["textLayers"]:
        if layer["horizontalAlign"] == "center":
            layer["horizontalAlign"] = "justify"
            layer["hangingPunctuation"] = True
        elif layer["horizontalAlign"] == "right":
            layer["horizontalAlign"] = "left"
            layer["textDirection"] = "ltr"


# -- solver registry --------------------------------------------------------

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


# -- server management -----------------------------------------------------

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
    """Start the server on the given port."""
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


# -- task runner ------------------------------------------------------------

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


# -- main ------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Figma Text & Typography real-task sanity check")
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
