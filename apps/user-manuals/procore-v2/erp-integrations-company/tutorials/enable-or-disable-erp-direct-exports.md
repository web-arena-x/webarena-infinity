# Enable or Disable ERP Direct Exports

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/enable-or-disable-erp-direct-exports

---

## Background

In most cases, to sync an item to your ERP system, the item must first be accepted or rejected for export by an accounting approver in the Company level ERP tool. When enabled, the Direct Export feature allows you to configure your ERP integration to bypass the accounting approver step when sending Commitments, CCOs, and Invoices to ERP.

If this feature was previously enabled, it can also be disabled. If disabled, items that were synced while the feature was enabled can then be managed through the Company level ERP Integrations tool by an accounting approver.

##### Â Tip

You can use the Workflows tool instead of the accounting approver step to manage the approval flow of an item that is sent to ERP. The following three (3) configuration options are available with this feature:

- **Direct Export disabled (default)**. You can keep using your integration the same way with no changes.
- **Direct Export enabled, workflows NOT applied**. When enabled without applying a workflow to the approval process for a Commitment, CCO, and/or Invoice, this feature simply allows these objects to be exported directly to your ERP system when clicking the 'Send to ERP' button on the item in its Project level tool. No approval in the Company level ERP integrations tool is required.
- **Direct Export enabled, workflows applied**. You can enable the Direct Export feature, and choose to use a workflow for the ERP approval process prior to the 'Send to ERP' step, instead of approving an item for export through the Company level ERP Integrations tool. To learn about Procore's v2 Workflows tool (in Beta), including how to create workflow templates and assign them to projects, see [Workflows](/product-manuals/workflows-company/).

## Things to Consider

- **Required User Permissions**:

 - 'Admin' on the company's ERP Integrations tool. 
    AND
 - The 'Can Push to Accounting' privilege in the Company Directory for each tool for which the feature will be enabled or disabled. 
    *Note*: *To learn how this privilege can be granted, see* [Grant Accounting Approver Privileges](/product-manuals/erp-integrations-company/tutorials/grant-accounting-approver-privileges)*.*
- **Considerations**

 - This feature affects all ERP-integrated projects within a company in Procore. It cannot be configured for only some ERP-integrated projects.
 - This feature can be enabled for one (1) or more of the following tools:

    - Commitments
    - Commitment Change Orders (CCOs)
    - Subcontractor Invoices
    - Owner Invoices *Notes:*

      - Availability of these options varies depending on the items supported for sync with your ERP integration. Not all ERP integrations support the sync of every item listed here.
      - Tool names can vary if your company has implemented a point of view dictionary. See [What tool names and terms are different in Procore for general contractors, owners, and specialty contractors?](/faq-what-tool-names-and-terms-are-different-in-procore-for-general-contractors-owners-and-specialty-contractors)
- **Prerequisites**

 - Your ERP integration must be configured to sync items from the tool for which the setting will be enabled/disabled.

##### Â important - limitation

Some integrations and customer implementations include custom fields that require an entry, or have limitations around the type or length of entry, for an object to successfully export. The Direct Export feature will attempt to initiate the export of such items, but in some cases clicking 'Send to ERP' will result in the item moving to the 'Ready to Export' page of the Company level ERP Integrations tool.

It is recommended that you check the 'Ready to Export' filter for such items after enabling this feature to ensure successful and timely exports.

**Example:**

- The VistaÂ® Integration by Procore can be configured to require selection of a Compliance Group for Commitments in the Company level ERP Integrations tool prior to export. Since a Compliance Group can't be selected on the Commitment when clicking the 'Send to ERP' button prior to export, that item will not export automatically. Approval will still be required in the Company level ERP Integrations tool.