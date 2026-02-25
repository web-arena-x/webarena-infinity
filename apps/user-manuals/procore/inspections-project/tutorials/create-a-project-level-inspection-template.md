# Create a Project Level Inspection Template

Source: https://v2.support.procore.com/product-manuals/inspections-project/tutorials/create-a-project-level-inspection-template

---

## Background

Creating inspection templates at the Project level allows you to easily use the same or similar templates in your project without having to remake them each time. Templates created at the Project level will not sync to the Company level. If you want to use a template on more than one project, create the template at the Company level. [You can also modify an existing Company level template](/product-manuals/inspections-company/tutorials/edit-a-company-level-inspection-template) to fit your project's unique needs.

## Things to Consider

- [Required User Permissions](/product-manuals/inspections-project/permissions)
- **Additional Information:**

 - Custom response sets are created and managed by company level 'Admin' users in the Company level Inspections tool. See [Create a Custom Response Set for Inspections](/product-manuals/inspections-company/tutorials/create-a-custom-response-set-for-inspections).
 - Field availability is based on how the inspection fieldset is configured. See [Create New Configurable Fieldsets](/product-manuals/admin-company/tutorials/create-new-configurable-fieldsets) or [Edit Configurable Fieldsets](/product-manuals/admin-company/tutorials/edit-configurable-fieldsets).
 - There is a limit of 1,000 items per section on an Inspection template.

##### Important

If a warning banner or icon appears on your **Inspection Templates** list, certain response requirements (like "Require Observation") may need adjustment. See this [FAQ](/faq-why-am-i-seeing-a-some-templates-need-updates-warning) for help.

## Prerequisites

- Add inspection types. See [Configure Advanced Settings: Company Level Inspections](/product-manuals/inspections-company/tutorials/configure-advanced-settings-company-level-inspections).

## Steps

1. Navigate to the Project level **Inspections** tool.
2. Click the **Configure Settings** icon.
3. Click the **Templates** tab.
4. Click **+ Create**.
5. Under General Information, enter the following:

   - **Name**
   - **Type**
   - **Trade**
   - **Description**
   - **Attachments**
6. Under **Inspection Items**, add sections and items to your inspection as follows:

   - **+ Add section**
   - **+ Add item**
   - **+ Quick Add**: See [What is Inspection Template Item Quick Add?](/product-manuals/inspections-company/tutorials/use-quick-add-on-a-company-inspection-template)**Note:**You can reorder individual items within a section of your template by dragging your item with the **reorder** icon. To reorder an entire section, click the **toggle on** icon next to **Reorder Sections** and drag the sections of your choice. .
   - **+ Add References**
7. Select a response type for individual items from the **Response Type** menu **OR** to select the same response type for multiple items, mark the checkboxes next to the individual items or the section header, then click the **Edit Response Type** button.
8. To **turn on inspection item requirements**, tab or scroll over to the **Require Observations** **On** or **Require Photos On** columns. **Note:** If the requirement is not provided by the user, the requirement will not be saved.
9. Click **Select a Response**.

   - **Status**: You can select either a 'Conforming' or 'Deficient' status, or you can select both.
   - **Responses**: You can select any of the possible responses for the 'Response Type', or you can select a combination of the three. You can also select 'Not Required'.
10. Click the **Add Conditions** icon to add conditional logic to your inspection item. See [Add Conditional Logic to a Project Level Inspection Template](/product-manuals/inspections-project/tutorials/add-conditional-logic-to-project-level-inspection-template).
11. Click **Create**.