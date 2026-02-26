# Evaluation Audit Guide

Principles for deciding when to update tasks, verifiers, or UI after reviewing agent evaluation results.

## Core Principle: Feasibility Is the Only Standard

If a human can complete the task through the UI, the task and verifier are correct — regardless of agent pass rate. A 0% pass rate on a feasible task is an agent problem, not a website problem.

The evaluation measures agent capability, not task difficulty targets. Adjusting tasks to improve pass rates would undermine the benchmark.

## When to Change

Update the task, verifier, or seed data when the failure is **not** the agent's fault:

| Root Cause | Action |
|------------|--------|
| **Verifier bug** — verifier rejects a correctly solved task (false negative) | Fix the verifier. Run sanity check to confirm. |
| **Impossible task** — the UI genuinely cannot perform the requested action | Remove or redesign the task. |
| **Ambiguous instruction** — multiple reasonable interpretations lead to different outcomes | Clarify the instruction. |
| **Seed data mismatch** — verifier references entities that don't exist in the seed state | Fix seed data or verifier to be consistent. |
| **Sanity check failure** — the solve-then-verify cycle fails | Debug the solve function or verifier (see [verifier-sanity-check.md](verifier-sanity-check.md)). |

## When NOT to Change

Do **not** update tasks, verifiers, or UI for these agent-side failures:

| Failure Pattern | Why It's Not a Bug |
|----------------|-------------------|
| Agent can't find a button that exists on a different page | Navigation is part of the task. |
| Agent navigates to an external site and gets stuck | Agent left the app; the app is not at fault. |
| Agent selects the wrong value from a dropdown | Agent error, not UI error. |
| Agent reports success but verifier shows incorrect state | Agent falsely claimed completion. |
| Agent can't complete multi-step tasks | Complexity is intentional for hard tasks. |
| Low pass rate alone | Pass rate reflects agent capability, not task quality. |

## Decision Flowchart

When a task fails during an agent evaluation:

```
1. Run the verifier sanity check for that task.
   - If sanity check FAILS → verifier or solve bug. Fix it.
   - If sanity check PASSES → verifier is correct. Continue.

2. Manually attempt the task in the UI.
   - If you CANNOT complete it → impossible task or UI bug. Fix it.
   - If you CAN complete it → task is feasible. Continue.

3. Attribute the failure to the agent.
   - Categorize: navigation failure, wrong value, false claim, etc.
   - No changes to the benchmark needed.
```

## Common False Positives

These look like bugs but aren't:

**"Successfully completed" but verifier fails** — The agent claimed success without actually performing the action correctly. Trust the verifier over the agent's self-report. The verifier checks actual application state.

**"CAPTCHA blocked me"** — The agent navigated to an external search engine instead of staying within the app. The app doesn't have CAPTCHAs; the agent left the app.

## The Three-Layer Testing Model

Each layer tests something different. Don't conflate them.

| Layer | Question | Method | What a Failure Means |
|-------|----------|--------|---------------------|
| **Verifier sanity check** | Does the verifier detect correct state? | Apply state directly, run verifier | Verifier bug |
| **Agent evaluation** | Can the agent perform the task? | Agent interacts with UI, verifier checks | Agent limitation |
| **Manual spot-check** | Is the full pipeline correct? | Human performs task, verifier checks | Task, UI, or verifier issue |

A failure at layer 2 (agent evaluation) only warrants changes if it's also reproducible at layer 1 (verifier bug) or layer 3 (task/UI issue). If the verifier sanity check passes and a human can do the task, the agent evaluation failure is purely an agent limitation.

See [verifier-sanity-check.md](verifier-sanity-check.md) for details on implementing layer 1.
