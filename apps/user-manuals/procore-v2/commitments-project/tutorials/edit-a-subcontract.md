# Edit a Subcontract (Legacy)

Source: https://v2.support.procore.com/product-manuals/commitments-project/tutorials/edit-a-subcontract

---

##### Â Legacy Content

This tutorial details Procore's legacy experience for editing a subcontract. The information on this page will be replaced with updated content when the redesigned commitments beta experience is generally available. To learn about this release and its timeline, see [Project Financials: Modernized Experience for Commitments](https://support.procore.com/tc/procore/Legacy/Release%5FDocumentation%5FArchives/2022/Project%5FFinancials:%5FModernized%5FExperience%5Ffor%5Fthe%5FCommitments%5FTool)

***Important!*** If you are using the commitments beta experience, please see the [Edit Subcontracts](/product-manuals/commitments-project/tutorials/edit-subcontracts) tutorial instead of the information below.

## Background

After you create a subcontract, you can edit it at any time.

## Things to Consider

- **Required User Permissions:**

 - **Admin** level permissions on the project's Commitments tool. 
    OR
 - **Read Only** or **Standard** level permissions on the project's Commitments tool with the ['](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template)[Update Work Order Contract](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template)['](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) granular permissions enabled on your permission template.
- For companies using the ERP Integrations tool: **Show/Hide**

 - If you are editing a subcontract that has NOT yet been synced with your company's [integrated ERP system](/glossary-of-terms), you may use the steps below. To determine if a subcontract has been synced with an ERP system, see [What do the ERP Icons mean?](/product-manuals/commitments-project/tutorials/edit-a-commitment)
 - If you are editing a subcontract that has already been synced with your company's integrated ERP system, see [Edit a Commitment Synced with ERP](/product-manuals/erp-integrations-company/tutorials/edit-a-commitment-synced-with-erp).

## Prerequisites

- [Create a Subcontract](/product-manuals/commitments-project/tutorials/create-a-subcontract)

## Steps

1. Navigate to the project's **Commitments** tool.
2. Under the **Contracts** tab, locate the subcontract.
3. Click the **Number** link to open the subcontract.
4. In the **General** tab, edit the following:

   - **Sign with DocuSignÂ®** If you have enabled the Procore + DocuSignÂ® integration (see [Enable or Disable the DocuSignÂ® Integration on a Procore Project](/product-manuals/admin-project/tutorials/enable-or-disable-the-docusign-integration-on-a-procore-project)), a checkmark appears in this box by default. If you do NOT want to collect signatures with DocuSignÂ®, remove the mark.

     ##### Â Tip

     **How do you collect signatures with DocuSign?** After the data entry for the item is complete, Procore recommends changing the item's status to 'Out for Signature' before clicking the **Complete with DocuSign** button to launch the DocuSignÂ® application. If you have not previously signed in, you will be prompted to [Log In to DocuSignÂ®](/product-manuals/docusign/tutorials/log-in-to-docusign). Once you are signed in, you can prepare the DocuSign\_Â®\_ envelope for signatures. After the signature process is complete, Procore automatically changes the status of the item to 'Approved' and marks the item as 'Executed'. To learn more, see [DocuSignÂ®](/product-manuals/docusign/).

- **#**Enter or validate the unique identifier for the subcontract. If you are creating the first commitment of a project, Procore automatically numbers the commitment in sequential order. For example, SC-01-001, SC-01-002, and so on.

 ##### Â Notes

 - If your company has implemented the ERP Integrations tool, your integrated ERP system may impose a maximum character limit. See [What is the maximum character length for a commitment's 'Number (#)'?](/faq-what-is-the-maximum-character-length-for-a-commitments-number)
 - When a commitment is exported to the Integration by Ryvit, it must have a unique commitment number. You can customize the numbering scheme for your project's commitments. To learn more, see [Can I customize the numbering system for financial objects in Procore?](/faq-can-i-customize-the-numbering-system-for-financial-management-objects-in-procore)