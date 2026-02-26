You are reviewing a set of agent trajectories for tasks that can only be completed through a website’s UI. These tasks are basic functional checks meant to evaluate whether the website works correctly.

Your goal is to determine whether each failed task is caused by:
- A real issue or bug in the website, or
- A limitation or mistake made by the agent.

## Decision Flowchart

When a task fails during an agent evaluation:

```
1. Run the verifier sanity check for the task (`sanity_check_function_test.py`).
   - If the sanity check FAILS → There is likely a bug in the verifier or the task solution. Fix it.
   - If the sanity check PASSES → The verifier is functioning correctly. Proceed to Step 2.

2. Review the relevant implementations for the task and determine whether the agent’s failure is due to a website bug.
   (For example: the agent executes correctly, but a website issue prevents task completion.)
   - If there is a bug in the website implementation → Fix the website.
   - If there is a bug in the verifier → Fix the verifier.
   - Otherwise → The task is feasible and functioning as intended. Proceed to Step 3.

3. Attribute the failure to the agent.
   - Categorize the failure (e.g., navigation error, incorrect value, false claim, etc.).
   - No changes to the benchmark are required.
```

Put your audit summary under the same result directory as the evaluation results, named `audit_summary.md`. 