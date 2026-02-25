# Create a Potential Change Order for a Client Contract from a Change Event

Source: https://v2.support.procore.com/product-manuals/change-events-project/tutorials/create-a-potential-change-order-for-a-client-contract-from-a-change-event

---

## Background

If your company has enabled the Change Events tool and configured your project to use a two (2) tier change order structure, the change event process requires you to create a potential change order. Then, you will create the Client Contract Change Order from the Client Contracts tool. For details about the tiers, see [What are the different change order tier settings in Project Financials?](/faq-what-are-the-different-change-order-tier-settings-in-project-financials)   
*Note*: Procore recommends that you create a Potential Change Order only for change event items that are *Out of Scope* and must be submitted to the client/owner for approval.

When you create a Potential Change Order, the Schedule of Values (SOV) will populate with the Revenue ROM values. If you have the Revenue ROM functionality hidden, the value will depend on the scope of the change event. *For In Scope* or *TBD* scope change events, the PCO will populate with $0. For *Out of Scope* change events, the PCO will populate from the RFQ if the status of that RFQ is *Pending Final Approval*. If there is no RFQ with that status, it will populate from the Cost ROM. For more information about RFQ statuses, see [What are the different RFQ statuses and how do they affect cost and change order amounts?](/faq-what-are-the-different-rfq-statuses).

## Things to Consider

- **Required User Permissions:**

 - 'Standard' level permissions or higher on the project's Change Events tool. 
     AND
 - 'Standard' level permissions on the project's Client Contracts tool and the 'Allow Standard Level Users to Create PCOs' configuration setting must be enabled on the Client Contracts tool.
- **Additional Information:**

 - Depending on the change order tier configuration setting configured for the Client Contracts tool, potential change orders can be transitioned into one (1) of the following items:\* For two (2) tier change orders, a 

    In Procore, a Client Contract Change Order (CCCO) is a change order that affects a client contract. A two-tier change order setup typically consists of a bundle of Potential Change Orders (PCOs) that must be approved by the general contractor or client. A three-tier change order setup typically consists of a bundle of Change Order Requests (CORs) that must be approved by the general contractor or client.

    Client Contract Change Order.\* For three (3) tier change orders, a 

    A *Change Order Request (COR)* is a Procore-specific package that can be created to contain one (1) or more *Potential Change Orders (PCOs)*. A COR is a formal request sent to a project's Owner that groups multiple PCOs for a single scope of work into a single package for review and approval.

    Change Order Request.\* To learn more see, [What are the different change order tier settings in Project Financials?](/faq-what-are-the-different-change-order-tier-settings-in-project-financials)

## Prerequisites

- The Change Events tool must be turned ON on the project. See [Add and Remove Project Tools](/product-manuals/admin-project/tutorials/add-and-remove-project-tools).
- The two (2) tier change order configuration settings must be turned ON the Client Contracts tool.
- The project's client contract must be in the 'Approved' status.

## Steps

1. Navigate to the project's **Change Events** tool.
2. In the table, mark the checkboxes for one (1) or more change event line item(s) to include in the new potential change order.

   ##### Â Note

   Procore creates the potential change order's Schedule of Values (SOV) using the selected change event line item(s).

- Click the **Bulk Actions** menu and choose the **Create Client PCO** option. Then choose the appropriate contract option from the sub menu.
- In the 'New Potential Change Order' page, complete the following data entry:

 - **Sign with DocuSignÂ®**If you have enabled the Procore + DocuSignÂ® integration (see [Enable or Disable the DocuSignÂ® Integration on a Procore Project](/product-manuals/admin-project/tutorials/enable-or-disable-the-docusign-integration-on-a-procore-project)), a checkmark appears in this box by default. If you do NOT want to collect signatures with DocuSignÂ®, remove the mark.

    Sign with DocuSign

    ##### Â Tip

    **How do you collect signatures with DocuSign?** After the data entry for the item is complete, Procore recommends changing the item's status to 'Out for Signature' before clicking the **Complete with DocuSign** button to launch the DocuSignÂ® application. If you have not previously signed in, you will be prompted to [Log In to DocuSignÂ®](/product-manuals/docusign/tutorials/log-in-to-docusign). Once you are signed in, you can prepare the DocuSign\_Â®\_ envelope for signatures. After the signature process is complete, Procore automatically changes the status of the item to 'Approved' and marks the item as 'Executed'. To learn more, see [DocuSignÂ®](/product-manuals/docusign/).

- **#**Accept the default number, enter a new number, or create a custom numbering scheme for this change order and future ones.

 Number

 ##### Â Notes

 - Procore automatically assigns the item a new number in sequential order. For example; 001, 002, 003, and so on.
 - To use a custom numbering scheme, enter any set of alphanumeric characters. Procore automatically assigns new numbers in sequential order using your custom scheme.