# View a Submittal - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/view-a-submittal

---

## Objective

To view a submittal.

## Things to Consider

##### Tip

Users may require specific roles on a submittal (or granular permissions) to view the submittal depending on its privacy settings.

**What user roles can view which types of submittals?** **Show/Hide**

In the table below, the ![icon-mindtouch-table-check.png](https://support.procore.com/@api/deki/files/91423/icon-mindtouch-table-check.png?revision=3&size=bestfit&width=18&height=18) icon indicates which user roles can view a submittal based on its status and privacy settings, and the ![icon-delete-x.png](https://support.procore.com/@api/deki/files/90870/icon-delete-x.png?revision=1&size=bestfit&width=18&height=18) icon indicates which user roles cannot view a submittal based on its status and privacy settings.

| User Role | Submittal Type | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| Public Submittal | Private Submittal |
| Creator | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png |
| Submittal Manager | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png |
| Workflow Member | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png |
| Distribution List Member | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png |
| No Role | icon-mindtouch-table-check.png | icon-delete-x.png 1 |
| Tool Admin | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png |

1 Users with the ['View Private Submittals Associated to Users within Same Company' granular permission](../../../company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#submittals "Grant Granular Permissions in a Project Permissions Template") enabled on their permissions template can view any submittal marked 'Private' if another user in their company (including them) is the submittal's creator or is designated as the Submittal Manager, a workflow member, or a Distribution List member.

- **Required User Permissions:**
 - *To view a submittal not marked 'Private':* 'Read Only' level permissions or higher on the project's Submittals tool.
- **Additional Information:**
 - A 'Private' submittal is visible to the following users:
    - The submittal's creator, Submittal Manager, Submittal Workflow members, and Distribution List members
    - Users with 'Admin' level permissions on the project's Submittals tool
    - Users with 'Read Only' or 'Standard' level permissions on the project's Submittals tool with the ['View Private Submittals Associated to Users within Same Company' granular permission](../../../company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#Submittals "Grant Granular Permissions in a Project Permissions Template") enabled on their permissions template (if another user in their company [including them] is the submittal's creator or is designated as the Submittal Manager, a Submittal Workflow member, or a Distribution List member)

## Steps

1. Navigate to the project's **Submittals** tool.
2. Click **View** next to the submittal you want to view.
3. View the following information:
   - **Submittal Workflow** This section includes attachments added to the submittal's 'General Information' when the submittal was created or edited. This section also details the submitters and approvers on the submittal. It also shows their official response, comments, and attachments that may have been added with their response. See [Add Users to the Submittal Workflow](create-a-submittal.md#Add_Users_to_the_Submittal_Workflow "Create a Submittal").

     ##### Note

     The ![icon-error.png](https://support.procore.com/@api/deki/files/281338/icon-error.png?revision=1&size=bestfit&width=16&height=16) exclamation point icon appears next to a user's name in the Submittal Workflow table when they no longer have the permissions necessary to respond to the submittal.
   - **General Information** This section includes all of the pertinent information about the submittal. For field information, see [Add General Information](create-a-submittal.md#add-general-information "Create a Submittal").
   - **Submittal Schedule Information** This area details all of the important dates related to the submittal. For field information, see [Calculate Submittal Schedule Information (If Enabled)](create-a-submittal.md#calculate-submittal-schedule-info "Create a Submittal").
   - **Delivery Information** This area details the on-site delivery information. For field information, see [Update the Delivery Information](create-a-submittal.md#Update_the_Delivery_Information "Create a Submittal").
   - **Revision History**. If any revisions have been created, click the arrow next to **Revision History**. This reveals the *Revision Number*, *Title*, *Date* *Created*, and *Status*. You can also click the PDF icon to download a copy of any listed revision.
4. *Optional:* To generate a PDF summary of the submittal's information, see [Export a Submittal](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/export-a-submittal "Export a Submittal").

## Next Step

- [Export a Submittal](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/export-a-submittal "Export a Submittal")

## See Also

- [View a Submittal Package](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/view-a-submittal-package "View a Submittal Package")
- [Search and Filter Submittals](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/search-for-and-filter-submittals "Search and Filter Submittals")
- [View Submittal Attachments](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/view-submittal-attachments "View Submittal Attachments")

## 

If you would like to learn more about Procore's submittals management software and how it can help your business, please visit our [construction submittals software product page ![icon-external-link.png](https://support.procore.com/@api/deki/files/186764/icon-external-link.png?revision=2&size=bestfit&width=14&height=14)](https://www.procore.com/project-management/submittals "https://www.procore.com/project-management/submittals").