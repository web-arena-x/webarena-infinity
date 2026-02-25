# Add ViewpointÂ® SpectrumÂ® Standard Cost Codes to a Project

Source: https://v2.support.procore.com/product-manuals/viewpoint-spectrum/tutorials/add-viewpoint-spectrum-standard-cost-codes-to-a-project

---

## Background

During the course of a construction project, commitments, and commitment changes orders get created. When this happens, the need to add new cost codes to the Procore project might arise. When you create new cost codes in ViewpointÂ® SpectrumÂ®, the integration syncs those codes with Procore's company level cost codes. You can then use the steps below to copy all the new codes to your Procore project.

## Things to Consider

- **Required User Permissions**:

  - You need one of the following:

    - *To add or edit project cost codes*, 'Admin' on the project's Admin tool.
    - *To add or edit project cost codes as a user with 'Standard' or 'Read Only' level permission to the project's Admin tool*, the 'Manage Cost Codes' granular permission must be enabled on the permission template associated with your user account on the project.
- **Prerequisites**:

  - The ERP Integrations tool must be enabled on the project.
  - The ViewpointÂ® SpectrumÂ® job must be added to Procore.

## Steps

- Add ViewpointÂ® SpectrumÂ® Standard Cost Codes to a Project
- Update the Project Cost Codes Cost Type Assignment
- Resend the Project Cost Codes to ERP Integrations

### Add ViewpointÂ® SpectrumÂ® Standard Cost Codes to a Project

1. Navigate to the Project level **Admin** tool.
2. Under 'Project Settings', click the **Work Breakdown Structure** link.
3. In the 'Segments' list, click the **Cost Codes** link.
4. Click **Cost Codes from Company**.
5. In the 'Add Cost Codes to this Project' window, choose from these options:

   - To copy all company cost codes to the project, click **Select All**.
   - To select specific cost codes, type a code in the **Search Cost Codes** box and highlight the codes to add.
   - To choose cost codes, expand the desired segment items and highlight the segment items to copy.
6. Click **Add**.

### âUpdate the Project Cost Codes Cost Type Assignment

1. Navigate to the project's **Admin** tool.  
   This reveals the 'General Project Information' page.
2. Under **Project Settings**, click **Cost Code Cost Type Assignments**. This reveals the 'Cost Code Cost Type Assignments' page.
3. For every cost code in your project's list, mark one or more checkboxes to assign the code to a cost type (or cost types).

       

   *Note*: This cost type abbreviations in this list are populated with the abbreviations that have been imported from ViewpointÂ® SpectrumÂ®.
4. Click **Save**.
5. Continue with Resend the Project Cost Codes to ERP Integrations.

### Resend the Project Cost Codes to ERP Integrations

Now that you've added the new cost code(s) and updated the cost type assignment(s) in the Admin tool, you'll need to send those changes to the **ERP Integrations** tool so it can be reviewed by an 

In Procore, an *Accounting Approver* is an individual with the authority to accept and reject Procore data for export to an integrated ERP system. Accounting approvers can unlink several item types, such as commitments, commitment change orders, prime contract change orders, and subcontractor invoices, that have been synced between Procore and an integrated ERP system. See [Which ERP Integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

Accounting Approver.

1. Do one of the following:

   - Navigate to the **Admin** tool.
   - Under 'Project Settings', click **General**.
2. Under the 'Project Settings' menu in the right pane, click **General**.   
   *Note*: A banner appears across the top of the page to notify you when a project has new cost codes or cost types that need to be synced with ViewpointÂ® SpectrumÂ®.
3. Click **Re-send to ERP**.

       

   âProcore sends the new cost code and cost type data to the ERP Integrations tool. A banner appears across the top of the page to indicate that the project data in the Admin tool is currently being reviewed by an accounting approver. While the project data is being reviewed, users cannot make changes in the Admin tool.

## Next Step

- [Update Project Cost Codes for Export to ViewpointÂ® SpectrumÂ®](/product-manuals/viewpoint-spectrum/tutorials/update-project-cost-codes-for-export-to-viewpoint-spectrum)