# Change a Project's Status to Active or Inactive

Source: https://v2.support.procore.com/product-manuals/admin-project/tutorials/change-a-projects-status-to-active-or-inactive

---

## Background

A Procore project in your company's Procore account can be placed in one (1) of two (2) statuses:

- **Active**. Indicates the project is in-progress and in an active state. Project actions for administrators and end users are available. This is the default state of a new Procore project.
- **Inactive**. Indicates the project is NOT active. Use this status to indicate that work on the project has been temporarily or permanently suspended. Inactive projects have the following properties:

 - Inactive projects are not visible by default in the company's Portfolio tool, but they can still be viewed. See [View Inactive Projects in the Company Portfolio](/product-manuals/portfolio-company/tutorials/view-inactive-projects-in-the-company-portfolio).
 - Automatic overdue email notifications will no longer be sent for the following tools: Action Plans, Correspondence, Observations, Punch List, RFIs, Submittals, and Tasks.
 - The inactive project will not appear as an option in the Company Reports tool's custom reports, or as an option to extract data from in the Procore Extracts application (i.e. the project will need to be set back to 'Active').
 - Overdue notifications will still be sent (if applicable) for the following: RFQs, Workflows, and Custom Tools.
 - Automated report emails will still be generated
 - Users in the project directory will still be able to access the project through the Portfolio.
 - Users in the project directory will still be able to create items with the appropriate permission to do so.
 - Items/tags/filters in that project will still prevent deletion at the company level (for example, Trades or Stages).
 - Fieldsets can still be applied.
 - Users with the appropriate permissions to the project's Procore tools can still make changes to inactive projects.
 - Weekly Schedule notifications will not be sent from a Procore project marked Inactive.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Project level Admin tool. 
     OR
 - 'Read Only' or 'Standard' level permissions on the Project level Admin tool with the ['Update General Settings' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.
- **Additional Information:**

 - When you create a project in Procore (see [Create a New Project](/product-manuals/portfolio-company/tutorials/create-a-new-project)), the system places it in the 'Active' status by default.
 - When a project is inactive:\* Automatic overdue email notifications will no longer be sent for the following tools: Action Plans, Correspondence, Observations, Punch List, RFIs, Submittals, and Tasks.\* Overdue notifications will still be sent (if applicable) for the following: RFQs, Workflows, and Custom Tools.\* The inactive project will not appear as an option in the Company Reports tool's custom reports, or as an option to extract data from in the Procore Extracts application (i.e. the project will need to be set back to 'Active').
 - If you are unable to set the project to Inactive, see [Why can't I create or activate Procore projects?](/faq-why-cant-i-create-or-activate-procore-projects)

## Steps

1. Navigate to the Project level **Admin** tool.
2. Make sure the **General** page is selected.
3. Under Project Information, locate the **Active** or **Inactive** toggle.
4. Click the toggle to the ON position to set the project to Active. 
    OR Click the toggle to the OFF position to set the project to Inactive.
5. Click **Update**.