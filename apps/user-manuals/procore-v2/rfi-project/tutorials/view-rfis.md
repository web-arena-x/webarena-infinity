# View RFIs

Source: https://v2.support.procore.com/product-manuals/rfi-project/tutorials/view-rfis

---

## Things to Consider

- [Required User Permissions](/product-manuals/rfi-project/permissions)

  ##### Â Tip

  Users may require specific roles on an RFI (or granular permissions) to view the RFI depending on the RFI's status and privacy settings.

  **What user roles can view which types of RFIs?** **Show/Hide**

  In the table below, the  icon indicates which user roles can view an RFI based on its status and privacy settings, and the  icon indicates which user roles cannot view an RFI based on its status and privacy settings.

  |  |  |  |  |  |  |  |
  | --- | --- | --- | --- | --- | --- | --- |
  | User Role | RFI Type |  |  |  |  |  |
  | Draft RFI | Draft 'Private' RFI | Open RFI | Open 'Private' RFI | Closed RFI | Closed 'Private' RFI |  |
  | Creator |  |  |  |  |  |  |
  | RFI Manager |  |  |  |  |  |  |
  | Assignee |  | 1 |  |  | 2 | 3 |
  | Distribution List Member |  | 1 |  |  | 2 | 3 |
  | No Role |  | 1 |  | 1 | 2 | 1 |
  | Tool Admin |  |  |  |  |  |  |

  1 Users with the ['View Private RFIs Associated to Users within Same Company' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on their permissions template can view any RFI marked 'Private' if another user in their company (including them) is the RFI's creator or is designated as the RFI Manager, an Assignee, or a Distribution List member.

  2 Assignees, Distribution List Members, and users without a role on the RFI can only view a closed RFI not marked 'Private' if the RFI was previously open.

  3 Assignees, Distribution List Members, and users without a role on the RFI can only view a closed RFI marked 'Private' if the RFI was previously open OR if they have the ['View Private RFIs Associated to Users within Same Company' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on their permissions template and another user in their company (including them) is the RFI's creator or is designated as the RFI Manager, an Assignee, or a Distribution List member.

- **Additional Information:**

  - The 'Only Show Official Responses to Standard and Read-Only Users' configuration setting must be turned OFF in order for a user with 'Standard' level permissions on the project's RFIs tool to view all responses to an RFI that they created. See [Configure Advanced Settings: RFIs](/product-manuals/rfi-project/tutorials/configure-advanced-settings-rfis).
  - Users with the ['Act as RFI Manager' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on their permissions templates can view all responses to RFIs that they create ('Standard' only) or that they are designated as RFI Manager for even if the 'Only Show Official Responses to Standard and Read-Only Users' configuration setting is turned ON.
  - Some image attachments may include the option to view them in a map view based on the files' GPS coordinates. See [Which Procore tools let me view digital image attachments in a map view?](/faq-which-procore-tools-let-me-view-a-digital-image-attachment-in-a-map-view)

## Steps

1. Navigate to the project's **RFIs** tool.
2. Click the **Items** tab.
3. Click **View** next to the RFI you want to view.