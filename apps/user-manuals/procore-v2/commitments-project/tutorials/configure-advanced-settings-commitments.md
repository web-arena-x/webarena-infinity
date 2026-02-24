# Configure Advanced Settings: Commitments

Source: https://v2.support.procore.com/product-manuals/commitments-project/tutorials/configure-advanced-settings-commitments

---

## Background

Users who have been granted 'Admin' permission can customize the Commitment tool's advanced settings at the beginning of the project. These settings define how the Commitments tool works for your end-users. For example, you can select which users are on the tool's default distribution list, whether or not a purchase order or subcontract is set to 'Private' by default and more. Unless noted otherwise, settings can be adjusted at any time over the course of a project.

##### Â Important

- Before your project users start creating commitments, it is important to configure the **Number of Commitment Change Order Tiers** setting as described below. To learn more, see [What are the different change order tier settings in Project Financials?](/faq-what-are-the-different-change-order-tier-settings-in-project-financials)
- Once a user creates a [Commitment Change Order](/glossary-of-terms) on your project, you are NOT permitted to modify your default change order tier setting.

## Things to Consider

- [Required User Permissions](/product-manuals/commitments-project/permissions)
- **Additional Information**:

 - Additional configuration settings are available in the **Advanced Settings** tab of a commitment. See [Edit the Advanced Settings Tab on a Commitment](/product-manuals/commitments-project/tutorials/edit-the-advanced-settings-on-a-commitment).

## Prerequisites

- Your company must be licensed for Procore's Project Financials tools.
- Add the Commitments tool to the list of Project Tools. See [Add and Remove Project Tools](/product-manuals/admin-project/tutorials/add-and-remove-project-tools).
- Determine the number of change order tiers that you want to apply to your project. To learn more, see [What are the different change order tier settings in Project Financials?](/faq-what-are-the-different-change-order-tier-settings-in-project-financials)

## Steps

1. Navigate to the project's **Commitments** tool.
2. Click the **Configure Settings** icon.

   - Contract Configuration
   - Contract Dates
   - Default Distributions
   - Default Contract Settings

#### Contract Configuration

This table details the settings in the Contract Configuration area. Always click **Update** at the bottom of the page to save your changes.

| Setting | Type | **Description** |
| --- | --- | --- |
| Contracts Private by Default | Checkbox | Mark this box to make new subcontracts private by default. Only 'Admin' users on the Commitments tool and users on the 'Private' list can see a 'Private' commitment. Remove the mark to allow users with 'Read Only' permission or above to view commitments. See [Create a Commitment](https://support.procore.com/products/online/user-guide/project-level/commitments/tutorials/create-a-commitment). |
| Enable Purchase Orders | Checkbox | Mark this box to enable purchase order creation in the project's Commitments tool. This is the default setting. Users must have the required user permissions to create purchase orders. Remove the mark to disable this setting. See [Create Purchase Orders](/process-guides/materials-user-guide-with-financials/create-a-purchase-order). |
| Enable Contracts | Checkbox | Mark this box to provide users with the ability to create subcontracts. This is the default setting. Users must have the required user permissions to create subcontracts. Remove the mark to prevent users from creating subcontracts. See [Create Subcontracts](/product-manuals/commitments-project/tutorials/create-subcontracts). |
| RFQs Will be Due After | Numeric | The default value in Procore is seven (7) working days. Change this value to determine the RFQ due date for your project. Users can adjust the value on each commitment. See [Respond to an RFQ as an RFQ Recipient](/product-manuals/change-events-project/tutorials/submit-a-quote-as-a-collaborator). *Note:* A Procore Administrator can also set which days Procore considers working days. See [Set Project Working Days](/product-manuals/admin-project/tutorials/set-project-working-days). |
| Number of Commitment Change Order Tiers | Drop-down list | Choose this setting before creating commitments. Once a user creates a commitment change order, this setting cannot be modified. See [What are the different change order tier settings in Project Financials?](/faq-what-are-the-different-change-order-tier-settings-in-project-financials)   - One (1) tier is the default setting. - Two (2) tier requires your team to create a potential change order followed by a commitment change order. If you choose this option, the **Enable Always Editable Schedule of Values** check box appears. - Three (3) tier requires your team to create a potential change order, followed by a change order request, and then a commitment change order. |
| Allow Standard Level users to Create CCOs | Checkbox | This setting is only available when the one (1) tier change order tier setting is enabled. Mark this box to allow users with 'Standard' level permissions to create commitment change orders. See [Create a Commitment Change Order](/process-guides/materials-user-guide-with-financials/create-a-change-order-cco). Note: When ON, this setting also allows users with 'Standard' level permissions to approve their own workflows. |
| Allow Standard Level Users to Create PCOs | Checkbox | This setting is only available when the two (2) tier or three (3) tier change order tier setting is enabled. Mark this box to allow users with 'Standard' permissions to create potential change orders. Remove this mark to restrict creation of potential change orders to users with 'Admin' level permissions. See [Create a Commitment Potential Change Order](/product-manuals/commitments-project/tutorials/create-a-commitment-potential-change-order). |
| Enable Always Editable Schedule of Values | Checkbox | Mark this box to allow users to add, update, import, and remove line items from a schedule of values in any commitment status. Remove the mark to limit edits. See [Create a Subcontractor Invoice](/process-guides/invoice-administrator-guide/create-subcontractor-invoices). *Note:* This setting is NOT supported when your project is configured to use the tool or when the Subcontractor Schedule of Values tab is enabled. See [Enable or Disable the Subcontractor SOV Tab on the Commitments Tool](/product-manuals/commitments-project/tutorials/enable-or-disable-the-ssov-tab-on-the-commitments-tool). |
| Beta Enable Field Initiated Change Orders | Checkbox | In the Field-Initiated Change Orders beta program, this default ON setting allows collaborators to submit change orders from the field. It works with the two (2) or three (3) tier setting in the Commitments tool. If activated, 'Allow Standard Level Users to Create PCOs' must also be marked. See [Allow Collaborators to Submit Field-Initiated Change Orders](/product-manuals/commitments-project/tutorials/allow-collaborators-to-submit-field-initiated-change-orders). *Note:* This setting is only available to participants in the beta program for [(Beta) Commitments: Allow Collaborators to Submit Field-Initiated Change Orders](https://support.procore.com/tc/procore/Legacy/Release%5FDocumentation%5FArchives/2022/Commitments:%5FAllow%5FCollaborators%5Fto%5FSubmit%5FField-Initiated%5FChange%5FOrders). |
| Beta Compliance Template | Checkbox | For companies with [Procore Pay](https://support.procore.com/products/online/procore-pay), choose one of your company's custom compliance templates from the drop-down list. This determines the compliance template for the project's 'Compliance' tab in the Commitments tool. See [Manage Compliance as an Administrator for the Payor](https://support.procore.com/products/online/user-guide/company-level/payments/tutorials/manage-compliance-as-an-administrator-for-the-payor). *Note:* This setting is only available to beta program participants with Procore Pay. For details, see [About Compliance Templates with Procore Pay (Beta)](https://support.procore.com/products/online/procore-pay/tutorials/about-compliance-templates-with-procore-pay). |

### Contract Dates

The Contract Date settings are in the Procore web application on the [Contract Fieldsets page](https://app.procore.com/11733/company/admin/configurable%5Ffield%5Fsets?configurable%5Ffield%5Fset%5Ftypes%5B%5D=ConfigurableFieldSet%3A%3APrimeContract&configurable%5Ffield%5Fset%5Ftypes%5B%5D=ConfigurableFieldSet%3A%3APurchaseOrderContract&configurable%5Ffield%5Fset%5Ftypes%5B%5D=ConfigurableFieldSet%3A%3AWorkOrderContract) in the Company Admin tool. To learn more, see [Which fields in the Commitments tool can be configured as required, optional, or hidden?](/faq-which-fields-in-the-commitments-tool-can-be-configured-as-required-optional-or-hidden)

### Default Distributions

This table details the settings in the Default Distributions area. Always click **Update** at the bottom of the page to save your changes.

| Setting | Type | **Description** |
| --- | --- | --- |
| Include Primary Contact in Default Distribution | Checkbox | Mark this checkbox to automatically include the person listed as the company's Primary Contact in the Directory tool in the default distribution list. *Note*: To be included on the distribution list, the vendor record must have a designated primary contact in the Company Directory. See [Add a Person to the Company Directory](/product-manuals/directory-company/tutorials/add-a-user-account-to-the-company-directory). |
| Commitment Distribution | Drop-down list | Select any user names from the Project Directory. Procore automatically adds the people to the distribution list for the purchase order or subcontract. |
| Commitment Change Order Distribution | Drop-down list | Select any Procore user(s) that should always be added to a commitment change order's distribution list by default when a change order is sent by email. |
| Request for Quote Distribution | Drop-down list | Select users to be notified when RFQ responses are submitted. *Note*: You have the ability to also modify the Request for Quote distribution within the RFQ. |
| Invoice Distribution | Drop-down list | When an invoice or the subcontractor SOV is submitted for a commitment, the user(s) and contact(s) listed in the Invoice Distribution list will receive an email when the status of either the Invoice or the subcontractor SOV is set to *Under Review*. |

### Default Contract Settings

This table details the settings in the Default Contract Settings area. Always click **Update** at the bottom of the page to save your changes.

| Setting | Type | **Description** |
| --- | --- | --- |
| Default Accounting Method for Purchase Orders | Drop-down list | Select *Unit/Quantity Based* (default setting) or *Amount Based*. Procore automatically applies the accounting method to the purchase orderâs invoices. |
| Default Accounting Method for Contracts | Drop-down list | Select *Unit/Quantity Based* or *Amount Based* (default setting). Procore automatically applies the accounting method to the subcontract's invoices. |
| Default Retainage Percent | Numeric | Enter a percentage amount (for example, 10%) to set the default [retainage](/glossary-of-terms) percentage on the contract's **first** invoice. If you do NOT change this setting using the steps in [Set or Release Retainage on a Subcontractor Invoice](/product-manuals/invoicing-project/tutorials/set-or-release-retainage-on-a-subcontractor-invoice), this setting will remain in effect on subsequent invoices.   - The percentage amount that you enter in the 'Default Retainage Percent' field calculates the retainage amounts on the contract's **first** invoice. - After creating your contract's first invoice, it is important to note that changing the 'Default Retainage Percent' value does NOT automatically change the retainage percentage on the contract's subsequent invoices. - To change the retainage percentage on subsequent invoices, you must change the setting in the invoice. For instructions, see in [Set or Release Retainage on a Subcontractor Invoice](/product-manuals/commitments-project/tutorials/set-or-release-retainage-on-a-subcontractor-invoice-legacy). - It is important to note that a new invoice always inherits the retainage percentage from the previous invoice. For example, if you set the retainage on Invoice #1 to 10%, Invoice #2 will automatically use the 10% setting. If you decide to change the retainage set on Invoice #2 from 10% to 5%, Invoice #3 will automatically use 5%. - If your company has enabled the [sliding scale retention](/glossary-of-terms) feature, the 'Default Retainage Percent' setting is always overridden by your contract's sliding scale retention settings. See [Enable Sliding Scale Retention Rules on a Commitment's Invoices](/product-manuals/commitments-project/tutorials/enable-sliding-scale-retention-rules-on-subcontractor-invoices). |
| Enable Comments by Default | Checkbox | Mark this checkbox to enable a Comments tab to add comments and attach files. This checkbox is cleared by default. |
| Enable Financial Markup By Default | Checkbox | If enabled, you will see the Financial Markup tab, so you can set up and apply markup for each commitment. Change Orders will automatically be associated with the correct cost code so changes are accurately reflected in the Budget tool. |
| Enable Payments By Default | Checkbox | To prevent users from being able to create payments, leave this box unchecked. It's checked by default. |
| Enable Invoices by Default | Checkbox | If enabled, you will see the Invoices subtab so that invoices can be created. To prevent users from being able to create invoices, leave this box unchecked. It's checked by default. |
| Show Cost Codes on Invoice PDF by Default | Checkbox | Mark this checkbox to show cost codes on invoice PDFs by default. |
| Enable Stored Material Retainage By Default | Checkbox | Mark this checkbox to enable stored material retainage by default. To learn more, see [About Stored Materials on Invoices](https://support.procore.com/products/online/user-guide/project-level/invoicing/tutorials/about-stored-materials-on-invoices). |
| Enable Completed Work Retainage By Default | Checkbox | Mark this checkbox to enable completed work retainage by default. To learn more, see [About Stored Materials on Invoices](https://support.procore.com/products/online/user-guide/project-level/invoicing/tutorials/about-stored-materials-on-invoices). |
| Enable Subcontractor SOV by Default | Checkbox | Mark this checkbox to enable the 'Subcontractor SOV' tab on the project's commitments. See Create a Subcontractor Schedule of Values. |

ââââââ