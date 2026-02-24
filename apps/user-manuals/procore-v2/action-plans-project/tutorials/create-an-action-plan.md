# Create an Action Plan

Source: https://v2.support.procore.com/product-manuals/action-plans-project/tutorials/create-an-action-plan

---

## Background

The Action Plans tool helps ensure that your unique company and project-specific requirements are clearly defined, centralized, and organized. Action plans created in Procore are reviewed for approval by key project stakeholders before being performed. Once an action plan is performed, it is reviewed again (along with any related records provided as evidence) after completion to confirm that the set standard of quality was met.

## Things to Consider

- [Required User Permissions](/product-manuals/action-plans-project/permissions)
- Action plans can be marked as 'Private' and only visible to certain users.
- When published, the status of an action plan is automatically set to 'In Progress'.
- Required Assignees can only be removed while creating or editing an action plan.
- Optional assignees can be removed while performing or editing an action plan.
- An item's due date can be modified or removed by a user with 'Admin' level permissions to the Action Plans tool while performing the action plan.
- To add references, you must have permissions to view the item(s) in the respective tool(s).
- To see references and to add requested records, users [performing an action plan](/product-manuals/action-plans-project/tutorials/perform-an-action-plan) must have permissions to view the item(s) in the respective tool(s).
- To be added as the Plan Manager, the user must have 'Admin' level permissions on the project's Action Plans tool.
- To be added as an Action Plan Approver, the user must have 'Standard' level permissions or higher on the project's Action Plans tool.
- To be added as a Completed Action Plan Receiver, the user must have 'Standard' level permissions or higher on the project's Action Plans tool.

## Prerequisites

- [Create Action Plan Types](/product-manuals/admin-company/tutorials/create-action-plan-types)
- *Optional:* [Create a Company Level Action Plan Template](/product-manuals/admin-company/tutorials/create-a-company-level-action-plan-template) or [Create and Edit a Project Level Action Plan Template](/product-manuals/action-plans-project/tutorials/create-and-edit-project-level-action-plan-template)

##### Â Tip

To help you get started, you can use Procore's pre-populated action plan templates.

## Steps

- Add General Information
- Add Sections and Items
- Copy Sections and Items

#### Add General Information

1. Navigate to the project's **Action Plans** tool.
2. Do one of the following:

   1. To create the action plan from a template, click **Create** and click the template name. *Note:* Action plan templates that are in 'Edit' mode cannot be selected.
   2. To create an action plan without a template, click **Create** and click **Create New Plan**.
3. Complete the following under 'General Information'.

   - Enter a **Name** for the action plan.
   - Select the **Plan Manager** who is the user responsible for overseeing all stages of the action plan throughout its cycle.
   - Select a **Type** from the list.

     - If the type is not listed, click **+Create Type**. See [Create Action Plan Types](/product-manuals/admin-company/tutorials/create-action-plan-types). *Note:* You must have 'Admin' level permissions on the Company level Admin tool to perform this action.
   - Select a **Location** from the list.

     - If the location is not listed, click **+Create Location.** See [Add Locations to a Project](/product-manuals/admin-project/tutorials/add-multi-tiered-locations-to-a-project). *Note:* You must have 'Admin' level permissions on the Company level Admin tool to perform this action.
   - Mark the **Private** checkbox to make the action plan visibile to only certain people.
   - Enter a **Description** for the action plan.
   - Click **Add Approvers** and select one or more users from the list.
   - Click **Completed Action Plan Receivers** and select one or more users from the list.
4. Click **Create & Add Sections**.

#### Add Sections and Items

1. Enter a name for the first section.
2. Complete the following for the first item within the first section:

   - Under 'Title', enter a name for the item.
   - Enter any 'Acceptance' Criteria for the item.
   - Click **+ Add Document** to add photos, drawings, forms, documents, and attachments to the action plan for reference. Action Plans always reference the latest version of uploaded drawings.
   - Click **+ Add Procore Item** to add items such as specifications, correspondence, submittals, observations, and meetings. The action plan will always reference the latest version of a specification.
   - Select a **Due Date** for the item.
   - Click **Edit Assignees** to assign responsible parties to the item and to designate whose signatures are requested.

     - Under Blocking Functionality, select one of three options to manage the workflow linearity of your Action Plan. See [What is 'Blocking Functionality' in an action plan?](/faq-what-is-blocking-functionality-in-an-action-plan)
     - **Assignee signature required to release rest of section:** This option requires the assignee's signature to unlock subsequent items within the same Action Plan section, ensuring linear progression.
     - **Assignee signature required to release rest of plan:** This option requires the assignee's signature to block the completion of all subsequent items and sections in the entire Action Plan.
     - **None:** This option allows item completion without an assignee's signature, enabling flexible, non-sequential task completion.
     - Select the **Assignee** drop-down menu (an entity or a specific person).
     - If the person is not listed in the drop-down menu, click **Create Person** to add a new contact as the assignee. See [What is a 'contact' in Procore?](/faq-what-is-a-contact-in-procore-and-which-project-tools-support-the-concept)
     - Select the **Verification Method** the assignee should use to verify the item's completion. See [Create Action Plan Verification Methods](/product-manuals/admin-company/tutorials/create-action-plan-verification-methods).
     - If the verification method is not listed in the drop-down menu, click **+Create New Verification Method**. *Note:* You must have 'Admin' level permissions on the Company level Admin tool to perform this action.
     - Enter a name for the verification method.
     - Click **Create**.
     - Click **Save**.
     - Under **Required**, select the checkbox to require an assignee signature. *Note*: If the Required checkbox associated with the assignee is not selected, blocking functionality will not be enabled.
     - Click **Add Assignee** to add additional responsible parties.
     - Click **Save**.
   - Click **Add Records** to request one or more records to be included as part of the item's completion.

     - Click **Inspections, Correspondence,** or **Forms** andmark one more checkboxes next to the template or type you want to request. *Note:* 'Read Only' level permissions or higher on the corresponding Project level tool is required to request records for that tool.
     - Click **Submittals**, **Meetings**, **Observations**, **Attachments** (including **Documents**), or **Photos** and mark the **checkbox** to request that record.
     - Click **Save** after selecting the requested records for the item.
3. Click **Add Item** to add a new item within the section.
4. Click **Add Section** to add a new section.
5. Continue adding sections and items as necessary.

   - [Copy Sections and Items on an Action Plan](/product-manuals/action-plans-project/tutorials/copy-action-plan-items-and-sections)
   - [Bulk edit items](/product-manuals/action-plans-project/tutorials/edit-an-action-plan)
   - [Rearrange sections or items.](/product-manuals/action-plans-project/tutorials/edit-an-action-plan)
   - [Delete a section or item.](/product-manuals/action-plans-project/tutorials/edit-an-action-plan)
6. When you are finished adding sections and items, click **Save Draft** to save it as a draft, or click **Publish** if you're ready for the action plan to be approved to be performed.

   ##### Â Note

   Clicking **Publish** shifts the action plan into 'View' mode where it can be approved and performed.