# Remove Configurable Fieldsets from Projects

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/remove-configurable-fieldsets-from-projects

---

## Background

A *configurable fieldset* is a group of fields in certain Procore tools that can be set to optional, required, or hidden, depending on the needs of your company. This allows for better control over data entry when users create and edit items in Procore projects.   
See [What are configurable fieldsets and which Procore tools support them?](/faq-what-are-configurable-fieldsets-and-which-procore-tools-support-them)

If configurable fieldsets were previously applied to a project, you can choose to remove the custom configurations from that project. After a project has been deselected, the fieldsets will return to Procore's default fieldsets.   
If you want to delete a fieldset, see [Delete Configurable Fieldsets](/product-manuals/admin-company/tutorials/delete-configurable-fieldsets).

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Company level Admin tool.
- **Additional Information:**

 - After a project has been deselected from the 'Assigned Projects' window, the fieldsets will return to Procore's default fieldsets.
 - Configurable fieldsets applied to projects will be reflected on both Procore's web and mobile applications.

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
2. Under 'Tool Settings', click the tool you want to view fieldsets for.
3. Click the **Fieldsets** tab. 
   *Note*: Tools without other settings in the Admin tool will open to this page automatically.
4. Locate the configurable fieldset you want to remove from projects.
5. Click the fieldset's link in the 'Assigned Projects' column (e.g. 15/30 Projects). 
     
   **Note:** This link indicates the number of projects the fieldset is currently applied to, out of the number of projects in the account.
6. Clear the checkboxes corresponding to the projects you want to remove the configured fieldset from.
7. Click **Update**. 
   **Note:** Any unselected projects will be updated with the Procore Default fieldset for that tool or section.