# Single sign-on with Entra ID

Source: https://docs.stripe.com/get-started/account/sso/entra-id

---

Entra ID

[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fsso%2Fentra-id)

[The Stripe Docs logo](/)

Search

`/`Ask AI

[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fsso%2Fentra-id)

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

Entra ID

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

# Single sign-on with Entra ID

## Learn how to setup single sign-on in the Dashboard with Entra ID.

Ask about this page

Copy for LLMView as Markdown

Use [Microsoft Entra ID](https://entra.microsoft.com/) (formerly known as Azure Active Directory) to verify domain ownership, create user role groups, configure single sign-on (SSO), and assign roles to manage access to your Stripe account.

Stripe supports Single Sign-On (SSO), allowing you to manage your team’s access and roles through your identity provider (IdP). This means your team can access Stripe without needing separate passwords. When SSO is configured, users (team members) are automatically redirected to your IdP for authentication when they sign in to Stripe.

Your IdP verifies if they have a valid role assignment to your Stripe accounts or [organization](/get-started/account/orgs/sso), and generates a SAML assertion used by Stripe to assign the proper roles in the Stripe Dashboard. When your account requires SSO, you must update team roles through your Identity Provider (IdP) for security. Changes to a team member’s roles only appear in Stripe after they sign in to the Dashboard again using the updated SAML assertion.

[## Verify domain ownership](#domain-verification)

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

[## Create groups of users in Entra ID](#assign-roles)

Create groups for Stripe roles and assign your team members (users) to these groups. Users can belong to only one group per Stripe account. For example, if you want a user to have an admin role, assign them to the administrator group. However, if you want a user to have multiple roles, such as view only and analyst, create a separate group specifically for those combined roles.

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

1. Log in to the [Entra ID Dashboard](https://entra.microsoft.com/).
2. In the left navigation pane, click **Groups**.
3. Click **Add new group**:
   - For **Group type**, select **Security**.
   - For **Group name**, enter the name of the group (for example, View only users in Stripe).
4. Click **No members added**, and add users to the group.

[## Create an Entra ID application](#create-entra-app)

#### Caution

In most cases, you should create only one application for Stripe in Entra ID, even if you have multiple Stripe accounts. You can assign users access to multiple accounts or your organization by adding multiple claims (one per account) to your application. If you have more than 50 accounts, see how to [set up multiple applications in Entra](#set-up-multiple-applications).

To configure Entra ID, create a new application to represent the relationship between Entra ID and the Stripe Dashboard:

1. In the left navigation pane, click **Applications** > **Enterprise applications**.
2. Click **Create your own application**, enter the name your application, select **Integrate any other application you don’t find in the gallery**, and click **Create**.
3. Under **Getting Started**, click **1. Assign users and groups**.
4. Click **Add user/group**, and select the groups you previously created.
5. In your app’s left navigation page, click **Overview** > **2. Set up single sign on**.
6. Select **SAML** to open the **SAML-based Sign on** page.
7. Click **Basic SAML Configuration**, enter the following values, and click **Save**.
   - Identifier: `https://dashboard.stripe.com/saml/metadata`
   - Reply URL: `https://dashboard.stripe.com/login/saml/consume`

[## Add attributes and claims](#add-claims)

You must assign attributes and claims to the groups you created.

1. On the **SAML-based Sign on** page, click **Attributes and claims**.
2. Click **Add new claim**. You must create a new claim for each Stripe account you’re configuring SSO for.
3. Click **Claim conditions** to create the mapping between the group and the role you want to the group for this Stripe account.
   1. Set the **Name** to `Stripe-Role-{{STRIPE_ACCOUNT_ID}}`. This identifies which Stripe account you authenticate your team member to (and is set to whichever Stripe account you’re signed in to while viewing this page, currently: )
   2. For **Source**, select **Attribute**.
   3. For **User type**, select **Members**.
   4. For **Group**, select the group you want.
   5. For **Source**, select **Attribute**.
   6. For **Value**, enter the [Dashboard role](/get-started/account/teams/roles) you want to assign (for example, `developer`), and click **Enter**. This means you’ve assigned this role to any members in this group.
4. Assign Stripe roles you want to the groups you created. If you want a user to have multiple roles (such as view only and analyst), you must create a separate group that exists specifically for those combined roles.

   ![](https://b.stripecdn.com/docs-statics-srv/assets/entra-groups.b650223fb46d9078da4161162dc89f8c.png)
5. Click **Save**.

### Set up multiple applications

If you have more than 50 Stripe accounts and add a separate claim for each account, you will likely exceed the claim limit in Entra. To manage access to a large number of accounts in Stripe, there are two options:

1. (Recommended) [Consolidate your SSO settings into an Organization](/get-started/account/orgs/sso), and reduce the number of claims by using organization-level roles.
2. Set up multiple Stripe applications (one per account). For every account, set the **Identifier (Entity ID)** to `https://dashboard.stripe.com/saml/metadata/{STRIPE_ACCOUNT_ID}`. We refer to this as an **Account ID**-based custom issuer.

[## Verify certificates](#verify-certificates)

On the **SAML-based Sign on** page, click **SAML certificates** to verify if the signing algorithm configuration is correct. Ensure the following values match:

- **Signing Option**: `Sign SAML assertion`
- **Signing Algorithm**: `SHA-256`

[## Configure Stripe](#configure-stripe)

To configure Stripe with SSO:

### Retrieve values from Entra ID

Retrieve the values for **Login URL**, **Microsoft Entra Identifier**, and **PEM SAML Certificate** from your app in Entra ID.

1. Open the Entra ID Dashboard.
2. In your app’s left navigation pane, click **Single sign-on**.
3. On the **SAML-based Sign on** page, go to **Set up Stripe**, and retrieve the following values for:
   - Login URL
   - Microsoft Entra Identifier
4. On the **SAML-based Sign on** page, click **SAML Certificates**.
5. Next to your certificate, click the overflow button (), and click **PEM certificate download**
6. Open the `.pem` file in a basic text editor. This is your **Identity provider certificate**.

### Configure your Stripe account to connect to Entra ID

Enter the values you retrieved from your app in Entra ID in Stripe:

1. In the Stripe Dashboard, go to **Settings** > **Team and security** > [User authentication](https://dashboard.stripe.com/account/user_authentication).
2. Next to the domain name, click the overflow button () > **Manage SSO settings**.
3. Click **Test your configuration** > **Next**.
4. Provide info for your identity provider:
   - For **Issuer ID**, enter the value for **Microsoft Entra Identifier** in Entra ID.
   - For **Identity provider URL**, enter the value for **Login URL** in Entra ID.
   - For **Identity provider certificate**, enter the certificate value from the `.pem` file you downloaded in Entra ID (include the begin certificate and end certificate text).
5. Click **Continue**.
6. If you set up an **Account ID**-based custom issuer earlier, select the **By Account ID** advanced settings option. Otherwise, continue with the default selected option.
7. Click **Test configuration** to open a new window to test your configuration. Exit this window, and return to the original window.
8. If you pass the test, click **Done**.

If the test fails, refer to [Troubleshoot SSO](/get-started/account/sso/troubleshooting), and address the reported issues in your Stripe app in Okta.

1. Select SSO enforcement. You can choose between **Off**, **Optional**, or **Mandatory**. You can change enforcement type in the future.
2. Click **Save settings** > **Done**.

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

## Rotate Identity Provider Certificate

Follow these steps to rotate the primary signing certificate for your SSO domain in Entra ID. This process ensures that you can test the new certificate before you make it the primary.

### Generate a new certificate

Create a new certificate to replace your existing primary certificate:

1. Open your Stripe application in Entra ID.
2. Go to **Sign On** in the side navigation.
3. Click **Edit** on SAML certificates section.
4. Select **New certificate** and click **Save**.
5. Click the **Overflow** menu and select **PEM certificate download**.

### Add the new certificate in Stripe

Add the new certificate as a secondary certificate in Stripe:

1. In the Stripe Dashboard, go to **Settings** > **Team and security** > **Single sign-on (SSO)**.
2. Select the domain from the list for which you want to rotate the certificate.
3. Click **Add** in the certificate section.
4. Copy and paste the downloaded certificate.
5. Click on **Continue** to add the new certificate.

### Activate the new certificate

Make the new certificate active in Entra ID:

1. Open your Stripe application in Entra ID.
2. Go to **Sign On** in side navigation.
3. Click the overflow menu, and select **Make certificate active**.
4. Verify that the certificate status changes to active.

### Test the new certificate

Ensure that users can log in by using SSO with the new certificate:

1. Log out from both Stripe and Entra ID.
2. Use SSO to sign in again and check for errors.

### Set the new certificate as primary

Make the new certificate primary in Stripe:

1. In the Stripe Dashboard, go to **Settings** > **Team and security** > **Single sign-on (SSO)**.
2. Select the domain from the list for which you want to rotate the certificate.
3. Click the overflow menu of the secondary certificate and select **Set as primary**.
4. Verify that the new certificate is displaying the primary label.

After completing these steps, you can optionally delete the old certificate by clicking the overflow menu and selecting **Delete**.