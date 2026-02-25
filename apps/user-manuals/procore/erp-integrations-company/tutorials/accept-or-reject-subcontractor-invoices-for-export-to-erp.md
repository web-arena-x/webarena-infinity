# Accept or Reject Subcontractor Invoices for Export to ERP

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/accept-or-reject-subcontractor-invoices-for-export-to-erp

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

After a user sends an invoice to the ERP Integrations tool for accounting acceptance, an accounting approver has the option to 'Accept' or 'Reject' the invoice.

## Things to Consider

- **Required User Permissions**:

 - You need both:

    - 'Standard' or 'Admin' on the company's ERP Integrations tool.
    - The person's account must be granted the 'Can Push to Accounting' privilege in the Company Directory. See [Grant Accounting Approver Privileges](/product-manuals/erp-integrations-company/tutorials/grant-accounting-approver-privileges).

## Steps

- Review an Invoice
- Accept an Invoice
- Reject an Invoice

### Review an Invoice

1. Navigate to the company's **ERP Integrations** tool.
2. Click the **Subcontractor Invoices** tab. 
   *Note*: If your web browser is minimized, click the **More** link and select **Subcontractor Invoices** from the list.
3. Under **Filter Invoices By**, make sure the **Ready to Export** link is highlighted. 
   The page that appears lists only the invoices that have been sent to the ERP Integrations tool for accounting acceptance.
4. Continue with one of the following:

   - Accept an Invoice
   - Reject an Invoice

### Accept an Invoice

1. Select the invoices you want to accept for export.
2. Click **Export**. 
   This sync process typically takes a few minutes.

   - If an invoice fails to export, you can view the failed item(s) by clicking the **Failed to Export** link in the Views menu in the right pane.

### Reject an Invoice

1. Select the invoices you want to reject.
2. Enter the reason(s) for rejecting the invoice in the **Reason** box. Then, click **Reject**. 
   The following events occur:

   - The system removes the invoice from the ERP Integrations tool and returns it to an editable state in the project's Commitments tool in the Invoices tab.
   - The system sends an automated email notification to the user who created the invoice to alert this person of the 'Reject' response.