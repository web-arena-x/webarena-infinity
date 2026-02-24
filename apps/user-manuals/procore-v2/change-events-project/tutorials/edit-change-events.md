# Edit Change Events

Source: https://v2.support.procore.com/product-manuals/change-events-project/tutorials/edit-change-events

---

## Background

On a construction project, a *change event* is any change that affects the original scope of a construction project. It can be any event that affects the scope of the work to be completed, causes a change to the project schedule, or results in unexpected costs. It allows your project's team members and stakeholders to prepare for a cost change before it becomes an actual cost.

##### Example 1: Create a Change Event to Establish a Change Order

A change event can come from many sources and is an event that establishes the change order process. Examples include:

- Accommodating an owner request.
- Accounting for a design flaw.
- Addressing an unforeseen issue caused by a vague document or specification.

A change event can also be used to document a project condition that resulted in a 

A *Backcharge* is an amount of money that a buyer holds back from a seller to recover any costs incurred as a consequence of the seller performing incomplete or defective work. For example, an *Owner* might bill a backcharge to a *General Contractor (GC)* for site clean-up or a GC might bill a backcharge to a *subcontractor* for property damage.

Backcharge. The intent of a backcharge is to recover the unforeseen expenses incurred when performing corrective actions that a party was contractually obligated to perform.

To ensure that you have fully documented the conditions that resulted in the backcharge, you can create a change event. Common scenarios for documenting backcharges this way include:

- Repairing something that a subcontractor damaged.
- Cleaning up an area that the subcontractor was obligated to clean.
- Replacing defective materials provided by the subcontractor.
- Reinstalling an incorrect installation performed by a subcontractor.
- Bringing a neglected issue into compliance with safety regulations.
- Providing unforeseen equipment rental and use costs.

With the Change Events tool in Procore, you can create a change event to record a reason for a change in a construction project. They also prepare project team members and stakeholders for the potential costs associated with the change event. After a change event is created, you can then send a Request for Quote (RFQ) to your subcontractors. Subcontractors can then respond to RFQs (or a general contractor can enter a response to an RFQ on the subcontractor's behalf). Included in the RFQ response is all the required documentation related to the change event's potential cost and schedule impact. After your subcontractor's RFQs responses are reviewed, your project team has the information it needs to proceed with creating a Potential Change Order (PCO).

## Things to Consider

- **Required User Permissions:**

 - *To edit change events you created*, 'Standard' level permissions or higher on the project's Change Events tool. 
     OR
 - *To edit any change event,* 'Admin' level permissions on the project's Change Events tool.
- **Alternate ways to create change events**:

 - To learn how to use other Procore platforms and tools to create a change event, see [Which Procore tools can I use to create a change event?](/faq-which-procore-tools-can-i-use-to-create-a-change-event)

## Steps

- Edit a Change Event
- Add Change Event Line Items
- Import Line Items
- Update Production Quantities

### Edit a Change Event

1. Navigate to the project's **Change Events** tool.
2. Locate the event to edit in the 'Change Events' table and click the hyperlinked **CE Number - Title** to open the Change Event.
3. Click **Edit**.
4. In the 'Edit Change Event' page, update the following as needed:

- **Number**. Procore automatically assigns new numbers to change events in ascending sequential order.

 Number

 ##### Â Notes

 - The default numbering scheme is 001, 002, 003, and so on.
 - You can customize the numbering scheme for the change events on your project at any time by typing an alphanumeric numbering scheme over the default value. For example, CE001, CE1000, CE-1000, and so on.
 - After customizing the numbering scheme, Procore uses it to assign new numbers to subsequent change events.

- **Title**

 Enter a descriptive title for the change event.

 Title
- **Status.** Select a status for the change event from the drop-down list. Your 

 A *Procore Administrator* is a user who has 'Admin' level permissions on all of the Company level Tools in Procore. Granting a user âAdminâ level permissions in the Company level Directory tool automatically assigns that user âAdminâ permissions on all Company level tools. Also called a *Company Administrator*.

 ProcoreÂ Administrator can also customize the options in this list. See [Customize Change Event Statuses](/product-manuals/admin-company/tutorials/set-the-default-change-management-configurations).

 Status
- **Origin**Select the Procore tool and item from which your change event originates.

 Origin
- **Type**

 Select the change event type. Your options include: *TBD*, *Allowance*, *Contingency*, *Owner Change*, or *Transfer*. See [Set the Default Change Management Configurations](/product-manuals/admin-company/tutorials/set-the-default-change-management-configurations).

 Type
- **Change Reason**

 Select a reason for the change from the drop-down menu. See [Set the Default Change Management Configurations](/product-manuals/admin-company/tutorials/set-the-default-change-management-configurations). 
 *Note:* When you enable the **Change Events - Empty Default "Change Reason"** feature in Procore Explore, the change reason for Change Events is empty by default.

 Change Reason
- **Description**

 Describe the event that may result in a change in costs.

 Description
- **Attachments**. Attach any relevant files.

 Attachments
- **Prime Contract for Markup Estimates.** Select the contract that contains the markup settings that you want to use to calculate the markup on the [Rough Order of Magnitude](/glossary-of-terms) (ROM) values. Procore automatically selects the contract with the lowest number.

 Prime Contract for Markup Estimates
- **Scope**

 Select one of the available scope options from the list: *In Scope*, *Out of Scope*, or *TBD*. See [What are the default scope options for change events in Procore?](/faq-what-are-the-default-scope-options-for-change-events-in-procore)

 Scope
- **Expecting Revenue** Select *YES* or *NO.* If *YES,* select one of the options from the **Line Item Revenue Source** field. If *NO,* Revenue ROM amounts will be set to zero (0).

 Expecting Revenue
- **Line Item Revenue Source**

 Select one of the options from the list: *Match with latest cost,* *No revenue expected, or Quantity x Unit Cost.*

 Line Item Revenue Source

Next, choose from these options:

- If you want to add line items to your change event now, continue with the steps in Add Change Event Line Items. 
   OR
- If you want to save the change event and add line items later, click **Save**.

### Add Change Event Line Items

##### Â Tip

**Did you know a user with 'Admin' settings on the Change Events tool can turn the Change Events tool's 'Column Display' settings ON and OFF?** For best results, your project's column display settings should be determined at the beginning of a project. To learn more, see [How do the Change Events tool's column display settings work?](/faq-how-do-the-change-event-tools-column-display-settings-work)