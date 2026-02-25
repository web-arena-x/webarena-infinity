# Assign a Project Permissions Template to a User in the Project Directory

Source: https://v2.support.procore.com/product-manuals/directory-project/tutorials/assign-a-project-permissions-template-to-a-user-in-the-project-directory

---

##### Â In Beta

A redesigned version of the Project Directory is currently in beta and can be enabled with [Procore Explore](/product-manuals/admin-company/tutorials/manage-features-with-procore-explore).

## Background

In Procore, Role-Based Permissions are used to manage user access to different Procore tools. Access for each role is defined in a permission template. By default, Procore provides customers with several [default role-based project permissions templates](/faq-what-are-the-default-project-permissions-templates-in-procore).

Users can be assigned a that is created in the company's Permissions tool, or a that is created in the company's Permissions tool or the Project level Directory tool.

## Things to Consider

- [Required User Permissions](/product-manuals/directory-project/permissions)
- Procore recommends selecting either a 

 In Procore, a *Global Permissions Template* is a project permissions template that can be assigned to any user on any project in your company's Procore account. See also *permission template* and *project-specific permission template*.

 Global Permissions Template or 

 In Procore, a *Project Specific Permissions Template* can only be assigned to a user who has been added to the corresponding project's Directory tool. See also *Permissions Template* and *Global Permissions Template*.

 Project Specific Permissions Template.

## Prerequisites

- [Create a Project Permissions Template](/product-manuals/permissions-company/tutorials/create-a-project-permissions-template) 
 OR
- [Create a Project Specific Permissions Template from the Project Directory](/product-manuals/directory-project/tutorials/create-a-project-specific-permissions-template-from-the-project-directory)

## Steps

1. Navigate to the Project level **Directory** tool.
2. Next to the user, click **Edit**. 
   OR Click the **user's name.**
3. Locate and click the **Project Permissions Templates** drop-down menu and select one of the following options:

   - **Do Not Apply a Template:** Select this option if you do NOT want to apply a permissions template and instead want to define unique permissions for the user.1. In the table below, select each permission level you want to provide the user for each tool.
   - **Global Permissions Template:** Select this option to provide the user with access to the project as defined in one of your company's global permissions templates.1. Under the 'Global Permissions Templates' section, select a permissions template.
   - **Project Specific Permissions Template:** To provide the user with project specific permissions for the project.1. Under the 'Project Specific Templates' header, select a permissions template.
4. Save in one of the following ways:

   - Click **Save** to save the changes without sending an email to the user.
   - Click **Save & Send Notification** to save and remind users that have previously logged in to Procore, that they have been invited to join your Procore project.
   - Click **Save and Send Invite to Procore** to save and invite a new user that has not yet logged into Procore.