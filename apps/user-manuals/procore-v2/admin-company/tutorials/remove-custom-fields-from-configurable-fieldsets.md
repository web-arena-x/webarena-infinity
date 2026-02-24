# Remove Custom Fields from Configurable Fieldsets

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/remove-custom-fields-from-configurable-fieldsets

---

## Background

Custom fields can be created for certain tools in Procore to allow for additional information to be filled out when creating or editing items. Similar to most fields in Procore, custom fields can be reported on in the Company and Project level Reports tools.

To better organize your fieldsets, custom fields can be removed from configurable fieldsets. See [What are configurable fieldsets and which Procore tools support them?](/faq-what-are-configurable-fieldsets-and-which-procore-tools-support-them)

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Company level Admin tool.
- **Additional Information:**

 - When custom fields are removed from a configurable fieldset that is applied to one or more projects, the custom fields will be removed from all of that fieldset's existing and new items within the projects.
 - Removing a custom field from a configurable fieldset does not delete the data associated with that field from Procore.
 - Removing a custom field from configurable fieldsets does not delete the custom field itself. See [Delete Custom Fields](/product-manuals/admin-company/tutorials/delete-custom-fields).

## Prerequisites

- [Create New Custom Fields](/product-manuals/admin-company/tutorials/create-new-custom-fields)

## Steps

1. Navigate to the Company level **Admin** tool.
2. Under 'Tool Settings', click the tool with the fieldset that you want to remove the custom field from.
3. Click the **Fieldsets** tab.
4. Click **Edit** next to the fieldset that you want to remove the custom field from.
5. Click the **vertical ellipsis** across from the field you want to remove and select **Remove**.
6. Click **Save**.
7. In the 'Apply changes to [#] project(s)?' window, do one of the following:

   - Click **Apply to Existing** to save your changes to the fieldset on projects that the fieldset is already applied to.
   - Click **Assign Projects** to add or remove the fieldset from projects.

     - In the 'Assign Projects' window, mark the checkbox next to each project you want to apply the fieldset to and click **Update**.
     - In the 'Apply changes to [#] project(s)?' window, click **Confirm**.