# Edit a Configurable PDF of an Owner Invoice (Legacy)

Source: https://v2.support.procore.com/product-manuals/prime-contracts-project/tutorials/edit-a-configurable-pdf-of-an-owner-invoice

---

##### Â Legacy Content

This page details the legacy owner invoice experience. A modernized experience is also available.

## Background

This tutorial shows you how to use the options in the Configurable PDF tab of an owner invoice. You can use the options in this tab to customize the way line items display on the PDF, such as how you want to group and summarize invoice line items so they display the way you want before you present the PDF to an owner.

## Things to Consider

- **Required User Permissions:**

  - **Admin** level permissions on the project's Prime Contracts tool.
- **Additional Information:**

  - If you click the **Email Invoice** button, only the **Detail** tab PDF of the Invoice will be sent to recipients, not the **Configurable PDF** tab.

## Prerequisites

- [Create Owner Invoices](/product-manuals/prime-contracts-project/tutorials/create-an-owner-invoice)
- [Create a Configurable PDF of an Owner Invoice](/product-manuals/prime-contracts-project/tutorials/create-a-configurable-pdf-of-an-owner-invoice)

## Steps

1. Navigate to the project's **Invoicing** tool.
2. Click the **Owner** tab.
3. Locate the invoice to work with. Then click its **Invoice #** link.
4. Click the **Configurable PDF** tab.
5. Edit the PDF in any of the following ways:

   1. **Summarization**  
      By clicking the arrows, you can expand and collapse the line items to show differing levels of data. To expand, click the arrow illustrated below. To collapse, click the arrow again.
   2. **Grouping**  
      Click the **Group** drop-down list to the group or subtotal line items by your selection:

      - *Optional:* **Sub Job**  
        This option is only available if the sub job feature is active on the project. See [Enable Sub Jobs on Projects for WBS](/process-guides/company-administration-work-breakdown-structure-guide/enable-sub-jobs-for-projects) and [Add 'Sub Job' Segment Items to a Procore Project](/process-guides/project-administration-work-breakdown-structure-guide/add-sub-jobs-to-a-project).
      - **Cost Code Tier 1**. If your cost code structure is tiered, this option groups data by the first tier.

        ##### Â Note

        For Procore project's using Procore's default cost codes that align with the [CSI MasterFormat](/glossary-of-terms), the '[Division](/glossary-of-terms)' concept is equivalent to the 'Cost Code Tier 1' option. If you want to group your data by 'Division', select the 'Cost Code Tier 1' option.

- **Cost Code Tier 2**. If your cost code structure is tiered, this option groups data by the second tier in your structure.
- **Cost Type**. This option lets you group data by your company's **Cost Type** segment. For details, see [What are Procore's default cost types?](/faq-what-are-procores-default-cost-types)
- **Manage Custom Groups**. You can click this button to create custom groupings for your configurable PDF. To learn how to manage groups, see [Create a Configurable PDF of an Owner Invoice](/product-manuals/prime-contracts-project/tutorials/create-a-configurable-pdf-of-an-owner-invoice).