# Create a Commitment Change Order

Source: https://v2.support.procore.com/product-manuals/commitments-project/tutorials/create-a-commitment-change-order-cco

---

## Background

In Procore, 

In Procore, a *Purchase Order (PO)* is a documented financial *commitment* that details the types, quantities, and agreed-upon prices for products or services. As part of the procurement process, purchase orders are created by a 'buyer' (for example, a *general contractor*) and issued to a 'seller' (for example, a *subcontractor*) to cover the cost of a contract. Once accepted by the 'seller,' a purchase order represents an agreement between the two parties

Purchase Order and 

A Subcontract is a legal agreement where a party on a prime contract engages a third-party (the subcontractor) to perform all or part of the work defined in the prime contract.

Subcontract are called commitments. A *commitment* is a contractual agreement between a buyer (for example, a project owner, a general contractor, or a specialty contractor) and a seller (for example, a contractor, a subcontractor, or a vendor). The seller is responsible for completing project work or fulfilling an order for the buyer. When you need to alter the terms of the original agreement, you can create a commitment change order.

##### Â Important

**When the Change Events tool is enabled on a project**

The process that you will use to create a commitment change order in Procore depends upon a few factors. First, if the Change Events tool is disabled on the project, you will use one of the processes below. Also, keep in mind that the number of steps required to create a commitment change order is dependent upon the change order tier setting that is configured on the project's Commitments tool. See [Configure the Number of Commitment Change Order Tiers](/product-manuals/commitments-project/tutorials/configure-the-number-of-commitment-change-order-tiers):

- **1-Tier configuration:**

 1. Create a commitment change order as described below.
- **2-Tier configuration**

 1. Create a commitment potential change order
 2. Create a commitment change order

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Commitments tool
- **Additional Information:**

 - **If the Change Events tool is disabled on the project:**

    - The steps for creating a change order are determined by the number of change order tiers configured for the Commitments tool. See [What are the different change order tier settings in Project Financials?](/faq-what-are-the-different-change-order-tier-settings-in-project-financials) and [Configure the Number of Change Order Tiers](/product-manuals/commitments-project/tutorials/configure-the-number-of-commitment-change-order-tiers).
 - **If the Change Events tool is enabled on the project:**

    - The **Create Commitment CO** button is not available.
    - Instead, click **Create Change Event**.
    - Next, follow the steps in [Create a Change Event](/product-manuals/change-events-project/tutorials/create-a-change-event).
    - Then, follow the steps in [Create a Commitment Change Order from a Change Event](/product-manuals/change-events-project/tutorials/create-a-commitment-change-order-from-a-change-event).
- For companies using the ERP Integrations tool: **Show/Hide**

 - Additional requirements, considerations, and limitations vary depending on the ERP system your company's account is integrated with. Most ERP systems have limitations on the number of characters that can be used for a commitment's title. See [Things to Know About your ERP Integration](https://support.procore.com/products/online/user-guide/company-level/erp-integrations/things-to-know-about-your-erp-integration) for details.

## Prerequisites

- Create a Commitment
- *Optional:* [Complete a Commitment Contract with DocuSignÂ®](/product-manuals/commitments-project/tutorials/complete-a-commitment-contract-with-docusign)

## Steps

### Create a Commitment Change Order

If you have created a purchase order or a subcontract and need to alter the terms of that item, use the steps below to create a commitment change order.

1. Navigate to the project's **Commitments** tool.
2. Under **Contracts**, locate the commitment. Then click **Edit**.
3. Click **Create Commitment CO**.

   ##### Â Notes

   If the Change Events tool is enabled on your project, the **Create Commitment CO** button is not available. Follow these steps instead:

   - First, click **Create Change Event**.
   - Next, follow the steps in [Create a Change Event](/product-manuals/change-events-project/tutorials/create-a-change-event).
   - Then, follow the steps in [Create a Commitment Change Order from a Change Event](/product-manuals/change-events-project/tutorials/create-a-commitment-change-order-from-a-change-event).

 
- In the **General** tab, do the following:

 - **Sign with DocuSignÂ®**If you have enabled the Procore + DocuSignÂ® integration (see [Enable or Disable the DocuSignÂ® Integration on a Procore Project](/product-manuals/admin-project/tutorials/enable-or-disable-the-docusign-integration-on-a-procore-project)), a checkmark appears in this box by default. If you do NOT want to collect signatures with DocuSignÂ®, remove the mark.

    ##### Â Tip

    **How do you collect signatures with DocuSign?** After the data entry for the item is complete, Procore recommends changing the item's status to 'Out for Signature' before clicking the **Complete with DocuSign** button to launch the DocuSignÂ® application. If you have not previously signed in, you will be prompted to [Log In to DocuSignÂ®](/product-manuals/docusign/tutorials/log-in-to-docusign). Once you are signed in, you can prepare the DocuSign\_Â®\_ envelope for signatures. After the signature process is complete, Procore automatically changes the status of the item to 'Approved' and marks the item as 'Executed'. To learn more, see [DocuSignÂ®](/product-manuals/docusign/).