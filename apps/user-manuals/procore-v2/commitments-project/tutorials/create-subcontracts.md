# Create Subcontracts

Source: https://v2.support.procore.com/product-manuals/commitments-project/tutorials/create-subcontracts

---

## Background

Subcontracts can be awarded during both the preconstruction and construction phases of a project and are typically created and tracked in Procore by project management. After a prime contract award, the project manager creates purchase orders and subcontracts for specific trades to secure materials and subcontractor services for a project.

## Things to Consider

- **Required User Permissions:**

 - *To create a subcontract and see/enter data on the* ***Schedule of Values (SOV)*** *tab:*

    - **Admin** level permissions on the project's Commitments tool.
    - **Standard** level permissions on the project's Commitments tool and the **Allow Users to See SOV Items** setting must be enabled and your name must be selected in the **Select a Person** drop-down list.
 - *To create a subcontract only*, **Read Only** or **Standard** level permissions on the project's Commitments tool with the ['Create Work Order Contract' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.
- **Additional Information:**

 - An alternative way to create a subcontract is to award a winning bid and convert it into a subcontract. See [Award a Winning Bid and Convert it into a Subcontract](/product-manuals/bidding-project/tutorials/award-a-winning-bid-and-convert-it-into-a-subcontract).
 - To set the accounting method for the subcontract, see [How do I set the accounting method for a contract or funding?](/faq-how-do-i-set-the-accounting-method-for-a-contract-or-funding)
 - After creating a subcontract, you have these options for creating change orders:

    - If your subcontract is configured for [1-Tier Change Orders](/faq-what-are-the-different-change-order-tier-settings-in-project-financials). Continue with [Create a Commitment Change Order](/process-guides/materials-user-guide-with-financials/create-a-change-order-cco).
    - If your subcontract is configured for [2-Tier Change Orders](/faq-what-are-the-different-change-order-tier-settings-in-project-financials). Ensure the subcontract is in the 'Approved' status and continue with [Create a Commitment Potential Change Order from a Change Event](/product-manuals/change-events-project/tutorials/create-a-commitment-potential-change-order-from-a-change-event).
    - If your subcontract is configured for [3-Tier Change Orders](/faq-what-are-the-different-change-order-tier-settings-in-project-financials). Ensure the subcontract is in the 'Approved' status and continue with [Create a Commitment Potential Change Order from a Change Event](/product-manuals/change-events-project/tutorials/create-a-commitment-potential-change-order-from-a-change-event).
 - **For companies using the** **ERP Integrations tool:** Prerequisites, requirements, limitations, and considerations might apply depending on the ERP system your Procore account is integrated with.

## Prerequisites

- [Configure Settings: Commitments](/product-manuals/commitments-project/tutorials/configure-advanced-settings-commitments)
- To use the Procore + DocuSignÂ® integration to request signatures, see [DocuSignÂ®](/product-manuals/docusign/tutorials/link-your-docusign-account-to-a-procore-project).

## Steps

1. Navigate to the project's **Commitments** tool.
2. On the **Contracts** tab, click the **Create** button and choose **Subcontract** from the drop-down list.
3. Continue with the next steps:

   - Add the Basic Information
   - Update the General Information
   - Update the Contract Access
   - Update the Contract Dates
   - Add the Scope of Work
   - Set the Accounting Method
   - Update the Schedule of Values

     - Add Line Items to the Schedule of Values
     - Import Line Items to the Schedule of Values from a CSV File
   - Attach Files
   - Save the Contract

#### Add the Basic Information

Update the basic information as follows:

##### Â Notes

- There are no required fields when adding the basic information.
- If you click the **Create** button without completing any data entry, Procore saves the contract, lists you as the creator, and automatically places it in the *Draft* status.

- **Contract Number**To number your contract(s), choose from these options:

 - If you number your contracts using a sequential numbering system, you can enter any combination of alpha-numeric characters in this box. For subsequent contracts, Procore automatically applies consecutive numbering in ascending order.

    ##### Example

    The examples below show you how Procore's ascending consecutive numbering works:

    - If the previous contract was 1, the next contracts are 2, 3, and so on.
    - If the previous contract was PC-0001, the next contracts are PC-0002, PC-0003, and so on.
    - If the previous contract was DCA00010-12-G-0001, the next contracts are DCA00010-12-G-0002, DCA00010-12-G-0003, and so on.

- If you do NOT number your contracts using sequential numbering, you can manually enter a unique number for each prime contract. To do this, type over the existing entry in the **Number** box. Duplicate contract numbers are NOT permitted.
- **Contract Company**Select the name of the project owner's or the project client's company from the drop-down list. This is the company that either owns the construction project or the client who has hired your company to oversee the project work. To appear as a list option, [Add a Company to the Project Directory](/product-manuals/directory-project/tutorials/add-a-company-to-the-project-directory).
- **Title** Type a descriptive name for the contract.
- *Optional:* **Sign with DocuSignÂ®**Move this toggle to the right to collect signatures with the Procore + DocuSignÂ® integration. To learn how to activate the integration in Procore, see [Enable or Disable the DocuSignÂ® Integration on a Procore Project](/product-manuals/admin-project/tutorials/enable-or-disable-the-docusign-integration-on-a-procore-project).

 ##### Â Tip

 **How do you collect signatures with DocuSign?** After the data entry for the item is complete, Procore recommends changing the item's status to 'Out for Signature' before clicking the **Complete with DocuSign** button to launch the DocuSignÂ® application. If you have not previously signed in, you will be prompted to [Log In to DocuSignÂ®](/product-manuals/docusign/tutorials/log-in-to-docusign). Once you are signed in, you can prepare the DocuSign\_Â®\_ envelope for signatures. After the signature process is complete, Procore automatically changes the status of the item to 'Approved' and marks the item as 'Executed'. To learn more, see [DocuSignÂ®](/product-manuals/docusign/).