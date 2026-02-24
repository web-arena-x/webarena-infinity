# Single sign-on with OneLogin

Source: https://docs.stripe.com/get-started/account/sso/onelogin

---

OneLogin

[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fsso%2Fonelogin)

[The Stripe Docs logo](/)

Search

`/`Ask AI

[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fsso%2Fonelogin)

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

[Auth0](/get-started/account/sso/v2/auth0)

[Entra ID](/get-started/account/sso/entra-id)

[Google Workspace](/get-started/account/sso/google-workspace)

[Okta](/get-started/account/sso/okta)

OneLogin

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

# Single sign-on with OneLogin

## Learn how to setup single sign-on in the Dashboard with OneLogin.

Ask about this page

Copy for LLMView as Markdown

Stripe supports Single Sign-On (SSO), allowing you to manage your team’s access and roles through your identity provider (IdP). This means your team can access Stripe without needing separate passwords. When SSO is configured, users (team members) are automatically redirected to your IdP for authentication when they sign in to Stripe.

Your IdP verifies if they have a valid role assignment to your Stripe accounts or [organization](/get-started/account/orgs/sso), and generates a SAML assertion used by Stripe to assign the proper roles in the Stripe Dashboard. When your account requires SSO, you must update team roles through your Identity Provider (IdP) for security. Changes to a team member’s roles only appear in Stripe after they sign in to the Dashboard again using the updated SAML assertion.

## Set up SSO

To integrate your Stripe account with your IdP, you’ll need to complete three steps:

1. [Prove ownership of the domains](#proving-domain-verification) that your team will use to sign in to the Dashboard.
2. [Configure OneLogin](#configuring-your-identity-provider) to work with Stripe.
3. [Configure Stripe](#configure-stripe) to work with OneLogin.

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

[## Configuring OneLogin](#configuring-your-identity-provider)

#### Caution

There isn’t an official Stripe SAML connector in OneLogin yet. The only available Stripe app is for password-based authentication. Don’t use the password-based authentication for SAML.

1. Create a new application to represent the relationship between OneLogin and the Stripe Dashboard. To do so, go to the **Applications** page, and select **Add App**.
2. Find the **SAML Test Connector (IdP w/ attr w/ sign response)** app.

1. Select **Save**, and go to the **Configuration** section. Then, enter the following values:
   - **Audience**: `https://dashboard.stripe.com/saml/metadata`
   - **Recipient**: `https://dashboard.stripe.com/login/saml/consume`
   - **Consumer URL Validator**: `https://dashboard.stripe.com/login/saml/consume`
   - **Consumer URL**: `https://dashboard.stripe.com/login/saml/consume`
2. Select **SSO** on the side panel, and set the **Signature Algorithm** to `SHA-256`.
3. Save your configuration changes by selecting **Save**.

### Assign roles to your team

To authenticate a team member to Stripe and assign them roles, configure OneLogin to send the roles in the SAML assertions.

1. Go to the **Parameters** section, and create a new **Field**
   - Set the **Field name** to  `Stripe-Role-` . This identifies which account you sign in to.
   - Select **Include in SAML assertion**.
2. In the next form, select the [Dashboard role](/get-started/account/teams/roles) you want your users to have by default. Select **Macro**, and input the desired default role in the field below

![](https://b.stripecdn.com/docs-statics-srv/assets/onelogin_new_parameter.0496199d3b37eca3ade10c4200adb7a2.png)

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

#### Support for multiple Stripe accounts

Repeat the previous step and add a **parameter** for each additional Stripe account. Select **Add parameter**, use the current account’s token for the **Field name** and choose the role you want your users to have by default.

The list of account tokens can be found in the **Accounts** section of your [Personal details](https://dashboard.stripe.com/settings/user) settings.

![](https://b.stripecdn.com/docs-statics-srv/assets/onelogin_multiple_accounts.881062c75df59f146f915201ac14cc0a.png)

1. Go to the **Users** tab. Here, you can assign team members to your application. You can also configure which Roles a user obtains upon log in.
2. Select the **User** you want to edit. Then, go to **Applications** on the side panel.
3. In the next modal that opens, you can configure the roles that a user obtains when they log in. To use multiple roles, add a semicolon after each role. In the following example, the user obtains the `analyst` and the `developer` role when they sign in.

![](https://b.stripecdn.com/docs-statics-srv/assets/onelogin_user_parameters.1a0e52025623a3a6e194de3f0b37dffb.png)

[## Configuring Stripe](#configure-stripe)

### Enter values from your identity provider

Next, configure your Stripe account to connect to your identity provider from the [User authentication](https://dashboard.stripe.com/account/user_authentication) page.

To configure Stripe to connect to your identity provider you need:

- **Issuer ID**: An identifier of your identity provider.
- **Identity provider URL**: The URL of your identity provider that your team members are redirected to, so they can authenticate.
- **Identity provider certificate**: The X.509 certificate that your identity provider signs assertions with.

### How to find these values in your identity provider

In OneLogin, you can find these values by navigating to the **SSO** tab of [your application](#configuring_your_identity_provider).

| Name of property in Stripe | Name of property in OneLogin |
| --- | --- |
| Issuer ID | Issuer URL |
| Identity provider URL | SAML 2.0 Endpoint (HTTP) |
| Identity provider certificate | X.509 certificate (click **View Details**) |

![](https://b.stripecdn.com/docs-statics-srv/assets/onelogin_sso_parameters.d0dce86d4dd82e95c9598f0dc922405e.png)

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