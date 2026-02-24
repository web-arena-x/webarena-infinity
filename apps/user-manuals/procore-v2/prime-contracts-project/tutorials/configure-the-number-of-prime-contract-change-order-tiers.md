# Configure the Number of Prime Contract Change Order Tiers

Source: https://v2.support.procore.com/product-manuals/prime-contracts-project/tutorials/configure-the-number-of-prime-contract-change-order-tiers

---

##### Â Limited Release

If you are a Procore customer in the United States, the name of this tool depends on a dictionary setting in your company's Procore account:

- The Prime Contracts tool is Procore's default tool name for the English (United States) dictionary.
- The Funding tool is only available with the Owners point-of-view dictionary.
- The Client Contracts tool is only available with the Specialty Contractors dictionary is active.

To learn about the dictionaries and required Project level and User level dictionary settings, see [What tool names and terms are different in Procore for general contractors, owners, and specialty contractors?](/faq-what-tool-names-and-terms-are-different-in-procore-for-general-contractors-owners-and-specialty-contractors)

## Background

When you initially set up the **Prime Contracts** tool for a project, you can choose between a 1- or 2-tier change order setting. This setting determines how many steps are required when managing change orders on a Procore project. You must configure this setting before your project users create change orders on a project. This setting cannot be changed after a change order is created.

## Things to Consider

- **Required User Permissions:**

  - **'**Admin**'** level permissions on the project's Prime Contracts tool.
- **Additional Information:**

  - This setting MUST be set configured before you create the first change order on the project.
  - If you do NOT specify a setting, 2-Tier is Procore's default setting.
  - You are NOT permitted to change this configuration setting after creating the first change order on a project.

## Prerequisites

- Review the information in [What are the different change order tier settings in Project Financials?](/faq-what-are-the-different-change-order-tier-settings-in-project-financials)

## Steps

1. Navigate to the project's **Prime Contracts**, **Client Contracts**, or **Funding** tool.
2. Click the **Configure Settings**  icon.
3. Select one (1) of these options from the **Number of Change Order Tiers** drop-down list:

   ##### Â Important

   This setting cannot be changed after the first change order is created on the project.

  
  

- **1-Tier (One-tier, a.k.a. 'single-tier')**  
  Users only need to create a single [change order](/glossary-of-terms) to send to the appropriate user(s) for review and approval.
- **2-Tier (Two-tier)**  
  This is Procore's default setting. With this setting, users first create one (1) or more [potential change order(s)](/glossary-of-terms). The potential change orders can then be grouped into a single change order to send to the appropriate user(s) for review and approval.

  ##### Â Note

  - Procore recommends applying the 1- or 2-Tier configuration setting to the tool.
  - A three (3) tier change order configuration is available. However, it is only recommended when your billing process requires you to group all of the 'Approved' change orders into a single, combined change order for final signature. To learn more, see [What are the different change order tier settings in Project Financials?](/faq-what-are-the-different-change-order-tier-settings-in-project-financials)