# Configure Assignment and Request Statuses for Resource Planning

Source: https://v2.support.procore.com/product-manuals/resource-planning-company/tutorials/configure-assignment-and-request-statuses-for-resource-planning

---

## Background

Resource Planning allows you to receive resource requests and make resource assignments, to manage your resources. You can create assignment and request statuses to help you organize and manage the requests you are receiving and assignments you are making.

Visibility of assignments with certain statuses is controlled by what status(es) the user has access to within their permission level. This means that resource managers can create assignments at different stages (for example, pending, forecasted, live) without giving unwanted access to that information.

## Things to Consider

- [Required User](/product-manuals/resource-planning-company/permissions) [Permissions](/product-manuals/resource-planning-company/permissions)
- You can manage user visibility of assignments and requests based on their statuses using permissions templates. See [Create Permissions Templates for Resource Planning](/product-manuals/resource-planning-company/tutorials/create-permissions-templates-for-resource-planning).
- If a user has permission to view only to certain statuses, the status field is required when creating requests or assignments.
- Statuses are visible on Assignments Boards, Assignments Gantt, the Assignment List and Request List.

## Prerequisites

- User visibility of assignment and requests is managed in Resource Planning Permissions. A user can only be assigned one set of permissions in Resource Planning. It is recommended that you configure user permissions in advance. See [Create Permissions Templates for Resource Planning](/product-manuals/resource-planning-company/tutorials/create-permissions-templates-for-resource-planning).

## Steps

### Status Name and Color

1. Navigate to the Company level **Resource Planning** tool.
2. Click the **Configure Settings**  icon.
3. Select **Assignment/Request Statuses**.
4. Click **New**.
5. Configure the status with the following properties:

   1. **Name**. Enter the name of the status.
   2. **Abbreviation (5 Characters)**. Enter the abbreviation for the status, limited to five characters.
   3. **Color**. Enter the color of the Status.
6. Click **Save**.

### Status Visibility

1. Navigate to the Company level **Resource Planning** tool.
2. Click the **Configure Settings**  icon.
3. Select **Permissions**.
4. Locate the Permission level you want to update, and click **Edit**. See [Edit Permissions Templates for Resource Planning](/product-manuals/resource-planning-company/tutorials/edit-permissions-templates-for-resource-planning).  
   OR  
   Click **New** to create a new Permission template. [Create Permissions Templates for Resource Planning](/product-manuals/resource-planning-company/tutorials/create-permissions-templates-for-resource-planning).
5. Locate the 'Statuses' section.
6. Mark the checkbox **Can View All Statuses** to allow users with this permission level to view all statuses.  
   OR  
   Clear the checkbox **Can View All Statuses.** Next, select from the dropdown list which assignment and request statuses should be visible for users with that permission level.
7. Click **Save**.