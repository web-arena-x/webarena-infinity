# Forward a Submittal by Email - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/forward-a-submittal-by-email

---

## Objective

To forward an email that contains information about a submittal to other Procore users from the Project level Submittals tool. 
*Important*: The steps in this article show you how to send  an email containing a summary about the submittal.

## Background

The email functionality on the Submittals tool allows you to send an email outside of the emails that are automatically generated from the Submittals tool. Automatic emails are sent out to approvers and members of the distribution list when the email is created, when an approver responds, when an approver's response is edited, and when any changes are made to the submittal (attachments are attached, the submittal status is changed, etc).

## Things to Consider

- **Required User Permissions:**
 - *To send an email to a user:*
    - 'Standard' or 'Admin' level permissions on the project's Submittals tool.
 - *To receive an emailed submittal:*
    - ‘Read-Only’ level or higher permissions to the project's Submittals tool. 
      *Note:* Recipients must be listed in the project's Directory tool.
- **Additional Information:**
 - If a person is missing from the recipient selection list, add them to the Project level Directory with 'Read Only' or higher level permissions to the Submittals tool. If you don't have permission to add users to the Project Directory, ask a member of your team who is responsible for Directory management to add them.  
    *Note:* The newly added user does NOT have to accept the invitation to join the project before they can be selected from the recipient list.

## Steps

1. Navigate to the project's **Submittals** tool.
2. Locate the desired submittal.
3. Click **View**.
4. Click the **Emails** subtab for the submittal.
5. Click **Compose Email**.
6. Under the 'Compose New Email' area, do the following:
   - **To**. Select the desired recipient(s) from the drop-down list.
   - **Cc.** Select any desired recipient(2) to receive a carbon copy of the email.
   - **Private**. Indicates privacy settings for the submittal. When a submittal is marked 'Private', it is only visible to users with 'Admin' level permissions on the Submittals tool, users in the Submittal Workflow, and members of the submittal's Distribution List. Users with the ['View Private Submittals Associated to Users within Same Company' granular permission](../../../company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#Submittals "Grant Granular Permissions in a Project Permissions Template") enabled on their permissions template can also view a submittal marked 'Private' if another user in their company is associated with the submittal. See [Mark a Submittal as Private](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/mark-a-submittal-as-private "products/online/user-guide/project-level/submittals/tutorials/mark-a-submittal-as-private").
   - **Title**. The descriptive name that best summarizes the information in the submittal.
   - **Attachments**. Attach any relevant files. You have these options:

     - Click **Attach File(s)**and then choose the appropriate option from the shortcut menu that appears. 
       OR
     - Use a drag-and-drop operation to move files from your computer into the grey **Drag and Drop File(s)** box.
   - **Message**: Enter the body of your email message.
7. Click **Send**.  
   The system sends the email to all of the recipients. A copy of the email and any replies are stored as a communication thread in the Emails subtab of the submittal.

## See Also

- [Forward a Submittal for Review](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/forward-a-submittal-for-review "Forward a Submittal for Review")