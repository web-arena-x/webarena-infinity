Audit the agent evaluation results inside `{evaluation_result_path}` following the guide at `./docs/real-task-audit.md.`

**Always** write an audit summary to `{evaluation_result_path}/audit_summary.md` documenting your findings. Include:
- Overall pass rate and task counts
- For each failed task: the root cause (verifier bug, impossible task, ambiguous instruction, or agent-side failure) and any fix applied
- A summary of agent-side failures by category (navigation failure, wrong value, false claim, timeout, etc.)