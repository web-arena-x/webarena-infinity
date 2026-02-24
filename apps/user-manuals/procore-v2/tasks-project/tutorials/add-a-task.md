# Add a Task

Source: https://v2.support.procore.com/product-manuals/tasks-project/tutorials/add-a-task

---

## Background

The **Tasks** tool enables you to track and manage action items throughout your construction project's lifespan. Using this tool, you can create tasks with due dates and assign them to one or more project users to ensure accountability.

## Things to Consider

- **Required User Permissions:**

  - See [Tasks - User Permissions](/product-manuals/tasks-project/permissions).
- **Additional Information:**

  - Overdue notification summary emails are sent daily to the task assignee(s) if a task is past due and remains in *Initiated* or *In Progress* status.
  - Overdue emails are not sent for tasks in *Closed*, *Void*, or Ready for Review status.

## Steps

1. Navigate to the project's **Tasks** tool.
2. Click **Create.**
3. Enter the following information:  
   *Note*: An asterisk (\*) denotes a required field.

   - **# (Number)**\*: Enter a number for the task.  
     *Note*: The system assigns numbers to tasks in sequential order and duplicate numbers are NOT permitted.
   - **Title**\*: Enter a descriptive title for the task.
   - **Status**: Select one of the available statuses.

     - **Initiated**: Indicates the task has been created. This is the default status.
     - **In Progress**: Indicates work on the task has started.
     - **Ready for Review**: Indicates the task is complete and ready for review.
     - **Closed**: Indicates the task and review of the work has been successfully completed.
     - **Void**: Indicates the task has been voided.
   - **Assignee(s)**: Select one or more project users from the drop-down menu, or select None if there is no assignee.
   - **Due Date**: Enter or select a date from the calendar for the task to be due.  
     *Note*: The Due Date field is automatically populated based on the default number of days specified on the Tasks tool's Configure Settings page. The due date also respects which days are set as 'working days' for the project. See [Configure Advanced Settings: Tasks](/product-manuals/tasks-project/tutorials/configure-advanced-settings-tasks) and [Set Project Working Days](/product-manuals/admin-project/tutorials/set-project-working-days).
   - **Distribution List.** Add users with 'Read-Only level permission or higher to the Task's distribution list.
   - **Category:** Select a predefined category associated with the task.  
     *Note*: Task categories are managed at the company level. See [Add Task Categories.](/product-manuals/admin-company/tutorials/add-task-categories)
   - **Description**: Type a brief summary describing the task.
   - **Attachments**: Click **Attach File(s)** or use a drag-and-drop operation to attach files to the task.
   - **Private**: Place a checkmark in this box to make the task private.  
     *Note*: Private tasks are only visible to the task's creator, assignee(s), and users with 'Admin' level permission on the project's Tasks tool.
4. Click **Add**.  
   A banner appears to indicate the task has been created, and the system adds your new task to the display table.  
   *Note*: The task also becomes visible on each assignee's My Open Items page in the Company level Portfolio tool and the Project level Home page.
5. Click **Send Mine** or **Send All** in the banner above the Tasks list page to send a digest email to assignees and creators of all of the tasks that have yet to be sent. The Tasks 'Date Notified' will be set to the date the Send button was clicked.

   - **Send Mine**: Clicking this option will send tasks that you have created.
   - **Send All**: Clicking this option will send all tasks that are ready to be sent. Be sure to speak with other team members to make sure that all tasks are ready to go out.  
     *Notes:*

     - Changes to assignees will create a new notification.
     - Assignees can only send tasks they created.
     - In order to see this banner, the task must have at least one assignee.