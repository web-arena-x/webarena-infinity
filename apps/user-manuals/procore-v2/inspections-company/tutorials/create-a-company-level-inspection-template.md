# Create a Company Level Inspection Template

Source: https://v2.support.procore.com/product-manuals/inspections-company/tutorials/create-a-company-level-inspection-template

---

## Background

Creating inspection templates at the Company level allows you to easily use the same or similar templates across your projects without having to remake them each time. You can always make a [new inspection template at your Project level](/product-manuals/inspections-project/tutorials/create-a-project-level-inspection-template), or you can [modify an existing Company level template](/product-manuals/inspections-company/tutorials/edit-a-company-level-inspection-template) for your project's unique needs.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Company level Inspections tool.
- **Additional Information:**

 - Although you can create new inspection templates at the Project level, you cannot add any inspection templates made at the Project level to another project in your company. For this reason, the best practice to manage your Inspections in Procore is to create inspection templates at the Company level to use at the Project level and modify those templates for each of your project's needs.
 - Field availability is based on how the inspection fieldset is configured. See [Create New Configurable Fieldsets](/product-manuals/admin-company/tutorials/create-new-configurable-fieldsets) or [Edit Configurable Fieldsets](/product-manuals/admin-company/tutorials/edit-configurable-fieldsets).
 - There is a limit of 1,000 items per section on an Inspection template.

##### Important

If a warning banner or icon appears on your **Inspection Templates** list, certain response requirements (like "Require Observation") may need adjustment. See this [FAQ](/faq-why-am-i-seeing-a-some-templates-need-updates-warning) for help.

## Video

## Steps

1. Navigate to the Company level **Inspections** tool.
2. Click **+** **Create.***Note:* You can also [Clone an Existing Company Level Inspection Template](/product-manuals/inspections-company/tutorials/clone-a-company-inspection-template). 
   This reveals the New Inspection Template page.
3. Under **General Information**, enter the following information:

   - **Name:** Title your inspection.
   - **Type**: Choose from the list of inspection types added to the company (e.g. Safety).
   - **Trade** : Add a trade to your inspection (e.g. Electrical, plumbing) .
   - **Description** : Include any relevant details about the inspection.
   - **Attachments:** Attach any relevant files to the templates by clicking **Attach Files** or by using a drag-and-drop operation. 
     *Note:* If you try to create an inspection template without a name or with a name that already exists, there will be an error message that details the reason. You can create an inspection with the same name as one in the Recycle Bin, but once you name it, you cannot restore a template in the Recycle Bin without first [editing an inspection template](/product-manuals/inspections-company/tutorials/edit-a-company-level-inspection-template) to change the name.)
4. Under **Inspection Items**, add sections and items to your inspection as follows:

   - **+ Add section** : Click this button to add a section to your inspection template.
   - **+ Add item** : Click this button to add an item within the current section.
   - **+ Quick Add**: See [What is Inspection Template Item Quick Add?](/product-manuals/inspections-company/tutorials/use-quick-add-on-a-company-inspection-template) *Note :* You can reorder individual items within a section of your template by dragging your item with the **reorder** icon. To reorder an entire section, click the **toggle on** icon next to **Reorder Sections** and drag the sections of your choice. Turn off **Reorder Sections** to continue creating your template.
   - **+ Add References**: Click this button to attach files from your computer for additional inspection item details.
5. Select a response type for individual items from the **Response Type** menu. 
   **OR** To select the same response type for multiple items, mark the checkboxes next to the individual items or the section header, then click the **Edit Response Type** button.
6. To **turn on inspection item requirements**, tab or scroll over to the **Require Observations** **On** or **Require Photos On** columns. 
   *Note:* If the requirement is not provided by the user, the requirement will not be saved.
7. Click **Select a Response**.

   - **Status**: You can select either a 'Conforming' or 'Deficient' status, or you can select both.
   - **Responses**: You can select any of the possible responses for the 'Response Type', or you can select a combination of the three. You can also select 'Not Required'.
   - Click 'X' to remove any of your response types.
8. Click the **Add Conditions** icon to add conditional logic to your inspection item. See [Add Conditional Logic to a Company Level Inspection Template](/product-manuals/inspections-company/tutorials/add-conditional-logic-to-company-level-inspection-template).
9. Click **Create**.