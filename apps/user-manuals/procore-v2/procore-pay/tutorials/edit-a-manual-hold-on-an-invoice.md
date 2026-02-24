# Edit a Manual Hold on a Subcontractor Invoice

Source: https://v2.support.procore.com/product-manuals/procore-pay/tutorials/edit-a-manual-hold-on-an-invoice

---

##### Â General Availability in Select Markets (United States)

[Procore Pay](https://www.procore.com/pay)  is available in the United States. It is designed for General Contractors and Owner-Builders who act as their own General Contractors on a job. Procore Pay extends the [Invoice Management](https://www.procore.com/invoice-management) functionality in the Procore web application to handle the payment process between general and specialty contractors.

## Background

With Procore Pay, manual holds can be applied to 

A Subcontractor Invoice is a request for payment submitted by a business or individual who has entered into a binding agreement with another contracting party. In Procore, a subcontractor invoice is an equivalent term for a payable invoice.

Subcontractor Invoice payments for a variety of reasons. These include quality issues, such as when delivered work is subpar or warranty support is uncertain. Holds might also be applied for incomplete work, work not meeting the specified quality level, contract disputes, financial concerns, or compliance issues. Whatever your reason for applying a hold, Procore Pay users can apply these hold types on subcontractor invoices:

- **Invoice Holds**. A 

  In Procore Pay, a *Payments Admin* is a designated Procore user who administers the Company level Payments tool for that company's Procore account. Typically, one (1) or a small number of trusted users are designated to perform the tasks associated with this role.

  Payments Admin, 

  In Procore Pay, a *Payments Disburser* is a Procore user granted permission to create and view disbursements in the Company level Payments tool. Because of the sensitive nature of payments, only a Payments Admin can add/remove disbursers.

  Payments Disburser, 

  An *Invoice Administrator* is a person or group of people responsible for collecting, reviewing, and creating invoices in Procore. An invoice administrator can be any person in your organization (for example, a project manager, an accountant, or a team of bookkeepers) who have been granted the appropriate permissions to manage invoices on your contracts and/or fundings.

  Invoice Administrator, and users with 'Admin' level permissions on the Payments tool can create an invoice hold to alert users about a hold on a specific subcontractor invoice.
- **Vendor Holds**. A 

  In Procore Pay, a *Payments Admin* is a designated Procore user who administers the Company level Payments tool for that company's Procore account. Typically, one (1) or a small number of trusted users are designated to perform the tasks associated with this role.

  Payments Admin or 

  In Procore Pay, a *Payments Disburser* is a Procore user granted permission to create and view disbursements in the Company level Payments tool. Because of the sensitive nature of payments, only a Payments Admin can add/remove disbursers.

  Payments Disburser, can apply a vendor hold to an invoice to alert users to pause payments on all of the vendor's invoices.

When creating a hold, users can also choose to share the hold with an invoice contact. Users can also edit the details of a hold. Once the conditions are satisfied, users can release the hold.

## Things to Consider

- [Required User Permissions](/product-manuals/procore-pay/permissions)
- **Additional Information**:

  - Users with the required user permissions create any number of *Invoice* or *Payment* holds on a subcontractor invoice. To learn more, see [What permissions do you need to manage holds on subcontractor invoices?](/faq-what-is-a-manual-hold-on-a-subcontractor-invoice)
  - To prevent Procore Pay users from creating disbursements that include subcontractor invoices with active holds, a [Payments Admin](/process-guides/payor-setup-guide/authorize-payment-admins) must [Configure Payment Requirements as a Payor](/process-guides/payor-setup-guide/configure-payment-requirements).

## Prerequisites

- [Create and Apply a Manual Hold on a Subcontractor Invoice](/process-guides/payor-setup-guide/create--apply-payment-holds)

## Video

## Steps

### What tool are you using?

Depending on your role and permissions settings, you can navigate to a subcontractor invoice from one of these tools:

**I am using the Payments tool.**

A 

In Procore Pay, a *Payments Admin* is a designated Procore user who administers the Company level Payments tool for that company's Procore account. Typically, one (1) or a small number of trusted users are designated to perform the tasks associated with this role.

Payments Admin or 

In Procore Pay, a *Payments Disburser* is a Procore user granted permission to create and view disbursements in the Company level Payments tool. Because of the sensitive nature of payments, only a Payments Admin can add/remove disbursers.

Payments Disburser can create, edit, view, and release *Invoice* or *Vendor* holds on subcontractor invoices from the Payments tool. They can also manage both types of holds on subcontractor invoices from the Payments tool.

##### Â Note

Users 'Admin' level permissions on the Payments tool are limited to creating *Invoice* holds. For more information, see

1. Navigate to the Company level **Payments** tool.
2. Click the **Subcontractor Invoices** tab. This tab is active by default.
3. Locate the invoice for the hold.
4. Choose one of these options:

   - Click the information icon to open the Payment Requirements panel.
   - Click the **Invoice #** link to open the invoice in the Project level **Commitments** tool. Then click the **Payment Requirements** tab.
5. Under **Payment Requirements**, click the **Holds** tab.

**I am using the Commitments tool.**

A 

In Procore Pay, a *Payments Admin* is a designated Procore user who administers the Company level Payments tool for that company's Procore account. Typically, one (1) or a small number of trusted users are designated to perform the tasks associated with this role.

Payments Admin or 

In Procore Pay, a *Payments Disburser* is a Procore user granted permission to create and view disbursements in the Company level Payments tool. Because of the sensitive nature of payments, only a Payments Admin can add/remove disbursers.

Payments Disburserthat has been granted invoice administrator permissions can create, edit, view, and release *Invoice* or *Vendor* holds on subcontractor invoices from the Commitments tool.

##### Â Note

Users granted only [Invoice administrator](/process-guides/payor-setup-guide/add-invoice-administrators) permissions are limited to creating, editing, and releasing *Invoice Holds*. For more information, see

1. Navigate to the Project level **Commitments** tool.
2. Under the **Contracts** tab, locate the contract in the table. Then, click the **Number** link to open it.
3. In the contract, click the **Invoices** tab.
4. Locate the invoice in the **Invoices (Requisitions)** table. Then, click the **Invoice #** link to open it.
5. In the invoice, click the **Holds** tab.