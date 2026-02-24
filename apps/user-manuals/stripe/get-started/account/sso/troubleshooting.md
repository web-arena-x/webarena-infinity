# Troubleshoot SSO

Source: https://docs.stripe.com/get-started/account/sso/troubleshooting

---

Troubleshoot SSO

[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fsso%2Ftroubleshooting)

[The Stripe Docs logo](/)

Search

`/`Ask AI

[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fsso%2Ftroubleshooting)

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

Troubleshoot SSO

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

# Troubleshoot SSO

## Learn how to resolve common errors that might occur when configuring SSO.

Ask about this page

Copy for LLMView as Markdown

When setting up SSO for your account, you can test your SSO configuration before saving it to prevent misconfiguring SSO and locking out your users. If the test wizard discovers errors, use this guide to understand and resolve them.

| Error | Description | Resolution |
| --- | --- | --- |
| The SAML request has expired | The SAML request included a timestamp that’s no longer valid. SAML requests are typically time-sensitive to make sure the user authenticated recently. | Try signing in again to generate a fresh SAML assertion from your identity provider. |
| Invalid SAML response | The SAML response received from the Identity Provider (IdP) doesn’t conform to the expected format or contains incorrect information. | Review the SAML response using tools like [SAML Tracer](https://chromewebstore.google.com/detail/saml-tracer/mpdajninpobndbfcldcmbpnnbhibjmch?hl=en) (for Chrome) or a similar tool. |
| Invalid issuer ID | The issuer ID (also called Entity ID) in the SAML response doesn’t match the issuer ID configured in Stripe. | Log into your identity provider and go to the integration settings. Confirm that the issuer ID for your Stripe app matches the issuer ID you configured in Stripe. |
| Invalid identity provider URL | The identity provider URL configured in Stripe that directs users to login to the identity provider is incorrect or unreachable. | Log into your identity provider and go to the integration settings. Confirm that the identity provider URL for your Stripe app matches your configuration in Stripe. |
| Invalid identity provider certificate | The certificate provided by the identity provider is invalid or not trusted. | Make sure that you’re using the correct IdP certificate. You can often find the latest certificate in the IdP dashboard under security settings. If the certificate has changed, download the new one and replace the existing certificate in your SSO configuration. |
| User doesn’t belong to the verified domain | The user attempting to authenticate doesn’t belong to the allowed domain. | Check the domain associated with the user’s email address. If they need to be granted access, verify their account configuration in the identity provider. Make sure that the user’s email address matches the domain allowed for SSO. If you need to make changes, update the user’s account in the IdP. |
| No roles were found for the user | No roles were found in the SAML response for the user. | Make sure that the identity provider is configured to send role assertions for the user. Review the roles associated with the user in the IdP, and verify they’re properly assigned. For a list of available roles and how to configure them, see [User roles](/get-started/account/teams/roles). |
| Invalid role assignment from identity provider | The role assertion in the SAML response is either missing or invalid. | Confirm that your identity provider is set up to send the necessary role assertions. Review the IdP’s configuration and role mappings. If role assertions are missing, consult the IdP documentation or IdP support on how to properly configure them. |

## Other common errors

The following examples are additional error messages that you might encounter and possible solutions.

### Configure your app error

When configuring your application, you might see an error message indicating an issue with authentication:

```
{"error":{"message":"Required field","param":"RelayState"}}
```

This might indicate that you’re starting authentication from an identity provider that doesn’t support service provider-initiated authentication. We support only identity provider-initiated authentication where the identity provider also supports service provider-initiated authentication. This issue might also occur if your identity provider isn’t correctly passing the `RelayState` parameter from the authentication request back with your assertion.

### Sign into Stripe error

When signing into Stripe, you might see the following error message:

```
SAML. Error: Invalid signature type
```

This error indicates that the SAML response isn’t signed with the correct algorithm. The signature algorithm must be `RSA-SHA256`, and the digest algorithm must be `SHA256`. We enforce these standards for security reasons because `SHA-256` is the industry-standard hashing algorithm. `SHA-1`, the previous standard, is no longer considered secure. Refer to your identity provider’s documentation for guidance on configuring your integration to use `SHA-256`.

### UI log in error

If you can’t use the UI to log in with SSO after configuration, it might indicate that your domain isn’t validated. Make sure the exact domain that you use for your email is verified in the [User authentication](https://dashboard.stripe.com/account/user_authentication) page.

If you’ve validated the same domain in multiple accounts with different identity provider configurations, we can’t determine which identity provider to use. To resolve this, use the following URL with your verified domain to directly sign into your account with SSO. This URL includes the domain and account for authentication. By changing the account token at the end of the URL, you can authenticate against a different account.

```
https://dashboard.stripe.com/login/saml_direct/domain/{{YOUR_DOMAIN}}/merchant/{{STRIPE_ACCOUNT_ID}}
```

If you have another account that isn’t controlled by SSO and haven’t validated your email address for that account, validate your email address and try again.

### Missing role error

If you encounter an error indicating you need to have a role when trying to sign in after configuring SSO, this means we haven’t received a role for the user in the SAML assertion from the identity provider. Verify that the assertion being sent to Stripe contains the following attribute.

```
<saml2:AttributeStatement>
  <saml2:Attribute Name="Stripe-Role-" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic">
    <saml2:AttributeValue>role_id
    </saml2:AttributeValue>
  </saml2:Attribute>
</saml2:AttributeStatement>
```

If the assertion already contains this attribute, make sure that you’re sending a valid `role_id`.

### CSRF token error

If you encounter a CSRF token error, verify that you’ve correctly configured the URLs in your identity provider. Pay close attention to the **SSO URL** and **Audience URI** or **Entity ID** as indicated in the documentation, and ensure you’ve entered them accurately in your identity provider setup.

### Locked out of the Dashboard

If only one team member is locked out of the Stripe Dashboard, it usually indicates an incorrect configuration within the identity provider. Typically, the problem is that the SAML authentication request doesn’t include a role for each Stripe account the team member needs to access. The team member must consult with their identity provider’s administrator to verify their configuration is correct.

If all team members are locked out of the Stripe Dashboard, it might be due to misconfigured SSO settings or an issue with the identity provider, such as an outage. In this scenario, the account representative must contact [Stripe support](https://support.stripe.com/contact). After identity verification, we change the account’s SSO configuration from `Required` to `Optional`, allowing the identity provider’s administrator to sign in and fix the configuration.

## SSO limitations

Stripe doesn’t support the following SSO features:

- **User deletion in SAML**: Due to the limitations of SAML, Stripe doesn’t get notified when user access is revoked in the IdP. If users attempt to log in again through SSO after their current session expires, Stripe automatically revokes their access. To remove access instantly, delete the users in your [Team settings](https://dashboard.stripe.com/settings/team).
- **System for Cross-domain Identity Management (SCIM)**: SCIM is a protocol that an IdP uses to synchronize user identity lifecycle processes—such as provisioning, deprovisioning access, and populating user details—with a service provider such as Stripe.

If a team member is added to your identity provider, Stripe handles Just-in-Time creation for that team member. This means that if the team member signs in with SSO to the Stripe Dashboard and doesn’t have an existing Stripe account, we create one for them. When you change a team member’s Dashboard role, Stripe updates their role the next time they sign in.

- **Mobile app authentication**: We don’t support SSO through Stripe’s mobile apps.
- **Configure SSO session length**: The SSO session length is set to 12 hours and isn’t configurable.
- **Native IdP-initiated login**: Support for authentication through the Service Provider necessary for Identity Provider-initiated login to work. Native IdP-initiated login isn’t supported due to security concerns with the SAML protocol.

For example, a man-in-the-middle attack might intercept the SAML assertion and replay it later to gain unauthorized access to an account. When team members attempt to sign in using their IdP, Stripe treats the request as a Service Provider-initiated login and authenticates the team member as expected.

## SSO supported features

Stripe supports the following SSO features:

- **Team members with different roles**: When signing in, your identity provider must send the correct team member’s role in the AttributeStatement. For a working example, see Okta’s [Mapping dynamic team member roles to groups](/get-started/account/sso/okta#assign-stripe-roles).
- **Sign in to multiple accounts using one SAML assertion**: Send Stripe an assertion from your identity provider with multiple role attributes that contain all the account ids that you want to configure access to. For example:

  ```
  <saml2:AttributeStatement>
    <saml2:Attribute Name="Stripe-Role-STRIPE-ACCOUNT-ID1" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic">
      <saml2:AttributeValue>role_id
      </saml2:AttributeValue>
    </saml2:Attribute>
    <saml2:Attribute Name="Stripe-Role-STRIPE-ACCOUNT-ID2" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic">
      <saml2:AttributeValue>role_id
      </saml2:AttributeValue>
    </saml2:Attribute>
  </saml2:AttributeStatement>
  ```
- **Disable SSO**: You can set the **enforcement mode** of your account to **Off** from the [User authentication](https://dashboard.stripe.com/account/user_authentication) page to disable SSO. This removes access for any user who can only access the team with SAML. This includes any user who doesn’t have a password set.
- **Migrate to another IdP**: To migrate to another IdP, update your SSO settings from the [User authentication](https://dashboard.stripe.com/account/user_authentication) page. When updating SSO settings, first set the **enforcement mode** of your account to **optional**.

This ensures that if there’s an issue, you can still sign in to the Stripe Dashboard with your email and password. If you have a test account, update your SSO settings in your test account first and validate the new settings before updating your other accounts.