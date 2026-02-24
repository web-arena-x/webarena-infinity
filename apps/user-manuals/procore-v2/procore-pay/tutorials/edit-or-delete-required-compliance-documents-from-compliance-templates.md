# Edit or Delete Required Compliance Documents from Compliance Templates

Source: https://v2.support.procore.com/product-manuals/procore-pay/tutorials/edit-or-delete-required-compliance-documents-from-compliance-templates

---

##### Â General Availability in Select Markets (United States)

[Procore Pay](https://www.procore.com/pay)  is available in the United States. It is designed for General Contractors and Owner-Builders who act as their own General Contractors on a job. Procore Pay extends the [Invoice Management](https://www.procore.com/invoice-management) functionality in the Procore web application to handle the payment process between general and specialty contractors.

## Background

Company Admins can edit or delete a compliance template at any time.

## Things to Consider

- [Required User Permissions](/product-manuals/procore-pay/permissions)
- **Additional Information**:

  - Compliance templates are only available with Procore Pay.
  - You can create multiple compliance templates to assign to your Procore projects. However, you can only assign one (1) template to a project.

## Prerequisites

- [Create Compliance Templates for Commitments as a Company Admin](/process-guides/about-the-compliance-tab-on-subcontractor-invoices-with-procore-pay/create-templates)
- [Add Required Compliance Documents to Compliance Templates](/process-guides/about-the-compliance-tab-on-subcontractor-invoices-with-procore-pay/add-requirements)

## Steps

- Edit a Required Compliance Document
- Delete a Required Compliance Document

### Edit a Required Compliance Document

1. Navigate to the Company level **Admin** tool.
2. Under **Tool Settings**, choose the option available in your project:

   - Click the **Contracts** tab.  
      OR
   - If you have the Change Management tools enabled, click the **Contracts and Change Orders** tab.
3. Click **Compliance Templates**.
4. Locate the template to update and choose one of these options:

   - **Manage**. Click this button to open the template.  
      OR
   - **Template Name**. Click this button to open the template.
5. *(Optional)* In the **General Information** card, click **Edit** to change the template name. Then click **Save**.
6. In the **Required Compliance Documents** card, find the requirement to update and click **Edit**.  
    This opens the Edit Requirement panel.
7. In the **Document Details** card, do the following:

   - **Document Type**. Choose an option from the list: *Bond*, *Closeout*, *License*, *Master Agreement*, *Other*, *Payroll*, *Permit*, *Project Insurance*, *Safety*, *Stored Material*, or *W-9.*
   - **Document Name**. Type a name for the document.
8. In the **Criteria** card, choose the **Collect At** requirement to determine if Procore Pay tracks the requirement:

   - **Commitment**. Assign this to a *Purchase Order*, *Subcontract*, or both *Subcontract & Purchase Order*. To get email alerts for upcoming or past document expirations, mark the checkbox.  
      OR
   - **Invoice**. Choose the commitment type. Then, set the billing cycle: *First Billing*, *Every Progress Billing*, or *Final Billing*.
9. Click **Save**.  
    A green success banner appears to confirm the update.
10. Repeat the steps above to update other requirements.

### Delete a Required Compliance Document

1. Navigate to the Company level **Admin** tool.
2. Under **Tool Settings**, click **Contracts**.
3. Click **Compliance Templates**.
4. Locate the template to update and choose one of these options:

   - **Manage**. Click this button to open the template.  
      OR
   - **Template Name**. Click this button to open the template.
5. In the **Required Compliance Documents** card, locate the document to delete and click the **trash can**  icon.
6. In the **Delete Compliance Requirement?** prompt, click **Delete**.  
    A GREEN success banner confirms the delete action.

   ##### Â Caution

   The compliance requirement cannot be restored to the template ones its deleted. This modification only affects new commitments (or invoices) on projects configured to use this compliance template.

- Repeat the steps above to delete any additional compliance documents from the template.

  ##### Â Notes

  - Deleting a requirement from a template does NOT remove the requirement from any existing commitments or invoices.
  - As an invoice administrator, you can delete any requirement from an project commitment or invoice, whether it originated from a template or not.