# SSO Setup Guides: SAML Configuration: ADFS Claim Rules Guide/Example

Source: https://support.joinhandshake.com/hc/en-us/articles/360012404753-SSO-Setup-Guides-SAML-Configuration-ADFS-Claim-Rules-Guide-Example

---

**This guide is only an example of a proper setup, and some values may change based on your configuration.**

# Setup Claim Rules on Your SAML Server

Edit Claim Rules

[![](https://files.readme.io/c2a99e3-handshake_claims1.png)](https://files.readme.io/c2a99e3-handshake_claims1.png)

Edit Rule - Transform to Name ID

[![](https://files.readme.io/88001f5-handshake_claims4.png)](https://files.readme.io/88001f5-handshake_claims4.png)

Edit Rule - UPN

[![c:[Type == "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn"]
=> issue(Type = "urn:oid:1.3.6.1.4.1.5923.1.1.1.6", Value = c.Value, Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/attributename"] = "urn:oasis:names:tc:SAML:2.0:nameid-format:transient");](https://files.readme.io/460e8e0-handshake_claims2.png)](https://files.readme.io/460e8e0-handshake_claims2.png)

*c:[Type == "<http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn>"]*  
*=> issue(Type = "urn:oid:1.3.6.1.4.1.5923.1.1.1.6", Value = c.Value, Properties["<http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/attributename>"] = "urn:oasis:names:tc:SAML:2.0:nameid-format:transient");*

Edit Rule - E-mail Address from UPN

[![](https://files.readme.io/b7154cb-handshake_claims3.png)](https://files.readme.io/b7154cb-handshake_claims3.png)

Now go to your Handshake SSO Preferences and specify the matching attribute value:

[![http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress](https://files.readme.io/68a8098-sso-prefs-adfs.png)](https://files.readme.io/68a8098-sso-prefs-adfs.png)

***If following our steps above exactly, this will be:***

*<http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress>*

Make sure to de-select "Requested authentication context?" before testing as you are using ADFS (This is also found on your Handshake SSO Preferences page)

[![](https://files.readme.io/eb60801-adfs-uncheck.png)](https://files.readme.io/eb60801-adfs-uncheck.png)