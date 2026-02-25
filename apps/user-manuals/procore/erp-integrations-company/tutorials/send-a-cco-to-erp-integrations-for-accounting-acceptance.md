# Send a CCO to ERP for Accounting Acceptance

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/send-a-cco-to-erp-integrations-for-accounting-acceptance

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

When you create a CCO on a Procore project, the new CCO must be sent to the ERP Integrations tool in Procore for acceptance by an accounting approver. After acceptance, the system will export the CCO data to your integrated ERP system.

## Things to Consider

- **Required User Permissions**:

 - You need both:

    - 'Admin' on the project's Commitments tool.
    - 'Admin' on the project's Change Orders tool
- **Requirements**:

 - **Contract Company**. Must be an ERP-linked vendor in the Directory tool.
 - **Status**. Must be 'Approved.'
 - **Schedule of Values (SOV)**. Must include at least one (1) line item with an ERP Standard Cost Code.

## Steps

1. Navigate to the project's **Change Orders** tool.
2. Click the **Commitments** tab.
3. Locate the desired CCO in the list. Then click **View**.
4. If all the CCO data appears as desired, click **Send to ERP**.

   - The system sends the CCO to the ERP Integrations tool. The following fields are locked and cannot be edited after export:

     - Contract Company
     - Title
     - Status
     - Total Amount