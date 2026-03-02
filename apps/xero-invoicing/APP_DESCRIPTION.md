# Xero Invoicing App

## Summary

A web application simulating Xero's invoicing module, enabling users to manage sales invoices, quotes, credit notes, repeating invoices, branding themes, invoice reminders, and invoice settings. The app is built around an Australian company ("Demo Company Pty Ltd") with a comprehensive set of contacts, transactions, and configuration data. All interactions are client-side with state synced to a server via REST API.

## Main Sections/Pages

1. **Dashboard** (`#/dashboard`) — Sales overview with summary cards showing draft, awaiting approval, awaiting payment, and overdue invoice counts/totals, plus a recent invoices table
2. **Invoices** (`#/invoices`) — Invoice list with tab filtering, create/edit forms, and detail views with payment management
3. **Quotes** (`#/quotes`) — Quote list with tab filtering, create/edit forms, detail views, and conversion to invoices
4. **Credit Notes** (`#/credit-notes`) — Credit note list, create/edit forms, detail views, and allocation to invoices
5. **Repeating Invoices** (`#/repeating-invoices`) — Repeating invoice list and create/edit forms for recurring billing
6. **Invoice Settings** (`#/settings`) — Transaction numbering, default due dates, tax mode, and display options
7. **Branding Themes** (`#/templates`) — Invoice template management (create, edit, delete, set default)
8. **Invoice Reminders** (`#/reminders`) — Automated reminder configuration with timing, email templates, and enable/disable toggle

## Complete List of Implemented Features and UI Interactions

### Invoices
- List view with tabs: All, Draft, Awaiting Approval, Awaiting Payment, Overdue, Paid
- Create new invoice with contact selection, dates, reference, currency, branding theme, tax mode, title, summary
- Edit existing invoices
- Line items with item selection (auto-fills description/price), quantity, unit price, discount %, account, tax rate, tracking categories (Region, Department)
- Auto-calculation of line amounts, subtotal, tax, and total based on tax mode (inclusive/exclusive/none)
- Save as Draft, Submit for Approval, or Approve directly
- Approve invoices (moves from draft/awaiting_approval to awaiting_payment)
- Send invoice (marks as sent, changes status to awaiting_payment)
- Mark as Sent
- Void invoice (with confirmation dialog)
- Delete invoice (with confirmation dialog)
- Copy invoice to new draft
- Create credit note from invoice (pre-fills contact and line items)
- Record payment (modal with date, amount, reference, bank account selection)
- Record partial payments (multiple payments per invoice)
- Remove payments
- Automatic status transition to "paid" when amount due reaches zero
- View payment history
- View history & notes (audit trail of all actions)
- Search invoices by number, contact name, reference, or amount

### Quotes
- List view with tabs: All, Draft, Sent, Accepted, Declined
- Create new quote with contact, dates, expiry date, reference, currency, theme, tax mode, title, summary, terms
- Edit existing quotes
- Line items identical to invoices
- Save as Draft or Save and Send
- Send quote (changes status to sent)
- Mark as Accepted
- Mark as Declined
- Create invoice from accepted quote (copies all line items, marks quote as invoiced)
- Copy quote to new draft
- Delete quote
- Invoiced badge indicator on quotes that have been converted

### Credit Notes
- List view with tabs: All, Draft, Open (awaiting_payment), Allocated (paid)
- Create new credit note with contact, date, reference, tax mode, line items
- Edit existing credit notes
- Save as Draft or Approve directly
- Approve credit note (moves to awaiting_payment)
- Allocate credit note to an open invoice (modal showing available invoices for same contact)
- Allocation reduces both credit note remaining credit and invoice amount due
- Automatic status transitions when fully allocated
- Delete credit note
- View allocations with links to allocated invoices

### Repeating Invoices
- List view showing contact, frequency, next invoice date, end date, save-as mode, status
- Create new repeating invoice with contact, frequency (weekly/fortnightly/monthly/bimonthly/quarterly/annually), start date, next date, end date
- Configure save-as mode: Draft, Approved, or Approved for Sending
- Branding theme and tax mode selection
- Line items with item, description, quantity, price, account, tax rate
- Reference field
- Edit existing repeating invoices
- Delete repeating invoices

### Invoice Settings
- Invoice prefix and next number (e.g., "INV-" starting at 67)
- Credit note prefix and next number (e.g., "CN-" starting at 13)
- Quote prefix and next number (e.g., "QU-" starting at 30)
- Default due date configuration (days after invoice, days after end of month, end of following month, end of current month)
- Default tax mode (Exclusive/Inclusive/No Tax)
- Display toggles: show tax column, show discount column, show item code

### Branding Themes
- Grid view of all themes with default indicator
- Create new theme with name, payment terms, terms & conditions
- Toggle options: show tax number, show payment advice
- Edit existing themes
- Set a theme as default (highlighted with blue border)
- Delete non-default themes

### Invoice Reminders
- List of configured reminders with enable/disable toggles
- Each reminder has: timing (before/after due date), number of days, email subject, email body
- Toggle reminders on/off individually
- Create new reminders
- Edit existing reminders
- Delete reminders
- Options to include invoice PDF and detail summary

### Search
- Global search bar in top navigation
- Searches across invoices, quotes, and credit notes
- Matches on: transaction number, contact name, reference, amount
- Results table with type, number, contact, date, total, status
- Clickable results navigate to detail view

### General UI
- Custom dropdowns (no native `<select>` elements) with click-to-open and item selection
- Searchable dropdowns for contact selection with type-to-filter
- Date inputs with YYYY-MM-DD format
- Toast notifications for all actions (success/error)
- Confirmation dialogs for destructive actions (void, delete)
- Modal overlays for payments and credit note allocation
- Hash-based routing for all views
- SSE connection for server-triggered resets
- LocalStorage persistence with seed version checking
- Full state push to server on every mutation

## Data Model

### Contacts (25 records)
- `id`: string (con_001 - con_025)
- `name`: string (company name)
- `email`: string
- `phone`: string
- `contactPerson`: string
- `address`: string
- `taxNumber`: string (ABN format)
- `defaultThemeId`: references BrandingTheme
- `defaultDueDate`: object { type, days }
- `defaultTaxRateId`: references TaxRate
- `outstandingBalance`: number
- `overdueBalance`: number
- `isCustomer`: boolean
- `isSupplier`: boolean

### Invoices (25 records)
- `id`: string (inv_001 - inv_025)
- `number`: string (INV-0042 through INV-0066)
- `contactId`: references Contact
- `status`: enum (draft | awaiting_approval | awaiting_payment | paid | voided | deleted)
- `date`: string (YYYY-MM-DD)
- `dueDate`: string (YYYY-MM-DD)
- `reference`: string
- `currency`: string (currency code, e.g., AUD, NZD)
- `brandingThemeId`: references BrandingTheme
- `taxMode`: enum (exclusive | inclusive | none)
- `lineItems`: array of LineItem
- `subtotal`: number
- `taxTotal`: number
- `total`: number
- `amountDue`: number
- `amountPaid`: number
- `payments`: array of Payment
- `notes`: array of { date, text, user }
- `sentAt`: string (ISO datetime) or null
- `title`: string
- `summary`: string

### LineItem (embedded in invoices/quotes/credit notes)
- `id`: string
- `itemId`: references Item (or null for custom)
- `description`: string
- `quantity`: number
- `unitPrice`: number
- `discountPercent`: number (0-100)
- `accountId`: references Account
- `taxRateId`: references TaxRate
- `trackingRegion`: references TrackingCategory option (or empty)
- `trackingDept`: references TrackingCategory option (or empty)

### Payment (embedded in invoices)
- `id`: string
- `date`: string (YYYY-MM-DD)
- `amount`: number
- `reference`: string
- `accountId`: references Account (Bank type)

### Quotes (8 records)
- `id`: string (quo_001 - quo_008)
- `number`: string (QU-0022 through QU-0029)
- `contactId`: references Contact
- `status`: enum (draft | sent | accepted | declined | deleted)
- `date`: string
- `expiryDate`: string
- `reference`: string
- `currency`: string
- `brandingThemeId`: references BrandingTheme
- `taxMode`: enum
- `lineItems`: array of LineItem
- `subtotal`, `taxTotal`, `total`: numbers
- `title`: string
- `summary`: string
- `terms`: string
- `notes`: array
- `sentAt`: string or null
- `isInvoiced`: boolean

### Credit Notes (5 records)
- `id`: string (cn_001 - cn_005)
- `number`: string (CN-0008 through CN-0012)
- `contactId`: references Contact
- `status`: enum (draft | awaiting_payment | paid | deleted)
- `date`: string
- `reference`: string
- `currency`: string
- `brandingThemeId`: references BrandingTheme
- `taxMode`: enum
- `lineItems`: array of LineItem
- `subtotal`, `taxTotal`, `total`: numbers
- `remainingCredit`: number
- `allocations`: array of { invoiceId, invoiceNumber, amount, date }
- `refunds`: array
- `notes`: array

### Repeating Invoices (5 records)
- `id`: string (rep_001 - rep_005)
- `contactId`: references Contact
- `status`: enum (active | draft)
- `frequency`: enum (weekly | fortnightly | monthly | bimonthly | quarterly | annually)
- `startDate`, `nextDate`, `endDate`: strings
- `currency`: string
- `brandingThemeId`: references BrandingTheme
- `taxMode`: enum
- `saveAs`: enum (draft | approved | approved_for_sending)
- `lineItems`: array (simplified - no tracking/discount)
- `dueDate`: object { type, days }
- `reference`: string
- `emailSubject`, `emailBody`: strings

### Items (15 records, product/service catalog)
- `id`: string (item_001 - item_015)
- `code`: string (e.g., DEV-HOUR, CONSULT-HR, WIDGET-A)
- `description`: string
- `unitPrice`: number
- `accountId`: references Account
- `taxRateId`: references TaxRate
- `isSold`: boolean
- `isPurchased`: boolean

### Tax Rates (6 records)
- `id`: string (tax_gst, tax_gst_free, tax_bas_excluded, tax_gst_input, tax_gst_free_exp, tax_exempt)
- `name`: string
- `rate`: number (0 or 10)
- `isDefault`: boolean
- `type`: enum (output | input | none)

### Accounts (30 records, chart of accounts)
- `id`: string (acc_090 - acc_820)
- `code`: string (e.g., 200, 260, 400)
- `name`: string
- `type`: enum (Revenue | Direct Costs | Expense | Current Asset | Current Liability | Bank)

### Tracking Categories (2 categories)
- Region: New South Wales, Victoria, Queensland, Western Australia, South Australia
- Department: Sales, Marketing, Operations, Support, Administration

### Currencies (9 records)
- AUD, USD, GBP, NZD, EUR, SGD, JPY, CAD, HKD

### Branding Themes (4 records)
- `id`: string (theme_standard, theme_professional, theme_simple, theme_retail)
- `name`: string
- `isDefault`: boolean
- `paymentTerms`: string
- `termsAndConditions`: string
- `showTaxNumber`, `showPaymentAdvice`: booleans

### Invoice Settings (singleton)
- `invoicePrefix`: "INV-", `invoiceNextNumber`: 67
- `creditNotePrefix`: "CN-", `creditNoteNextNumber`: 13
- `quotePrefix`: "QU-", `quoteNextNumber`: 30
- `defaultDueDate`: { type: "daysAfterInvoice", days: 30 }
- `defaultQuoteExpiry`: { type: "daysAfterQuote", days: 30 }
- `defaultTaxMode`: "exclusive"
- `showTaxColumn`, `showDiscountColumn`, `showItemCode`: booleans

### Invoice Reminders (4 records)
- 7 days before due date (enabled)
- 1 day after due date (enabled)
- 14 days after due date (enabled)
- 30 days after due date (disabled)

## Navigation Structure

Sidebar navigation:
- **Dashboard** → `#/dashboard`
- **Sales section:**
  - Invoices → `#/invoices` (tabs filter the list)
  - Quotes → `#/quotes` (tabs filter the list)
  - Credit Notes → `#/credit-notes` (tabs filter the list)
  - Repeating Invoices → `#/repeating-invoices`
- **Settings section:**
  - Invoice Settings → `#/settings`
  - Branding Themes → `#/templates`
  - Invoice Reminders → `#/reminders`

Sub-routes:
- `#/invoices/new` — Create invoice form
- `#/invoices/{id}` — Invoice detail view
- `#/invoices/edit/{id}` — Edit invoice form
- `#/quotes/new`, `#/quotes/{id}`, `#/quotes/edit/{id}` — Quote routes
- `#/credit-notes/new`, `#/credit-notes/{id}`, `#/credit-notes/edit/{id}` — Credit note routes
- `#/repeating-invoices/new`, `#/repeating-invoices/edit/{id}` — Repeating invoice routes
- `#/templates/new`, `#/templates/edit/{id}` — Branding theme routes
- `#/reminders/new`, `#/reminders/edit/{id}` — Reminder routes

## Available Form Controls

### Dropdowns (custom, non-native)
- Contact selector (searchable with type-to-filter, 24 customer contacts)
- Currency (9 options: AUD, USD, GBP, NZD, EUR, SGD, JPY, CAD, HKD)
- Branding Theme (4 options: Standard, Professional Services, Simple Clean, Retail)
- Tax Mode (3 options: Tax Exclusive, Tax Inclusive, No Tax)
- Item selector per line (15 items: DEV-HOUR, CONSULT-HR, PM-DAY, HOSTING-MO, SUPPORT-MO, TRAINING, DESIGN-HR, LICENSE-AN, AUDIT, DATA-MIG, WIDGET-A, WIDGET-B, CABLE-USB, SETUP-FEE, TRAVEL)
- Account per line (revenue/direct cost accounts: 200 Sales, 210 Interest Income, 215 Other Revenue, 260 Consulting, 270 Advertising, 300 Purchases, 310 COGS)
- Tax Rate per line (GST on Income 10%, GST Free Income 0%, BAS Excluded 0%, Tax Exempt 0%)
- Region tracking per line (5 options: NSW, VIC, QLD, WA, SA + None)
- Department tracking per line (5 options: Sales, Marketing, Operations, Support, Administration + None)
- Frequency for repeating invoices (Weekly, Fortnightly, Monthly, Every 2 Months, Quarterly, Annually)
- Save As for repeating invoices (Draft, Approved, Approved for Sending)
- Due date type (days after invoice date, days after end of month, of the following month, of the current month)
- Bank account for payments (Business Bank Account, Business Savings Account)
- Invoice selector for credit note allocation (filtered to same contact, open invoices only)
- Reminder timing (Before due date, After due date)

### Toggles
- Show tax column (Invoice Settings)
- Show discount column (Invoice Settings)
- Show item code (Invoice Settings)
- Show tax number (Branding Theme)
- Show payment advice (Branding Theme)
- Include invoice PDF (Reminders)
- Include detail summary (Reminders)
- Enable/disable individual reminders

### Text Inputs
- Invoice/quote/CN number prefix
- Next number (numeric)
- Due date days (numeric)
- Reference field on all transactions
- Title field on invoices and quotes
- Search input in top bar
- Line item description
- Line item quantity, unit price, discount % (numeric)
- Payment date, amount (numeric), reference
- Theme name
- Reminder days (numeric), subject, email body
- Credit note allocation amount (numeric)

### Text Areas
- Invoice/quote summary
- Quote terms & conditions
- Theme payment terms
- Theme terms & conditions
- Reminder email body

### Date Inputs
- Invoice date, due date
- Quote date, expiry date
- Credit note date
- Repeating invoice start date, next date, end date
- Payment date

## Seed Data Summary

### Organization
- **Demo Company (AU)** / Demo Company Pty Ltd, ABN 12 345 678 901, based at 100 Queen Street, Melbourne VIC 3000

### Contacts (25 businesses)
Key contacts: Pinnacle Construction Group (Melbourne), TechVault Solutions (Sydney), Greenfield Organics (Brisbane), Horizon Media & Advertising (Sydney), Baxter & Associates Legal (Melbourne), Pacific Freight Lines (Perth), CloudNine Analytics (Sydney), Murray River Winery (Echuca VIC), Stellar Education Services (Brisbane), Redback Mining Supplies (Perth), Coastal Living Interiors (Bondi Beach), Alpha Logistics International (Melbourne), Bright Spark Electrical (Brisbane), Summit Health Group (Sydney), Outback Adventures Tourism (Alice Springs), Wellington & Partners (NZ), Northern Territory Power Corp (Darwin), Sapphire Bay Resort (Cairns), Metro Fabrication Works (Port Melbourne), Cascade Software Solutions (Canberra), Harbour City Plumbing (Pyrmont), Fresh Start Catering (Melbourne), Vanguard Security Systems (Perth), Southern Cross Veterinary (Kew VIC), Atlas Engineering Consultants (Brisbane)

### Invoices (25 total)
- 5 Paid (INV-0042 through INV-0066, including one in NZD)
- 1 Voided (INV-0065)
- 3 Draft (INV-0058, INV-0059, INV-0060)
- 2 Awaiting Approval (INV-0056, INV-0057)
- 13 Awaiting Payment (INV-0045 through INV-0055, plus INV-0061, INV-0062, INV-0063, INV-0054)
- Amounts range from $328.90 to $41,800.00
- One invoice has partial payment applied (INV-0045: $4,950 of $15,840 paid)

### Quotes (8 total)
- 3 Accepted (QU-0022, QU-0027, QU-0029 — one marked as invoiced)
- 3 Sent (QU-0023, QU-0024, QU-0028)
- 1 Draft (QU-0025)
- 1 Declined (QU-0026)
- Amounts range from $4,940 to $76,725

### Credit Notes (5 total)
- 2 Paid/Allocated (CN-0008 to INV-0045, CN-0010 to INV-0043)
- 2 Awaiting Payment/Open (CN-0009 for $249.75, CN-0012 for $2,035)
- 1 Draft (CN-0011 for $968)

### Repeating Invoices (5 total)
- 4 Active (monthly: Greenfield Organics, CloudNine Analytics, Cascade Software, Vanguard Security)
- 1 Draft (quarterly: Summit Health Group)

### Items (15 products/services)
Services: DEV-HOUR ($185), CONSULT-HR ($250), PM-DAY ($1,400), HOSTING-MO ($299), SUPPORT-MO ($450), TRAINING ($2,200/day), DESIGN-HR ($165), LICENSE-AN ($1,200), AUDIT ($5,500), DATA-MIG ($3,800), SETUP-FEE ($500), TRAVEL (reimbursable)
Products: WIDGET-A ($24.95), WIDGET-B ($49.95), CABLE-USB ($12.50)
