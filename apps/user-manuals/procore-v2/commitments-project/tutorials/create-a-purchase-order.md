# Create a Purchase Order (Legacy)

Source: https://v2.support.procore.com/product-manuals/commitments-project/tutorials/create-a-purchase-order

---

##### Â Legacy Content

This tutorial details Procore's legacy experience for creating a purchase order. The information on this page will be replaced with updated content when the redesigned commitments beta experience is generally available. To learn about this release and its timeline, see [Project Financials: Modernized Experience for Commitments](https://support.procore.com/tc/procore/Legacy/Release%5FDocumentation%5FArchives/2022/Project%5FFinancials:%5FModernized%5FExperience%5Ffor%5Fthe%5FCommitments%5FTool).

***Important!*** If you are using the commitments beta experience, please see the [Create Purchase Orders](/process-guides/materials-user-guide-with-financials/create-a-purchase-order) tutorial instead of the information below.

## Background

In Procore, a *Purchase Order (PO)* is a documented financial *commitment* that details the types, quantities, and agreed-upon prices for products or services. As part of the procurement process, purchase orders are created by a 'buyer' (for example, a *general contractor*) and issued to a 'seller' (for example, a *subcontractor*) to cover the cost of a contract. Once accepted by the 'seller,' a purchase order represents an agreement between the two parties

## Things to Consider

- **Required User Permissions:**

 - *To create a purchase order and see/enter data on the Schedule of Values:*\* 'Admin' level permissions on the project's Commitments tool.   
     OR\* 'Standard' level permissions on the project's Commitments tool and the 'Allow Users to See SOV Items' setting must be enabled and your name must be selected in the 'Select a Person' drop-down list
 - *To create a purchase order only*, 'Read Only' or 'Standard' level permissions on the project's Commitments tool with the ['Create Purchase Order Contract' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.
- **Additional Information:**

 - Purchase orders can be transitioned into a Change Order Request (for 1-tier Change Orders) or into a Potential Change Order (for 3-tier Change Orders).
 - You can only create a Potential Change Order from a Purchase Order that's in the 'Approved' status.
 - To learn how to set the accounting method, see [How do I set the accounting method for a contract or funding?](/faq-how-do-i-set-the-accounting-method-for-a-contract-or-funding)
- **For companies using the** **ERP Integrations tool:** Prerequisites, requirements, limitations, and considerations might apply depending on the ERP system your Procore account is integrated with.

## Prerequisites

- [Configure Settings: Commitments](/product-manuals/commitments-project/tutorials/configure-advanced-settings-commitments)

## Steps

- Step 1: Create a Purchase Order
- Step 2: Enter the Schedule of Values (SOV)

### Step 1: Create a Purchase Order

1. Navigate to the project's **Commitments** tool.
2. Choose an option to begin creating a purchase order:

   - If this is the first commitment for the project, click **+ Create** and select **Purchase Order** from the drop-down menu in the center of the page.
   - If you have already created the first commitment, click **+ Create** and select **Purchase Order** from the drop-down menu in the top right corner of the page.

     ##### Â Note

     - The **Create** button is available when you are viewing the Contracts and Recycle Bin tabs. New purchase orders are always added to the Contracts tab.
     - The **Export** button is only available on the Contracts tab. To learn more, see [Export a Commitments List](/product-manuals/commitments-project/tutorials/export-a-commitments-list).

- In the 'New Purchase Order' page under **General Information**, do the following:

 - **Sign with DocuSign** If your project is using the Procore + DocuSignÂ® integration (see [Enable or Disable the DocuSignÂ® Integration on a Procore Project](/product-manuals/admin-project/tutorials/enable-or-disable-the-docusign-integration-on-a-procore-project)), a checkmark appears in this box by default. If you do NOT want to sign the purchase order with DocuSignÂ®, remove the checkmark.

    ##### Â Tip

    **How do you collect signatures with DocuSign?** After the data entry for the item is complete, Procore recommends changing the item's status to 'Out for Signature' before clicking the **Complete with DocuSign** button to launch the DocuSignÂ® application. If you have not previously signed in, you will be prompted to [Log In to DocuSignÂ®](/product-manuals/docusign/tutorials/log-in-to-docusign). Once you are signed in, you can prepare the DocuSign\_Â®\_ envelope for signatures. After the signature process is complete, Procore automatically changes the status of the item to 'Approved' and marks the item as 'Executed'. To learn more, see [DocuSignÂ®](/product-manuals/docusign/).