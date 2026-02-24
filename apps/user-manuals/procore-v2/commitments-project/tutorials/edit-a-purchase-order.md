# Edit a Purchase Order (Legacy)

Source: https://v2.support.procore.com/product-manuals/commitments-project/tutorials/edit-a-purchase-order

---

##### Â Legacy Content

This tutorial details Procore's legacy experience for editing a purchase order. The information on this page will be replaced with updated content when the redesigned commitments beta experience is generally available. To learn about this release and its timeline, see [Project Financials: Modernized Experience for Commitments](https://support.procore.com/tc/procore/Legacy/Release%5FDocumentation%5FArchives/2022/Project%5FFinancials:%5FModernized%5FExperience%5Ffor%5Fthe%5FCommitments%5FTool)

***Important!*** If you are using the commitments beta experience, please see the [Edit Purchase Orders](/product-manuals/commitments-project/tutorials/edit-purchase-orders) tutorial instead of the information below.

## Background

After you create a purchase order, you can edit it at any time.

## Things to Consider

- **Required User Permissions:**

 - **Admin** level permissions on the project's **Commitments** tool. 
    OR
 - **Read Only** or **Standard** level permissions on the project's Commitments tool with the ['Update Purchase Order Contract'](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) granular permissions enabled on your permission template.
- For companies using the ERP Integrations tool: **Show/Hide**

 - If you are editing a purchase order that has NOT yet been synced with your company's [integrated ERP system](/glossary-of-terms), you may use the steps below. To determine if a purchase order has been synced with an ERP system, see [What do the ERP Icons mean?](/product-manuals/commitments-project/tutorials/edit-a-commitment)
 - If you are editing a purchase order that has already been synced with your company's integrated ERP system, see [Edit a Commitment Synced with ERP](/product-manuals/erp-integrations-company/tutorials/edit-a-commitment-synced-with-erp).

## Prerequisites

- [Create a Purchase Order](/product-manuals/commitments-project/tutorials/create-a-purchase-order)

## Steps

1. Navigate to the project's **Commitments** tool.
2. Under the **Contracts** tab, locate the purchase order.
3. Click the **Number** link to open the purchase order.
4. In the **General** tab, click **Edit**.
5. Under **General Information**, edit the following:

   - **Sign with DocuSign**If your project is using the Procore + DocuSignÂ® integration (see [Enable or Disable the DocuSignÂ® Integration on a Procore Project](/product-manuals/admin-project/tutorials/enable-or-disable-the-docusign-integration-on-a-procore-project)), a checkmark appears in this box by default. If you do NOT want to sign the purchase order with DocuSignÂ®, remove the checkmark.
   - **#** Enter or confirm the unique identifier for the purchase order. If you are creating the first purchase order for your project, Procore automatically numbers your purchase orders in sequential order. For example, PO-01-001, PO-01-002, and so on.

     ##### Â Notes

     - For companies using the ERP Integrations tool, your integrated ERP system may impose a maximum character limit. See [What is the maximum character length for a commitment's 'Number (#)'?](/faq-what-is-the-maximum-character-length-for-a-commitments-number) ***Important!*** When a commitment is exported to Integration by Ryvit, it must have a unique number.
     - You can customize the numbering scheme for your project's purchase orders and subcontracts. To learn more, see [Can I customize the numbering system for financial objects in Procore?](/faq-can-i-customize-the-numbering-system-for-financial-management-objects-in-procore)

- **Title**Provide a descriptive name for the purchase order.

 ##### Â Notes

 - If your company has enabled the ERP Integrations tool, be aware that some [integrated ERP systems](/glossary-of-terms) impose character limits on the 'Title' field when data exported from Procore is imported into their system.
 - For details about character limits, see [What is the maximum character length for a commitment's 'Title'?](/faq-what-is-the-maximum-character-length-for-a-commitment-title)