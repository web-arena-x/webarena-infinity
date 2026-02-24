# Use Bulk Actions > Edit in the Submittals Tool - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/use-bulk-actions-edit-in-the-submittals-tool

---

## Objective

To use the Bulk Actions menu in the Submittals tool to perform bulk edits on a batch of submittals.

## Background

Use the Bulk Actions > Edit option when you want to apply the same edits on multiple submittals.

## Things to Consider

- **Required User Permissions**:
 - 'Admin' level permissions to the project's Submittals tool.
- **Supported Views**:
 - The Bulk Actions menu is supported in the Submittals tool's *Items*, *Packages*, *Spec Sections*, and *Ball In Court* views. See [Switch Between Submittals Views](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/switch-between-submittals-views "Switch Between Submittals Views").
 - The Bulk Actions menu is dimmed and unavailable in the Recycle Bin view.
- **Additional Information**:
 - Automatic email notifications are not sent for submittal updates made using Bulk Actions. To learn more about automatic email notifications for the project's Submittals tool, see [Who receives an email when a submittal is created or updated?](https://support.procore.com/faq/who-receives-an-email-when-a-submittal-is-created-or-updated "Who receives an email when a submittal is created or updated?")
 - To bulk edit submittals contained in a single submittal package, follow the steps in [Bulk Edit Submittals in a Package](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/bulk-edit-submittals "Bulk Edit Submittals in a Package").

## Steps

1. Navigate to the project's **Submittals** tool.
2. Locate the submittals to modify in the **Items**, **Packages**, **Specification Sections** or **Ball In Court** tabs. Then:
   - To select all of the submittals in the list, mark the checkbox at the top of the left column. 
     OR
   - To select one or more of the submittals in the list, mark the check box to the left of each desired submittal.
3. Choose **Bulk Actions** > **Edit** .  
   *Note*: The Bulk Actions menu is NOT available in the *Recycle Bin*. See [Perform Bulk Actions on Submittals](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/perform-bulk-actions-on-submittals "Perform Bulk Actions on Submittals").
4. Choose from these editing options: 
   (*Note:* Editing options in your project's Submittals tool can vary if your company has configured [custom fields](https://support.procore.com/faq/what-are-custom-fields-and-which-procore-tools-support-them "What are custom fields and which Procore tools support them?") and [configurable fieldsets](https://support.procore.com/faq/what-are-configurable-fieldsets-and-which-procore-tools-support-them "What are configurable fieldsets and which Procore tools support them?").) 
     
   ![submittals-bulk-edit-page.png](https://support.procore.com/@api/deki/files/88347/submittals-bulk-edit-page.png?revision=2)
   - ****Specification Section****. Denotes the corresponding section from the project's specifications. See [Where do the selections in the 'Specification Sections' drop-down list in the Submittals tool come from?](https://support.procore.com/faq/where-do-the-selections-in-the-spec-sections-drop-down-list-come-from "Where do the selections in the 'Spec Sections' drop-down list in the Submittals tool come from?")
   - ****Submittal Manager****. The name of the [submittal manager](../../../../../../references/construction-management/glossary-of-terms.md#Submittal_Manager "Glossary of Terms"). This is the person who is responsible for overseeing the submittal throughout its lifecycle in Procore. Each submittal can have a different submittal manager, or your project team can configure a 'Default Submittal Manager' for all of your submittals. See [What is the 'Submittal Manager' role?](https://support.procore.com/faq/what-is-the-submittal-manager-role "What is the 'Submittal Manager' role?")
   - ****Responsible Contractor****. The company that is responsible for completing the work specified on the submittal.  
     *Note*: Users can only be added to the 'Received From' field if their Procore Directory record is associated to the company listed as the 'Responsible Contractor' on the submittal.
   - ****Cost Code****. Select a cost code to associate with the selected submittals.
   - ****Received From****. The contact for the responsible contractor who provided the submittal information to the project team. 
     *Note*: Users can only be added to the 'Received From' field if their Procore Directory record is associated to the company listed as the 'Responsible Contractor' on the submittal. To add a user to the 'Received From' field who is not associated with a submittal's current 'Responsible Contractor', first select the desired user's company in the 'Responsible Contractor' menu. Then you are able to select the user's name in the 'Received From' menu.
   - **Add to Distribution List.** Add one (1) or more users and/or distribution groups to selected submittals’ distribution lists.
   - **Remove from Distribution List.**Remove one (1) or more users and/or distribution groups from selected submittals’ distribution lists.
   - ****Private****. Select **Yes** to make the selected submittals Private. Otherwise, choose **No**.
   - ****Status****. The current status of the submittal. Only a user with 'Admin' level permission to the Submittals tool can change a submittal's status. See [What are the default submittal statuses in Procore?](https://support.procore.com/faq/what-are-the-default-submittal-statuses-in-procore "What are the default submittal statuses in Procore?") and [What is a 'Draft' Submittal?](https://support.procore.com/faq/what-is-a-draft-submittal "What is a 'Draft' Submittal?")
   - ****Type****. The information type associated with the submittal. The default type selections in Procore include: **Document**, **Plans**, **Prints**, **Product Information**, **Product Manual**, **Sample**, **Shop Drawing**, and **Other**. See [Create Custom Submittal Types](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/create-custom-submittal-types "Create Custom Submittal Types").
   - ****Location****. The location at the job site for the submittal. This can be an existing location from the Location list or a tiered location. See [Add Tiered Locations to a Project](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/add-multi-tiered-locations-to-a-project "Add Tiered Locations to a Project").
   - ****Sub Job****. If sub jobs are enabled on your project, select one to associate it with the selected submittals. See [What's the difference between a job, a parent job, and a sub job?](https://support.procore.com/faq/what's-the-difference-between-a-job-a-parent-job-and-a-sub-job "What's the difference between a job, a parent job, and a sub job?")
   - ****Lead Time****. The expected number of calendar days that will be required for the material/services for the submittal to arrive.
   - ****Submit By****. Select the date by which a contractor/subcontractor must submit all relevant documentation (i.e., documents, drawings, manuals, plans, and so on) for the submittal to the project's design team for review.
   - ****Received Date****. The date that the submittal information was received from the contractor/subcontractor responsible for the performing work associated with the submittal.
   - ****Issue Date****. The date the contractor/subcontractor submitted the submittal items (i.e., documents, plans, and so on) to your project team for the review process.
   - ****Required On-Site Date****. The date by which materials related to the work detailed on the submittal must be delivered and available at the construction site.
5. Click **Update**.  
   A GREEN banner appears to confirm the total number of submittals successfully edited. A RED banner appears when edits are not successfully saved.

## See Also

- [Perform Bulk Actions on a Submittal](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/perform-bulk-actions-on-submittals "Perform Bulk Actions on Submittals")