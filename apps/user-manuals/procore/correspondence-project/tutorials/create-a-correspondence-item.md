# Create a Correspondence Item

Source: https://v2.support.procore.com/product-manuals/correspondence-project/tutorials/create-a-correspondence-item

---

## Background

You can use the Correspondence tool to create a correspondence item that is based on a specific correspondence type, such as a General Correspondence. This article will use General Correspondence as the correspondence type for the correspondence item creation tutorial, however you can replace the 'General Correspondence' name throughout this tutorial with any other correspondence type you create to learn how to create a correspondence item for that correspondence type. Additionally, you can set a correspondence to private to limit the amount of collaborators who have access to a correspondence.

## Things to Consider

- **Required User Permissions:**

 - 'Standard' level permissions or higher on the item's correspondence type. 
    OR
 - 'Read Only' level permissions on the item's correspondence type with the ['Create Item' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.
- **Differences for items with a workflow applied, once created and issued:**

 - 'Status': Read-only field that auto-populates with information from the workflow.
 - 'Due Date': Read-only field that auto-populates with dates determined by the workflow and has a name change to 'Current Step Due Date'.
 - 'Assignees': Read-only field that auto-populates with the user assigned to the current step as determined by the workflow. The field's name changes to 'Current Step Assignee', but the 'Assignees' field remains a reportable, single field listing all assignees across the workflow.
 - 'Distribution Member': Any distribution members in the workflow template automatically populate here and cannot be removed once the workflow initiates. Manual selection of additional distribution members is allowed on the correspondence item, and those can be removed if desired. Notifications are only sent to members on the *workflow distribution list*, not the correspondence item distribution list.

## Prerequisites

- Must have a correspondence type of 'General Correspondence' at the company level. See [Create a New Correspondence Type](/product-manuals/admin-company/tutorials/create-a-new-correspondence-type) or [Edit a Correspondence Type](/product-manuals/admin-company/tutorials/edit-a-correspondence-type).

## Steps

1. Navigate to the project's **Correspondence** tool.
2. Click **+ Create** and from the dropdown list select **General Correspondence**.
3. On the **New General Correspondence** page, complete the form with the desired information. 
   *Note:* An asterisk (\*) denotes a required field.

   - **Number:** This is the unique number to identify this correspondence item. The prefix and number will display in the correspondence in the list view, when linked to other tools, as well as any other location where the correspondence item is listed.
   - \* **Status:** Select one of the following options: 
     *Note:* If a workflow is applied to the correspondence item, the workflow template controls the status once the item is created and issued.
   - \* **Open:** The correspondence is open.
   - \* **Closed Successful:** The correspondence is closed and was successful.
   - \* **Closed Unsuccessful:** The correspondence is closed and was unsuccessful or not approved.
   - \* **Custom Status:** You can select a custom status if any were created. See [Manage Custom Statuses for Correspondence Types](/product-manuals/admin-company/tutorials/manage-custom-statuses-for-correspondence-types).
   - **Subject:** The subject is a title of the correspondence item which will display in the correspondence in the list view, when linked to other tools, as well as any other location where the correspondence item is listed.
   - **Private:** Select **Private** to make the correspondence private. Private correspondences are only visible to the correspondence's creator, the user listed in **Received From**, the users listed in **Assignees**, the users listed in **Distribution**, and users with company or project level 'Admin' permissions.

     ##### Â Note

     - Users who belong to the same companies as the users listed on the item can also view private items if the General Correspondence type has the granular permission of 'View Private Items Accessible to Users within Same Company' enabled.
     - Reach out to your Procore point of contact if you wish for Private correspondence items to be hidden from users with 'Admin' level permissions at the company or project level, ensuring they will not have the ability to view or respond to private items unless they are specifically included on the correspondence item. (If your company is based in Australia or New Zealand, this additional level of privacy will be enabled by default).
     - You can always see who has permissions to private items via the 'Permissions' tab when viewing a correspondence item.

- **Assignees:** Assign responsibility for responding to a general correspondence to one or more project team members from the users in the Directory. Add users with 'Read Only' level permissions or higher to the distribution list. Depending on the user's permission level, they can respond to the correspondence. 
 *Note:* If a workflow is applied to the correspondence item, this field is replaced with 'Current Step Assignee' and is read-only.
- **Due Date:** Enter or select a date from the calendar for the response to be due. 
 *Note:* If a workflow is applied to the correspondence item, this field changes to 'Current Step Due Date' and is read-only.
- **Received From:** Add the person who the correspondence item originated from.
- **Distribution Member:** Add users with 'Read Only level permission or higher to the distribution list. Depending on the user's permission level, they can respond to the correspondence, similar to the 'CC' field of an email. 
 *Note:* If a workflow is applied, once the correspondence item is Issued, any distribution members in the workflow template automatically populate here and cannot be removed. Manually add (or remove) *additional* distribution members on the correspondence item to give them item access. However, notifications are only sent to members on the *workflow distribution list*, not the correspondence item distribution list.
- **\*Schedule Impact:** Select whether this correspondence item's subject does or will affect the schedule.

 - 'Yes': The schedule is impacted in a known way.
 - 'Yes (unknown)': Yes, the schedule is impacted but the details or extent of the impact is not yet known.
 - 'No': The schedule is not impacted.
 - 'TBD': To be determined. You are not sure whether the schedule will be impacted or not.
 - 'N/A': The schedule is not relevant to this correspondence item.
- **Sub Job:** Select a sub job to connect to the correspondence item.
- **Cost Code:** Select a cost code to assign to the correspondence item.
- **Trades:** Select one or more trades to associate with the correspondence item.
- **Location:** Select the location pertaining to the correspondence from the drop-down list.   
 *Note:* If Procore is configured to allow users to create locations (see [Allow or Disallow Users to Create Locations Within a Tool](/product-manuals/admin-project/tutorials/allow-or-disallow-users-to-create-locations-within-a-tool)), you can click **Add New Location** at the bottom of the list.
- **Description:** Provide details about the General Correspondence you want to communicate.
- **Attachments:** Attach the applicable files you want to include in your communication of this General Correspondence. The attachment maximum for each correspondence item is 2,500 files. Attachments included in Responses to the correspondence item do not count toward this maximum. See [What file types and formats are supported in the Unified Attachment Viewer?](/faq-what-file-types-and-formats-are-supported-in-the-attachment-viewer)
- Click one of these buttons:

 - **Save as Draft:** If you want to save your work in a Draft version that can be issued out to the users listed on the General Correspondence at a later date, click this button.| OR
 - **Create & Issue:** If you want to issue this correspondence to the users listed on the General Correspondence who will be notified via email, click this button. 
    *Note:* If a [workflow is applied](/product-manuals/workflows-company/tutorials/start-a-workflow-on-a-project) to the correspondence item, you are asked to confirm understanding that creating the item automatically triggers the start of the assigned workflow.

## Next Step

- [Respond to a Correspondence Item](/product-manuals/correspondence-project/tutorials/respond-to-a-correspondence-item)