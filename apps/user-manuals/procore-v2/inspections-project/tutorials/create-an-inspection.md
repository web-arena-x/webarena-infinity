# Create an Inspection

Source: https://v2.support.procore.com/product-manuals/inspections-project/tutorials/create-an-inspection

---

## Things to Consider

- [Required User Permissions](/product-manuals/inspections-project/permissions)
- After a company template is copied to your project, it becomes a project template that can be modified without affecting the company template from which it originated.
- Project templates may be modified in the Project level Inspections tool throughout the duration of the project, but changes will only be reflected on project checklists that are created from the modified template.
- You can use a default inspection template more than once.
- To create an inspection for **equipment**, you must first configure the following settings:

 - The Equipment tool must be enabled for your project. See [Add and Remove Project Tools](/product-manuals/admin-project/tutorials/add-and-remove-project-tools).
 - Equipment records must be added to your project. See [Add or Remove Equipment from Projects](/process-guides/project-equipment-user-guide/add-from-company-web).
 - Equipment must be enabled on your configurable fieldset for inspections. See [Edit Configurable Fieldsets](/product-manuals/admin-company/tutorials/edit-configurable-fieldsets).

## Prerequisites

- [Create a Company Level Inspections Template](/product-manuals/inspections-company/tutorials/create-a-company-level-inspection-template)
- [Add Company Level Inspection Templates to Your Project](/product-manuals/inspections-project/tutorials/add-company-level-inspection-templates-to-your-project) 
   **OR** 
 [Create a Project Level Inspection Template](/product-manuals/inspections-project/tutorials/create-a-project-level-inspection-template)

## Steps

1. Navigate to the Project level **Inspections** tool.
2. Click **Create**. **Note:** If your company does not yet have Company level inspection templates set up, you first need to [create an inspection template](/product-manuals/inspections-company/tutorials/create-a-company-level-inspection-template).
3. Select **Inspection**.
4. Select a default inspection template from your list of templates from the drop-down menu. **Note:** Templates must be added to your project. See [Add Company Level Inspection Templates to Your Project](/product-manuals/inspections-project/tutorials/add-company-level-inspection-templates-to-your-project).
5. Enter the relevant information for each field.
6. *Optional:* Under **Inspection Items Preview**, review the inspection items and their response options.
7. Click **Create**.

## Bulk Create Inspections

##### Beta

The **Bulk Create Inspections** feature is currently in open beta and can be enabled within [Procore Explore](/product-manuals/admin-company/tutorials/manage-features-with-procore-explore).

With the bulk create feature, you can quickly create multiple inspections with identical details to save time.

1. In the new field titled **Number of Inspections**, enter the desired quantity. You can use the up/down arrows or type the number directly.
2. Optionally, you can set the **starting number** for the inspections in the sequence. For example, if you set the starting number to 64 and the number of inspections to 5, the inspections will be numbered sequentially starting at 64.
3. Fill in all the other inspection details (e.g., location, assignee, due date) as you normally would.   
   **Note:** All the inspections created in this bulk action will have the exact same details. This feature does not allow you to assign different locations or assignees for each individual inspection.
4. Once you have filled in all the details, click **Create**.

## Next Steps

- [Perform an Inspection](/product-manuals/inspections-project/tutorials/perform-an-inspection)