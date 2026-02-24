# View or Edit Markup Estimates on Change Event Line Items

Source: https://v2.support.procore.com/product-manuals/change-events-project/tutorials/view-or-edit-markup-estimates-on-change-event-line-items

---

## Background

The 'Revenue ROM' feature in Procore is designed to reflect the potential impact of a change event on your project's budget before your team creates a 

A *Change Order* (CO) is a written record of a contract modification that details any amendment(s) to the original agreement's scope of work. Most construction contracts are executed with a clearly defined scope of work, so any work that is added, substituted, or deleted from the original contract's scope (such as changes to a project's designs, conditions, schedules, and/or costs) will typically require an approved change order.

Change Order. With this feature, Procore uses the value in the 'Revenue ROM' column to automatically calculate the estimated markup.

If you have the required user permissions, you can also apply a setting in the Configure Settings page of the project's Change Events tool to specify the prime contract's markup settings to use for estimating markup as follows:

- You can select which prime contract to use to estimate markup on all new change events.
- You can copy the prime contract setting to estimate markup on all existing change events.

## Things to Consider

- **Required User Permissions:**

 - *To edit any change event or Change Events configurations*, 'Admin' level permissions on the Change Events tool. 
     OR
 - *To edit only the change events you created*, 'Standard' level permissions on the Change Events tool.

## Steps

- Add Estimated Markup to a Single Change Event OR
- Add Estimated Markup to All of the Change Events on a Project OR
- Beta Edit Financial Markup Estimate on a Change Event

### Add Estimated Markup to a Single Change Event

1. Navigate to the project's **Change Events** tool.
2. Locate the change event to work with.
3. Click the **Edit** button next to that change event.
4. In the 'General' tab, under 'General Information' scroll down to the **Prime** **Contract (For Markup Estimates)** drop-down list.
5. Select the appropriate prime contract from the drop-down list.
6. Click **Save**.

### Add Estimated Markup to All of the Change Events on a Project

1. Navigate to the project's **Change Events** tool.
2. Click **Configure Settings** .
3. Click **Copy to Existing Change Events** to copy the markup settings from the default Prime Contract (This is the first Prime Contract on your project when sorted by number then title).
4. Click **Confirm**.

   ##### Â NoteSÂ

   - Markup is calculated using the Revenue ROM values based on the markup settings defined for the prime contract. See [Add Financial Markup to Prime Contract Change Orders](/product-manuals/prime-contracts-project/tutorials/add-financial-markup-to-prime-contract-change-orders).

#### Edit Financial Markup (Vertical) Estimate on a Change Event

*Note:* A **Prime** **Contract for Markup Estimates** must be selected on a change event before markup can be edited on individual line items. See Add Estimated Markup to a Single Change Event.

1. Navigate to the project's **Change Events** tool.
2. Locate the change event with the financial markup (vertical) to be edited and click its number to view the change event.
3. Click the value being edited in the markup section of the change event.
4. Click **Manual** **markup** and enter a new markup amount.
5. Changes are saved automatically once you click outside of the experience.

##### Â Important notes!

- If you manually enter a markup value, it will no longer stay updated with the prime contract's markup settings.

 - **To reapply the contracted financial markup to the change event line items**, the user must remove the current financial markup from the change event then complete the steps list here: Add Estimated Markup to a Single Change Event.
- When users create a Prime Contract Change Order from a change event with the edited financial markup, the Prime Contract Change Order will inherit the edited financial markup percentages entered on the change event.
- Only vertical markup can be edited on a change event
- There are some scenarios where edited financial markup in change events will not be able to pass to the Prime Contract Change Order due to complexity and the possibility of conflicting markup rules and logic.
- In the following scenarios, the user will have to edit the change order markup in the Prime Contract Change Order Schedule of Values. 
 *Note*: Edited markups will remain in the change event, but the new Prime Contract Change Order will use the selected prime contract markup rules

 - When multiple change events are used to create a change order.
 - When adding change event line items to an existing Prime Contract Change Order with markup logic already applied
 - Creating a new Prime Contract Change Order from a change event where the selected prime contract conflicts with the change events 'Prime Contract for Markup Estimates' field