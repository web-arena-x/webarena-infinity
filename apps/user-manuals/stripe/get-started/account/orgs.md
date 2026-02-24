# Stripe Organizations

Source: https://docs.stripe.com/get-started/account/orgs

---

Organizations

[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Forgs)

[The Stripe Docs logo](/)

Search

`/`Ask AI

[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Forgs)

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

Organizations

[Build an organization](/get-started/account/orgs/build)

[Manage access to your organization](/get-started/account/orgs/team)

[Manage SSO](/get-started/account/orgs/sso)

[Share customers and payment methods](/get-started/account/orgs/sharing/customers-payment-methods)

[Supported setups](/get-started/account/orgs/setup)

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

# Stripe Organizations

## Unify and manage your business across multiple accounts.

Centralize reporting, operations, and team management across your enterprise

Build an organization to maintain separate business entities under consolidated ownership and access.

[Build an organization](/get-started/account/orgs/build)

![](https://b.stripecdn.com/docs-statics-srv/assets/orgs-hero.e513e54ff276a07f9b0e8f6ce427de50.png)

Simplify your operations and account management using Organizations. This feature provides a centralized view in the [Stripe Dashboard](https://dashboard.stripe.com/org/dashboard) of all of your business lines or subsidiaries. You can use it to:

- Gauge your entire business’ performance.
- See all of your [transactions](/dashboard/basics#transactions), [disputes](/disputes/responding), [invoices](/invoicing/dashboard/manage-invoices), [connected accounts](/connect/dashboard/viewing-all-accounts), [customers](/dashboard/basics#customers), and more.
- Download unified reports across currencies.
- Streamline team management and SSO from a centralized location.
- Perform custom SQL queries with [Sigma](/stripe-data/how-sigma-works) across all accounts.

## Use cases

Operating across multiple Stripe accounts is a common practice for many businesses. Consider the following scenarios:

| Scenario | Description |
| --- | --- |
| **Global expansion** | Create separate Stripe accounts for each country or region to take advantage of local acquiring. |
| **Separate business units** | Create separate Stripe accounts for each independent business unit to isolate operations and finances. |
| **Franchise groups** | Centrally manage franchise locations, represented as connected accounts under a platform. |
| **Company acquisitions** | Acquire another business that uses Stripe. |

## Centralize and simplify financial reporting

Use Organizations to assess your finances and growth across accounts.

[![](https://b.stripecdn.com/docs-statics-srv/assets/orgs-overview.01082b131139e7e71115a5ac1c4f0155.png)

Organization overview](/get-started/account/orgs/setup "Organization overview")Learn about different account setups that you can add to an organization.

[![](https://b.stripecdn.com/docs-statics-srv/assets/orgs-reporting.14280f6608a3900bbd394835de06786f.png)

View and download consolidated reports](/reports/multiple-accounts "View and download consolidated reports")View and download consolidated reports across accounts, including balance, activity, and payout reconciliation reports.

[![](https://b.stripecdn.com/docs-statics-srv/assets/orgs-sigma.37b3cc1c61252b938510425d3f0a964d.png)

Query across accounts](/stripe-data/sigma-organizations "Query across accounts")Run custom and templated SQL queries to aggregate data across accounts with Sigma for Organizations.

## Reduce operational overhead

Reduce time spent supporting customers, managing your team, and setting up your business.

[![](https://b.stripecdn.com/docs-statics-srv/assets/orgs-team-management.4395cbdb85da004e26ccc635daecebc2.png)

Centralize team management](/get-started/account/orgs/team "Centralize team management")Manage all your team members in one place, assigning organization roles.

[![](https://b.stripecdn.com/docs-statics-srv/assets/orgs-sso.ec296fe28613f426a0652ba7ab953e2d.png)

Centralize SSO](/get-started/account/orgs/sso "Centralize SSO")Centrally configure SSO across your entire organization while maintaining access to your accounts.

[![](https://b.stripecdn.com/docs-statics-srv/assets/orgs-search.0feb296772c7aeeadda0bed189a30bbd.png)

Search globally](/dashboard/search#org-search "Search globally")Let team members search for information about your business across all of the accounts they have access to.

## Share resources across accounts Public preview

Let accounts build a shared customer base while safeguarding proprietary and sensitive data.

[![](https://b.stripecdn.com/docs-statics-srv/assets/orgs-share-customer-information.35cf3466bbabfe66de5360e287fe681d.png)

Share customer information across accounts](/get-started/account/orgs/sharing/customers-payment-methods "Share customer information across accounts")Track customer information for multiple accounts under a single ID and sync key information across accounts.

[![](https://b.stripecdn.com/docs-statics-srv/assets/orgs-sandbox.59f659b0d40e0202150eb07c14c08ae8.png)

Create a multi-account sandbox](/sandboxes/dashboard/organizations "Create a multi-account sandbox")Test the behavior between shared accounts in a coordinated environment.