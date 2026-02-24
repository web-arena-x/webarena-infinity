# Build an organization

Source: https://docs.stripe.com/get-started/account/orgs/build

---

Build an organization

[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Forgs%2Fbuild)

[The Stripe Docs logo](/)

Search

`/`Ask AI

[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Forgs%2Fbuild)

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

Build an organization

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

# Build an organization

## Select accounts to combine into an organization.

Ask about this page

Copy for LLMView as Markdown

Create an organization, managing your accounts from a single location in the Stripe Dashboard. After you create an organization, you can invite additional team members to [access your organization](/get-started/account/orgs/team) by navigating to your [Team and security](https://dashboard.stripe.com/org/settings/team) settings.

## Before you begin

- The person who creates the organization must be a [Super Administrator](/get-started/account/teams/roles) in each account added to the organization. Stripe automatically assigns this role to the account owner, who can assign the Super Administrator role to the organization creator, if it’s a different person. If an account’s owner leaves, you can [request an ownership transfer](https://support.stripe.com/questions/change-the-owner-of-a-stripe-account).
- You must [Consolidate the IdPs](/get-started/account/orgs/sso) of any accounts with SSO enabled before you add them to the organization.

## Create an organization

To create an organization from one of your Stripe accounts:

1. Navigate to your [Account details](https://dashboard.stripe.com/settings/account) in the Dashboard.
2. Click **Create organization**.
3. Enter a name for your organization.
4. Select the accounts you want to add to the organization. You can add up to 75 accounts.
5. Agree to the [Terms of Service](https://stripe.com/legal/organizations).
6. Click **Create**.

## Manage SSO behavior

After you create an organization, [SSO](/get-started/account/sso) configuration for all accounts transfers to the organization. You must update your identity provider (IdP) to assign roles through the organization and consolidate account SSO management under the organization’s IdP.

1. Obtain your `org_id` from your [organization management settings](https://dashboard.stripe.com/org/settings/org) in the Dashboard.
2. Add or update your IdP attribute statement to use `Stripe-Role-org_id` (instead of `Stripe-Role-acct_id`) so you can assign roles in the organization.

#### Common mistake

Failure to update your SSO integration can result in restricted user access.

## Add an existing account to an organization

After you create an organization, you can add an existing account. An organization can include up to 75 accounts, and each account can belong to only one organization.

1. Click **Add account** next to **Business accounts** on the [homepage](https://dashboard.stripe.com/org/dashboard).
2. Select **Choose from existing accounts**.
3. Select the accounts you want to add. If you’re a Super Administrator of an account, you can add the account to your organization directly. If you’re an Administrator of an account, you can send an invite to the Super Administrator. If you’re not sure who the Super Administrator is, check the account’s [Team settings](https://dashboard.stripe.com/settings/team). The person who created an account is automatically made a Super Administrator. India Stripe Accounts aren’t eligible at this time.
4. Click **Add**.

## Add a new account to an organization

To add a new account to an organization:

1. Click the account picker, then select **Create new account**.
2. Select **Create a new account in your organization**.
3. Add the account name, then select the country of operation.
4. (Optional) Select a legal entity, business details, or payout bank account information you want to copy from existing accounts within your organization.
5. Click **Create account**.

## Add a new account outside of an organization

To add a new account outside of an organization:

1. Click the account picker, then select **Create new account**.
2. Select **Create an account outside of your organization**.
3. Add the account name, then select the country of operation.
4. Click **Create**.

## Remove an account from an organization

To remove an account from an organization:

1. Click the account picker, and select your organization.
2. Go to [Organization management](https://dashboard.stripe.com/org/settings/org), and click the overflow menu () next to the name of the account you want to remove.
3. Click **Remove from organization**.
4. Make sure you assign account-level roles to any users who inherited them from the organization if you want them to continue having those permissions in the removed account.

You must be a [Super Administrator](/get-started/account/teams/roles) of the organization to remove an account. If you remove every account from an organization, Stripe permanently closes it.

#### Data pipeline effects

If you remove an account from an organization, we automatically remove the account from all [data pipelines](/stripe-data/access-data-in-warehouse) in the organization.