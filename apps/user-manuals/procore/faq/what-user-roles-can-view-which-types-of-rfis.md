# What user roles can view which types of RFIs? - Procore

Source: https://support.procore.com/faq/what-user-roles-can-view-which-types-of-rfis

---

## Background

Users may require specific roles on an RFI (or granular permissions) to view the RFI depending on the RFI's status and privacy settings.

## Answer

Users may require specific roles on an RFI (or granular permissions) to view the RFI depending on the RFI's status and privacy settings.

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

1 Users with the ['View Private RFIs Associated to Users within Same Company' granular permission](../products/online/user-guide/company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#RFIs "Grant Granular Permissions in a Project Permissions Template") enabled on their permissions template can view any RFI marked 'Private' if another user in their company (including them) is the RFI's creator or is designated as the RFI Manager, an Assignee, or a Distribution List member.

2 Assignees, Distribution List Members, and users without a role on the RFI can only view a closed RFI not marked 'Private' if the RFI was previously open.

3 Assignees, Distribution List Members, and users without a role on the RFI can only view a closed RFI marked 'Private' if the RFI was previously open OR if they have the ['View Private RFIs Associated to Users within Same Company' granular permission](../products/online/user-guide/company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#RFIs "Grant Granular Permissions in a Project Permissions Template") enabled on their permissions template and another user in their company (including them) is the RFI's creator or is designated as the RFI Manager, an Assignee, or a Distribution List members.

## See Also

- What is the RFI Manager role?
- [What is a 'Draft' RFI?](what-is-a-draft-rfi.md)