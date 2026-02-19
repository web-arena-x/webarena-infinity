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

# ── Name-based lookup helpers ──────────────────────────────────

def find_theme(state, name):
    return next(t for t in state["themes"] if t["name"] == name)

def find_theme_settings(state, theme_id):
    return next(ts for ts in state["themeSettings"] if ts["themeId"] == theme_id)

def find_section(state, section_id):
    return next(s for s in state["sections"] if s["id"] == section_id)

def find_block(state, block_id):
    return next(b for b in state["blocks"] if b["id"] == block_id)

def find_template(state, template_id):
    return next(t for t in state["templates"] if t["id"] == template_id)

# ── Seed state construction via Node ───────────────────────────

def get_seed_state():
    """Evaluate js/data.js through Node and return the seed state dict."""
    data_js_path = os.path.join(SCRIPT_DIR, "js", "data.js")
    with open(data_js_path) as f:
        js_code = f.read()

    js_code += """
console.log(JSON.stringify({
    _seedVersion: SEED_DATA_VERSION,
    currentUser: CURRENT_USER,
    themes: THEMES,
    templates: TEMPLATES,
    sections: SECTIONS,
    blocks: BLOCKS,
    themeSettings: THEME_SETTINGS,
    _nextThemeId: 8,
    _nextTemplateId: 33,
    _nextSectionId: 42,
    _nextBlockId: 33,
    _nextColorSchemeId: 6
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

# ── Per-task solve functions ───────────────────────────────────

def solve_task_e1(state):
    """Rename theme 'Craft' to 'Artisan'."""
    theme = find_theme(state, "Craft")
    theme["name"] = "Artisan"

def solve_task_e2(state):
    """Delete theme 'Crave' (id 6) and clean up."""
    theme_id = 6
    state["themes"] = [t for t in state["themes"] if t["id"] != theme_id]
    # Clean up templates
    template_ids = [t["id"] for t in state["templates"] if t["themeId"] == theme_id]
    state["templates"] = [t for t in state["templates"] if t["themeId"] != theme_id]
    # Clean up sections
    section_ids = [s["id"] for s in state["sections"] if s["themeId"] == theme_id]
    state["sections"] = [s for s in state["sections"] if s["themeId"] != theme_id]
    # Clean up blocks
    state["blocks"] = [b for b in state["blocks"] if b["themeId"] != theme_id]
    # Clean up theme settings
    state["themeSettings"] = [ts for ts in state["themeSettings"] if ts["themeId"] != theme_id]

def solve_task_e3(state):
    """Publish 'Sense' (make it live, demote Dawn to draft)."""
    for t in state["themes"]:
        if t["status"] == "live":
            t["status"] = "draft"
    sense = find_theme(state, "Sense")
    sense["status"] = "live"

def solve_task_e4(state):
    """Duplicate Dawn — create a new 'Copy of Dawn' theme."""
    dawn = find_theme(state, "Dawn")
    new_id = state["_nextThemeId"]
    state["_nextThemeId"] += 1
    new_theme = copy.deepcopy(dawn)
    new_theme["id"] = new_id
    new_theme["name"] = "Copy of Dawn"
    new_theme["status"] = "draft"
    state["themes"].append(new_theme)

    # Duplicate templates
    template_map = {}
    dawn_templates = [t for t in state["templates"] if t["themeId"] == dawn["id"]]
    for t in dawn_templates:
        new_tid = state["_nextTemplateId"]
        state["_nextTemplateId"] += 1
        template_map[t["id"]] = new_tid
        new_t = copy.deepcopy(t)
        new_t["id"] = new_tid
        new_t["themeId"] = new_id
        state["templates"].append(new_t)

    # Duplicate sections
    section_map = {}
    dawn_sections = [s for s in state["sections"] if s["themeId"] == dawn["id"]]
    for s in dawn_sections:
        new_sid = state["_nextSectionId"]
        state["_nextSectionId"] += 1
        section_map[s["id"]] = new_sid
        new_s = copy.deepcopy(s)
        new_s["id"] = new_sid
        new_s["themeId"] = new_id
        new_s["templateId"] = template_map.get(s["templateId"], s["templateId"])
        state["sections"].append(new_s)

    # Duplicate blocks
    dawn_blocks = [b for b in state["blocks"] if b["themeId"] == dawn["id"]]
    for b in dawn_blocks:
        new_bid = state["_nextBlockId"]
        state["_nextBlockId"] += 1
        new_b = copy.deepcopy(b)
        new_b["id"] = new_bid
        new_b["themeId"] = new_id
        new_b["sectionId"] = section_map.get(b["sectionId"], b["sectionId"])
        state["blocks"].append(new_b)

    # Duplicate theme settings
    dawn_settings = find_theme_settings(state, dawn["id"])
    new_settings = copy.deepcopy(dawn_settings)
    new_settings["themeId"] = new_id
    state["themeSettings"].append(new_settings)

def solve_task_e5(state):
    """Add theme 'Minimalist'."""
    new_id = state["_nextThemeId"]
    state["_nextThemeId"] += 1
    state["themes"].append({
        "id": new_id,
        "name": "Minimalist",
        "status": "draft",
        "version": "1.0",
        "architecture": "online_store_2.0",
        "source": "shopify",
        "price": 0,
        "lastSaved": "2026-01-01T00:00:00Z",
        "createdAt": "2026-01-01T00:00:00Z",
        "updatedAt": "2026-01-01T00:00:00Z",
        "updateAvailable": False,
        "updateVersion": None,
        "previewUrl": "",
        "customCss": "",
        "themeStyle": "default"
    })

    # Add default templates and sections
    default_types = ["product", "collection", "page", "blog", "cart", "search"]
    for dtype in default_types:
        tid = state["_nextTemplateId"]
        state["_nextTemplateId"] += 1
        state["templates"].append({
            "id": tid, "themeId": new_id,
            "name": "Default " + dtype, "type": dtype,
            "handle": dtype, "isDefault": True
        })
        hid = state["_nextSectionId"]
        state["_nextSectionId"] += 1
        state["sections"].append({
            "id": hid, "templateId": tid, "themeId": new_id,
            "type": "header", "name": "Header", "area": "header",
            "position": 0, "hidden": False, "customCss": "", "colorSchemeId": 1
        })
        fid = state["_nextSectionId"]
        state["_nextSectionId"] += 1
        state["sections"].append({
            "id": fid, "templateId": tid, "themeId": new_id,
            "type": "footer", "name": "Footer", "area": "footer",
            "position": 0, "hidden": False, "customCss": "", "colorSchemeId": 1
        })

    # Add theme settings
    state["themeSettings"].append({
        "themeId": new_id,
        "logo": {"url": "", "altText": "", "width": 120},
        "favicon": {"url": ""},
        "colors": [
            {"id": 1, "name": "Scheme 1", "isDefault": True, "background": "#ffffff",
             "backgroundGradient": "", "text": "#121212", "solidButtonBg": "#121212",
             "solidButtonText": "#ffffff", "outlineButton": "#121212", "shadow": "#121212"},
            {"id": 2, "name": "Scheme 2", "isDefault": False, "background": "#f3f3f3",
             "backgroundGradient": "", "text": "#1a1a1a", "solidButtonBg": "#1a1a1a",
             "solidButtonText": "#f3f3f3", "outlineButton": "#1a1a1a", "shadow": "#1a1a1a"},
            {"id": 3, "name": "Accent", "isDefault": False, "background": "#2c5f2d",
             "backgroundGradient": "", "text": "#ffffff", "solidButtonBg": "#97bc62",
             "solidButtonText": "#2c5f2d", "outlineButton": "#ffffff", "shadow": "#1a3a1c"},
            {"id": 4, "name": "Dark Mode", "isDefault": False, "background": "#1a1a2e",
             "backgroundGradient": "", "text": "#e0e0e0", "solidButtonBg": "#e94560",
             "solidButtonText": "#ffffff", "outlineButton": "#e94560", "shadow": "#0f0f1a"},
            {"id": 5, "name": "Warm Earth", "isDefault": False, "background": "#fdf6ec",
             "backgroundGradient": "", "text": "#3d2c1e", "solidButtonBg": "#c8553d",
             "solidButtonText": "#fdf6ec", "outlineButton": "#c8553d", "shadow": "#3d2c1e"}
        ],
        "typography": {"headingFont": "Assistant", "bodyFont": "Assistant", "fontSizeScale": 100},
        "layout": {"pageWidth": 1200, "sectionSpacing": 36, "gridHorizontalSpacing": 12, "gridVerticalSpacing": 12},
        "animations": {"revealOnScroll": True, "hoverEffect": "none"},
        "buttons": {"style": "rounded", "borderRadius": 4},
        "variantPills": {"style": "rounded"},
        "inputs": {"style": "outlined", "borderRadius": 4},
        "badges": {"salePosition": "top-left", "saleShape": "rectangle", "soldOutPosition": "bottom-left", "soldOutShape": "rectangle"},
        "socialLinks": {"instagram": "https://instagram.com/northwindtraders", "tiktok": "", "facebook": "https://facebook.com/northwindtraders", "pinterest": "https://pinterest.com/northwindtraders", "twitter": "https://twitter.com/northwindtraders", "youtube": "", "linkedin": "", "snapchat": "", "tumblr": "", "vimeo": ""},
        "searchBehavior": {"enableSuggestions": True, "showVendor": True, "showPrice": True},
        "currencyFormat": {"showCurrencyCode": False},
        "cart": {"type": "drawer", "showVendor": False, "enableNote": True, "emptyDrawerCollection": "", "cartColorSchemeId": 1},
        "customCss": ""
    })

def solve_task_e6(state):
    """Show (unhide) 'Related products' section in Dawn's default product template."""
    section = find_section(state, 6)  # Section id 6 = Related products
    section["hidden"] = False

def solve_task_e7(state):
    """Remove 'Email signup' section (id 7) from Dawn's Default product template."""
    state["blocks"] = [b for b in state["blocks"] if b.get("sectionId") != 7]
    state["sections"] = [s for s in state["sections"] if s["id"] != 7]

def solve_task_e8(state):
    """Change heading font to 'Montserrat' for Dawn theme."""
    settings = find_theme_settings(state, 1)
    settings["typography"]["headingFont"] = "Montserrat"

def solve_task_e9(state):
    """Disable search suggestions for Dawn theme."""
    settings = find_theme_settings(state, 1)
    settings["searchBehavior"]["enableSuggestions"] = False

def solve_task_e10(state):
    """Enable currency code display for Dawn theme."""
    settings = find_theme_settings(state, 1)
    settings["currencyFormat"]["showCurrencyCode"] = True

def solve_task_m1(state):
    """Add a Rich text section to Dawn's Default product template."""
    sid = state["_nextSectionId"]
    state["_nextSectionId"] += 1
    state["sections"].append({
        "id": sid, "templateId": 1, "themeId": 1,
        "type": "rich-text", "name": "Rich text", "area": "template",
        "position": 5, "hidden": False, "customCss": "", "colorSchemeId": 1
    })

def solve_task_m2(state):
    """Rename 'Image banner' section (id 3) to 'Hero Section'."""
    section = find_section(state, 3)
    section["name"] = "Hero Section"

def solve_task_m3(state):
    """Change cart type to 'page' for Dawn theme."""
    settings = find_theme_settings(state, 1)
    settings["cart"]["type"] = "page"

def solve_task_m4(state):
    """Change hover effect to '3d-lift' for Dawn theme."""
    settings = find_theme_settings(state, 1)
    settings["animations"]["hoverEffect"] = "3d-lift"

def solve_task_m5(state):
    """Remove 'Aisha Patel' block (id 22) from Team members section."""
    state["blocks"] = [b for b in state["blocks"] if b["id"] != 22]

def solve_task_m6(state):
    """Set YouTube URL for Dawn theme."""
    settings = find_theme_settings(state, 1)
    settings["socialLinks"]["youtube"] = "https://youtube.com/@northwindtraders"

def solve_task_m7(state):
    """Add a new color scheme to Dawn theme."""
    settings = find_theme_settings(state, 1)
    new_id = state["_nextColorSchemeId"]
    state["_nextColorSchemeId"] += 1
    settings["colors"].append({
        "id": new_id, "name": "Scheme 6", "isDefault": False,
        "background": "#ffffff", "backgroundGradient": "",
        "text": "#121212", "solidButtonBg": "#121212",
        "solidButtonText": "#ffffff", "outlineButton": "#121212",
        "shadow": "#121212"
    })

def solve_task_m8(state):
    """Duplicate 'Featured collection' section (id 5) in Default product template."""
    source = find_section(state, 5)
    new_sid = state["_nextSectionId"]
    state["_nextSectionId"] += 1
    new_section = copy.deepcopy(source)
    new_section["id"] = new_sid
    new_section["name"] = source["name"] + " (copy)"
    new_section["position"] = source["position"] + 1

    # Shift later sections
    for s in state["sections"]:
        if (s["templateId"] == source["templateId"] and
            s["area"] == source["area"] and
            s["position"] > source["position"] and
            s["id"] != new_sid):
            s["position"] += 1

    state["sections"].append(new_section)

    # Duplicate blocks belonging to section 5
    # (No blocks for section 5 in seed data, but be safe)
    source_blocks = [b for b in state["blocks"] if b["sectionId"] == 5]
    for sb in source_blocks:
        new_bid = state["_nextBlockId"]
        state["_nextBlockId"] += 1
        new_b = copy.deepcopy(sb)
        new_b["id"] = new_bid
        new_b["sectionId"] = new_sid
        state["blocks"].append(new_b)

def solve_task_m9(state):
    """Change button style to 'pill' for Dawn theme."""
    settings = find_theme_settings(state, 1)
    settings["buttons"]["style"] = "pill"

def solve_task_m10(state):
    """Change sale badge position to 'top-right' and shape to 'circle'."""
    settings = find_theme_settings(state, 1)
    settings["badges"]["salePosition"] = "top-right"
    settings["badges"]["saleShape"] = "circle"

def solve_task_h1(state):
    """Update blocks in 'Our story' section (id 23)."""
    # Block 18 = Heading, Block 19 = Content (text)
    heading = find_block(state, 18)
    heading["settings"]["text"] = "Our Values"

    content = find_block(state, 19)
    content["settings"]["text"] = "We are committed to sustainability and ethical sourcing in everything we do."

def solve_task_h2(state):
    """Add Rich text section to Contact template (5), then add Heading block."""
    sid = state["_nextSectionId"]
    state["_nextSectionId"] += 1
    state["sections"].append({
        "id": sid, "templateId": 5, "themeId": 1,
        "type": "rich-text", "name": "Rich text", "area": "template",
        "position": 2, "hidden": False, "customCss": "", "colorSchemeId": 1
    })

    bid = state["_nextBlockId"]
    state["_nextBlockId"] += 1
    state["blocks"].append({
        "id": bid, "sectionId": sid, "themeId": 1,
        "type": "heading", "name": "Heading",
        "position": 0, "hidden": False,
        "settings": {"text": "", "size": "h2"}
    })

def solve_task_h3(state):
    """Rename 'Accent' color scheme to 'Forest' and change background."""
    settings = find_theme_settings(state, 1)
    scheme = next(c for c in settings["colors"] if c["id"] == 3)
    scheme["name"] = "Forest"
    scheme["background"] = "#1b4332"

def solve_task_h4(state):
    """Change cart type to 'popup' and disable cart note."""
    settings = find_theme_settings(state, 1)
    settings["cart"]["type"] = "popup"
    settings["cart"]["enableNote"] = False

def solve_task_h5(state):
    """Set TikTok, LinkedIn URLs and clear Pinterest."""
    settings = find_theme_settings(state, 1)
    settings["socialLinks"]["tiktok"] = "https://tiktok.com/@northwindtraders"
    settings["socialLinks"]["linkedin"] = "https://linkedin.com/company/northwindtraders"
    settings["socialLinks"]["pinterest"] = ""

def solve_task_h6(state):
    """Add new Announcement block to Announcement bar (section 2)."""
    bid = state["_nextBlockId"]
    state["_nextBlockId"] += 1
    state["blocks"].append({
        "id": bid, "sectionId": 2, "themeId": 1,
        "type": "announcement", "name": "Announcement",
        "position": 2, "hidden": False,
        "settings": {"text": "", "link": ""}
    })

def solve_task_h7(state):
    """Remove 'Sale announcement' (block 2), hide 'Subheading' (block 4)."""
    state["blocks"] = [b for b in state["blocks"] if b["id"] != 2]
    subheading = find_block(state, 4)
    subheading["hidden"] = True

def solve_task_h8(state):
    """Change fonts and page width for Dawn theme."""
    settings = find_theme_settings(state, 1)
    settings["typography"]["headingFont"] = "Playfair Display"
    settings["typography"]["bodyFont"] = "Lato"
    settings["layout"]["pageWidth"] = 1400

def solve_task_h9(state):
    """Publish 'Impact' and rename to 'Impact Pro'."""
    for t in state["themes"]:
        if t["status"] == "live":
            t["status"] = "draft"
    impact = find_theme(state, "Impact")
    impact["status"] = "live"
    impact["name"] = "Impact Pro"

def solve_task_h10(state):
    """Remove 'Dark Mode' color scheme (id 4), change input style to 'filled'."""
    settings = find_theme_settings(state, 1)
    settings["colors"] = [c for c in settings["colors"] if c["id"] != 4]
    settings["inputs"]["style"] = "filled"

    # Reset sections using this color scheme to default
    for s in state["sections"]:
        if s.get("themeId") == 1 and s.get("colorSchemeId") == 4:
            s["colorSchemeId"] = 1


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

# ── Server lifecycle ───────────────────────────────────────────

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

# ── Verifier loading ──────────────────────────────────────────

def load_verifier(task_id):
    path = os.path.join(TASKS_DIR, f"{task_id}.py")
    spec = importlib.util.spec_from_file_location(task_id, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.verify

# ── Worker: run a batch of tasks on one server ────────────────

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

# ── Main ───────────────────────────────────────────────────────

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
    print(f"Seed loaded: {len(seed_state['themes'])} themes, "
          f"{len(seed_state['templates'])} templates, "
          f"{len(seed_state['sections'])} sections, "
          f"{len(seed_state['blocks'])} blocks")

    num_workers = min(args.workers, len(task_ids))
    all_results = []

    if num_workers <= 1:
        all_results = run_tasks(task_ids, args.port, seed_state)
    else:
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
