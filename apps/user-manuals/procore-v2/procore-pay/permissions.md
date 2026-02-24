# Procore Pay

Source: https://v2.support.procore.com/product-manuals/procore-pay/permissions

---

Table of Contents

## Permissions

With Payments, General Contractors (payors) that are using Procore Pay to manage invoice payments, can pay subcontractors (payees) in Procore. Permissions differ based on task, and whether you are a payor or a payee.

For both payors and payees, some actions, not specifically related to payments, are accessible through permissions in other tools.

### Payors

As a **payor**, permissions to the Payment tool and its settings are managed in the company's Permissions tool. Additionally, there are two (2) supplemental **role-based permissions** that allow you to take actions within the payments tool. These role-based permissions are either set through a form request, or directly in the Payments tool:

- **Payments Admin**, which, due to the sensitive nature of payments, is provisioned by Procore after submitting a [request](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-or-remove-payments-admins).
- **Payments Disburser**, which is set in the Payments tool by a Payments Admin. See [Add Payments Disbursers as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-disbursers).
- **Payments Beneficiary Approver**, which is set in the Payments tool by a Payments Admin. See [Add Payments Beneficiary Approvers as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-beneficiary-approvers).

##### Permissions

Users can take action with this permission level.

Users can take action with this permission level AND one or more role-based permissions.

##### Â Note

To see the Payments tool in your menu, you need to have permissions for Payments set in the company's **Permissions tool**.

- **'Read Only'** level permissions allow you to see the tool and the subcontractor invoices tab. However, you cannot click any links in the subcontractor invoices tab.
- **'Standard'** level permissions give you 'Read Only' access and allow users to modify lien waivers and payment requirements via the subcontractor invoices tab.
- **'Admin'** level permissions give you the 'Standard' permissions and allow you to see the gear icon for tool settings. However, when you click on settings, you can only see the 'Payment Requirements' tab.

Additionally, users may need supplemental **role-based permission** in the Payments tool to take action.

- **Payments Disburser** allows you to see the 'Disbursements' tab.
- **Payments Admin** gives you the 'Payments Disburser' access. Additionally, you to see the 'Beneficiaries' tab as well as the 'Payments Processing' tab in the tool's settings.

| Action (Alphabetical) | Permissions Tool | Read Only | Standard | Admin | Notes |
| --- | --- | --- | --- | --- | --- |
| About Holds in Procore Pay  [Web](/product-manuals/procore-pay/tutorials/about-holds-in-procore-pay) |  |  |  | - Payments Admin  OR - Payments Disburser | Users with permissions on other Procore tools have limited permissions to manage holds in Procore Pay. For details, see Common Questions in [About Holds in Procore Pay](https://support.procore.com/products/online/user-guide/company-level/payments/tutorials/about-holds-in-procore-pay). |
| About the Beneficiaries Tab [Web](/process-guides/payments-beneficiary-approver-guide/about-the-beneficiaries-tab) |  |  |  | - Payments Admin  OR - Payments Beneficiary Approver | Invoice Administrators can invite a [payee](https://support.procore.com/products/online/user-guide/company-level/payments/glossary) to join Procore Pay as a [beneficiary](https://support.procore.com/products/online/user-guide/company-level/payments/glossary). |
| About the Disbursements Tab   [Web](/process-guides/payments-disburser-guide/about-the-disbursements-tab) |  |  |  | - Payments Admin  OR - Payments Disburser | [Company Admins](/faq-what-is-a-company-admin) can also access the the Subcontractor Invoices tab, but cannot create disbursements. |
| About the Payments Settings  [Web](/product-manuals/procore-pay/tutorials/about-the-payments-settings) |  |  |  | - Payments Admin  OR - Payments Disburser | [Company Admins](/faq-what-is-a-company-admin) can also access the Payment Settings page, but are limited to accessing Payment Requirements settings in the Payment Requirements tab. Payment Disbursers are limited to accessing the Payment Requirements settings in the Payment Settings tab. |
| About the Payments Tool   [Web](/product-manuals/procore-pay/tutorials/about-the-payments-tool) |  |  |  | - Payments Admin  OR - Payments Disburser | [Company Admins](/faq-what-is-a-company-admin) can also access the Payments tool, but are limited to accessing Payment Requirements settings in the Payment Requirements tab. Company Admins can also access the Subcontractor Invoices tab, but cannot create disbursements. Payments Disbursers can also access the Payment Beneficiary Approvers can only access the Beneficiaries tab to approve beneficiary bank accounts. |
| About the Subcontractor Invoices Tab [Web](/process-guides/payor-setup-guide/add-entities) |  |  |  | - Payments Admin  OR - Payments Disburser | [Company Admins](/faq-what-is-a-company-admin) can also access the Subcontractor Invoices tab. Only [Payments Admins](/process-guides/payor-setup-guide/authorize-payment-admins) and [Payment Disbursers](/process-guides/payor-setup-guide/add-payments-disbursers) can create disbursements. |
| Add Business Entities as a Payor   [Web](/process-guides/payor-setup-guide/add-entities) |  |  |  | - Payments Admin |  |
| Add Funding Accounts as a Payor   [Web](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-funding-accounts) |  |  |  | - Payments Admin |  |
| Add Payments Beneficiary Approvers as a Payor   [Web](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-beneficiary-approvers) |  |  |  | - Payments Admin | To be added as a Payments Beneficiary Approver, you must have a [user account](/product-manuals/directory-company/tutorials/add-a-user-account-to-the-company-directory) in the Company level Directory and your account must be [added as an employee](/product-manuals/directory-company/tutorials/add-someone-as-an-employee-of-your-company). The user must also have 'Read Only' level permissions or higher on the Company level Directory tool. |
| Add Payments Disbursers as a Payor  [Web](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-disbursers) |  |  |  | - Payments Admin | To be added as a Payments Disburser, you must have a [user account](/product-manuals/directory-company/tutorials/add-a-user-account-to-the-company-directory) in the Company level Directory and your account must be [added as an employee](/product-manuals/directory-company/tutorials/add-someone-as-an-employee-of-your-company). In addition, you must be granted 'Read-Only' level permissions or higher to the Payments tool. |
| Add or Remove Payments Admins as a Payor   [Web](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-or-remove-payments-admins) | You must [contact Payment Operations](/reference-procore-pay-support) to manage your Payment Admins. | To request to add a Payments Admin, you must be an authorized signer on your company's transaction banking agreement for Procore Pay. You must also have a [user account](/product-manuals/directory-company/tutorials/add-a-user-account-to-the-company-directory) in the Company level Directory and your account must be [added as an employee](/product-manuals/directory-company/tutorials/add-someone-as-an-employee-of-your-company). |  |  |  |
| Add Subcontractor Invoices to a 'Draft' Disbursement   [Web](/product-manuals/procore-pay/tutorials/add-subcontractor-invoices-to-a-draft-disbursement) |  |  |  | - Payments Disburser  OR - Payments Admin |  |
| Approve a Beneficiary Bank Account as a Payor   [Web](/process-guides/payor-setup-guide/approve-beneficiary-accounts) |  |  |  | - Payments Admin  OR - Payments Beneficiary Approver |  |
| Approve or Reject a Disbursement with a Custom Payments Workflow   [Web](/product-manuals/procore-pay/tutorials/approve-or-reject-a-disbursement-with-a-custom-payments-workflow) |  |  |  | - Payments Disburser  OR - Payments Admin | Assignees of the disbursement's current workflow step can also take this action with 'Standard' or 'Read Only' on the Company level Admin tool with the optional 'View Complete Workflow History as a Workflow Participant,' 'View Previous Step Only', and 'Can Start Workflows' granular permissions on the company permissions template. |
| Assign a Default Workflow Template for Procore Pay   [Web](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/assign-a-default-template) |  |  |  | - Payments Admin |  |
| Authorize Disbursements  [Web](/product-manuals/procore-pay/tutorials/authorize-disbursements) |  |  |  | - Payments Disburser  OR - Payments Admin | To authorize a disbursement with a Payments Workflow, you must be the Workflow Approver on the final workflow step. See [Best Practices for Creating a Payments Workflow](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/best-practices). |
| Cancel Disbursements Before Authorization as a Payor  [Web](/process-guides/payments-disburser-guide/complete-the-transactional-mfa-challenge) |  |  |  | - Payments Admin  OR - Payments Disburser |  |
| Complete the Transactional MFA Challenge for Disbursements  [Web](/process-guides/payments-disburser-guide/complete-the-transactional-mfa-challenge) |  | - Payments Disburser  OR - Payments Admin | - Payments Disburser  OR - Payments Admin | - Payments Disburser  OR - Payments Admin |  |
| Configure Payment Processing as a Payor  [Web](/product-manuals/procore-pay/tutorials/configure-payment-processing-as-a-payor) |  |  |  | - Payments Admin |  |
| Configure Payment Requirements as a Payor  [Web](/process-guides/payor-setup-guide/configure-payment-requirements) |  |  |  | - Payments Admin | [Company Admins](/faq-what-is-a-company-admin) can also take this action. |
| Configure the Settings for a Payments Workflow Template   [Web](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/configure-a-template) |  |  |  | - Payments Admin | Users must also have 'Read Only', 'Standard', or 'Admin' level permissions on the [Workflows Tool](https://support.procore.com/products/online/user-guide/company-level/workflows). |
| Create Disbursements  [Web](/process-guides/payments-admin-guide/create-disbursements) |  |  |  | - Payments Disburser  OR - Payments Admin |  |
| Create Lien Waiver Templates  [Web](/process-guides/payor-setup-guide/create-lien-waiver-templates) |  |  |  |  | [Company Admins](/faq-what-is-a-company-admin) can also take this action. |
| Create and Apply a Manual Hold on a Subcontractor Invoice   [Web](/process-guides/payor-setup-guide/create--apply-payment-holds) |  |  |  | - Payments Disburser  OR - Payments Admin | [Company Admins](/faq-what-is-a-company-admin) and [Invoice Administrators](/process-guides/payor-setup-guide/add-invoice-administrators) can only create Invoice Holds. For details, see [What permissions do you need to manage holds on subcontractor invoices?](/faq-what-is-a-manual-hold-on-a-subcontractor-invoice) |
| Customize the Payment Controls for Your Active Projects   [Web](/product-manuals/procore-pay/tutorials/manage-payments-project-controls-for-a-single-project) |  |  |  | - Payments Admin |  |
| Deactivate Funding Accounts as a Payor  [Web](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/deactivate-accounts) |  |  |  | - Payments Admin |  |
| Delete Lien Waiver Templates  [Web](/process-guides/payments-disburser-guide/delete-lien-waiver-templates) |  |  |  |  | [Company Admins](/faq-what-is-a-company-admin) can also take this action. |
| Disable Disbursements  [Web](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/disable-disbursements) |  |  |  | - Payments Admin |  |
| Edit Funding Accounts as a Payor  [Web](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/edit-funding-accounts) |  |  |  | - Payments Admin |  |
| Edit Lien Waiver Templates  [Web](/process-guides/payments-disburser-guide/edit-lien-waiver-templates) |  |  |  |  | [Company Admins](/faq-what-is-a-company-admin) can also take this action. |
| Edit a Manual Hold on an Invoice from the Payments Tool  [Web](/process-guides/invoice-administrator-guide/edit-holds) |  |  |  |  | Users must also be either a [Company Admin](/faq-what-is-a-company-admin) or a [Project Admin](/faq-what-is-a-project-administrator) to take this action. |
| Enable Disbursements  [Web](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/enable-disbursements) |  |  |  | - Payments Admin |  |
| Enable Procore Pay as a Payor  [Web](/process-guides/payor-setup-guide/enable-procore-pay) |  |  |  |  | Procore assigns an Implementation Project Manager to oversee the Procore Pay implementation process with your team. |
| Enable or Disable Procore Pay on Your Projects  [Web](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/enable-or-disable-pay) |  |  |  | - Payments Admin |  |
| Enable Lien Waivers in the Company Payments Tool  [Web](/process-guides/payor-setup-guide/enable-lien-waivers) |  |  |  | - Payments Disburser  OR - Payments Admin |  |
| Export Subcontractor Invoices from the Payments Tool  [Web](/process-guides/payments-admin-guide/export-a-list-of-invoices) |  |  |  | - Payments Admin | Users also nee [invoice administrator](/process-guides/payor-setup-guide/add-invoice-administrators) permissions on the project to view invoices. |
| Log in to Procore Pay with Multi-Factor Authentication  [Web](/process-guides/payments-disburser-guide/log-in-to-procore-pay-with-mfa) |  | - Payments Disburser  OR - Payments Admin | - Payments Disburser  OR - Payments Admin | - Payments Disburser  OR - Payments Admin |  |
| Manage Advanced Settings for Payment Processing |  |  |  | - Payments Admin |  |
| Manage Business Entities as a Payor  [Web](https://support.procore.com/products/online/user-guide/company-level/payments/tutorials/manage-business-entities-as-a-payor) |  |  |  | - Payments Admin |  |
| Manage Project Controls   [Web](/product-manuals/procore-pay/tutorials/manage-payments-project-controls-for-a-single-project) |  |  |  | - Payments Admin |  |
| Manage Project Controls in Bulk  [Web](/product-manuals/procore-pay/tutorials/manage-project-controls-in-bulk) |  |  |  | - Payments Admin |  |
| Manage Rows & Columns on the Subcontractor Invoices Tab  [Web](/process-guides/payments-admin-guide/manage-rows--columns) |  |  |  |  |  |
| Open Invoices in the Payments Tool  [Web](/product-manuals/procore-pay/tutorials/open-invoices-in-the-payments-tool) |  |  |  |  | Users must also have access to the invoice. |
| Preview Lien Waivers on Subcontractor Invoices  [Web](/process-guides/invoice-administrator-guide/preview-lien-waivers) |  |  |  |  | You must also be an [invoice administrator](/process-guides/payor-setup-guide/add-invoice-administrators). Locked unconditional lien waivers are only visible after they have been unlocked. |
| Release a Manual Hold on an Invoice from the Payments Tool  [Web](/process-guides/invoice-administrator-guide/release-holds) |  |  |  |  | Users must also be either a [Company Admins](/faq-what-is-a-company-admin) or a [Project Admin](/faq-what-is-a-project-administrator) to take this action. |
| Remove Payments Beneficiary Approvers as a Payor   [Web](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/remove-beneficiary-approvers) |  |  |  | - Payments Admin |  |
| Remove Payments Disbursers as a Payor  [Web](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/remove-disbursers) |  |  |  | - Payments Admin |  |
| Review Sub-Tier Lien Waivers as an Invoice Administrator  [Web](/process-guides/invoice-administrator-guide/review-sub-tier-lien-waivers-as-an-invoice-administrator) |  |  |  |  |  |
| Search for and Apply Filters on the Subcontractor Invoices Tab  [Web](/process-guides/payments-admin-guide/apply-search--filter-options) |  |  |  |  |  |
| Set Up MFA for Procore Pay on Your Device  [Web](/process-guides/payor-setup-guide/set-up-mfa-on-a-mobile-device) |  | - Payments Disburser  OR - Payments Admin  OR - Payments Beneficiary Approver | - Payments Disburser  OR - Payments Admin  OR - Payments Beneficiary Approver | - Payments Disburser  OR - Payments Admin  OR - Payments Beneficiary Approver |  |
| Set a Default Funding Account as a Payor  [Web](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/set-a-default-funding-account) |  |  |  | - Payments Admin |  |
| View Business Entities & Accounts as a Payor   [Web](/product-manuals/procore-pay/tutorials/view-business-entities-and-accounts-as-a-payor) |  |  |  | - Payments Admin |  |
| View Funding Accounts as a Payor  [Web](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/view-business-entities--funding-accounts) |  |  |  | - Payments Admin |  |
| View Payment Requirements as a Payor  [Web](/process-guides/payments-admin-guide/view-payment-requirements) |  |  |  | - Payments Admin  OR - Payments Disburser |  |
| View the Payment Requirements Change History  [Web](/product-manuals/procore-pay/tutorials/view-the-payment-requirements-change-history) |  |  |  | - Payments Admin  OR - Payments Disburser |  |
| View Payments Permissions as a Payor  [Web](/process-guides/payments-admin-guide/view-payment-permissions) |  |  |  | - Payments Admin |  |
| View Signed Lien Waivers on Subcontractor Invoices  [Web](/product-manuals/procore-pay/tutorials/view-signed-lien-waivers-on-subcontractor-invoices) |  |  |  |  | You must also be an [invoice administrator](/process-guides/payor-setup-guide/add-invoice-administrators). Locked unconditional lien waivers are only visible after they have been [unlocked](/product-manuals/procore-pay/tutorials/unlock-a-signed-unconditional-lien-waiver-as-an-invoice-contact). |
| View Sub-Tier Information on a Subcontractor Invoice  [Web](/process-guides/invoice-administrator-guide/view-sub-tier-information-on-a-subcontractor-invoice) |  |  |  |  |  |
| View a Disbursement  [Web](/process-guides/payments-disburser-guide/view-a-disbursement) |  | - Payments Disburser  OR - Payments Admin | - Payments Disburser  OR - Payments Admin | - Payments Disburser  OR - Payments Admin |  |
| View a Disbursements List  [Web](/process-guides/payments-disburser-guide/view-a-disbursements-list) |  | - Payments Disburser  OR - Payments Admin | - Payments Disburser  OR - Payments Admin | - Payments Disburser  OR - Payments Admin |  |
| View the Payments Tool Change History  [Web](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/view-history) |  |  |  | - Payments Admin |  |

#### Admin Tool

##### Â Important

Permissions for these actions are set in the Company level Permissions tool.

Users can take the action with this permission level. If permissions are marked for both tools, a user needs one marked permissions from each section to take the action.

**EXAMPLE**

To create and apply a manual hold on an invoice from the Commitments tool, users need:

- 'Read Only' level permissions or higher for the Payments tool.  
   AND
- 'Admin' level permissions on the Company level Admin tool.

| Action (Alphabetical) | Payments Tool | Company Admin Tool |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Read Only | Standard | Admin | Read Only | Standard | Admin |
| Beta Add Required Compliance Documents to Compliance Templates  [Web](/process-guides/about-the-compliance-tab-on-subcontractor-invoices-with-procore-pay/add-requirements) |  |  |  |  |  |  |
| Beta Change Compliance Template Names  [Web](/product-manuals/procore-pay/tutorials/change-compliance-template-names) |  |  |  |  |  |  |
| Beta Create Compliance Templates as a Company Admin  [Web](/process-guides/about-the-compliance-tab-on-subcontractor-invoices-with-procore-pay/create-templates) |  |  |  |  |  |  |
| Beta Edit or Delete Required Compliance Documents from Compliance Templates  [Web](/process-guides/about-the-compliance-tab-on-subcontractor-invoices-with-procore-pay/delete-compliance-docs) |  |  |  |  |  |  |

#### Commitments Tool

| Action (Alphabetical) | Payments Tool | Commitments Tool |  |  |  |  | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Read Only | Standard | Admin | Read Only | Standard | Admin |  |
| About Holds in Procore Pay  [Web](https://support.procore.com/products/online/user-guide/company-level/payments/tutorials/about-holds-in-procore-pay) |  |  |  |  |  |  | Users with 'Admin' level permissions on the Commitments or Payments tools can create, edit, view, or release *Invoice Holds*. In addition, they can only view *Vendor Holds*. |
| Accept of Decline an Invite to Bill as an Invoice Contact  [Web](/product-manuals/invoicing-project/tutorials/accept-or-decline-an-invite-to-bill-as-an-invoice-contact) |  |  |  |  |  |  | The payor must designate the user as the Invoice Contact on the commitment. Some payors choose to provide invoice contacts with 'Standard' level permissions on the Commitments tool. It is important to note that providing external collaborators with permissions higher than 'Read Only' level permissions is not recommended by Procore. |
| Add Sub-Tier Subcontractor Information to Commitments  [Web](/product-manuals/procore-pay/tutorials/add-sub-tier-subcontractor-information-to-commitments) |  |  |  |  |  |  |  |
| Add Sub-Tier Information for a Subcontractor Invoice  [Web](/process-guides/invoice-administrator-guide/add-sub-tier-information-for-a-subcontractor-invoice) |  |  |  |  |  |  |  |
| Configure a Compliance Template in Commitment Settings   [Web](/product-manuals/commitments-project/tutorials/configure-advanced-settings-commitments) |  |  |  |  |  |  |  |
| Create and Apply a Manual Hold on an Invoice from the Commitments Tool [Web](/process-guides/payor-setup-guide/create--apply-payment-holds) |  |  |  |  |  |  |  |
| Create Contract Compliance Documents for Commitments as an Invoice Administrator  [Web](/process-guides/invoice-administrator-guide/create-contract-documents--statuses) |  |  |  |  |  |  |  |
| Create a Subcontractor Invoice on Behalf of an Invoice Contact  [Web](/product-manuals/invoicing-project/tutorials/create-an-invoice-on-behalf-of-an-invoice-contact) |  |  |  |  |  |  |  |
| Create a New Subcontractor Invoice as an Invoice Contact  [Web](/product-manuals/invoicing-project/tutorials/create-a-new-subcontractor-invoice-as-an-invoice-contact) |  |  |  |  |  |  | Use this method if your 'Invite to Bill' is lost or missing (or if you are unsure whether an invoice administrator sent one). Some payors choose to provide invoice contacts with 'Standard' level permissions on the Commitments tool. It is important to note that providing external collaborators with permissions higher than 'Read Only' level permissions is not recommended by Procore. |
| Edit a Manual Hold on a Subcontractor Invoice as a Payor  [Web](/process-guides/invoice-administrator-guide/edit-holds) |  |  |  |  |  |  |  |
| Enable Lien Waivers and Set Default Templates on Projects  [Web](/process-guides/payor-setup-guide/enable-templates-on-projects) |  |  |  |  |  |  |  |
| Enable Sub-Tier Waivers on Subcontractor Invoices as an Invoice Administrator [Web](/process-guides/payor-setup-guide/enable-sub-tier-waivers) |  |  |  |  |  |  |  |
| Generate Lien Waivers on Subcontractor Invoices  [Web](/process-guides/invoice-administrator-guide/generate-lien-waivers) |  |  |  |  |  |  |  |
| Invite Beneficiaries to Procore Pay from the Commitments Tool  [Web](/process-guides/payor-setup-guide/invite-beneficiaries-to-pay) |  |  |  |  |  |  |  |
| Manage Contract Compliance Documents & Statuses for a Commitment  [Web](https://support.procore.com/products/online/procore-pay/tutorials/manage-contract-compliance-documents-and-statuses-for-a-commitment) |  |  |  |  |  |  | [Company Admins](/faq-what-is-a-company-admin) and [Project Admins](/faq-what-is-a-project-administrator) can also take this action. |
| Manage Insurance & Compliance Statuses for a Commitment  [Web](/process-guides/invoice-administrator-guide/manage-insurance-documents--statuses) |  |  |  |  |  |  | [Company Admins](/faq-what-is-a-company-admin) and [Project Admins](/faq-what-is-a-project-administrator) can also take this action. |
| Preview Lien Waivers on Subcontractor Invoices  [Web](/process-guides/invoice-administrator-guide/preview-lien-waivers) |  |  |  |  |  |  |  |
| Regenerate Lien Waivers on Subcontractor Invoices  [Web](/process-guides/payee-user-guide/regenerate-lien-waivers) |  |  |  |  |  |  |  |
| Release a Manual Hold on an Invoice from the Commitments Tool  [Web](/process-guides/invoice-administrator-guide/release-holds) |  |  |  |  |  |  |  |
| Send a New Invoice as an Invoice Contact with Procore Pay  [Web](/process-guides/payee-user-guide/preview-lien-waivers) |  |  |  |  |  |  | Some payors choose to provide invoice contacts with 'Standard' level permissions on the Commitments tool. It is important to note that providing external collaborators with permissions higher than 'Read Only' level permissions is not recommended by Procore. |
| Send a Request to Unlock a Signed Unconditional Lien Waiver  [Web](/process-guides/invoice-administrator-guide/request-to-unlock-signed-unconditional-waivers) |  |  |  |  |  |  |  |
| Upload Signed Lien Waivers on Subcontractor Invoices  [Web](/product-manuals/procore-pay/tutorials/upload-signed-lien-waivers-for-subcontractor-invoices) |  |  |  |  |  |  |  |
| Upload Sub-Tier Waivers to a Subcontractor Invoice as an Invoice Contact  [Web](/process-guides/payee-user-guide/upload-sub-tier-waivers) |  |  |  |  |  |  |  |
| View Payment Requirements on an a Subcontractor Invoice as an Invoice Administrator  [Web](/process-guides/invoice-administrator-guide/view-requirements) |  |  |  |  |  |  |  |