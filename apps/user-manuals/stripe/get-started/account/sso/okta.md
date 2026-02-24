# Single sign-on with Okta

Source: https://docs.stripe.com/get-started/account/sso/okta

---

Okta

[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fsso%2Fokta)

[The Stripe Docs logo](/)

Search

`/`Ask AI

[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fsso%2Fokta)

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

Okta

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

# Single sign-on with Okta

## Learn how to setup single sign-on in the Dashboard with Okta.

Ask about this page

Copy for LLMView as Markdown

Stripe supports Single Sign-On (SSO), allowing you to manage your team’s access and roles through your identity provider (IdP). This means your team can access Stripe without needing separate passwords. When SSO is configured, users (team members) are automatically redirected to your IdP for authentication when they sign in to Stripe.

Your IdP verifies if they have a valid role assignment to your Stripe accounts or [organization](/get-started/account/orgs/sso), and generates a SAML assertion used by Stripe to assign the proper roles in the Stripe Dashboard. When your account requires SSO, you must update team roles through your Identity Provider (IdP) for security. Changes to a team member’s roles only appear in Stripe after they sign in to the Dashboard again using the updated SAML assertion.

[## Verify domain ownership](#verify-domain-verification)

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

[## Create a Stripe app in Okta](#create-app)

Create an app in Okta to represent the relationship between the Stripe Dashboard and Okta:

1. Open and log in to the Okta admin portal.
2. In the left navigation pane, go to **Dashboard** > **Applications** > **Add Application**.
3. Click **Create App Integration** > **SAML 2.0** > **Next**.
4. Enter an **App name** (for example `Stripe Integration`), then click **Next**.
5. Configure your SAML settings in Okta:
   - For **Single sign-on URL**, add the value: `https://dashboard.stripe.com/login/saml/consume`.
   - For **Audience URI**, add the value: `https://dashboard.stripe.com/saml/metadata`.
   - For **Name ID format**, select `EmailAddress`.
   - For **Application username**, select `Email`.
6. Next, click **Show Advanced Settings**:
   - For **Signature Algorithm**, select `RSA-SHA256`.
   - For **Digest Algorithm**, select `SHA256`.
7. Click **Next**, then select **This is an internal app that we created** for **App type**.
8. Click **Finish**.

[## Assign Stripe roles in Okta](#assign-stripe-roles)

Assign Stripe roles for your users by creating attribute statements in your Stripe app in Okta. Stripe roles give users different degrees of access to the Stripe Dashboard. An attribute statement consists of two components. The `name` represents the Stripe account where you want to assign roles. The `value` represents the roles you want to assign to the Stripe account. Users can have different roles in a single account or across multiple accounts in an [organization](/get-started/account/orgs/sso).

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

### Create a custom role attribute

1. In the left navigation pane, go to **Directory** > **Profile Editor**.
2. Click the name of your Stripe app, then click **Add Attribute**.
3. Set **Data type** to `String Array`.
4. For **Display name**, enter `Stripe Roles`.
5. For **Variable name**, enter `stripe_roles`.
6. Select **Define enumerated list of values**, then add an attribute member for each Stripe role you want to assign to your users. For example, Display name: `Administrator`, Value: `admin`.

   #### Warning

   Make sure to assign at least one user or group the `super_admin` role. This ensures your organization receives important notifications about your account health. Only users with the Super Admin role can make changes to your account structure, close the account, or change the default bank account.
7. For **Attribute required**, select **Yes**.
8. For **Attribute type**, select **Group**.
9. For **Group Priority**, select **Combine values across groups**. Select this if you want to assign a user multiple roles across multiple Stripe accounts.
10. Click **Save**, and copy the variable name of the attribute you created for later use.

![](https://b.stripecdn.com/docs-statics-srv/assets/okta_profile_editor_add_attribute_enum.54a4493a2d8c5f344b6efd7eeeea7d1f.png)

### Create a group of users

1. In the left navigation pane, go to **Directory** > **Groups**.
2. Click **Add group**, enter a group name (such as Super Admins in Stripe), then click **Save**.
3. In the group list, click the name of your group, then click **Assign people**.
4. Add users by searching for their first name, primary email address, or username.

### Grant the group access to the Stripe app

1. Click the **Applications** tab > **Assign applications**.
2. Next to the name of your Stripe app, click **Assign**.
3. Select any Stripe roles you want to give to the group, then click **Save and go back** > **Done**. This assigns the roles to all the users in this group. All the users in this group can log into Stripe, and their role is automatically set to the value you set.

   ![](https://b.stripecdn.com/docs-statics-srv/assets/okta_group_assign_role.b5ea106d2ac34805328b0cc6b0139707.png)

   If a user belongs to multiple groups, Okta combines the roles assigned across all the groups. For example, if a user belongs to the following groups:

   - `IAM Group`
   - `Stripe Admin Group`
   - `Stripe Developer Group`

   Then, they’re assigned the roles from all of the groups:

   ![](https://b.stripecdn.com/docs-statics-srv/assets/okta_application_role_groups_combination.cfacba3c3b8508cea17b4715e48ebc43.png)

### Update the value of your attribute statement

1. In the left navigation pane, go to **Applications**, then click your Stripe app.
2. Click the **General** tab > **SAML settings** > **Edit**.
3. In the **Attribute Statements** section, assign a dynamic role to a user:
   - For **Name**, enter the Stripe account ID. Use the format `Stripe-Role-<account-id>`. For example, if the account ID is `acct_1JgxGwHIzIlFIyZf`, enter the name `Stripe-Role-acct_1JgxGwHIzIlFIyZf`. For a list of account ids, go to the **Accounts** section in your [Personal details](https://dashboard.stripe.com/settings/user) settings in the Stripe Dashboard.
   - For **Name format**, select `Basic`.
   - For **Value**, enter `appuser.<variable-name>`. If you didn’t save the variable name, go to **Directory** > **Profile Editor**, click your Stripe app, and use the variable name next to the applicable attribute. For example, `appuser.stripe_roles`.
4. Click **Save**. This tells Okta to send an attribute statement with each assertion for the account and role.

### Optional Assign roles in multiple Stripe accounts

To assign roles across multiple Stripe accounts, create a separate attribute statement in your app for each of your accounts.

![](https://b.stripecdn.com/docs-statics-srv/assets/okta_attribute_statements.d16b78113f5a0f92458980c165f9fc79.png)

### Optional Assign roles in your organization

If you use [Organizations](/get-started/account/orgs), grant team members access to your organization by assigning roles in your organization. [Organization-level roles](/get-started/account/orgs/team#organization-account-roles) grant access to the Organization, as well as all of the accounts within it.

1. Find your `organization-id` in Stripe by account switching to your organizations and navigating to **Settings > Organizations management**.
2. In Okta, in your app’s list of **Attribute Statements**, create an attribute statement using the format `Stripe-Role-<organization-id>`.

[## Configure Stripe](#configure-stripe)

To configure Stripe with SSO:

### Retrieve the following values from Okta

1. Open the Okta admin portal.
2. In the left navigation pane, go to **Applications**, then select your Stripe app.
3. Click the **Sign On** tab > **View SAML Setup Instructions** to open a page that displays the following values:
   - **Identity provider Issuer**: An identifier of your identity provider.
   - **Identity provider single Sign-On URL**: The URL of your identity provider that your users are redirected to, so they can authenticate.
   - **X.509 Certificate**: The X.509 certificate that your identity provider uses to sign assertions.

### Configure your Stripe account to connect with Okta

1. In the Stripe Dashboard, go to **Settings** > **Team and security** > [User authentication](https://dashboard.stripe.com/account/user_authentication).
2. Next to the domain name, click the overflow button () > **Manage SSO settings**.
3. Click **Test your configuration** > **Next**.
4. Provide info for your identity provider:

   - For **Issuer ID**, enter the value for **Identity provider Issuer** in Okta.
   - For **Identity provider URL**, enter the value for **Identity provider single Sign-On URL** in Okta.
   - For **Identity provider certificate**, enter the value for **X.509 Certificate** in Okta.
5. Click **Test configuration** to open a new window to test your configuration. Exit this window, and return to the original window.
6. If you pass the test, click **Done**.

   If the test fails, refer to [Troubleshoot SSO](/get-started/account/sso/troubleshooting), and address the reported issues in your Stripe app in Okta.
7. Select SSO enforcement. You can choose between **Off**, **Optional**, or **Mandatory**. You can change enforcement type in the future.
8. Click **Save settings** > **Done**.

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

1. Open your Stripe application in Okta.
2. Go to **Sign On** tab.
3. Under **SAML Signing Certificates**, click **Generate new certificate**.
4. For the newly created certificate, click the **Actions** menu and select **Download certificate**.

### Add the new certificate in Stripe

Add the new certificate as a secondary certificate in Stripe:

1. In the Stripe Dashboard, go to **Settings** > **Team and security** > **Single sign-on (SSO)**.
2. Select the domain from the list for which you want to rotate the certificate.
3. Click **Add** in the certificate section.
4. Copy and paste the downloaded certificate.
5. Click on **Continue** to add the new certificate.

### Activate the new certificate

Make the new certificate active in Okta:

1. Open your Stripe application in Okta.
2. Go to **Sign On** tab.
3. Under **SAML Signing Certificates**, click the **Actions** menu for the new certificate and select **Active**.
4. Verify that the certificate status changes to active.

### Test the new certificate

Ensure that users can log in by using SSO with the new certificate:

1. Log out from both Stripe dashboard and Okta.
2. Use SSO to sign in again and check for errors.

### Set the new certificate as primary

Make the new certificate primary in Stripe:

1. In the Stripe Dashboard, go to **Settings** > **Team and security** > **Single sign-on (SSO)**.
2. Select the domain from the list for which you want to rotate the certificate.
3. Click the overflow menu of the secondary certificate and select **Set as primary**.
4. Verify that the new certificate is displaying the primary label.

After completing these steps, you can optionally delete the old certificate by clicking the overflow menu and selecting **Delete**.

## See also

- [Troubleshoot SSO](/get-started/account/sso/troubleshooting)