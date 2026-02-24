# Edit Subcontracts

Source: https://v2.support.procore.com/product-manuals/commitments-project/tutorials/edit-subcontracts

---

## Background

After you create a subcontract, you can edit it at any time.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Commitments tool. 
    OR
 - 'Read Only' or 'Standard' level permissions on the project's Commitments tool with the ['Update Work Order Contract'](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) granular permissions enabled on your permission template.
- For companies using the ERP Integrations tool: **Show/Hide**

 - If you are editing a subcontract that has NOT yet been synced with your company's [integrated ERP system](/glossary-of-terms), you may use the steps below. To determine if a subcontract has been synced with an ERP system, see [What do the ERP Icons mean?](/product-manuals/commitments-project/tutorials/edit-a-commitment)
 - If you are editing a subcontract that has already been synced with your company's integrated ERP system, see [Edit a Commitment Synced with ERP](/product-manuals/erp-integrations-company/tutorials/edit-a-commitment-synced-with-erp).

## Prerequisites

- [(Beta) Create Subcontracts](/product-manuals/commitments-project/tutorials/create-subcontracts)

## Steps

1. Navigate to the project's **Commitments** tool.
2. On the **Contracts** tab, locate the contract to edit and click its **Number** link.
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
- **Contract Company**Select the name of the project owner's or the project client's company from the drop-down list. This is the company that either owns the construction project or the client who has hired your company to oversee the project work. To appear as a list option, [Add a Company to the Project Directory](/process-guides/set-up-a-project-directory/create-companies).
- **Title**Type a descriptive name for the contract.
- *Optional:* **Sign with DocuSignÂ®**Move this toggle to the right to collect signatures with the Procore + DocuSignÂ® integration. To learn how to activate the integration in Procore, see [Enable or Disable the DocuSignÂ® Integration on a Procore Project](/product-manuals/admin-project/tutorials/enable-or-disable-the-docusign-integration-on-a-procore-project).

 ##### Â Tip

 **How do you collect signatures with DocuSign?** After the data entry for the item is complete, Procore recommends changing the item's status to 'Out for Signature' before clicking the **Complete with DocuSign** button to launch the DocuSignÂ® application. If you have not previously signed in, you will be prompted to [Log In to DocuSignÂ®](/product-manuals/docusign/tutorials/log-in-to-docusign). Once you are signed in, you can prepare the DocuSign\_Â®\_ envelope for signatures. After the signature process is complete, Procore automatically changes the status of the item to 'Approved' and marks the item as 'Executed'. To learn more, see [DocuSignÂ®](/product-manuals/docusign/).