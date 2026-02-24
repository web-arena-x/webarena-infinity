# About the Subcontractor Invoices Tab in the Payments Tool

Source: https://v2.support.procore.com/product-manuals/procore-pay/tutorials/about-the-subcontractor-invoices-tab-in-the-payments-tool

---

##### Â General Availability in Select Markets (United States)

[Procore Pay](https://www.procore.com/pay)  is available in the United States. It is designed for General Contractors and Owner-Builders who act as their own General Contractors on a job. Procore Pay extends the [Invoice Management](https://www.procore.com/invoice-management) functionality in the Procore web application to handle the payment process between general and specialty contractors.

## Background

Company Admins, Payment Admins, and Disbursers can use the table in the Subcontractor Invoices tab to view a list of all the invoices on the active, Pay-enabled projects in your company's Procore account. From this tab, Payments Disbursers or Payment Admins can track your payment requirements, view any manual holds applied to the invoice, and click links to launch the invoice in the Invoice Management tools. For each invoice, you can also view the Beneficiary Name, Project, Payment Requirements, and other billing information. You can also search the data table for a specific invoice, apply filters, and group line items. Only Payments Disbursers can create disbursements.

## Things to Consider

- [Required User Permissions](/product-manuals/procore-pay/permissions)

## Prerequisites

- [Add or Remove Payments Admins as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-or-remove-payments-admins)

## Key Features

- Subcontractor Invoices Table
- Default Columns
- Create Disbursement
- Manage Rows & Columns
- Apply Search & Filter Options
- Export a List

### Subcontractor Invoices Table

The key feature in the **Subcontractor Invoices** tab is the table, which lets you view all of the invoices in your Procore projects that you have been granted permission to see. To learn about the recommended permissions, see [What is a Payments Admin?](/process-guides/payor-setup-guide/authorize-payment-admins) and [What is a Payments Disburser?](/process-guides/payor-setup-guide/add-payments-disbursers)

This tab contains the following elements:

- **Export**. Click this button to export a list of subcontractor invoices.
- **Search**. Enter keywords or phrases to search the list for matching items.
- **Filters**. Click this button to adjust the page filters.
- **Select a Column to Group**. Choose one or more option(s) from this list to group the table rows by the option(s) selected.
- **Invoice Status.** Choose an option from this list to filter the data in the list by invoice status.
- **Payment Status**. Choose an option from this list to filter the data by payment status.

### Default Columns

This table details the default columns.

| **Column** | **Description** | **Default Setting** | **Learn More** |
| --- | --- | --- | --- |
| **Invoice #** | Click a hyperlink to open the corresponding invoice number at the Project level. Procore assigns an Invoice # at creation. *Note*: Users can also mark one (1) or more Invoice # checkboxes to activate the **Add to Disbursement** button to add invoices to *Draft* disbursements. See [Add Subcontractor Invoices to a 'Draft' Disbursement](/product-manuals/procore-pay/tutorials/add-subcontractor-invoices-to-a-draft-disbursement). | ON | [Create Subcontractor Invoices](/process-guides/invoice-administrator-guide/create-subcontractor-invoices) |
| **Payment Readiness: Requirements** | Displays a pie chart of the invoice's payment requirements. BLACK indicates all requirements are met, GRAY indicates incomplete requirements. A unit fraction shows completed payment requirements for each invoice. Click the link to view the invoiceâs payment requirements | ON | [Manage Payment Requirements](/product-manuals/procore-pay/tutorials/manage-payment-requirements-as-a-payor) |
| **Payment Readiness: Holds** | Shows the number of holds applied to an invoice. See [What is a manual payment hold on a project invoice?](/faq-what-is-a-manual-hold-on-a-subcontractor-invoice) | ON | [Manage Payment Holds](/faq-what-is-a-manual-hold-on-a-subcontractor-invoice) |
| **Payment Status** | Shows the current payment status of each invoice. The status options include: *Paid, Partially Paid,* or *Unpaid* | ON |  |
| **Disbursement No.** | Displays the disbursement number for the subcontractor invoice, if included in a disbursement. | ON | [Create Disbursements](/process-guides/payments-admin-guide/create-disbursements) |
| **Invoice Status** | Shows the current status of each invoice. Use the Project level Invoicing tool to change status. See [What are the default statuses for Procore invoices?](/faq-what-are-the-default-statuses-for-procore-invoices) | ON | [Bulk Edit the Status of Subcontractor Invoices with the Invoicing Tool](/product-manuals/invoicing-project/tutorials/bulk-edit-subcontractor-invoice-status-with-the-invoicing-tool) |
| **Beneficiary Name** | Shows the name of the payee. This corresponds to the 'Contract Company' set on the invoice's commitment contract. To change the company name, edit the **Name** field under the company's account profile in the Company level Directory tool. | OFF | [Edit a Company in the Company Directory](/product-manuals/directory-company/tutorials/edit-a-company-in-the-company-directory) |
| **Beneficiary Account Status** | Shows the onboarding status of the beneficiary. | ON |  |
| **Project** | Shows the name of the Procore project associated with each invoice. | ON | [Change the Name of a Procore Project](/product-manuals/admin-project/tutorials/change-the-name-of-a-procore-project) |
| **Billing Period** | Shows the invoice billing period. An invoice administrator creates billing periods. | ON | [Manage Billing Periods](/product-manuals/invoicing-project/tutorials/manage-billing-periods) |
| **Amounts Group** | Groups the 'Amount' columns in the table | ON | - |
| **Gross Amount** | Shows the total amount of the invoice before subtracting retainage. | ON | [Create a Commitment](/product-manuals/commitments-project/tutorials/create-a-commitment-change-order-cco) |
| **Net Amount** | Shows the actual cost of the invoice after subtracting retainage. | ON | [Create a Commitment](/product-manuals/commitments-project/tutorials/create-a-commitment-change-order-cco) |
| **Paid Amount** | Shows the amount paid against the invoice to date. | ON | [Create Subcontractor Invoices](/process-guides/invoice-administrator-guide/create-subcontractor-invoices) |
| **Invoice Dates** | Shows the dates entered as the Period Start and Period End on the invoice. These show the Billing Period Dates by default. You can change the dates. | ON | [Create Subcontractor Invoices](/process-guides/invoice-administrator-guide/create-subcontractor-invoices) |
| **Payment Date** | Shows the Payment Date entered on the invoice. | ON | [Create Subcontractor Invoices](/process-guides/invoice-administrator-guide/create-subcontractor-invoices) |
| **Submitted Date** | Shows the Submitted Date entered on the invoice. | ON | [Create Subcontractor Invoices](/process-guides/invoice-administrator-guide/create-subcontractor-invoices) |
| **Contract** | Click the hyperlink to launch the Project level Commitments tool and open the commitment. | ON | [View Commitments](/product-manuals/commitments-project/tutorials/view-commitments) |
| **Total Contract Amount** | Shows the commitment contract's total amount. | ON | [Create a Commitment](/product-manuals/commitments-project/tutorials/create-a-commitment-change-order-cco) |
| **% Complete** | Shows the percentage of Total Completed and Stored to Date as a % of the Total Amount of the Commitment Contract for the invoice. | ON | [Create Subcontractor Invoices](/process-guides/invoice-administrator-guide/create-subcontractor-invoices) |

### Create Disbursement

When you select more than one (1) checkbox as pictured above, the **Create Disbursement** button appears. To learn more, see [Create Disbursements](/process-guides/payments-admin-guide/create-disbursements).

### Manage Rows & Columns

To learn how to manage the rows and columns, see [Manage Rows & Columns on the Subcontractor Invoices Tab](/process-guides/payments-admin-guide/manage-rows--columns).

### Apply Search & Filter Options

To learn how to apply the search and filter options, see [Search for and Apply Filters on the Subcontractor Invoices Tab](/process-guides/payments-admin-guide/apply-search--filter-options).

### Export a List

To learn how to export a list of subcontractor invoices, see [Export Subcontractor Invoices from the Payments Tool](/process-guides/payments-admin-guide/export-a-list-of-invoices).