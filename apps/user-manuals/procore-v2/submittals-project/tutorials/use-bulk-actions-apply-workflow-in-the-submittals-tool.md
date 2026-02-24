# Use Bulk Actions > Apply Workflow in the Submittals Tool

Source: https://v2.support.procore.com/product-manuals/submittals-project/tutorials/use-bulk-actions-apply-workflow-in-the-submittals-tool

---

## Background

Use the Bulk Actions > Apply Workflow option when you want to apply the same submittal workflow to multiple submittals. This option provides you with the ability to select a workflow template to apply. You can also edit the workflow's membership as needed on the selected submittals.

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions to the Project level Submittals tool.
- **Prerequisites:**

  - Create at least one (1) submittal workflow template to apply using the steps below. See [Manage Submittal Workflow Templates](/product-manuals/submittals-project/tutorials/manage-submittal-workflow-templates).
- **Supported Views:**

  - The Bulk Actions menu is supported in the Submittals tool's Items, Packages, Spec Sections, and Ball In Court views. See [Switch Between Submittals Views](/product-manuals/submittals-project/tutorials/switch-between-submittals-views).
  - The Bulk Actions menu is grayed out and unavailable in the Recycle Bin view.
- **Additional Information:**

  - If you want to bulk edit the submittals that are contained in the same submittal package, follow the steps in [Bulk Edit Submittals in a Package](/product-manuals/submittals-project/tutorials/bulk-edit-submittals).
- **Limitations:**

  - The submittal(s) must be in the 'Draft' status and must NOT have any existing submitters or approvers in the Submittal Workflow.
  - Changes to the workflow using the steps below are only applied to the selected submittals and do NOT affect the template.To edit the membership of the template, see [Manage Submittal Workflow Templates](/product-manuals/submittals-project/tutorials/manage-submittal-workflow-templates).

## Steps

1. Navigate to the project's **Submittals** tool. This reveals the Items view of the Submittals page. This page lists all of the individual submittals for the project (except for any submittals sent to the Recycle Bin).
2. Locate the submittals in the 'Draft' status to which you want to apply a submittal workflow:

   - To select all of the submittals in the list, mark the checkbox at the top of the left column.  
      OR
   - To select one or more of the submittals in the list, mark the check box to the left of each desired submittal.
3. Choose **Bulk Actions** > **Apply Workflow**. *Note*: The Bulk Actions menu is supported in the *Items*, *Packages*, *Spec Sections*, and *Ball In Court* views. It it NOT supported in the *Recycle Bin*. This reveals the Bulk Edit page. The 'Selected Submittals' box shows the individual submittals to which your edits will be applied.
4. Select due date behavior from the following options:  
   *Note: These options will only be visible if the 'Submit By Date' field is enabled on the* [fieldset configured](/faq-what-are-configurable-fieldsets-and-which-procore-tools-support-them) *for the project's Submittals tool. If 'Submit By Date' is NOT enabled, these options will NOT appear, and the workflow will automatically use the âCalculate from todayâs date' option.*

   - **Calculate from today's date.** This option calculates the workflow due date by adding the number in the Days to Submit/Respond to today's date.
   - **Calculate from each submittal's Submit By date.** This option sets the first step of the workflow to each submittal's Submit By date, with the due dates for the following steps calculated forward from that date.
5. Select a submittal workflow template to apply. To learn how to create a template, see [Manage Submittal Workflow Templates](/product-manuals/submittals-project/tutorials/manage-submittal-workflow-templates).
6. Edit the submittal workflow on the selected items using these options:

   - Click **Add Step** to add new members to the workflow. *Note*: This action does NOT affect the membership on the template. It simply updates the workflow on the selected submittals.
   - Click the '**x**' on a line item to remove the submitter or approver. *Note*: To learn more about the other workflow options, see [Add a Submitter and Approvers to the Submittal Workflow](/product-manuals/submittals-project/tutorials/add-submitter-and-approvers-to-the-submittal-workflow)
7. Click **Apply Template**. This applies the workflow template to the selected submittals. A GREEN banner appears to confirm the total number of submittals that were successfully edited. A RED banner will appear in the event that the edits are NOT successfully saved.