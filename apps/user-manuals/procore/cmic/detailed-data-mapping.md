# CMiC

Source: https://v2.support.procore.com/product-manuals/cmic/detailed-data-mapping

---

Table of Contents

## Detailed Data Mapping

### Overview

| PROCORE | Exports data from Procore to CMiC | Imports data from CMiC to Procore | CMiC | Notes |
| --- | --- | --- | --- | --- |
| **COMPANY LEVEL WBS CODES** COST CODES & COST TYPES | | | **MASTER COST CODES & CATEGORIES** | - Custom WBS segments are not supported at this time. - Project level cost codes must be added to the project from the Company level ERP Standard Cost Code List. New cost codes must be created in your ERP system, and cannot be created in Procore. |
| **PROJECT LEVEL WBS CODES** COST CODES & COST TYPES | | | **COST CODES & CATEGORIES** | - Custom WBS segments are not supported at this time. - Project level cost codes must be added to the project from the Company level ERP Standard Cost Code List. New cost codes must be created in your ERP system, and cannot be created in Procore. |
| **COMPANIES**   CUSTOMERS | | | **BUSINESS PARTNERS/VENDORS CUSTOMERS** | - Import companies by type, including those without a specified company type, from CMiC to Procore. |
| **PROJECTS** | | | **CONTROL JOBS** | |
| **SUB JOBS** | | | **JOBS** | |
| **BUDGET** | | | **BUDGETED COST AMOUNT** | - Budgets containing line items with $0 values can be exported from Procore to CMiC. |
| **BUDGET MODIFICATIONS (LEGACY)** OR **BUDGET CHANGES (NEW)** | | | **UPDATES CURRENT BUDGET AMOUNT** **POTENTIAL CHANGE ITEM (PCI)** | |
| **COST FORECAST DATA** | | | **PROJECTED COST** | - Exports the âEstimated Cost at Completion' and âForecast to Complete' values from a Procore budget to CMiC. |
| **COMMITMENTS** | | | **SUBCONTRACTS** | |
| **COMMITMENT CHANGE ORDERS** | | | **SUBCONTRACT CHANGE ORDERS** | |
| **SUBCONTRACTOR INVOICES** | | | **REQUEST FOR PAYMENT** | |
| **SUBCONTRACT INVOICE PAYMENTS** | | | **PAYMENTS** | - Export of payment records from Procore to CMiC is only supported for customers in the United States who have licensed Procore Pay. |
| **PRIME CONTRACT** | | | **PRIME CONTRACT** | |
| **PRIME CONTRACT CHANGE ORDERS** | | | **POTENTIAL CHANGE ITEM (PCI)** OR **OWNER CHANGE ORDER (OCO)** | - PCCO with multiple linked PCOs can be exported as individual PCIs to CMiC. See [Export a PCCO with Multiple PCOs as Individual PCIs to CMiC](/product-manuals/cmic/tutorials/export-a-pcco-with-multiple-pcos-as-individual-pcis-to-cmic). - PCCOs can be exported as OCOs to CMiC. See [Export a PCCO as an OCO to CMiC](/product-manuals/cmic/tutorials/export-a-pcco-as-an-oco-to-cmic). |
| **JOB-TO-DATE COSTS** | | | **JOB COSTS** | |
| **DIRECT COSTS** | | | **JOB COSTS TRANSACTION DETAILS** | - Import direct costs, including their image URLs, from CMiC to Procore. |

### Projects/Jobs

Exporting a Procore project to CMiC creates a 'project' in CMiC, but not a 'job'. You must create a job manually in CMiC after exporting your Procore project through the integration.

| PROCORE | Exports data from Procore to CMiC | Imports data from CMiC to Procore | CMiC | Notes |
| --- | --- | --- | --- | --- |
| CMIC ID | | | Project Code | |
| Project Name | | | Project Name | |
| Address | | | Address 1 | |
| City | | | City | |
| State | | | State | |
| ZIP | | | Zip | |
| Cost Code Code/Description | | | Cost Code Code/Description | - Project level cost codes must be added to the project from the Company level ERP Standard Cost Code List. New cost codes must be created in your ERP system, and cannot be created in Procore. - Cost codes added to a job in CMiC after the job is synced with Procore can be added to the project in Procore by clicking 'Refresh Cost Codes' in the Project level Admin tool's Work Breakdown Structure (WBS) cost code section. If multicompany is enabled, a specific company ID will be assigned to multicompany projects during the import and export of jobs in Procore. - Cost codes and cost types are synced with Procore projects when importing jobs to Procore, exporting jobs from Procore, resending projects to CMiC, and exporting budgets to Procore. |
| Cost Type Code/Description | | | Category Code/Description | - Cost codes and cost types are synced with Procore projects when importing jobs to Procore, exporting jobs from Procore, resending projects to CMiC, and exporting budgets to Procore. |
| Start Date | | | Begin Date | |
| Completion Date | | | End Date | |
| Company ID | | | Company ID | - If multicompany is enabled, a specific company ID will be assigned to multicompany projects during the import and export of jobs in Procore. - Once a project is synced as a multicompany project, all downstream transactions, such as contracts, invoices, and more, will automatically sync with the specific company. |

### Sub Jobs

| PROCORE | Exports data from Procore to CMiC | Imports data from CMiC to Procore | CMiC |
| --- | --- | --- | --- |
| Sub Job Code | | | Project Code |
| Sub Job Name | | | Project Name |
| Cost Code | | | Cost Code |
| Cost Type | | | Category |

### Vendors

When Companies in Procore are exported to CMiC, they will create a Business Partner and Vendor record. Additionally, when companies identified as a Customer in CMiC are imported to Procore, the integration will create a Company record in the Company Directory. Below is a table that displays the field mapping between these records.

| PROCORE | Exports data from Procore to CMiC | Imports data from CMiC to Procore | CMiC | Notes |
| --- | --- | --- | --- | --- |
| ERP Vendor ID | | | Vendor Code/Business Partner Code | - Export note: The ERP Vendor ID is entered manually by an accounting approver when a company is exported from Procore to CMiC. This is stored as the ERP Vendor ID (you can view it in the company-level ERP Integrations tool under Vendors or in the company-level Directory tool) and is then used on other vendor-related exports (Commitments, CCOs). |
| Name | | | Vendor Name/Business Partner Code | - If a Vendor has a masked Vendor Class or masked JcdtSrcCode in Boomi, it will not appear in the Ready to Import filter list. |
| Address | | | Street/Address | |
| City | | | City | |
| State | | | State/Province | |
| ZIP | | | Zip/Post Code | |
| Business Phone | | | Phone | |
| Business Fax | | | Fax | |
| Email Address | | | E-mail | |
| Website | | | Web Site | |
| EIN | | | Registration Code | - Include the Employer Identification Number (EIN) of a vendor when importing their record to the Procore directory. Procore currently supports CMiC Registration Codes in US EIN format only. |
| **Customers** | | | **Customers** | |
| ERP Vendor ID | | | Customer Code/Business Partner Code | - Import note: This is stored as the ERP Vendor ID (you can view it in the company-level ERP Integrations tool under Vendors or in the company-level Directory tool). - Export note: When Companies in Procore are exported to CMiC they will create a Business Partner and Vendor record. Business partner records must be manually assigned as a Customer in CMiC. |
| Name | | | Vendor Name/Business Partner Code | |
| Address | | | Street/Address | |
| City | | | City | |
| State | | | State/Province | |
| Zip | | | Zip/Post Code | |
| Business Phone | | | Phone | |
| Business Fax | | | Fax | |
| Email Address | | | E-mail | |
| Website | | | Web Site | |

### Budgets

Original Budget Amounts/Pending Original Budget edits are exported to CMiC as a PCI Type. The PCI will export over with an "Approved" status and will need to be posted in CMiC.

| PROCORE | Exports data from Procore to CMiC | Imports data from CMiC to Procore | CMiC |
| --- | --- | --- | --- |
| Original Budget | | | Original Estimate |
| Cost Code 1 | | | Cost Code |
| Cost Type 1 | | | Categories |

1*To sync previously unused project level cost codes to CMiC, you must add a cost budget line item to the Budget in Procore using that code. Syncing is automatic following the addition of cost budget line items.*

### Budget Modifications (Legacy)

##### Â Phased Release: Budget Changes

Some ERP integrated clients may have already transitioned from Budget Modifications (Legacy) to the new Budget Changes experience. The legacy experience will continue to be available until November 2024. To learn more about the timeline for migration, see [Common Questions](/process-guides/about-budget-changes/common-questions).

**Choosing to use the new Budget Changes experience will not impact the function of your ERP integration.** You should still thoroughly review the available documentation before migrating to the new experience. We recommend you also discuss any concerns or questions about migrating your Budget Modifications to Budget Changes with your Procore point of contact .

To learn more about the new Budget Changes experience, see [About Budget Changes](/process-guides/about-budget-changes/).

| PROCORE | Exports data from Procore to CMiC | Imports data from CMiC to Procore | CMiC |
| --- | --- | --- | --- |
| Project | | | Job |
| Project Name | | | Job Name |
| From/To | | | Cost Code ID |
| From/To | | | Cost Code Name |
| From/To | | | Cost Type ID |
| From/To | | | Cost Type Name |
| Amount | | | Transfer Amount |

### Budget Changes (New)

| PROCORE | Exports data from Procore to CMiC | Imports data from CMiC to Procore | CMiC |
| --- | --- | --- | --- |
| Project | | | Job |
| Budget Change Number | | | PCI No. |
| Status | | | Approved |
| System Date of Export | | | Date |
| Name | | | Description |
| Description | | | Scope |
| From/To | | | Cost Code ID |
| From/To | | | Cost Code Name |
| From/To | | | Cost Type ID |
| From/To | | | Cost Type Name |
| Amount 1 | | | Transfer Amount |

1*Amount populates the 'Budgeted Amount' by default, but can be set up to update ''Billing Amounts' as well. This requires assistance from ERP IIS. Contact support if interested in getting this to also populate the 'Billing Amounts' on a Budget Change export to CMiC.*

### Forecasting/Projections

Estimated Cost at Completion exports to CMiC as a PCI Type.

| PROCORE | Exports data from Procore to CMiC | Imports data from CMiC to Procore | CMiC |
| --- | --- | --- | --- |
| Cost Code | | | Phase |
| Cost Type | | | Cost Type |
| Estimated Cost at Completion Total 1 | | | Total Budgeted Amount |
| Type | | | PCI Type |
| Date of Export | | | Date |
| [month of export] Procore Forecast Amounts | | | Description |

1 *To export Estimated Cost at Completion Total values you must first enable the feature. See* [How do I export cost forecast data from a Procore budget to ERP?](/faq-how-do-i-export-cost-forecast-data-from-a-procore-budget-to-erp)

### Commitments

| PROCORE | Exports data from Procore to CMiC | Imports data from CMiC to Procore | CMiC |
| --- | --- | --- | --- |
| **Commitment Header** | | | **Commitment Header** |
| Contract # | | | Contract Number |
| Commitment Type 1 | | | Contract Type |
| Contract Company 2 | | | Vendor |
| Date Created | | | Date |
| Start Date | | | Start Date |
| Issued Date | | | Issued Date |
| Estimated Completion Date | | | End Date |
| Signed Contract Received Date | | | Executed Date |
| Title | | | Description |
| Default Retainage | | | Default Retainage Percentage |
| Description | | | Scope of Work |
| **Commitment Item (Purchase Orders)** | | | **Commitment Item** |
| Qty | | | Quantity |
| UOM | | | WM |
| Unit Cost | | | Rate |
| Contract Amount or Subtotal | | | Amount |
| **Commitment Item (Subcontracts)** | | | **Commitment Item** |
| Job ID | | | Job ID |
| Line Item Description | | | Task Description |
| Cost Code | | | Cost Code |
| Type | | | Category |
| UOM 3 | | | WM |
| Unit Cost 3 | | | Rate |
| Contract Amount or Subtotal | | | Amount |

1 *When a commitment is created in Procore, you must select a type: Purchase Order or Subcontract. This is used as the commitment type for* *CMiC**.*

2 *The ERP Vendor ID associated with the Contract Company is used on the import file for* *CMiC**. You cannot export a commitment for a Contract Company that does not have an ERP Vendor ID.*

3 *Subcontracts that are using the Accounting Method of "Unit/Quantity Based" will have these on the Schedule Of Values.*

### Commitment Change Orders

To sync a CCO, the Commitment has to be synced to CMiC first. The CCO will export to the Subcontract/PO and will need to be posted once it successfully exports to CMiC. When entering the SOV for a Commitment Change Order in Procore, you have the option of selecting an existing line item or entering a new line item.

| PROCORE | Exports data from Procore to CMiC | Imports data from CMiC to Procore | CMiC |
| --- | --- | --- | --- |
| **Commitment Change Order Header** | | | **Commitment Change Order Header** |
| Title | | | Description |
| System Date at Time of Export | | | Invoice Date in CMiC |
| Change Order Number | | | Contract No |
| Status | | | Pending |
| Description | | | Scope of Work |
| **Commitment Change Order Item (Purchase Order or Unit/Quantity Based Subcontract)** | | | **Commitment Change Order Item** |
| Item ID 1 | | | |
| Qty | | | Unit |
| Contract Amount or Subtotal | | | Extended Price |
| **Commitment Change Order Item (When New Line Item is Selected Entering the SOV on the CCO)** | | | **Commitment Change Order Item** |
| CMiC ID | | | Item ID |
| Qty 2 | | | Unit |
| Unit Cost 2 | | | Rate |
| UOM 2 | | | WM |
| Contract Amount or Subtotal 3 | | | Extended Price |

1 *This field is pulled from the Cost Type.*

2 *Typically, Quantity, Units, and Unit Cost are only used on Purchase Orders.*

3 *The field is titled Contract Amount when working in a Subcontract, and it is titled Subtotal when working in a Purchase Order.*

### Subcontractor Invoices

| **PROCORE** | Exports data from Procore to CMiC | Imports data from CMiC to Procore | CMiC |
| --- | --- | --- | --- |
| **Subcontractor Invoice** | | | **Invoice Header** |
| Contract Company | | | Vendor Name |
| ERP ID | | | Invoice Code |
| Description 1 | | | Description |
| Total Completed and Stored to Date | | | Original Invoice Amount |
| Total Retainage | | | Retainage Amt |
| Billing Date | | | Invoice Date |
| Billing Date + 30 Days | | | Due Date |
| Accounting Date 2 | | | Posting Date |
| | | | **Distributions** |
| Commitment # | | | Contract |
| Project # | | | Job/EQP/WO |
| Sub Job # | | | Job/EQP/WO |
| Cost Code | | | Phase/Component/WI |
| Category | | | Cat/Component/WI |
| Description of Work | | | Description |
| Work Completed this Period | | | Amount |
| Work Retainage | | | Retainage |
| **AP Invoice Payments** **3** | | | |
| **Payment Issued** | | | **Payment** |
| Payment Status | | | Payment Status |
| Amount | | | Check Amount / Payment Amount |
| Payment Funding Date | | | Check Post Date / Check Date |
| Check Number | | | Check Number |
| Check Description | | | Check Description |

1*The description for an invoice that will be created in* *CMiC* *can be entered into the Description field by an accounting approver on the Ready to Export screen in the ERP Integrations tool under Subcontractor Invoices. If no description is entered at the time of export, the Description field will be blank on the invoice created in* *CMiC**.*

2*This is filled automatically based on the Billing Date of the Invoice in Procore, but can be overridden at the time of export on the Ready to Export screen in the ERP Integrations tool under Subcontractor Invoices.*

3*The* *subcontractor invoice must exist in Procore to sync payments.*

### Prime Contracts

| PROCORE | Exports data from Procore to CMiC | Imports data from CMiC to Procore | CMiC |
| --- | --- | --- | --- |
| **Prime Contract** | | | **Job/Contract/Budget** |
| Title | | | Job Code + Prime Contract |
| # | | | Job # |
| Status | | | Approved |
| Description | | | Job Code + Message |
| Original Contract Amount | | | Total Budgeted Revenue Amount |
| **Prime Contract Schedule of Values** | | | **Contract/Enter Budget** |
| Budget Code (Cost Code) | | | Cost Code |
| Budget Code (Cost Type) | | | Category |
| Description | | | Cost Code Description |
| Amount | | | Budgeted Revenue Amount |
| **Prime Contract** **1** | | | **Job/Contract/Budget** |
| Title | | | Job Contract Code + Prime Contract |
| # | | | Parent Job Code | Job Contract Code |
| Status | | | Approved |
| Description | | | Job Contract Code + Prime Contract |
| Currency ISO Code | | | JbcCurrCode |
| **Prime Contract Schedule of Values** **1** | | | **Contract/Enter Budget** |
| Job Number/Sub Job Number | | | Job Code (Bill Code) |
| Budget Code (Cost Code) | | | Cost CodeÂ  (Bill Code) |
| Budget Code (Cost Type) | | | Category (Bill Code) |
| Description | | | Contract Description - BillÂ  Code Description |
| Amount | | | Budgeted Revenue Amount |

1 *Prime Contracts from multiple jobs in CMiC can be imported as separate prime contracts to a Procore project. 
Note:* *Existing CMiC users can reach out to their Procore point of contact to enable the âMultiple Prime Contracts Syncâ feature. If you enable this feature, you will not be able to revert to the Single Prime Contract Sync functionality.Â*

### Prime Contract Change Orders

| PROCORE | Exports data from Procore to CMiC | Imports data from CMiC to Procore | CMiC |
| --- | --- | --- | --- |
| **PCCO** | | | **PCI** |
| Project Number | | | Job Code |
| Title | | | Name |
| Transaction Date | | | Reference Date |
| PCCO Number | | | PCI Code |
| Description | | | Scope Description |
| Amount | | | Bill Amount |
| Cost Code | | | Code |
| Unit of Measurement | | | Budget WM Code |
| Line Item Type | | | Category Code |
| Ext Amount | | | Budget Amount |
| **PCCO** **1** | | | **PCI** |
| Potential Change Order | | | Subcontract Code Vendor Code Subcontract Change Order Number |
| PC Number-PCCO Number-PCO Number | | | **PCI Name** Change Event Line Item Description |
| **PCCO** **2** | | | **OCO** |
| Potential Change Order | | | **PCI** Subcontract Code Vendor Code Subcontract Change Order Number |
| PCCO Number | | | Owner Change Code |
| PC Number-PCCO Number-PCO Number | | | **PCI Name** Change Event Line Item Description |
| Schedule Impact 3 | | | Days Impact |

1 *PCCO with multiple linked PCOs is exported as separate PCIs to CMiC when the âCreate Multiple PCIsâ setting is enabled in Procore. See* [Export a PCCO with Multiple PCOs as Individual PCIs to CMiC](/product-manuals/cmic/tutorials/export-a-pcco-with-multiple-pcos-as-individual-pcis-to-cmic)*.*

2 *PCCOs are exported as OCOs to CMiC when the âCreate Owner Change Ordersâ setting is enabled in Procore. See* [Export a PCCO as an OCO to CMiC](/product-manuals/cmic/tutorials/export-a-pcco-as-an-oco-to-cmic)*.*

3*The 'Date of Substantial Completion as of This Change Order thereforeâ field in CMiC is calculated based on the 'Project End Date' and the 'Days Impact' fields.*

### Job Costs

**Import from** **CMiC** **only.** Cost information is retrieved from CMiC for each Cost Code/Type on Synced projects for use in 2 locations in Procore, the Budget and the Job Costs report. Job Cost information can be synced in either the ERP Integrations tool under the Job Costs sub-tab or within the Project Admin tool under Work Breakdown Structure, within Cost Codes there is a "Refresh Cost Codes" button.

| PROCORE | Exports data from Procore to CMiC | Imports data from CMiC to Procore | CMiC |
| --- | --- | --- | --- |
| **Budget** | | | |
| JTD Cost | | | JTD Cost |
| Direct Costs | | | JTD Cost - Commitment Invoiced 1 |
| **Job Costs Report** | | | |
| Cost Code | | | Cost Code |
| Cat. | | | Cost Type |
| Original Budget | | | Original Budget |
| Commitment Invoiced | | | Commitment Invoiced |
| Job-to-Date Cost | | | JTD Cost |

1 *This is a calculated column that displays the difference between the two database fields in* *CMiC**.*

### Job Cost Transaction Details

**Import from CMiC only.** If the feature is enabled, all posted âActualâ cost transaction details from the Job Costing Transaction Record in CMiC are imported into the Direct Cost tool for each project. This provides transaction detail for the costs displayed in Procore, and if the budget view is configured properly, the values of those transactions can be viewed in the Direct Costs or JTD Cost columns for a budget line item.

| PROCORE | Exports data from Procore to CMiC | Imports data from CMiC to Procore | CMiC | Notes |
| --- | --- | --- | --- | --- |
| **Direct Cost Type** | | | **Cost Type** | |
| Invoice | | | Journal Code Mapping | - Cross reference table created to map Journal Codes from the Transaction Record to the proper Procore Transaction Type. Requires work with ERP IIS to help set up, please reach out to support if interested in getting this set up. |
| Expense | | | Journal Code Mapping | - Cross reference table created to map Journal Codes from the Transaction Record to the proper Procore Transaction Type. Requires work with ERP IIS to help set up, please reach out to support if interested in getting this set up. |
| Subcontractor Invoice | | | Journal Code Mapping | - Cross reference table created to map Journal Codes from the Transaction Record to the proper Procore Transaction Type. Requires work with ERP IIS to help set up, please reach out to support if interested in getting this set up. |
| Payroll | | | Journal Code Mapping | - Cross reference table created to map Journal Codes from the Transaction Record to the proper Procore Transaction Type. Requires work with ERP IIS to help set up, please reach out to support if interested in getting this set up. |
| **Direct Cost General Information** | | | | |
| Date | | | Reference Date or Post Date | - You can choose whether âReference Dateâ or âPost Dateâ will be pulled into Procore from CMiC for the âDateâ field in the Direct Cost Tool. |
| Vendor | | | Source Code | |
| Received Date | | | Post Date | - You can choose whether âPost Dateâ or âInvoice/Reference Dateâ will be pulled into Procore from CMiC for the âReceived Dateâ field in the Direct Cost Tool. |
| Invoice # | | | Invoice # | |
| Status | | | Approved | |
| Description | | | Source Description Reference Code URL(s) | - You can choose whether to include the âReference Codeâ when importing the âSource Descriptionâ into Procore for the âDescriptionâ field of line items in the Direct Costs tool. - Include image URLs of direct costs in CMiC as part of the âDescriptionâ field of direct cost transactions in the Direct Costs tool when importing direct costs into Procore. To enable this feature, reach out to your Procore point of contact. |
| Budget Code | | | Cost Code | |
| Cost Type | | | Category | |
| Qty | | | Quantity | |
| UOM | | | WM | |
| Unit Cost | | | Unit Cost | |
| Amount | | | Amount | |

### Procore Pay Payments

##### Â General Availability in Select Markets (United States)

[Procore Pay](https://www.procore.com/pay) is available in the United States. It is designed for General Contractors and Owner-Builders who act as their own General Contractors on a job. Procore Pay extends the [Invoice Management](https://www.procore.com/invoice-management) functionality in the Procore web application to handle the payment process between general and specialty contractors.

| PROCORE | Exports data from Procore to CMiC | Imports data from CMiC to Procore | CMiC |
| --- | --- | --- | --- |
| Check No. | | | Check Number |
| Check Description | | | Check Description |
| Date Payment Initiated | | | Check Date |
| Date Payment Initiated | | | Post Date |
| Amount | | | Check Amount |