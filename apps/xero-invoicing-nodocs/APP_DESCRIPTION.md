# Xero Invoicing — App Description

## Summary

A cloud-based invoicing application modeled after Xero's invoicing module. The app manages the full invoice lifecycle for "Kiwi Consulting Ltd" — from creation through approval, sending, payment recording, and voiding. It includes contact management, invoice settings, and a reporting dashboard with aging summaries.

## Main Sections / Pages

### 1. Dashboard (`#/dashboard`)
- Summary stat cards: Total Invoiced, Outstanding, Overdue, Paid
- Aging summary table: Current, 1–30 days, 31–60 days, 61–90 days, 90+ days
- Invoice status breakdown (count per status)
- Recent invoices table (10 most recent)

### 2. Invoice List (`#/invoices`)
- Paginated table (20 per page) of all 113 invoices
- Columns: Number, Reference, To (contact), Date, Due Date, Total, Due, Status
- **Filters**: Status dropdown, Contact dropdown, Date From, Date To, Search text
- **Sorting**: Click any column header to sort asc/desc
- **Bulk actions**: Select invoices via checkboxes → Approve, Send, Delete Drafts
- **Pagination**: Page navigation with "Showing X–Y of Z" indicator

### 3. Invoice Detail (`#/invoices/{id}`)
- Professional invoice preview layout with company details and billing address
- Invoice metadata: number, reference, dates, currency
- Line items table with description, quantity, unit price, tax, account, amount
- Totals section: subtotal, tax, total, amount paid, amount due
- Notes section
- **Payments section**: Lists all payments with date, amount, bank account, reference; allows removal
- **Activity timeline**: Chronological log (created, approved, sent, payment, voided events)
- **Action buttons** (context-dependent on status):
  - Draft: Edit, Approve, Approve & Send, Delete
  - Awaiting Approval: Edit, Approve, Approve & Send
  - Awaiting Payment/Overdue: Edit, Add Payment, Resend, Mark as Sent, Copy, Void
  - Paid: Copy to New

### 4. Invoice Create/Edit Form (`#/new-invoice` or `#/edit-invoice/{id}`)
- **Contact selection**: Searchable dropdown of all contacts, with "Add new contact" quick-add button
- **Invoice number**: Auto-generated (e.g., INV-0121) or custom editable
- **Reference**: Free text field
- **Invoice date** and **Due date**: Text inputs (YYYY-MM-DD format)
- **Currency**: Dropdown (NZD, AUD, USD, GBP, EUR, CAD, JPY, SGD, HKD, CNY, FJD)
- **Branding theme**: Dropdown (Standard, Professional Blue, Minimal Clean, Bold Corporate)
- **Line items table**: Each row has:
  - Description (text input)
  - Quantity (number input)
  - Unit Price (number input)
  - Tax Rate (dropdown: GST on Income 15%, No GST 0%, Zero Rated, Exempt, AU GST 10%, US Sales Tax 8.5%, etc.)
  - Account Code (dropdown: 200-Sales, 210-Interest Income, 260-Other Revenue, 270-Consulting Revenue, 280-Service Revenue, 290-Subscription Revenue, 300-Licensing Revenue, 310-Training Revenue, 320-Rental Revenue)
  - Line Total (auto-calculated: qty × unit price)
  - Remove button
- **Add Line Item** button
- Auto-calculated totals: Subtotal, Tax (GST), Total
- **Notes/Memo**: Textarea
- **Save buttons**: "Save as Draft" or "Approve"
- **Validation**: Contact required, dates required, at least one line item required

### 5. Record Payment (Modal from Invoice Detail)
- Amount (pre-filled with amount due, max = amount due)
- Date (YYYY-MM-DD, defaults to today)
- Bank Account dropdown (Business Cheque Account, Business Savings Account, USD Holding Account, AUD Holding Account, Credit Card - Visa)
- Reference text field
- Note text field
- Exchange Rate (shown only for foreign currency invoices)
- Supports partial payments (multiple payments per invoice)

### 6. Contacts (`#/contacts`)
- Paginated table of all 25 contacts
- Columns: Name (with avatar), Email, Phone, City, Outstanding balance
- Search by name, email, or phone
- "New Contact" button

### 7. Contact Detail (`#/contacts/{id}`)
- Contact info: Email, Phone, Tax ID, Type, Created date
- Billing address
- Financial summary: Outstanding balance, Total invoices count
- Invoice history table for this contact
- Edit and Delete buttons (delete only if no invoices)

### 8. Invoice Settings (`#/settings`)
- **Default Due Date Terms**: Dropdown (7/14/20/30/60 days after invoice, End of month, End of month + 7/14/30 days)
- **Default Tax Rate**: Dropdown of all tax rates
- **Invoice Number Sequence**: Prefix (text, default "INV-"), Next Number (number, default 121), Zero Padding (number, default 4)
- **Default Branding Theme**: Dropdown
- **Default Email Template**: Subject and Body text fields with placeholders ({ContactName}, {InvoiceNumber}, {Total}, {DueDate})
- **Late Payment Penalty**: Toggle enable/disable, Penalty Rate % (default 1.5), Frequency (Monthly/Weekly/Daily)
- **Company Details**: Company Name, Email, Phone, Address, Tax ID/GST Number
- **Save Settings** button

## Data Model

### Contacts (25 entities)
- `id` (con_1 through con_25)
- `name`, `email`, `phone`
- `billingAddress` { street, city, region, postalCode, country }
- `taxId`, `contactType` ("customer"), `createdAt`

### Invoices (113 entities)
- `id` (inv_1 through inv_113)
- `invoiceNumber` (INV-0001 through INV-0113)
- `reference` (PO numbers, REF numbers, job numbers, or empty)
- `contactId` (references a contact)
- `status`: draft | awaiting_approval | awaiting_payment | paid | overdue | voided
- `issueDate`, `dueDate` (YYYY-MM-DD strings)
- `currency` (mostly NZD, some AUD and USD)
- `lineItems[]` — each: { id, description, quantity, unitPrice, taxRateId, accountCode, lineTotal }
- `subtotal`, `taxTotal`, `total`, `amountPaid`, `amountDue`
- `notes`, `brandingThemeId`
- `createdAt`, `updatedAt`, `sentAt`, `paidAt`, `voidedAt` (ISO timestamps)
- `activity[]` — each: { type, date, user, detail }

### Payments (46 entities)
- `id` (pay_1 through pay_46+)
- `invoiceId` (references an invoice)
- `date` (YYYY-MM-DD), `amount`, `bankAccountId`, `reference`, `note`, `exchangeRate`

### Tax Rates (8 entries)
| ID | Name | Rate |
|----|------|------|
| tax_1 | GST on Income (15%) | 15% |
| tax_2 | GST on Expenses (15%) | 15% |
| tax_3 | No GST (0%) | 0% |
| tax_4 | GST on Imports (15%) | 0% |
| tax_5 | Zero Rated (0%) | 0% |
| tax_6 | Exempt (0%) | 0% |
| tax_7 | AU GST on Income (10%) | 10% |
| tax_8 | US Sales Tax (8.5%) | 8.5% |

### Account Codes (15 entries)
Revenue accounts: 200-Sales, 210-Interest Income, 260-Other Revenue, 270-Consulting Revenue, 280-Service Revenue, 290-Subscription Revenue, 300-Licensing Revenue, 310-Training Revenue, 320-Rental Revenue
Expense accounts: 400-Advertising, 410-Bank Fees, 420-Cleaning, 460-Printing & Stationery, 470-Rent, 489-Software Licenses

### Bank Accounts (5 entries)
- Business Cheque Account (NZD)
- Business Savings Account (NZD)
- USD Holding Account (USD)
- AUD Holding Account (AUD)
- Credit Card - Visa (NZD)

### Currencies (11 entries)
NZD, AUD, USD, GBP, EUR, CAD, JPY, SGD, HKD, CNY, FJD

### Branding Themes (4 entries)
Standard (default), Professional Blue, Minimal Clean, Bold Corporate

### Settings
- `defaultDueDateTerms`: "20" (days after invoice)
- `defaultTaxRateId`: "tax_1" (GST on Income 15%)
- `invoiceNumberPrefix`: "INV-"
- `invoiceNumberNextNumber`: 121
- `invoiceNumberPadding`: 4
- `defaultBrandingThemeId`: "theme_1"
- `defaultEmailSubject`: "Invoice {InvoiceNumber} from Kiwi Consulting Ltd"
- `defaultEmailBody`: Template with placeholders
- `latePenaltyEnabled`: false
- `latePenaltyRate`: 1.5
- `latePenaltyFrequency`: "monthly"
- Company: "Kiwi Consulting Ltd", accounts@kiwiconsulting.co.nz, +64 9 555 0100
- Address: "25 Queen Street, Level 5, Auckland 1010, New Zealand"
- Tax ID: "NZ-12-345-678"

## Navigation Structure

| Route | View | How to Reach |
|-------|------|-------------|
| `#/dashboard` | Dashboard summary | Sidebar "Dashboard" link |
| `#/invoices` | Invoice list | Sidebar "Invoices" link |
| `#/invoices/{id}` | Invoice detail | Click invoice number in list |
| `#/new-invoice` | Create invoice form | "New Invoice" button on list page |
| `#/edit-invoice/{id}` | Edit invoice form | "Edit" button on detail page |
| `#/contacts` | Contacts list | Sidebar "Contacts" link |
| `#/contacts/{id}` | Contact detail | Click contact row in list |
| `#/settings` | Invoice settings | Sidebar "Settings" link |

## Seed Data Summary

### Invoice Status Distribution
| Status | Count |
|--------|-------|
| Paid | 42 |
| Awaiting Payment | 30 |
| Overdue | 14 |
| Draft | 12 |
| Awaiting Approval | 10 |
| Voided | 5 |
| **Total** | **113** |

### Contacts (25 businesses)
- Ridgeway University (Auckland), Hamilton Plumbing Services (Hamilton), Coastal Cafe Group (Queenstown), Nexus Technologies Ltd (Wellington), Bright Spark Electrical (Auckland), Summit Financial Advisors (Christchurch), Green Valley Organics (Palmerston North), Metro Print Solutions (Auckland), Pinnacle Construction Co (Tauranga), Oceanview Resort & Spa (Auckland), DataFlow Analytics Inc (San Francisco, USA), Swift Courier Services (Auckland), Harmony Music Academy (Wellington), Pacific Timber Supplies (Rotorua), Bloom & Branch Florists (Auckland), Ironclad Security Systems (Auckland), Clearwater Environmental (Nelson), Apex Legal Partners (Wellington), TrueNorth Marketing Agency (Auckland), Heritage Craft Brewery (Dunedin), CloudBridge Software (Sydney, Australia), Meridian Health Clinic (Auckland), Redwood Property Management (Auckland), Atlas Import/Export Ltd (Auckland), Velocity Sports Equipment (Hamilton)

### Invoice Date Range
- Invoices span October 2025 through March 2026
- Due dates: 7, 14, 20, or 30 days after issue date
- Currencies: Mostly NZD, some AUD (~7%) and USD (~7%)

### Line Items
- Each invoice has 1–4 line items
- Descriptions cover: IT/tech services, accounting, marketing, training, consulting, legal, environmental, logistics, events, construction
- Unit prices range from $45 to $2,500
- Quantities range from 0.5 to 100

### Payments
- 46 payment records across paid and partially-paid invoices
- All paid invoices have exactly one full payment
- Some awaiting_payment invoices have partial payments
- Exchange rates: NZD=1, AUD=1.08, USD=1.58

## Available Form Controls

### Dropdowns (Custom, non-native)
- Invoice status filter (7 options including "All")
- Contact filter (25 contacts + "All")
- Contact selection on invoice form (searchable)
- Currency selection (11 currencies)
- Branding theme (4 themes)
- Tax rate per line item (8 rates)
- Account code per line item (9 revenue accounts)
- Bank account for payments (5 accounts)
- Due date terms in settings (9 options)
- Default tax rate in settings
- Default branding theme in settings
- Late penalty frequency (Monthly/Weekly/Daily)

### Text Inputs
- Invoice search (number, reference, contact name)
- Contact search (name, email, phone)
- Invoice number, Reference, Notes
- Date fields (invoice date, due date, payment date)
- Settings: email subject, prefix, company details
- Contact form: name, email, phone, address fields, tax ID

### Number Inputs
- Line item quantity and unit price
- Payment amount and exchange rate
- Settings: next invoice number, zero padding, penalty rate

### Toggles
- Late payment penalty enable/disable

### Checkboxes
- Individual invoice selection in list
- Select all invoices on current page

### Action Buttons
- New Invoice, Save as Draft, Approve, Approve & Send
- Edit, Delete, Void, Copy to New, Mark as Sent, Resend
- Add Payment, Save Payment, Remove Payment
- New Contact, Save Contact, Delete Contact
- Save Settings
- Bulk: Approve, Send, Delete Drafts, Clear Selection
