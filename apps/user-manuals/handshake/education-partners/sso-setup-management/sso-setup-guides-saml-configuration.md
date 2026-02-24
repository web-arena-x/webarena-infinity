# SSO Setup Guides: SAML Configuration

Source: https://support.joinhandshake.com/hc/en-us/articles/360012361513-SSO-Setup-Guides-SAML-Configuration

---

# Step 1. Download Handshake's Metadata

If you are on InCommon, you should already have our metadata (reference [here](http://md.incommon.org/InCommon/InCommon-metadata.xml). Use "save link as" to download InCommon reference).

If you are not on InCommon, you can download a copy [here](https://mdq.incommon.org/entities/https%3A%2F%2Fapp.joinhandshake.com%2Fsp).

# Step 2: Configure Your SAML Service

Handshake's entityID is: `https://app.joinhandshake.com/sp` Handshake's AssertionConsumerService Post URL is: `https://app.joinhandshake.com/saml_consume`

**Attribute or NameID Suggestions** RequestedAttribute: `FriendlyName="eduPersonPrincipalName"` Requested Format: `NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri"` **NOTE:**The attribute or NameID you specify should return a value matching the format of the auth\_identifier field from your student syncs. Also you should specify this value, **either** a NameID **OR** an attribute, in your Handshake SSO Preferences (after step 4 [HERE](sso-setup-guides-in-app-setup-and-testing.md)), ***but not both***.

**ADFS or Azure AD Configuration**

We've created a guide to configure your claim rules if you are using ADFS as your Identity Provider, which can be found [here](https://support.joinhandshake.com/hc/en-us/articles/360012404753). The main difference between these two Identity Providers and others we support is that you will want to ensure this setting is "un-checked" in your Handshake SSO Preferences page:

![mceclip0.png](https://support.joinhandshake.com/hc/article_attachments/1500018812622)

**You will need to leave this box unchecked (disabled) if you are using an active directory like ADFS, Azure AD or Okta.**

**If you are configuring an Azure AD SAML integration,** in Azure you will only need to enter the Entity ID and Reply URL shown above. Copy the App Federation Metadata URL and import it into the "Import" field of your SSO Preferences page in Handshake. You can leave the NameID Format blank for the purposes of testing(or if you know the format of the attribute you will be assigning as the "auth\_identifier" for students, use that), and ensure "Requested authentication context?" is un-checked before testing!

# Step 3: Login to Handshake to Setup SSO

Setting SSO up on Handshake is self-service! After your career services admin has added you to Handshake you can begin [SSO Setup and Testing](sso-setup-guides-in-app-setup-and-testing.md).

# More Questions?

Reach out to our Support Team.