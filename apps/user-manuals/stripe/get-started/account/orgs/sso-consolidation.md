# Consolidate your SSO integrations

Source: https://docs.stripe.com/get-started/account/orgs/sso-consolidation

---

Consolidate SSO

[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Forgs%2Fsso-consolidation)

[The Stripe Docs logo](/)

Search

`/`Ask AI

[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Forgs%2Fsso-consolidation)

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

[Branding](/get-started/account/branding)

[Statement descriptors](/get-started/account/statement-descriptors)

[Custom email domain](/get-started/account/email-domain)

[Custom domain](/payments/checkout/custom-domains)

[Single sign-on](/get-started/account/sso)

Setup SSO

Consolidate SSO

[Troubleshoot SSO](/get-started/account/sso/troubleshooting)

[SCIM user provisioning](/get-started/account/sso/scim)

[Stripe Verified](/verified)

[Quickstarts](/quickstarts)

Start developing

[Build with an LLM](/building-with-llms)

Use Stripe without code

Migrate to Stripe

Common use cases

[Overview](/get-started/use-cases)[Accept simple payments as a startup](/get-started/use-cases/startup)[Sell subscriptions as a SaaS startup](/get-started/use-cases/saas-subscriptions)[Build a subscriptions solution with usage-based pricing](/get-started/use-cases/usage-based-billing)[Accept payments in person](/get-started/use-cases/in-person-payments)[Send invoices to collect payments](/get-started/use-cases/invoices)

United StatesEnglish (United States)

# Consolidate your SSO integrations

## Consolidate single sign-on (SSO) settings across multiple accounts.

Ask about this page

Copy for LLMView as Markdown

Use Stripe Organizations to create a centralized organization for managing and operating across multiple Stripe accounts. If you’ve configured single sign-on (SSO) for user authentication, make sure that all your Stripe accounts share the same SSO integration before onboarding into an Organization. Whether you use Organizations or not, we recommend consolidating SSO integrations.

This guide outlines the process of consolidating SSO integrations across multiple accounts. You must consolidate multiple Okta apps (that each authenticate users to a separate Stripe account) to a single Okta app that authenticates users to multiple Stripe accounts. If you’ve already consolidated your SSO integrations, or initially set up Okta as a single integration with multiple accounts, you don’t need to take any additional steps.

This consolidation doesn’t require any changes to your group assignments or downtime for users that log into Stripe.

#### Configure one Organization per identity provider application

When you set up SSO for multiple Organizations, don’t reuse the same identity provider application for each one. Instead, configure one identity provider application for each Organization.

## Example SSO setup prior to consolidation

Follow this guide to learn how to consolidate [SSO settings](https://dashboard.stripe.com/org/settings/security/user_authentication) for multiple Stripe accounts that belong to a fictitious company called Acme Inc. Acme Inc has four Stripe accounts, each with a separate Okta app and SSO integration:

- Acme Financial
- Acme Travel
- Acme Insurance
- Acme Consulting

In Okta, Acme set up a separate group for each role users require in each Stripe account. For example:

![](https://b.stripecdn.com/docs-statics-srv/assets/consolidation_1.4807fe1fd5aa6076345f14684bbfec35.png)

In the **Profile Editor** for each app, Acme created a mapping for the roles in each Stripe account:

![](https://b.stripecdn.com/docs-statics-srv/assets/consolidation_2.b77058f777752b3d4311a57259e588d5.png)

![](https://b.stripecdn.com/docs-statics-srv/assets/consolidation_3.11913135275d1b024da286ebce99892c.png)

Next, Acme created a separate Okta app for each Stripe account.

![](https://b.stripecdn.com/docs-statics-srv/assets/consolidation_4.8a1503c0f8134150062d31fe13ab67ac.png)

Each account contains one **Attribute Statement**, which defines the roles users have for that one Stripe account.

![](https://b.stripecdn.com/docs-statics-srv/assets/consolidation_5.cce233b18ee635a70bba13c88fb477f4.png)

To onboard your accounts to Organizations, you can’t have separate Okta apps and SSO integrations for each Stripe account. You must consolidate these Okta apps into one Okta app for all accounts and preserve granular role assignments so that users can access specific accounts in Stripe.

[## Designate a primary Okta App](#designate-okta-app)

Choose one of your existing Okta apps to be the new primary Okta app.

![](https://b.stripecdn.com/docs-statics-srv/assets/consolidation_6_step_1.caa2ffd1108c25d2830f433614bd9220.png)

[## Add a new profile mapping of roles for each Stripe account](#add-profile-mapping)

Create a new attribute mapping for each of your Stripe accounts. This allows you to choose which Stripe account users have access to when assigning each group to the app.

![](https://b.stripecdn.com/docs-statics-srv/assets/consolidation_7_step_2.90c817e66e9f7685ff24cf483ca0cfca.png)

In each profile mapping, you can configure which roles are allowed to be assigned. View the full list of roles and values in the [user roles](/get-started/account/teams/roles) page.

![](https://b.stripecdn.com/docs-statics-srv/assets/consolidation_8_step_2a.97e9f86e50f551ce8cff806cd394c6fb.png)

[## Assign a role in the new primary app](#assign-role)

For each of your groups in Okta, assign the group to the primary app, then choose roles and accounts that users in the group have access to.

![](https://b.stripecdn.com/docs-statics-srv/assets/consolidation_9_step_3.6b1eac7b697622131b60cee107c32fb5.png)

![](https://b.stripecdn.com/docs-statics-srv/assets/consolidation_10_step_3a.feb9eb9d8246add074b413e7f44aad4f.png)

[## Add an attribute statement for users’ roles in each Stripe account](#add-attribute)

In the SAML settings of your primary Okta app, name each attribute statement either `Stripe-Role-acct_id` or `Stripe-Role-org_id`. Set the value as the profile mapping that contains users’ roles for that Stripe account or organization.

![](https://b.stripecdn.com/docs-statics-srv/assets/consolidation_11_step_4.4f91427615b58334ccda52efa1b558a5.png)

[## Configure SSO for all of your Stripe accounts to redirect users during authentication](#configure-sso)

Next, we need to make sure that the SSO settings in Stripe for each of your accounts directs to the same primary Okta app. To do this, you can update your SSO settings for each account.

To locate the three pieces of metadata associated with your primary app, which are required by Stripe in Okta, go to the **Sign On** tab of your primary app in Okta. In the bottom right corner of the page, click **View SAML Setup Instructions**, then copy the metadata.

![](https://b.stripecdn.com/docs-statics-srv/assets/consolidation_12_step_5.59a88c49f5f6fabbb621940d92dd3dec.png)

![](https://b.stripecdn.com/docs-statics-srv/assets/consolidation_13_step_5a.053718fdc281776ab21caaa003eb4d8c.png)

To access your SSO settings in each Stripe account, click **Settings > Team and security > User authentication**. Open the menu associated with the domain and click **Manage SSO settings**. Paste the metadata from your primary app in Okta.

![](https://b.stripecdn.com/docs-statics-srv/assets/consolidation_14_step_5b.55bdaf38c0633a132039a5ac16137b09.png)

After you paste the metadata and confirm the changes, users can sign into Stripe by clicking your primary app in Okta. Use the account picker to switch accounts in Stripe.

[## OptionalSet up bookmarks in Okta to directs users to each Stripe account](#bookmarks)