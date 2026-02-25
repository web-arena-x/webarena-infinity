# Edit a Prime Contract

Source: https://v2.support.procore.com/product-manuals/prime-contracts-project/tutorials/edit-a-prime-contract

---

## Background

You can edit a prime contract at any time before you place it into the **Approved** status.

## Things to Consider

- **Required User Permissions:**

  - **Admin** level permissions on the project's Prime Contracts tool.  
    OR
  - **Read Only** or **Standard** level permissions on the project's Prime Contracts tool with **Update Prime Contracts** granular permission enabled on your permissions template.
- **Additional Information:**

  - Some fields cannot be edited when items are in the **Approved** status. For example, you cannot edit a [Schedule of Values](/glossary-of-terms) (SOV) on an owner invoice or Prime Contract Change Order (PCCO) is already in the **Approved** status.

## Prerequisites

- [Create Prime Contracts](/product-manuals/prime-contracts-project/tutorials/create-prime-contracts)
- Set the accounting method on the contract. See [Edit the Advanced Settings on a Prime Contract](/product-manuals/prime-contracts-project/tutorials/edit-the-advanced-settings-on-a-prime-contract).

## Steps

- Edit a Prime Contract
- Add, Delete, and Rearrange SOV Line Items

### Edit a Prime Contract

1. Navigate to the project's **Prime Contracts** tool.
2. Locate the contract to work with, then click its **Number** link.
3. Click **Edit**.
4. In the **General** tab, under **General Information**, modify the following information as needed:  
   *Notes*: There are no required fields when creating a new prime contract. If you click **Create** without completing any data entry, the system saves the contract with your name listed as the creator and places it in the *Draft* status by default.

   - **Sign with DocuSignÂ©**  
     If you are using the Procore + DocuSignÂ© integration (see [DocuSignÂ©](https://support.procore.com/integrations/docusign)), a checkmark appears by default. Clear the checkmark from the box if the prime contract does NOT require a DocuSignÂ© signature.
   - **Contract #**Accept the default contract number, enter a new number for the prime contract, or create a custom numbering scheme to use.  
     *Notes*:

     1. If you plan to create multiple prime contracts, Procore increments this number for you by default. For example; 1, 2, 3, and so on.
     2. To use a custom numbering scheme, you can enter a set of alphanumeric characters (for example, PC-1 or PC-01 or PC-001), and Procore increments the number on new contracts.
   - **Title**  
     Enter a descriptive name for the prime contract.
   - **Owner/Client**  
     Select the project owner/client from the drop-down list.
   - **Architect/Engineer**  
     Select the lead architect for the project from the drop-down list.
   - **Contractor**  
     Enter the company name of the primary contractor managing the construction project. If you are setting up the prime contract, this will typically be your company's name.
   - **Status**  
     Select the current status for the prime contract. Options include *Draft*, *Out for Bid*, *Out for Signature*, *Approved*, *Complete*, or *Terminated.  
     Note:* To create change orders and invoices, a prime contract's status must be set to *Approved* or *Complete*.
   - **Executed**  
     Place a mark in this check box if the contract has been fully executed.
   - **Make this Visible Only to Administrators and the Following Users**  
     Place a mark in this check box to limit visibility to users with 'Admin' permission and any users designated in the 'Allow These Users to See SOV Items' checkbox.
   - **Allow These Users to See SOV Items**  
     Place a mark in this check box. Then select the names of any users who have been granted 'Standard' or 'Read Only' permissions on the Prime tool from the 'Select a Person' drop-down list.
   - **Default Retainage**.   
     Specify a default percentage that will automatically be applied to all line item costs for retainage purposes. For example, enter: 10%
   - **Description**  
     Enter a descriptive summary to provide more detail about the prime contract.
   - **Attachments**  
     Attach any relevant files to the prime contract. For example, an electronic copy of the signed contract.
5. Under **Contract Dates**, do the following:

   - **Date Created**  
     Shows the date the contract was created. This cannot be modified.
   - **Start Date**  
     Specify the project's official start date.
   - **Estimated Completion Date**{  
     Specify the estimated date for project completion.
   - **Substantial Completion Date\***  
     Select the date from the calendar control. The substantial completion date refers to the date that work is considered sufficiently complete to satisfy contractual requirements. It also indicates the date that the project owner or client can assume occupancy of all or part of a project and the general contractor is entitled to receive contract balance payment (less retainage) until final completion.  
     *Note*: If enabled, the substantial completion date will be updated to each Prime Contract Change Order's Revised Substantial Completion Date once each Prime Contract Change Order has a status of Approved.
   - **Actual Completion Date**  
     Select the date from the calendar control. This represents that final payments have been processed and the contract is considered closed.
   - **Contract Date\***  
     Select the date from the calendar control. This represents the effective date of the contractual agreement. This is the date the contract goes into force.
   - **Signed Contract Received Date**  
     Select the date from the calendar control. This represents the date that the executed contract was received.

     ##### Â Tip

     **Will you be collecting signatures on this contract with DocuSign****Â©****?** If so, be aware that the 'Signed Contract Received Date' field is labeled 'Signature Required' field after a user clicks the **Sign with DocuSign****Â©** button or if the DocuSign**Â©** envelope has been sent to recipients and is awaiting signature(s) (i.e., while awaiting signatures, the status of the contract is set to *Pending*). When the final signature is completed, the Procore + DocuSign**Â©** integration updates this field to show the signature date. You can now click View to open the signed PDF in DocuSign**Â©**.

- **Execution Date\***  
  Select the date from the calendar control. This represents the date the agreement was signed by all parties.
- **Issued On Date\***  
  Select the date from the calendar control. This date represents the date the contractual agreement was issued to both parties.
- **Returned Date**  
  Select the date from the calendar control.
- **Letter of Intent Date**  
  Select the date from the calendar control. A *letter of intent* *date* is the date the Letter of Intent (LOI) document outlining the agreement between parties is received before the contract is finalized.
- **Approval Letter Date\***  
  Select the date from the calendar control. A *letter of approval date* is the date that compliance with the fees, statements, and disclosures stated in the Letter of Approval (LOA) for the contract was signed into the record.
- **Contract Termination Date**  
  Select the date from the calendar control. A *contract termination date* is a date outlined in the prime where all parties have met all contractual obligations and terms.
- Under **Additional Information**, do the following:

  - **Inclusions**. Specify any agreed-upon inclusions in the contract.
  - **Exclusions**. Specify any agreed-upon exclusions in the contract.
- Click **Save**.

### Add, Delete, and Rearrange SOV Line Items

1. Navigate to the **Prime Contracts** tool.
2. Click the **Schedule of Values** tab.
3. Click the vertical ellipsis (â®). Then choose from the following menu options:

   - **Add Above**. Select this option to add a line item above the current line item.
   - **Add Below**. Select this option to add a line item below the current line item.
   - **Delete**. Select this option to delete the current line item.

     ##### Â Tip

     To rearrange line items in the list, you can type over the numbers in the **#** column. This lets you specify the list order of each item on the SOV.

- Click **Save**.