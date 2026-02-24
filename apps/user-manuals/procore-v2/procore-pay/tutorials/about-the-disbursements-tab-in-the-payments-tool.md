# About the Disbursements Tab in the Payments Tool

Source: https://v2.support.procore.com/product-manuals/procore-pay/tutorials/about-the-disbursements-tab-in-the-payments-tool

---

##### Â General Availability in Select Markets (United States)

[Procore Pay](https://www.procore.com/pay)  is available in the United States. It is designed for General Contractors and Owner-Builders who act as their own General Contractors on a job. Procore Pay extends the [Invoice Management](https://www.procore.com/invoice-management) functionality in the Procore web application to handle the payment process between general and specialty contractors.

## Background

A 

In Procore Pay, a *Payments Admin* is a designated Procore user who administers the Company level Payments tool for that company's Procore account. Typically, one (1) or a small number of trusted users are designated to perform the tasks associated with this role.

Payments Admin or 

In Procore Pay, a *Payments Disburser* is a Procore user granted permission to create and view disbursements in the Company level Payments tool. Because of the sensitive nature of payments, only a Payments Admin can add/remove disbursers.

Payments Disburser can use the options in the Disbursements tab to create and manage disbursements. On this tab, you can apply filters to the table to narrow down the disbursements to show only those that meet your criteria in the list. The table also provides important information about each disbursement, such as the Disbursement No. (which is assigned to the disbursement at creation), the bank account used to fund the disbursement, the amount of the disbursement, and the date and time it was created. To view a disbursement in more detail, click its **Disbursement No.** link.

## Things to Consider

- [Required User Permissions](/product-manuals/procore-pay/permissions)

## Prerequisites

- [Enable Disbursements](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/enable-disbursements)
- [Add Payments Disbursers as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-disbursers)

## Steps

1. Navigate to the Company level **Payments** tool.  
    The Subcontractor Invoices tab is active by default.
2. Click the **Disbursements** tab.   
   The key features and controls in the Disbursements tab include:

   - Filters
   - Default Columns
   - Optional Columns

     ##### Â Tip

     **Don't see the Disbursements tab?** Only a Payments Admin or Payments Disburser can view this tab. Your company's Payments Admin can assign users to the Payments Disburser role. See [Add Payments Disbursers as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-disbursers).

#### Filters

You can filter the table data using these options.

This table shows the filters available in the Disbursements tab.

| Element | Type | Description | Learn More |
| --- | --- | --- | --- |
| **Created On** | Drop-down list | Apply one (1) or more filters to show only those invoices on the list: *Last 30 Days*, *Last 60 Days*, *Year to Date*. | [Create Disbursements](/process-guides/payments-admin-guide/create-disbursements) |
| **Funding Account** | Drop-down list | Apply one (1) or more filters to show only those invoices related to the selected funding account. Accounts are managed by a Payments Admin. |  |
| **Drawdown Status** | Drop-down list | Apply one (1) or more filters to show only invoices in the selected statuses. |  |
| **Workflow Status** (Only available if your team has implemented a custom Payments workflow) | Drop-down list | Apply one of these filters to show only those invoices in the corresponding workflow status. To learn about statuses, see | [Best Practices for Creating a Payments Workflow](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/best-practices) |

#### Default Columns

This illustration shows you the default columns in the disbursements table.

This table details the default columns in the disbursements table.

| Element | Type | Description | Learn More... |
| --- | --- | --- | --- |
| **Disbursement No.** | Column | Shows the number assigned to a disbursement. | [Create Disbursements](/process-guides/payments-admin-guide/create-disbursements) |
| **Name** | Column | Shows the name assigned to a disbursement. | [Create Disbursements](/process-guides/payments-admin-guide/create-disbursements) |
| **Funding Account** | Column | Shows the name of the funding bank account that funded the disbursement. |  |
| **Aggregate Disbursement Amount** | Column | Shows the aggregate disbursement amount. This shows the grand total of all the payment amounts in a single disbursement. | [Create Disbursements](/process-guides/payments-admin-guide/create-disbursements) |
| **Drawdown Status** | Column | Shows the current drawdown status of a disbursement. |  |
| **Created By** | Column | Shows the name of the Payments Admin who created the disbursement. | [Create Disbursements](/process-guides/payments-admin-guide/create-disbursements) |
| **Created On** | Column | Shows the date the disbursement was created. | [Create Disbursements](/process-guides/payments-admin-guide/create-disbursements) |

#### Optional Columns

This table details the optional columns in the disbursements table.

| Element | Type | Description | Learn More... |
| --- | --- | --- | --- |
| **Workflow Status** (Only available if your team has implemented a custom Payments workflow) | Column | This column reflects the current workflow status of each disbursement. To learn about statuses, see | [Best Practices for Creating a Payments Workflow](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/best-practices) |