# Edit Configurable Fieldsets

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/edit-configurable-fieldsets

---

## Background

A *configurable fieldset* is a group of fields in certain Procore tools that can be set to optional, required, or hidden, depending on the needs of your company. This allows for better control over data entry when users create and edit items in Procore projects. See [What are configurable fieldsets and which Procore tools support them?](/faq-what-are-configurable-fieldsets-and-which-procore-tools-support-them)

## Things to Consider

- [Required User Permissions](/product-manuals/rfi-project/permissions)
- **Additional Information**:

 - By default, configurable fieldsets are only applied to new projects. However, you can select which existing projects to apply them to.
 - Configurable fieldsets applied to projects will be reflected on both Procore's web and mobile applications.
 - Changing a field's requirements ('Required' or 'Optional') will impact creating new items or updating existing items on projects that the configurable fieldset was applied to.
 - When custom fields are added to or removed from a configurable fieldset that is applied to one or more projects, the custom fields will be added to or removed from all of the fieldset's existing and new items within the projects.

## Prerequisites

See [Create New Configurable Fieldsets](/product-manuals/admin-company/tutorials/create-new-configurable-fieldsets) OR **click here to view the steps.**

1. Navigate to the Company level **Admin** tool.
2. Under 'Tool Settings', click the tool you want to create configurable fieldsets for.
3. Click the **Fieldsets** tab. *Note:* Tools without other settings in the Company level Admin tool will open to this page automatically.
4. Click **Create Fieldset** and if required, select the fieldset type.
5. Enter a name for the fieldset, then click **Create**.
6. On the 'Edit Fieldset' page, each field name has the following options:

   - Do one of the following:

     - Click the toggle to the ON position to make the field visible in the section.
     - Click the toggle to the OFF position to hide the field in the section. *Note:* A icon indicates that the field is visible by default and cannot be changed to hidden.
   - Do one of the following:

     - Mark the 'Required' checkbox to designate the field as required.
     - Clear the 'Required' checkbox to designate the field as optional. *Notes:*

       - Fields without a checkbox are optional by default and cannot be changed to required.
       - A gray marked checkbox indicates that the field is required by default and cannot be changed to optional.
7. *Optional:* If available, click **Create Section** to create a new section. See [Create Custom Sections](/product-manuals/admin-company/tutorials/create-custom-sections).
8. Click **Save**.
9. In the 'Apply changes to [#] project(s)?' window, click **Assign Projects** to add the fieldset to projects.

   - In the 'Assign Projects' window, mark the checkbox next to each project you want to apply the fieldset to and click **Update**.
   - In the 'Apply changes to [#] project(s)?' window, click **Confirm**.
10. *Optional:* To set a fieldset as the default for new projects, click the icon at the end of its row on the 'Fieldsets' tab and select **Set as New Project Default**.

    ##### Â Note

    Projects created from a project template that includes fieldsets will inherit the fieldsets from the project template instead of your company's default fieldsets. See [Configure a Project Template](/product-manuals/portfolio-company/tutorials/configure-a-project-template).

---

## Steps

1. Navigate to the Company level **Admin** tool.
2. Under 'Tool Settings', click the tool you want to edit configurable fieldsets for.
3. Click the **Fieldsets** tab.   
   Tools without other settings in the Company level Admin tool will open to this page automatically.
4. *Optional:* If you want to rename a fieldset:

   1. Click into the **Title** field and edit the name.
   2. Press ESC on your keyboard.
5. Click **Edit** next to the fieldset you want to modify.
6. On the 'Edit Fieldset' page, each field name has the following options:

   - Click the toggle to the ON position to make the field visible in the section.
   - Click the toggle to the OFF position to hide the field in the section. 
     icon indicates that the field is visible by default and cannot be changed to hidden.
   - Mark the 'Required' checkbox to designate the field as required. 
     **OR** Clear the 'Required' checkbox to designate the field as optional.
     **Notes:**

     - Fields without a checkbox are optional by default and cannot be changed to required.
     - A gray marked checkboxindicates that the field is required by default and cannot be changed to optional.
7. *Optional:* Click **Create Section** to create a new section. 
   **Note:** This is only available for some tools.

   - Enter the section name, then click **Create**.
8. *Optional:* Click **Add Custom Field** in the relevant section.

   - Create New

     - Click **Create New**.
     - Enter the **Field Name.**
     - Enter the **Field Type.**
     - Click **Create**.
   - Choose Existing

     - Click **Choose from Existing**.
     - Click **Add** next to the custom field. 
       **Note:** Not all custom field types are available for all tools. See [What field types are available for Custom Fields in Procore Tools?](/faq-what-field-types-are-available-for-custom-fields-in-procore-tools)
9. Click **Save**.
10. In the 'Apply changes to [#] project(s)?' window:

- Click **Apply to Existing** to save your changes to the fieldset on projects that the fieldset is already applied to. 
 **OR**
- Click **Assign Projects** to add or remove the fieldset from projects.

 - In the 'Assign Projects' window, mark the checkbox next to each project you want to apply the fieldset to and click **Update**.
 - In the 'Apply changes to [#] project(s)?' window, click **Confirm**.