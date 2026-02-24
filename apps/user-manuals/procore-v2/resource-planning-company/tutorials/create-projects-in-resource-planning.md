# Create Projects in Resource Planning

Source: https://v2.support.procore.com/product-manuals/resource-planning-company/tutorials/create-projects-in-resource-planning

---

## Background

Resource Planning gives you the ability to create projects so that you can manage your resources for those initiatives.

##### Â Note

Projects can be created in either [Procore's Portfolio tool](/product-manuals/portfolio-company/tutorials/create-a-new-project) or Resource Planning, but your company must choose one as your system of record. Your Procore point of contact  guides your company through this decision based on your setup.

This article is for customers who have Resource Planning as their system of record for project creation and management.

## Things to Consider

- [Required User](/product-manuals/resource-planning-company/permissions) [Permissions](/product-manuals/resource-planning-company/permissions)
- **If data syncs are enabled:**

  - Projects must have a Project ID to create the project in the Portfolio tool.
  - If you have one project template in the Portfolio tool, the template is applied when the project is synced to the Portfolio tool. If you have more than one project template, no template is applied.
  - Only some information synced between Resource Planning and the Portfolio tool. See [What project information is synced between Resource Planning and Procore Projects?](/faq-what-project-information-is-synced-between-resource-planning-and-procore-projects)
  - Projects created in the Portfolio tool will NOT sync to Resource Planning as your company has chosen to manage projects in Resource Planning as the system of record.
- **If data syncs are disabled**:

  - Active projects are linked between Resource Planning and the Portfolio tool if their unique project numbers match.
  - Information must be manually maintained in both tools.

## Prerequisites

- Your company must choose Resource Planning as the system of record for project creation and management.
- [Configure Groups for Resource Planning](/product-manuals/resource-planning-company/tutorials/configure-groups-for-resource-planning)

## Steps

1. Navigate to the Company level **Resource Planning** tool.
2. Click **Projects** and select **Project List.**
3. Click **Create**.
4. Complete the form with the following information:

   - **Project Name.** Enter the project's name.
   - **Project Number.** Enter the project's project number.
   - **Status.** Enter the project's 'Status' by selecting **Active**, **Pending**, or **Inactive**.
   - **Groups.** Select the project's groups.
   - **Project Start Date.** Enter the project's start date.
   - **Planned End Date.** Enter the project's estimated end date.
   - **Daily Start Time.** Enter the project's daily start time.
   - **Daily End Time.** Enter the project's daily end time.
   - **Timezone.** Select the project's timezone.
   - **Address.** Enter the project's street address.
   - **Address 2.** Enter the project's street address, continued.
   - **City.** Enter the project's city or town.
   - **State.** Enter the project's state or province.
   - **Postal.** Enter the project's postal code.
   - **Country.** Enter the project's country.
   - **Estimated Average Rate.** Enter the project's average rate per hour.
   - **Project Color.** Select the project's color.
   - **Custom Fields.** Custom fields you created for projects appear at the bottom. See [Configure Custom Fields for Resource Planning](/product-manuals/resource-planning-company/tutorials/configure-custom-fields-for-resource-planning).
5. Click **Create**.

   - If data sync is **enabled**:

     - Active projects created in Resource Planning are automatically synced and available in the Portfolio tool and can be used with other Procore tools.
     - Only some information synced between Resource Planning and the Portfolio tool. See [What project information is synced between Resource Planning and Procore Projects?](/faq-what-project-information-is-synced-between-resource-planning-and-procore-projects)
   - If data sync is **disabled**:

     - Projects are not synced to Procore.
     - To see projects in the Portfolio tool, you must manually [create new projects in the Portfolio tool.](/product-manuals/portfolio-company/tutorials/create-a-new-project)
     - Projects created in the Portfolio and the Resource Planning tools are managed independently.