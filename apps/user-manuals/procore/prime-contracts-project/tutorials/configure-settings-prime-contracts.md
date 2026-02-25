# Configure Settings: Prime Contracts

Source: https://v2.support.procore.com/product-manuals/prime-contracts-project/tutorials/configure-settings-prime-contracts

---

## Background

When setting up a Procore project, a user with 'Admin' permission on the Prime Contracts tool will first use the steps below to configure the tool's settings for users of the tool. Because users can create a *single prime contract* or *multiple prime contracts* on a single project (see [Create Prime Contracts](/product-manuals/prime-contracts-project/tutorials/create-prime-contracts)), the settings listed below are applied globally to all of the prime contracts in a project:

- **Contract Configuration**. Define the number of prime change order tiers for the project, gives you the option to grant users with 'Standard' permission on the Prime Contracts tool, the privilege to create potential change orders, and the ability to choose if you want to make the Schedule of Values (SOV) editable.
- **Default Distributions**. Specify the users to include by default on the Prime Contracts tool's email notification distributions.
- **Funding Sources**. List any funding sources related to the prime contract. A *funding source* can include federal, state, and local funds, bonds, grants, tax revenue, loans, programs, and more.

You can also set up customized settings to apply to each prime contract that your users create in a single project. To learn more, see [Edit the Advanced Settings on a Prime Contract](/product-manuals/prime-contracts-project/tutorials/edit-the-advanced-settings-on-a-prime-contract).

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the project's Prime Contracts tool.
- **Additional Information:**

  - Additional settings for a project's prime contract are in the tool's Advanced Settings tab. See [Edit the Advanced Settings on a Prime Contract](/product-manuals/prime-contracts-project/tutorials/edit-the-advanced-settings-on-a-prime-contract).

## Prerequisites

- Determine the number of change order tiers that you want to apply to your project. To learn more, see [What are the different change order tier settings in Project Financials?](/faq-what-are-the-different-change-order-tier-settings-in-project-financials)

## Steps

1. Navigate to the project's **Prime** **Contracts** tool.
2. Click the **Configure Settings**  icon.
3. Under **Contract Configuration**, do the following:

   1. **Number of Prime Contract Change Order Tiers**Select one option from the drop-down list to define how change orders will be managed on the project:

      ##### Â Important

      This setting cannot be changed after the first change order is created on the project.

- **1**. A *one (1) tier change order configuration* requires users to create only Prime Contract Change Orders. See [Create a Prime Contract Change Order](/product-manuals/prime-contracts-project/tutorials/create-a-prime-contract-change-order).
- **2**. A *two (2) tier change order configuration* gives users the ability to create potential change order (see [Create a Potential Change Order for a Prime Contract](/product-manuals/prime-contracts-project/tutorials/create-a-potential-change-order-for-a-prime-contract)) that can then be grouped into a single Prime Contract Change Order) and sent to a user for approval. This is the default setting for Procore projects.

  ##### Â Notes

  - A three (3) tier change order configuration is also available. To learn more, see [What are the different change order tier settings in Project Financials?](/faq-what-are-the-different-change-order-tier-settings-in-project-financials)
  - If your company or project billing process does NOT require you to group all of the approved change orders for the month into a single, combined change order for final signature, Procore recommends configuring the two-tier change order configuration setting on the Prime Contracts tool.

- **Allow Standard Level Users to Create PCOs**Place a mark in this checkbox to grant users with 'Standard' permissions the ability to create a PCO on the Change Orders tab of a Prime Contract.  
  *Note*: If you clear the mark from the checkbox, only users with 'Admin' permission can create a PCO using the Change Orders tab of a Prime Contract.
- **Enable Always Editable Schedule of** **Values**Mark this checkbox to provide users with editing permissions the ability to add, update, and remove line items from the SOV when the contract is in any status. Clear the mark to restrict users from editing the schedule of values. This setting is turned OFF by default. To learn more, see [What is the 'Enable Always Editable Schedule of Values' setting?](/faq-what-is-the-enable-always-editable-schedule-of-values-setting)

  ##### Â Note

  **For Procore users who turn the 'Enable Always Editable Schedule of Values' setting ON**, only a select number of [integrated ERP systems](/glossary-of-terms) support a one-directional sync from the integrated ERP system to Procore's Prime Contracts tool. Updating a prime contract's line items when its data is being synced with an integrated ERP system is NOT recommended.