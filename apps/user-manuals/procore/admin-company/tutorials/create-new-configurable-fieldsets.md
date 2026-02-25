# Create New Configurable Fieldsets

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/create-new-configurable-fieldsets

---

## Background

*Configurable fieldsets* are the fields in certain Procore tools that can be set to optional, required, or hidden, depending on the needs of your company. This allows for better control over data entry when users create and edit items in Procore projects. See [What are configurable fieldsets and which Procore tools support them?](/faq-what-are-configurable-fieldsets-and-which-procore-tools-support-them)

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Company level Admin tool.
- **Additional Information:**

 - You can create multiple versions of configurable fieldsets to use in different projects. 
    *Note:* If you want to configure a fieldset for the Project level Admin tool (for creating and updating project information), see [Create a Project Fieldset](/product-manuals/admin-company/tutorials/create-a-default-project-fieldset).
 - Configurable fieldsets applied to projects will be reflected on both Procore's web and mobile applications.
 - If you want to configure fieldsets for specific tools, see [What are configurable fieldsets and which Procore tools support them?](/faq-what-are-configurable-fieldsets-and-which-procore-tools-support-them)
 - If a field that is not currently supported on the Procore mobile app is marked as 'Required,' the unsupported field will not appear on the mobile app and the item can still be submitted without the required field. Items created and edited on the web application will still require the 'Required' fieldset regardless of whether the field is supported on the mobile app.

## Steps

1. Navigate to the Company level **Admin** tool.
2. Under 'Tool Settings', click the tool you want to create configurable fieldsets for.
3. Click the **Fieldsets** tab. 
     
   *Note:* Tools without other settings in the Company level Admin tool will open to this page automatically.
4. Click **Create Fieldset** and if required, select the fieldset type.
5. Enter a name for the fieldset, then click **Create**.
6. On the 'Edit Fieldset' page, each field name has the following options:

   - Click the toggle to the ON position to make the field visible in the section. 
     OR Click the toggle to the OFF position to hide the field in the section.
     *Note:* A icon indicates that the field is visible by default and cannot be changed to hidden.
   - Mark the 'Required' checkbox to designate the field as required. 
     OR Clear the 'Required' checkbox to designate the field as optional.
     *Notes:*

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