# Update the Tool Settings for Contracts & Change Orders

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/update-the-tool-settings-for-contracts

---

## Background

The Contracts page provides your company's Procore Administrator with the ability to configure your company's account-wide preferences for the Commitments tool. When you update these preferences, your changes affect all projects in your company's Procore account.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Company Admin tool.
- **Additional Information:**

 - Any changes affect all projects in your company's Procore account.

## Steps

1. Navigate to the Company **Admin** tool.
2. Under **Tool Settings**, click **Contracts & Change Orders**.

   - **To update Contract Settings:**

     - Click the **Contracts Settings** tab.
     - Locate the setting: **Restrict Edits to the Schedule of Values and Contract Company for the Following Objects Unless They Have a Status of Draft or Out for Bid.**
     - Choose which objects to restrict by checking the box next to one or more of the following:

       - Prime Contracts
       - Purchase Orders
       - Subcontracts *Note:* If the project setting 'Always Editable Schedule of Values' is enabled, SOV edits will NOT be restricted, regardless of the Prime Contract or Commitment status.
     - Click Save.
   - **To update Change Order Settings:**

     - Locate the setting: **Restrict Edits to the Schedule of Values for the Following Objects Unless They Have a Status of Draft.**
     - Choose which objects to restrict by checking the box next to one or more of the following:

       - Prime Contract Change Orders
       - Commitment Change Orders

         *Note:* For two-tiered change orders, this will also prevent users from adding or removing potential change orders of any status unless the change order has a status of Draft.
     - Locate the setting: **Pending-billable Status**.

       - Add a checkmark to enable the setting. 
         *Note:* This setting applies only to **single-tier** change orders at this time.
     - Click **Save**.

       ##### Important

       Enabling the **Claimable Variations** setting directly impacts how users manage the change management process. This feature adds functionality that allows users to track and report on potential costs that can be claimed from an owner.

       The setting introduces a new **Pending - Billable** status for **single-tier** change orders. This new status allows unapproved change orders to be included on invoices.

       - Invoice lines can be grouped by change order status.
       - This new status, which changes based on the language selected in Procore, displays in financial workflows.
       - Edits can be made to the Schedule of Values (SoV) while in the new status.   
         *If the new value is less than the billed to date amount, a warning message appears.*
       - Once a Budget view is configured to include the new status, a filter can be applied using the status.