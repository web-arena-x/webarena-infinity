# Edit a Correspondence Item

Source: https://v2.support.procore.com/product-manuals/correspondence-project/tutorials/edit-a-correspondence-item

---

## Things to Consider

- **Required User Permissions:**

 - *To edit any correspondence item:* 'Admin' level permissions on the item's correspondence type.
 - *To edit a 'Draft' correspondence item that you created:* 'Standard' level permissions on the item's correspondence type. 
    OR 'Read Only' level permissions on the item's correspondence type with the ['Create Item' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.
 - *To edit an 'Open' correspondence item that you created:* 'Standard' level permissions on the item's correspondence type. 
    OR 'Read Only' level permissions on the item's correspondence type with the ['Edit Open Items They Created' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.
- **Additional Information:**

 - If Procore was asked to enable the 'non-editable' setting at the company level, only 'Draft' correspondence items are editable, regardless of user permissions. Consider [creating and linking a new item](/product-manuals/correspondence-project/tutorials/create-an-link-an-rfi-change-event-or-a-different-correspondence-item-to-an-existing-correspondence-item) instead.
 - If you have been assigned or associated to a correspondence item and you want to add a response to the item, see [Respond to a Correspondence Item](/product-manuals/correspondence-project/tutorials/respond-to-a-correspondence-item).
 - If a workflow is applied to the item, and the item is issued, the following fields are auto-populated with the workflow information: Status, Due Date, Assignees, and Distribution Member. Also, the 'Post Response and Change Status' button is no longer available unless 'Responses' are enabled on the fieldset.
 - Email notification information:

    - Editing an 'Open' correspondence item results in an email notification to the item's creator and anyone in the 'Assignee', 'Distribution Member', or 'Received From' fields, if an admin has enabled 'Updated Item' email notifications for the correspondence type.
    - Email notifications are sent for all correspondence items until their status is changed to 'Closed'.
    - See [Who receives correspondence item emails and push notifications?](/faq-who-receives-correspondence-item-emails-and-push-notifications) for more details.

## Steps

1. Navigate to the project's **Correspondence** tool.
2. Click the **List** tab.
3. Click the **Number** next to the correspondence item that you want to edit.
4. Click **Edit.** If you're looking for multiple documents, see tips for [bulk editing](/product-manuals/correspondence-project/tutorials/perform-bulk-actions-on-correspondence-items).   
   *Note:* If there is no 'Edit' button, Procore was asked to enable the 'non-editable' setting at the company level to keep communication records reliable for all 'Open' and 'Closed' items in the Correspondence tool. Consider [creating and linking a new item](/product-manuals/correspondence-project/tutorials/create-an-link-an-rfi-change-event-or-a-different-correspondence-item-to-an-existing-correspondence-item) instead.
5. Modify the task's General Information by clicking into the following fields: 
   *Note:* An asterisk (\*) denotes a required field.

   - **Number:** This is the unique number to identify this correspondence item. The prefix and number will display in the correspondence in the list view, when linked to other tools, as well as any other location where the correspondence item is listed.
   - **Status:** Select the appropriate status for your correspondence item: 
     *Note:* If a workflow is applied, the status is determined by the workflow and is not editable.
   - **Closed:** The correspondence has been closed.
   - **Open:** The correspondence is open.
   - **Custom Status:** Custom statuses previously created for the correspondence type can be selected when editing correspondence items. See [Configure Advanced Settings: Correspondence](/product-manuals/correspondence-project/tutorials/configure-advanced-settings-correspondence).
   - **Subject:** The subject is a title of the correspondence item which will display in the correspondence in the list view, when linked to other tools, as well as any other location where the correspondence item is listed.
   - **Private:** Select **Private** to make the correspondence private. Private correspondences are only visible to the correspondence's creator, the user listed in 'Received From', the users listed in 'Assignees', the users listed in 'Distribution', and users with company or project level 'Admin' permissions.

     ##### Â Note

     - Users who belong to the same companies as the users listed on the item can also view private items if the General Correspondence type has the granular permission of 'View Private Items Accessible to Users within Same Company' enabled.
     - Reach out to your Procore point of contact if you wish for Private correspondence items to be hidden from users with 'Admin' level permissions at the company or project level, ensuring they will not have the ability to view or respond to private items unless they are specifically included on the correspondence item. (If your company is based in Australia or New Zealand, this additional level of privacy will be enabled by default).
     - You can always see who has permissions to private items via the 'Permissions' tab when viewing a correspondence item.

- **Assignees:** Assign responsibility for responding to a general correspondence to one or more project team members from the users in the Directory. Add users with 'Read Only' level permissions or higher to the distribution list. Depending on the user's permission level, they can respond to the correspondence. 
 *Note:* If a workflow is applied, this field is replaced with 'Current Step Assignee' and is read-only.
- **Due Date:** Enter or select a date from the calendar for the response to be due. 
 *Note:* If a workflow is applied to the item, this field changes to 'Current Step Due Date' and is read-only.
- **Received From:** Similar to 'CC' on emails, add people who are not directly responsible, but should be aware of this General Correspondence. Add users with 'Read Only' level permissions or higher to the distribution list. Depending on the user's permission level, they can respond to the correspondence.
- **Distribution Member:** Add users with 'Read Only' level permission or higher to the distribution list. Depending on the user's permission level, they can respond to the correspondence. 
 *Note:* If a workflow is applied to the item, once the item is Issued, any distribution members in the workflow template automatically populate here and cannot be removed. Manually add (or remove) *additional* distribution members on the correspondence item to give them item access. However, notifications are only sent to members on the *workflow distribution list*, not the correspondence item distribution list.
- **Schedule Impact:** Select whether this correspondence item's subject does or will affect the schedule.

 - 'Yes': The schedule is impacted in a known way.
 - 'Yes (unknown)': Yes, the schedule is impacted but the details or extent of the impact is not yet known.
 - 'No': The schedule is not impacted.
 - 'TBD': To be determined. You are not sure whether the schedule will be impacted or not.
 - 'N/A': The schedule is not relevant to this correspondence item.
- **Sub Job:** Select a sub job to connect to the correspondence item.
- **Cost Code:** Select a cost code to assign to the correspondence item.
- **Trades:** Select one or more trades to associate with the correspondence item.
- **Location:** Select the location pertaining to the correspondence from the drop-down list. 
 *Note:* If Procore is configured to allow users to create locations (see [Allow or Disallow Users to Create Locations Within a Tool](/product-manuals/admin-project/tutorials/allow-or-disallow-users-to-create-locations-within-a-tool)), you can click the **Create a New Location** button at the bottom of the list.
- **Description:** Provide details about the General Correspondence you want to communicate.
- **Attachments:** Attach the applicable files you want to include in your communication of this General Correspondence. The attachment maximum for each correspondence item is 2,500 files. Attachments included in Responses to the correspondence item do not count toward this maximum.
- **Schedule Tasks:** Search for and select one or more schedule tasks from the project's schedule to associate with the correspondence item.
- Click **Save**.