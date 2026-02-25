# Configure a Prime Contract's Advanced Settings (Beta)

Source: https://v2.support.procore.com/product-manuals/prime-contracts-project/tutorials/configure-a-prime-contracts-advanced-settings

---

##### Â In Beta

This content is for participants in the Project Financials: Modernized Experience for Prime Contracts beta program.

## Background

If you are a user with 'Admin' level permissions on the Prime Contracts tool, the steps below show you how to edit advanced settings for the project's prime contract. This includes choosing an accounting method for the Schedule of Values (SOV), enabling financial markup, owner invoice settings, comments settings, and payment settings. In addition to these Advanced Settings, additional contract configuration settings are on the tool's Configure Settings page. See [Configure Settings: Prime Contracts](/product-manuals/prime-contracts-project/tutorials/configure-settings-prime-contracts).

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the project's Prime Contracts tool.
- **Additional Information:**

  - Additional contract configuration settings are on the tool's Configure Settings page. See [Configure Settings: Prime Contracts](/product-manuals/prime-contracts-project/tutorials/configure-settings-prime-contracts).

## Steps

- Edit the Advanced Settings

  - Turn Financial Markup ON and OFF on a Contract
  - Set Up Owner Invoices for a Contract
  - Turn Payments Received ON and OFF on a Contract
  - Set the Accounting Method on a Prime Contract

### Edit the Advanced Settings

1. Navigate to the project's **Prime Contracts** tool.
2. Locate the prime contract to work with. Then click its **Number** link.
3. Click the **Edit Advanced Settings** button.
4. Choose from these options:

   - Turn Financial Markup ON and OFF on a Contract
   - Set Up Owner Invoices for a Contract
   - Turn Payments Received ON and OFF on a Contract

### Turn Financial Markup ON and OFF on a Contract

You can turn the Financials Markups tab ON and OFF on an individual prime contract. Procore's default setting is ON. To learn how to use this feature, see [Add Financial Markup to Prime Contract Change Orders](/product-manuals/prime-contracts-project/tutorials/add-financial-markup-to-prime-contract-change-orders).

Under the 'Financial Markup' section, do the following:

- To turn the Financials Markup tab ON, place a checkmark in the **Enable Financials Markup** box.   
  OR
- To turn the Financials Markup tab OFF, remove the checkmark from the **Enable Financials Markup** box.

If this is the only setting you want to change, click **Save**. Otherwise, continue with the next step.

### Set Up Owner Invoices on a Contract

If you are planning to generate invoices to send to a project's owner or a client for the work your team performs, you use the controls in this section to set up the owner invoice feature for a prime contract.

1. Scroll to the 'Owner Invoices' section.
2. Choose to enable or disable the following options:

   - **Enable Owner Invoices**. To turn the owner invoice feature ON for this contract, place a checkmark in this box. ON is the default setting. To turn this feature OFF, remove the checkmark.
   - **Enable Completed Work Retainage**. To turn the completed work retainage feature on, place a checkmark in this box. ON is the default setting. To turn this feature OFF, remove the checkmark.
   - **Enable Stored Material Retainage**. To turn the stored material retainage feature on, place a checkmark in this box. ON is the default setting. To turn this feature OFF, remove the checkmark.
   - **Level of Detail to Display Change Orders**. This setting determines how Procore displays change orders in the 'Detail' tab of the prime contract. Your options include:\* **Line items in each Potential Change Order**. This is the default setting. This setting lists all of the line items for all potential change orders related to the prime contract.\* **Prime Contract Change Order**. This selection lists only the change orders related to the prime contract.\* **Potential Change Order**. This selection lists only the potential change orders related to the prime contract.
   - **Approve Subcontractor Invoices when Owner Approves Owner Invoices**. Place a checkmark in this box so that once an owner approves an owner invoice, the subcontractor invoice is also approved. This function is only enabled when you choose to pre-fill your owner invoices with data from your project's subcontractor invoices. To learn more about pre-filling invoices, see [Create Owner Invoices](/product-manuals/prime-contracts-project/tutorials/create-owner-invoices).
   - **Show Cost Code on PDF**. Place a checkmark in this box to show cost codes on the PDF. There is no cost code column in the Configurable PDF tab, but cost codes will show in headers if grouped by cost code.

If these are the only settings you want to change, click **Save**. Otherwise, continue with the next step.

### Turn Payments Received ON and OFF on a Contract

You can turn the Payments Received tab ON and OFF on an individual prime contract. Procore's default setting in ON. To learn how to use this feature, see [Add Financial Markup to Prime Contract Change Orders](/product-manuals/prime-contracts-project/tutorials/add-financial-markup-to-prime-contract-change-orders).

1. Scroll to the 'Payments Received' section.
2. Choose from these options:

   - To turn the 'Payments Received' tab ON, place a checkmark in the **Enable Payments** box. ON is the default setting.   
     To turn the 'Payments Received' tab OFF, place a checkmark in the **Enable Payments** box.

If these are the only settings you want to change, click **Save**.

### Set the Accounting Method on a Prime Contract

Before users start adding line items to a prime contract, you can choose the accounting method that to use. The accounting method cannot be changed after line items are created.

1. Scroll to the 'Schedule of Values' section.
2. Choose the accounting method for the contract:

   - **Amount Based**Choose this method to enter a lump sum amount for a line item on a Schedule of Values. Amount Based is Procore's default setting for contracts.
   - **Unit/Quantity Based**Choose this method when ordering materials in quantity. With this method, users enter a quantity and unit price for the line item on the Schedule of Values and Procore automatically calculates the total for the line item for you.
3. Click **Save**.