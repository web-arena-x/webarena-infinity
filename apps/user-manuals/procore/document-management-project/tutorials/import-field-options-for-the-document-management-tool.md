# Import Field Options for the Document Management Tool

Source: https://v2.support.procore.com/product-manuals/document-management-project/tutorials/import-field-options-for-the-document-management-tool

---

##### Regional availability

The Document Management tool is available in select countries. It is not yet available for Procore accounts in the U.S. To learn more, please reach out to your Procore point of contact.

## Background

If you want to add a large number of field options for a Document Management field, you can download a CSV file template and import the options.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permission to the Company level Admin tool. 
    *Note:* Users with 'Admin' level permissions to Document Management tool can show or hide default field options for a specific project on the Configure Settings page. See [Configure Settings: Document Management](/product-manuals/document-management-project/tutorials/configure-settings-document-management).

## Prerequisites

- You can only import fields after all fields have been removed. See the Delete Field Options section below.

## Steps

1. Navigate to the Company level **Admin** tool.
2. On the sidebar, scroll down to 'Tool Settings' and click **Document Management**.
3. Click the **Default Fields** tab.
4. Click the **arrow** icon next to the field (**Classification**, **Discipline**, **Status**, **Type**, **Volume / System**) that you want to manage options for.
5. Follow the steps below:

   - Delete Existing Field Options
   - Download and Fill Out the Template
   - Import the Template

### Step 1: Delete Existing Field Options

*Note:* After you delete field options, you won't be able to use them on any projects. However, these options will not be deleted from any current documents that use them.

1. Click the **vertical ellipsis** icon for the field and select **Delete All**.
2. Click **Delete Options** to confirm the deletion.   
    If the changes do not show in the table after a few moments, refresh the page and return to the table.

### Step 2: Download and Fill Out the Template

1. Click the **vertical ellipsis** icon for the field and select **Download Template**. 
    A CSV file will download to your computer.
2. Open the CSV file and fill out the field options under the provided columns. Do not change the headings of the template or add any additional columns.
3. Save your file.

### Step 3: Import the Template

1. Click the **vertical ellipsis** icon for the field and select **Import Template**.
2. Select the file that you updated.
3. If the template contains one or more options that were previously deleted, you'll see a 'Recover Options' window.

   - To recover any options, click **Continue**.
   - To return to your import and create a unique field option, click **Cancel**.
   - To continue with the import without making changes, click **Ignore**.
4. The field options are automatically added. You can make any changes as needed. See [Manage Custom and Default Fields and Fieldsets for the Document Management Tool](/product-manuals/document-management-project/tutorials/manage-custom-and-default-fields-and-fieldsets-for-the-document-management-tool) for more information.