# Set up automatic user provisioning with SCIMPublic preview

Source: https://docs.stripe.com/get-started/account/sso/scim

---

SCIM user provisioning

[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fsso%2Fscim)

[The Stripe Docs logo](/)

Search

`/`Ask AI

[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fsso%2Fscim)

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

[Consolidate SSO](/get-started/account/orgs/sso-consolidation)

[Troubleshoot SSO](/get-started/account/sso/troubleshooting)

SCIM user provisioning

[Stripe Verified](/verified)

[Quickstarts](/quickstarts)

Start developing

[Build with an LLM](/building-with-llms)

Use Stripe without code

Migrate to Stripe

Common use cases

[Overview](/get-started/use-cases)[Accept simple payments as a startup](/get-started/use-cases/startup)[Sell subscriptions as a SaaS startup](/get-started/use-cases/saas-subscriptions)[Build a subscriptions solution with usage-based pricing](/get-started/use-cases/usage-based-billing)[Accept payments in person](/get-started/use-cases/in-person-payments)[Send invoices to collect payments](/get-started/use-cases/invoices)

United StatesEnglish (United States)

# Set up automatic user provisioning with SCIMPublic preview

## Automatically provision and deprovision team members who are assigned access to Stripe from your Identity Provider (IdP).

Ask about this page

Copy for LLMView as Markdown

By default, when you set up Single Sign-On with SAML, users are provisioned Just-In-Time (JIT) the first time they sign into Stripe from your IdP. With SCIM, you can automatically provision team members in Stripe even before they sign in, and deprovision them on-demand when they should no longer have access to Stripe.

Stripe adheres to the SCIM 2.0 protocol, and only supports the following capabilities in public preview:

### Users:

- Provision a user (not groups) to Stripe (`POST /scim/v2/Users`)
- Retrieve a user from Stripe (`GET /scim/v2/Users/<user_id>`)
- Update a user in Stripe (`PUT /scim/v2/Users/<user_id>` or `PATCH /scim/v2/Users/<user_id>`)
- List all users in Stripe (`GET /scim/v2/Users`)
- Deprovision a user from Stripe (`DELETE /scim/v2/Users/<user_id>`)

## How it works

When you enable SCIM provisioning, Stripe provisions users based on requests to the Stripe SCIM endpoint, using your account’s or organization’s SCIM API key. Existing users continue to have access to Stripe.

While SCIM handles provisioning for team members, their roles are still managed independently through SAML, based on attribute statements passed by your IdP during login. When a user is provisioned through SCIM, they aren’t assigned any permissions until the user signs in.

When your IdP or SCIM client provisions new team members to Stripe, they automatically display in your list of team members under **Settings** > **Team and Security** > [Team](https://dashboard.stripe.com/settings/team). When your IdP or SCIM client deprovisions team members, we immediately revoke their access and remove them from your list of team members. Deprovisioned team members are automatically logged out of the Dashboard and can’t access Stripe. If your accounts belong to an organization, you must configure both SSO and SCIM provisioning from your organization. You can’t configure SSO or SCIM for individual accounts in an organization.

## Before you begin

Before you can enable SCIM provisioning, you must first enable [Single Sign-On](/get-started/account/sso).

## Enable SCIM provisioning

To enable SCIM provisioning in your account or organization:

1. From the Team and security settings page, go to [SCIM provisioning](https://dashboard.stripe.com/settings/security/scim-provisioning) and click **Enable**.
2. Copy your SCIM endpoint URL and SCIM API key to your IdP or SCIM client.

#### Limitations

#### Rate limits

Learn more about how Stripe API uses [rate limits](/rate-limits) to restrict the number of API requests per second.

### Configure in Okta

If you’re configuring SCIM provisioning from Okta as your IdP:

1. Open your Stripe application.
2. Click on the **General** tab. Edit your **App Settings** and click **Enable SCIM provisioning**.
3. Click on the **Provisioning** tab. Under **Settings**, click **Integration** and **Edit**.
4. For **SCIM connector base URL**, enter `https://access.stripe.com/scim/v2`.
5. For **Unique identifier field for users**, add `email` as the value.
6. For **Supported provisioning actions**, select:
   - Push New Users
   - Push Profile Updates
7. For **Authentication Mode**, select `HTTP Header`.
8. For **Authorization**, enter your SCIM API key as the bearer token.
9. Click **Save**.
10. Under the **Settings** > **To App** tab, click **Edit** and enable the following:
    - **Create Users**
    - **Deactivate Users**

### Configure in Entra ID

If you’re configuring SCIM provisioning from Entra ID as your IdP:

1. Open your Stripe application under **Enterprise applications**.
2. Click **Provisioning** > **Connect your application**.
3. For **Tenant URL**, enter **https://access.stripe.com/scim/v2**.
4. For **Secret token**, enter your SCIM API key.
5. Click **Test connection** > **Create**.

#### Provisioning delay

Entra ID has a fixed automatic provisioning interval of 40 minutes.

## Disable SCIM provisioning

To disable SCIM provisioning:

1. From the Team and security settings page, go to [SCIM provisioning](https://dashboard.stripe.com/settings/security/scim-provisioning).
2. Click **Disable**. This automatically deletes your SCIM API key.

## Rotate a SCIM API key

To rotate your SCIM API key:

1. From the **Developers** menu, go to [API keys](https://dashboard.stripe.com/apikeys).
   - If you’re managing an organization, go to [Organizations API keys](https://dashboard.stripe.com/org/api-keys/secret).
2. Next to your SCIM API key, click the overflow menu () and select **Rotate key**.