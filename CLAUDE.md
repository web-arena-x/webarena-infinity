# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Project Is

Mirror-Mirror is a scalable pipeline for auto-generating web-app testing environments and evaluating AI browser agents (Gemini, GPT, Claude) against them. The pipeline: generates HTML/CSS/JS apps from documentation using Claude Code → runs browser agents on task suites → audits results and iterates.

## Commands

### Local Evaluation

```bash
# Single task (starts server automatically, results go to apps/<app>/results/)
python evaluation/run_eval_parallel.py --model gemini --task-id task_e1 --workers 1 --web-app apps/linear-account-settings

# Filter by difficulty
python evaluation/run_eval_parallel.py --model gpt --difficulty easy --workers 4 --web-app apps/linear-account-settings

# Parallel evaluation against remote pre-running servers
python evaluation/run_eval_parallel.py --model gemini --workers 8 \
    --env-host ec2-host --base-port 8001 --web-app apps/linear-account-settings
```

### Running an App Server Directly

Servers use `SimpleHTTPRequestHandler` and serve files relative to CWD, so you must `cd` into the app directory first:

```bash
cd apps/gmail && python3 server.py --port 8000
```

### AWS Pipeline

Each environment runs as a self-contained pipeline on one EC2 instance (no SQS, no cross-machine coordination).

```bash
# Launch one EC2 instance per environment in manifest
bash infra/setup/launch.sh --manifest infra/env_manifest.jsonl --model gemini

# SSH into each instance, then:
#   claude login
#   claude plugins install frontend-design
#   nohup python infra/pipeline.py --app-name <env_id> --docs-path <docs> \
#     --model gemini --workers 8 --push > /tmp/mirror-mirror-logs/pipeline.log 2>&1 &

# Monitor progress
bash infra/setup/monitor.sh

# Collect results from all branches
python infra/collect_results.py

# Tear down
bash infra/setup/teardown.sh --release-eips
```

### Package Management

Uses `uv` (not pip). Python >=3.12 required. The single dependency is `browser-use>=0.11.9`. Shared venv lives at `~/mirror-mirror/.venv` — run `uv sync` from the repo root, then `uv pip install playwright && uv run python -m playwright install chromium`.

## Architecture

### Pipeline Data Flow

Each environment runs independently on one EC2 instance via `infra/pipeline.py`:

```
pipeline.py (one instance per environment)
├─ Phase 1: Generate App (Claude CLI)
│   └─ Writes app code + APP_DESCRIPTION.md
├─ Phase 2: Function Tasks
│   ├─ 2a: Generate function tasks (Claude CLI, once)
│   │   └─ Sanity check (fix if needed) → commit
│   └─ 2b: Eval-Audit loop (up to max_iterations)
│       └─ eval → audit failures (Claude) → sanity check → commit
├─ Phase 3: Real Tasks
│   ├─ 3a: Generate real tasks (Claude CLI, once)
│   │   └─ Sanity check (fix if needed) → commit
│   └─ 3b: Eval-Audit loop (up to max_iterations)
│       └─ eval → audit failures (Claude) → sanity check → commit
├─ Phase 4: Task Hardening (N rounds, --hardening-rounds)
│   └─ Per round:
│       ├─ 4a: Analyze agent behavior + generate harder tasks (Claude)
│       │   └─ Reads history.json from results/, appends to tasks.json
│       │   └─ Sanity check (fix if needed, revert if irrecoverable) → commit
│       └─ 4b: Eval-Audit loop (new tasks only, via --task-id filter)
│           └─ eval → audit failures (Claude) → sanity check → commit
└─ Phase 5: Final Regression Eval
    └─ Full-suite eval on function tasks + real tasks (no audit)
```

### Environment Protocol (every app must follow)

Each app exposes a standard HTTP API consumed by the evaluation harness:

- `GET /api/state` — returns current app state JSON (read by verifiers)
- `PUT /api/state` — browser pushes state on every mutation
- `POST /api/reset` — restores seed state, sends SSE reset event
- `GET /api/events` — SSE stream for reset notifications
- `GET /*` — static file serving

**State sync contract:** Browser PUTs full state on first load → server captures as immutable `_seed_state` → browser PUTs on every mutation → verifiers read via GET → reset restores seed state and sends SSE event to browser.

### App Structure (each app under `apps/`)

```
{app-name}/
├── server.py          # HTTP server implementing the protocol above
├── index.html         # Entry point
├── js/                # app.js, state.js, views.js, components.js, data.js
├── css/styles.css
├── tasks.json         # 24 tasks: 8 easy, 8 medium, 8 hard
├── tasks/             # Verifier scripts (task_e1.py .. task_h8.py)
├── sanity_check.py    # Automated verifier validation
├── Dockerfile
└── results/           # Evaluation output per model run
```

### Verifier Pattern

Each `tasks/task_*.py` exports `verify(server_url: str) -> tuple[bool, str]`. Verifiers read `/api/state` and check conditions — they never interact with the UI.

### Key Design Constraints for Apps

- No native OS UI elements (`<select>`, `alert()`, `confirm()`, file pickers) — use custom JS-rendered equivalents
- Rich realistic seed data (10+ items per dropdown, varied formats)
- Form validation with required fields and conditional requirements
- Every value checked by a verifier must be achievable through the UI

### Infrastructure

- **One instance per environment** — each EC2 runs `pipeline.py` independently (m5.4xlarge, 16 vCPU, 64GB)
- **Elastic IPs** — stable across stop/start for persistent `claude login` sessions
- **Branch per environment** — commits at each checkpoint, push at end for results collection
- **`.claudeignore`** — generated locally (not committed) to hide other apps from Claude context

### Reference Apps

`apps/linear/` and `apps/gitlab-org-management/` are hand-built gold-standard implementations. Use these as references when creating new environments.

### Design Documentation

- `docs/web-app-design-guide.md` — how to build apps (UI patterns, data richness)
- `docs/task-design-guide.md` — how to write tasks and verifiers
- `docs/environment-protocol.md` — the API contract above in full detail
- `docs/verifier-sanity-check.md` — automated sanity check authoring
- `docs/evaluation-audit-guide.md` — how to audit and revise after eval
- `docs/task-hardening-guide.md` — how to generate harder tasks from agent behavior

### Environment Manifest

`infra/env_manifest.jsonl` defines environments to generate. Each line maps an `env_id` to a `docs_path` containing the source documentation.

## Lessons Learned

### Cross-Module Contract Mismatches (views.js ↔ app.js)

The #1 source of bugs in generated apps. No type system enforces consistency, so string keys drift between the HTML that views.js renders and the handler maps in app.js. **Always audit after generation:**

- **One dispatch mechanism per element.** Don't put `data-action` on elements that also have class-based handlers (`.email-star`, `.email-checkbox`). If both exist, `handleClick` ordering determines which fires — a subtle, silent bug.
- **Grep handler maps against rendered HTML.** Every key in `handleDropdownSelect`/`handleToggleChange`/`handleRadioChange` maps must appear verbatim as an ID or `name` in views.js. Watch for prefix drift (`settings-` vs `setting-`), casing drift (`camelCase` vs `kebab-case`), and suffix drift (`settings-language` vs `language-dropdown`).
- **Grep all `data-action="..."` values** in views.js/components.js and verify each has a `case` in `handleAction`. Missing cases fail silently (`console.warn` only).
- **Check verifier data shapes against data.js.** If seed data uses objects (`[{email, blockedAt}]`), verifiers must access the nested field, not compare against the object.

### Multi-Agent Module Integration

When delegating large JS files to separate background agents:

- Define cross-module contracts (function signatures, route formats, data flow) **before** delegating
- Do a post-integration review tracing all cross-module calls (especially render pipelines)
- Sanity checks test state logic only, not UI rendering — always test in a browser too

### Eval Harness Reliability

- `start_server()` auto-kills zombie processes on the target port before launching (`kill_port()` in `evaluation/server.py`)
- `agent.setup()` polls for seed state (up to 10s) rather than using a fixed sleep, handling slow browser startups under parallel load
- `GET /api/state` returns 404 until a browser PUTs state — this is by design, not a bug

### Results Management

- All `**/results/` directories are gitignored by default to keep diffs clean
- To promote a specific result for version control: `git add -f apps/<app>/results/<dir>/`
- Already-committed results remain tracked (gitignore only affects untracked files)
- Multi-run eval (`--repetitions N`) nests output under one parent dir: `run1/`, `run2/`, ..., `merged/` (with `success/` + `fail/`)
