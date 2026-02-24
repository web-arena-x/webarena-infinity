# Shift the Ball In Court on an RFI - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/shift-the-ball-in-court-on-an-rfi

---

## Objective

To shift the Ball In Court responsibility on an RFI to another user in the RFI workflow.

## Things to Consider

- **Required User Permissions:**
 - 'Admin' level permission on the RFIs tool. 
    OR
 - 'Read Only' or 'Standard' level permissions on the project's RFIs tool with the ['Act as RFI Manager' granular permission](../../../company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#RFIs "Grant Granular Permissions in a Project Permissions Template") enabled on your permissions template AND be the RFI's creator ('Standard' only) or RFI Manager.
- **Additional Information:**
 - If the RFI has been forwarded to another user by one of its **Assignees** (see [Forward an RFI for Review](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/forward-an-rfi-for-review "Forward an RFI for Review")) the other user is given the Ball In Court responsibility until they post a response to the RFI. To remove that user from the list of **Assignees**, edit the RFI and click the X next to their name in the **Assignees** field.
 - If an **Assignee** on the RFI has added one or more other users as **Assignees** (see [Add Assignees to an RFI as an Assignee on an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/add-assignees-to-an-rfi-as-an-assignee-on-an-rfi "Add Assignees to an RFI as an Assignee on an RFI")) the other users share the original **Assignee's** Ball In Court responsibility. If at least one of their responses are required, Ball In Court responsibility stays with the **Assignees** until those with required responses complete their response. After all required responses have been completed, the Ball In Court responsibility shifts to the **RFI Manager**.
 - If the **Enable Email Reminders for Overdue RFIs** setting is enabled on the project (see [Configure Advanced Settings: RFIs](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/configure-advanced-settings-rfis "Configure Advanced Settings: RFIs")), the system sends out email notifications to users with the current Ball In Court responsibility on an RFI if their action on the RFI is overdue.

## Steps

1. Navigate to the project's **RFIs** tool.
2. Click the **Items** tab.
3. Click **View** next to the RFI you want to shift the Ball In Court responsibility for.
4. Click one of the following buttons at the bottom of the page:
   - **Return to Assignee's Court**. Click this button to shift the responsibility to the user or users in the **Assignees** field.  
     OR
   - **Return to RFI Manager's Court.**Click this button to shift the responsibility to the user in the **RFI Manager** field. 
       
     A green banner displays to confirm the Ball In Court responsibility shifted and emails are sent according to the project's settings. See [When does the RFIs tool send email notifications?](https://support.procore.com/faq/when-does-the-rfis-tool-send-email-notifications "When does the RFIs tool send email notifications?")

## See Also

- [Edit an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/edit-an-rfi "Edit an RFI")

## 

If you would like to learn more about Procore's RFI software and how it can help your business, please visit our [request for information (RFI) construction software product page ![icon-external-link.png](https://support.procore.com/@api/deki/files/186764/icon-external-link.png?revision=2&size=bestfit&width=14&height=14)](https://www.procore.com/project-management/rfis "https://www.procore.com/project-management/rfis").