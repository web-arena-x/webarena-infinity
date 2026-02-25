# Edit a Permission Group for the Document Management Tool

Source: https://v2.support.procore.com/product-manuals/document-management-project/tutorials/edit-a-permission-group-for-the-document-management-tool

---

##### Regional availability

The Document Management tool is available in select countries. It is not yet available for Procore accounts in the U.S. To learn more, please reach out to your Procore point of contact.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions to the project's Document Management tool.

## Steps

1. Navigate to the project's **Document Management** tool.
2. Click the **Configure Settings** icon.
3. In the 'Permission Groups' section of the **Permissions** tab, locate the permission group that you want to edit.
4. Click the **edit** icon for the permission group.
5. See the sections below for available actions:

   - Add or Remove People
   - Edit Permission Group Settings

### Add or Remove People

1. In the Edit Permission Group panel, click the **People** tab.
2. Click **Edit People**.
3. Add or remove people as necessary:

   - To add a person to the group, mark the checkbox next to each user you want to add to the permission group.
   - To remove a person from the group, click the **delete** icon. 
     ***Important!*** Removing a person from the group will impact their document permissions for the project.
4. When you are done making changes to the permission group, click **Submit**.

### Edit Permission Group Settings

1. In the 'Edit Permission Group' panel, click the **Permissions** tab.
2. See the sections below for more information on making changes to the permission group settings.

#### Edit Upload and Submit Permissions

1. In the 'Upload Permissions' section, mark or clear the checkbox to determine whether this group should have permission to upload and submit files to the tool:

   - **Upload New Files**: Allows users to upload files to the tool and complete information. See [Upload Documents](/product-manuals/document-management-project/tutorials/upload-documents-to-the-document-management-tool) and [Complete Information for Documents](/product-manuals/document-management-project/tutorials/complete-information-for-documents-in-the-document-management-tool). 
     *Note:* If the 'Upload New Files' permission is disabled, the 'Submit New Files' permission is automatically disabled.
   - **Submit New Files**: Allows users to submit completed documents to the project. See [Submit Documents](/product-manuals/document-management-project/tutorials/submit-documents-in-the-document-management-tool).
2. If you are done making changes, click **Save**.

#### Edit the Permission Type

1. In the 'Document Permissions' section, click **Grant Permissions**.
2. Under 'Select Permission Type', choose **Admin**, **Owner**, or **Viewer**.
3. Click **Submit**.
4. If you are done making changes, click **Save**.

#### Edit Document Permissions

1. In the 'Document Permissions' section, click **Grant Permissions** to add new permissions or click the **edit** icon next to any existing document permissions to modify them.
2. Under 'Select Documents', choose one of the following to give the group permissions to:

   - **All Documents**
   - **Only Documents with Selected Attributes**.

     1. Click the **Add Attribute Set** button.
     2. Click **Select Attributes** to choose one attribute (field) that is relevant for controlling access for this group. 
        *Note:* You can select a custom field (attribute) if it's one of the following field types: company, location, or single select (dropdown).
     3. Click the '**includes any of**' menu to select one or more values for the attribute selected above. 
        *Note:* If *any* of your selected values apply to a document, the document will show in each group members' Document Management tool. A document does not need *all* the selected values in order to be available to a group member.
     4. If you want to add additional attribute sets, repeat these steps.
3. Click **Submit**.
4. If you are done making changes to the permission group, click **Save**.

#### Edit Workflow template access permissions

1. In the 'Workflow template access permissions' section, click to choose one of these options for the user group you are currently editing:

   - **Auto Apply All Configured Templates**: Gives access to select any workflow templates created for the project when assigning a workflow template to a document.
   - **Custom Selection**: Limits the workflow template(s) that user group can choose from. This reduces the chance of a team accidentally choosing a template that doesn't fit their needs.

     - Click to select which templates the user group can access.
2. Click **Save**.

#### Edit Attributes for Document Access

*Note:* This is only applicable if 'Only Documents with Selected Attributes' is selected for the permission group:

1. Under 'Document Permissions', click the **edit** icon.
2. Add or remove attributes as necessary.   
   *Note:* You can select a custom field (attribute) if it's one of the following field types: company, location, or single select (dropdown).
3. Click **Submit**.
4. If you are done making changes, click **Save**.