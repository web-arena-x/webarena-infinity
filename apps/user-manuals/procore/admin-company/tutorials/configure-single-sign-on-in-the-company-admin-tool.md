# Configure Single Sign-On in the Company Admin Tool

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/configure-single-sign-on-in-the-company-admin-tool

---

## Background

Procore supports SP-initiated and IdP-initiated SSO with Okta, OneLogin, and Microsoft Azure AD. See [What is the difference between SP- and IdP-Initiated SSO?](/faq-what-is-the-difference-between-sp-and-idp-initiated-sso) Procore also supports SSO with other service providers that are SAML 2.0 and SHA 256 compliant.

To assist you with understanding the terms discussed below, here are some definitions:

- Identity Provider (IdP). This is the service that verifies the identity of your end users (e.g., Okta, OneLogin, or Microsoft Azure AD).
- Issuer URL (Entity ID). A unique string that identifies the provider issuing a SAML request.
- **SAML**. Short for *Security Assertion Markup Language*.
- Service Provider (SP). Procore
- **Target URL**. The IdP URL that will receive SAML requests from Procore.
- **X.509 Certificate**. This is an encrypted digital certificate that contains the required values that allow the SSO service to verify the identities of your users.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Company level Admin tool.
- **Additional Information:**

 - Please contact your SSO service provider if you need assistance locating the **Issuer URL**, **Target URL**, and **x509 Certificate**.

## Prerequisites

- Configure the Procore application in your identity provider's SSO software or solution.
- Obtain the required SSO Settings from your identity provider's SSO software or solution.

## Steps

1. Navigate to the Company level **Admin** tool.
2. Under 'Company Settings,' click **Single Sign On Configuration**. *Note:* The data you enter on the page below is always obtained from the issuer (e.g., Okta, OneLogin, or Microsoft Azure AD).

   ##### Â Tip

   See the links below for more detailed instructions about configuring SSO with Okta, OneLogin, Azure Active Directory, and Google.

   - [Okta SSO](https://support.procore.com/integrations/okta-sso)
   - [OneLogin SSO](https://support.procore.com/integrations/onelogin-sso)
   - [Azure Active Directory SSO](https://support.procore.com/integrations/azure-ad-sso)
   - [Google SSO](https://support.procore.com/integrations/google-sso)

    - Enter the **Single Sign On Issuer URL**. This is commonly referred to as the *issuer* and is a unique URL that identifies the provider issuing a SAML request.
- Enter the **Single Sign On Target URL**. This is the URL that will receive SAML requests from the provider.
- Enter the **Single Sign On x509 Certificate**. This is the encrypted digital certificate information.

 #### SSO Content Reuse

 ##### Â Optional - Unique Entity ID

 **When configuring SSO for a single Procore instance, you should NOT check this box.**

 If your company licenses more than one Procore instance, and you want to configure unique Procore enterprise applications within your IdP tenant for each instance, you can by enabling **Unique Entity ID.** If enabled, you are still limited to one (1) enterprise application per Procore company instance.

 ***Important:*** *SSO for Procore targets users by email domain. An email domain can only be targeted once in all of Procore, so if you're considering setting up SSO with Unique Entity IDs across multiple Procore instances, remember that you can only target an email domain once, in a single instance.*

 To generate a Unique Entity ID for an enterprise application, check the **Enable** **Unique Entity ID** box in the Procore Admin tool's SSO configuration page for the Procore instance you want to specify on an enterprise application. Checking this box will generate a unique Entity ID URL in the field below, which you will then copy and paste into the appropriate Entity ID field in your IdP's configuration page.

 ***Notes:*** *You must save your configuration with the box checked to generate the Unique Entity ID. Enabling this feature does not impact user membership or access to a given instance. Access to a company in Procore is determined by a user's presence in the Directory tool, and their configured permissions within Procore. Auto-provisioning with SSO is not supported at this time.*

- Click **Save Changes**.
- Reach out to Procore Support or your company's Procore point of contact to request to target the email domains of users who will be authenticating through SSO.
- After you receive confirmation that the SSO configuration is ready, mark the **Enable Single Sign On** checkbox on the 'Single Sign On Configuration' page.
- Click **Save Changes**.