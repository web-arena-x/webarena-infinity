# Evaluation Harness Documentation

## 1. Overview

This module contains an evaluation harness used to measure a browser agent’s performance across multiple web application tasks.

- Each web application defines its own tasks.
- Each task has a corresponding verifier used to evaluate correctness.

---

## 2. Task Definition

For each web application (`./{web-app-name}`):

- Task definitions are located at:  
  ./{web-app-name}/tasks.json

- Task verifiers are located at:  
  ./{web-app-name}/tasks/task*.py

Each `task*.py` file contains the logic required to verify whether the agent successfully completed the task.

---

## 3. Agent

The agent is implemented using a browser automation framework ("browser use").  
It interacts with the web applications to complete tasks defined in `tasks.json`.

---

## 4. Evaluation Procedure

For each task, the evaluation harness performs the following steps:

For every tasks:
    1. Resets the environment to a clean state for each task
    2. Executes the agent on the task.
    3. Runs the corresponding verifier to evaluate the result.

For more detailed information about the evaluation flow and environment reset process, refer to:

gitlab-org-management/HARNESS.md

---

## 5. Report Generation

The final report must:

- Combine:
  - Task trajectories (step-by-step agent actions)
  - Full transcript of the agent’s interaction
- Be correctly named
- Be presented as a simple HTML file displaying the results clearly

---

## 6. Available Web Applications

Currently available:

- ./gitlab-org-management