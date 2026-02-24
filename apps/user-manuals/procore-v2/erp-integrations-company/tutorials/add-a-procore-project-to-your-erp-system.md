# Add a Procore Project to your ERP System

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/add-a-procore-project-to-your-erp-system

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

Some ERP integrations allow you to create a new project in Procore and send it to your company's ERP Integrations tool to be reviewed and exported by an accounting approver. If approved and exported, Procore sends the project and some of its data to your ERP system.

After an 

In Procore, an *Accounting Approver* is an individual with the authority to accept and reject Procore data for export to an integrated ERP system. Accounting approvers can unlink several item types, such as commitments, commitment change orders, prime contract change orders, and subcontractor invoices, that have been synced between Procore and an integrated ERP system. See [Which ERP Integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

Accounting Approver reviews and accepts the Procore project for export to your ERP system in the Company level ERP Integrations tool, the project is exported during the synchronization process.

Not all integrations support syncing a new project from Procore to your ERP system. Some integrations require project creation to take place in your ERP system.

## Things to Consider

- **Required User Permissions**:

 - You need both:

    - 'Standard' or 'Admin' on the company's ERP Integrations tool.
    - The person's account must be granted the 'Can Push to Accounting' privilege in the Company Directory. See [Grant Accounting Approver Privileges](/product-manuals/erp-integrations-company/tutorials/grant-accounting-approver-privileges).
- **Requirements**:

 - You must select the 'ERP Standard Cost Codes' list for use on your new project.
 - All cost codes must have at least one (1) cost type assignment.
 - If your cost codes already have cost type assignments, your company has already configured the cost type assignments for your cost codes.
 - When entering your project data, be aware of the following requirements:

    - **Project Name**. Your ERP integration may impose a character limit on the Project Name field. If your project name exceeds this limit, your project name might be truncated in your ERP system, or your project may not export successfully.
    - **Active Project**. Your new project must be marked as 'Active' in Procore.

## Steps

1. Create a New Project
2. Add the 'ERP Cost Codes' list to your Procore project.
3. Assign default cost types to cost codes.
4. Send your new project to the ERP Integrations tool for accounting acceptance.

### Create a New Project

#### Launch the Project Creation Assistant

1. Navigate to the company's **Portfolio** tool.
2. Click **Create Project**.

#### Add Project Details

1. Make sure **Project Details** is highlighted in the right sidebar.

   - Enter all of your project's information, like address, project name, and other general information. For detailed descriptions of all available fields, see [Create a New Project](/product-manuals/portfolio-company/tutorials/create-a-new-project).

### ERP Project Creation

Under **ERP Integration**, do the following (*Note: this step is only relevant to companies that are integrated with certain ERP systems*):

1. **Allow project to be synced with ERP**. Leave this checkbox marked if you plan to sync any part of the project's financials with your ERP software. This will ensure that the ERP Standard cost code list will be available to select from when configuring your Project Level cost codes.

##### Â Important

- This checkbox will be marked by default if your company has an available set of ERP cost codes, unless the template the project is created from does not have this box marked.
- If you plan to sync your new Procore project with your ERP software you MUST leave this checkbox marked. If you un-mark this box, you will not be able to re-mark it later if cost codes from a different Company Level list have been copied to the Project Level list in the Project Admin tool.

2. Click **Create Project**.

- If you applied a project template and the template defines the desired project tools, you will move on to Add Project Cost Codes.
- If you did not apply a project template or your template does not define the desired project tools, you will be prompted to choose the tools that you'll use on your new project before you can add cost codes.

### Add ERP Standard Project Cost Codes

1. Make sure that **Cost Code** is highlighted in the right sidebar. This reveals the cost code page for your new project.

   ##### Â Important

   - You must select cost codes from the ERP Standard Cost Codes list to be able to sync your project with your ERP system.
   - If you select a non-ERP cost code list your project will NOT sync successfully.