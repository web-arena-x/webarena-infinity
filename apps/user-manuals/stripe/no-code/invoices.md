# Use invoices

Source: https://docs.stripe.com/no-code/invoices

---

Send invoices

[Create account](https://dashboard.stripe.com/register/invoicing) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fno-code%2Finvoices)

[The Stripe Docs logo](/)

Search

`/`Ask AI

[Create account](https://dashboard.stripe.com/register/invoicing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fno-code%2Finvoices)

[Get started](/get-started)

[Payments](/payments)

[Revenue](/revenue)

[Platforms and marketplaces](/connect)

[Money management](/money-management)

[Developer resources](/development)

APIs & SDKsHelp

[Overview](/get-started)[See all products](/products)

About the APIs

[Stripe glossary](/glossary)

Start building

Create an account

[Quickstarts](/quickstarts)

Start developing

[Build with an LLM](/building-with-llms)

Use Stripe without code

[Overview](/no-code)

[Find your use case](/no-code/get-started)

[Create Payment Links](/no-code/payment-links)

[Create a buy button](/no-code/buy-button)

Send invoices

[Create subscriptions](/no-code/subscriptions)

[Send quotes](/no-code/quotes)

[Accept in-person payments](/no-code/in-person)

[Pay out money](/no-code/payout)

[Set up customer portal](/no-code/customer-portal)

[Dashboard assistant](/assistant)

Migrate to Stripe

Common use cases

[Overview](/get-started/use-cases)[Accept simple payments as a startup](/get-started/use-cases/startup)[Sell subscriptions as a SaaS startup](/get-started/use-cases/saas-subscriptions)[Build a subscriptions solution with usage-based pricing](/get-started/use-cases/usage-based-billing)[Accept payments in person](/get-started/use-cases/in-person-payments)[Send invoices to collect payments](/get-started/use-cases/invoices)

United StatesEnglish (United States)

# Use invoices

## Send an invoice your customers can pay online.

Ask about this page

Copy for LLMView as Markdown

- **Compatible with:** Customer portal, Hosted Invoice Page
- **Requires:** Stripe account
- **Good for:** Professional services, e-commerce businesses, B2B businesses
- **Pricing:** [Pay-as-you-go](https://stripe.com/pricing), [Stripe Billing pricing](https://stripe.com/billing/pricing) for recurring payments

Automatically charge your customer’s payment method on file, or email them the [invoice](/api/invoices) with or without a link to a payment page. You can also send the invoice or payment page link manually.

#### Note

To learn about managing subscriptions and recurring revenue, see the [Subscriptions](/billing) docs.

![Hosted Invoice Page](https://b.stripecdn.com/docs-statics-srv/assets/hosted-invoice-page-guide.df3cc5a1e4180c338269aacdfa792180.png)

Hosted Invoice Page

![Invoice PDF](https://b.stripecdn.com/docs-statics-srv/assets/invoice-pdf-guide.d79c407ca08ee4b14dc0519fb3772309.png)

Invoice PDF

[## Set up your business brand Optional](#establish-business)

Before you start using Stripe Invoicing, help your future customers understand your products and terms of service by [adding your business details](https://dashboard.stripe.com/settings/account?support_details) and [customizing how your brand appears](https://dashboard.stripe.com/settings/branding).

Customers see these business and branding details on the [Hosted Invoice Page](/invoicing/hosted-invoice-page) when they pay an invoice online. To let customers manage past invoices and their own billing information, set up the [customer portal](/no-code/customer-portal).

![Brand your business](https://b.stripecdn.com/docs-statics-srv/assets/hosted-invoice-page.79b4c18913fe9fb30f47ad8a5f062b6f.png)

Brand your business

[## Choose your payment methods Optional](#payment-methods)

By default, customers can pay invoices with any of the payment methods that you enable in your [invoice template](https://dashboard.stripe.com/settings/billing/invoice). If you’re a first-time user, Stripe automatically enables card, [Link](/payments/link), bank transfers, Cash App Pay, and WeChat Pay payment methods. To enable additional payment methods, you need to activate them in your [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods).

In some situations, restrictions might prevent payment methods from being used for an invoice. For instance, a payment method might only operate in one currency, or have limitations on the amount that can be paid. Stripe doesn’t automatically select a payment method when these limitations prevent it from being used. To learn more, read about [supported payment methods](/invoicing/payment-methods#supported).

![Choose additional payment methods](https://b.stripecdn.com/docs-statics-srv/assets/supported-payment-methods.949a2d41b8da98f93ad94c95c986e75c.png)

Choose additional payment methods

[## How to get paid](#get-paid)

You can [create and send](https://dashboard.stripe.com/invoices/create) an invoice from the Dashboard. Invoices provide an itemized list of goods and services rendered, which includes the cost, quantity, and taxes. You can also use them as a tool to collect payment. [Learn more](/invoicing/dashboard).

![Create and send an invoice](https://b.stripecdn.com/docs-statics-srv/assets/create-send-invoices.985a3078348be3c2591f8d5e2d96e21c.png)

Create and send an invoice

[## Set up a custom template Optional](#custom-templates)

You can use the [invoice template](https://dashboard.stripe.com/account/billing/invoice) to customize ​​the content of your invoices. Set a default memo, footer, and numbering scheme. Determine your default payment terms. Because you know more about your customers and your business than Stripe does, make sure your invoices include all of the required information. See the full invoice customization guide at [Customize invoices](/invoicing/customize).

![Configure the Invoice template](https://b.stripecdn.com/docs-statics-srv/assets/invoice-template.d50c4ba2210f06442b6adbb7279fe7a4.png)

Configure the Invoice template

![Manage tax information](https://b.stripecdn.com/docs-statics-srv/assets/manage-tax-information.3bbd3b8425726dc4ac243bb5bfd707a3.png)

Manage tax information

[## Track an invoice](#track-invoice)

Invoices move through different statuses from the time they’re created to when they’re paid. Track the status of an invoice on the [invoices page](https://dashboard.stripe.com/test/invoices) in the Dashboard. To let your customer know that the due date for an invoice is approaching, [send them an email reminder](/invoicing/send-email). Learn more in our [invoice management docs](/invoicing/dashboard/manage-invoices).

![Track and manage your invoices](https://b.stripecdn.com/docs-statics-srv/assets/track-invoices.647ee840cc77e53c4d8537ec43ba9289.png)

Track and manage your invoices

[## Automate Invoice Reconciliation and Collection](#invoicing-plus)

To automate Stripe Invoicing and get paid faster, choose to [automatically charge](/invoicing/automatic-charging) your customer’s payment method on file. You can also let Stripe handle [invoice recovery](/invoicing/automatic-collection) issues.

![Automate invoicing](https://b.stripecdn.com/docs-statics-srv/assets/advanced-invoicing-features.70dfe42ac952e7924876201c06e5902d.png)

Automate invoicing

### Close your books and account for revenue

Using [automatic reconciliation](/invoicing/automatic-reconciliation) means that you don’t need to expose your sensitive bank account details to users or manually reconcile open invoices with your bank. With auto-reconciliation for invoices, Stripe can:

- Match incoming payments with invoice amounts.
- Manage overpayment or underpayment, when the amount paid doesn’t match the invoice.
- Reduce the number of API calls required to transfer funds into Stripe.
- Manage payment retries on open invoices.

![Close your books](https://b.stripecdn.com/docs-statics-srv/assets/invoicing-auto-reconciliation.2d4b2648e4b67e8b2a2c7225a22bec69.png)

Close your books