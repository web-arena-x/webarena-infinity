# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Project Is

Mirror-Mirror is a scalable pipeline for auto-generating web-app testing environments and evaluating AI browser agents (Gemini, GPT, Claude) against them. The pipeline: generates HTML/CSS/JS apps from documentation using Claude Code → runs browser agents on task suites → audits results and iterates.

## Commands

### Local Evaluation

```bash
# Single task (starts server automatically, results go to apps/linear-account-settings/results/)
python evaluation/run_eval.py --model gemini --task-id task_e1 --web-app apps/linear-account-settings

# Filter by difficulty
python evaluation/run_eval.py --model gpt --difficulty easy --web-app apps/linear-account-settings

# Parallel evaluation (local servers on ports 8001+)
python evaluation/run_eval_parallel.py --model claude --workers 4 --web-app apps/linear-account-settings

# Parallel evaluation against remote pre-running servers
python evaluation/run_eval_parallel.py --model gemini --workers 8 \
    --env-host ec2-host --base-port 8001 --web-app apps/linear-account-settings
```

### Docker

```bash
docker compose up                    # 4 gitlab + 4 linear instances
docker compose up --scale gitlab=20  # scale up
```

### Running an App Server Directly

Servers use `SimpleHTTPRequestHandler` and serve files relative to CWD, so you must `cd` into the app directory first:

```bash
cd apps/gmail && python3 server.py --port 8000
```

### AWS Pipeline

```bash
# Launch infrastructure
bash infra/setup/vpc_and_sg.sh
bash infra/setup/seed_branches.sh
bash infra/setup/launch_pipeline.sh 5

# Seed jobs
python infra/orchestrator.py --seed-only --manifest infra/env_manifest.jsonl

# On env generator EC2
python infra/env_worker.py

# On agent tester EC2
python infra/agent_worker.py
```

### Package Management

Uses `uv` (not pip). Python >=3.12 required. The single dependency is `browser-use>=0.11.9`. Shared venv lives at `~/mirror-mirror/.venv` — run `uv sync` from the repo root, then `uv pip install playwright && uv run python -m playwright install chromium`.

## Architecture

### Pipeline Data Flow

```
orchestrator.py → GENERATE_QUEUE (SQS) → env_worker.py
    generates app with Claude Code → sanity check → commit to env branch
    → EVAL_QUEUE → agent_worker.py
        runs browser agents → results.json + report.html → EVAL_DONE_QUEUE
    → env_worker.py audits results → revises app (up to 3 iterations)
    → PIPELINE_DONE_QUEUE → orchestrator.py monitors completion
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

### Infrastructure Parallelism

- **Env generators:** 5 parallel workers per EC2 instance, each in a separate git worktree with isolated port range (worker 0: ports 8001-8008, worker 1: 8009-8016, etc.)
- **File-based git locking** (`_git_lock`) prevents concurrent worktree operations
- **tmux-based Claude invocation** — required because `claude --print` needs a PTY to produce stdout; workers run inside tmux sessions for both PTY and live observability (`tmux attach -t claude-W0`)

### Reference Apps

`apps/linear/` and `apps/gitlab-org-management/` are hand-built gold-standard implementations. Use these as references when creating new environments.

### Design Documentation

- `docs/web-app-design-guide.md` — how to build apps (UI patterns, data richness)
- `docs/task-design-guide.md` — how to write tasks and verifiers
- `docs/environment-protocol.md` — the API contract above in full detail
- `docs/verifier-sanity-check.md` — automated sanity check authoring
- `docs/evaluation-audit-guide.md` — how to audit and revise after eval

### Environment Manifest

`infra/env_manifest.jsonl` defines environments to generate. Each line maps an `env_id` to a `docs_path` containing the source documentation.

## Lessons Learned

### Multi-Agent Module Integration

When delegating large JS files (views.js, app.js, etc.) to separate background agents:

- Define cross-module contracts (function signatures, route formats, data flow) **before** delegating
- Do a post-integration review tracing all cross-module calls (especially render pipelines)
- Sanity checks test state logic only, not UI rendering — always test in a browser or simulate the full render path in Node
- Common failure modes: interface mismatches (missing args, wrong route formats, double sort/page)
