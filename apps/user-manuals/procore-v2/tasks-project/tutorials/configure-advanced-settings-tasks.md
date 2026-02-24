# Configure Advanced Settings: Tasks

Source: https://v2.support.procore.com/product-manuals/tasks-project/tutorials/configure-advanced-settings-tasks

---

## Background

The **Tasks** tool allows you to configure advanced settings, such as default due dates for task items, default distribution lists, and task notification emails.

## Things to Consider

- **Required User Permissions:**

  - To configure tasks project settings, see [Tasks - User Permissions](/product-manuals/tasks-project/permissions).
  - To send task notification emails for tasks that you created, see [Tasks - User Permissions](/product-manuals/tasks-project/permissions).

## Steps

1. Navigate to the project's **Tasks** tool.
2. Click **Configure Settings**.
3. Configure the following settings:

   - **Task Items Private by Default:**

     - Mark this checkbox to make task items 'Private' by default.
   - **Default Due Date for Task items:**

     - Enter the desired default number of days in which a new task item will be due.  
       *Note:* The due date respects which days are set as 'working days' for the project.   
       See [Set Project Working Days](/product-manuals/admin-project/tutorials/set-project-working-days).
   - **Default Distribution List:**

     - Users added to this field will be automatically added to the distribution list for all new Tasks created after their addition to the list.
   - **Tasks Emails:**

     - Select the events for which you want to receive notifications.
     - Adjust the notification settings to specify which recipients should receive updates for each event.
     - Default settings are:

       ##### Â Note

       - Task Createdevent emails are not sent immediately upon task creation. These emails are delivered after clicking 'Send Mine/All' from the banner at the top of the page.
       - All other event emails are sent automatically. However, they depend on the 'Task Created' email being sent first. If the 'Task Created' email hasnât been sent, notifications for all other events will not be delivered, even if they are enabled.