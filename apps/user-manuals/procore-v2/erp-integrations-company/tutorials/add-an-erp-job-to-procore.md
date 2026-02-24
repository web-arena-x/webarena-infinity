# Add an ERP Job to Procore

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/add-an-erp-job-to-procore

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

If you first created a construction job in your ERP system, you may use the steps below to add it to Procore. This creates a new Procore project that contains all of the relevant job information for your ERP system.

## Things to Consider

- **Required User Permissions**:

 - 'Standard' level permission or higher on the ERP Integrations tool plus ONE of the following:\* 'Admin' level permissions on the company's Directory tool. 
     OR\* The user must be granted the 'Create a New Project' privilege. See [Allow Users to Create New Projects](/product-manuals/directory-company/tutorials/allow-users-to-create-new-projects).

## Steps

1. Navigate to the **ERP Integrations** tool.
2. Click the **Jobs** tab.
3. Under **Filter Jobs By**, click **Ready to Import**. 
    This reveals a list of all your ERP system jobs that have not yet been imported to Procore. The Ready to Import list summarizes jobs by *Project Name*.
4. Locate the job that needs to be imported to Procore. 
   (*Note*: If you have a long list of projects, use the advanced search and filter options).
5. If you want to apply a Procore project template to the new project, select one from the **Procore Project Template** list. See [Configure a Project Template](/product-manuals/portfolio-company/tutorials/configure-a-project-template).   
    Note: If the project template does not appear in the list, please verify the following:

   - The project has been marked as a template.
   - The 'Allow Project to be synced with ERP' checkbox must be checked in the Project Admin tool under ERP Integration Settings.
6. Click **Add to Procore**. 
    This syncs the data from the job in your ERP system with the Procore project.
7. After the sync is complete, click the **Synced** link in the 'Filters' menu to view the newly created Procore project. 
   *Note*: The name of the job in your ERP system is used as the Procore project name.