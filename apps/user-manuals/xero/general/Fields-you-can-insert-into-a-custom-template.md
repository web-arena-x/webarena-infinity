# Fields you can insert into an advanced invoice template

Source: https://central.xero.com/s/article/Fields-you-can-insert-into-a-custom-template

---

## Overview

- View the default fields included in advanced invoice templates when they're downloaded from Xero.
- Browse through other optional fields if you'd like to customise your template further.

Fields included in the default templates

| **Field** | **Default field in template** | **Description of field in Xero** |
| --- | --- | --- |
| **«Amount»** | Statements | Invoice total amount. |
| **«Balance»** | Statements | Running total of sales invoices. |
| **«ContactAccountNumber»** | Invoices Credit notes Statements Purchase orders Quotes | Contact's account number. |
| **«ContactName»** | Invoices Credit notes Statements Purchase orders Quotes | Contact's name. |
| **«ContactPostalAddress»** | Invoices Credit notes Statements Purchase orders Quotes | Contact's postal address. Combination of all of the contact billing address fields. |
| **«ContactTaxDisplayName»** | Invoices Credit notes Statements Purchase orders Quotes | GST number – only shows when the contact has a tax number. |
| **«ContactTaxNumber»** | Invoices Credit notes Statements Purchase orders Quotes | Contact's GST number. |
| **«Currency»** | Statements | [The ISO 4217 currency code](http://www.iso.org/iso/currency_codes) (ISO website) of the sales invoice. |
| **«CurrencyConversionMessage»** | Invoices Credit notes Purchase orders Quotes | A summary field that displays "Conversion Rate: 1 {{InvoiceCurrency}} = {{CurrencyRate}} {{DefaultCurrency}}". |
| **«CurrencyName»** | Statements | The full name of the currency. |
| **«CurrentDueAmount»** | Statements | Combined value of statement. |
| **«DefaultCurrencyTaxMessage»** | Invoices Credit notes Purchase orders Quotes | Organisation's default currency tax message. |
| **«DeliveryAddress»** | Purchase orders | Delivery address details. |
| **«DeliveryContact»** | Purchase orders | Contact person for delivery. |
| **«DeliveryDetail»** | Purchase orders | Delivery detail including the due date, address, phone number and instructions. |
| **«DeliveryInstructions»** | Purchase orders | Instructions for delivery. |
| **«DeliveryPhone»** | Purchase orders | Contact phone number for delivery. |
| **«Description»** | Invoices Credit notes Statements Purchase orders Quotes | Line description. For statements, a combination of '{{InvoiceTitle}} # {{InvoiceNumber}}'. |
| **«DueDate»** | Statements | Sales invoice due date. |
| **«ExpiryDate»** | Quotes | Quote expiry date. |
| **«InvoiceAmountDue»** | Invoices Credit notes Purchase orders Quotes | Total less any payments. |
| **«InvoiceCurrency»** | Invoices Credit notes Purchase orders Quotes | [The ISO 4217 currency code](http://www.iso.org/iso/currency_codes) (ISO website). |
| **«InvoiceDate»** | Invoices Credit notes Statements Purchase orders Quotes | Date. |
| **«InvoiceDueDate»** | Invoices Purchase orders | Due date. |
| **«InvoiceNumber»** | Invoices Credit notes Purchase orders Quotes | Number (for example, INV 002). |
| **«InvoiceSubTotal»** | Invoices Credit notes Purchase orders Quotes | Total (excluding tax). |
| **«InvoiceTitle»** | Invoices Credit notes Statements Purchase orders Quotes | Title of the document (for example, invoice, credit note or statement). |
| **«InvoiceTotal»** | Invoices Credit notes Purchase orders | Total (including tax). |
| **«InvoiceTotalNetPayments»** | Invoices | Net total of all payments and credits made to this sales invoice. Default $0.00. |
| **«ItemCode»** | Invoices Credit notes Purchase orders Quotes | Inventory item code. |
| **«LineAmount»** | Invoices Credit notes Quotes | Line amount. |
| **«OpeningBalance»** | Statements | Balance at start of statement, if activity statement. |
| **«OrganisationName»** | Invoices Credit notes Statements Purchase orders Quotes | Legal trading name of organisation. |
| **«OrganisationPostalAddress»** | Invoices Credit notes Statements Purchase orders Quotes | Organisation address. Combination of all of the organisation postal address fields. |
| **«OrganisationTaxDisplayName»** | Invoices Credit notes Statements Purchase orders Quotes | GST number. |
| **«OrganisationTaxDisplayNumber»** | Invoices Credit notes Statements Purchase orders Quotes | Organisation's GST number. |
| **«OverdueAmount»** | Statements | The amount of the statement that's overdue. |
| **«PaidAmount»** | Statements | Amount paid for each sales invoice. |
| **«PaymentImage»** | Invoices | Credit card logos for payment services. |
| **«PaymentMessageAndUrl»** | Invoices | Payment service URL or URL to online invoice. |
| **«Quantity»** | Invoices Credit notes Purchase orders Quotes | Line quantity. |
| **«QuoteTerms»** | Quotes | Terms and conditions of the quote. |
| **«QuoteTitle»** | Quotes | The title of your quote. |
| **«Reference»** | Invoices Credit notes Statements Purchase orders Quotes | Reference field (Shortened to 10 characters on statements. Replace statement template with field **LongReference** if you want the full reference to display). |
| **«RegisteredOffice»** | Invoices Credit notes Statements Purchase orders Quotes | Combination of your NZBN and Registered office address data. |
| **«StartDate»** | Statements | Date the statement period starts. |
| **«StatementDate»** | Statements | Date statement produced (for example, statement end date). |
| **«Summary»** | Quotes | Summary description of your quote. |
| **«TableEnd:Line»** | Statements | The end of the table of sales invoices included in the template. |
| **«TableEnd:LineItem»** | Invoices Credit notes Purchase orders Quotes | The end of the table of line items. |
| **«TableEnd:TaxSubTotal»** | Invoices Credit notes Purchase orders Quotes | The end of the table of tax amounts in the summary. |
| **«TableStart:Line»** | Statements | The start of the table of sales invoices included in the template. |
| **«TableStart:LineItem»** | Invoices Credit notes Purchase orders Quotes | The start of the table of line items. |
| **«TableStart:TaxSubTotal»** | Invoices Credit notes Purchase orders Quotes | The start of the table of tax amounts in the summary. |
| **«TaxCode»** | Invoices Credit notes Purchase orders Quotes | Tax component for this subtotal. |
| **«TaxPercentageOrName»** | Invoices Credit notes Purchase orders Quotes | Tax rate for this line item. |
| **«TaxTotal»** | Invoices Credit notes Purchase orders | Amount of this tax component that needs to be paid. |
| **«TotalDueAmount»** | Statements | Balance at end of statement. |
| **«UnitAmount»** | Invoices Credit notes Purchase orders Quotes | Price per unit. |

Invoice template fields

| **Fields you can insert in template** | **Description of field** |
| --- | --- |
| **ContactContactNumber** | Contact's phone number. |
| **ContactEmailAddress** | Contact's email address. |
| **ContactFirstName** | Contact's first name. |
| **ContactLastName** | Contact's last name. |
| **ContactPhysicalAddress** | Contact's street address, in the regional format of the organisation. Combination of all delivery address fields. |
| **ContactPhysicalAddressLines** | Contact's delivery (delivery/street) address (lines 1-4). |
| **ContactPhysicalAttentionTo** | Attention to field (delivery/street address). |
| **ContactPhysicalCity** | Contact's city (delivery/street address). |
| **ContactPhysicalCountry** | Contact's country (delivery/street address). |
| **ContactPhysicalPostCode** | Contact's postcode (delivery/street address). |
| **ContactPhysicalRegion** | Contact's region (delivery/street address). |
| **ContactPostalAddressLines** | Contact's billing (postal) address (lines 1-4). |
| **ContactPostalAttentionTo** | Attention to field (billing/postal address). |
| **ContactPostalCity** | Contact's city (billing/postal address). |
| **ContactPostalCountry** | Contact's country (billing/postal address). |
| **ContactPostalPostCode** | Contact's postal or zip code (billing/postal address). |
| **ContactPostalRegion** | Contact's region (billing/postal address). |
| **CurrencyRate** | Currency rate used on multicurrency. |
| **DefaultCurrency** | [The ISO 4217 currency code](http://www.iso.org/iso/currency_codes) (ISO website). |
| **DefaultCurrencyTaxAmount** | Amount of tax paid in default currency. |
| **DiscountAmount** | Amount of discount for given line. |
| **DiscountPercentage** | Discount percentage for given line. |
| **DiscountedUnitPrice** | Unit price less the discount. |
| **InvoiceTaxTotal** | Tax total. |
| **ItemName** | Inventory item name. |
| **MultiCurrencyDisplayMessage** | Combination of {{Default Currency Tax Message}} and {{CurrencyConversionMessage}}. Used in sample template. |
| **NetGoodsAmount** | Net amount converted into base currency. Insert into the currency conversion table. |
| **OrganisationPhysicalAddress** | Organisation's physical address, in the regional format of the organisation. Combination of all physical address fields. |
| **OrganisationPhysicalAddressLines** | Organisation's physical address (lines 1-4). |
| **OrganisationPhysicalAttentionTo** | Attention to field. |
| **OrganisationPhysicalCity** | Organisation's city (physical address). |
| **OrganisationPhysicalCountry** | Organisation's country (physical address). |
| **OrganisationPhysicalPostCode** | Organisation's postcode (physical address). |
| **OrganisationPhysicalRegion** | Organisation's region (physical address). |
| **OrganisationPostalAddressLines** | Organisation's postal address (lines 1-4). |
| **OrganisationPostalAttentionTo** | Attention to field. |
| **OrganisationPostalCity** | Organisation's city (postal address). |
| **OrganisationPostalCountry** | Organisation's country (postal address). |
| **OrganisationPostalPostCode** | Organisation's postal or zip code (postal address). |
| **OrganisationPostalRegion** | Organisation's region (postal address). |
| **OrganisationTaxNumber** | GST number. |
| **PayPalImage** | Paypal credit card logos. |
| **PayPalMessageAndUrl** | PayPal URL. |
| **RegistrationNumber** | NZBN. |
| **TaxInclusiveDiscountAmount** | Amount of discount for line, tax inclusive. |
| **TaxInclusiveDiscountUnitPrice** | Unit price less the discount, tax inclusive. |
| **TaxInclusiveLineAmount** | Tax inclusive line amount. Replace field **«LineAmount»** with this field. Also insert field **«TaxInclusiveUnitAmount»**. |
| **TaxInclusiveTotalDiscountAmount** | Total combined discount across all lines, tax inclusive. |
| **TaxInclusiveUnitAmount** | Tax inclusive unit amount. Replace field **«UnitAmount»** with this field. Also insert field **«TaxInclusiveLineAmount»**. |
| **TaxOnLineAmount** | Tax amount for individual line item. |
| **TaxRateName** | Tax rate name. |
| **TotalDiscountAmount** | Total combined discount across all lines. |
| **TaxPercentage** | Tax percentage. |
| **TaxPercentageOrName** | Displays tax rate as a percentage if greater than 0%, otherwise displays full tax rate name. |
| **TaxRateName** | Full tax rate name. |

There are a number of apps that connect to Xero that allow for even more fields in your invoice templates. You can explore these in the [Xero App Store](https://apps.xero.com/!h9k17/function/invoicing-jobs?utm_source=xc&utm_medium=internal-referral&utm_campaign=invoicing&utm_content=invoicing-jobs).

Quote template fields

| Fields you can insert in template | Description of field |
| --- | --- |
| **ContactContactNumber** | Contact's phone number. |
| **ContactEmailAddress** | Contact's email address. |
| **ContactFirstName** | Contact's first name. |
| **ContactLastName** | Contact's last name. |
| **ContactPhysicalAddress** | Contact's street address, in the regional format of the organisation. Combination of all delivery address fields. |
| **ContactPhysicalAddressLines** | Contact's delivery (street) address (lines 1-4). |
| **ContactPhysicalAttentionTo** | Attention to field (delivery/street address). |
| **ContactPhysicalCity** | Contact's city (delivery/street address). |
| **ContactPhysicalCountry** | Contact's country (delivery/street address). |
| **ContactPhysicalPostCode** | Contact's postcode (delivery/street address). |
| **ContactPhysicalRegion** | Contact's region (delivery/street address). |
| **ContactPostalAddressLines** | Contact's billing (postal) address (lines 1-4). |
| **ContactPostalAttentionTo** | Attention to field (billing/postal address). |
| **ContactPostalCity** | Contact's city (billing/postal address). |
| **ContactPostalCountry** | Contact's country (billing/postal address). |
| **ContactPostalPostCode** | Contact's postal or zip code (billing/postal address). |
| **ContactPostalRegion** | Contact's region (billing/postal address). |
| **CurrencyRate** | Currency rate used on multicurrency. |
| **DefaultCurrency** | [The ISO 4217 currency code](http://www.iso.org/iso/currency_codes) (ISO website). |
| **DefaultCurrencyTaxAmount** | Amount of tax paid in default currency. |
| **DiscountAmount** | Amount of discount for given line. |
| **DiscountPercentage** | Discount percentage for given line. |
| **DiscountedUnitPrice** | Unit price less the discount. |
| **InvoiceTaxTotal** | Tax total. |
| **ItemName** | Inventory item name. |
| **MultiCurrencyDisplayMessage** | Combination of {{Default Currency Tax Message}} and {{CurrencyConversionMessage}}. Used in sample template. |
| **OrganisationPhysicalAddress** | Organisation's physical address, in the regional format of the organisation. Combination of all physical address fields. |
| **OrganisationPhysicalAddressLines** | Organisation's physical address (lines 1-4). |
| **OrganisationPhysicalAttentionTo** | Attention to field. |
| **OrganisationPhysicalCity** | Organisation's city (physical address). |
| **OrganisationPhysicalCountry** | Organisation's country (physical address). |
| **OrganisationPhysicalPostCode** | Organisation's postcode (physical address). |
| **OrganisationPhysicalRegion** | Organisation's region (physical address). |
| **OrganisationPostalAddressLines** | Organisation's postal address (lines 1-4). |
| **OrganisationPostalAttentionTo** | Attention to field. |
| **OrganisationPostalCity** | Organisation's city (postal address). |
| **OrganisationPostalCountry** | Organisation's country (postal address). |
| **OrganisationPostalPostCode** | Organisation's postal or zip code (postal address). |
| **OrganisationPostalRegion** | Organisation's region (postal address). |
| **OrganisationTaxNumber** | GST number. |
| **QuantityTotal** | Sum of the quantity column. |
| **RegistrationNumber** | NZBN. |
| **TaxInclusiveDiscountAmount** | Amount of discount for line, tax inclusive. |
| **TaxInclusiveDiscountUnitPrice** | Unit price less the discount, tax inclusive. |
| **TaxInclusiveLineAmount** | Tax inclusive line amount. Replace field **«LineAmount»** with this field. Also insert field **«TaxInclusiveUnitAmount»**. |
| **TaxInclusiveTotalDiscountAmount** | Total combined discount across all lines, tax inclusive. |
| **TaxInclusiveUnitAmount** | Tax inclusive unit amount. Replace field **«UnitAmount»** with this field. Also insert field **«TaxInclusiveLineAmount»**. |
| **TaxOnLineAmount** | Tax amount for individual line item. |
| **TaxRateName** | Tax rate name. |
| **TotalDiscountAmount** | Total combined discount across all lines. |
| **TaxPercentage** | Tax percentage. |
| **TaxPercentageOrName** | Displays tax rate as a percentage if greater than 0%, otherwise displays full tax rate name. |
| **TaxRateName** | Full tax rate name. |

Statement template fields

| Fields you can insert in template | Description of field |
| --- | --- |
| **ContactContactNumber** | Contact's phone number. |
| **ContactEmailAddress** | Contact's email address. |
| **ContactFirstName** | Contact's first name. |
| **ContactLastName** | Contact's last name. |
| **ContactPhysicalAddress** | Contact's street address, in the regional format of the organisation. Combination of all delivery address fields. |
| **ContactPhysicalAddressLines** | Contact's delivery (street) address (lines 1-4). |
| **ContactPhysicalAttentionTo** | Attention to field (delivery/street address). |
| **ContactPhysicalCity** | Contact's city (delivery/street address). |
| **ContactPhysicalCountry** | Contact's country (delivery/street address). |
| **ContactPhysicalPostCode** | Contact's postcode (delivery/street address). |
| **ContactPhysicalRegion** | Contact's region (delivery/street address). |
| **ContactPostalAddressLines** | Contact's billing (postal) address (lines 1-4). |
| **ContactPostalAttentionTo** | Attention to field (billing/postal address). |
| **ContactPostalCity** | Contact's city (billing/postal address). |
| **ContactPostalCountry** | Contact's country (billing/postal address). |
| **ContactPostalPostCode** | Contact's postal or zip code (billing/postal address). |
| **ContactPostalRegion** | Contact's region (billing/postal address). |
| **LongReference** | Replace field **«Reference»** with this field to display full (not shortened) reference. |
| **OrganisationPhysicalAddress** | Organisation's physical address, in the regional format of the organisation. Combination of all physical address fields. |
| **OrganisationPhysicalAddressLines** | Organisation's physical address (lines 1-4). |
| **OrganisationPhysicalAttentionTo** | Attention to field. |
| **OrganisationPhysicalCity** | Organisation's city (physical address). |
| **OrganisationPhysicalCountry** | Organisation's country (physical address). |
| **OrganisationPhysicalPostCode** | Organisation's postcode (physical address). |
| **OrganisationPhysicalRegion** | Organisation's region (physical address). |
| **OrganisationPostalAddressLines** | Organisation's postal address (lines 1-4). |
| **OrganisationPostalAttentionTo** | Attention to field. |
| **OrganisationPostalCity** | Organisation's city (postal address). |
| **OrganisationPostalCountry** | Organisation's country (postal address). |
| **OrganisationPostalPostCode** | Organisation's postal or zip code (postal address). |
| **OrganisationPostalRegion** | Organisation's region (postal address). |
| **OrganisationTaxNumber** | GST number. |
| **RegistrationNumber** | NZBN. |

Credit note template fields

| Fields you can insert in template | Description of field |
| --- | --- |
| **ContactContactNumber** | Contact's phone number. |
| **ContactEmailAddress** | Contact's email address. |
| **ContactFirstName** | Contact's first name. |
| **ContactLastName** | Contact's last name. |
| **ContactPhysicalAddress** | Contact's street address, in the regional format of the organisation. Combination of all delivery address fields. |
| **ContactPhysicalAddressLines** | Contact's delivery (street) address (lines 1-4). |
| **ContactPhysicalAttentionTo** | Attention to field (delivery/street address). |
| **ContactPhysicalCity** | Contact's city (delivery/street address). |
| **ContactPhysicalCountry** | Contact's country (delivery/street address). |
| **ContactPhysicalPostCode** | Contact's postcode (delivery/street address). |
| **ContactPhysicalRegion** | Contact's region (delivery/street address). |
| **ContactPostalAddressLines** | Contact's billing (postal) address (lines 1-4). |
| **ContactPostalAttentionTo** | Attention to field (billing/postal address). |
| **ContactPostalCity** | Contact's city (billing/postal address). |
| **ContactPostalCountry** | Contact's country (billing/postal address). |
| **ContactPostalPostCode** | Contact's postal or zip code (billing/postal address). |
| **ContactPostalRegion** | Contact's region (billing/postal address). |
| **CurrencyRate** | Currency rate used on multicurrency. |
| **DefaultCurrency** | [The ISO 4217 currency code](http://www.iso.org/iso/currency_codes) (ISO website). |
| **DefaultCurrencyTaxAmount** | Amount of tax paid in default currency. |
| **InvoiceTaxTotal** | Tax total. |
| **InvoiceTotalNetPayments** | Net total of all payments and credits made to this sales invoice. Default $0.00. |
| **ItemName** | Inventory item name. |
| **MultiCurrencyDisplayMessage** | Combination of {{Default Currency Tax Message}} and {{CurrencyConversionMessage}}. Used in sample template. |
| **NetGoodsAmount** | Net amount converted into base currency. Insert into the currency conversion table. |
| **OrganisationPhysicalAddress** | Organisation's physical address, in the regional format of the organisation. Combination of all physical address fields. |
| **OrganisationPhysicalAddressLines** | Organisation's physical address (lines 1-4). |
| **OrganisationPhysicalAttentionTo** | Attention to field. |
| **OrganisationPhysicalCity** | Organisation's city (physical address). |
| **OrganisationPhysicalCountry** | Organisation's country (physical address). |
| **OrganisationPhysicalPostCode** | Organisation's postcode (physical address). |
| **OrganisationPhysicalRegion** | Organisation's region (physical address). |
| **OrganisationPostalAddressLines** | Organisation's postal address (lines 1-4). |
| **OrganisationPostalAttentionTo** | Attention to field. |
| **OrganisationPostalCity** | Organisation's city (postal address). |
| **OrganisationPostalCountry** | Organisation's country (postal address). |
| **OrganisationPostalPostCode** | Organisation's postal or zip code (postal address). |
| **OrganisationPostalRegion** | Organisation's region (postal address). |
| **OrganisationTaxNumber** | GST number. |
| **RegistrationNumber** | NZBN. |
| **TaxInclusiveLineAmount** | Tax inclusive line amount. Replace field **«LineAmount»** with this field. Also insert field **«TaxInclusiveUnitAmount»**. |
| **TaxInclusiveUnitAmount** | Tax inclusive unit amount. Replace field **«UnitAmount»** with this field. Also insert field **«TaxInclusiveLineAmount»**. |
| **TaxOnLineAmount** | Tax amount for individual line item. |
| **TaxRateName** | Tax rate name. |
| **TaxPercentage** | Tax percentage. |
| **TaxPercentageOrName** | Displays tax rate as a percentage if greater than 0%, otherwise displays full tax rate name. |
| **TaxRateName** | Full tax rate name. |

Purchase order template fields

| Fields you can insert in template | Description of field |
| --- | --- |
| **ContactContactNumber** | Contact's phone number. |
| **ContactEmailAddress** | Contact's email address. |
| **ContactFirstName** | Contact's first name. |
| **ContactLastName** | Contact's last name. |
| **ContactPhysicalAddress** | Contact's street address, in the regional format of the organisation. Combination of all delivery address fields. |
| **ContactPhysicalAddressLines** | Contact's delivery (street) address (lines 1-4). |
| **ContactPhysicalAttentionTo** | Attention to field (delivery/street address). |
| **ContactPhysicalCity** | Contact's city (delivery/street address). |
| **ContactPhysicalCountry** | Contact's country (delivery/street address). |
| **ContactPhysicalPostCode** | Contact's postcode (delivery/street address). |
| **ContactPhysicalRegion** | Contact's region (delivery/street address). |
| **ContactPostalAddressLines** | Contact's billing (postal) address (lines 1-4). |
| **ContactPostalAttentionTo** | Attention to field (billing/postal address). |
| **ContactPostalCity** | Contact's city (billing/postal address). |
| **ContactPostalCountry** | Contact's country (billing/postal address). |
| **ContactPostalPostCode** | Contact's postal or zip code (billing/postal address). |
| **ContactPostalRegion** | Contact's region (billing/postal address). |
| **CurrencyRate** | Currency rate used on multicurrency. |
| **DefaultCurrency** | [The ISO 4217 currency code](http://www.iso.org/iso/currency_codes) (ISO website). |
| **DefaultCurrencyTaxAmount** | Amount of tax paid in default currency. |
| **DeliveryContact** | Delivery Contact. |
| **DeliveryPhone** | Delivery telephone number. |
| **DeliveryAddress** | Delivery address. |
| **DeliveryInstructions** | Delivery instructions. |
| **DiscountAmount** | Amount of discount for given line. |
| **DiscountPercentage** | Discount percentage for given line. |
| **DiscountedUnitPrice** | Unit price less the discount. |
| **InvoiceTaxTotal** | Tax total. |
| **ItemName** | Inventory item name. |
| **MultiCurrencyDisplayMessage** | Combination of {{Default Currency Tax Message}} and {{CurrencyConversionMessage}}. Used in sample template. |
| **OrganisationPhysicalAddress** | Organisation's physical address, in the regional format of the organisation. Combination of all physical address fields. |
| **OrganisationPhysicalAddressLines** | Organisation's physical address (lines 1-4). |
| **OrganisationPhysicalAttentionTo** | Attention to field. |
| **OrganisationPhysicalCity** | Organisation's city (physical address). |
| **OrganisationPhysicalCountry** | Organisation's country (physical address). |
| **OrganisationPhysicalPostCode** | Organisation's postcode (physical address). |
| **OrganisationPhysicalRegion** | Organisation's region (physical address). |
| **OrganisationPostalAddressLines** | Organisation's postal address (lines 1-4). |
| **OrganisationPostalAttentionTo** | Attention to field. |
| **OrganisationPostalCity** | Organisation's city (postal address). |
| **OrganisationPostalCountry** | Organisation's country (postal address). |
| **OrganisationPostalPostCode** | Organisation's postal or zip code (postal address). |
| **OrganisationPostalRegion** | Organisation's region (postal address). |
| **OrganisationTaxNumber** | GST number. |
| **QuantityTotal** | Sum of the quantity column. |
| **RegistrationNumber** | NZBN. |
| **TaxInclusiveDiscountAmount** | Amount of discount for line, tax inclusive. |
| **TaxInclusiveDiscountUnitPrice** | Unit price less the discount, tax inclusive. |
| **TaxInclusiveLineAmount** | Tax inclusive line amount. Replace field **«LineAmount»** with this field. Also insert field **«TaxInclusiveUnitAmount»**. |
| **TaxInclusiveTotalDiscountAmount** | Total combined discount across all lines, tax inclusive. |
| **TaxInclusiveUnitAmount** | Tax inclusive unit amount. Replace field **«UnitAmount»** with this field. Also insert field **«TaxInclusiveLineAmount»**. |
| **TaxOnLineAmount** | Tax amount for individual line item. |
| **TaxRateName** | Tax rate name. |
| **TotalDiscountAmount** | Total combined discount across all lines. |
| **TaxPercentage** | Tax percentage. |
| **TaxPercentageOrName** | Displays tax rate as a percentage if greater than 0%, otherwise displays full tax rate name. |
| **TaxRateName** | Full tax rate name. |

## What's next?

Once you’ve identified the fields you want to add, [insert them into your template](Add-or-edit-advanced-invoices-quotes-templates.md).