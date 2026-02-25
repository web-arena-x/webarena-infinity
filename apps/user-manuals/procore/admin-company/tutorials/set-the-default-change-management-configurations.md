# Set the Default Change Management Configurations

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/set-the-default-change-management-configurations

---

## Background

The change management configuration settings in the Company Admin tool let you create customized change order reasons, change types, and change statuses. Users can then select your customized options when creating change orders in Procore.

## Things to Consider

- **Required User Permissions**:

 - 'Admin' on the Company Admin tool.
- **Additional Information**:

 - You cannot delete a change reason that is already associated with a change order.

## Steps

- Customize Change Order Reasons
- Customize Change Types
- Customize Change Event Statuses

#### Customize Change Order Reasons

You can customize the change reasons your users see when they create or edit change orders. See [Create a Commitment Change Order (CCO)](/process-guides/materials-user-guide-with-financials/create-a-change-order-cco).

1. Navigate to the Company **Admin** tool.
2. Under **Tool Settings**, click **Change Management.**
3. Under **Change Reasons**, do the following:

   - **Add a custom change reason.** Type a reason in the blank box and click **Add (+)**.
   - **Change a default or custom change reason.** Click a table cell and type to replace the text.
   - **Show a default or custom change reason as a selection in the Reason list in a change event.** Mark the **Available** check box. This is the default setting.
   - **Hide a default or custom change reason from the Reason list in a change event.** Remove the checkmark from the **Available** box.

     ##### Â Notes

     - To learn more, see [What are Procore's default change types and change reasons?](/faq-what-are-procores-default-change-types-and-change-reasons)
     - The system's default reasons can be edited to match your team's specific change reasons and usage.   
       *Note:* The **Change Events - Empty Default "Change Reason"** feature can be enabled in Procore Explore so the change reason for Change Events is empty by default.

- **To remove a custom change reason**, click the delete icon. You cannot remove change reasons when tied to existing change orders in Procore.

#### Customize Change Types

You can customize the change types your users see when they create or edit change events. See [Create Change Events](/product-manuals/change-events-project/tutorials/create-change-events).

1. Navigate to the Company **Admin** tool.
2. Under **Tools Settings**, click **Change Management** **.**
3. Under **Change Types**, do the following:

   - **To add a change type**, enter a type in the box and click the **Add (+)** button.
   - **To edit an existing change type**, double-click the appropriate value in the table. Then type over the existing text with your new value.

     ##### Â Notes

     - To see the system default change types, [click here](/faq-what-are-procores-default-change-types-and-change-reasons).
     - The default values in Change Types column cannot be edited. However, you can edit the values in the **Abbreviations** column.
     - If you have created custom change types for your company, you may edit them.

- **To remove a change type**, click the **delete** icon. *Notes*:

 - You cannot delete the system's default change type selections, only the custom ones that you create for use with your system.
 - You cannot delete a change type if it has been associated with an existing change event.
 - You can only set a change type when creating a change event, but you can filter by change types when looking at Prime PCOs.

#### Customize Change Event Statuses

You can customize the statuses that are available to your end users when working with change events.

1. Navigate to the Company **Admin** tool.
2. Click **Change Management.**
3. Under **Change Event Statuses**, do the following:

   - **To add a change event status**, type your desired text in the blank box. For example, type Revise and Resubmit. Then select one of the available status considerations (e.g., *Open*, *Closed*, *Void*, or *Pending*). Then click the plus (+) button.
   - **To edit an existing change event status**, double-click the appropriate value in the table. Then type over the existing text with your new value (*Note*: You cannot edit the system's default change event status selections, only the custom ones that you create for use with your system).
   - **To make a status the default selection for a new change event**, place a checkmark in the box. You can only select one box.
   - **To remove a change event status**, click the delete icon. *Notes*:

     - You cannot delete the system's default change event status selections, you can only delete the custom ones that you create for use with your company account.
     - You cannot delete a change event status if it has been associated with an existing change event.