# Accept or Reject a Commitment for Export to ERP

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/accept-or-reject-a-commitment-for-export-to-erp

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

After sending a commitment to your company's ERP Integrations tool, a designated accounting approver has the option to 'Accept' or 'Reject' it for export to your ERP system.

## Things to Consider

- **Required User Permissions**:â

 - You need both:

    - 'Standard' or 'Admin' on the company's ERP Integrations tool.
    - The person's account must be granted the 'Can Push to Accounting' privilege in the Company Directory. See [Grant Accounting Approver Privileges](/product-manuals/erp-integrations-company/tutorials/grant-accounting-approver-privileges).

## Steps

### Review a Commitment

1. Navigate to the company's **ERP Integrations** tool.
2. Click the **Commitments** subtab.
3. In the 'Views' menu, click the **Ready to Export** link.   
    This page that appears lists only the commitments that have been sent to the ERP Integrations tool for accounting approval.
4. Continue with one of the following:

   - âAccept a Commitment
   - Reject a Commitment

### Accept a Commitmentâ

1. Locate the commitment in the 'Commitments - Ready to be Exported' list.
2. Choose the **Accept** option.
3. Click **Export**.   
    The export process typically takes a few minutes.   
   *Note: If for any reason a commitment fails to export, you can view the failed item(s) by clicking the Failed to Export menu option. If an export fails, follow the steps in Reject a Commitment and then* [Re-send a Rejected Commitment to ERP](/product-manuals/erp-integrations-company/tutorials/resend-a-rejected-commitment-to-erp-integrations-for-accounting-acceptance)*.*
4. (Optional) To verify that the sync was successful, log into your ERP system and verify that your data appears as expected.

### Reject a Commitment

1. Locate the commitment in the **Commitments - Ready to be Exported** list.
2. Choose **Reject**.
3. Enter a short explanation about the reason(s) for the rejection.
4. Click **Reject**. 
    The following events occur:

   - The system removes the commitment from the ERP Integration tool and returns it to an editable state in the project's Commitments tool.
   - The system sends an automated email notification to the creator of the commitment. This alerts that person of the 'Reject' response.