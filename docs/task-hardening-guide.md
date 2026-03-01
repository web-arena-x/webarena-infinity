# Task Hardening Guide

How to generate harder evaluation tasks based on agent behavior analysis.

## Purpose

After an initial round of tasks has been evaluated, pass rates may be too high — agents solve most tasks easily. Task hardening adds **new, harder** tasks to the suite without modifying existing ones. It works by analyzing *how* agents solve tasks (not just pass/fail) and designing tasks that exploit agent weaknesses and disrupt common success strategies.

## Agent Behavior Analysis

Before generating harder tasks, read the agent's `history.json` files from the latest evaluation results to understand *how* the agent solves tasks. Look for:

### Action Sequences and Step Counts
- Which tasks are solved in very few steps (easy wins)?
- Which tasks take many steps but still pass (the agent struggled)?
- Which tasks exceed the max steps (agent got lost)?

### Navigation Patterns
- Does the agent navigate directly to the right page, or explore?
- Does it rely on visible navigation (sidebar, tabs) vs. search?
- Does it handle multi-page workflows or get stuck after the first page?

### Common Success Strategies
- Does the agent click the first matching element without verifying context?
- Does it read existing data before acting, or guess?
- Does it handle dropdowns/modals correctly every time, or intermittently?
- Does it use keyboard shortcuts vs. mouse clicks?

### Reasoning Quality
- From `model_output.thinking` (if available): does the agent plan ahead or react step-by-step?
- Does it verify its own work, or move on after a single attempt?
- Does it correctly interpret ambiguous instructions?

## Hardening Techniques

Use these techniques to design tasks that are genuinely challenging for agents while remaining natural and realistic for humans. The goal is not artificial complexity, but operational realism: discovery, interpretation, cross-feature reasoning, state awareness, and differentiated execution.


### 1. Exploratory Discovery (Goal-Driven, Multi-Source)

Require the agent to uncover information before acting — and not from a single obvious location. The instruction should embed discovery inside a meaningful objective.

**Make it harder by:**
- Requiring aggregation or comparison (ratios, trends, rankings).
- Pulling data from multiple sections (issues, milestones, teams, settings).
- Leaving the location of required data implicit.
- Basing the final action on derived insight.

**Example:**
> Identify the project with the highest ratio of overdue issues to total open issues, then switch it to weekly sprints starting next cycle.


### 2. Indirect & Relational References

Describe targets by behavior, relationships, or historical patterns rather than explicit names.

**Make it harder by:**
- Referencing time windows (e.g., “this quarter”).
- Using comparative metrics (fewest, highest, longest).
- Linking entities relationally (e.g., reassign from lowest performer to highest performer).

**Example:**
> Reassign issues owned by the team member who has resolved the fewest tickets this quarter to the person who resolved the most.


### 3. Chained, Dependent Operations

Ensure later steps depend on computed results from earlier steps. The agent must derive intermediate outputs before proceeding.

**Make it harder by:**
- Requiring name generation from discovered data.
- Creating new entities based on computed properties.
- Mixing configuration updates with content changes.

**Example:**
> Find the milestone with the longest overdue duration. Create a new milestone named “Recovery – [original milestone name]”, move all its open issues into it, and extend the deadline by 30 days from today.


### 4. Bulk Conditional Operations with Differentiated Treatment (Bulk & Distribute)

Avoid uniform bulk actions. Instead, segment the matching set and apply different treatments to different subgroups.

**Make it harder by:**
- Layering multiple filters.
- Introducing exceptions.
- Applying different actions per condition.
- Combining reassignment, movement, comments, and state changes.

**Example:**
> For all issues open longer than 45 days:
> - If assigned to Backend, move them to the “Stability” milestone.
> - If unassigned, assign them to the team lead.
> - If labeled “blocked”, add a comment requesting a status update instead of moving them.


### 5. Cross-Feature Orchestration

Span multiple entity types or sections of the application. The agent must navigate across different areas (issues, milestones, permissions, settings).

**Make it harder by:**
- Combining configuration changes with content updates.
- Linking planning artifacts to workflow controls.
- Requiring transitions between operational and administrative areas.

**Example:**
> Create a new milestone called “Q2 Hardening” in the API project. Move all high-priority unassigned issues into it, assign them to the engineering manager, and enable required approvals for that project’s merge requests.


### 6. Disambiguation Under Ambiguity

Introduce similar or near-duplicate entities that require careful selection based on subtle qualifiers.

**Make it harder by:**
- Using similarly named projects or milestones.
- Including archived or inactive entities.
- Referring to relative properties (most recently created, not archived, etc.).

**Example:**
> Extend the deadline of the “Design Review” milestone in the project that was created most recently — not the archived one — by two weeks.


### 7. Non-Obvious Navigation Paths

Require actions hidden behind nested settings, secondary panels, or context menus.

**Make it harder by:**
- Combining discovery with buried configuration changes.
- Requiring toggles in deep settings pages.
- Including multi-step navigation before modification.

**Example:**
> For the repository with the highest number of open pull requests, enable required reviews with at least 2 approvals and disable auto-merge.


### 8. State-Dependent Logic

The correct action depends on the current state. The agent must read before writing.

**Make it harder by:**
- Introducing branching logic.
- Including “leave unchanged” paths.
- Combining multiple conditional checks.

**Example:**
> If notifications are set to “All Activity”, change them to “Mentions Only”. If already “Mentions Only”, leave them. If disabled entirely, enable them but set to “Mentions Only”.


### Design Principles for Realistic Hard Tasks

To make tasks meaningfully challenging rather than artificially complex:

1. Tie actions to a realistic operational goal.
2. Require intermediate reasoning and derived insights.
3. Use differentiated bulk handling instead of uniform updates.
4. Introduce ambiguity that requires disambiguation.
5. Span multiple features or entity types.
6. Incorporate state checks and conditional branches.
7. Combine discovery, transformation, and configuration changes in one flow.

## Task ID Convention

Continue numbering from the highest existing task ID. For example, if the current suite ends at `task_h24`, new tasks start at:
- Easy: `task_e25`, `task_e26`, ...
- Medium: `task_m25`, `task_m26`, ...
- Hard: `task_h25`, `task_h26`, ...

Use the same numeric suffix across difficulties within a round to keep IDs tidy, but this is a convention, not a requirement. The critical rule is: **never reuse an existing task ID**.

## Difficulty Distribution

Weight new tasks toward harder difficulties:

| Difficulty | Proportion | Rationale |
|-----------|-----------|-----------|
| Easy | ~10% | Regression coverage — ensure basic functionality still works |
| Medium | ~40% | Sweet spot for measuring improvement |
| Hard | ~50% | Primary target — these are what hardening is for |

For a round of 20 tasks: ~2 easy, ~8 medium, ~10 hard.

## Quality Bar

Every hardened task must:

1. **Pass the sanity check.** The solve function must produce state that the verifier accepts.
2. **Be feasible for a human.** A person using the app's UI must be able to complete the task. If you can't describe the steps a human would take, the task is impossible.
3. **Be deterministic.** The verifier must produce the same result on the same state every time. No randomness, no timing dependencies.
4. **Not modify existing tasks.** Hardening *adds* tasks. Existing task IDs, instructions, verifiers, and solvers are never changed.
5. **Follow the real task design guide.** All principles from `docs/real-task-design-guide.md` apply — natural phrasing, no implementation leaks, unambiguous instructions.

## What NOT to Do

- **Don't make tasks impossible.** If a feature doesn't exist in the app, don't write a task for it.
- **Don't make tasks artificially tricky.** Misleading instructions or trick questions don't reflect real user needs.
- **Don't duplicate existing tasks.** Check the current task suite to avoid overlap.
- **Don't reference task IDs or verifier internals.** Instructions must read as natural user requests.
- **Don't modify the app's UI or state code.** Hardening only adds tasks, verifiers, and solvers.
