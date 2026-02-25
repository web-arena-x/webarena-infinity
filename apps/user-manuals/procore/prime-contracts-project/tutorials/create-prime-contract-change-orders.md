# Create Prime Contract Change Orders (Beta)

Source: https://v2.support.procore.com/product-manuals/prime-contracts-project/tutorials/create-prime-contract-change-orders

---

## Background

If the Change Events tool is enabled on your project, your project's change order tier configuration setting. The tier setting determines the number of steps that take place before creating a prime contract change order. To learn more, see [What are the different change order tier settings in Project Financials?](/faq-what-are-the-different-change-order-tier-settings-in-project-financials))

| Change Order Tier Setting | For three (3) tier, start here... | For two (2) tier, start here... | For one (1) tier, start here... |
| --- | --- | --- | --- |
| **One (1) Tier** | N/A | N/A | See below |
| **Two (2) Tier** | N/A | [Create a Potential Change Order for a Prime Contract from a Change Event](/product-manuals/change-events-project/tutorials/create-a-prime-potential-change-order-from-a-change-event) | See below |
| **Three (3) Tier** | [Create a Potential Change Order for a Prime Contract from a Change Event](/product-manuals/change-events-project/tutorials/create-a-prime-potential-change-order-from-a-change-event) | [Create a Change Order Request](/product-manuals/prime-contracts-project/tutorials/create-a-change-order-request) | See below |

## Things to Consider

- **Required User Permissions:**

  - 'Standard' or 'Admin' level permissions on the project's Change Events tool.  
    AND
  - 'Standard' or 'Admin' level permissions on the project's Prime Contracts tool.

    ##### Â Notes

    For users with 'Standard' level permissions on the project's Prime Contracts tool to perform this task, the following must also be true:

    - The user must be added to the 'Private' drop-down list of the prime contract. See [Create Prime Contracts](/product-manuals/prime-contracts-project/tutorials/create-prime-contracts).
    - If the project is configured to use the two (2) or three (3) tier change order setting (see [What are the different change order tier settings in Project Financials?](/faq-what-are-the-different-change-order-tier-settings-in-project-financials)), the 'Allow Standard Users to Create PCO's' checkbox setting must be enabled. See [Configure Settings: Prime Contract](/product-manuals/prime-contracts-project/tutorials/configure-settings-prime-contracts).

- **Required Configuration Setting:**

  - To complete the steps below, you must enable the 1-tier configuration setting for Prime Contract Change Orders. See [Configure the Number of Prime Contract Change Order Tiers](/product-manuals/prime-contracts-project/tutorials/configure-the-number-of-prime-contract-change-order-tiers).
- **Additional Information:**

  - After you create a change event, you can also create an RFQ to send to the affected subcontractor(s). See [Create RFQs](/product-manuals/change-events-project/tutorials/create-rfqs-from-a-change-event).'
- **Show/Hide: If your company has enabled the ERP Integrations tool**

  If your company has enabled the ERP Integrations tool, keep these things in mind:

  - QuickBooksÂ® Desktop**:** Prime Contract Change Order exports are NOT supported.
  - Sage 100 ContractorÂ®**:** Prime Contract Change Orderexports are NOT supported.
  - Sage 300 CREÂ®**:**

    - **Title**. The Prime Contract Change Order title must be 30 characters or less.
    - **Number (#)**. The Prime Contract Change Order number must be five (5) characters or less.
    - **Status**. The **Prime Contract** must be in the **Approved** status.
    - **Associated Line Item**. For each line item that you add to the change order's Schedule of Values (SOV), you may designate one (1) associated line item for each change order line item or the same associated line item for all change order line items. *Note*: The **Associated Line Item** list is only visible and available when the ERP Integrations tool has been configured to work with Sage 300 CREÂ® and the Export Prime Contract Change Order capability has been switched on in Procore by your Integration Implementation Specialist.
  - ViewpointÂ® SpectrumÂ®**:** Prime Contract Change Order exports are NOT supported.
  - VistaÂ®**:** Prime Contract Change Order exports are supported.
  - CMiC**:**

    - **Date.** Required field.
    - **Status**. The **Prime Contract** must be in the **Approved** status.
    - **Associated Line Item**. For each line item that you add to the change order's Schedule of Values (SOV), you may designate one (1) associated line item for each change order line item or the same associated line item for all change order line items. *Note*: The **Associated Line Item** list is only visible and available when the ERP Integrations tool has been configured to work with CMiC and the Export Prime Contract Change Order capability has been switched on in Procore by your Integration Implementation Specialist.
    - **Markups.** Horizontal Markups are allowed. Vertical Markups are not allowed at this time.

## Prerequisites

- The Change Events tool must be enabled on the project. See [Add and Remove Tools on a Project](/product-manuals/admin-project/tutorials/add-and-remove-project-tools).
- Your project's **Prime Contract** must be in the 'Approved' status. See [Approve a Prime Contract](/product-manuals/prime-contracts-project/tutorials/approve-a-prime-contract).

## Steps

1. Locate the **Prime Contract** to modify. Then click its **Number** link.
2. Click the **Create** button and choose one of these options:

   - If your project uses the one (1) tier change order tier setting, choose the **Create** **Prime Contract CO**option.
   - If your project uses the two (2) or three (3) tier change order tier setting, choose the **Create****Prime PCO** option. You must create a potential change order before you can create a Prime Contract Change Order (i.e., for 2-tier change orders) or change order request (i.e., for 3-tier change orders).

     ##### Example

     The illustration below shows you the location of the 'Create' button. The options in the drop-down list will vary, depending on your project's change order tier setting.

- Update the **General Information**:

  Show/Hide: General Information

  - **Sign with DocuSignÂ®**  
    If you have enabled the Procore + DocuSignÂ® integration (see [Enable or Disable the DocuSignÂ® Integration on a Procore Project](/product-manuals/admin-project/tutorials/enable-or-disable-the-docusign-integration-on-a-procore-project)), a checkmark appears in this box by default. If you do NOT want to collect signatures with DocuSignÂ®, remove the mark.

    ##### Â Tip

    **How do you collect signatures with DocuSign?** After the data entry for the item is complete, Procore recommends changing the item's status to 'Out for Signature' before clicking the **Send to DocuSign** button to launch the DocuSignÂ® application. If you have not previously signed in, you will be prompted to [Log In to DocuSignÂ®](/product-manuals/docusign/tutorials/log-in-to-docusign). Once you are signed in, you can prepare the DocuSign\_Â®\_ envelope for signatures. After the signature process is complete, Procore automatically changes the status of the item to 'Approved' and marks the item as 'Executed'. To learn more, see [DocuSignÂ®](https://support.procore.com/integrations/docusign).

  - **#**  
    Accept the default number, enter a new number, or create a custom numbering scheme for this change order and future ones.
  - **Created By**  
    Procore automatically populates this field with the name of the user who created the change order.
  - **Revision**  
    If you revise a change order later, you can enter the revision number here.
  - **Created By**  
    Procore automatically populates this field with the name of the user who created the change order.
  - **Title**  
    Enter a descriptive name here.
  - **Status**  
    Procore automatically assigns agreements the 'Default' status. To select a different status, choose one of the status labels from the drop-down list. Options include *Draft*, *Out for Bid*, *Out for Signature*, *Approved*, *Complete*, or *Terminated.*

    ##### Â Note

    To create Prime Contract Change Orders (PCCOs) and owner invoices, your prime contract's status must be set to *Approved* or *Complete*.
- **Executed**  
  Place a mark in this check box if the agreement has been fully executed. A *fully executed* agreement is legally effective and has been signed by authorized representatives for each party.
- **Default Retainage**  
  Enter a number to represent the percentage that will be withheld as [retainage](/glossary-of-terms) on the line items included in the [Schedule of Values](/glossary-of-terms). For example, if you plan to withhold ten (10) percent of the line item's value, enter 10%.
- **Contractor**  
  Select the 'Contractor' from this drop-down list. This is the company that your team hired to perform the work. To appear as a list option, [Add a Company to the Project Directory](/process-guides/set-up-a-project-directory/create-companies).
- **Architect/Engineer**  
  Select the lead architect or engineer for the project from this drop-down list. To appear as an option in this list, the company must have a record in the Project Directory.
- **Description**  
  Enter a more detailed description of the agreement. You can apply the options in the formatting toolbar to your text.