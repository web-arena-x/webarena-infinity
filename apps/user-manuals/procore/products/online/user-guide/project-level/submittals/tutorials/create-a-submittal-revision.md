# Create a Submittal Revision - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/create-a-submittal-revision

---

## Objective

To create a revision of an existing submittal using the Project level Submittals tool.

## Things to Consider

- **Required User Permissions:**
 - *To create a revision for a submittal that you created:*
    - 'Read Only' or 'Standard' level permissions on the project's Submittals tool with the ['Create Submittal' granular permission](../../../company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#Submittals "Grant Granular Permissions in a Project Permissions Template") enabled on your permissions template.  
      OR
    - 'Standard' level permissions on the project's Submittals tool without a permissions template assigned to you.
 - *To create a revision for a submittal that you did not create:*
    - 'Standard' level permissions on the project's Submittals tool and be designated as the [Submittal Manager](../../../../../../references/construction-management/glossary-of-terms.md#Submittal_Manager "Glossary of Terms").
 - *To create a revision for any submittal:*
    - 'Admin' level permissions on the project's Submittals tool.
- **Additional Information:**
 - You can only create a revision for the most current revision of submittal. For example, if a submittal at Revision 0, you can only create Revision 1. To learn more, see [What is a submittal revision?](https://support.procore.com/faq/what-is-a-submittal-revision "What is a submittal revision?")

## Steps

1. Navigate to the project's **Submittals** tool. 
   This reveals the Submittals page.
2. In the Submittals log, locate the desired submittal. Then click **View**.  
   This opens the submittal in view mode.
3. Click the vertical ellipsis![icon-ellipsis-vertical.png](https://support.procore.com/@api/deki/files/158014/icon-ellipsis-vertical.png?revision=2&size=bestfit&width=17&height=17), then click **Create Revision**. This opens the 'Create Revision' page.  
   *Note*: This button is only visible and available when you are viewing the most current revision of a submittal. You can only create a new revision from the most recent one.
4. Scroll to the 'General Information' area and note that all of the general information from the previous revision is inherited. In addition, the revision number is automatically incremented by one (n +1). In the example below, the previous revision number was 1, so Procore automatically increments the new revision number to 2.
5. Revise the following submittal information as needed:
   - **Title**. The descriptive name that best summarizes the information in the submittal.
   - **Spec Section**. Denotes the corresponding section from the project's specifications book. See [Where do the selections in the 'Specification Sections' drop-down list in the Submittals tool come from?](https://support.procore.com/faq/where-do-the-selections-in-the-spec-sections-drop-down-list-come-from "Where do the selections in the 'Spec Sections' drop-down list in the Submittals tool come from?")
   - **Received From**. The contact for the responsible contractor who provided the submittal information to the project team.
   - **Submittal** **Package.**The [submittal package](../../../../../../references/construction-management/glossary-of-terms.md#Submittal_Package "Glossary of Terms") that contains the submittal. In Procore, adding submittals to a package is optional. The decision to add submittals to a submittal package is based on your project's requirements, which is determined by your company's or project's management team. For instructions, see [Create a Submittal Package](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/create-a-submittal-package "Create a Submittal Package").
   - **Status**. The current status of the submittal. Only a user with 'Admin' level permission to the Submittals tool can change a submittal's status. See [What are the default submittal statuses in Procore?](https://support.procore.com/faq/what-are-the-default-submittal-statuses-in-procore "What are the default submittal statuses in Procore?") and [What is a 'Draft' Submittal?](https://support.procore.com/faq/what-is-a-draft-submittal "What is a 'Draft' Submittal?")
   - **Cost Code**. The [cost code](../../../../../../references/construction-management/glossary-of-terms.md#Cost_Code "Glossary of Terms") for the submittal. Cost codes are managed in the 'Cost Code' segment in Procore's [Work Breakdown Structure](https://support.procore.com/products/online/work-breakdown-structure "Work Breakdown Structure").
   - **Type**. The information type associated with the submittal. The default type selections in Procore include: *Document*, *Pay Request, Payroll,**Plans*, *Prints*, *Product Information*, *Product Manual*, *Sample*, *Shop Drawing*, *Specification,*and *Other*. See [Create Custom Submittal Types](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/create-custom-submittal-types "Create Custom Submittal Types").
   - **Location**. The location at the job site for the submittal. This can be an existing location from the Location list or a tiered location. See [Add Tiered Locations to a Project](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/add-multi-tiered-locations-to-a-project "Add Tiered Locations to a Project").
   - **Private**. Indicates privacy settings for the submittal. When a submittal is marked 'Private', it is only visible to users with 'Admin' level permissions on the Submittals tool, users in the Submittal Workflow, and members of the submittal's Distribution List. Users with the ['View Private Submittals Associated to Users within Same Company' granular permission](../../../company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#Submittals "Grant Granular Permissions in a Project Permissions Template") enabled on their permissions template can also view a submittal marked 'Private' if another user in their company is associated with the submittal. See [Mark a Submittal as Private](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/mark-a-submittal-as-private "products/online/user-guide/project-level/submittals/tutorials/mark-a-submittal-as-private").
   - **Description**. Informative details, notes, and/or actions that describe the submittal.
   - **Attachments**. Attach any relevant files. You have these options:

     - Click **Attach File(s)**and then choose the appropriate option from the shortcut menu that appears. 
       OR
     - Use a drag-and-drop operation to move files from your computer into the grey **Drag and Drop File(s)** box.

     *Note:* If the previous revision of the submittal had any file attachments, you will need to reattach them in the new revision, if desired. Attachments are NOT carried over between revisions.
   - **Submittal Workflow**. The people assigned to complete the [submittal workflow](../../../../../../references/construction-management/glossary-of-terms.md#Submittal_Workflow "Glossary of Terms"). In Procore, the submittal workflow includes two roles: a [submitter](../../../../../../references/construction-management/glossary-of-terms.md#Submitter "Glossary of Terms") and the approvers who are responsible for performing/completing the [approval process](../../../../../../references/construction-management/glossary-of-terms.md#Approval_Process "Glossary of Terms"). Typically, approvers are members of the design team.
   - **Distribution List**. The people who will receive email notifications from Procore as the submittal progresses through the [submittal workflow](../../../../../../references/construction-management/glossary-of-terms.md#Submittal_Workflow "Glossary of Terms"). If your project team has created any distribution lists in the Project Directory, you can select those lists here. See [Add a Distribution Group to the Procore Directory](https://support.procore.com/products/online/user-guide/project-level/directory/tutorials/add-a-distribution-group-to-the-project-directory "Add a Distribution Group to the Project Directory")).
   - **Related Items**. Any related items that have been added to the submittal (i.e., drawings, documents, plans, and so on). See [Add a Related Item to a Submittal](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/add-a-related-item-to-a-submittal "Add a Related Item to a Submittal").
   - **Custom Fields**​. If your company has added custom text fields for use with the Submittals tool, enter the required data as specified by your project team in these fields. See [Configure Advanced Settings: Submittals Tool](configure-settings-submittals-tool.md#Configure_the_Submittal_Tool's_Settings "Configure Advanced Settings: Submittals Tool").
6. Choose from the following:
   - **Create & Send Emails**: Use this option to create the new submittal﻿ revision and send it to the designated submittal approver(s), as well as all members on the submittal's distribution list (optional).
   - **Create But Do Not Send Emails**: Use this option to only create the new revision but not send any email notifications.

## See Also

- [What is a submittal revision?](https://support.procore.com/faq/what-is-a-submittal-revision "faq/what-is-a-submittal-revision")
- [Search for and Filter Submittals](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/search-for-and-filter-submittals "Search for and Filter Submittals")

## 

If you would like to learn more about Procore's submittals management software and how it can help your business, please visit our [construction submittals software product page ![icon-external-link.png](https://support.procore.com/@api/deki/files/186764/icon-external-link.png?revision=2&size=bestfit&width=14&height=14)](https://www.procore.com/project-management/submittals "https://www.procore.com/project-management/submittals").