# Manage PDF Configurations for Exported Meetings

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/manage-pdf-configurations-for-exported-meetings

---

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Company level Admin tool.
- **Additional Information:**

 - If your company has custom meeting PDF templates built by Procore's Custom Solutions team, reach out to your Procore point of contact to confirm whether the meetings PDF configurations can be used on your projects.

## Steps

- Create a PDF Configuration
- Edit an Existing PDF Configuration
- Update the Assigned Projects for an Existing PDF Configuration
- Delete a PDF Configuration

### Create a PDF Configuration

1. Navigate to the Company level **Admin** tool.
2. Under 'Tool Settings', click **Meetings**.
3. Click the **PDF Configurations** tab.
4. Click **Create**.
5. In the 'Create PDF Configuration' window, enter a name for the PDF configuration.
6. Click **Create**.
7. On the 'Edit PDF Configuration' page, complete the following:

   - **Attendees Phone Number Display:** Select **Business Phone** or **Cell Phone** to choose which phone number for each attendee will display. The phone numbers included are based on the user's information in the Project level Directory. See [Edit a User Account in the Project Directory](/product-manuals/directory-project/tutorials/edit-a-user-account-in-the-project-directory).
   - **Attendees Table Format:** Select **One Column**, **Two Columns**, **Move to end of PDF**, or **Remove Table**. 
     *Note:* If you select **Two Columns**, the attendees' email addresses and their attendance statuses will not be included in the PDF exports.
   - **Disclaimer Footer Text:** Enter text you want to display at the bottom of the PDF pages. This will replace Procore's default text. 
     *Note:* This text only displays on PDF exports of meetings that are in minutes mode. See [Convert a Meeting from Agenda to Minutes Mode](/product-manuals/meetings-project/tutorials/convert-a-meeting-to-minutes-mode).
8. Click **Update**.
9. In the 'Apply changes' window, click **Assign Projects** to assign the PDF configuration to one or more existing projects.

   ##### Â Important

   Assigning a PDF configuration to a project will affect all meeting exports in that project, including exports for meetings that existed before the PDF configuration was assigned to the project.

- Mark the checkbox next to each project that you want to assign the PDF configuration to (or mark the **Select All Projects** checkbox to assign it to all projects) and click **Update**.
- In the 'Apply changes' window, click **Update**.
- *Optional:* To set the PDF configuration as the default for new projects, hover your cursor under the 'Default for New Projects' column on the 'PDF Configurations' page and click **Set as default**.

### Edit an Existing PDF Configuration

1. Navigate to the Company level **Admin** tool.
2. Under 'Tool Settings', click **Meetings**.
3. Click the **PDF Configurations** tab.
4. Click **Edit** next to the name of the PDF configuration you want to edit.
5. On the 'Edit PDF Configurations' page, update the fields you want to change on the PDF configuration. See Create a PDF Configuration above for more information.
6. Click **Update**.
7. In the 'Apply changes' window, click **Update**.

### Update the Assigned Projects for an Existing PDF Configuration

1. Navigate to the Company level **Admin** tool.
2. Under 'Tool Settings', click **Meetings**.
3. Click the **PDF Configurations** tab.
4. Click the **[#/#] Projects** link on the PDF configuration's row in the 'Assigned Projects' column.
5. To add the PDF configuration assignment to one or more projects, mark the checkbox next to each project that you want to assign the PDF configuration to (or mark the **Select All Projects** checkbox to assign it to all projects) and click **Update**.
6. To remove the PDF configuration assignment from one or more projects, clear the checkbox next to each project that you want to remove the PDF configuration assignment from (or clear the **Select All Projects** checkbox to remove it from all projects) and click **Update**.

### Delete a PDF Configuration

##### Â Note

PDF configurations can only be deleted when they are not assigned to any projects.

1. Navigate to the Company level **Admin** tool.
2. Under 'Tool Settings', click **Meetings**.
3. Click the **PDF Configurations** tab.
4. Click the delete icon at the end of the PDF configuration's row.
5. In the 'Delete [PDF Configuration Name]' window, click **Delete**.