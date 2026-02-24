# Branding your Stripe account

Source: https://docs.stripe.com/get-started/account/branding

---

Branding

[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fbranding)

[The Stripe Docs logo](/)

Search

`/`Ask AI

[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fbranding)

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

[Overview](/get-started/account)

[Activate your account](/get-started/account/activate)

[Add funds to your balance](/get-started/account/add-funds)

[Account checklist](/get-started/account/checklist)

[Acceptable verification documents](/acceptable-verification-documents)

Account structure

[Start a team](/get-started/account/teams)

[Organizations](/get-started/account/orgs)

[Multiple separate accounts](/get-started/account/multiple-accounts)

[Linked external accounts](/get-started/account/linked-external-accounts)

Settings

[Profile](/get-started/account/profile)

Branding

[Statement descriptors](/get-started/account/statement-descriptors)

[Custom email domain](/get-started/account/email-domain)

[Custom domain](/payments/checkout/custom-domains)

[Single sign-on](/get-started/account/sso)

[Stripe Verified](/verified)

[Quickstarts](/quickstarts)

Start developing

[Build with an LLM](/building-with-llms)

Use Stripe without code

Migrate to Stripe

Common use cases

[Overview](/get-started/use-cases)[Accept simple payments as a startup](/get-started/use-cases/startup)[Sell subscriptions as a SaaS startup](/get-started/use-cases/saas-subscriptions)[Build a subscriptions solution with usage-based pricing](/get-started/use-cases/usage-based-billing)[Accept payments in person](/get-started/use-cases/in-person-payments)[Send invoices to collect payments](/get-started/use-cases/invoices)

United StatesEnglish (United States)

# Branding your Stripe account

## Customize the appearance of your Stripe account and customer-facing elements.

Ask about this page

Copy for LLMView as Markdown

Customize the appearance of your emails, checkout, payment links, customer portal, and invoices in your [Branding settings](https://dashboard.stripe.com/account/branding).

Loading video content...

## Branding

Icons and logos must be in JPG or PNG format, less than 512kb in size, and equal to or greater than 128px by 128px.

- **Icon**—A square, digital-friendly icon or logo.
- **Logo**—A non-square logo to override some uses of the icon.
- **Brand color**—Used on receipts, invoices, and the customer portal.
- **Accent color**—Used as a background on emails and pages.

### Apply brand settings

Brand settings apply to your whole account and take effect in many places.

| Setting | Emails | Checkout & Payment Links | Customer portal | Hosted Invoice Page | Invoice PDFs |
| --- | --- | --- | --- | --- | --- |
| **Icon** | Yes | Yes | Yes | Yes | Yes |
| **Logo** | No | Yes | No | No | Yes |
| **Brand color** | Yes | No | Yes | Yes | Yes |
| **Accent color** | Yes (background color) | Yes | Yes | Yes | No |

### Branding with Connect

If you maintain a platform with Connect, the customer portal uses the brand settings of the connected account under these circumstances:

- The platform uses direct charges
- The platform uses destination charges with `on_behalf_of`

For all other connected accounts, you can configure the brand settings with the [Accounts](/api/v2/core/accounts/create#v2_create_accounts-configuration-merchant-branding) API.

## Customize policies and contact information

You can display your return, refund, and legal policies, and your support contact information to your customers on Checkout. Go to [Checkout Settings](https://dashboard.stripe.com/settings/checkout) to configure the information you want to display, including:

- Details about your return and refund policies
- Your support phone number, email, and website
- Links to your terms of service and privacy policy

Presenting this information can increase buyer confidence and minimize cart abandonment.

### Configure support and legal policies

From [Checkout Settings](https://dashboard.stripe.com/settings/checkout), add support contact information to your sessions by enabling **Contact information**. Similarly, add links to your **Terms of service** and **Privacy policy** to your sessions by enabling **Legal policies**. If you require customers to implicitly consent to your legal policies when they complete their checkout, select the **Display agreement to legal terms** checkbox.

You must add your support contact information and legal policy links in your [Public Detail Settings](https://dashboard.stripe.com/settings/public).

The following previews show how Checkout displays a dialog with the support contact information, links to the store legal policies, and information about the payment terms.

![A checkout page with contact information.](https://b.stripecdn.com/docs-statics-srv/assets/contact-modal.2b81bc2e74657f7c94a45a743439c81f.png)

Preview of contact information on Checkout.

![A checkout page with legal policies.](https://b.stripecdn.com/docs-statics-srv/assets/legal-modal.9351cb51408c2a9f5c0ae23aab03e138.png)

Preview of legal policies on Checkout.

### Configure return and refund policies

Display your return, refund, or exchange policies, by enabling **Return and Refund policies**. Although businesses that sell physical goods use return policies, businesses that sell digital goods or customized physical goods typically use refund policies. Because they’re not mutually exclusive, you can select both options if your business sells both categories of goods. You can edit your return and refund details, including:

- Whether you accept returns, refunds, or exchanges
- Whether returns, refunds, or exchanges are free or if they’re subject to a fee
- How many days after a purchase you’ll accept returns, refunds, or exchanges
- How customers can return items shipped to them
- Whether you accept in-store returns
- A link to the full return and refund policy
- A custom message

If you accept free returns, refunds, or exchanges, Checkout highlights the policy for customers.

The following previews show how Checkout displays a return policy. In this example, it’s for purchases that can be returned by shipping them or in-store for a full refund (or exchange) for up to 60 days. You can display similar information for refunds.

![Preview of return policies on Checkout](https://b.stripecdn.com/docs-statics-srv/assets/return-policy-modal.0c7a9ff71b8bc2c155842532801e06a8.png)

Preview of return policies on Checkout.

![Preview of a policy highlight on Checkout](https://b.stripecdn.com/docs-statics-srv/assets/policy-highlight.334828420693a33d376977a2c0fe5851.png)

Preview of a policy highlight on Checkout.

## Other customization options

- **Custom domains**

 Checkout, Payment Links, and customer portal pages use stripe.com as the default domain. You can optionally set up your own [custom domain](/payments/checkout/custom-domains) for those products.
- **Custom email domain**

 By default, when Stripe sends invoices, receipts, and failed payment notifications to your customers, it sends them from the stripe.com domain. Set up your own [custom domain](/get-started/account/email-domain) to change this.
- **Payments, debits, and bank transfer emails**

 You can decide which emails your customers receive about payments, debits, and bank transfers in your [Customer emails settings](https://dashboard.stripe.com/settings/emails). You can also choose the default language to use for emails when you don’t know a customer’s preference.
- **Billing (subscription and invoicing) emails**

 You can turn on customer emails for [Billing](/billing/revenue-recovery/customer-emails) and [Invoicing](/invoicing/send-email) in the Dashboard or through the API.