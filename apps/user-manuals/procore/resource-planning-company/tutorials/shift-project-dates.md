# Shift Project Dates

Source: https://v2.support.procore.com/product-manuals/resource-planning-company/tutorials/shift-project-dates

---

## Background

Resource Planning gives you the ability to shift project dates, including the assignments and requests. When moved, any associated assignments and requests are shifted by the same duration and in the same direction in time. There are two ways to shift project dates:

- Shift Project to shift future projects that have not yet started.
- Move a Project on the Gantt to shift projects that are in progress.

## Things to Consider

- [Required User](/product-manuals/resource-planning-company/permissions) [Permissions](/product-manuals/resource-planning-company/permissions)
- There are two ways to shift project dates:

  - **Move Project on the Gantt (Beta)**

    - Shift dates for projects that are in progress.
  - **Shift Project**

    - You can only shift future projects that have not yet started.
    - The 'Shift Project' setting must be enabled. See [Configure Integration Settings for Resource Planning](/product-manuals/resource-planning-company/tutorials/configure-integration-settings-for-resource-planning).
    - The project's start date must be in the future, set in the project's information section.
    - The project's status must be 'Active' or 'Pending'.

##### Â Important

For customers with Resource Planning **integrations:**

- The **Shift Project toggle must be turned ON** if your integrated projects are created and managed outside of Resource Planning. See [Configure Integration Settings for Resource Planning](/product-manuals/resource-planning-company/tutorials/configure-integration-settings-for-resource-planning).  
  *Note:* If you have an integration where start date is ignored, or where a project is created in Resource Planning, you do not need to turn the Shift Project toggle on.
- The **start date** must be updated in your system of record. Projects, assignments, and requests will automatically shift the next time your system syncs with Resource Planning.
- If a **project end date** has been shortened or extended via an integration, along with a new start date, assignment and request end dates will need to be manually updated.

## Steps

You can edit project information in the following places:

- [Assignments Boards](#shift-project-from-the-assignments-boards)
- [Assignment Gantt](#shift-project-from-the-assignment-gantt)
- [Assignment Gantt (Beta)](#shift-project-from-the-assignment-gantt-beta)

## Shift Project from the Assignments Boards

1. Navigate to the Company level **Resource Planning** tool.
2. Click **Assignments** and select **Boards.**
3. Next to the project you want to shift, click the **horizontal ellipsis**  and select **Shift Project**.
4. Enter a new project start date.
5. Click **Update**.  
   The start date is updated and any associated resource assignments and requests are shifted by the same duration and in the same direction in time.

## Shift Project from the Assignment Gantt

1. Navigate to the Company level **Resource Planning** tool.
2. Click **Assignments** and select **Gantt.**
3. Next to the project you want to shift, click the **horizontal ellipsis**  and select **Shift Project**.
4. Enter a new project start date.
5. Click **Update**.  
   The start date is updated and any associated resource assignments and requests are shifted by the same duration and in the same direction in time.

## Shift Project from the Assignment Gantt (Beta)

##### Â In Beta

This feature is in beta and available for customers using the Resource Planning tool.

1. Navigate to the Company level **Resource Planning** tool.
2. Click **Assignments** and select **Gantt (Beta)**.
3. Click the **expand**  icon to expand the project.
4. Press and hold the **SHIFT** key and select the project, categories, assignments, and requests to shift the project and maintain the tasks timing and spacing.  
   *Note:* If you only select the project, the project's start and end dates will move but the project's categories, assignments, and requests will retain their original dates.
5. Click and hold the last selection, then move the grouping to the desired dates using a drag and drop operation.