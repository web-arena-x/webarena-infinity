# Multiple separate accounts

Source: https://docs.stripe.com/get-started/account/multiple-accounts

---

Multiple separate accounts

[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fmultiple-accounts)

[The Stripe Docs logo](/)

Search

`/`Ask AI

[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fmultiple-accounts)

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

Multiple separate accounts

[Linked external accounts](/get-started/account/linked-external-accounts)

Settings

[Profile](/get-started/account/profile)

[Branding](/get-started/account/branding)

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

# Multiple separate accounts

## Learn how to create and manage multiple separate Stripe accounts.

Ask about this page

Copy for LLMView as Markdown

You must use separate Stripe accounts for projects, websites, or businesses that operate independently from one another. When you activate a new account, it’s subject to Stripe’s standard policies and pricing—it doesn’t inherit any special status or other similar considerations that might apply to your existing account.

#### Note

If you operate multiple accounts related to the same business, such as for local acquiring or maintaining separate business lines, you can create an [organization](/get-started/account/orgs) for centralized reporting and management.

You can create additional Stripe accounts associated with your email address. You might create some accounts yourself, or you might be given access to other accounts as a [team member](/get-started/account/teams). To create a new account, click on the name of your current Stripe account in the upper-left corner, and select **New account**. To switch the account you’re currently viewing in the [Dashboard](https://dashboard.stripe.com/), click on the name of your current Stripe account in the upper-left corner and then select the account to switch to.

Using additional accounts has a number of benefits:

- **Separate tax and legal entity information**: You can only associate each account with the tax ID and legal entity of one business. If you operate multiple businesses that have separate tax ID information (for example, separate legal entities), you must create additional accounts for each.
- **Unique statement descriptor and public business information**: Using the same Stripe account for separate businesses can cause confusion as the [public business information](/get-started/account/activate#public-business-information) used is the same for both. For example, a customer who purchases from your business “XYZ” might see a charge from your business “ABC” on their statement, potentially resulting in a dispute. Each additional account has its own public information to accurately describe your business and payments.
- **Reporting and reconciliation**: Separating the payments processed by your businesses helps you find payments, create and export [reports](/stripe-reports), and reconcile payouts to your bank account.
- **Payouts to separate bank accounts**: Each additional account can use a separate bank account for [payouts](/payouts) (although you can use the same bank account if you want).

When you have multiple projects or businesses that operate under the same legal entity, you can use the same tax ID and business information across multiple accounts. Make sure to provide suitable [public business information](/get-started/account/activate#public-business-information) to avoid customer confusion.

## See also

- [Start a team](/get-started/account/teams)
- [User roles](/get-started/account/teams/roles)