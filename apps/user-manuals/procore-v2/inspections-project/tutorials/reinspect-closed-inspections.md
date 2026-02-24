# Reinspect Closed Inspections

Source: https://v2.support.procore.com/product-manuals/inspections-project/tutorials/reinspect-closed-inspections

---

## Background

Reinspections are a crucial step to ensure that any previously identified issues have been properly fixed. By creating a reinspection, you can verify that all work meets project standards and that any potential risks have been reduced.

## Things to Consider

- [Required User Permissions](/product-manuals/inspections-project/permissions)
- The previous inspection will close after the reinspection is created.
- You cannot reinspect an inspection that has already been reinspected.
- You cannot reinspect an invalid reinspection.

## Prerequisites

- [Create an Inspection](/product-manuals/inspections-project/tutorials/create-an-inspection)

## Steps

1. Navigate to the Project level **Inspections** tool.
2. Click **View** next to the inspection you want to reinspect.
3. Click the **ellipsis**icon, then click **Reinspect**.

   - This option is only visible to users with the 'Create a Reinspection' permission.
   - It will also not appear if the inspection has already been reinspected or if it is an invalid reinspection of a previous one.
   - If the inspection is not yet closed, a warning message will appear: "Creating a reinspection will close this inspection."
   - Click **Continue** to proceed or click **Cancel** to return to the original inspection.
4. A new '**child inspection'** is created.

   - All line items from the previous inspection will carry over.
   - Line items that previously passed will retain their passed status.