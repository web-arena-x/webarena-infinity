# Single Sign-On for Premium Employers

Source: https://support.joinhandshake.com/hc/en-us/articles/360019327993-Single-Sign-On-for-Premium-Employers

---

Single sign-on (SSO) allows Premium partners (Essentials and Talent Engagement Suite customers) and their employees to securely access Handshake using the same credentials they use for other corporate applications.

Handshake supports SAML 2.0 authentication. If your company’s identity provider (IdP) supports SAML 2.0, SSO can be enabled for your Handshake account. To get started, contact your Handshake account manager to request SSO support.

*Premium features are for Handshake Premium accounts only. For more information, check out this* [*resource*](https://www.joinhandshake.com/employers-premium/)*!*

### 

### Configure SSO in Handshake

After SSO is enabled, it must be configured in Handshake by the company profile Owner or an Admin.

- *If you're unsure who the Owner is, refer to* [*Who is the Owner of My Company’s Profile?*](#).

1. Click on your name in the upper-right corner of any page, then select **Company settings** from the dropdown.

![Company settings.png](https://support.joinhandshake.com/hc/article_attachments/28310013802647)

2. In the left menu, select Single **Sign-On Settings**, then enter the following information:

1. - **Identity Provider's Single Sign-On URL** (*required*)
     - Provided by your identity provider.
   - **Identity Provider's Single Logout URL** (*optional*)
     - Provided by your identity provider.
   - **Identity Provider's Entity ID URI** (*required*)
   - **Name Identifier Format** (*optional*)
     - Currently, only the email address format is supported.
   - **Name Identifier Attribute** *(optional*)
     - The attribute in the SAML response that contains the name identifier. This value is configured in your identity provider.

3. When finished, click the green **Save Settings** button in the lower-right corner of the page.

### SSO settings.png

### Logging in

Once SSO is configured, all employees are automatically directed to authenticate through the company’s identity provider when logging in to Handshake.

![SSO login page.png](https://support.joinhandshake.com/hc/article_attachments/26655841583511)