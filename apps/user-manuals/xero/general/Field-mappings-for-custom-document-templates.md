# Field mappings for custom document templates

Source: https://central.xero.com/s/article/Field-mappings-for-custom-document-templates

---

## Overview

- See where the fields in Practice Manager can be used in custom templates.

## What you need to know

This article maps the fields found in Practice Manager against the custom document templates those fields can be used in.

The first column of each table shows the correct format to use for the merge field names in the templates. A tick **✔** indicates the type of template you can use each field on.

Tip

To learn more about how merge fields work in custom templates, [download a sample template](Set-up-custom-document-templates.md) we provide and open it in Microsoft Word.

Staff fields

This table maps the fields found under **Contact details** on the **Information** tab in the [staff details screen](/s/article/Add-staff?userregion=true) against the templates that they can be used in. When you use one of these fields in a template, Practice Manager populates the document with the details of the user who’s creating the document.

| **Merge field name** | **Quote** | **Job Brief** | **Statement** | **Invoice** |
| --- | --- | --- | --- | --- |
| Name | **✔** | **✔** | **✔** | **✔** |
| Email | **✔** | **✔** | **✔** | **✔** |
| Phone | **✔** | **✔** | **✔** | **✔** |
| Mobile | **✔** | **✔** | **✔** | **✔** |

Settings fields

This table maps the fields found in the [practice settings screen](Set-up-your-practice-settings.md) against the documents that they can be used in.

| **Merge field name** | **Quote** | **Job Brief** | **Statement** | **Invoice** |
| --- | --- | --- | --- | --- |
| TITLE | **✔** | **✔** | **✔** | **✔** |
| Today | **✔** | **✔** | **✔** | **✔** |
| PreferenceInformation | **✔** | **✔** | **✔** | **✔** |
| PreferenceTaskHeading | **✔** | **✔** | **✔** | **✔** |
| PreferenceCostHeading | **✔** | **✔** | **✔** | **✔** |
| PreferenceOptionHeading | **✔** | **✔** | **✔** | **✔** |
| PreferenceTaxName | **✔** | **✔** | **✔** | **✔** |
| PreferenceTerms | **✔** | **✔** | **✔** | **✔** |
| PaymentAdviceHeading | **✔** | **✔** | **✔** | **✔** |
| PaymentAdviceText | **✔** | **✔** | **✔** | **✔** |

Client fields

This table maps the fields found in the [client details screen](Create-a-client-in-Practice-Manager.md) against the documents that they can be used in.

| **Merge field name** | **Quote** | **Job Brief** | **Statement** | **Invoice** |
| --- | --- | --- | --- | --- |
| Name | **✔** | **✔** | **✔** | **✔** |
| Email | **✔** | **✔** | **✔** | **✔** |
| Phone | **✔** | **✔** | **✔** | **✔** |
| ClientCity | **✔** | **✔** | **✔** | **✔** |
| ClientRegion | **✔** | **✔** | **✔** | **✔** |
| ClientPostCode | **✔** | **✔** | **✔** | **✔** |
| ClientCountry | **✔** | **✔** | **✔** | **✔** |
| ClientAddressText | **✔** | **✔** | **✔** | **✔** |
| ClientPostalAddress | **✔** | **✔** | **✔** | **✔** |
| ClientPostalCity | **✔** | **✔** | **✔** | **✔** |
| ClientPostalRegion | **✔** | **✔** | **✔** | **✔** |
| ClientPostalPostCode | **✔** | **✔** | **✔** | **✔** |
| ClientPostalCountry | **✔** | **✔** | **✔** | **✔** |
| ClientPostalAddressText | **✔** | **✔** | **✔** | **✔** |
| ClientBillingAddress | **✔** | **✔** | **✔** | **✔** |
| ClientAccountManagerName | **✔** | **✔** | **✔** | **✔** |
| ClientAccountManagerEmail | **✔** | **✔** | **✔** | **✔** |
| ClientAccountManagerPhone | **✔** | **✔** | **✔** | **✔** |
| ClientAccountManagerMobile | **✔** | **✔** | **✔** | **✔** |

Contact fields

This table maps the fields found in the [contact details screen](Create-a-client-in-Practice-Manager.md) against the documents that they can be used in.

| **Merge field name** | **Quote** | **Job Brief** | **Invoice** |
| --- | --- | --- | --- |
| ContactName | **✔** | **✔** | **✔** |
| ContactPhone | **✔** | **✔** | **✔** |
| ContactMobile | **✔** | **✔** | **✔** |
| ContactPosition | **✔** | **✔** | **✔** |
| ContactEmail | **✔** | **✔** | **✔** |
| ContactSalutation | **✔** | **✔** | **✔** |
| ContactAddressee | **✔** | **✔** | **✔** |
| ContactSalutationOrName | **✔** | **✔** | **✔** |
| ContactAddresseeOrName | **✔** | **✔** | **✔** |

Quote fields

This table maps the fields found in the [quote details screen](Create-a-quote-in-Practice-Manager.md) for a specific quote or estimate against the documents that they can be used in.

| **Merge field name** | **Quote** | **Job Brief** |
| --- | --- | --- |
| QuoteType | **✔** | **–** |
| QuoteDate | **✔** | **–** |
| QuoteValidDate | **✔** | **–** |
| QuoteNumber | **✔** | **✔** |
| QuoteJobNumber | **✔** | **–** |
| QuoteName | **✔** | **–** |
| QuoteDescription | **✔** | **–** |
| QuoteOptionExplanation | **✔** | **–** |
| QuoteTaxRate | **✔** | **–** |
| QuoteSubTotal | **✔** | **–** |
| QuoteTaxTotal | **✔** | **–** |
| QuoteTax1Total (US only) | **✔** | **–** |
| QuoteTax2Total (US only) | **✔** | **–** |
| QuoteTaskSubTotal | **✔** | **–** |
| QuoteTaskSubTotalIncludingTax | **✔** | **–** |

Task Table fields

This table maps the fields found in the [task details screen](Job-tasks.md) for a specific against the documents that they can be used in.

| **Merge field name** | **Quote** | **Job Brief** | **Invoice** |
| --- | --- | --- | --- |
| Description | **✔** | **✔** | **✔** |
| Name | **✔** | **✔** | **✔** |
| Label | **✔** | **✔** | **✔** |
| Note | **✔** | **✔** | **✔** |
| Time | **✔** | **–** | **✔** |
| TimeHourMinute | **✔** | **–** | **✔** |
| TimeDecimal | **✔** | **–** | **✔** |
| Rate | **✔** | **–** | **✔** |
| Amount | **✔** | **–** | **✔** |
| AmountTax | **✔** | **–** | **✔** |
| AmountTotal | **✔** | **–** | **✔** |
| Days | **✔** | **✔** | **✔** |
| DailyRate | **✔** | **–** | **✔** |
| TaxRate1 | **–** | **–** | **✔** |
| TaxRate2 | **–** | **–** | **✔** |
| EstimatedTime | **–** | **✔** | **–** |
| ActualTime | **–** | **✔** | **–** |
| RemainingTime | **–** | **✔** | **–** |
| StartDate | **–** | **✔** | **–** |
| DueDate | **–** | **✔** | **–** |
| Staff | **–** | **✔** | **–** |
| Completed | **–** | **✔** | **–** |
| DateComplete | **–** | **✔** | **–** |
| CompletedBy | **–** | **✔** | **–** |

Cost Table fields

This table maps the fields found in the [cost details screen](Enter-costs-and-expenses-on-a-job.md) for a specific job against the documents that they can be used in.

| **Merge field name** | **Quote** | **Job Brief** | **Invoice** |
| --- | --- | --- | --- |
| Description | **✔** | **✔** | **✔** |
| Code | **✔** | **✔** | **✔** |
| Note | **✔** | **✔** | **✔** |
| Quantity | **✔** | **✔** | **✔** |
| Rate | **✔** | **–** | **✔** |
| Amount | **✔** | **✔** | **✔** |
| AmountTax | **✔** | **–** | **✔** |
| AmountTotal | **✔** | **–** | **✔** |
| TaxRate1 | **–** | **–** | **✔** |
| TaxRate2 | **–** | **–** | **✔** |
| Date | **–** | **✔** | **–** |
| Folder | **–** | **✔** | **–** |
| UnitCost | **–** | **✔** | **–** |
| UnitPrice | **–** | **✔** | **–** |
| Cost | **–** | **✔** | **–** |

Option Table fields

This table maps the fields found in the [quote options screen](Create-a-quote-in-Practice-Manager.md) for a specific quote or estimate against the documents that they can be used in.

| **Merge field name** | **Quote** |
| --- | --- |
| Description | **✔** |
| Code | **✔** |
| Note | **✔** |
| Quantity | **✔** |
| Rate | **✔** |
| Amount | **✔** |
| AmountTax | **✔** |
| AmountTotal | **✔** |

Job fields

This table maps the fields found in the [job details screen](Create-or-edit-a-job.md) for a specific job against the documents that they can be used in.

| **Merge field name** | **Job Brief** |
| --- | --- |
| JobNumber | **✔** |
| JobName | **✔** |
| JobDate | **✔** |
| JobFolder | **✔** |
| JobDescription | **✔** |
| JobClientOrderNumber | **✔** |
| JobPriority | **✔** |
| JobStaff | **✔** |
| JobManager | **✔** |
| JobStartDate | **✔** |
| JobDueDate | **✔** |
| JobBudget | **✔** |
| JobState | **✔** |
| JobCategory | **✔** |
| Manager | **–** |

Invoice fields

This table maps the fields found in the [invoice details screen](Create-an-invoice.md) for a specific invoice against the documents that they can be used in.

| **Merge field name** | **Invoice** |
| --- | --- |
| DueDate | **✔** |
| Number | **✔** |
| Description | **✔** |
| Type | **✔** |
| TaxRate | **✔** |
| SubTotal | **✔** |
| TaxTotal | **✔** |
| Tax1Total | **✔** |
| Tax2Total | **✔** |
| Total | **✔** |
| AmountPaid | **✔** |
| AmountDue | **✔** |
| CostSubTotal | **✔** |
| TaskSubTotal | **✔** |
| TaskTotalTime | **✔** |
| TaskTotalTimeHourMinute | **✔** |
| TaskTotalTimeDecimal | **✔** |
| OrderNumber | **✔** |
| JobNumber | **✔** |
| JobName | **✔** |
| Manager | **✔** |

Job Table (Invoice only) fields

This table maps the fields found in the [job details screen](Create-or-edit-a-job.md) for a specific invoice against the documents that they can be used in.

| **Merge field name** | **Invoice** |
| --- | --- |
| Name | **✔** |
| Description | **✔** |
| Number | **✔** |
| ClientOrderNumber | **✔** |
| SubTotal | **✔** |
| TaskSubTotal | **✔** |
| TaskTotalTime | **✔** |
| TaskTotalTimeHourMinutes | **✔** |
| TaskTotalTimeDecimal | **✔** |
| CostSubTotal | **✔** |
| QuoteNumber | **✔** |
| Manager | **✔** |

Time Table (Invoice only) fields

This table shows the fields found on the **Time Sheets** tab for a specific invoice that you can use if you select any option other than **None** when you upload a custom invoice template.

| **Merge field name** | **Invoice** |
| --- | --- |
| Date | **✔** |
| Staff | **✔** |
| Description | **✔** |
| Name | **✔** |
| Label | **✔** |
| Note | **✔** |
| Time | **✔** |
| TimeHourMinute | **✔** |
| TimeDecimal | **✔** |
| Rate | **✔** |
| Amount | **✔** |

Milestone Table fields

This table maps the fields found under **Milestones** in the [job details screen](Add-milestones-to-a-job.md) for a specific job against the documents that they can be used in.

| **Merge field name** | **Job Brief** |
| --- | --- |
| Date | **✔** |
| Name | **✔** |
| Folder | **✔** |
| Completed | **✔** |
| DateCompleted | **✔** |
| CompletedBy | **✔** |

Note Table fields

This table maps the fields found on the **Notes** tab in the [job details screen](Create-or-edit-a-job.md) for a specific job against the documents that they can be used in.

| **Merge field name** | **Job Brief** |
| --- | --- |
| Date | **✔** |
| Time | **✔** |
| Folder | **✔** |
| CreatedBy | **✔** |

Task To-do Table fields

This table maps the fields found in the [to-do list](To-do-list.md) for a specific job against the documents that they can be used in.

| **Merge field name** | **Job Brief** |
| --- | --- |
| Name | **✔** |
| Completed | **✔** |
| DateCompleted | **✔** |
| CompletedBy | **✔** |

Statement fields

This table maps the fields found on [account statements](Send-a-statement.md) against the documents that they can be used in.

| **Merge field name** | **Statement** |
| --- | --- |
| StatementSubTotal | **✔** |
| StatementTaxTotal | **✔** |
| StatementTotal | **✔** |
| StatementStatementAmountPaid | **✔** |
| StatementAmountDue | **✔** |
| StatementDate | **✔** |

Invoice Table (Statements only) fields

This table maps the fields found on [account statements](Send-a-statement.md) against the documents that they can be used in.

| **Merge field name** | **Statement** |
| --- | --- |
| Name | **✔** |
| Date | **✔** |
| Number | **✔** |
| Description | **✔** |
| SubTotal | **✔** |
| TaxTotal | **✔** |
| Total | **✔** |
| AmountPaid | **✔** |
| AmountDue | **✔** |
| JobName | **✔** |
| JobSummary | **✔** |
| DueDate | **✔** |

Tax Table (tax letters and tax return cover pages only) fields

This table shows the fields that can be used on [tax payment](About-tax-payments.md) templates.

| **Merge field name** | **Tax Return Cover Page** | **Provisional Tax Letter** | **Terminal Tax Letter** |
| --- | --- | --- | --- |
| AgentName | **✔** | **✔** | **✔** |
| AgentAddress | **✔** | **✔** | **✔** |
| AgentPhone | **✔** | **✔** | **✔** |
| AgentFax | **✔** | **✔** | **✔** |
| ReturnPeriodFrom | **✔** | **–** | **–** |
| ReturnPeriodTo | **✔** | **–** | **–** |
| ReturnTaxYear | **✔** | **–** | **–** |
| ReturnTaxType | **✔** | **–** | **–** |
| PaymentDateApproved | **–** | **✔** | **✔** |
| PaymentAddressee | **–** | **✔** | **✔** |
| PaymentSalutation | **–** | **✔** | **✔** |
| PaymentInstallment | **–** | **✔** | **✔** |
| PaymentTaxYear | **–** | **✔** | **✔** |
| PaymentDate | **–** | **✔** | **✔** |

Custom fields (supported on templates)

This table shows the templates that [custom fields in Practice Manager](Create-custom-fields.md) can be used on.

| **Custom field usage area** | **Quote** | **Job Brief** | **Statement** | **Invoice** | **Tax Letter** |
| --- | --- | --- | --- | --- | --- |
| Job | **–** | **✔** | **–** | **–** | **–** |
| Job Task | **–** | **✔** | **–** | **–** | **–** |
| Job Cost | **–** | **✔** | **–** | **–** | **–** |
| Client | **✔** | **✔** | **✔** | **✔** | **✔** |
| Contact | **✔** | **✔** | **–** | **✔** | **–** |

Use the merge field format [UsageArea Field Name] to insert a custom field into a template as follows, where 'XXX' is the name of the custom field:

| **Usage area** | **Field name format** |
| --- | --- |
| Job | JobCustom XXX |
| Job Task | JobTaskCustom XXX |
| Job Cost | JobCostCustom XXX |
| Client | ClientCustom XXX |
| Contact | ContactCustom XXX |

For example, a job custom field called "Product Type" would have a merge field of "JobCustom Product Type".

Warning

If you’re using Microsoft Word for Mac, you’ll need to manually add double quotation marks around the name of the custom field in the merge field. On a Windows computer, Word adds the quotation marks automatically.

## What's next?

Put this information to use by [creating and editing a custom template](Set-up-custom-document-templates.md).