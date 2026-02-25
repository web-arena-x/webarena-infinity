# Configure Action Plans Notification Settings

Source: https://v2.support.procore.com/product-manuals/action-plans-project/tutorials/configure-action-plans-notification-settings

---

## Things to Consider

- **Required User Permissions:**

 - For full access of the tool, 'Admin' level permissions on the project's Action Plans tool. 
     OR
 - *To edit notifications:*

    - 'Read Only' level permissions or higher on the project's Action Plans tool with the 'Edit Notifications' granular permission enabled on your permissions template.
- **Additional Information:**

 - Notifications for the Action Plans tool respect which days are set as 'working days' for the project. See [Set Project Working Days](/product-manuals/admin-project/tutorials/set-project-working-days).

## Steps

1. Navigate to the project's **Action Plans** tool.
2. Click the **Configure Settings** icon.
3. Click the **Notifications** tab.
4. Mark the checkboxes for the roles you want notifications to be sent to:

   - **Creator**
   - **Plan Manager**
   - **Plan Approver**
   - **Plan Receiver**
   - **Assignees**
5. Mark one or both of the Notification Type checkboxes:

   - **Email**
   - **Push (iOS and Android)**
6. Click **Update** to save your notification settings.

### Configurable Notifications

Action Plans can be configured for the following notifications:

| Notification | Time of Delivery |
| --- | --- |
| A plan has been published and a user is assigned items | For Assignees, this notification will be sent as soon as the user clicks **Publish**. Users that have been assigned more than one role, such as Assignee, Approver, and Receiver, will receive one email for the item with the highest priority. The current priority is Approver, Assignee, Receiver, Manager, Creator. If a user has been assigned the role of Approver, Assignee, Receiver, Manager, and Creator, the user will receive an email that is formatted specifically for an Approver, then an Assignee, after that a Receiver, Manager and Creator. |
| A plan has been signed by all approvers | For everyone, this notification will be sent as soon as all approvers have signed the item. *Important:* If an assignee is marked to receive this notification, the list of items in their email will only include items that have not been signed (hence incomplete) |
| An assignee was assigned items to a previously published plan | For assignees, this notification is sent immediately. For everyone else, the notification will be sent the next morning at approximately 6:30 a.m. project time. |
| # days until your assigned item is due | For everyone, the notification will be sent the next morning at approximately 6:30 a.m. project time. For example, if the user configures an item to be due in 4 days, and if the item is due in 4 days, the email will be sent today. |
| An assignee has an assigned item that is due today | For everyone, the notification will be sent the day the item is due at approximately 6:15 a.m. project time. |
| An assigned item is unblocked and the assignee can now take action | For everyone, the notification will be sent immediately after the item has been unblocked. |
| Items are overdue | For everyone, the notification will be sent every morning at approximately 6:15 a.m. project time including overdue items from the past 2 weeks. If an item is overdue for more than 2 weeks, the email will exclude those items from the **Items Assigned to You** list. |
| All assignee signatures for a plan have been collected | For everyone, the notification will be sent after all assignees have signed. |
| Action Plan has been signed by all receivers | For everyone, the notification will be sent as soon as all the receivers have signed. |