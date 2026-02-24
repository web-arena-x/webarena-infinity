# Manage Configurable Fieldsets and Default Fields for the Document Management Tool

Source: https://v2.support.procore.com/product-manuals/document-management-project/tutorials/manage-configurable-fieldsets-and-default-fields-for-the-document-management-tool

---

##### Regional availability

The Document Management tool is available in select countries. It is not yet available for Procore accounts in the U.S. To learn more, please reach out to your Procore point of contact.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permission to the Company level Admin tool. 
    *Note:* Users with 'Admin' level permissions to Document Management tool can show or hide default field options for a specific project on the Configure Settings page. See [Configure Settings: Document Management](/product-manuals/document-management-project/tutorials/configure-settings-document-management).
- **Additional Information**:

 - Default fields required by Procore can't be turned off or removed. See [Why can't I turn off certain document 'Types' for the Document Management tool?](/faq-why-cant-i-turn-off-certain-document-types-for-the-document-management-tool)

## Steps

Fields for the Document Management tool can be managed at the Company and Project level. See the following options:

- Configure Custom Fields, Fieldsets, and Default Fields for Projects

 - [Create Custom Fields](#configure-custom-fields-fieldsets-and-default-fields-for-projects)
 - [Create Configurable Fieldsets](#null)
 - [Edit Default Fields](#null)
- [Show or Hide Option for a Field](#show-or-hide-options-for-a-field)

## Configure Custom Fields, Fieldsets, and Default Fields for Projects

#### Create Custom fields

1. Navigate to the Company level **Admin** tool.
2. On the sidebar, scroll down to 'Tool Settings' and click **Document Management**.
3. Click the **Custom Fields** tab.
4. Click **Create Custom Field**.
5. Enter a name and select a field type for your custom field.
6. Click **Create.**
7. Your new custom field is now available for use in the following scenarios:

   - Fieldsets
   - [Naming standard](/product-manuals/document-management-project/tutorials/edit-the-naming-standard-for-the-document-management-tool) - Consider adding a custom field to the naming standard if it's one of the following field types: company, location, number, plain text (short), or single select (dropdown)
   - [Document upload requirements](/product-manuals/document-management-project/tutorials/edit-upload-requirements-for-the-document-management-tool)
   - [Permission groups](/product-manuals/document-management-project/tutorials/edit-a-permission-group-for-the-document-management-tool) - Consider adding a custom field to the permission standards if it's one of the following field types: company, location, or single select (dropdown).
   - [Column](/product-manuals/document-management-project/tutorials/configure-your-view-in-the-document-mangement-tool) in the Document Management tool's search results
   - [Filter](/product-manuals/document-management-project/tutorials/search-for-and-filter-documents-in-the-document-management-tool) for the Document Management tool's search results, including when [exporting](/product-manuals/document-management-project/tutorials/export-information-from-the-document-management-tool) column data.

#### Create New Configurable Fieldset

1. Navigate to the Company level **Admin** tool.
2. On the sidebar, scroll down to 'Tool Settings' and click **Document Management**.
3. The **Fieldsets** tab opens automatically.
4. Click **Create New**.
5. Enter a name for the fieldset and click **Create**.
6. On the 'Edit Fieldset' page, mark the **Required** checkbox next to any additional fields that you want to make required. 
   *Note:* Fields provided by Procore cannot be turned off, and required fields (Name, Revision, Status, and Type) cannot be marked as optional. For more information on the fields, see [What are the different fields in the Document Management tool?](/faq-what-are-the-different-fields-in-the-document-management-tool)
7. *Optional:* Click **Add Custom field** to create a new custom field *or* to select from existing custom fields. 
    A banner at the top tells you how many existing custom fields you've already added to the current fieldset. For information about where custom fields appear, see Create Custom Fields.
8. Click **Save**.
9. In the 'Apply changes to project(s)?' window, click **Assign Projects** to add the fieldset to projects.

   - In the 'Assign Projects' window, mark the checkbox next to each project you want to apply the fieldset to and click **Update**.
   - In the 'Apply changes to project(s)?' window, click **Confirm**.
10. *Optional:* To set a fieldset as the default for new projects, click **Set as Default**.

#### Edit Default Fields

1. Navigate to the Company level **Admin** tool.
2. On the sidebar, scroll down to 'Tool Settings' and click **Document Management**.
3. Click the **Default Fields** tab. 
    You can manage options for the following fields:

   - **Classification**: A specific sub-type of a document type.
   - **Discipline**: The discipline associated with this document.
   - **Status**: The state of a document as it goes through a process.
   - **Type**: The different categories of documents, like drawings, specifications, or models.
   - **Volume / System**: A complete set of equipment that works together for one role or purpose.
4. Click the **arrow** icon next to a field name to show options for that field.
5. Click **Edit**.
6. Modify the options for the field as necessary:

   - To rename an option's **Code** or update its **Description**, click into the field and enter the updated text.
   - To hide an option, clear the checkbox.
   - To show an option, mark the checkbox.
   - To add an option, click **Add Option**.
   - To delete an option, click the **delete** icon.
7. When you're ready to save the changes, click **Save**.

##### Â Note

Procore also allows *project* Admins to edit field option descriptions for a single project from the Document Management tool's Configure Settings **Configure Settings** page. See [Configure Settings: Document Management](/product-manuals/document-management-project/tutorials/configure-settings-document-management).