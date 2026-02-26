# Verifier Sanity Check Guide

## What It Is

A verifier sanity check confirms that **verifiers correctly recognize a solved task**. For each task, it directly constructs the expected end-state (bypassing the agent entirely), then runs the verifier and asserts it returns `True`.

## Why It's Not Cheating

The evaluation stack has three independent layers:

| Layer | Tests | Method |
|-------|-------|--------|
| **Verifier sanity check** | Do verifiers detect correct state? | Apply state directly, run verifier |
| **Agent evaluation** | Can the agent perform tasks? | Agent interacts with UI, verifier checks result |
| **Manual spot-check** | Is everything end-to-end correct? | Human performs task, verifier checks result |

The sanity check tests layer 1 only. A passing sanity check means "the verifier is not buggy." It says nothing about whether an agent can complete the task. Conversely, a *failing* sanity check means the verifier is broken — it would produce false negatives during real evaluation, undermining results.

### What it catches

- Field name typos (`role` vs `role.name`)
- Hardcoded IDs that don't match seed data
- Inverted boolean logic (`is not True` vs `is not False`)
- Missing cross-reference checks (verifier checks a secondary data location the solve forgot to update)
- Stale expectations that no longer match task instructions

## Architecture

### Core Loop

For each task:

```
1. Reset environment to seed state
2. Read the clean seed state
3. Compute the expected end-state (the "solve")
4. Write the end-state back to the environment
5. Run the verifier — assert it passes
```

The solve function applies the **minimum state changes** needed to satisfy the verifier. It bypasses the UI entirely — no browser, no agent, no clicking. This makes it deterministic and fast.

### Solve Functions Are Inverses of Verifiers

Each solve function is derived directly from the corresponding verifier. Read the verifier line by line, then write the state mutation that satisfies every check:

```
Verifier checks X          →  Solve produces X
Verifier checks absence    →  Solve removes the entity
Verifier checks relationship →  Solve creates the relationship
```

If the verifier doesn't check a field, the solve doesn't need to set it. The solve is the verifier's inverse — nothing more, nothing less.

## Key Design Principles

### 1. Name-Based Lookups Over Hardcoded IDs

Entity IDs are an implementation detail of the seed data. If a new entity is inserted or ordering changes, hardcoded IDs silently break.

```python
# Fragile — breaks if seed data changes
user_id = 6
group_id = 7

# Robust — stays in sync with seed data
user = find_entity(state["users"], name="Emma Wilson")
group = find_entity(state["groups"], name="CI/CD")
```

Write simple lookup helpers that search by name. If an entity isn't found, fail loudly — that's a seed data mismatch worth knowing about.

### 2. Match the Serialized Data Shape

Verifiers read state after JSON serialization. The solve must produce data in the same shape — structured objects, not plain strings. See [task-design-guide.md § Verifier Conventions](task-design-guide.md#verifier-conventions) for the full explanation.

Define constants for enums/structured values once, reuse everywhere.

### 3. Honor State Invariants

Many applications maintain the same data in multiple locations (e.g., a denormalized user record in two different arrays). If the verifier checks both locations, the solve must update both. Identify these invariants upfront and write a sync helper.

### 4. Clean Up Cascading References on Deletion

When a solve deletes an entity, it must also remove all foreign-key references:

```
Delete project →  also remove project memberships, project shares, etc.
Delete group   →  also remove subgroups, projects, memberships, shares
```

Even if the verifier only checks one of these, cleaning up all references is defensive and matches real application behavior.

### 5. Use the Environment's ID Counters

When creating new entities, use whatever auto-increment counter the environment provides. Don't pick arbitrary IDs that might collide with existing data.

### 6. Derive Seed State From the Source of Truth

If seed data is defined in JavaScript, SQL, or another format, evaluate it programmatically rather than duplicating it as Python dicts. Duplication drifts.

For JavaScript seed data, pipe it through `node -` and parse the JSON output. For SQL fixtures, query the database. The point is: one source of truth, one derivation path.

> **Note:** In practice, existing sanity checks (e.g., gitlab-org-management) construct the expected state directly in Python rather than evaluating the JS source. This is pragmatic when the seed data is stable, but be aware that the Python representation can drift from the JS source over time.

## Parallel Execution

For speed, run multiple tasks concurrently. Each worker needs an **isolated environment** (its own server/database instance on a unique port). Workers pull tasks from a shared pool or receive pre-partitioned batches.

Per-worker flow:
1. Start isolated environment on assigned port
2. Seed the environment (so resets have a baseline to restore)
3. Loop: reset → solve → verify → collect result
4. Tear down environment

Use `concurrent.futures.ThreadPoolExecutor` or equivalent. Since each worker has its own environment, there are no shared-state race conditions.

## CLI Conventions

```
python3 sanity_check_{real|function}.py                      # All tasks, sequential
python3 sanity_check_{real|function}.py --workers N          # N parallel environments
python3 sanity_check_{real|function}.py --task-id <id>       # Single task (for debugging)
python3 sanity_check_{real|function}.py --port <base>        # Custom base port
```

Single-task mode is critical for debugging — when a task fails, you need fast iteration.

## Output Conventions

```
  PASS  task_e1       Group 'DevOps Team' created with correct visibility.
  FAIL  task_m3       Expected role 'Owner', got 'Maintainer'.

23/24 passed
Failed: task_m3
```

Exit code 0 if all pass, 1 if any fail (CI-friendly).

## Debugging a Failure

When a task fails, the bug is in the solve function or the verifier (never the agent — there is no agent). To diagnose:

1. **Read the verifier** line by line. Identify exactly which check fails.
2. **Read the solve function.** Does it produce what the verifier expects?
3. **Inspect the state.** Add a print between step 4 (write state) and step 5 (verify) to dump the relevant slice of state.
4. **Common root causes:**
   - Shape mismatch (string vs object, flat vs nested)
   - Lookup returns wrong entity (name typo, duplicate names)
   - State sync forgotten (updated primary location but not secondary)
   - Verifier has a hardcoded ID that doesn't match seed data
   - Verifier checks a field the solve didn't set

## Implementation Checklist

For each new web app:

- [ ] Read every verifier. Catalog what each one checks (field names, entities, conditions).
- [ ] Identify the seed data source. Write a function that loads it into Python.
- [ ] Identify the state shape: fields, ID counters, sync invariants.
- [ ] Write lookup helpers for each entity type.
- [ ] Define constants for enums/structured values (roles, visibility levels, etc.).
- [ ] Write one solve function per task, derived from the verifier.
- [ ] Test: single task → all tasks → parallel.
