#!/usr/bin/env python3
"""
Verifier sanity check — for each task, directly apply the expected state
changes via the API, run the verifier, and assert it passes.

Usage:
    python3 sanity_check.py                      # Run all 30 tasks sequentially
    python3 sanity_check.py --workers 4           # Run with 4 parallel server workers
    python3 sanity_check.py --task-id task_e1     # Run a single task
    python3 sanity_check.py --port 9000           # Custom base port
"""

import argparse
import copy
import importlib.util
import json
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TASKS_DIR = os.path.join(SCRIPT_DIR, "tasks")

# ── Helpers ────────────────────────────────────────────────────────

def find_section(state, name, template_id="home"):
    return next(s for s in state["sections"]
                if s["name"] == name and s["templateId"] == template_id)

def find_section_by_type(state, section_type, template_id="home", group="template"):
    return next(s for s in state["sections"]
                if s["type"] == section_type and s["templateId"] == template_id and s["group"] == group)

# ── Seed state construction via Node ───────────────────────────────

def get_seed_state():
    """Evaluate js/data.js through Node and return the seed state dict."""
    data_js_path = os.path.join(SCRIPT_DIR, "js", "data.js")
    with open(data_js_path) as f:
        js_code = f.read()

    js_code += """
console.log(JSON.stringify({
    _seedVersion: SEED_DATA_VERSION,
    theme: { name: "Dawn", status: "Live" },
    themeSettings: THEME_SETTINGS,
    templates: TEMPLATES,
    sections: SECTIONS,
    products: PRODUCTS,
    collections: COLLECTIONS,
    markets: MARKETS,
    _nextSectionId: _nextSectionId,
    _nextBlockId: _nextBlockId,
    _nextColorSchemeId: _nextColorSchemeId
}));
"""
    result = subprocess.run(
        ["node", "-"],
        input=js_code,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"Failed to evaluate seed data: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    return json.loads(result.stdout.strip())

# ── Per-task solve functions ───────────────────────────────────────

def solve_task_e1(state):
    """Change heading font to 'Playfair Display'."""
    state["themeSettings"]["typography"]["headingFont"] = "Playfair Display"

def solve_task_e2(state):
    """Enable showCurrencyCodes."""
    state["themeSettings"]["currencyFormat"]["showCurrencyCodes"] = True

def solve_task_e3(state):
    """Set Instagram link."""
    state["themeSettings"]["socialMedia"]["instagram"] = "https://instagram.com/mystorefront"

def solve_task_e4(state):
    """Hide the Rich text section."""
    section = find_section(state, "Rich text")
    section["visible"] = False

def solve_task_e5(state):
    """Remove the third slide from Slideshow."""
    section = find_section(state, "Slideshow")
    slides = [b for b in section["blocks"] if b["type"] == "slide"]
    slides.sort(key=lambda b: b["order"])
    # Remove third slide (index 2)
    third_slide = slides[2]
    section["blocks"] = [b for b in section["blocks"] if b["id"] != third_slide["id"]]

def solve_task_e6(state):
    """Change cart type to 'Page'."""
    state["themeSettings"]["cart"]["type"] = "Page"

def solve_task_e7(state):
    """Set hover effect to 'Vertical lift'."""
    state["themeSettings"]["animations"]["hoverEffect"] = "Vertical lift"

def solve_task_e8(state):
    """Enable revealSectionsOnScroll."""
    state["themeSettings"]["animations"]["revealSectionsOnScroll"] = True

def solve_task_e9(state):
    """Set body font size scale to 120."""
    state["themeSettings"]["typography"]["bodyFontSizeScale"] = 120

def solve_task_e10(state):
    """Disable search suggestions."""
    state["themeSettings"]["searchBehavior"]["enableSuggestions"] = False

def solve_task_m1(state):
    """Add new color scheme with background '#f0e6d3' and text '#1a1a2e'."""
    scheme_id = "scheme_" + str(state["_nextColorSchemeId"])
    state["_nextColorSchemeId"] += 1
    state["themeSettings"]["colors"]["schemes"].append({
        "id": scheme_id,
        "name": "Scheme " + scheme_id.split("_")[1],
        "background": "#f0e6d3",
        "backgroundGradient": "",
        "text": "#1a1a2e",
        "solidButtonBackground": "#121212",
        "solidButtonLabel": "#ffffff",
        "outlineButton": "#121212",
        "shadow": "#121212"
    })

def solve_task_m2(state):
    """Add new 'Image with text' section to template area."""
    template_sections = [s for s in state["sections"]
                         if s["templateId"] == "home" and s["group"] == "template"]
    max_order = max(s["order"] for s in template_sections) if template_sections else 0
    section_id = "section_" + str(state["_nextSectionId"])
    state["_nextSectionId"] += 1
    state["sections"].append({
        "id": section_id,
        "type": "image_with_text",
        "name": "Image with text",
        "templateId": "home",
        "group": "template",
        "order": max_order + 1,
        "visible": True,
        "collapsed": False,
        "settings": {"colorSchemeId": "scheme_1"},
        "blocks": []
    })

def solve_task_m3(state):
    """Change heading font to 'Montserrat' and scale to 130."""
    state["themeSettings"]["typography"]["headingFont"] = "Montserrat"
    state["themeSettings"]["typography"]["headingFontSizeScale"] = 130

def solve_task_m4(state):
    """Move Featured collection above Image banner."""
    fc = find_section(state, "Featured collection")
    ib = find_section(state, "Image banner")
    # Swap orders so FC is before IB
    fc_order = fc["order"]
    ib_order = ib["order"]
    if fc_order > ib_order:
        fc["order"] = ib_order
        ib["order"] = fc_order

def solve_task_m5(state):
    """Set page width to 1200 and section spacing to 36."""
    state["themeSettings"]["layout"]["pageWidth"] = 1200
    state["themeSettings"]["layout"]["sectionSpacing"] = 36

def solve_task_m6(state):
    """Enable showVendor and showPrice in search behavior."""
    state["themeSettings"]["searchBehavior"]["showVendor"] = True
    state["themeSettings"]["searchBehavior"]["showPrice"] = True

def solve_task_m7(state):
    """Set cart type to Drawer and enable cart note."""
    state["themeSettings"]["cart"]["type"] = "Drawer"
    state["themeSettings"]["cart"]["enableCartNote"] = True

def solve_task_m8(state):
    """Set Facebook and YouTube links."""
    state["themeSettings"]["socialMedia"]["facebook"] = "https://facebook.com/mystore"
    state["themeSettings"]["socialMedia"]["youtube"] = "https://youtube.com/@mystore"

def solve_task_m9(state):
    """Enable showSecondImageOnHover and showVendor in product cards."""
    state["themeSettings"]["productCards"]["showSecondImageOnHover"] = True
    state["themeSettings"]["productCards"]["showVendor"] = True

def solve_task_m10(state):
    """Duplicate the Slideshow section."""
    src = find_section(state, "Slideshow")
    new_section_id = "section_" + str(state["_nextSectionId"])
    state["_nextSectionId"] += 1

    template_sections = [s for s in state["sections"]
                         if s["templateId"] == "home" and s["group"] == src["group"]]
    max_order = max(s["order"] for s in template_sections)

    new_blocks = []
    for b in src["blocks"]:
        new_block_id = "block_" + str(state["_nextBlockId"])
        state["_nextBlockId"] += 1
        new_block = copy.deepcopy(b)
        new_block["id"] = new_block_id
        new_block["sectionId"] = new_section_id
        new_blocks.append(new_block)

    new_section = copy.deepcopy(src)
    new_section["id"] = new_section_id
    new_section["name"] = src["name"] + " (copy)"
    new_section["order"] = max_order + 1
    new_section["blocks"] = new_blocks
    state["sections"].append(new_section)

def solve_task_h1(state):
    """Add color scheme with 4 specific colors."""
    scheme_id = "scheme_" + str(state["_nextColorSchemeId"])
    state["_nextColorSchemeId"] += 1
    state["themeSettings"]["colors"]["schemes"].append({
        "id": scheme_id,
        "name": "Scheme " + scheme_id.split("_")[1],
        "background": "#1a1a2e",
        "backgroundGradient": "",
        "text": "#eaeaea",
        "solidButtonBackground": "#e94560",
        "solidButtonLabel": "#ffffff",
        "outlineButton": "#121212",
        "shadow": "#121212"
    })

def solve_task_h2(state):
    """Add Multicolumn section then add Column block."""
    template_sections = [s for s in state["sections"]
                         if s["templateId"] == "home" and s["group"] == "template"]
    max_order = max(s["order"] for s in template_sections)
    section_id = "section_" + str(state["_nextSectionId"])
    state["_nextSectionId"] += 1
    block_id = "block_" + str(state["_nextBlockId"])
    state["_nextBlockId"] += 1
    state["sections"].append({
        "id": section_id,
        "type": "multicolumn",
        "name": "Multicolumn",
        "templateId": "home",
        "group": "template",
        "order": max_order + 1,
        "visible": True,
        "collapsed": False,
        "settings": {"colorSchemeId": "scheme_1"},
        "blocks": [{
            "id": block_id,
            "type": "column",
            "name": "Column",
            "sectionId": section_id,
            "order": 0,
            "visible": True,
            "settings": {}
        }]
    })

def solve_task_h3(state):
    """Apply Crave theme style, then override heading font to Bitter."""
    # Apply Crave style settings (matching what applyThemeStyle does)
    crave = next(s for s in [
        {"id": "crave", "settings": {
            "typography": {"headingFont": "Playfair Display", "headingFontSizeScale": 130,
                          "bodyFont": "Lato", "bodyFontSizeScale": 105},
            "buttons": {"borderRadius": 8, "shadow": "Small"},
            "animations": {"hoverEffect": "3D lift", "revealSectionsOnScroll": True}
        }}
    ] if s["id"] == "crave")

    for key, val in crave["settings"].get("typography", {}).items():
        state["themeSettings"]["typography"][key] = val
    for key, val in crave["settings"].get("buttons", {}).items():
        state["themeSettings"]["buttons"][key] = val
    for key, val in crave["settings"].get("animations", {}).items():
        state["themeSettings"]["animations"][key] = val
    state["themeSettings"]["activeThemeStyle"] = "crave"

    # Override heading font
    state["themeSettings"]["typography"]["headingFont"] = "Bitter"

def solve_task_h4(state):
    """Cart: type=Drawer, showVendor=true, enableCartNote=true, drawerCollection='Best Sellers'."""
    state["themeSettings"]["cart"]["type"] = "Drawer"
    state["themeSettings"]["cart"]["showVendor"] = True
    state["themeSettings"]["cart"]["enableCartNote"] = True
    state["themeSettings"]["cart"]["drawerCollection"] = "Best Sellers"

def solve_task_h5(state):
    """Layout: pageWidth=1400, sectionSpacing=48, gridHorizontalSpace=24, gridVerticalSpace=20."""
    state["themeSettings"]["layout"]["pageWidth"] = 1400
    state["themeSettings"]["layout"]["sectionSpacing"] = 48
    state["themeSettings"]["layout"]["gridHorizontalSpace"] = 24
    state["themeSettings"]["layout"]["gridVerticalSpace"] = 20

def solve_task_h6(state):
    """Add Image banner section, then add Heading and Button blocks."""
    template_sections = [s for s in state["sections"]
                         if s["templateId"] == "home" and s["group"] == "template"]
    max_order = max(s["order"] for s in template_sections)
    section_id = "section_" + str(state["_nextSectionId"])
    state["_nextSectionId"] += 1
    heading_block_id = "block_" + str(state["_nextBlockId"])
    state["_nextBlockId"] += 1
    button_block_id = "block_" + str(state["_nextBlockId"])
    state["_nextBlockId"] += 1
    state["sections"].append({
        "id": section_id,
        "type": "image_banner",
        "name": "Image banner",
        "templateId": "home",
        "group": "template",
        "order": max_order + 1,
        "visible": True,
        "collapsed": False,
        "settings": {"colorSchemeId": "scheme_1"},
        "blocks": [
            {
                "id": heading_block_id,
                "type": "heading",
                "name": "Heading",
                "sectionId": section_id,
                "order": 0,
                "visible": True,
                "settings": {}
            },
            {
                "id": button_block_id,
                "type": "button",
                "name": "Button",
                "sectionId": section_id,
                "order": 1,
                "visible": True,
                "settings": {}
            }
        ]
    })

def solve_task_h7(state):
    """Badges: salePosition='Top right', saleShape='Circle', soldOutPosition='Bottom right'."""
    state["themeSettings"]["badges"]["salePosition"] = "Top right"
    state["themeSettings"]["badges"]["saleShape"] = "Circle"
    state["themeSettings"]["badges"]["soldOutPosition"] = "Bottom right"

def solve_task_h8(state):
    """Add color scheme with gradient and white text."""
    scheme_id = "scheme_" + str(state["_nextColorSchemeId"])
    state["_nextColorSchemeId"] += 1
    state["themeSettings"]["colors"]["schemes"].append({
        "id": scheme_id,
        "name": "Scheme " + scheme_id.split("_")[1],
        "background": "#ffffff",
        "backgroundGradient": "linear-gradient(135deg, #667eea, #764ba2)",
        "text": "#ffffff",
        "solidButtonBackground": "#121212",
        "solidButtonLabel": "#ffffff",
        "outlineButton": "#121212",
        "shadow": "#121212"
    })

def solve_task_h9(state):
    """Set 5 social media links to greenleaf URLs."""
    state["themeSettings"]["socialMedia"]["facebook"] = "https://facebook.com/greenleaf"
    state["themeSettings"]["socialMedia"]["instagram"] = "https://instagram.com/greenleaf"
    state["themeSettings"]["socialMedia"]["twitter"] = "https://twitter.com/greenleaf"
    state["themeSettings"]["socialMedia"]["pinterest"] = "https://pinterest.com/greenleaf"
    state["themeSettings"]["socialMedia"]["youtube"] = "https://youtube.com/greenleaf"

def solve_task_h10(state):
    """Hide Announcement bar, move Newsletter to last in template, set page width to 1000."""
    # 1. Hide announcement bar
    announcement = next(s for s in state["sections"]
                        if s["name"] == "Announcement bar" and s["templateId"] == "home")
    announcement["visible"] = False

    # 2. Move Newsletter to last in template group
    template_sections = [s for s in state["sections"]
                         if s["templateId"] == "home" and s["group"] == "template"]
    newsletter = next(s for s in template_sections if s["name"] == "Newsletter")
    max_order = max(s["order"] for s in template_sections)
    newsletter["order"] = max_order + 1

    # 3. Set page width to 1000
    state["themeSettings"]["layout"]["pageWidth"] = 1000


SOLVERS = {
    "task_e1": solve_task_e1, "task_e2": solve_task_e2,
    "task_e3": solve_task_e3, "task_e4": solve_task_e4,
    "task_e5": solve_task_e5, "task_e6": solve_task_e6,
    "task_e7": solve_task_e7, "task_e8": solve_task_e8,
    "task_e9": solve_task_e9, "task_e10": solve_task_e10,
    "task_m1": solve_task_m1, "task_m2": solve_task_m2,
    "task_m3": solve_task_m3, "task_m4": solve_task_m4,
    "task_m5": solve_task_m5, "task_m6": solve_task_m6,
    "task_m7": solve_task_m7, "task_m8": solve_task_m8,
    "task_m9": solve_task_m9, "task_m10": solve_task_m10,
    "task_h1": solve_task_h1, "task_h2": solve_task_h2,
    "task_h3": solve_task_h3, "task_h4": solve_task_h4,
    "task_h5": solve_task_h5, "task_h6": solve_task_h6,
    "task_h7": solve_task_h7, "task_h8": solve_task_h8,
    "task_h9": solve_task_h9, "task_h10": solve_task_h10,
}

# ── Server lifecycle ───────────────────────────────────────────────

def start_server(port):
    return subprocess.Popen(
        [sys.executable, "server.py", "--port", str(port)],
        cwd=SCRIPT_DIR,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

def wait_for_server(port, timeout=10):
    url = f"http://localhost:{port}/"
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            r = requests.get(url, timeout=2)
            if r.status_code == 200:
                return True
        except requests.ConnectionError:
            pass
        time.sleep(0.3)
    return False

def stop_server(proc):
    if proc.poll() is not None:
        return
    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait()

# ── Verifier loading ──────────────────────────────────────────────

def load_verifier(task_id):
    path = os.path.join(TASKS_DIR, f"{task_id}.py")
    spec = importlib.util.spec_from_file_location(task_id, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.verify

# ── Worker: run a batch of tasks on one server ────────────────────

def run_tasks(task_ids, port, seed_state):
    """Start a server on *port*, run each task, return list of (task_id, passed, message)."""
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
                results.append((tid, False, "Failed to seed server state"))
            return results

        for tid in task_ids:
            try:
                # Reset to seed
                requests.post(f"{base}/api/reset", timeout=5)

                # Fetch clean seed state
                state = requests.get(f"{base}/api/state", timeout=5).json()

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

# ── Main ───────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Verifier sanity check")
    parser.add_argument("--workers", type=int, default=1,
                        help="Number of parallel server workers (default: 1)")
    parser.add_argument("--task-id", type=str,
                        help="Run a single task (e.g. task_e1)")
    parser.add_argument("--port", type=int, default=18000,
                        help="Base port for servers (default: 18000)")
    args = parser.parse_args()

    # Determine which tasks to run
    if args.task_id:
        task_ids = [args.task_id]
    else:
        with open(os.path.join(SCRIPT_DIR, "tasks.json")) as f:
            task_ids = [t["id"] for t in json.load(f)]

    for tid in task_ids:
        if tid not in SOLVERS:
            print(f"Unknown task: {tid}", file=sys.stderr)
            sys.exit(1)

    # Build seed state from js/data.js
    print("Loading seed state via Node...")
    seed_state = get_seed_state()
    print(f"Seed loaded: {len(seed_state['sections'])} sections, "
          f"{len(seed_state['products'])} products, "
          f"{len(seed_state['collections'])} collections")

    num_workers = min(args.workers, len(task_ids))
    all_results = []

    if num_workers <= 1:
        # Sequential — single server
        all_results = run_tasks(task_ids, args.port, seed_state)
    else:
        # Parallel — one server per worker, tasks round-robin partitioned
        chunks = [[] for _ in range(num_workers)]
        for i, tid in enumerate(task_ids):
            chunks[i % num_workers].append(tid)

        with ThreadPoolExecutor(max_workers=num_workers) as pool:
            futures = {
                pool.submit(run_tasks, chunk, args.port + i, seed_state): i
                for i, chunk in enumerate(chunks) if chunk
            }
            for f in as_completed(futures):
                all_results.extend(f.result())

    # Sort by original task order
    order = {tid: i for i, tid in enumerate(task_ids)}
    all_results.sort(key=lambda r: order.get(r[0], 999))

    # Print results
    print()
    passed_count = 0
    failed = []
    for tid, passed, message in all_results:
        status = "PASS" if passed else "FAIL"
        if passed:
            passed_count += 1
        else:
            failed.append(tid)
        print(f"  {status}  {tid:12s}  {message}")

    total = len(all_results)
    print(f"\n{passed_count}/{total} passed")
    if failed:
        print(f"Failed: {', '.join(failed)}")
        sys.exit(1)
    else:
        print("All verifiers passed!")

if __name__ == "__main__":
    main()
