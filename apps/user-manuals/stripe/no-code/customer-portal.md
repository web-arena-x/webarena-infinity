# Set up the customer portal

Source: https://docs.stripe.com/no-code/customer-portal

---

Set up customer portal

[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fno-code%2Fcustomer-portal)

[The Stripe Docs logo](/)

Search

`/`Ask AI

[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fno-code%2Fcustomer-portal)

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

[Send invoices](/no-code/invoices)

[Create subscriptions](/no-code/subscriptions)

[Send quotes](/no-code/quotes)

[Accept in-person payments](/no-code/in-person)

[Pay out money](/no-code/payout)

Set up customer portal

[Dashboard assistant](/assistant)

Migrate to Stripe

Common use cases

[Overview](/get-started/use-cases)[Accept simple payments as a startup](/get-started/use-cases/startup)[Sell subscriptions as a SaaS startup](/get-started/use-cases/saas-subscriptions)[Build a subscriptions solution with usage-based pricing](/get-started/use-cases/usage-based-billing)[Accept payments in person](/get-started/use-cases/in-person-payments)[Send invoices to collect payments](/get-started/use-cases/invoices)

United StatesEnglish (United States)

# Set up the customer portal

## Let your customers manage their own billing accounts with a portal that Stripe hosts.

Ask about this page

Copy for LLMView as Markdown

- **Stripe compatibility:** Payment Links, Checkout, pricing table, customer portal
- **Requires:** Stripe account
- **Good for:** SaaS businesses, individual creators, e-commerce businesses
- **Pricing:** [Stripe Billing pricing](https://stripe.com/billing/pricing) for recurring payments, [Invoicing pricing](https://stripe.com/invoicing/pricing) for invoice-only setup

When you’re ready to offer your customers a way to self-serve their billing accounts, you can set up the customer portal. Use it to let your customers manage their billing information, subscriptions, and invoices as your business scales.

Stripe hosts the customer portal, which means you can use it even if you don’t have a website. You can also link users to it from an existing site or Stripe integration.

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register/).

[## Create a product](#create-product)

To create a product in the Dashboard:

1. Go to **More** > **Product catalog**.
2. Click **+Add product**.
3. Enter the **Name** of your product.
4. (Optional) Add a **Description**. The description appears at checkout, on the [customer portal](/customer-management), and in [quotes](/quotes).
5. (Optional) Add an **Image** of your product. Use a JPEG, PNG, or WEBP file that’s smaller than 2MB. The image appears at checkout.
6. (Optional) If you’re using [Stripe Tax](/tax), select a **Tax code** for your product. See [tax codes](/tax/tax-codes) for more information about the appropriate category for your product.
7. (Optional) Enter a **Statement descriptor**. This descriptor overrides any account descriptors for recurring payments. Choose something that your customers would recognize on a bank statement.
8. (Optional) Enter a **Unit label**. This describes how you sell your product. For example, if you charge by the seat, enter “seat” so the line item includes “per seat” for the price. Unit labels appear at checkout, and in invoices, receipts, and the [customer portal](/billing/subscriptions/customer-portal).

[## Set up the customer portal](#set-up-customer-portal)

1. **Activate a customer portal link**

   On the [customer portal configuration](https://dashboard.stripe.com/settings/billing/portal) page, click **Activate link** in the **Ways to get started** section.
2. **Configure the portal**

   Go to the [customer portal configuration](https://dashboard.stripe.com/settings/billing/portal) page and select your configuration options. Learn more about [configuration options](/customer-management/configure-portal).
3. **Share the portal login link**

   Add the link you activated to your site, or send it directly to your customers. They can log in to the portal with their email address and a one-time passcode.

   Make sure your customers have an [email](/api/customers/object#customer_object-email) set. If multiple customers have the same email address, Stripe selects the most recently created customer that has both that email and an active subscription.

   For security purposes:

   - Customers can’t update their email address through this link.
   - If a customer doesn’t receive a one-time passcode after clicking the login link, make sure their email address matches the email address of an existing customer. To check, enter the email address in the search bar of the [Dashboard](https://dashboard.stripe.com/).

[## OptionalCustomize branding](#branding)

[## OptionalPrefill customer email](#url-parameters)