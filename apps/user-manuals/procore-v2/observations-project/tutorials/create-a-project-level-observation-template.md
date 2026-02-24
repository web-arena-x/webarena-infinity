# Create a Project Level Observation Template

Source: https://v2.support.procore.com/product-manuals/observations-project/tutorials/create-a-project-level-observation-template

---

## Background

Observation templates allow Procore users to create a library of common observation items that can be organized by type. Default titles, trades, and assignees can be assigned to these observation templates. When a Procore user creates a new observation from a mobile device, they can select one of these templates, which will auto-populate fields on the new observation item with default information from the template. Users can then add or edit information as needed, save the observation item, and move on. This allows users to select common observation items from their library and create new observation items more efficiently and with significantly less typing.

## Prerequisites

- [Add Project Level Observation Types](/product-manuals/observations-project/tutorials/add-project-level-observation-types)

## Things to Consider

- **Required User Permissions:**

  - To create a Project level observation template, 'Admin' on the Project level Observations tool.
  - To be designated as a 'Default Assignee' on the template, 'Standard' level permission or higher on the Project level Observations tool.
- **Additional Information:**

  - Observation templates created at the Project level will only be present on the indicated project.
  - To manage observation templates at the Company level so that the template will appear on all projects, see [Create a Company Level Observation Template.](/product-manuals/admin-company/tutorials/create-a-company-level-observation-template)
  - Once created, these observation templates are only available for use on Procore's mobile applications. See [Create an Observation (iOS)](/product-manuals/observations-ios/tutorials/create-an-observation-ios).

## Steps

1. Navigate to the Project level **Observation** tool.
2. Click **Configure Settings** .
3. Click **Observation Templates**.
4. Scroll to the category under which you want to create a template.
5. Enter the following information in the empty fields.

   - **Template Title**: Enter the title of the template. This will populate in the subject of the observation.
   - **Default Trade**: Select the trade that is associated with the type of observation.
   - **Default Assignee**: Select the assignee that will most likely be responsible for resolving items like this. For a project user to appear as a selection in this list, the user's profile must be added to the Project Directory (see [Add a User Account to the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory)) and be granted 'Standard' level permission or higher on the Project level Observations tool. See [Change a User's Permissions in the Project Directory](/product-manuals/directory-project/tutorials/change-a-users-permissions-in-the-project-directory).
   - **Active**: Mark the checkbox if you want your team to leverage this template when creating observation items on this project.
6. Click **Add**.