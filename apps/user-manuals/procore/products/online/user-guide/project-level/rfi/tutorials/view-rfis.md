# View RFIs - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/view-rfis

---

## Objective

To view an RFI using the project's RFI tool.

## Things to Consider

- **Required User Permissions:**
 - *To view RFIs not marked as 'Private':*
    - 'Read Only' level permissions or higher on the project's RFIs tool
 - *To view all RFIs:*
    - 'Admin' level permissions on the project's RFIs tool

##### Tip

Users may require specific roles on an RFI (or granular permissions) to view the RFI depending on the RFI's status and privacy settings.

**What user roles can view which types of RFIs?** **Show/Hide**

In the table below, the ![icon-mindtouch-table-check.png](https://support.procore.com/@api/deki/files/91423/icon-mindtouch-table-check.png?revision=3&size=bestfit&width=18&height=18) icon indicates which user roles can view an RFI based on its status and privacy settings, and the ![icon-delete-x.png](https://support.procore.com/@api/deki/files/90870/icon-delete-x.png?revision=1&size=bestfit&width=18&height=18) icon indicates which user roles cannot view an RFI based on its status and privacy settings.

| User Role | RFI Type | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| Draft RFI | Draft 'Private' RFI | Open RFI | Open 'Private' RFI | Closed RFI | Closed 'Private' RFI |
| Creator | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png |
| RFI Manager | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png |
| Assignee | icon-delete-x.png | icon-mindtouch-table-check.png 1 | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png 2 | icon-mindtouch-table-check.png 3 |
| Distribution List Member | icon-delete-x.png | icon-mindtouch-table-check.png 1 | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png 2 | icon-mindtouch-table-check.png 3 |
| No Role | icon-delete-x.png | icon-mindtouch-table-check.png 1 | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png 1 | icon-mindtouch-table-check.png 2 | icon-mindtouch-table-check.png 1 |
| Tool Admin | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png |

1 Users with the ['View Private RFIs Associated to Users within Same Company' granular permission](../../../company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#RFIs "Grant Granular Permissions in a Project Permissions Template") enabled on their permissions template can view any RFI marked 'Private' if another user in their company (including them) is the RFI's creator or is designated as the RFI Manager, an Assignee, or a Distribution List member.

2 Assignees, Distribution List Members, and users without a role on the RFI can only view a closed RFI not marked 'Private' if the RFI was previously open.

3 Assignees, Distribution List Members, and users without a role on the RFI can only view a closed RFI marked 'Private' if the RFI was previously open OR if they have the ['View Private RFIs Associated to Users within Same Company' granular permission](../../../company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#RFIs "Grant Granular Permissions in a Project Permissions Template") enabled on their permissions template and another user in their company (including them) is the RFI's creator or is designated as the RFI Manager, an Assignee, or a Distribution List member.

- **Additional Information:**
 - The 'Only Show Official Responses to Standard and Read-Only Users' configuration setting must be turned OFF in order for a user with 'Standard' level permissions on the project's RFIs tool to view all responses to an RFI that they created. See [Configure Advanced Settings: RFIs](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/configure-advanced-settings-rfis "Configure Advanced Settings: RFIs").
 - Users with the ['Act as RFI Manager' granular permission](../../../company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#RFIs "Grant Granular Permissions in a Project Permissions Template") enabled on their permissions templates can view all responses to RFIs that they create ('Standard' only) or that they are designated as RFI Manager for even if the 'Only Show Official Responses to Standard and Read-Only Users' configuration setting is turned ON.
 - Some image attachments may include the option to view them in a map view based on the files' GPS coordinates. See [Which Procore tools let me view digital image attachments in a map view?](https://support.procore.com/faq/which-procore-tools-let-me-view-a-digital-image-attachment-in-a-map-view "Which Procore tools let me view a digital image attachments in a map view?")

## Steps

1. Navigate to the project's **RFIs** tool.
2. Click the **Items** tab.
3. Click **View** next to the RFI you want to view. 
     
   ![view-rfi.png](https://support.procore.com/@api/deki/files/73646/view-rfi.png?revision=2) 
     
   OR Click the link in the 'Subject' column for the RFI you want to view.

The RFIs page contains the following tabs:

- [General](#General "View RFIs")
- [Related Items](#Related_Items "View RFIs")
- [Emails](#Emails "View RFIs")
- [Change History](#Change_History "View RFIs")

### General

The **General** tab shows the RFI's **Request, Responses, and** **General Information**cards.

### Related Items

The **Related Items** tab lets you view or add related items and notes to the RFI. If the related item is stored in Procore (e.g., submittal, bid package, etc.) you will be able to view it and all its information by clicking the hyperlink 'Description' column. If you want to add a new related item, see [Add a Related Item to an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/add-a-related-item-to-an-rfi "Add a Related Item to an RFI").

### Emails

The **Emails** tab is where you can view or export existing emails forwarded from the RFI in Procore (see [Forward an RFI by Email](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/forward-an-rfi-by-email "Forward an RFI by Email")) or sent to the RFI from outside of Procore using the RFI's unique email address.

### Change History

The **Change History** tab is only visible to users with 'Admin' level permissions on the project's RFIs tool. This tab includes a summary of all of the changes made to the RFI throughout its lifecycle.

## See Also

- [Create an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/create-an-rfi "Create an RFI")
- [Edit an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/edit-an-rfi "Edit an RFI")
- [Export an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/export-an-rfi "Export an RFI")
- [Respond to an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/respond-to-an-rfi "Reply to an RFI")
- [Close an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/close-an-rfi "Close an RFI")

## 

If you would like to learn more about Procore's RFI software and how it can help your business, please visit our [request for information (RFI) construction software product page ![icon-external-link.png](https://support.procore.com/@api/deki/files/186764/icon-external-link.png?revision=2&size=bestfit&width=14&height=14)](https://www.procore.com/project-management/rfis "https://www.procore.com/project-management/rfis").