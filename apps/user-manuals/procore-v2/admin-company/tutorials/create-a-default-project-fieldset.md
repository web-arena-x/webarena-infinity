# Create Project Fieldset

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/create-a-default-project-fieldset

---

## Background

Configurable fieldsets refer to fields in specific Procore tools that can be set as optional, required, or hidden. The project fieldset includes fields available when creating and editing project information. Once configured in the company's Admin tool, these fields can be edited for each project in that project's Admin tool or in the 'Overview' tab of the Bid Board and Portfolio Planning tool.

See [Which fields on the create or update project page can be configured as required, optional, or hidden?](/faq-which-fields-on-the-create-or-update-project-page-can-be-configured-as-required-optional-or-hidden)

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Company level Admin tool.
- **Additional Information:**

 - Only one fieldset can be created. If a fieldset already exists, the Create Fieldset button is disabled.
 - The fieldset will apply to all new and existing projects. It cannot be assigned to individual projects.
 - If you want to configure fieldsets for specific tools, see [What are configurable fieldsets and which Procore tools support them?](/faq-what-are-configurable-fieldsets-and-which-procore-tools-support-them)
 - The fields in this fieldset are also visible in the Bid Board tool.

## Steps

1. Navigate to the Company level **Admin** tool.
2. Under 'Project Settings', click **Fieldset**.
3. Click **Create Fieldset**.
4. Enter the name and click **Create**.
5. On the 'Edit Fieldset' page, each field name has the following options:

   - Click the toggle to the ON position to make the field visible in the section. 
     OR Click the toggle to the OFF position to hide the field in the section.
     *Note:* A icon indicates that the field is visible by default and cannot be changed to hidden.
   - Mark the 'Required' checkbox to designate the field as required. 
     OR Clear the 'Required' checkbox to designate the field as optional.
     *Notes:*

     - Fields without a checkbox are optional by default and cannot be changed to required.
     - A gray marked checkboxindicates that the field is required by default and cannot be changed to optional.
6. *Optional:* Click **Create Section** to create a new section.

   1. Enter the section name, then click **Create**.
7. *Optional:* In the relevant section, click Add Custom Field.

   - Create New

     1. Click **Create New**.
     2. Enter the **Field Name.**
     3. Enter the **Field Type.**
     4. Click **Create**.
   - Choose Existing

     1. Click **Choose from Existing**.
     2. Click **Add** next to the custom field. 
        *Note:* Not all custom field types are available for all tools. See [What field types are available for Custom Fields in Procore Tools?](/faq-what-field-types-are-available-for-custom-fields-in-procore-tools)
8. Click **Save**.
9. In the window, click **Confirm**.