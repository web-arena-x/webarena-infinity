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

def find_entity(collection, **kwargs):
    for item in collection:
        if all(item.get(k) == v for k, v in kwargs.items()):
            return item
    key_str = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
    raise ValueError(f"Entity not found: {key_str}")

def find_app(state, name):
    return find_entity(state["apps"], name=name)

def find_theme(state, name):
    return find_entity(state["themes"], name=name)

def find_page(state, name):
    return find_entity(state["pages"], name=name)

def find_event(state, title):
    return find_entity(state["events"], title=title)

def find_alert(state, name):
    return find_entity(state["alertRules"], name=name)

def find_optimization(state, title):
    return find_entity(state["optimizations"], title=title)

def find_report(state, name):
    return find_entity(state["savedReports"], name=name)

# ── Seed state construction via Node ───────────────────────────

def get_seed_state():
    """Evaluate js/data.js through Node and return the seed state dict."""
    data_js_path = os.path.join(SCRIPT_DIR, "js", "data.js")
    with open(data_js_path) as f:
        js_code = f.read()

    js_code += """
console.log(JSON.stringify({
    _seedVersion: SEED_DATA_VERSION,
    store: STORE,
    currentUser: CURRENT_USER,
    themes: THEMES,
    apps: APPS,
    pages: PAGES,
    performanceRecords: PERFORMANCE_RECORDS,
    events: EVENTS,
    performanceBudgets: PERFORMANCE_BUDGETS,
    alertRules: ALERT_RULES,
    optimizations: OPTIMIZATIONS,
    savedReports: SAVED_REPORTS,
    _nextThemeId: 7,
    _nextAppId: 11,
    _nextPageId: 13,
    _nextEventId: 9,
    _nextAlertId: 7,
    _nextOptimizationId: 9,
    _nextReportId: 5
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
    """Change store name to 'Urban Threads Boutique'."""
    state["store"]["name"] = "Urban Threads Boutique"

def solve_task_e2(state):
    """Uninstall 'Hotjar Behavior Analytics'."""
    app = find_app(state, "Hotjar Behavior Analytics")
    app["installed"] = False
    app["installedAt"] = None
    app["status"] = "available"

def solve_task_e3(state):
    """Mark 'Compress hero banner image on homepage' as completed."""
    opt = find_optimization(state, "Compress hero banner image on homepage")
    opt["status"] = "completed"

def solve_task_e4(state):
    """Delete 'CLS Regression Alert' alert rule."""
    state["alertRules"] = [a for a in state["alertRules"] if a["name"] != "CLS Regression Alert"]

def solve_task_e5(state):
    """Delete 'Product Page CLS Report' saved report."""
    state["savedReports"] = [r for r in state["savedReports"] if r["name"] != "Product Page CLS Report"]

def solve_task_e6(state):
    """Disable 'LCP Budget Exceeded' alert rule."""
    alert = find_alert(state, "LCP Budget Exceeded")
    alert["enabled"] = False

def solve_task_e7(state):
    """Enable password protection."""
    state["store"]["passwordProtected"] = True

def solve_task_e8(state):
    """Dismiss 'Defer Klaviyo popup script loading' optimization."""
    opt = find_optimization(state, "Defer Klaviyo popup script loading")
    opt["status"] = "dismissed"

def solve_task_e9(state):
    """Pause monitoring for 'Style Guide Blog'."""
    page = find_page(state, "Style Guide Blog")
    page["monitored"] = False

def solve_task_e10(state):
    """Remove event 'Valentines Day sale ended'."""
    state["events"] = [e for e in state["events"] if e["title"] != "Valentines Day sale ended"]

def solve_task_m1(state):
    """Activate 'Refresh' theme."""
    for t in state["themes"]:
        t["active"] = False
    find_theme(state, "Refresh")["active"] = True

def solve_task_m2(state):
    """Create alert 'Collection Page LCP' - LCP > 3000, pageType=collection."""
    aid = state["_nextAlertId"]; state["_nextAlertId"] += 1
    state["alertRules"].append({
        "id": aid,
        "name": "Collection Page LCP",
        "metric": "lcp",
        "condition": "greater_than",
        "threshold": 3000,
        "pageType": "collection",
        "deviceType": "all",
        "enabled": True,
        "notifyEmail": True,
        "createdAt": "2026-02-19T00:00:00Z"
    })

def solve_task_m3(state):
    """Install 'Yotpo Reviews & UGC'."""
    app = find_app(state, "Yotpo Reviews & UGC")
    app["installed"] = True
    app["installedAt"] = "2026-02-19T00:00:00Z"
    app["status"] = "active"

def solve_task_m4(state):
    """Add page 'FAQ Page' with path /pages/faq, type page."""
    pid = state["_nextPageId"]; state["_nextPageId"] += 1
    state["pages"].append({
        "id": pid,
        "path": "/pages/faq",
        "name": "FAQ Page",
        "type": "page",
        "monitored": True,
        "priority": "medium"
    })

def solve_task_m5(state):
    """Create saved report 'Mobile CLS Trends'."""
    rid = state["_nextReportId"]; state["_nextReportId"] += 1
    state["savedReports"].append({
        "id": rid,
        "name": "Mobile CLS Trends",
        "metric": "cls",
        "reportType": "over_time",
        "filters": {
            "deviceType": "mobile",
            "dateRange": "last_30_days",
            "pageType": "all"
        },
        "createdAt": "2026-02-19T00:00:00Z"
    })

def solve_task_m6(state):
    """Update LCP budget: target=2000, warning=3000."""
    state["performanceBudgets"]["lcp"]["target"] = 2000
    state["performanceBudgets"]["lcp"]["warning"] = 3000

def solve_task_m7(state):
    """Add event 'Migrated to new image CDN'."""
    eid = state["_nextEventId"]; state["_nextEventId"] += 1
    state["events"].append({
        "id": eid,
        "date": "2026-02-19T00:00:00Z",
        "type": "code_change",
        "title": "Migrated to new image CDN",
        "description": "",
        "metric": "lcp",
        "impact": "positive"
    })

def solve_task_m8(state):
    """Dawn theme: stickyHeader=false, cartType=page."""
    dawn = find_theme(state, "Dawn")
    dawn["settings"]["stickyHeader"] = False
    dawn["settings"]["cartType"] = "page"

def solve_task_m9(state):
    """Create optimization 'Minify custom JavaScript files'."""
    oid = state["_nextOptimizationId"]; state["_nextOptimizationId"] += 1
    state["optimizations"].append({
        "id": oid,
        "title": "Minify custom JavaScript files",
        "description": "",
        "metric": "inp",
        "priority": "high",
        "status": "pending",
        "estimatedImpact": "",
        "category": "scripts",
        "pageAffected": "*",
        "createdAt": "2026-02-19T00:00:00Z"
    })

def solve_task_m10(state):
    """Update event 'Installed PageFly Builder' -> title + impact."""
    event = find_event(state, "Installed PageFly Builder")
    event["title"] = "Installed PageFly Landing Page Builder"
    event["impact"] = "neutral"

def solve_task_h1(state):
    """Uninstall 'Privy Pop Ups' and add event."""
    app = find_app(state, "Privy Pop Ups")
    app["installed"] = False
    app["installedAt"] = None
    app["status"] = "available"
    eid = state["_nextEventId"]; state["_nextEventId"] += 1
    state["events"].append({
        "id": eid,
        "date": "2026-02-19T00:00:00Z",
        "type": "app_uninstalled",
        "title": "Uninstalled Privy Pop Ups",
        "description": "",
        "metric": "cls",
        "impact": "positive"
    })

def solve_task_h2(state):
    """Activate Craft, enable lazyLoading, paginationLimit=32."""
    for t in state["themes"]:
        t["active"] = False
    craft = find_theme(state, "Craft")
    craft["active"] = True
    craft["settings"]["lazyLoading"] = True
    craft["settings"]["paginationLimit"] = 32

def solve_task_h3(state):
    """Create 'Cart INP Alert' and enable 'Product Page CLS'."""
    aid = state["_nextAlertId"]; state["_nextAlertId"] += 1
    state["alertRules"].append({
        "id": aid,
        "name": "Cart INP Alert",
        "metric": "inp",
        "condition": "greater_than",
        "threshold": 250,
        "pageType": "cart",
        "deviceType": "mobile",
        "enabled": True,
        "notifyEmail": True,
        "createdAt": "2026-02-19T00:00:00Z"
    })
    cls_alert = find_alert(state, "Product Page CLS")
    cls_alert["enabled"] = True

def solve_task_h4(state):
    """Install GTM, set containerId=GTM-W8X3K9P, deferLoading=true."""
    app = find_app(state, "Google Tag Manager")
    app["installed"] = True
    app["installedAt"] = "2026-02-19T00:00:00Z"
    app["status"] = "active"
    app["settings"]["containerId"] = "GTM-W8X3K9P"
    app["settings"]["deferLoading"] = True

def solve_task_h5(state):
    """Create optimization 'Implement responsive images...' and complete Instafeed one."""
    oid = state["_nextOptimizationId"]; state["_nextOptimizationId"] += 1
    state["optimizations"].append({
        "id": oid,
        "title": "Implement responsive images with srcset",
        "description": "",
        "metric": "lcp",
        "priority": "critical",
        "status": "pending",
        "estimatedImpact": "400ms LCP improvement",
        "category": "images",
        "pageAffected": "/products/*",
        "createdAt": "2026-02-19T00:00:00Z"
    })
    existing = find_optimization(state, "Remove unused Instafeed scripts from product pages")
    existing["status"] = "completed"

def solve_task_h6(state):
    """Create saved report 'Cart Performance Analysis'."""
    rid = state["_nextReportId"]; state["_nextReportId"] += 1
    state["savedReports"].append({
        "id": rid,
        "name": "Cart Performance Analysis",
        "metric": "inp",
        "reportType": "by_page_url",
        "filters": {
            "deviceType": "mobile",
            "dateRange": "last_7_days",
            "pageType": "cart"
        },
        "createdAt": "2026-02-19T00:00:00Z"
    })

def solve_task_h7(state):
    """Store name + domain + CLS budget."""
    state["store"]["name"] = "Urban Threads Co."
    state["store"]["domain"] = "shop.urbanthreads.com"
    state["performanceBudgets"]["cls"]["target"] = 0.05
    state["performanceBudgets"]["cls"]["warning"] = 0.15

def solve_task_h8(state):
    """Add page 'Loyalty Program' and event 'Launched loyalty program page'."""
    pid = state["_nextPageId"]; state["_nextPageId"] += 1
    state["pages"].append({
        "id": pid,
        "path": "/pages/loyalty-program",
        "name": "Loyalty Program",
        "type": "page",
        "monitored": True,
        "priority": "high"
    })
    eid = state["_nextEventId"]; state["_nextEventId"] += 1
    state["events"].append({
        "id": eid,
        "date": "2026-02-19T00:00:00Z",
        "type": "custom",
        "title": "Launched loyalty program page",
        "description": "",
        "metric": "all",
        "impact": "neutral"
    })

def solve_task_h9(state):
    """Dawn settings + Homepage LCP Monitor threshold=3000."""
    dawn = find_theme(state, "Dawn")
    dawn["settings"]["pageTransitions"] = True
    dawn["settings"]["animationsEnabled"] = True
    dawn["settings"]["paginationLimit"] = 12
    alert = find_alert(state, "Homepage LCP Monitor")
    alert["threshold"] = 3000

def solve_task_h10(state):
    """Uninstall Instafeed and Lucky Orange."""
    for name in ["Instafeed Instagram Feed", "Lucky Orange Analytics"]:
        app = find_app(state, name)
        app["installed"] = False
        app["installedAt"] = None
        app["status"] = "available"

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
          f"{len(seed_state['apps'])} apps, "
          f"{len(seed_state['pages'])} pages")

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
