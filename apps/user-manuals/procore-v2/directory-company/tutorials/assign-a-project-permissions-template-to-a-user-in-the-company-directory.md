# Assign a Project Permissions Template to a User in the Company Directory

Source: https://v2.support.procore.com/product-manuals/directory-company/tutorials/assign-a-project-permissions-template-to-a-user-in-the-company-directory

---

## Background

Project permissions templates let you assign consistent access levels to multiple users at once. It is suggested to build these templates around specific job roles and collaborators.

Once created, you can apply these templates to users through the Company or Project Directory. This article focuses on assigning templates within the Company Directory.

## Things to Consider

- [Required User Permissions](/product-manuals/directory-company/permissions)
- Only global permissions templates can be selected as default permissions templates.
- You can only bulk update permissions for users on active projects.

## Prerequisites

- [Create a Project Permissions Template](/product-manuals/permissions-company/tutorials/create-a-project-permissions-template)

## Steps

- Change the User's Permission Templates for Current Projects
- Set the User's Default Permission Template for New Projects

### Change the User's Permission Templates for Current Projects

1. Navigate to the Company level **Directory** tool.
2. Navigate to the **Users** tab.
3. Click **Edit** next to the user you want to assign a permissions template to.
4. In the 'Current Project Settings' list, click the **Change Template** link.
5. In the **Template** drop-down list, select the template you want to assign to the user.
6. Review the tool permissions for the selected template. 
   *Notes:*

   - If you chose a [global permission template](/glossary-of-terms) from the 'Template' list, you can place a mark in the **Apply this template to all projects [User Name] belongs** **to** checkbox. The default setting for this checkbox is cleared.
   - If you choose a [project specific permission template](/glossary-of-terms) from the 'Template' list, this checkbox will not affect the user's other project template assignments.
7. Click **Apply**.

##### In Beta

This functionality can be [enabled in Procore Explore](/product-manuals/admin-company/tutorials/manage-features-with-procore-explore) by joining the beta for **Bulk Add a User to Projects from Company Directory**.

1. Navigate to the Company level **Directory** tool.
2. Click **Users**.
3. Click **View** next to the user you want to update.
4. Click the **Projects** tab.
5. Click the vertical ellipsis and select **Edit Permission Template on Assigned Projects**.
6. Select the **project permission template** to be applied to all currently assigned projects.
7. Select which projects to assign:

   - **Active Projects** the user is currently assigned to.
   - **Inactive Projects** the user is currently assigned to.
   - **All Projects** the user is currently assigned to.
8. Click **Save**.

### Set the User's Default Permission Template for New Projects

1. Navigate to the Company level **Directory** tool.
2. Navigate to the **Users** tab.
3. Click **Edit** next to the user you want to assign a permissions template to.
4. In the 'New Project Settings' area, click **Select Default Template**.
5. In the **Template** drop-down list, select the template you want to assign as the user's default permissions template when they are added to new projects.
6. Review the permissions preview for the selected template.
7. Click **Apply** to close the 'Select Default Permission Template' window.

##### In Beta

This functionality can be [enabled in Procore Explore](/product-manuals/admin-company/tutorials/manage-features-with-procore-explore) by joining the beta for Bulk Add a User to Projects from Company Directory.

1. Navigate to the Company level **Directory** tool.
2. Click **Users**.
3. Click **View** next to the user you want to update.
4. Click the **Projects** tab.
5. Click the vertical ellipsis and select **Edit Default Project Permission Template**.
6. Select the desired **permission template** from the drop-down menu.
7. Click **Save**.