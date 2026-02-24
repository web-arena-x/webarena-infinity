# Add and Manage Subtasks for a Lookahead Schedule

Source: https://v2.support.procore.com/product-manuals/schedule-project/tutorials/add-and-manage-subtasks-for-a-lookahead-schedule

---

## Background

A lookahead is a snapshot of the master schedule uploaded to Procore over a specified duration ranging from one to six weeks. The lookahead feature allows companies to manage schedule tasks on the master schedule in greater detail. You can use a lookahead to create subtasks, add notes to existing schedule tasks, and edit schedule tasks. In addition, schedule tasks and lookahead subtasks will carry over to each lookahead created if the dates overlap with one another.

## Things to Consider

- **Required User Permissions:**

  - *To add and manage subtasks for a lookahead schedule*:

    - You need one of the following:

      - 'Admin' permissions on the project's Schedule tool.
      - 'Read Only' or 'Standard' level permissions on the Schedule tool with the following [granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template:

        1. Delete Lookaheads
        2. Create Lookahead Task
        3. Delete Lookahead Tasks
        4. Update Lookahead Tasks
- **Additional Information:**

  - Edits and changes made on a lookahead will not reflect on the master schedule.
- **Prerequisites:**

  - To manage subtasks on a lookahead you must have already created a lookahead on the project's Schedule tool.

### Manage Lookahead Tasks

Users can manage an individual task on a lookahead by its day-to-day progress and status. Tasks can be managed with the following options:

##### Â Note

**Critical** and **Standard** subtasks are inherited directly from the parent schedule task that has been uploaded to project's Schedule tool. Critical tasks are identified by a red box and standard task are identified by a blue box. Users cannot designate a subtask as critical or noncritical on a lookahead and the colors of the boxes can't be modified.

- **Critical:** To mark a task as Critical on a lookahead, click the day and date box one time and a light red box will appear.   
  *Notes:* Click the day and date box for each day a task will be performed. A red box denotes a task is Critical.
- **Critical Complete:** To mark a critical task as Complete, click the light red box a second time and the critical task turns dark red.
- **Standard:** To mark a task as Standard on a lookahead, click day and date once and a light blue box will appear.  
  *Notes:* Click the day and date box for each day a task will be performed. A blue box denotes a task is Non-critical.
- **Standard Complete:** To mark a standard task as complete, click the light blue box a second time and the standard task turns dark blue.

The following actions are also available:

- Delete a Lookahead Schedule
- Create a Subtask
- Edit a Task
- Delete a Task

##### Delete a Lookahead

- Click the delete trashicon to **delete** a lookahead.  
    
  *Note:* Deleting a lookahead will not impact the master schedule or other lookaheads where dates overlap.

##### Create a Subtask

1. Navigate to the project's Schedule tool.
2. Click the **Lookaheads** tab.
3. Select the lookahead you want to add a **Subtask** to.
4. Click the plus icon in the **Notes** column of schedule task you want to add a subtask to and the **Create Subtask** menu will appear.  
   *Note:* Click **+Add Another Subtask** to create another subtask.
5. Fill out the **Create Subtask** menu.  
   *Note:* Any data from the 'Resource', 'Company', and 'Assignees' fields in the main task is added automatically in the **Create Subtask** menu but can be edited as necessary.
6. Click **Create**.
7. The Subtask will appear on the lookahead as under the main task.   
   *Note:* You can add multiple Subtasks.

##### Edit a Task

1. Navigate to the project's schedule tool.
2. Click the **Lookaheads** tab.
3. Select the lookahead task you want to edit.
4. In the Notes column of the task you want to edit, click the **Edit Task**icon.
5. Fill out the **Edit Task** menu.
6. Click **Update**.

##### Delete a Task

1. Navigate to the project's Schedule tool.
2. Click the **Lookaheads** tab.
3. Select the lookahead you want to delete a task from.
4. In the Notes column of the task you want to delete, click the **Task Info**icon.
5. Click the vertical ellipsison the Task menu and click **Delete**.
6. On the Delete Task window, click **Proceed** to delete the task from the lookahead.