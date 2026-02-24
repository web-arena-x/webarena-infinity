# Manage Submittal Workflow Templates - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/manage-submittal-workflow-templates

---

## Objective

To manage submittal workflow templates.

## Background

In Procore, a **submittal workflow template** provides users with 'Admin' level permission on the Submittals tool with the ability to define the submitter(s) and approver(s) for your project's submittal review process. You can create multiple workflow templates to suit the specific needs of your review process.

## Things to Consider

- **Required User Permissions:**
 - 'Admin' level permissions on the project's Submittals tool
- **Additional Information:**
 - Submittal workflow templates can be applied to 'Draft' submittals using Bulk Actions as long as they do not have any existing submitters or approvers in their workflows. See [Use Bulk Actions > Apply Workflow in the Submittals Tool](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/use-bulk-actions-apply-workflow-in-the-submittals-tool "Use Bulk Actions > Apply Workflow in the Submittals Tool").
 - Submittal workflow templates can be applied in bulk to submittals in packages as long as the submittals do not have any existing submitters or approvers in their workflows. See [Bulk Edit Submittals in a Package](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/bulk-edit-submittals "Bulk Edit Submittals in a Package").
 - Any changes you make to an existing submittal workflow template, including deleting the template, will not affect submittals that used the template.

## Steps

- [Create a Submittal Workflow Template](#Create_a_Submittal_Workflow_Template "Manage Submittal Workflow Templates")
- [Delete a Submittal Workflow Template](#Delete_a_Submittal_Workflow_Template "Manage Submittal Workflow Templates")

### Create a Submittal Workflow Template

1. Navigate to the project's **Submittals** tool.
2. Click the **Configure Settings** ![icons-settings-gear.png](https://support.procore.com/@api/deki/files/89566/icons-settings-gear.png?revision=2&size=bestfit&width=15&height=15) icon.
3. Click ****Submittal Workflow Templates****in the right sidebar.
4. Complete the following: 
   *Note:* An asterisk (\*) below indicates a required field.
   - ****\*Template Name:**** Enter a name for your new submittal workflow template.
   - ****\*Name:**** Click on the space below the 'Name' column to search for and select one or more users or distribution groups to add them to the first step in the submittal workflow.
     - To make the user's response required, mark the checkbox next to their name. 
       OR
     - To make the user's response optional, clear the checkbox next to their name. 
       **Note*:* If you add more than one user to the same step in the submittal workflow, the [Ball In Court](../../../../../../references/construction-management/glossary-of-terms.md#Ball_In_Court "Glossary of Terms") responsibility on the submittal will shift to the next workflow step after all of the users with responses required in the step have submitted their response.
   - ****Role:**** Select **Approver**or **Submitter**. 
     *Notes:*
     - To be added to the submittal workflow, a user must exist in the Project level Directory tool (see [Add a User Account to the Project Directory](https://support.procore.com/products/online/user-guide/project-level/directory/tutorials/add-user-account-to-project-directory "Add a User Account to the Project Directory"))and must have 'Standard' level permissions or higher on the project's Submittals tool.
     - If you add one or more users as 'Submitters' in the submittal workflow, we recommend that you designate a Submittal Manager (or another submittal reviewer at your company) as an 'Approver' in the step immediately after the 'Submitter' step. This allows your internal team to review the submittal before it is sent to any reviewers outside of your company (for example, the project's design team) in later steps of the submittal workflow.
   - **Days to Submit/Respond:** Enter a number of days for the submitter or approver to submit a response. The default value is based on the 'New Submittals Will Be Due In' setting for the project (see [Configure Settings: Submittals Tool](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/configure-settings-submittals-tool "Configure Settings: Submittals Tool")). 
       
     ![submittals-submittal-workflow-template.png](https://support.procore.com/@api/deki/files/292150/submittals-submittal-workflow-template.png?revision=1)
5. To add another step in the workflow, click **Add Step** and repeat step 4.
6. To add another workflow template, click **Add New Template** and repeat steps 4 and 5 as needed.
7. Click **Update**. 
   Your new template will be available to add on new or existing submittals.

### Delete a Submittal Workflow Template

1. Navigate to the project's **Submittals** tool.
2. Click the **Configure Settings** ![icons-settings-gear.png](https://support.procore.com/@api/deki/files/89566/icons-settings-gear.png?revision=2&size=bestfit&width=15&height=15) icon.
3. Click ****Submittal Workflow Templates****in the right sidebar.
4. Click the ![icon-delete-trash.png](https://support.procore.com/@api/deki/files/90896/icon-delete-trash.png?revision=1&size=bestfit&width=15&height=15) trash can icon across from the template name.

## See Also

- [Apply a Submittal Workflow Template to a Submittal](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/apply-a-submittal-workflow-template-to-a-submittal "Apply a Submittal Workflow Template to a Submittal")

## 

If you would like to learn more about Procore's submittals management software and how it can help your business, please visit our [construction submittals software product page ![icon-external-link.png](https://support.procore.com/@api/deki/files/186764/icon-external-link.png?revision=2&size=bestfit&width=14&height=14)](https://www.procore.com/project-management/submittals "https://www.procore.com/project-management/submittals").