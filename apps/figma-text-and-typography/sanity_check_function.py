#!/usr/bin/env python3
"""
Sanity check for Figma Text & Typography function-test tasks.

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


def find_style_by_id(state, style_id):
    """Find a text style by ID. Raises if not found."""
    for s in state["textStyles"]:
        if s["id"] == style_id:
            return s
    raise ValueError(f"Text style not found: id={style_id!r}")


# -- solve functions --------------------------------------------------------

def solve_task_1(state):
    """Create a new text layer with content 'Hello World'."""
    next_id = state.get("_nextTextLayerId", 100)
    prefs = state["preferences"]
    layer = {
        "id": f"tl_{str(next_id).zfill(3)}",
        "name": "Hello World",
        "content": "Hello World",
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
        "createdAt": "2026-03-07T00:00:00Z",
        "updatedAt": "2026-03-07T00:00:00Z",
    }
    state["textLayers"].append(layer)
    state["_nextTextLayerId"] = next_id + 1


def solve_task_2(state):
    """Delete the text layer 'Strikethrough Example'."""
    state["textLayers"] = [l for l in state["textLayers"] if l["name"] != "Strikethrough Example"]


def solve_task_3(state):
    """Duplicate the text layer 'Page Title'."""
    src = find_layer(state, "Page Title")
    next_id = state.get("_nextTextLayerId", 100)
    copy = deepcopy(src)
    copy["id"] = f"tl_{str(next_id).zfill(3)}"
    copy["name"] = src["name"] + " (copy)"
    copy["y"] = src["y"] + 40
    copy["createdAt"] = "2026-03-07T00:00:00Z"
    copy["updatedAt"] = "2026-03-07T00:00:00Z"
    state["textLayers"].append(copy)
    state["_nextTextLayerId"] = next_id + 1


def solve_task_4(state):
    """Rename 'Body Text' to 'Main Body Copy'."""
    layer = find_layer(state, "Body Text")
    layer["name"] = "Main Body Copy"


def solve_task_5(state):
    """Hide 'Copyright Notice'."""
    layer = find_layer(state, "Copyright Notice")
    layer["visible"] = False


def solve_task_6(state):
    """Lock 'Page Title'."""
    layer = find_layer(state, "Page Title")
    layer["locked"] = True


def solve_task_7(state):
    """Change 'Section Header' font to Roboto."""
    layer = find_layer(state, "Section Header")
    layer["fontFamily"] = "Roboto"
    # Roboto is variable, set default axes
    layer["variableAxes"] = {"wght": 400, "wdth": 100}


def solve_task_8(state):
    """Change 'Page Title' font style to Extra Bold."""
    layer = find_layer(state, "Page Title")
    layer["fontStyle"] = "Extra Bold"


def solve_task_9(state):
    """Change 'Body Text' font size to 18."""
    layer = find_layer(state, "Body Text")
    layer["fontSize"] = 18


def solve_task_10(state):
    """Set 'Page Title' line height to 64 px."""
    layer = find_layer(state, "Page Title")
    layer["lineHeight"] = {"value": 64, "unit": "px"}


def solve_task_11(state):
    """Change 'Body Text' line height to 24 px."""
    layer = find_layer(state, "Body Text")
    layer["lineHeight"] = {"value": 24, "unit": "px"}


def solve_task_12(state):
    """Set 'Section Header' letter spacing to 0.05 em."""
    layer = find_layer(state, "Section Header")
    layer["letterSpacing"] = {"value": 0.05, "unit": "em"}


def solve_task_13(state):
    """Change 'Code Sample' letter spacing to 1 px."""
    layer = find_layer(state, "Code Sample")
    layer["letterSpacing"] = {"value": 1, "unit": "px"}


def solve_task_14(state):
    """Change 'Body Text' alignment to justify."""
    layer = find_layer(state, "Body Text")
    layer["horizontalAlign"] = "justify"


def solve_task_15(state):
    """Change 'Page Title' alignment to center."""
    layer = find_layer(state, "Page Title")
    layer["horizontalAlign"] = "center"


def solve_task_16(state):
    """Change 'Call to Action' vertical alignment to bottom."""
    layer = find_layer(state, "Call to Action")
    layer["verticalAlign"] = "bottom"


def solve_task_17(state):
    """Change 'Body Text' to fixed 600x300."""
    layer = find_layer(state, "Body Text")
    layer["resizing"] = "fixed"
    layer["width"] = 600
    layer["height"] = 300


def solve_task_18(state):
    """Change 'Truncated Preview' to auto-width."""
    layer = find_layer(state, "Truncated Preview")
    layer["resizing"] = "auto-width"
    layer["width"] = None
    layer["height"] = None


def solve_task_19(state):
    """Set 'Body Text' decoration to underline."""
    layer = find_layer(state, "Body Text")
    layer["textDecoration"] = "underline"


def solve_task_20(state):
    """Remove strikethrough from 'Strikethrough Example'."""
    layer = find_layer(state, "Strikethrough Example")
    layer["textDecoration"] = "none"


def solve_task_21(state):
    """Change 'Page Title' letter case to uppercase."""
    layer = find_layer(state, "Page Title")
    layer["letterCase"] = "uppercase"


def solve_task_22(state):
    """Change 'Small Caps Header' letter case to lowercase."""
    layer = find_layer(state, "Small Caps Header")
    layer["letterCase"] = "lowercase"


def solve_task_23(state):
    """Change 'Body Text' direction to RTL."""
    layer = find_layer(state, "Body Text")
    layer["textDirection"] = "rtl"


def solve_task_24(state):
    """Change 'Arabic Welcome' direction to LTR."""
    layer = find_layer(state, "Arabic Welcome")
    layer["textDirection"] = "ltr"


def solve_task_25(state):
    """Set 'Body Text' paragraph spacing to 24."""
    layer = find_layer(state, "Body Text")
    layer["paragraphSpacing"] = 24


def solve_task_26(state):
    """Set 'Body Text' paragraph indent to 32."""
    layer = find_layer(state, "Body Text")
    layer["paragraphIndent"] = 32


def solve_task_27(state):
    """Enable hanging punctuation on 'Body Text'."""
    layer = find_layer(state, "Body Text")
    layer["hangingPunctuation"] = True


def solve_task_28(state):
    """Change 'Feature List' list style to numbered."""
    layer = find_layer(state, "Feature List")
    layer["listStyle"] = "numbered"


def solve_task_29(state):
    """Change 'Step Instructions' list style to bulleted."""
    layer = find_layer(state, "Step Instructions")
    layer["listStyle"] = "bulleted"


def solve_task_30(state):
    """Set 'Feature List' list spacing to 8."""
    layer = find_layer(state, "Feature List")
    layer["listSpacing"] = 8


def solve_task_31(state):
    """Enable hanging list on 'Pricing Tiers'."""
    layer = find_layer(state, "Pricing Tiers")
    layer["hangingList"] = True


def solve_task_32(state):
    """Enable truncation on 'Body Text' with maxLines 5."""
    layer = find_layer(state, "Body Text")
    layer["truncation"] = {"enabled": True, "maxLines": 5}


def solve_task_33(state):
    """Disable truncation on 'Truncated Preview'."""
    layer = find_layer(state, "Truncated Preview")
    layer["truncation"] = {"enabled": False, "maxLines": None}


def solve_task_34(state):
    """Change 'Truncated Preview' max lines to 5."""
    layer = find_layer(state, "Truncated Preview")
    layer["truncation"] = {"enabled": True, "maxLines": 5}


def solve_task_35(state):
    """Enable vertical trim on 'Page Title'."""
    layer = find_layer(state, "Page Title")
    layer["verticalTrim"] = True


def solve_task_36(state):
    """Disable vertical trim on 'Variable Font Demo'."""
    layer = find_layer(state, "Variable Font Demo")
    layer["verticalTrim"] = False


def solve_task_37(state):
    """Disable 'calt' on 'Page Title'."""
    layer = find_layer(state, "Page Title")
    layer["openTypeFeatures"]["calt"] = False


def solve_task_38(state):
    """Disable 'zero' on 'Code Sample'."""
    layer = find_layer(state, "Code Sample")
    layer["openTypeFeatures"]["zero"] = False


def solve_task_39(state):
    """Enable 'ss01' on 'Page Title'."""
    layer = find_layer(state, "Page Title")
    layer["openTypeFeatures"]["ss01"] = True


def solve_task_40(state):
    """Set 'Variable Font Demo' wght to 700."""
    layer = find_layer(state, "Variable Font Demo")
    layer["variableAxes"]["wght"] = 700


def solve_task_41(state):
    """Set 'Variable Font Demo' slnt to -10."""
    layer = find_layer(state, "Variable Font Demo")
    layer["variableAxes"]["slnt"] = -10


def solve_task_42(state):
    """Create text style 'Heading/H4'."""
    next_id = state.get("_nextTextStyleId", 100)
    prefs = state["preferences"]
    style = {
        "id": f"ts_{str(next_id).zfill(3)}",
        "name": "Heading/H4",
        "fontFamily": prefs["defaultFontFamily"],
        "fontStyle": prefs["defaultFontStyle"],
        "fontSize": prefs["defaultFontSize"],
        "lineHeight": deepcopy(prefs["defaultLineHeight"]),
        "letterSpacing": deepcopy(prefs["defaultLetterSpacing"]),
        "paragraphSpacing": 0,
        "paragraphIndent": 0,
        "textDecoration": "none",
        "letterCase": "none",
        "listStyle": "none",
        "openTypeFeatures": {"liga": True, "kern": True},
        "description": "Quaternary heading",
        "createdAt": "2026-03-07T00:00:00Z",
        "updatedAt": "2026-03-07T00:00:00Z",
    }
    state["textStyles"].append(style)
    state["_nextTextStyleId"] = next_id + 1


def solve_task_43(state):
    """Delete text style 'Heading/Display' and detach from layers."""
    style = find_style(state, "Heading/Display")
    style_id = style["id"]
    state["textStyles"] = [s for s in state["textStyles"] if s["id"] != style_id]
    for layer in state["textLayers"]:
        if layer.get("textStyleId") == style_id:
            layer["textStyleId"] = None


def solve_task_44(state):
    """Edit 'Body/Regular' style fontSize to 18, update dependent layers."""
    style = find_style(state, "Body/Regular")
    style["fontSize"] = 18
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


def solve_task_45(state):
    """Apply 'Body/Small' to 'Feature List'."""
    layer = find_layer(state, "Feature List")
    style = find_style(state, "Body/Small")
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


def solve_task_46(state):
    """Detach text style from 'Page Title'."""
    layer = find_layer(state, "Page Title")
    layer["textStyleId"] = None


def solve_task_47(state):
    """Change 'Indented Quote' font to Georgia."""
    layer = find_layer(state, "Indented Quote")
    layer["fontFamily"] = "Georgia"
    # Georgia is not variable
    layer["variableAxes"] = {}


def solve_task_48(state):
    """Disable smart quotes."""
    state["preferences"]["smartQuotes"] = False


def solve_task_49(state):
    """Disable smart symbols."""
    state["preferences"]["smartSymbols"] = False


def solve_task_50(state):
    """Change default font family to Roboto."""
    state["preferences"]["defaultFontFamily"] = "Roboto"


def solve_task_51(state):
    """Change default font size to 14."""
    state["preferences"]["defaultFontSize"] = 14


def solve_task_52(state):
    """Change default alignment to center."""
    state["preferences"]["defaultHorizontalAlign"] = "center"


def solve_task_53(state):
    """Change default text direction to RTL."""
    state["preferences"]["defaultTextDirection"] = "rtl"


def solve_task_54(state):
    """Change spelling language to French."""
    state["preferences"]["spellingLanguage"] = "French"


def solve_task_55(state):
    """Disable snap to grid."""
    state["preferences"]["snapToGrid"] = False


def solve_task_56(state):
    """Disable show font preview."""
    state["preferences"]["showFontPreview"] = False


def solve_task_57(state):
    """Change nudge amount to 4."""
    state["preferences"]["nudgeAmount"] = 4


def solve_task_58(state):
    """Change big nudge amount to 20."""
    state["preferences"]["bigNudgeAmount"] = 20


def solve_task_59(state):
    """Change 'Call to Action' width to 320."""
    layer = find_layer(state, "Call to Action")
    layer["width"] = 320


def solve_task_60(state):
    """Change 'Call to Action' height to 72."""
    layer = find_layer(state, "Call to Action")
    layer["height"] = 72


def solve_task_61(state):
    """Disable hanging list on 'Feature List'."""
    layer = find_layer(state, "Feature List")
    layer["hangingList"] = False


def solve_task_62(state):
    """Disable hanging punctuation on 'Indented Quote'."""
    layer = find_layer(state, "Indented Quote")
    layer["hangingPunctuation"] = False


def solve_task_63(state):
    """Change default font style to Bold."""
    state["preferences"]["defaultFontStyle"] = "Bold"


def solve_task_64(state):
    """Set 'Step Instructions' list spacing to 10."""
    layer = find_layer(state, "Step Instructions")
    layer["listSpacing"] = 10


def solve_task_65(state):
    """Change 'Pricing Tiers' list style to bulleted."""
    layer = find_layer(state, "Pricing Tiers")
    layer["listStyle"] = "bulleted"


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
    parser = argparse.ArgumentParser(description="Figma Text & Typography function-task sanity check")
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
