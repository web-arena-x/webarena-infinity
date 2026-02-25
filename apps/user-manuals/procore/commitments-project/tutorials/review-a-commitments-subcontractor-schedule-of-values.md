# Review a Subcontractor SOV for a Commitment

Source: https://v2.support.procore.com/product-manuals/commitments-project/tutorials/review-a-commitments-subcontractor-schedule-of-values

---

## Background

A *Subcontractor Schedule of Values (Subcontractor SOV)* on a commitment is typically completed when the upstream contractor (for example, a general contractor) requires a detailed line-item breakdown of work performed by a downstream contractor (for example, a subcontractor).

In Procore, the Subcontractor SOV tab is enabled on the project's Commitments tool by default. This tab provides downstream contractors with the ability to provide detailed line items for work performed to upstream contractors. It also ensures that subcontractors do not modify the line items on the general 'Schedule of Values' tab. This is because the intent of a commitment's general SOV tab is to a line item that shows the contract amount for each cost code and cost type.

For the Subcontractor SOV tab, a general contractor sends a request that the subcontractor to add line items to the Subcontractor SOV when the general contractor requires additional information about the subcontractor's payment for work performed. The Subcontractor SOV can then be reviewd and approved by the general contractor.

## Things to Consider

- **Required User Permissions:**

 - You must be an [invoice administrator](/process-guides/payor-setup-guide/add-invoice-administrators).
- **Additional Information:**

 - If you are listed in the Invoice Distribution of the Commitments tool, when a subcontractor SOV is submitted for the commitment, you and other users listed in the Invoice Distribution list will receive an email notification that the Subcontractor Schedule of Values has been submitted by the subcontractor once the status of the subcontractor SOV is set to 'Under Review.' See [Configure Settings: Commitments](/product-manuals/commitments-project/tutorials/configure-advanced-settings-commitments).

## Prerequisites

- The Subcontractor SOV tab must be enabled. See [Enable or Disable the Subcontractor SOV Tab on a Commitment](/product-manuals/commitments-project/tutorials/enable-or-disable-the-ssov-tab-on-a-commitment).
- Add the line items to review to the Subcontractor SOV. This can be performed by the upstream or downstream contractor.

 - If you are the upstream contractor (for example, the general contractor), see [Add a Subcontractor SOV to a Commitment](/product-manuals/commitments-project/tutorials/add-a-subcontractor-sov-to-a-commitment).
 - If you are the downstream contractor (for example, the subcontractor), see [Update the Subcontractor SOV as an Invoice Contact from the Commitments Tool](/product-manuals/commitments-project/tutorials/update-a-subcontractor-schedule-of-values-as-an-invoice-contact-from-the-commitments-tool).

## Steps

1. Navigate to the project's **Commitments** tool.
2. Under the **Contracts** tab, locate the purchase order or subcontract. Then click **Edit**.
3. Click the **Subcontractor SOV** tab.
4. *Optional:* To edit the line items on the Subcontractor SOV tab, click **Edit**.
5. Review the line items on the Subcontractor SOV tab. Then choose from these options:

   - To approve the Subcontractor SOV, change the status to 'Approved.'
   - To reject the Subcontractor SOV and have the downstream contractor edit the line items, click 'Revise & Resubmit.'
6. Click **Submit**.