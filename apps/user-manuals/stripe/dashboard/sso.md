# Single sign-on (SSO)

Source: https://docs.stripe.com/dashboard/sso

---

Single sign-on

[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fsso)

[The Stripe Docs logo](/)

Search

`/`Ask AI

[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fsso)

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

Single sign-on

Setup SSO

[Consolidate SSO](/get-started/account/orgs/sso-consolidation)

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

# Single sign-on (SSO)

## Configure authentication for access to the Stripe Dashboard with an Identity Provider.

Ask about this page

Copy for LLMView as Markdown

Single Sign-On (SSO) allows your team to sign in through an Identity Provider (IdP) using one set of credentials and access multiple applications, such as Stripe. Enabling SSO for your team increases security and makes it easier for them to sign in to Stripe. Stripe specifically supports Security Assertion Markup Language (SAML) 2.0, so your IdP can manage the creation of user accounts (team members) as well as authentication and authorization during sign-in. Any identity provider that supports SAML 2.0 works with Stripe.

#### Security incidents

If your Identity Provider (IdP) is compromised, unauthorized parties could access your Stripe account. You’re responsible for mitigating your exposure to security incidents by evaluating your security needs and implementing the necessary security protocols and controls.

## Setup SSO with an Identity Provider

[Auth0

Learn how to setup single sign-on in the Dashboard with Auth0.](/get-started/account/sso/v2/auth0 "Auth0")

[Entra ID

Learn how to setup single sign-on in the Dashboard with Entra ID (formerly known as Azure AD).](/get-started/account/sso/entra-id "Entra ID")

[Google Workspace

Learn how to setup single sign-on in the Dashboard with Google Workspace.](/get-started/account/sso/google-workspace "Google Workspace")

[Okta

Learn how to setup single sign-on in the Dashboard with Okta.](/get-started/account/sso/okta "Okta")

[OneLogin

Learn how to setup single sign-on in the Dashboard with OneLogin.](/get-started/account/sso/onelogin "OneLogin")

[Other

Learn how to setup single sign-on in the Dashboard with a different identity provider.](/get-started/account/sso/other "Other")

## Additional resources

[Consolidate SSO

Learn how to consolidate single sign-on (SSO) settings across multiple accounts.](/get-started/account/orgs/sso-consolidation "Consolidate SSO")

[Troubleshoot SSO

Learn how to resolve failed configuration checks when setting up SSO.](/get-started/account/sso/troubleshooting "Troubleshoot SSO")

## Supported features

Stripe supports the following SSO features:

- **SSO configuration options**: Configure Stripe accounts to either mandate SSO for all users or allow sign-in using SSO or email and password.
- **Just-In-Time account creation**: Automatically create new Stripe accounts for users without existing access upon their first SSO sign-in.
- **Granular Dashboard roles**: Assign granular [user roles](/get-started/account/teams/roles) through your IdP.
- **IdP-initiated SSO**: Authenticate directly from an IdP’s website or browser extension.
- **Service Provider-initiated SSO**: Initiate SSO login directly from Stripe’s [login page](https://dashboard.stripe.com/login).
- **System for Cross-domain Identity Management (SCIM)**: [SCIM](/get-started/account/sso/scim) is a protocol that an IdP can use to synchronize user identity lifecycle processes (for example, provisioning and deprovisioning access, and populating user details) with the service provider, such as Stripe.

### Limitations

Stripe doesn’t support the following SSO features:

- **User Deletion in SAML**: When users aren’t managed through SCIM, Stripe doesn’t receive immediate notifications if user access is revoked in IdP. If users attempt to log in through SSO after their session expires, Stripe revokes their access. To remove access immediately, you can delete users from your [Team settings](https://dashboard.stripe.com/settings/team) or enable SCIM user provisioning.