# Close a Submittal

Source: https://v2.support.procore.com/product-manuals/submittals-project/tutorials/close-a-submittal

---

## Background

After a submittal has been approved by all of the individuals who have been designated as approvers in the submittal's approval workflow, a user who has been assigned 'Admin' level permissions can mark the submittal as Closed. This indicates the submittal approval workflow is complete and/or requires no further action.

## Things to Consider

- **Required User Permission**:

  - *To close a submittal,* 'Admin' level permissions on the project's Submittals tool.
  - *To edit a closed submittal,* 'Admin' level permissions on the projects Submittals tool.

## Steps

There are three (3) ways to close a submittal in Procore:

- Close a Submittal from the Submittals Items Page
- Close a Submittal from its Edit Page
- Close and Distribute a Submittal

### Close a Submittal from the Submittals Items Page

1. Navigate to the project's **Submittals** tool.  
    This reveals the Submittals page.
2. Locate the desired submittal in the list. Then click the **Status** box for the desired submittal and select *Closed* from the list.  
    (*Note*: Your company's list may contain custom status values that were created for use on your projects. See [Create a Custom Submittal Log Status](/product-manuals/admin-company/tutorials/create-custom-submittal-log-statuses).)

### Close a Submittal from its Edit Page

1. Navigate to the project's **Submittals** tool.  
    This reveals the Submittals page.
2. Locate the desired submittal and click **Edit**. See Search for and Filter Submittals.  
    This opens the submittal in edit mode.
3. Select *Closed* from the **Status** list.  
    (*Note*: Your company's list may contain custom status values that were created for use on your projects. See [Create a Custom Submittal Log Status](/product-manuals/admin-company/tutorials/create-custom-submittal-log-statuses).)
4. Edit any other information as needed.
5. Do one of the following:

   - If you want to save the submittal without sending an email notification to approvers and members of the distribution list, click **Update**.
   - If you want to send an email notification to approvers and members of the distribution list, click **Update and Send Email(s)** .

### Close and Distribute a Submittal

1. Navigate to the project's **Submittals** tool.
2. Click the **Items** tab.
3. Click **View** next to the submittal you want to distribute.
4. If at least one required member of the submittal workflow has submitted their response, click **Close and Distribute**.
5. Enter the information you want to include in the distribution.

   ##### Â Note

   - The distribution list and the user roles selected in the Submittals tool configuration settings to receive a notification for the action 'Submittal Distributed', are automatically added as recipients.

- Mark the checkbox if you want to automatically **Create a Revision Upon Close and Distribution**.
- Mark the checkboxes for what General Information to include in the distribution.
- Mark the checkboxes to select which Workflow Responses to include in the distribution.
- Do one of the following:

  - Click **Distribute**
  - **Distribute and Create Revision** to distribute the submittal.

##### Â Note

The following events occur when a submittal is distributed:

- Procore generates a PDF of the submittal and sends it by email to the chosen recipients.
- The PDF shows the name and company of the person who distributed the submittal.
- The submittal's status is set to *Closed.*
- The date, action, and timestamp are logged in the Change History tab of the submittal.
- The 'Submittal Distributed' banner appears (as illustrated below) showing the date and time the submittal was distributed.