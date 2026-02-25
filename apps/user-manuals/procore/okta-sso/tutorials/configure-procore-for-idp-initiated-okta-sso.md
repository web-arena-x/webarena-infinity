# Configure Procore for IdP-Initated Okta SSO

Source: https://v2.support.procore.com/product-manuals/okta-sso/tutorials/configure-procore-for-idp-initiated-okta-sso

---

##### Â Note

If your organization is using the [Portfolio Financials and Capital Planning](https://support.procore.com/products/portfolio-financials) products in Procore, you will need to reach out to your Procore point of contact  or the Support team to set up your Okta SSO.

## Background

If your company wants to configure Single Sign-On with Okta, you can leverage one of Procore's supported SSO solutions:

- **Identity Provider Initiated (IdP-initiated) SSO**. With this option, your end users must log into your Identity Provider's SSO page (for example, Azure AD or Okta) and then click an icon to log into and open the Procore web application. To configure this solution, see the Steps below.  
   OR
- **Service Provider Initiated (SP-initiated) SSO**. Referred to as Procore-initiated SSO, this option gives your end users the ability to sign into the Procore Login page and then sends an authorization request to the IdP. Once the IdP authenticates the user's identify, the user is logged into Procore. To configure this solution with Okta, see [Configure Procore-Initiated SSO for Okta](/product-manuals/okta-sso/tutorials/configure-sp-initiated-sso-for-procore-in-okta).

## Things to Consider

- **Required Permissions**:

  - Administrator permissions to Okta  
     AND
  - 'Admin' level permissions to Procore's Company level Admin tool.
- **Supported Authentication Protocol**:

  - Security Assertion Markup Language (SAML 2.0)
- **Limitations**:

  - Just In Time (JIT) provisioning is NOT supported.

#### SSO Content Reuse

##### Â Optional - Unique Entity ID

**When configuring SSO for a single Procore instance, you should NOT check this box.**

If your company licenses more than one Procore instance, and you want to configure unique Procore enterprise applications within your IdP tenant for each instance, you can by enabling **Unique Entity ID.** If enabled, you are still limited to one (1) enterprise application per Procore company instance.

***Important:*** *SSO for Procore targets users by email domain. An email domain can only be targeted once in all of Procore, so if you're considering setting up SSO with Unique Entity IDs across multiple Procore instances, remember that you can only target an email domain once, in a single instance.*

To generate a Unique Entity ID for an enterprise application, check the **Enable** **Unique Entity ID** box in the Procore Admin tool's SSO configuration page for the Procore instance you want to specify on an enterprise application. Checking this box will generate a unique Entity ID URL in the field below, which you will then copy and paste into the appropriate Entity ID field in your IdP's configuration page.

***Notes:*** *You must save your configuration with the box checked to generate the Unique Entity ID. Enabling this feature does not impact user membership or access to a given instance. Access to a company in Procore is determined by a user's presence in the Directory tool, and their configured permissions within Procore. Auto-provisioning with SSO is not supported at this time.*