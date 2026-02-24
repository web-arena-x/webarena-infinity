# Add a Change Event Line Item to an Unapproved Prime Potential Change Order

Source: https://v2.support.procore.com/product-manuals/change-events-project/tutorials/add-a-change-event-line-item-to-an-unapproved-prime-pco

---

## Background

If the Project level Prime Contracts tool is configured with the 2-tier change order configuration setting (see [What are the different change order tier settings in Project Financials?](/faq-what-are-the-different-change-order-tier-settings-in-project-financials)), you must perform the Steps below before you can create a [prime contract change order](/glossary-of-terms).

##### Â Tip

**When do I create a potential change order?** Procore recommends creating a potential change order only for any change event line item that is set to 'Out of Scope' and requires your client's or project owner's approval to proceed.

*Note:* If your project team is using Procore's 

A *Request for Quote (RFQ)* is a business process where a client requests a price quote from a *collaborator*, such as a *subcontractor*, vendor, or another supplier. The collaborator reviews the client's RFQ requirements and then responds by providing a written price quote. In Procore, RFQs are created after a *change event* occurs and helps the client to avoid incurring unexpected and costly alterations or substitutions.

Request for Quote (RFQ) feature, you can create a potential change order either before or after a response is submitted for an RFQ has been responded to. However, if you wait until after an RFQ response is submitted, Procore automatically populates the potential change order's Schedule of Values (SOV) with data from the RFQ.

When you create a potential change order, Procore can also be configured to automatically populate its SOV with the 

*Rough Order of Magnitude (ROM)* is a rough numerical cost estimate that is used in the construction industry to gain a rough idea of the cost(s) to complete a project. ROM estimates are typically provided by a knowledgeable, high-level expert during the initiation/beginning phases of a project when there is still a high level of uncertainty about the project. ROM estimates are understood to have a lower level of accuracy than a definitive/conclusive estimate. Procore also provides an option for tracking potential revenue for change events using a Revenue ROM option that lets you use the latest cost amounts when changes are out of scope.

Rough Order of Magnitude (Revenue ROM) values. If you choose to hide the Revenue ROM feature, the value depends on the scope assigned to the change event:

- For *In Scope* or *TBD* change events, the potential change order populates with $0.
- For *Out of Scope* change events, the potential change order populates from the RFQ. The RFQ must be in the *Pending Final Approval* status. If there is no RFQ, the system populates from the 'Cost ROM' value.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Change Events tool AND
 - 'Admin' level permissions on the project's Prime Contracts tool
- **Additional Information:**

 - You can only add change event line items to prime potential change order that do not have the status of 'Approved.'

## Prerequisites

- [Create a Potential Change Order for a Prime Contract](/product-manuals/prime-contracts-project/tutorials/create-a-potential-change-order-for-a-prime-contract)

## Steps

1. Navigate to the project's **Change Events** tool.
2. Select one or more change event line items. You can select line items from multiple change events.
3. Click the **Bulk Actions** menu. Then choose **Add to Unapproved Prime PCO** and select the unapproved prime potential change order from the list.

Procore automatically creates the line items on the potential change order's SOV using the selected change event line items.