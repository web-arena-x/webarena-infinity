# Add a Template Correspondence Type

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/add-a-template-correspondence-type

---

## Background

Procore has created several template correspondence types based on popular construction use cases and recommended practices. These template correspondence types have unique default fieldsets and can be added to one or more projects after the steps below are completed.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Company level Admin tool.
- Each Procore account has a limit on the number of correspondence types:

 - Accounts with the GC Essentials, GC Enhance, or GC Premier starter pack or with the SC Essentials, SC Enhance, or SC Premier starter pack are limited to 10 correspondence types that are created from a Procore template. Custom workflows in the Company Workflows tool are *not* supported.
 - All other account packages, such as with Project Management Pro or Project Management Owners, are limited to 30 correspondence types (custom or from template). If you need more than 30, please work with your Procore point of contact.
- Template correspondence types that have already been added to your company's Procore account are not included in the 'Choose Templates' list.
- If your company already created a custom type with the same name as a template type below, the template type may not show in the 'Choose Templates' list.

## Steps

1. Navigate to the Company level **Admin** tool.
2. Under 'Tool Settings', click **Correspondence**.
3. Click the **Types** tab.
4. Click **+Create**.
5. In the 'Add Correspondence Type' window, select the **Start from Template** button. *Note:* See [Create a New Correspondence Type](/product-manuals/admin-company/tutorials/create-a-new-correspondence-type) for information about the **Make New Custom** **Type** option that is available to Procore customers with the Project Management Pro or Project Management Owners package.
6. Mark the checkbox next to each of the following template correspondence types that you want to add to your company: *Note:* Read through the Things to Consider section above to ensure you understand why some template types may not show in the 'Choose Templates' list.
7. *Optional:* Mark the **Items are private by default** checkbox if you want all items that are created under this correspondence type to be private by default.
8. *Optional:* Mark the **Send Email Reminders for Overdue Items** checkbox if you want Procore to send automatic email reminders to assignees when an item they are assigned to is overdue. Enabling or disabling this feature affects all projects that use this correspondence type. This is a global feature that cannot be configured for a single project.
9. Click **Add**. This creates a configurable fieldset for the template correspondence type that can be applied to existing projects, set as the default fieldset for the correspondence type on new projects, or edited.

## Next Steps

[Apply Configurable Fieldsets to Projects](/product-manuals/admin-company/tutorials/apply-configurable-fieldsets-to-projects)