# Configure Google SSO for Procore

Source: https://v2.support.procore.com/product-manuals/google-sso/tutorials/configure-google-sso-for-procore

---

##### Â Note

If your organization is using the [Portfolio Financials and Capital Planning](/product-manuals/portfolio-financials/) products in Procore, you will need to reach out to your Procore point of contact or the Support team to set up your Google SSO.

## Background

To assist you with understanding the terms discussed below, here are some definitions:

- Identity Provider (IdP). This is the service that verifies the identity of your end users (e.g., Okta, OneLogin, or Microsoft Azure AD).
- Issuer URL (Entity ID). A unique string that identifies the provider issuing a SAML request.
- **SAML**. Short for *Security Assertion Markup Language*.
- Service Provider (SP). Procore
- **Target URL**. The IdP URL that will receive SAML requests from Procore.
- **X.509 Certificate**. This is an encrypted digital certificate that contains the required values that allow the SSO service to verify the identities of your users.

The following configurations are supported with the Google SSO:

- **Service Provider Initiated (SP-initiated) SSO**. Referred to as Procore-initiated SSO, this option gives your end users the ability to sign into the Procore Login page and then sends an authorization request to the IdP. Once the IdP authenticates the user's identity, the user is logged into Procore.
- **Identity Provider Initiated (IdP-initiated) SSO**. With this option, your end users must log into your Identity Provider's SSO page and then click an icon to log into and open the Procore web application.

## Things to Consider

- **Required User Permissions:**

 - *To add Procore as a custom SAML application in Google:*\* Access to a Google super administrator account.
 - *To configure Google SSO in Procore:*\* 'Admin' level permissions on the Company level Admin tool.

## Steps

- Add Procore as a Custom SAML Application in Google
- Configure Google SSO in Procore

### Add Procore as a Custom SAML Application in Google

See Google's [Set up your own custom SAML application](https://support.google.com/a/answer/6087519?hl=en) for more information on the steps below.

1. Navigate to the **Google Identity Provider details** page in Google's Admin console.
2. Open a blank document on your computer.
3. Copy the **SSO URL** from the **Google Identity Provider details** page and paste it into your blank document.
4. Copy the **Entity ID** from the **Google Identity Provider details** page and paste it into your blank document.
5. Download the **Certificate** from the **Google Identity Provider details** page.
6. Open the **Certificate** and copy the text between **Begin Certificate** and **End Certificate**.
7. Paste the **Certificate** text into your blank document.
8. Complete the following in Google's **Service Provider Details** window:

   - **ACS URL:** <https://login.procore.com/saml/consume>
   - **Entity ID:** <https://login.procore.com/>

     #### SSO Content Reuse

     ##### Â Optional - Unique Entity ID

     **When configuring SSO for a single Procore instance, you should NOT check this box.**

     If your company licenses more than one Procore instance, and you want to configure unique Procore enterprise applications within your IdP tenant for each instance, you can by enabling **Unique Entity ID.** If enabled, you are still limited to one (1) enterprise application per Procore company instance.

     ***Important:*** *SSO for Procore targets users by email domain. An email domain can only be targeted once in all of Procore, so if you're considering setting up SSO with Unique Entity IDs across multiple Procore instances, remember that you can only target an email domain once, in a single instance.*

     To generate a Unique Entity ID for an enterprise application, check the **Enable** **Unique Entity ID** box in the Procore Admin tool's SSO configuration page for the Procore instance you want to specify on an enterprise application. Checking this box will generate a unique Entity ID URL in the field below, which you will then copy and paste into the appropriate Entity ID field in your IdP's configuration page.

     ***Notes:*** *You must save your configuration with the box checked to generate the Unique Entity ID. Enabling this feature does not impact user membership or access to a given instance. Access to a company in Procore is determined by a user's presence in the Directory tool, and their configured permissions within Procore. Auto-provisioning with SSO is not supported at this time.*

- **Start URL:** Leave this field blank.
- **Certificate:** Copy and paste the **Certificate** text from your blank document.
- **Signed Response:** Mark this checkbox.
- **Name ID:** Select **Basic Information** in the first drop-down menu and Primary Email in the second drop-down menu.
- **Name ID Format:** Select **EMAIL** in the drop-down menu.

### Configure Google SSO in Procore

1. Navigate to the Company level **Admin** tool in Procore.
2. Under **Company Settings**, click **Single Sign On Configuration**.
3. Complete the following:

   - Enter the **Entity ID** from the **Google Identity Provider details** page in the **Single Sign On Issuer URL** field.
   - Enter the **SSO URL** from the **Google Identity Provider details** page in the **Single Sign On Target URL** field.
   - Enter the **Certificate** text in the **Single Sign On x509 Certificate** field.
4. Click **Save Changes**.
5. Reach out to Procore Support or your company's Procore point of contact to request to enable SSO. Include the email domain you'd like to target for SSO in your request.
6. After you receive confirmation that the SSO configuration is ready, mark the **Enable Single Sign On** checkbox on the 'Single Sign On Configuration' page.
7. Do one of the following:

   - Select the **Allow Password Login** option.
   - Select the **Service Provider Forward** option.
8. Click **Save Changes**.