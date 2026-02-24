# Accept or Reject a CCO for Export to ERP

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/accept-or-reject-a-cco-for-export-to-erp

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

After a user sends a CCO to the ERP Integrations tool for accounting acceptance, an accounting approver has the option to 'Accept' or 'Reject' the CCO for export to the ERP system.

## Things to Consider

- **Required User Permissions**:

 - You need both:

    - 'Standard' or 'Admin' on the company's ERP Integrations tool.
    - The person's account must be granted the 'Can Push to Accounting' privilege in the Company Directory. See [Grant Accounting Approver Privileges](/product-manuals/erp-integrations-company/tutorials/grant-accounting-approver-privileges).

## Steps

- Review a Commitment Change Order
- Accept a Commitment Change Order
- Reject a Commitment Change Order

### Review a Commitment Change Order

1. Navigate to the company's **ERP Integrations** tool.
2. In the ERP Integrations tool, click the **Change Orders** subtab.
3. In the 'Views' menu, click the **Ready to Export** link.   
    The page that appears lists only the CCOs that have been sent to the ERP Integrations tool for accounting acceptance.
4. Continue with one of the following:

   - âAccept a Commitment Change Order
   - Reject a Commitment Change Order

### Accept a Commitment Change Order

1. Locate the CCO in the 'Change Orders - Ready to be Exported' list.
2. Choose the **Accept** option.
3. If prompted, enter a description in the **Description** box.
4. Click **Export**.   
    This syncs the CCO with your ERP system. The process typically takes a few minutes.

   - If for any reason a CCO fails to export, you can view the failed item(s) by clicking the **Failed to Export**.
   - When a CCO fails to export, follow the steps in Reject a Commitment Change Order and then resend the CCO to ERP for acceptance.

### Reject a Commitment Change Order

1. Locate the CCO in the 'Change Orders - Ready to be Exported' list.
2. Choose **Reject**.
3. Enter a short explanation about the reason(s) for the rejection.
4. Click **Reject**.   
    The following events occur:

   - The system removes the CCO from the ERP Integrations tool and returns it to an editable state in the project's Change Orders tool and in the Commitments tool's Change Order subtab.
   - The system sends an automated email notification to the user who created the CCO to alert this person of the 'Reject' response.