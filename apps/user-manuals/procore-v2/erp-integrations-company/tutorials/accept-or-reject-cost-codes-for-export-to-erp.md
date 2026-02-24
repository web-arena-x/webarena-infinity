# Accept or Reject Cost Codes for Export to ERP

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/accept-or-reject-cost-codes-for-export-to-erp

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

After adding cost codes as segment items in the Work Breakdown Structure area of the Company level Admin tool, you can then send the codes to the ERP Integrations tool where they can be accepted or rejected by an 

In Procore, an *Accounting Approver* is an individual with the authority to accept and reject Procore data for export to an integrated ERP system. Accounting approvers can unlink several item types, such as commitments, commitment change orders, prime contract change orders, and subcontractor invoices, that have been synced between Procore and an integrated ERP system. See [Which ERP Integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

Accounting Approver. The accountant then has the option to 'Accept' or 'Reject' the code(s) as follows:

- **Accept**. An 'Accept' response exports the Company level cost codes from Procore and creates new codes in your ERP system.
- **Reject**. A 'Reject' response removes the cost codes from the ERP Integrations tool's 'Ready to Export' list and places it into an editable state in the project's Admin tool for updating (see [Add Segment Items](/process-guides/company-administration-work-breakdown-structure-guide/add-segment-items) or [Import Segment Items into your Company Level Admin Tool](/product-manuals/procore-imports/tutorials/import-segment-items-into-your-company-level-admin-tool-procore-imports)).

If there is at least one (1) item awaiting accounting approval in the ERP Integrations tool's 'Ready to Export' view, accounting approvers will receive one automated email notification per day with the Subject Line "ERP Integrations Daily Summary" until all items in the 'Ready to Export' view have been accepted or rejected.

## Things to Consider

- **Required User Permissions**:

 - You need both:

    - 'Standard' or 'Admin' on the company's ERP Integrations tool.
    - The person's account must be granted the 'Can Push to Accounting' privilege in the Company Directory. See [Grant Accounting Approver Privileges](/product-manuals/erp-integrations-company/tutorials/grant-accounting-approver-privileges).
- **Prerequisites**:

 - [Configure Cost Code Preferences for ERP](/product-manuals/erp-integrations-company/tutorials/configure-cost-code-preferences-for-erp)
 - [Send Unsynced ERP Standard Cost Codes to ERP Integrations for Accounting Acceptance](/product-manuals/erp-integrations-company/tutorials/send-unsynced-erp-standard-cost-codes-to-erp-for-accounting-acceptance)

## Steps

### Accept the Cost Code

1. Navigate to the company's **ERP Integrations** tool.
2. Click the **Standard Cost Codes** tab.
3. Under **Filter Standard Cost Codes By**, make sure **Ready to Export** is selected.
4. Review any cost code(s) and descriptions in the 'ERP Cost Code List'.   
    This list only shows unsynced cost codes.
5. Select an option in the following drop-down lists:

   - **General Ledger Account - Income**. Choose the appropriate income account for each cost code. An *income account* is used for revenues, expenses, gains, and losses.
   - **General Ledger Account - Expense (Optional)**. If your company uses separate expense accounts, choose one from this list.   
     *Note*: Any changes you make will automatically be saved.
6. Click **Export Cost Codes**.
7. The 'Export Status' column in the ERP Cost Code list shows the status of your export. It may take a few minutes to export your codes. When the export is complete, the column reads 'Success.'

### Reject the Cost Code

1. Navigate to the **ERP Integrations** tool.
2. Click the **Standard Cost Codes** tab.
3. Under **Filter Standard Cost Codes By**, make sure **Ready to Export** is selected.
4. Review the code(s) in the 'ERP Cost Code List'.   
    This list only shows unsynced cost codes.
5. Click **Reject All**. 
      
      
    The system removes the codes from the "Ready to Export" list in the ERP Integrations tool. A YELLOW banner appears at the top of the page to confirm that the code(s) have been removed.