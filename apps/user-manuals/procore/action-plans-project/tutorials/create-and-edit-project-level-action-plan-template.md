# Create and Edit a Project Level Action Plan Template

Source: https://v2.support.procore.com/product-manuals/action-plans-project/tutorials/create-and-edit-project-level-action-plan-template

---

## Background

Templates can be created at the Company level or Project level, allowing you to easily use the same action plan structure across your project without needing to recreate templates with similar requirements multiple times. Templates can be created from scratch or can be built from templates that were previously created at Company level.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Action Plans tool. 
     OR
 - 'Read Only' or 'Standard' level permissions on the project's Action Plans tool with the 'Create and Edit Project Templates' granular permission enabled on your permissions template.
- **Additional Information**:

 - The default general information and default sections and items can be changed while an action plan is being created from a template by users with the appropriate permissions.
 - Project templates can have the same name as templates managed at the Company level.
 - Every field in a project template is fillable and will copy over to action plans that are created using that template.
 - You can set templates to 'Private' by default. However, when creating an action plan from a template, users can select to make the action plan private or not.

## Prerequisites

- [Create Action Plan Types](/product-manuals/admin-company/tutorials/create-action-plan-types)
- *Optional:* [Create a Company Level Action Plan Template](/product-manuals/admin-company/tutorials/create-a-company-level-action-plan-template) or Create and Edit a Project Level Action Plan Template

## Steps

- Add Default General Information
- Add Default Sections and Items
- Copy Sections and Items
- Bulk Edit Items
- Rearrange Sections or Items
- Delete Sections or Items
- View and Edit a Company level Template at the Project level

### Add Default General Information

1. Navigate to the Project level **Action Plans** tool.
2. Click the **Action Plans Settings** icon.
3. Navigate to the 'Templates' tab.
4. Click **+Create Template**.
5. Select to create a new template from an existing company template, or to create a new template from scratch.
6. Enter the general information.
7. Continue and Add Default Sections and Items or click **Save Draft** or **Publish**.

### Add Default Sections and Items

1. Enter a name for the section.
2. Complete the information for each item within the section:

   - Under the 'Title' column, enter a name for the item.
   - Under the 'Acceptance Criteria' column, enter any requirements associated with this item's successful completion.
   - Click **+ Add Document** to add photos, drawings, forms, documents, and attachments to the action plan for reference.\* Action Plans always reference the latest version of uploaded drawings.
   - Click **+ Add Procore Item** to add items such as specifications, correspondence, submittals, observations, and meetings.\* The action plan will always reference the latest version of a specification.
   - Under the 'Assignees' column, click **+Edit Assignees** to assign responsible parties to the item and to designate whose signatures are requested.

     - In the 'Edit Assignees' window, complete the following:

       - Under 'Blocking Functionality', select the button for one of the following options: (See [What is 'Blocking Functionality' in an action plan?](/faq-what-is-blocking-functionality-in-an-action-plan))

         - **Assignee signature required to release rest of section**. This will require the assignee's signature before all remaining items in the same section are released to be completed but will allow released items in other sections to be completed.
         - **Assignee signature required to release rest of plan**. This will require the assignee's signature before all items in all remaining sections are released to be completed.
         - **None**. This will allow other released items in the action plan to be completed regardless of when this item's assignee adds their signature. 
           *Note:* The assignee's signature must be marked as 'Required'.
         - Click **Select Assignee** and select the entity (e.g., 'Contractor') for the responsible party. 
           *Note:* Specific users can be added as assignees when action plans are being performed.
         - Click **Select Verification Method** and select the method the responsible party should use to verify the item's completion. See [Create Action Plan Verification Methods](/product-manuals/admin-company/tutorials/create-action-plan-verification-methods).
         - To create a new verification method while creating the action plan template:

           - Click **+Create New Verification Method**.
           - Enter a name for the verification method.
           - Click **Create**.
           - If you selected **Assignee signature required to release rest of section** or **Assignee signature required to release rest of plan** as noted above: Mark the checkbox in the 'Required' column to require the assignee's signature and to block remaining items in the section or in the plan from being completed until this assignee adds their signature.
           - Click **+Add Assignee** to add additional entities for additional responsible parties.
           - Click **Save**. *Notes:*

             - Assignees added when an action plan is being created or edited are considered required and can only be removed while creating or editing an action plan.
             - Additional assignees added while an action plan is being performed are considered optional and can be removed while performing or editing an action plan.
   - Under the 'Records' column, click **+Add Records** to request one or more records to be included as part of the item's completion.

     - Click **Inspections** and mark one or more checkboxes next to each inspection template that you want to be used for adding or creating inspections for the item. Note: 'Read Only' level permissions or higher on the Project level Inspections tool are required to request records using project inspections templates.
     - Click **Correspondence** and mark one or more checkboxes next to each correspondence type that you want to be used for adding or creating correspondence items for the item. *Note:* 'Read Only' level permissions or higher on one of the project's correspondence types are required to request correspondence records.
     - Click **Forms** and mark one or more checkboxes next to each form that you want attached as a record *Note:* 'Read Only' level permissions or higher on the Project level Forms tool are required to request form records.
     - Click **Submittals**, **Meetings**, **Observations**, **Attachments**, or **Photos** and mark the **checkbox** to request that record.
     - Click **Save** after selecting the requested records for the item.
3. Click **+Add Item** to add a new item within the section.
4. Click **+Add Section** to add a new section.
5. Continue adding sections and items as necessary.

   - Copy sections and items on an action plan
   - Bulk edit items
   - Rearrange sections or items
   - Delete a section or item
6. Click Save **Draft** or **Publish**.

### Copy Sections and Items on an Action Plan

1. Under '**Sections and Items**', locate the section or item you want to copy.
2. Do one of the following:

   1. If you are copying a section, hover over the section title bar and click **Duplicate** .
   2. If you are copying an item, hover over the item and click **Duplicate** .
3. Fill out the information as needed in the newly created section or item.
4. Do one of the following:

   1. Click **Save Draft**.
   2. Click **Publish.**

### Bulk Edit Items

1. Mark the checkboxes next to the items you want to edit.
2. Select to **Add**, **Edit**, or **Replace Assignees** based on the change you want to make.

   - You can add Assignees, Records, or References.
   - You can edit Acceptance Criteria, Due Dates or Item Status.
   - You can Replace Assignees and update their Verification Method.
3. Enter the new information.
4. Click **Save**.

### Rearrange Sections or Items

1. Hover your cursor over the beginning of the row with the section or item you want to move.
2. Click and hold the vertical grip (â®â®) **icon**.
3. Drag and drop the row to move it up or down in the table's order.

### Delete a Section or Item

1. Hover your cursor over the end of the row.
2. Click the icon.
3. Click **Delete**.

### View and Edit a Company level Template at the Project level

1. Navigate to the Project level **Action Plans** tool.
2. Click the settings gear to access **Action Plans Settings**.
3. Navigate to the 'Templates' tab.
4. Select the Company template you want to manage. *Note:* The vector symbol indicates that the action plan template is managed at the Company level.
5. Click the Edit button to make changes to the template.
6. Onces changes have been made, click Publish. *Note:* Changes are automatically saved.

## Next Steps

- [Create an Action Plan](/product-manuals/action-plans-project/tutorials/create-an-action-plan)