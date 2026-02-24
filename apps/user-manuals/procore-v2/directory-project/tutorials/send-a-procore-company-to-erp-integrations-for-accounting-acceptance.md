# Send a Procore Company to ERP Integrations for Accounting Acceptance

Source: https://v2.support.procore.com/product-manuals/directory-project/tutorials/send-a-procore-company-to-erp-integrations-for-accounting-acceptance

---

##### Â In Beta

A redesigned version of the Project Directory is currently in beta and can be enabled with [Procore Explore](/product-manuals/admin-company/tutorials/manage-features-with-procore-explore).

## Background

If you have a company record in Procore that does not exist in your 

In Procore, the term *integrated ERP System*, is used to refer to *Enterprise Resource Planning (ERP)* software applications that can be configured to exchange data between Procore and a supported application using the Company level ERP Integrations tool. See [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

Integrated ERP System, you can export it. The first step is to locate the company record in Procore's Project level Directory tool. Next, send the record to the ERP Integrations tool where it can then be accepted for export by an accounting approver.

## Things to Consider

- [Required User Permissions](/product-manuals/directory-project/permissions)
- The entry in the 'Company Name' field is subject to maximum character length limits. For details, see [What is the maximum character length for a 'Company Name' in the Directory tool?](/faq-what-is-the-maximum-character-length-for-a-company-name-in-the-directory-tool)

## Steps

1. Navigate to the Project level **Directory** tool.
2. Click the **Companies** tab.
3. Click **Edit** next to the company. 
   OR Click the **company name**.
4. Review the record. 
   *Notes:*

   - If you want to make any changes, it is recommended that you modify and save them before sending the company record to the ERP Integrations tool for acceptance by an 

     In Procore, an *Accounting Approver* is an individual with the authority to accept and reject Procore data for export to an integrated ERP system. Accounting approvers can unlink several item types, such as commitments, commitment change orders, prime contract change orders, and subcontractor invoices, that have been synced between Procore and an integrated ERP system. See [Which ERP Integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

     Accounting Approver.
   - The entry in the 'Name' field is subject to the same maximum character length limits for the 'Company Name' field that appears when you first add a company to the Directory tool. For details, see [What is the maximum character length for a 'Company Name' in the Directory tool?](/faq-what-is-the-maximum-character-length-for-a-company-name-in-the-directory-tool)
5. Click **+Send to ERP**.

   *Notes*:

   - If the **Send to ERP** (or **Re-send to ERP**) button is grayed out and unavailable, hover your cursor over the question mark (?) to learn why. Typically, it's because the project's ERP data has not yet been synced or because the item does not meet the minimum requirements (see above).
   - If the **Retrieve from ERP** button appears, the data has already been sent to the ERP Integrations tool.

   The system sends the company record to the ERP Integrations tool for acceptance. Once accepted by an accounting approver, the system exports the company from Procore and then adds it as a vendor record in your third-party ERP system (e.g., Integration by Procore: ViewpointÂ® SpectrumÂ®, Integration by Procore: VistaÂ®, QuickBooksÂ®, Sage 100 ContractorÂ®, Sage 300 CREÂ®, etc.).

## Next Steps

- [Accept or Reject a Company for Export to ERP](/product-manuals/erp-integrations-company/tutorials/accept-or-reject-a-company-for-export-to-erp)