# Mirror-Mirror Progress

## Project Goal

Build a scalable pipeline that **auto-generates web-app testing environments** from documentation, then **evaluates AI agents** on those environments. Each environment is a self-contained single-page web app with programmatic task verifiers.

## What Exists

### Reference App (Hand-Built)

- **`apps/gitlab-org-management/`** — GitLab org management clone (gold-standard reference)
- **`apps/gitlab-org-management-no-guide/`** — Variant without design guide (for ablation)

### Generated Apps (from Pipeline)

| App | Doc Source | Best Pass Rate |
|-----|-----------|----------------|
| `apps/linear-account-settings/` | `user-manuals/linear/02-account` | 86.7% (Gemini) |
| `apps/shopify-web-performance/` | `user-manuals/shopify/web-performance` | 70.0% (Gemini) |
| `apps/shopify-theme-editor/` | `user-manuals/shopify/themes` | 53.3% (Gemini) |

### Documentation Sources

`apps/user-manuals/` contains full product documentation for Linear, GitLab, and Shopify — used as input for environment generation.

### Design Docs

`docs/` has 6 guides: environment protocol, evaluation/audit, task design, verifier sanity checks, web-app design, and evaluation harness architecture.

## Evaluation Harness

- `evaluation/run_eval.py` — single-threaded eval runner
- `evaluation/run_eval_parallel.py` — parallel worker pool eval runner
- Results stored inside each app: `apps/{app}/results/{model}_{timestamp}/`
- Reports track per-task pass/fail, screenshots, and step-by-step agent actions

## Infrastructure (AWS Pipeline)

| Component | Instance | Script |
|---|---|---|
| **Controller** | t3.medium | `infra/orchestrator.py` — dispatches jobs via SQS |
| **Env Generators** | m5.xlarge | `infra/env_worker.py` — generates apps with Claude Code |
| **Agent Testers** | c5.4xlarge | `infra/agent_worker.py` — runs browser agent eval against apps |

Flow: Controller → SQS → Env Generator (generate → sanity check → commit) → SQS → Agent Tester (eval → commit results) → SQS → Env Generator (audit → revise) → loop up to 3 iterations.

### Environment Manifest

`infra/env_manifest.jsonl` — each line maps a descriptive `env_id` to a `docs_path`:

```
linear-account-settings  → apps/user-manuals/linear/02-account
gitlab-plan-and-track    → apps/user-manuals/gitlab/topics/plan_and_track.md
shopify-dynamic-checkout → apps/user-manuals/shopify/dynamic-checkout
shopify-web-performance  → apps/user-manuals/shopify/web-performance
shopify-theme-editor     → apps/user-manuals/shopify/themes
```

### Branch Strategy

Branch name = `env_id` directly (no `env-` prefix). Branches inherit everything from main; a `.claudeignore` file hides irrelevant apps and docs from Claude Code, so nothing is deleted.

## Pipeline Run History

### Run 1 — Failed

Generated 5 envs (`env-001` through `env-005`). All generated but quality was insufficient. All removed from main.

**Bugs found & fixed:**
1. Results never committed — `.gitignore` had `results/` blocking `git add`
2. Audit prompt too vague — didn't tell Claude to read `report.html`/`results.json`
3. Missing `frontend-design` plugin on remote EC2
4. Eval-done SQS message stealing between parallel workers
5. Git concurrency issues — added `_git_lock` and worktree pruning

### Run 2 — Failed

All 5 envs reported `generation_failed` immediately. Claude Code returned empty stdout with rc=0.

**Root cause:** `claude --print` produces no output without a TTY. `subprocess.run()` doesn't provide one.

**Fix:** Replaced subprocess with tmux-based invocation. Each worker runs Claude inside a named tmux session (`claude-W0`, `claude-W1`, ...) for PTY + live observability.

### Run 3 — Success

Generated 3 working environments with iterative audit:

| Env | Pass Rate | Notes |
|-----|-----------|-------|
| linear-account-settings | 86.7% | 26/30 tasks passing |
| shopify-web-performance | 70.0% | 21/30 tasks passing |
| shopify-theme-editor | 53.3% | 16/30 tasks, regenerated once |

## Recent Changes (2026-02-24)

- Moved all product docs to `apps/user-manuals/` (was scattered under `apps/{product}/docs/`)
- Replaced opaque `env-001` IDs with descriptive names (`linear-account-settings`, etc.)
- Eval results now default to `apps/{app}/results/` (was `evaluation/results/`)
- Seed branches use `.claudeignore` instead of `git rm` to hide irrelevant files
- `collect_results.py` reads env_ids from manifest instead of numeric iteration

## Observations

- Documentation quality is the most important factor for generation quality
- Models are good at finding evaluation bugs and correcting errors across iterations
- Browser cache state causes tricky false failures
- Cross-app data consistency emerges naturally when referencing existing apps
