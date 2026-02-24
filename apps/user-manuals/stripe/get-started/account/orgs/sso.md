# Organization-level SSO

Source: https://docs.stripe.com/get-started/account/orgs/sso

---

Manage SSO

[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Forgs%2Fsso)

[The Stripe Docs logo](/)

Search

`/`Ask AI

[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Forgs%2Fsso)

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

Manage SSO

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

# Organization-level SSO

## Manage single sign-on (SSO) for all accounts within your organization.

Ask about this page

Copy for LLMView as Markdown

If your business operates across multiple Stripe accounts and uses single sign-on (SSO) to authenticate users, you can centrally configure SSO with Stripe Organizations. You can add accounts that already have SSO configured to an organization, or configure SSO for all your accounts after you create an organization.

To set up SSO on Stripe for the first time, see [Single sign-on](/get-started/account/sso).

## Add accounts that you configured with SSO to an organization

If you have multiple accounts with SSO configured, you can’t preserve their individual SSO settings in your organization. You must [consolidate multiple authentication apps](/get-started/account/orgs/sso-consolidation) into a single authentication app for multiple accounts.

When you create your organization, Stripe consolidates the SSO settings of your accounts under your organization’s [single sign-on](https://dashboard.stripe.com/org/settings/security/sso) settings. This action updates the SSO settings in each individual account to read-only. You can still log into individual accounts, but you must edit settings such as verified domains and enforcement exclusively from the organization.

After setting up your organization with SSO, you can add accounts that share the organization’s SSO configuration. If your organization is set up with SSO set to **Optional**, you can also add accounts that don’t use SSO. You can’t add accounts that have separate SSO authentication.

## Configure SSO throughout an organization

Instead of setting up SSO separately in each account, you can centrally configure SSO throughout all accounts in your organization. Any organization-level verified domains or SSO configurations apply to all accounts within the organization.

### SSO settings for each domain

You can configure separate SSO settings for each verified domain or reuse the same SSO settings for multiple domains. For example, within the same organization, you can require SSO for one domain, set SSO to **Optional** for another, or disable it entirely to enable email and password logins.

### Multiple Identity Providers

Stripe allows you to have multiple IdPs when each verified domain has only one IdP. For example, you can configure users with a `rocketrides.com` email address to authenticate with Okta and configure users with a `rocketdelivery.com` email address to authenticate with AzureAD.

## Assign account-level and organization-level roles

Organization-level SSO operates similarly to SSO in a single account. When Stripe receives a SAML assertion from an IdP, we examine the accounts and roles specified within that SAML assertion. Based on this information, Stripe assigns roles to the user. You can assign a single account-level role, a single organization-level role, or a combination of both account-level and organization-level roles.

When you assign these roles, use the `Stripe-Role-{accountID}` or `Stripe-Role-{org-id}` prefixes for the account and organization IDs respectively. We assign claims that include an account ID at the account-level, and claims that include organization IDs at the organization-level. Learn more about [account-level and organization-level roles](/get-started/account/orgs/team).

The snippet of the SAML assertion below has three claims being made for the user:

1. In `acct_ONE` the user is being assigned the `developer` role
2. In `acct_TWO` the user is being assigned the `developer` role
3. In `org_ALPHA` the user is being assigned the `view-only` role

As a result of these assertions, Stripe grants this user a session with the `developer` role in the `acct_ONE` and `acct_TWO` accounts. Additionally, we assign the `view-only` role in the `org-ALPHA` Organization and all accounts within that Organization:

```
<saml2:Attribute Name="Stripe-Role-acct_ONE" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified">
        <saml2:AttributeValue xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">developer</saml2:AttributeValue>
      </saml2:Attribute>
      <saml2:Attribute Name="Stripe-Role-acct_TWO" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified">
        <saml2:AttributeValue xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">developer</saml2:AttributeValue>
      <saml2:Attribute Name="Stripe-Role-org_ALPHA" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified">
        <saml2:AttributeValue xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">view_only</saml2:AttributeValue>
```