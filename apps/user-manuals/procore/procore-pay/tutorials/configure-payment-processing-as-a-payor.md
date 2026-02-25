# Configure Payment Processing as a Payor

Source: https://v2.support.procore.com/product-manuals/procore-pay/tutorials/configure-payment-processing-as-a-payor

---

##### Â General Availability in Select Markets (United States)

[Procore Pay](https://www.procore.com/pay)  is available in the United States. It is designed for General Contractors and Owner-Builders who act as their own General Contractors on a job. Procore Pay extends the [Invoice Management](https://www.procore.com/invoice-management) functionality in the Procore web application to handle the payment process between general and specialty contractors.

## Background

When managing your company's Payment Settings for Procore Pay, the Payments Processing tab in the Company level Payments tool provides your Payments Admin with a way to manage:

- Your company's funding accounts
- Your company's Payments Disbursers
- The status of Procore Pay on your company's Procore projects
- The default funding accounts for your company's Procore projects

It also lets you turn the disbursements feature ON/OFF and review a change history that logs all the actions performed in the Company level Payments tool.

## Things to Consider

- [Required User Permissions](/product-manuals/procore-pay/permissions)

## Prerequisites

- [Add or Remove Payments Admins as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-or-remove-payments-admins)

## Steps

To learn about the options on each page of the Payments Processing tab, navigate to the Company level **Payments** tool and click the **Payments Settings**  icon. This opens the Payments Settings page. The Funding Accounts tab is active by default. On the left side of the page, the table contains links to the following pages:

- Funding Accounts
- Payments Permissions
- Project Controls
- Advanced Settings
- Change History

#### Funding Accounts

Only a 

In Procore Pay, a *Payments Admin* is a designated Procore user who administers the Company level Payments tool for that company's Procore account. Typically, one (1) or a small number of trusted users are designated to perform the tasks associated with this role.

Payments Admin can manage and link funding accounts to Procore Pay. In the payor environment, a *funding account* is the external bank account from which your company's drawdown funds are requested to pay a disbursement.

##### Â Important

- Account verification for Procore Pay is done using a commercially available database/registry of bank account information. Procore Pay stores only the account's **Nickname**, **Bank ID**, and **Next Check Number** entered by your Payments Admin. This provides Payments Disbursers with a method to identify the correct account for transmitting payments. Identifying bank account information is never entered nor stored in Procore Pay or any other Procore product.
- Account verification is done by an embedded software platform that provides Procore Pay users with an integrated money movement solution.

**Click here to learn about the table.**

##### Funding Accounts Page

The table below describes the elements in the Funding Accounts page.

*\* Procore is a financial technology company, not a bank. Banking services provided by Goldman Sachs Bank USA, a member of the Federal Reserve System and member FDIC. Additional Goldman Sachs Bank USA services may be accessed on its Transaction Banking online platform by visiting* <https://txb.gs.com/cx/login>*. Goldman Sachs accounts and services are subject to its terms and conditions.*

| **Element** | **Options** | **Description** | **Learn More** |
| --- | --- | --- | --- |
| Add Funding Account | Button | Click this button to add a new funding account to Procore Pay | - [Add Funding Accounts as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-funding-accounts) |
| Account Nickname | Account Nickname and last four (4) digits. | An account nickname shows only enough bank information so your company's Payment Disbursers can select the appropriate funding account to route payments. | - [Add Funding Accounts as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-funding-accounts) - [Create Disbursements](/process-guides/payments-admin-guide/create-disbursements) |
| Bank ID | A unique bank ID is created when linking an account. | Show the ID number assigned to the bank. | - [Add Funding Accounts as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-funding-accounts) |
| Next Check No. | A unique check number is used to create a new check number on a payment. | Shows the next number that Procore Pay assigns to the next check. Check numbers are applied to the invoice payments in a disbursement. | - [Add Funding Accounts as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-funding-accounts) |
| Added By | Only a Payments Admin can add funding accounts to Procore Pay. | Shows the name of the Payment Admin that added the account to Procore Pay. | - [Add Funding Accounts as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-funding-accounts) |
| Account State | *Default* or *Deactivated* | Provides a visual cue to quickly identify your company's default withdrawal account and any deactivated accounts. | - [Set a Default Funding Account as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/set-a-default-funding-account) - [Deactivate Funding Accounts as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/deactivate-accounts) |
| Verification Status | *Verified*, *Pending*, *Failed* | Provides a visual cue to quickly identify the verification status of each linked funding account. |  |
| Overflow | *Edit*, *Deactivate* | Click the **Overflow**    menu icon and choose one of the available options from the drop-down list. | - [Edit Funding Accounts as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/edit-funding-accounts) - [Deactivate Funding Accounts as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/deactivate-accounts) |

---

#### Payments Permissions

With the controls on the Payments Permission page, a Payments Admin securely controls who has access to create and view disbursements in the payor environment. There are two (2) roles in Procore Pay: *Payments Admin* and *Payments Disburser*. Only a member of Procore's Payments Operations Team can add a Payments Admin to your account. This requires an authorized user at your company to complete, sign, and return the Payment Administrator Designation Form to Procore. For details see, [Add or Remove Payments Admins as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-or-remove-payments-admins). Once added, only your Payments Admin can add your company's Payments Disbursers.

The illustration below shows you the Payments Permissions page.

**Click here to learn about the table.**

##### Payments Permissions Page

The tables below detail the elements in the Payments Permissions page.

| Table | Column | Description | Learn More... |
| --- | --- | --- | --- |
| **Payments Admins** | Payments Admins | Shows the first and last names of the users at your company who are designated as Payment Admins. *To designate a Payments Admin in the payor environment, an authorized user from your company must complete, sign, and return a Payment Administrator Designation Form to Procore. To remove a Payments Admin, contact your*  Procore point of contact  *. Payment Admins can only be removed by the Procore Payments Operations team.* | [Add or Remove Payment Admins as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-or-remove-payments-admins) |
|  | Added On | Shows the date and time that the Procore Payment Operations Team added your company's authorized Payments Admin. |  |  |
| **Payments Disbursers** | Add Disbursers | Only a Payments Admin can see the **Add Disbursers** button. Click this button to add a new Payments Disburser. | [Add Payments Disbursers as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-disbursers) |
|  | Payments Disbursers | Shows the first and last name of each disburser. |  |  |
|  | Added On | Shows the date, time, and timezone that the Payments Admin added the disburser. |  |  |
|  |  | Only a Payments Admin can remove a disburser. Click the    **remove** icon next to the user's name to revoke the disburser's access. | [Remove Payments Disbursers as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/remove-disbursers) |  |
| **Payments Beneficary Approvers** | Add Beneficiary Approvers | Only a Payments Admin can see the **Add Beneficiary Approvers** button. Click this button to add a new Payments Disburser. | [Add a Payments Beneficiary Approver as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-beneficiary-approvers) |
|  | Added On | Shows the date, time, and timezone that the Payments Admin added the approver. |  |  |
|  |  | Only a Payments Admin can remove a disburser. Click the    **remove** icon next to the user's name to revoke the approver's access. |  |  |

---

#### Project Controls

Payments Admins can use the Project Controls page in the Payments Processing tab of the Payment Settings to control how Procore Pay works on your existing Procore projects. With the controls on this page, you can make changes to projects individually or in bulk. With the controls on this page, you can:

- Turn Procore Pay ON or OFF on Procore Projects
- Change the Funding Account on Procore Projects

The illustration below shows you the Project Controls page. For a list of available tasks, see [Manage Project Controls](/product-manuals/procore-pay/tutorials/manage-payments-project-controls-for-a-single-project).

**Click here to learn about the table.**

##### Project Controls Page

The table below details the elements on the Project Controls page.

| Element | Type | Description | Learn More |
| --- | --- | --- | --- |
| **Search** | Field | Type your keyword(s) in the **Search** field and click the    magnifying glass or press ENTER to show projects or funding accounts matching your entry. *Note:* Procore Pay searches the entries in the Project, Pay, and Bank Account columns for matches. | - |
| **Edit Pay** | Button with a drop-down list | Procore Pay enables this button after you mark one (1) or more project checkboxes in the list. When enabled, you can change the **Pay** status on the selected project(s). *Enabled* indicates the Procore Pay features are turned ON on a project. *Disabled* indicates that the Procore Pay features are turned OFF on the project. | [Enable or Disable Procore Pay on Your Projects](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/enable-or-disable-pay) |
| **Edit Bank Account** | Button with a drop-down list | Procore Pay enables this button after you place a mark in one (1) or more project checkboxes in the list. When enabled, you can change the **Bank Account** setting on the selected project. The account nickname that you select here will automatically populate the 'Select a Bank Account' drop-down list when one of your company's Payments Disbursers creates a new disbursement. See [Create Disbursements](/process-guides/payments-admin-guide/create-disbursements). *Note:* If you choose the *Select at Disbursement* option, Payments Disbursers are required to select the appropriate bank account nickname on new disbursements. | [Update Your Project's Bank Accounts](/product-manuals/procore-pay/tutorials/manage-payments-project-controls-for-a-single-project) |
| **Line items** | Check box | Mark one or multiple checkboxes to enable the **Edit Pay** or **Edit Bank Account** button. Then select an option from the drop-down menu. | - |
| **Project** | Column | Shows the Procore project name. This list shows all projects marked 'Active' in your company's [Portfolio](https://support.procore.com/products/online/user-guide/company-level/portfolio). | [Change a Project's Status to Active or Inactive](/product-manuals/admin-project/tutorials/change-a-projects-status-to-active-or-inactive) |
| **Pay** | Column | Shows the project's **Pay** status. *Enabled* indicates the Procore Pay features are turned ON on a project. *Disabled* indicates that the Procore Pay features are turned OFF on the project. | [Update Your Project's 'Pay' Status](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/enable-or-disable-pay) |
| **Bank Account** | Column | Shows the account nickname for any funding accounts linked to Procore Pay. See [Add Funding Accounts](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-funding-accounts). The account nickname that you select here will automatically populate the 'Select a Funding Account' drop-down list when one of your company's Payments Disbursers creates a new disbursement. See [Create Disbursements](/process-guides/payments-admin-guide/create-disbursements). *Note:* If you choose the *Select at Disbursement* option, Payments Disbursers are required to select the appropriate bank account nickname on new disbursements. | [Add Funding Accounts as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-funding-accounts) |
| **Grand Totals** | Field | Shows the total number of projects where Procore Pay is enabled as a unit fraction. | - |

---

#### Advanced Settings

With the controls in the Advanced Settings page, a Payments Admin can enable and disable the Disbursements feature for Procore Pay. During the implementation process, this feature is enabled by default. Only your Payments Admin can change these settings.

- [Enable Disbursements](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/enable-disbursements)
- [Disable Disbursements](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/disable-disbursements)

The illustration below shows you the Advanced Settings page.

**Click here to learn about the table.**

##### Advanced Settings Page

The tables below detail the options when disbursements are turned ON or OFF on the Advanced Settings page.

| Users can perform this task... | ON | OFF | Learn More... |
| --- | --- | --- | --- |
| A Payments Admin can add disbursers. |  |  | [Add Payment Disbursers as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-disbursers) |
| A Payments Disburser can create a disbursement. |  |  | [Create Disbursements](/process-guides/payments-admin-guide/create-disbursements) |
| A Payments Admin can remove disbursers. |  |  | [Remove Payment Disbursers as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/remove-disbursers) |
| A Payments Admin or Payments Disburser can view a single disbursement or the disbursements list. |  |  | [View Disbursements as a Payor](https://support.procore.com/products/online/user-guide/company-level/payments/tutorials/view-disbursements-as-a-payor) |

---

#### Change History

Only a Payments Admin has access to view the Payments tool's Change History. The table on the Change History page logs the actions performed by Payments Admins and Payments Disbursers with the Company level Payments tool. For step-by-step instructions, see [View the Payments Tool Change History](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/view-history).

**Click here to learn about the table.**

##### Change History Page

The table below describes the default columns on the Change History page.

| **Column** | **Description** |
| --- | --- |
| **Date** | Shows the date and timestamp of the action. |
| **Action By** | Shows the first and last name of the Procore user as their name appears in the Company Directory. *Note:* Only a member of Procore's Payments Operations Team can add Payments Admins to your account. This requires an authorized user at your company to complete and sign Procore's Payment Administrator Designation Form. Once added, this entry indicates the user was added by 'Procore Support'. For details, see [Add or Remove Payments Admins as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-or-remove-payments-admins). |
| **Changed** | Provides a brief description of the action. |
| **From** | Shows the value that the action changed from. *Note:* If the action originated from a setting with a blank or null value, Procore shows the double dash symbol (--). |
| **To** | Shows the To value that the action changed to. *Note:* If the action resulted in a setting with a blank or null value, Procore shows the double dash symbol (--). |

ââââââ

---