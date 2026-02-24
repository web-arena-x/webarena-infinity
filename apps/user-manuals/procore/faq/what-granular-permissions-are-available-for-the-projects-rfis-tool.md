# What granular permissions are available for the project's RFIs tool? - Procore

Source: https://support.procore.com/faq/what-granular-permissions-are-available-for-the-projects-rfis-tool

---

## Background

In Procore, the term granular permissions refers to task-based privileges that can be granted to users with 'Read Only' or 'Standard' level permissions on certain tools through the users' assigned [permissions templates](../references/construction-management/glossary-of-terms.md#Permission_Template "Glossary of Terms"). The table below shows the granular permissions that are available for the project's RFIs tool.

## Answer

| Granular Permission Name | Granular Permission Description |
| --- | --- |
| Act as RFI Manager | Grants a user the privilege to be selected as the RFI Manager for individual RFIs or to be selected as a project's default RFI Manager. For more information about what tasks users with this granular permission enabled on their permissions template can perform, see [What tasks does the 'Act as RFI Manager' granular permission allow users to perform?](what-is-the-rfi-manager-role.md#What_tasks_does_the_'Act_as_RFI_Manager'_granular_permission_allow_users_to_perform.3F "What is the RFI Manager role?") |
| Mark Official Responses 1 | Grants a user the privilege to mark (or unmark) official responses on an RFI if they are the RFI's creator or if they are an Assignee or a Distribution List member on the RFI. |
| View Private RFIs Associated to Users within Same Company | Grants a user the privilege to view any RFI marked 'Private' if another user in their company (including them) is the RFI's creator or is designated as the RFI Manager, an Assignee, or a Distribution List member. |
| View External Items | Grants a user with 'Read Only' or 'Standard' permissions the privilege to view any External RFI. |

1. The 'Only Show Official Responses to Standard and Read-Only Users' configuration setting must be turned OFF in order for a user with 'Standard' level permissions on the project's RFIs tool to view all responses to an RFI that they created. See [Configure Advanced Settings: RFIs](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/configure-advanced-settings-rfis "Configure Advanced Settings: RFIs"). Users with the ['Act as RFI Manager' granular permission](../products/online/user-guide/company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#RFIs "Grant Granular Permissions in a Permission Template") enabled on their permissions templates can view all responses to RFIs that they create ('Standard' only) or that they are designated as RFI Manager for even if this setting is turned ON.

## See Also

- [RFIs: Permissions](https://support.procore.com/products/online/user-guide/project-level/rfi/permissions "Permissions")
- [Grant Granular Permissions in a Project Permissions Template](https://support.procore.com/products/online/user-guide/company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template "Grant Granular Permissions in a Project Permissions Template")