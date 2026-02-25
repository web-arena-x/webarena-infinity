# Yardi VoyagerÂ®

Source: https://v2.support.procore.com/product-manuals/yardi-voyager/detailed-data-mapping

---

Table of Contents

## Detailed Data Mapping

### Overview

| PROCORE | Exports data from Procore to Yardi VoyagerÂ® | Imports data from Yardi VoyagerÂ® to Procore | Yardi VoyagerÂ® | Notes |
| --- | --- | --- | --- | --- |
| [COMPANIES](#companiesvendors) |  |  | **VENDORS** | - Import companies by type, including those without a specified company type, from Yardi VoyagerÂ® to Procore. - Vendors marked as Credit Card Vendors are not supported. |
| [PROJECTS](#projectsjobs)  Cost Codes  Cost Types |  |  | **JOBS** Cost Categories Cost Codes | - The Yardi VoyagerÂ® integration supports linking Procore projects to Yardi VoyagerÂ® jobs. Before you can export a project from Procore, you must first create the corresponding job in Yardi VoyagerÂ®. Please see our [Yardi VoyagerÂ® Things to Know](/product-manuals/yardi-voyager/things-to-know) page for additional requirements. |
| [SUB JOBS](#sub-jobs)  Cost Codes  Cost Types |  |  | **JOBS**  Cost Categories  Cost Codes | - |
| [ORIGINAL BUDGET ESTIMATES](#original-budget-estimate) |  |  | **ORIGINAL BUDGETS** | - |
| [BUDGET CHANGES](#budget-changes) |  |  | **BUDGET REVISIONS** | - |
| [COMMITMENTS](#commitments) Subcontracts and Purchase Orders |  |  | **CONTRACTS** | - Interfaces (Plug-in Version 25) must be installed to successfully sync work retainage. |
| [COMMITMENT CHANGE ORDERS](#commitment-change-orders-ccos) |  |  | **CHANGE ORDERS** | - |
| [COMMITMENT INVOICES](#subcontractor-invoice) |  |  | **PAYABLES** | - Purchase Order Invoices are not included at this time. |
| [COMMITMENT PAYMENTS ISSUED](#paid-invoices) |  |  | **PAID INVOICES** | - |
| [DIRECT COSTS](#direct-costs) |  |  | **PAYABLES JOURNAL ENTRIES** | - Direct costsfor line items with contract IDs are imported as subcontractor invoices, while those without contract IDs are imported as invoices. - Direct costs imported from journal entries will be split into separate direct cost transactions in Procore for each job or sub job. - Due to a Yardi VoyagerÂ® update, Job Cost adjustment functionality is not available at this time. |

### Projects/Jobs

Yardi VoyagerÂ® only supports the linking of projects that originate from Procore's Estimating and Bidding tools. This requirement only applies to projects that begin in Procore. Please see our [Yardi VoyagerÂ® Things to Know](/product-manuals/yardi-voyager/things-to-know) page for additional requirements.

| PROCORE | Exports data from Procore to Yardi VoyagerÂ® | Imports data from Yardi VoyagerÂ® to Procore | Yardi VoyagerÂ® |
| --- | --- | --- | --- |
| Job ID |  |  | Job ID |
| Property ID |  |  | Property ID |
| Project Name |  |  | Job Description |
| Status |  |  | Status |
| Address |  |  | Mailing Address |
| Cost Code |  |  | Cost Categories |
| Cost Type |  |  | Cost Code |

### Sub Jobs

Yardi VoyagerÂ® supports the import of sub jobs only. Sub job exports are not available.

| PROCORE | Exports data from Procore to Yardi VoyagerÂ® | Imports data from Yardi VoyagerÂ® to Procore | Yardi VoyagerÂ® |
| --- | --- | --- | --- |
| Job ID |  |  | Job ID |
| Property ID |  |  | Property ID |
| Project Name |  |  | Job Description |
| Status |  |  | Status |
| Address |  |  | Mailing Address |
| Cost Code |  |  | Cost Categories |
| Cost Type |  |  | Cost Code |

### Companies/Vendors

| PROCORE | Exports data from Procore to Yardi VoyagerÂ® | Imports data from Yardi VoyagerÂ® to Procore | Yardi VoyagerÂ® |
| --- | --- | --- | --- |
| Company Name |  |  | Vendor Name |
| Address |  |  | Address |
| State |  |  | State |
| Email |  |  | Email |
| Phone |  |  | Phone |
| Only Active Vendors Sync |  |  | Is Active |

### Original Budget Estimate

| PROCORE | Exports data from Procore to Yardi VoyagerÂ® | Imports data from Yardi VoyagerÂ® to Procore | Yardi VoyagerÂ® |
| --- | --- | --- | --- |
| Original Budget |  |  | New Amount |
| Job ID |  |  | Job ID |
| Cost Code |  |  | Cost Categories |

### Budget Changes

##### Â Phased Release: Budget Changes

Some ERP integrated clients may have already transitioned from Budget Modifications (Legacy) to the new Budget Changes experience. The legacy experience will continue to be available until November 2024. To learn more about the timeline for migration, see [Common Questions](/process-guides/about-budget-changes/common-questions).

**Choosing to use the new Budget Changes experience will not impact the function of your ERP integration.** You should still thoroughly review the available documentation before migrating to the new experience. We recommend you also discuss any concerns or questions about migrating your Budget Modifications to Budget Changes with your Procore point of contact .

To learn more about the new Budget Changes experience, see [About Budget Changes](/process-guides/about-budget-changes/).

| PROCORE | Exports data from Procore to Yardi VoyagerÂ® | Imports data from Yardi VoyagerÂ® to Procore | Yardi VoyagerÂ® |
| --- | --- | --- | --- |
| Cost Code |  |  | Cost Code |
| Amount |  |  | Value |
| Date |  |  | Revision Date |
| Revision Number |  |  | Revision Number |
| Revision Type |  |  | Revision Type |
| Revision Status |  |  | Revision Status |

### Commitments

Yardi VoyagerÂ® supports the export of subcontracts and purchase orders.

| PROCORE | Exports data from Procore to Yardi VoyagerÂ® | Imports data from Yardi VoyagerÂ® to Procore | Yardi VoyagerÂ® |
| --- | --- | --- | --- |
| Contract Name |  |  | Contract Name |
| Title 1 |  |  | Title |
| Description |  |  | Remarks |
| Contract Company |  |  | Vendor |
| Status |  |  | Status |
| Executed |  |  | Executed |
| Start Date |  |  | Start Date |
| Contract Date |  |  | Contract Date |
| Estimated Completion Date |  |  | End Date |
| Retainage |  |  | Retention Percent |
| Cost Code |  |  | Cost Code |
| Amount |  |  | Contract Amount |

*1* *Commitment titles exceeding 30 characters will be truncated in* *Yardi VoyagerÂ®* *during export.*

### Commitment Change Orders (CCOs)

Yardi VoyagerÂ® supports the export of CCOs for subcontracts and purchase orders.

| PROCORE | Exports data from Procore to Yardi VoyagerÂ® | Imports data from Yardi VoyagerÂ® to Procore | Yardi VoyagerÂ® |
| --- | --- | --- | --- |
| Title |  |  | Description |
| Status |  |  | Status |
| Due Date |  |  | Date |
| Amount |  |  | Contract Amount |
| Commitment Retainage Percent |  |  | Retention Percent |
| Cost Code |  |  | Cost Code |

### Subcontractor Invoice

Yardi VoyagerÂ® supports the export of subcontractor invoices only. Purchase order invoice exports are not supported at this time. When an invoice is exported from Procore to Yardi VoyagerÂ®, it is automatically posted in the Accounts Payable (AP) module.

| PROCORE | Exports data from Procore to Yardi VoyagerÂ® | Imports data from Yardi VoyagerÂ® to Procore | Yardi VoyagerÂ® |
| --- | --- | --- | --- |
| Subcontractor Invoice |  |  | Subcontractor Invoice |
| Invoice Number |  |  | Invoice Number |
| Comments |  |  | Notes |
| Company |  |  | Vendor |
| Date |  |  | Date |
| Cost Code |  |  | Cost Code |
| Retention Amount |  |  | Retention Amount |

### Paid Invoices

Yardi VoyagerÂ® supports the import of paid subcontractor invoices.

| PROCORE | Exports data from Procore to Yardi VoyagerÂ® | Imports data from Yardi VoyagerÂ® to Procore | Yardi VoyagerÂ® |
| --- | --- | --- | --- |
| Invoice Number |  |  | Invoice Number |
| Amount |  |  | Amount Paid |
| Check Number |  |  | Check Number |
| Notes |  |  | Notes |
| Payment Type |  |  | Payment Method |
| Payment Date |  |  | Payment Date |
| Payment Number |  |  | Payment Number |

### Direct Costs

| PROCORE | Exports data from Procore to Yardi VoyagerÂ® | Imports data from Yardi VoyagerÂ® to Procore | Yardi VoyagerÂ® | Notes |
| --- | --- | --- | --- | --- |
| Received Date |  |  | Transaction Date | - The **Received Date** can be set to only come through from Non-Committed costs populating into the Direct Costs tool. See [Update General Project Information](../admin-project/tutorials/update-general-project-information.md#:~:text=Non%2DCommitment%20Costs,a%20configurable%20column.). |
| Company |  |  | Vendor |  |
| Status |  |  | Status |  |
| Description |  |  | Notes |  |
| Budget Code |  |  | Cost Code |  |
| Amount |  |  | Amount Paid |  |

### Procore Pay Payments

##### Â General Availability in Select Markets (United States)

[Procore Pay](https://www.procore.com/pay)  is available in the United States. It is designed for General Contractors and Owner-Builders who act as their own General Contractors on a job. Procore Pay extends the [Invoice Management](https://www.procore.com/invoice-management) functionality in the Procore web application to handle the payment process between general and specialty contractors.

| PROCORE | Exports data from Procore to Yardi VoyagerÂ® | Imports data from Yardi VoyagerÂ® to Procore | Yardi VoyagerÂ® |
| --- | --- | --- | --- |
| Amount |  |  | Amount Paid |
| Bank ID |  |  | Bank ID |
| Date Paid |  |  | Payment Date |
| Project Number |  |  | Property ID |
| Check Number |  |  | Check Number |
| Vendor Code |  |  | Payee ID |
| Invoice Number |  |  | Invoice Number |
| Notes |  |  | Notes |
| Payment Method |  |  | Payment Method |
| Payment Number |  |  | Payment Number |