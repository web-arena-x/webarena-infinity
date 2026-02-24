# Create New Custom Fields

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/create-new-custom-fields

---

## Background

Custom fields can be created for certain tools in Procore to allow for additional information to be filled out when creating or editing items. Similar to most fields in Procore, custom fields can be reported on in the Company and Project level Reports tools in most cases.

## Things to Consider

- [Required User Permissions](/product-manuals/admin-company/permissions)
- To see which tools support custom fields, see [What are custom fields and which Procore tools support them?](/faq-what-are-custom-fields-and-which-procore-tools-support-them)
- All tools supporting custom fields also support custom fields through the Procore API. See [Working with Configurable Fieldsets](https://developers.procore.com/documentation/tutorial-config-fieldsets) on the [Procore Developer Portal](https://developers.procore.com/) for additional information.
- After they are created, custom fields can be added to any new or existing configurable fieldset for supported tools.
- When custom fields are added to a configurable fieldset that is applied to one or more projects, the custom fields will be added to all of the fieldset's existing and new items within the projects.
- Custom fields can be included in reports in the Project and Company level Reports tools in most cases. See [Create a Custom Project Report](/product-manuals/reports-project/tutorials/create-a-project-single-tool-report) and [Create a Custom Company Report](/product-manuals/reports-company/tutorials/create-a-company-single-tool-report).
- Options for multi select or single select dropdown field types are automatically alphabetized.
- Custom fields added to a configurable fieldset are only available for some tools on the Procore mobile app. See [What are custom fields and which Procore tools support them?](/faq-what-are-custom-fields-and-which-procore-tools-support-them)
- **Prerequisites:**

 - To use custom fields on projects, the fields must be added to a configurable fieldset and then applied to one or more projects. See [What are configurable fieldsets and which Procore tools support them?](/faq-what-are-configurable-fieldsets-and-which-procore-tools-support-them)

## Steps

1. Navigate to the Company level **Admin** tool.
2. Under 'Tool Settings', click the tool you want to create custom fields for.
3. [Create Custom Fields for a Configurable Fieldset](#steps)
4. [Apply a Fieldset to Projects](#apply-a-fieldset-to-projects)

### Create Custom Fields for a Configurable Fieldset

There are two ways to create new custom fields to use on projects. Choose one of the following:

- **Option 1:** To create custom fields that you can add to fieldsets later, see Create Custom Fields from the Custom Fields Tab.
- **Option 2:** To create custom fields while in a fieldset on the Fieldsets tab, see Create Custom Fields Within a Fieldset.

#### Option 1: Create Custom Fields from the Custom Fields Tab

1. Click the **Custom Fields** tab.
2. Click **Create Custom Field**.
3. Complete the following information for the new field:

   - **Field Name:** Enter a name for the field.
   - **Field Type:** Select the type of field you want to create. 
     *Note:* Certain field types may not be available for all tools.

     **Expand or Collapse Field Type Options**

     - **Checkbox:** The field will be a checkbox that can be marked or cleared.
     - **Company:** The field will be a drop-down menu that allows users to select a Company from the Project Directory.
     - **Date:** The field will allow the user to select a calendar date.
     - **File Uploads:** The field will allow attachments to be added from supported tools in Procore or the user's computer.
     - **Location:** The field will be a drop-down menu that allows users to select an existing location.
     - **Multi Select:** The field will be a drop-down menu that allows users to select multiple values.
     - **Number:** The field will allow a number value to be entered. 
       *Note:* When a user enters a number into a 'Number' custom field with no decimal value or with two zeros after a decimal point, PDF exports with the field will show a decimal value of .0 for the number. For example, if a user enters 123 or 123.00, the PDF export will show the number as 123.0.
     - **Plain Text (Short):** The field will be a free text field.
     - **Project Directory User (Multi Select):** The field will be a drop-down menu that allows users to select one or more users from the Project Directory.
     - **Project Directory User (Single Select):** The field will be a drop-down menu that allows users to select a user from the Project Directory.
     - **Read Only Entry:** The field will allow you to type a message, such as instructions, in the text box, which will be visible on an item.
     - **Rich Text (Long):** The field will be a rich text field that supports paragraphs to allow longer responses and bold, italic, and underlined text.
     - **Single Select (Dropdown):** The field will be a drop-down menu that allows users to select one value.
     - **Tool User (Single Select):** The field will be a drop-down menu that allows users to select a user with 'Read Only' or higher permissions to the tool.
     - **Date / Time:** The field will be a combination of a calendar menu and a time of day entry.
4. For **Multi Select** and **Single Select** field types, complete the following steps to add options:

   1. Click **Add Options**.
   2. Enter the option in the field.
   3. For each additional option needed, click **Add Option** and enter the option.
   4. Click **Save Options**.
   5. Click **Done**.
5. Click **Create**.
6. Next, the field must be added to a fieldset to be applied to a project. Follow these steps:

   1. Click the **Fieldsets** tab.
   2. Click **Edit** next to the fieldset you want to add the custom fields to.
   3. *Optional:* Add the field to a custom section. 
      See [Create Custom Sections](/product-manuals/admin-company/tutorials/create-custom-sections) and [What are custom sections and which Procore tools support them?](/faq-what-are-custom-sections-and-which-procore-tools-support-them)
   4. Click **Add Custom Field** at the bottom of the page.
   5. Click **Choose From Existing**.
   6. Click **Add** next to the custom field you want to add to the fieldset.
   7. Click **Add** to confirm adding the field.

      - Click the toggle to the ON position to make the custom field visible in the section, or click to the OFF position to hide the custom field.
      - If the custom field should be required, mark the 'Required' checkbox. Otherwise, the field will be optional.
   8. *Optional:* Click and drag on the **reorder grip** icon to rearrange the order that the custom fields will appear on a fieldset. 
      *Note:* Procore Standard fields cannot be reordered.
   9. Click **Save** to save your changes to the configurable fieldset.
   10. If the fieldset is already applied to one or more projects, click **Apply to Existing**. 
       OR If you have just created a new fieldset, click **Assign Projects** and begin at step 3 in the [Apply a Fieldset with Custom Fields to Projects](/product-manuals/admin-company/tutorials/apply-configurable-fieldsets-to-projects) section below.

#### Option 2: Create Custom Fields Within a Fieldset

1. Click the **Fieldsets** tab.
2. Click **Edit** next to the fieldset you want to add the custom fields to. 
   OR Click **Create New** to create a new fieldset. See [Create New Configurable Fieldsets](/product-manuals/admin-company/tutorials/create-new-configurable-fieldsets).
3. *Optional:* Add the field to a custom section. 
   See [Create Custom Sections](/product-manuals/admin-company/tutorials/create-custom-sections) and [What are custom sections and which Procore tools support them?](/faq-what-are-custom-sections-and-which-procore-tools-support-them)
4. Scroll toward the bottom of the page and click **Add Custom Field**.
5. Click **Create New**.
6. Complete the following information for the new field:

   - **Field Name:** Enter a name for the field.
   - **Field Type:** Select the type of field you want to create. 
     *Note:* Some field types may not be available for all tools.

     **Expand or Collapse Field Type Options**

     - **Checkbox:** The field will be a checkbox that can be marked or cleared.
     - **Company:** The field will be a drop-down menu that allows users to select a Company from the Project Directory.
     - **Date:** The field will allow the user to select a calendar date.
     - **File Uploads:** The field will allow attachments to be added from supported tools in Procore or the user's computer.
     - **Location:** The field will be a drop-down menu that allows users to select an existing location.
     - **Multi Select:** The field will be a drop-down menu that allows users to select multiple values.
     - **Number:** The field will allow a number value to be entered. 
       *Note:* When a user enters a number into a 'Number' custom field with no decimal value or with two zeroes after a decimal point, PDF exports with the field will show a decimal value of .0 for the number. For example, if a user enters 123 or 123.00, the PDF export will show the number as 123.0.
     - **Plain Text (Short):** The field will be a free text field.
     - **Project Directory User (Multi Select):** The field will be a drop-down menu that allows users to select one or more users from the Project Directory.
     - **Project Directory User (Single Select):** The field will be a drop-down menu that allows users to select a user from the Project Directory.
     - **Read Only Entry:** The field will allow you to type a message, such as instructions, in the text box, which will be visible on an item.
     - **Rich Text (Long):** The field will be a rich text field that supports paragraphs to allow longer responses and bold, italic, and underlined text.
     - **Single Select (Dropdown):** The field will be a drop-down menu that allows users to select one value.
     - **Tool User (Single Select):** The field will be a drop-down menu that allows users to select a user with 'Read Only' or higher permissions to the tool.
     - **Date / Time:** The field will be a combination of a calendar menu and a time of day entry.
7. For **Multi Select** and **Single Select** field types, complete the following steps to add options:

   1. Click **Add Options**.
   2. Enter the option in the field.
   3. For each additional option needed, click **Add Option** and enter the option.
   4. Click **Save Options**.
   5. Click **Done**.
8. Click **Create** and the field will automatically be added to the bottom of the fieldset.
9. Click the toggle to the ON position to make the custom field visible in the section, or click to the OFF position to hide the custom field.
10. If the custom field should be required, mark the 'Required' checkbox. Otherwise, the field will be optional.
11. Click **Save.**
12. If the fieldset is already applied to one or more projects, click **Apply to Existing**. 
    OR If you have just created a new fieldset, click **Assign Projects** and begin at step 3 of the section below.
13. *Optional:* Click and drag on the **reorder grip** icon to rearrange the order that the custom fields will appear on a fieldset. 
    *Note:* Procore Standard fields cannot be reordered.

## Apply a Fieldset to Projects

### Apply a Fieldset to Projects

1. Click the **Fieldsets** tab.
2. Click the link in the Assigned Projects column for the fieldset you want to apply to projects.
3. Mark the checkboxes next to the projects you want to assign the fieldsets to. 
   OR Click **Select All** to select all projects.
4. Click **Update**.
5. Click **Confirm** to confirm that you want to apply the fieldsets to the selected projects. 
   *Note:* Procore's default fieldsets in the selected projects will be replaced with the fieldsets you configured.
6. *Optional:* You can set any configurable fieldset as the default for new projects. 
   If you want to set a fieldset as the default for new projects:

   1. Click the **vertical ellipsis** icon across from the fieldset.
   2. Click **Set as New Project Default**.