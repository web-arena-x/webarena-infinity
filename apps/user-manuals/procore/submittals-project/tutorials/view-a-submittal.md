# View a Submittal

Source: https://v2.support.procore.com/product-manuals/submittals-project/tutorials/view-a-submittal

---

## Things to Consider

##### Â Tip

Users may require specific roles on a submittal (or granular permissions) to view the submittal depending on its privacy settings.

**What user roles can view which types of submittals?** **Show/Hide**

In the table below, the  icon indicates which user roles can view a submittal based on its status and privacy settings, and the  icon indicates which user roles cannot view a submittal based on its status and privacy settings.

|  |  |  |
| --- | --- | --- |
| User Role | Submittal Type |  |
| Public Submittal | Private Submittal |  |
| Creator |  |  |
| Submittal Manager |  |  |
| Workflow Member |  |  |
| Distribution List Member |  |  |
| No Role |  | 1 |
| Tool Admin |  |  |

1 Users with the ['View Private Submittals Associated to Users within Same Company' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on their permissions template can view any submittal marked 'Private' if another user in their company (including them) is the submittal's creator or is designated as the Submittal Manager, a workflow member, or a Distribution List member.

- **Required User Permissions:**

  - *To view a submittal not marked 'Private':* 'Read Only' level permissions or higher on the project's Submittals tool.
- **Additional Information:**

  - A 'Private' submittal is visible to the following users:\* The submittal's creator, Submittal Manager, Submittal Workflow members, and Distribution List members\* Users with 'Admin' level permissions on the project's Submittals tool\* Users with 'Read Only' or 'Standard' level permissions on the project's Submittals tool with the ['View Private Submittals Associated to Users within Same Company' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on their permissions template (if another user in their company [including them] is the submittal's creator or is designated as the Submittal Manager, a Submittal Workflow member, or a Distribution List member)

## Steps

1. Navigate to the project's **Submittals** tool.
2. Click **View** next to the submittal you want to view.
3. View the following information:

   - **Submittal Workflow**  
      This section includes attachments added to the submittal's 'General Information' when the submittal was created or edited. This section also details the submitters and approvers on the submittal. It also shows their official response, comments, and attachments that may have been added with their response. See [Add Users to the Submittal Workflow](/product-manuals/submittals-project/tutorials/create-a-submittal).

     ##### Â Note

     The  exclamation point icon appears next to a user's name in the Submittal Workflow table when they no longer have the permissions necessary to respond to the submittal.

- **General Information**  
   This section includes all of the pertinent information about the submittal. For field information, see [Add General Information](/product-manuals/submittals-project/tutorials/create-a-submittal).
- **Submittal Schedule Information**  
   This area details all of the important dates related to the submittal. For field information, see [Calculate Submittal Schedule Information (If Enabled)](/product-manuals/submittals-project/tutorials/create-a-submittal).
- **Delivery Information**  
   This area details the on-site delivery information. For field information, see [Update the Delivery Information](/product-manuals/submittals-project/tutorials/create-a-submittal).
- **Revision History**. If any revisions have been created, click the arrow next to **Revision History**. This reveals the *Revision Number*, *Title*, *Date* *Created*, and *Status*. You can also click the PDF icon to download a copy of any listed revision.
- *Optional:* To generate a PDF summary of the submittal's information, see [Export a Submittal](/product-manuals/submittals-project/tutorials/export-a-submittal).