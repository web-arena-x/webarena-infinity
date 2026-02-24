# Configure Settings: Document Management

Source: https://v2.support.procore.com/product-manuals/document-management-project/tutorials/configure-settings-document-management

---

##### Regional availability

The Document Management tool is available in select countries. It is not yet available for Procore accounts in the U.S. To learn more, please reach out to your Procore point of contact.

## Background

Important settings for the Document Management tool are managed on the Configure Settings page, such as: creating and managing permission groups, customizing permission settings for documents, and standardizing fields for document metadata.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions to the project's Document Management tool.

## Steps

##### Â Note

Settings for the **Document Management** tool can also be managed in the project's Admin tool. See [Configure Document Management Settings in the Admin Tool](/product-manuals/admin-project/tutorials/configure-document-management-settings-in-the-admin-tool-beta).

1. Navigate to the project's **Document Management** tool.
2. Click the **Configure Settings** icon.
3. Click the tab of the tool area you want to view or modify. See additional directions for each area below:

       
   - **Views Tab**

     - Collections
   - **Permissions Tab**

     - Permission Group
     - Document Permissions
     - Workflow Permissions
   - **Documents Tab**

     - Upload Requirements
     - Naming Standards
     - Document Fields
   - **Workflows Tab**

     - Document Workflows
   - **Notifications**

     - Document Upload
     - Document Submission

#### Views Tab

Click the **Views** tab to create Collections for the project. Collections help filter and organize documents so users can quickly find the revisions they need. See the following articles related to Collections:

- [Create and Edit Collections](/product-manuals/document-management-project/tutorials/create-and-edit-collections)
- [What is a Collection in the Document Management tool?](/faq-what-is-a-collection-in-the-document-management-tool)

#### Permissions Tab

Click the **Permissions** tab to access the following settings:

#### Permission Groups

In the **Permission Groups** section, you can create and manage permission groups to control access to documents in the project. See the following tutorials related to permission groups:

- [Create a Permission Group](/product-manuals/document-management-project/tutorials/create-a-permission-group-for-the-document-management-tool)
- [Edit a Permission Group](/product-manuals/document-management-project/tutorials/edit-a-permission-group-for-the-document-management-tool)
- [Duplicate a Permission Group](/product-manuals/document-management-project/tutorials/duplicate-a-permission-group-for-the-document-management-tool)
- [Delete a Permission Group](/product-manuals/document-management-project/tutorials/delete-a-permission-group-in-the-document-management-tool)
- [View Permission Groups](/product-manuals/document-management-project/tutorials/view-permission-groups-for-the-document-management-tool)

#### Document Permissions

In the **Document Permissions** section, you can customize the actions that people and groups can perform on documents. See [View and Manage Settings for Document Permissions.](/product-manuals/document-management-project/tutorials/view-and-manage-document-permissions-for-the-document-management-tool)

#### Workflow Permissions

Permissions selected in this section are specific to documents in a workflow. Any permissions set here will override normal permissions set from the Document Permissions above. See [View and Manage Workflow Permissions in the Document Management Tool](/product-manuals/document-management-project/tutorials/view-and-manage-workflow-permissions-in-the-document-management-tool).

#### Documents Tab

Click the **Documents** tab to access the following settings:

##### Upload Requirements

In the **Upload Requirements** section, you can select naming standards and required fields for document uploads. See [Edit the Upload Requirements for Documents](/product-manuals/document-management-project/tutorials/edit-upload-requirements-for-the-document-management-tool).

##### Naming Standards

In the **Naming Standards** section, you can build naming standards that automatically apply to uploaded documents. See [Edit the Naming Standard for Documents.](/product-manuals/document-management-project/tutorials/edit-the-naming-standard-for-the-document-management-tool)

##### Document Fields

In the **Document Fields** section, you can view document metadata fields, mark certain fields as inactive or active, and edit field option descriptions.

To edit the description of a field *option,* follow these steps from within the 'Document Fields' section: 
*Note:* Changes made here only apply to the current project.

1. Click the name of a field that gives users options via a drop-down menu, such as 'Status' or 'Discipline'.
2. Click the **Edit Field** button.
3. Find the option you want to edit and click on its text in the 'Description' column to change it.
4. Click the **Save** button.   
   *Note:* Your changes only affect the current project.

For field changes at the company level, see [Manage Custom and Default Fields and Fieldsets for the Document Management Tool](/product-manuals/document-management-project/tutorials/manage-custom-and-default-fields-and-fieldsets-for-the-document-management-tool).

#### Workflows Tab

Click the **Workflows** tab to access the following settings:*Note:* You will only see the Workflows tab if your organization is using the [Workflows tool](/product-manuals/workflows-company/) in Procore.

##### Document Workflows

If one or more workflows have been assigned to the project, you can view and configure workflows in this section.

###### Bulk Edit Workflow Assignees

To edit a workflow template's Assignees or Workflow Manager, follow these steps:

1. Find the template you want to modify and click the people icon in the 'Roles' column.
2. Select whether you want your changes to apply to the workflow template and workflows in progress *or* just the workflow template for documents that use the template in the future. 
   *Note:* If you choose to include in-progress workflows, once you click 'Save' those workflows reflect your changes and any removed Assignees cannot respond to current or upcoming workflow steps. However, any responses already made in previous steps are preserved.
3. Modify the assignees as needed. Click in the field to add a new name, or click the x next to a name to remove it.
4. Click **Save.**

Project Admin can change additional workflow functionality:

- If certain types of document errors arise, [resolve them](/faq-how-do-i-resolve-document-errors-in-the-document-management_tool) in the 'Action Required' saved view.
- [Restrict workflow template access](/product-manuals/document-management-project/tutorials/edit-a-permission-group-for-the-document-management-tool) for different teams. This reduces the chance of a team accidentally choosing a template that doesn't fit their needs.
- For more workflow template configuration options, see [About Workflows in the Document Management Tool](/product-manuals/document-management-project/tutorials/about-workflows-in-the-document-management-tool) or [Configure a Custom Workflow Template on a Project](/product-manuals/workflows-company/tutorials/configure-workflow-templates-on-projects).

#### Notifications

In the **Notifications** tab, select which users you want notified when a document is uploaded or submitted in the Document Management tool. View detailed instructions below, or see [Workflow](https://support.procore.com/products/online/user-guide/project-level/document-management/tutorials/configure-settings-document-management#Workflows_Tab) if you're curious about notifications that alert users to their turn in a document approval process.

##### Document Upload

Notify selected companies, distribution groups, or individual users when a new document is uploaded to the Document Management tool. The notification is an email with links to all relevant saved views and a .csv file listing all the updated documents.

1. Click the **+ Add Recipients** button in the 'Recipients' column. 
   *Note:* If you're adding or modifying an existing recipients list, this is a link instead of a button.
2. Click in the **Companies**, **Distribution Groups**, or **Users** field to select or search for the group or user you want to add.
3. Click **Update.**
4. Make sure the 'Active' toggle is set to your preference of **on** or **off**.   
    *Note:* The number listed in the Recipients column may be lower than expected because Procore only counts each user once. For example, if you add a new group of 3 users, but two of them were already in a different group that already gets notified in this same way, the total recipient count only increases by 1.

##### Document Submission

Notify selected users or distribution groups when a new document that matches the filter criteria of a saved view is submitted to the Document Management tool. The notification is an email with links to all relevant documents and a .csv file listing them.

1. Click the **+ Add Recipients** button in the 'Recipients' column of the saved view you want to align notifications with. 
   *Note:* If you're adding or modifying an existing recipients list, this is a link instead of a button.
2. Click in the **Companies**, **Distribution Groups**, or **Users** field to select or search for the group or user you want notified when a new document is submitted into this saved view.
3. Click **Update.**

   *Note:* The number listed in the Recipients column may be lower than expected because Procore only counts each user once. For example, if you add a new group of 3 users, but two of them were already in a different group that already gets notified in this same way, the total recipient count only increases by 1.