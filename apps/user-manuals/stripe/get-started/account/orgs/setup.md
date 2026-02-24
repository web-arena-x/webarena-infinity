# Supported Organization setups

Source: https://docs.stripe.com/get-started/account/orgs/setup

---

Supported setups

[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Forgs%2Fsetup)

[The Stripe Docs logo](/)

Search

`/`Ask AI

[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Forgs%2Fsetup)

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

[Build an organization](/get-started/account/orgs/build)

[Manage access to your organization](/get-started/account/orgs/team)

[Manage SSO](/get-started/account/orgs/sso)

[Share customers and payment methods](/get-started/account/orgs/sharing/customers-payment-methods)

Supported setups

[Multiple separate accounts](/get-started/account/multiple-accounts)

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

# Supported Organization setups

## Learn about different business use cases that benefit from organization structuring.

Ask about this page

Copy for LLMView as Markdown

Organizations support the following account setups: multiple standalone accounts, platforms, and connected accounts.

## Organizations versus Connect platforms

Organizations and [Connect](/connect/how-connect-works) platforms both allow a Stripe user to manage multiple related accounts. However, they each serve distinct purposes.

- **Ownership**: A Connect platform extends its Stripe integration to third parties, while an organization centralizes the management of multiple accounts under common ownership.
- **Operation**: A Connect platform is itself an account—it processes payments and has balances, customers, subscriptions, and more. An organization doesn’t conduct its own business through Stripe. It acts as a container structure to view and manage the operation of its separate businesses.
- **Structure**: A Connect platform can belong to an organization. For example, Rocket, Inc. might have separate Connect platforms operating in different global regions, all of which are accounts within the Rocket organization, as shown in the [Connect example setup](#connect-platforms).

## Multiple standalone accounts

It’s common to manage multiple Stripe accounts that represent different business lines, countries of operation, legal entities, and acquisitions.

After you [add these accounts to an organization](/get-started/account/orgs/build), you can search and download consolidated reports across your accounts without any changes to your Stripe integration. After you create an organization, you can add new business lines or add existing accounts.

## Multiple platform accounts

If you have several Connect platforms that correspond to different countries of operation or business lines, you can add them to an organization.

After you add your platforms to an organization, you can search for connected accounts and data within a specific platform or across all your platforms.

## Multiple connected accounts under a Connect platform

In certain cases, you might own multiple connected accounts connected to the same platform. This commonly occurs in franchise groups where several franchises are under common ownership.

You can add your connected accounts to an organization, independent of their platform. This allows you to use the unified search and reporting across your accounts.

## Multiple business lines represented as connected accounts

In some cases, you might represent multiple business lines as a platform with connected accounts, even though your business isn’t a traditional platform or marketplace. This is common if you want to consolidate payment integrations or clone payment methods stored in the platform to connected accounts.

By creating an organization that encompasses the platform and connected accounts, you can use unified search and reporting across all the accounts without impacting your payment integrations.