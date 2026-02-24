# Accept or Reject a Company for Export to ERP

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/accept-or-reject-a-company-for-export-to-erp

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

After sending a company record to your ERP Integrations tool, a designated accounting approver has the option to accept or reject it for export to your ERP system.

## Things to Consider

- **Required User Permissions**:

 - You need both:

    - 'Standard' or 'Admin' on the company's ERP Integrations tool.
    - The person's account must be granted the 'Can Push to Accounting' privilege in the Company Directory. See [Grant Accounting Approver Privileges](/product-manuals/erp-integrations-company/tutorials/grant-accounting-approver-privileges).

## Steps

1. Navigate to the company's **ERP Integrations** tool.
2. Click **Companies**.
3. Under **Filters**, click **Ready to Export**. 
   *Notes*:

   - This page only lists active company records. Inactive companies cannot be exported to an integrated ERP system.
   - If a company record is not listed here, check to see if it is inactive. See [Deactivate a Company in the Company Directory](/product-manuals/directory-company/tutorials/inactivate-a-company-in-the-company-directory).
4. Review the companies in the list. Then do the following:

   - Accept the Company
   - Reject the Company

### Accept the Company

1. Locate the company record to export in the '**Companies Only in Procore**' list. To view the company record, click the company name hyperlink.

   ##### Â Notes

   - If the company record you want to export is not listed, check to see if the record was marked *Inactive* in Procore.
   - This page only lists *Active* company records in Procore.
   - Company records marked *Inactive* cannot be exported to the 

     In Procore, the term *integrated ERP System*, is used to refer to *Enterprise Resource Planning (ERP)* software applications that can be configured to exchange data between Procore and a supported application using the Company level ERP Integrations tool. See [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

     Integrated ERP System. See [Deactivate a Company in the Project Directory](/product-manuals/directory-project/tutorials/deactivate-a-company-in-the-project-directory).

- Choose **Accept**.
- In the **Company Type** drop-down list, select the company type. For example, if the record is for a subcontractor, select *sub*.
- Select the company type from the **Company Type** drop-down list.
- Enter the Company ID from your ERP.

 ##### Â Notes

 - You must enter a unique ERP Company ID in this field.
 - In your ERP system, a unique company number is assigned to a new record using the numbering system established by your company. Some companies enter the next available number in a sequence, while others use an alphabetical characters to represent the customer name (for example, All Star Concrete = ASC).
 - If your ERP Company ID entry in Procore has already been assigned to a record in your ERP system, the integration will NOT export the record.