# Single sign-on with Auth0

Source: https://docs.stripe.com/get-started/account/sso/v2/auth0

---

Auth0

[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fsso%2Fv2%2Fauth0)

[The Stripe Docs logo](/)

Search

`/`Ask AI

[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fsso%2Fv2%2Fauth0)

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

Auth0

[Entra ID](/get-started/account/sso/entra-id)

[Google Workspace](/get-started/account/sso/google-workspace)

[Okta](/get-started/account/sso/okta)

[OneLogin](/get-started/account/sso/onelogin)

[Other](/get-started/account/sso/other)

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

# Single sign-on with Auth0

## Learn how to setup single sign-on in the Dashboard with Auth0.

Ask about this page

Copy for LLMView as Markdown

Stripe supports Single Sign-On (SSO), allowing you to manage your team’s access and roles through your identity provider (IdP). This means your team can access Stripe without needing separate passwords. When SSO is configured, users (team members) are automatically redirected to your IdP for authentication when they sign in to Stripe.

Your IdP verifies if they have a valid role assignment to your Stripe accounts or [organization](/get-started/account/orgs/sso), and generates a SAML assertion used by Stripe to assign the proper roles in the Stripe Dashboard. When your account requires SSO, you must update team roles through your Identity Provider (IdP) for security. Changes to a team member’s roles only appear in Stripe after they sign in to the Dashboard again using the updated SAML assertion.

## Set up SSO

To integrate your Stripe account with your IdP, complete these steps:

1. [Prove ownership of the domains](#proving-domain-verification) that your team uses to sign in to the Dashboard.
2. [Configure Auth0](#configuring-your-identity-provider) to work with Stripe.
3. [Configure Stripe](#configure-stripe) to work with Auth0.

[## Proving Domain Ownership](#proving-domain-verification)

A domain is the portion of an email address after the `@` symbol (such as `kavholm.com`). You must configure SSO for Stripe for each of your business’s email domains. To verify domain ownership:

1. Go to [Single sign-on (SSO)](https://dashboard.stripe.com/settings/security/sso) in the Stripe Dashboard, and click **+ New domain** to view your account’s unique verification code.

   ```
   stripe-verification=4242424242424242424242
   ```
2. Add the verification code as a `TXT` record to your Domain Name System (DNS) provider.
3. Return to the Stripe Dashboard, and click **Save and verify**. Depending on your DNS provider, it can take 24 hours or more to verify your domain.
4. After successful verification, don’t delete the `TXT` record from your DNS provider. If you delete it, you might lose access to the Dashboard because Stripe frequently checks the DNS records of your domain.

#### Multiple Stripe accounts support

If you’re configuring SSO for multiple Stripe accounts, we recommend creating an [organization](/get-started/account/orgs) to centrally configure SSO across all of your accounts.

[## Configuring Auth0](#configuring-your-identity-provider)

Follow these steps to create an application.

1. Create a new application to represent the relationship between Auth0 and the Stripe Dashboard. To do this, go to your Auth0 dashboard and click **Create Application**.

![Auth0 dashboard](https://b.stripecdn.com/docs-statics-srv/assets/auth0_create_application.7b6f15263843de76df131e481f7955a5.png)

1. Set the **Name** field and then select **Regular Web Applications**. Select **Create** to make your Auth0 application for Stripe authentication.

![creating an application on Auth0](https://b.stripecdn.com/docs-statics-srv/assets/auth0_new_application.6ec3142f2df9f391b7f442ced92630d0.png)

1. Go to the **Addons** tab and select **SAML2 web app**.

![activating SAML on an Auth0 application](https://b.stripecdn.com/docs-statics-srv/assets/auth0_navigate_to_addons.d7d7fa5fb2e17fc0b0399eeab8321ff8.png)

- In the window that opens, set `https://dashboard.stripe.com/login/saml/consume` as the **Application Callback URL**.
- Replace the contents of the **Settings** box with the following JSON information and then select **Enable**.

```
{
 "audience": "https://dashboard.stripe.com/saml/metadata",
 "recipient": "https://dashboard.stripe.com/login/saml/consume",
 "mappings": {
    "email": "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier"
 },
 "signatureAlgorithm": "rsa-sha256",
 "digestAlgorithm": "sha256",
 "destination": "https://dashboard.stripe.com/login/saml/consume",
 "signResponse": false,
 "nameIdentifierFormat": "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress",
 "nameIdentifierProbes": [
    "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress"
 ]
}
```

### Assign roles to your team

The following setup is an example of how to set up dynamic roles. As long as the SAML Response contains the appropriate fields, Stripe grants the corresponding roles in the Stripe Dashboard. See Auth0’s documentation for more information on dynamic roles.

1. In the **Auth Pipeline section**, go to the **Rules** section, and then select **Create Rule**.

![rules on the Auth0 dashboard](https://b.stripecdn.com/docs-statics-srv/assets/auth0_rules.b2453159ff14fa9990f3540dc0a8b0a2.png)

1. Choose the **empty rule** template, at the beginning of the page.

![creating an empty rule on Auth0](https://b.stripecdn.com/docs-statics-srv/assets/auth0_empty_rule_template.54a70bae08bdf3f457938d012eb3b6fd.png)

1. Set your rule name (for example, “SAML attribute mapping”) and then paste the following JavaScript code in the online editor. Then, click **Save**.

This script configures the Stripe roles you want to support in the Stripe Dashboard per Stripe account. You *must* include your team members’ roles as an attribute statement in any assertion that you send to Stripe. You can dynamically assign your team members different sets of roles per Stripe account. In the snippet example provided, Stripe assigns a newly signed-in user the default role `view_only`. If a user’s assertion doesn’t contain any role attribute statements, that user can’t log in through their identity provider.

```
function (user, context, callback) {
 // If there's no user app_metadata, create it.
 if (typeof (user.app_metadata) === 'undefined') {
    user.app_metadata = {};
 }

 // If the user doesn't have roles for the account, add a default value.
 if (typeof (user.app_metadata.) === 'undefined') {
    user.app_metadata. = ['view_only'];
 }

 // Add a mapping from app_metadata to the required SAML attribute.
 context.samlConfiguration.mappings = {
    "Stripe-Role-": "app_metadata."
 };

 callback(null, user, context);
}
```

1. Go to the **Users** tab, where you can assign team member roles for your application.

You can also override the Stripe Dashboard roles for your team members by updating the `app_metadata` field on Auth0. Set the metadata value to the [roles for your team members](https://dashboard.stripe.com/settings/team). Add entries for each Stripe account that needs access.

![user details on Auth0](https://b.stripecdn.com/docs-statics-srv/assets/auth0_user_metadata.89d76126775577363ddbd3f0d748e2f0.png)

Stripe supports the following roles. Some of these roles are only available if your account uses the applicable Stripe product. For more information, see [User roles supported by Stripe](/get-started/account/teams/roles).

| Role | Value |
| --- | --- |
| Administrator | `admin` |
| Analyst | `analyst` |
| Cardholder | `cardholder` |
| Connect Onboarding Analyst | `connect_onboarding_analyst` |
| Connect Risk Analyst | `connect_risk_analyst` |
| Data Migration Specialist | `data_migration_specialist` |
| Developer | `developer` |
| Dispute Analyst | `dispute_analyst` |
| Financial Connections Specialist | `financial_connections_specialist` |
| IAM Admin | `iam_admin` |
| Identity Analyst | `identity_analyst` |
| Identity View only | `identity_view_only` |
| Issuing Support Agent | `issuing_support_agent` |
| Opal View only | `opal_view_only` |
| Sandbox Administrator | `sandbox_admin` |
| Sandbox User | `sandbox_user` |
| Super Administrator | `super_admin` |
| Support Associate | `support_associate` |
| Support Communications | `support_communications` |
| Support Specialist | `support_specialist` |
| Refund Analyst | `refund_analyst` |
| Tax Analyst | `tax_analyst` |
| Terminal Specialist | `terminal_specialist` |
| Top-up Specialist | `topup_specialist` |
| Transfer Analyst | `transfer_analyst` |
| View only | `view_only` |

### Multiple Stripe accounts

If you have team members with multiple Stripe accounts, update the JavaScript rule to handle several accounts.

```
function (user, context, callback) {
 // If there's no user app_metadata, create it.
 if (typeof (user.app_metadata) === 'undefined') {
    user.app_metadata = {};
 }

 // If the user doesn't have roles for the accounts, add a default value.
 if (typeof (user.app_metadata.acct_1234}) === 'undefined') {
    user.app_metadata.acct_1234} = ['view_only'];
 }
 if (typeof (user.app_metadata.acct_5678}) === 'undefined') {
    user.app_metadata.acct_5678} = ['view_only'];
 }

 // Add a mapping from app_metadata to the required SAML attribute.
 context.samlConfiguration.mappings = {
    "Stripe-Role-acct_1234": "app_metadata.acct_1234"
    "Stripe-Role-acct_5678": "app_metadata.acct_5678"
 };

 callback(null, user, context);
}
```

In the user profiles, add one entry per account in the `app_metadata` field.

The following example shows user app metadata that is associated with two Stripe accounts. The team member has the both `analyst` and `developer` roles for the first account, and the role `view_only` for the second account.

```
{
 "acct_1234": [
    "analyst",
    "developer"
 ],
 "acct_5678": [
    "view_only",
 ]
}
```

You can find the list of account tokens in the **Accounts** section of your [Personal details](https://dashboard.stripe.com/settings/user) settings.

[## Configuring Stripe](#configure-stripe)

Configure your Stripe account to connect to your identity provider from the [User authentication](https://dashboard.stripe.com/account/user_authentication) page.

To configure Stripe to connect to your identity provider you need:

- **Issuer ID**: An identifier of your identity provider.
- **Identity provider URL**: The URL of your identity provider that your team members are redirected to, so they can authenticate.
- **Identity provider certificate**: The X.509 certificate that your identity provider uses to signs assertions.

#### Find these values in your identity provider

In **Auth0**, go to the settings in the **Applications** menu. Select your application name, then go to the **Addons** tab, select the **SAML2** button, then select the **Usage** tab.

| Name of property in Stripe | Name of property in Auth0 |
| --- | --- |
| Issuer ID | Issuer |
| Identity provider URL | Identity Provider Login URL |
| Identity provider certificate | Auth0 certificate |

#### Test your configuration

Before saving your settings, a test runs to validate your SSO integration. After you click the **Test** button, a window opens in your browser that redirects to your identity provider to sign in. After you sign in, the window automatically closes and test results display on the original page.

If the test succeeds, you can save the settings, and select an enforcement mode. If the test fails, modify your configuration to address the issues reported and test the integration again.

#### Select an enforcement mode for SSO

When using SSO, there are three separate enforcement modes that you can choose from. These affect which methods of authentication your team members can use.

| Mode | SSO authentication allowed | Regular authentication allowed |
| --- | --- | --- |
| Off | No | Yes |
| Optional | Yes | Yes |
| Required | Yes | No |

[## Authenticate with SSO](#authenticate-sso)

After you finish configuring SSO, you can inform your users to sign in with any of these methods:

### Stripe’s sign in page

Users can go to the [Stripe sign in page](https://dashboard.stripe.com/login), enter their email, then select **Use single sign-on (SSO)**.

If a user has access to multiple accounts, Stripe authenticates them with the default account connected to the user. If a user only has access to SAML merchants, or doesn’t have access to any merchants, Stripe redirects them to the IdP, regardless of the contents in the password field.

### IdP-initiated login

To use IdP-initiated login, your [IdP needs to support Service Provider-initiated login](/get-started/account/sso/troubleshooting). Verify if this is possible using your IdP’s documentation.

### SSO URL

Use the following login URL with your domain to directly sign in to your account with SSO. This URL includes the domain and account you want to use for SSO authentication. If you change the account token at the end of the URL, it authenticates you against a different account.

```
https://dashboard.stripe.com/login/saml_direct/domain/{{YOUR_DOMAIN}}/merchant/{{STRIPE_ACCOUNT_ID}}
```

#### Support for multiple Stripe accounts

If you’re configuring SSO for multiple Stripe accounts, first create an [organization](/get-started/account/orgs) to centrally configure SSO across all of your accounts. You can change the account token at the end of the SSO URL to authenticate against another account. You can find the list of account tokens in the **Accounts** section of your [Personal details](https://dashboard.stripe.com/settings/user) settings.

**Multiple IdP connections:** If you have multiple Stripe businesses with multiple IdP settings (for example, different SAML endpoints or issuer IDs) but share the same domain, we recommend using login URLs.

## Revoke team member access

You can revoke a team member’s access using either active or passive methods.

### Actively revoke access with an assertion

Send Stripe an assertion from your identity provider to grant a team member access to specific Stripe accounts. This also lets you revoke a team member’s access. To revoke access for a team member, assign them a role of `none` for the Stripe account’s access you want to revoke. For example:

```
<saml2:attribute name="Stripe-Role-STRIPE-ACCOUNT-ID" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic">
 <saml2:attributevalue>none
 </saml2:attributevalue>
</saml2:attribute>
```

#### Caution

You can’t revoke access for the owner of a Stripe account.

### Passively revoke access with enforcement mode

When **enforcement mode** is set to **required**, only team members who can authenticate with your identity provider can access your Stripe account. In **required** mode, you can revoke a team member’s access to a Stripe account by preventing your identity provider from authenticating them. In the Stripe Dashboard, set SSO to **required** in [User authentication](https://dashboard.stripe.com/account/user_authentication).