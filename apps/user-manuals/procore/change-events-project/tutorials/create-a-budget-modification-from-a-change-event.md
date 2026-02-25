# Create a Budget Modification from a Change Event

Source: https://v2.support.procore.com/product-manuals/change-events-project/tutorials/create-a-budget-modification-from-a-change-event

---

##### Â Legacy Content

The Budget Modifications feature is being replaced by a [new Budget Changes feature](/process-guides/about-budget-changes/). Starting in October 2022, Procore will be working with Procore customers to migrate from budget modifications to the Budget Changes feature by October 16, 2023. Once you migrate, you will no longer have access to the budget modifications feature. If you have any questions before your company starts the migration, contact your Procore point of contact.

## Background

Creating a budget modification allows you to transfer funds from cost code to cost code, most likely for a change event that was "in scope" where there is no need to communicate with the owner (for example, a 

A *Contingency* is an amount of money held in reserve to pay for accidental or additional unforeseen costs during a construction project.

Contingency or 

A *Backcharge* is an amount of money that a buyer holds back from a seller to recover any costs incurred as a consequence of the seller performing incomplete or defective work. For example, an *Owner* might bill a backcharge to a *General Contractor (GC)* for site clean-up or a GC might bill a backcharge to a *subcontractor* for property damage.

Backcharge).

## Things to Consider

- **Required User Permissions:**

 - 'Standard' or 'Admin' level permissions on the project's Change Events tool AND
 - 'Standard' or 'Admin' level permissions on the project's Budget tool.
- **Additional Information:**

 - Budget Modifications are designed to give a Project Manager the flexibility to more accurately manage the "current" budget over the lifecycle of a construction project. Transfer allocated funds as necessary to make more realistic adjustments as budgeted items become over/under budget.
 - Budget modifications may not be visible to your client.
 - Transfers created using budget modifications will not be reflected on the Prime Contract's Schedule of Values or the Prime Contract Invoices, since they are intended for internal budget adjustments.
 - Budget modifications will be reflected in the Budget Modification column in the Budget.
 - The "Budget Modifications" report displays an exhaustive and detailed record of all budget modifications. (The Reports tab must be active. Requires 'Admin' user permissions on the Budget tool.)
 - If you added a line item to the budget (for $0) after it's locked, you will not be allowed to delete the line item if it's ever associated with a budget modification.
 - By default, you can only transfer money from one line item to another, which results in net-zero transactions. However, there is an advanced configuration setting that allows you to add or subtract money to/from a specific line item that will increase/decrease budget totals accordingly. To enable the add/subtract option, go to the tool's advanced configuration settings and mark the "Allow Budget Modifications Which Modify Grand Total " checkbox. (Requires 'Admin' user permissions on the Budget tool).

## Prerequisites

- [Lock a Budget](/product-manuals/budget-project/tutorials/lock-a-budget)

## Steps

1. Navigate to the project's **Change Events** tool.
2. Locate the change event line item that you want to move money into using a budget modification.
3. Click the cell in the **Budget Modification** column for that line item.

   ##### Â Tip

   To edit the cell value, a BLUE triangle icon must be visible. If it is NOT visible, do the following:

   - Check to see if the budget is unlocked.
   - Determine if you have been granted the appropriate permissions on the project's Budget tool.

- Complete the following fields:

 - **From**. Select a cost code from the list. This is the cost code that you will transfer funds from.
 - **To**. This field is pre-filled with the selected change event line item. Editing this information not permitted.
 - **Transfer Amount**. Enter the dollar amount of the transfer.
 - **Notes**. Enter any relevant notes about the budget modification.
- Click **Create**.