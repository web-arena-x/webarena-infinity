# SSO Setup Guides: Externally Embedding Your Handshake Login URL

Source: https://support.joinhandshake.com/hc/en-us/articles/360012403913-SSO-Setup-Guides-Externally-Embedding-Your-Handshake-Login-URL

---

**CURRENTLY *ONLY* FOR SAML SSO SETUPS (and some CAS configurations)**

If you'd like to direct students to login to Handshake via SSO from your institution's website or portal, you can do so by requesting a "Special Auth URL" from Handshake Support.

This URL will look something like this (we will replace '84' with your school ID to form the correct URL):

```
https://app.joinhandshake.com/auth?auth=84
```

This URL creates a redirect to your institution's identity provider, which is equivalent to students selecting 'login with SSO' from your school-specific Handshake login page (essentially saving them a step when logging into Handshake from your institution's external website):

[![](https://files.readme.io/b0b0698-login-with-sso-button.png)](https://files.readme.io/b0b0698-login-with-sso-button.png)

This URL will look something like: `https://idp.stanford.edu/idp/profile/SAML2/Redirect/SSO?SAMLRequest=`

**Uses:** This URL is typically used in either a button or hyperlink off of your school website, or via announcements or invite emails so that students are directed straight to SSO to log in. Note that students can always go to app.joinhandshake.com and login with Handshake email and password if they have any issues with this link or logging in via SSO.