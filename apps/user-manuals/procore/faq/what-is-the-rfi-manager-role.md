# What is the RFI Manager role? - Procore

Source: https://support.procore.com/faq/what-is-the-rfi-manager-role

---

##### **NOTE: This page is linked in the Procore web app**

**Locations**: [https://app.procore.com/webclients/h.../rfis/settings](https://app.procore.com/webclients/host/companies/11733/projects/1004955/tools/rfis/settings "https://app.procore.com/webclients/host/companies/11733/projects/1004955/tools/rfis/settings")

- RFIs > RFI Settings > Settings > RFI Manager > What is an RFI Manager?

## Answer

In Procore, an *RFI Manager* is the person responsible for overseeing an RFI throughout its lifecycle. This person is the gatekeeper between the RFI's Creator and the Design Team and is responsible for reviewing all Draft RFIs and either (1) providing a response to the RFIs and closing them out, or (2) opening the draft RFIs, assigning them a number, and then assigning them to the appropriate member of the design team, who then provides a response to the RFI's question.

### What is the RFI Manager's workflow?

Once the RFI manager reviews all the Draft RFIs that have been created and assigned in the RFIs tool, they can either:

- Respond to and close the RFI. See [How do I submit a response to a 'Draft' RFI when I am the RFI Manager?](https://support.procore.com/faq/how-do-i-submit-a-response-to-a-draft-rfi-when-i-am-the-rfi-manager "How do I submit a response to a 'Draft' RFI when I am the RFI Manager?")  
  OR
- Reassign it to one or more people to collect their responses.

When all of the responses are received, the RFI manager then chooses the 'Official Response'. At that point, the RFI can be closed (or, if a change event is needed, see [Create a Change Event](https://support.procore.com/products/online/user-guide/project-level/change-events/tutorials/create-a-change-event "Create a Change Event")). The responsible party can also be notified. Below shows you the typical workflow for an RFI manager.

[RFIs - Workflow Diagrams](#s14119)

### How to Configure the Default RFI Manager

Users with 'Admin' level permissions on the project's RFIs tool can choose one user to be the default RFI Manager for all RFIs on the project. See [Configure Advanced Settings: RFIs](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/configure-advanced-settings-rfis "Configure Advanced Settings: RFIs"). The default RFI manager can either be a user with 'Admin' level permissions on the project's RFIs tool or a user with 'Read Only' or 'Standard' level permissions on the project's RFIs tool with the ['Act as RFI Manager' granular permission](../products/online/user-guide/company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#RFIs "Grant Granular Permissions in a Project Permissions Template") enabled on their permission template. To learn more about what tasks the ['Act as RFI Manager' granular permission](../products/online/user-guide/company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#RFIs "Grant Granular Permissions in a Project Permissions Template") allows users to perform, see [What tasks does the 'Act as RFI Manager' granular permission allow users to perform?](#What_tasks_does_the_'Act_as_RFI_Manager'_granular_permission_allow_users_to_perform.3F "What is the RFI Manager role?") below.

### How to Change the Default RFI Manager Assignment

When an RFI is being created, the system will automatically select the designated default RFI Manager in the 'RFI Manager' field on all RFIs created after the default RFI Manager setting was configured. When an RFI is being created or edited, users with the appropriate permissions can change its 'RFI Manager' to a different user with 'Admin' level permissions on the project's RFIs tool or to a different user with 'Read Only' or 'Standard' level permissions on the project's RFIs tool with the ['Act as RFI Manager' granular permission](../products/online/user-guide/company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#RFIs "Grant Granular Permissions in a Project Permissions Template") enabled on their permission template. See [Create an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/create-an-rfi "Create an RFI") and [Edit an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/edit-an-rfi "Edit an RFI").

*Notes*:

- If you are a user with 'Standard' level permission on the RFIs tool, you can select a user with 'Read Only' or 'Standard' level permissions on the project's RFIs tool with the ['Act as RFI Manager' granular permission](../products/online/user-guide/company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#RFIs "Grant Granular Permissions in a Project Permissions Template") enabled on their permissions template or a user with 'Admin' level permission as the 'RFI Manager' when you create an RFI. You will not be permitted to change this assignment after the RFI is created unless you have the 'Act as RFI Manager' granular permission enabled on your own permissions template.
- If you are a user with 'Admin' level permission on the RFIs tool, you can select a user with 'Read Only' or 'Standard' level permissions on the project's RFIs tool with the ['Act as RFI Manager' granular permission](../products/online/user-guide/company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#RFIs "Grant Granular Permissions in a Project Permissions Template") enabled on their permissions template or a user with 'Admin' level permission as the 'RFI Manager' when you create an RFI. You can change this assignment after the RFI is created by editing the RFI. See [Edit an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/edit-an-rfi "Edit an RFI").

### What tasks does the 'Act as RFI Manager' granular permission allow users to perform?

Users with 'Read Only' or  'Standard' level permissions on the project's RFIs tool with the ['Act as RFI Manager' granular permission](../products/online/user-guide/company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#RFIs "Grant Granular Permissions in a Project Permissions Template") enabled on their permissions template can perform some additional tasks for RFIs they create ('Standard' only) or that they are designated as 'RFI Manager' for.

The table below lists the tasks 'Read Only' or 'Standard' level users with this granular permission can perform as an RFI's creator or its 'RFI Manager' and the tasks that only users with 'Admin' level permissions on the project's RFIs tool can perform.

| Task | With 'Act as RFI Manager' Granular Permission | | Granular Permission N/A |
| --- | --- | --- | --- |
| Read Only | Standard | Admin |
| [Add a Related Item to an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/add-a-related-item-to-an-rfi "Add a Related Item to an RFI") |  |  | icon-mindtouch-table-check.png |
| Add a Response to an RFI (Not as an Assignee) | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png |
| Add Assignees to an RFI (Not as an Assignee) | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png |
| Be Designated as a Project's Default RFI Manager | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png |
| [Choose an "Official Response" for an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/choose-an-official-response-for-an-rfi "Choose an \"Official Response\" for an RFI") | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png |
| [Close an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/close-an-rfi "Close an RFI")  icon-mindtouch-table-mobile.png | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png1 | icon-mindtouch-table-check.png |
| [Configure Settings: RFIs](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/configure-advanced-settings-rfis "Configure Advanced Settings: RFIs") |  |  | icon-mindtouch-table-check.png |
| Create an Open RFI |  | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png |
| [Delete a Response to an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/delete-a-response-to-an-rfi "https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/delete-a-response-to-an-rfi") |  |  | icon-mindtouch-table-check.png |
| [Delete an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/delete-an-rfi "Delete an RFI") |  |  | icon-mindtouch-table-check.png |
| [Designate the Default RFI Manager for a Project's RFIs](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/designate-the-default-rfi-manager-for-a-projects-rfis "Designate the Default RFI Manager for a Project's RFIs") |  |  | icon-mindtouch-table-check.png |
| [Edit an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/edit-an-rfi "Edit an RFI")  icon-mindtouch-table-mobile.png | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png |
| Export All Responses on an RFI | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png |
| **[Perform Bulk Actions on RFIs](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/perform-bulk-actions-on-rfis "Perform Bulk Actions on RFIs")** |  |  | icon-mindtouch-table-check.png |
| [Reopen an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/reopen-an-rfi "Reopen an RFI")  icon-mindtouch-table-mobile.png | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png |
| [Respond to an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/respond-to-an-rfi "Reply to an RFI")   icon-mindtouch-table-mobile.png | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png |
| [Retrieve an RFI from the Recycle Bin](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/retrieve-an-rfi-from-the-recycle-bin "Retrieve an RFI from the Recycle Bin") |  |  | icon-mindtouch-table-check.png |
| Select Any Available RFI Manager when Creating an RFI |  | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png |
| **[Shift the Ball in Court on a RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/shift-the-ball-in-court-on-an-rfi "Shift the Ball In Court on an RFI")** | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png |
| View All Responses on an RFI | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png |
| View Private RFIs | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png | icon-mindtouch-table-check.png |

*Note:* Other tasks can be performed with 'Read Only' or 'Standard' permission levels. Some of these other tasks may require different granular permissions to be enabled. See [RFI: Permissions](https://support.procore.com/products/online/user-guide/project-level/rfi/permissions "Permissions") and [Grant Granular Permissions in a Project Permissions Template](../products/online/user-guide/company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#RFIs "Grant Granular Permissions in a Project Permissions Template").

1 Users with 'Read Only' or 'Standard' level permissions on the project's RFIs tool with the ['Act as RFI Manager' granular permission](../products/online/user-guide/company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#RFIs "Grant Granular Permissions in a Permission Template") enabled on their permissions template can perform this task for RFIs that they create ('Standard' only) or that they are designated as RFI Manager for. For more information about what tasks users with this granular permission enabled on their permissions template can perform, see [What tasks does the RFI Manager granular permission allow users to perform?](#What_tasks_does_the_'Act_as_RFI_Manager'_granular_permission_allow_users_to_perform.3F "What is the RFI Manager role?")

## See Also

- [Configure Advanced Settings: RFIs](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/configure-advanced-settings-rfis "Configure Advanced Settings: RFIs")
- [Create an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/create-an-rfi "Create an RFI")

## 

If you would like to learn more about Procore's RFI software and how it can help your business, please visit our [request for information (RFI) construction software product page ![icon-external-link.png](https://support.procore.com/@api/deki/files/186764/icon-external-link.png?revision=2&size=bestfit&width=14&height=14)](https://www.procore.com/project-management/rfis "https://www.procore.com/project-management/rfis").