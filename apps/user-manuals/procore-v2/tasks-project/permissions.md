# Tasks

Source: https://v2.support.procore.com/product-manuals/tasks-project/permissions

---

Table of Contents

## Permissions

##### Â Important

Some actions that impact this tool are done in other Procore tools.

| | The action is available on Procore's Web, iOS, and/or Android application.

Users can take the action with this permission level.

Users can take this action with this permission level AND one or more additional requirements, like [granular permissions](/faq-what-are-permissions-in-procore-and-how-do-they-work).

See [What granular permissions are available for the Project level Tasks tool?](/faq-what-granular-permissions-are-available-for-the-project-level-tasks-tool) for detailed information.

| [Tasks Tutorials](/product-manuals/tasks-project/tutorials)  Action | None | Read Only | Standard | Admin | Notes |
| --- | --- | --- | --- | --- | --- |
| Add Comments to a Task   Web  iOS  Android |  | - Add Comments to Tasks / Edit Tasks / Change Task Status | - Add Comments to Tasks / Edit Tasks / Change Task Status |  | - *As Creator of the task,*Â *Standard* users can update the task to any status or add comments. - *As Assignee for the task*, *Standard* users can add comments or update the status to 'Initiated', 'In Progress', or 'Ready for Review', but NOT to 'Closed' or 'Void.' To change the status to Closed or Void, they require '*Close Assigned Tasks*â enabled. - *Read Only* users can add comments to the tasks they created only if âCreate Tasks' is enabled. |
| Add a Related Item to a Task  Web |  |  |  |  |  |
| Add a Task   Web iOS  Android |  | - Create Tasks |  |  | - *Read Only* users require 'Create Tasks' enabled to add a task and assign it to *Admin* level users. - *Read Only* users require both 'Create Tasks' and 'Assign Tasks to Standard Users' enabled to add a task and assign it to users with 'Standard' level permissions. - *Standard* users require 'Assign Tasks to Standard Users' enabled to assign a task to users with 'Standard' level permissions. |
| Change the Status of a Task   Web  iOS  Android |  | - Edit Tasks / Change Task Status | - Edit Tasks / Change Task Status |  | Read Only users require 'Create Tasks' enabled to change the status of tasks they created.  'Standard' users assigned to a task created by someone can only add comments or edit the status of the task. However, they cannot change a task status to 'Closed' or 'Void' unless they have created the task. To change the status to âClosed' or 'Void', they require 'Close Assigned Tasksâ granular permission enabled. |
| Edit a Task   Web  iOS  Android |  | - Edit Tasks | - Edit Tasks |  | âEdit Tasksâ allows users to assign tasks to both Standard and Admin users.  Read Only users require 'Create Tasks' enabled to edit the tasks they created.  'Standard' users assigned to a task created by someone can only add comments or edit the status of the task. However, they cannot change a task status to 'Closed' or 'Void' unless they have created the task. To change the status to âClosed' or 'Void', they require 'Close Assigned Tasksâ granular permission enabled. |
| Configure Tasks Project Settings   Web iOS  Android |  | - Manage Project-level Task Settings | - Manage Project-level Task Settings |  |  |
| Delete a Task   Web iOS  Android |  | - Delete Tasks | - Delete Tasks |  |  |
| Export a Project's Task List   Web |  |  |  |  |  |
| Search for Tasks   Web iOS  Android |  |  |  |  |  |
| Send Task Notification Emails for Any Task   Web iOS  Android |  | - Notify About Task Changes | - Notify About Task Changes |  |  |
| Send Task Notification Emails for Tasks You Created   Web iOS  Android |  | - Create Tasks |  |  |  |
| View Any Task   Web iOS  Android |  | - View All Tasks | - View All Tasks |  |  |
| View Tasks (Not Private)   Web iOS  Android |  |  |  |  |  |
| View Tasks (Private)   Web iOS  Android |  |  |  |  | 'Read Only' and 'Standard' users can view private tasks if they are the **Creator**, **Assignee**, or on the **Distribution List.** |
| View the Change History of a Task   Web iOS  Android |  | - View Task Change History | - View Task Change History |  |  |