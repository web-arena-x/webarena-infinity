You are adding harder evaluation tasks to `apps/{app-name}`. This is hardening round {round_number}.

## Context: Agent Evaluation Results

{hardening_analysis}

Results directory: `{results_path}`
Read history.json files in the results directory for passed tasks to understand HOW agents solve them — their action sequences, navigation patterns, and reasoning.

## Instructions

1. **Analyze the app.** Read the app code under `apps/{app-name}/` (index.html, js/, css/) to understand all UI features, navigation paths, and available actions.

2. **Review existing tasks.** Read `apps/{app-name}/tasks.json` to see what's already covered. Do NOT modify existing tasks, verifiers, or solvers.

3. **Analyze agent behavior.** Read history.json files from `{results_path}` for tasks that passed — especially those that passed easily (few steps, low elapsed time). Identify patterns the agent relies on and strategies it uses.

4. **Generate {tasks_per_round} new harder tasks.** Apply techniques from `docs/task-hardening-guide.md`:
   - Discovery: require finding info before acting
   - Indirect references: describe targets by properties, not names
   - Chained operations: step N depends on step N-1
   - Bulk conditional: complex filters defining scope
   - Cross-feature: span multiple entity types
   - Disambiguation: similar entities, must pick the right one
   - Non-obvious UI paths: actions behind context menus, nested pages

   Weight toward medium (~40%) and hard (~50%), with a few easy (~10%) for regression.

5. **Continue task IDs** from the highest existing ID number. Never reuse an existing task ID.

6. **Append** new tasks to `apps/{app-name}/tasks.json`. Do not remove or modify existing entries.

7. **Create verifiers** in `apps/{app-name}/tasks/` following the patterns in existing verifiers and `docs/real-task-design-guide.md`.

8. **Add solvers** to `apps/{app-name}/sanity_check_real.py` following `docs/verifier-sanity-check.md`. Each solver must programmatically produce the state that makes its verifier pass.

## Constraints

- Follow `docs/real-task-design-guide.md` for task and verifier design
- Follow `docs/task-hardening-guide.md` for hardening techniques
- Follow `docs/verifier-sanity-check.md` for sanity check patterns
- Do NOT modify existing tasks, verifiers, solvers, or app code
- All tasks must be completable through the UI by a human
- Every verifier must be deterministic