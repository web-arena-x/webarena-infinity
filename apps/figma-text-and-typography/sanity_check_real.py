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
