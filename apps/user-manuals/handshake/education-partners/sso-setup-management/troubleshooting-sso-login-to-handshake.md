# Troubleshooting SSO Login to Handshake

Source: https://support.joinhandshake.com/hc/en-us/articles/360007797394-Troubleshooting-SSO-Login-to-Handshake

---

For a Career Services user or Student to successfully log in via SSO in Handshake, the account *must* have an **auth \_identifier** configured within the accounts settings — this is the only value used for SSO authorization and verification.

- Student accounts typically have an **auth \_identifier** populated on their accounts via the student data import.
  - *To learn more about importing student data in Handshake, refer to* [Importing Student Data](https://support.joinhandshake.com/hc/en-us/articles/233086688).
- Career Services users can have an **auth \_identifier** manually entered on their profiles at any time.

## Possible error messages

There's a couple error messages that can be received in Handshake when a user attempts to log in via SSO. Below are the most common error messages, with a reasoning and resolution to troubleshoot each.

- [Successfully logged into SSO, but couldn't find your account](#h_01G9FPFHZMNWSGHD21PJ10DRN5)
- [Communication issue with school - Error code 1 and 2](#h_01G9FPFX1AXFZBZZWN9GYPXGDM)
- [Authorization timeout - Error code 6](#h_01G9FQ57288NPVWPJ2NM8MJMSP)
- [Failed to validate the SAML/Invalid Signature - Error code 4](#h_01G9FQPWRPJYJWP81H110B0KN4)

*For more information on error codes, refer to* [SSO Setup Guides: Login Error Codes by SSO Type](https://support.joinhandshake.com/hc/en-us/articles/360012284814)

### Successfully logged into SSO, but couldn't find your account

"You successfully logged in to your Single Sign On portal but we could not find your Handshake account. You either don't have an account yet or your account is not configured correctly. Please use the options below to configure your account to log in."

![mceclip1.png](https://support.joinhandshake.com/hc/article_attachments/26001362628119)

This message may occur if the **auth \_identifier** field is blank or invalid on the users account. Confirm if the correct **auth \_identifier**has been added to the users account in Handshake.

*If a student creates their account, before being imported into Handshake, the* **auth \_identifier** *will be blank.*

If most or all of your Career Services users and students are receiving this error, there's likely a configuration issue with SSO between your institution and Handshake. We recommend contacting our Support team and including any IT or networking contacts at your institution in the request.

For more information on contacting Handshakes Tech Support team, refer to [University Technical Support Guidelines and Resources](https://support.joinhandshake.com/hc/en-us/articles/360000869147).

### Communication issue with school - Error code 1 and 2

"There was an issue communicating with your school. Try again later, or sign in using your Handshake email and password. Error code 2."

![mceclip2.png](https://support.joinhandshake.com/hc/article_attachments/26001362630039)

This error can occur if any recent changes were made by your IT team. In some cases, a change that was made can be rolled back until your IT team can work with Handshake Support to align with the updates.

If you're a career services user, connect with your IT team to confirm if any changes or updates were made.

A few things that you may share with them:

- A list of email addresses and accounts that cannot log in
- Screenshots of error messages
- This article (with the steps to resolve outlines below)

**Note**: if there is an SSO outage, we recommend users login to Handshake using their Handshake credentials until the issue is resolved. If a user has not set up their Handshake credentials, they'll be taken through an email verification process and setup.

#### IT/SSO team Troubleshooting Steps

**If a small subset of users:**

1. Check your Handshake SSO Preferences, and verify that the 'Host' you have set for LDAP users is correct.
2. If using a hostname there, did you have every IP address associated with that host unblocked by Handshake? Sporadic errors here typically indicate there's an additional/rotating or new IP being used.
3. Did you unblock *both* of Handshake's LDAP IP's, or just one?  Both are required or you'll have sporadic errors like this.

**If all users:**

1. Check your Handshake SSO Preferences, and verify that the LDAP bind username and password are correct.
2. Check that the 'Host' you've set is correct, and that you've had Handshake unblock *all* IP's associated with this host.
3. Make sure you've unblocked Handshake's IP's. For more information on which IP's need to be unblocked, refer to [SSO Setup Guides: LDAP Configuration](https://support.joinhandshake.com/hc/en-us/articles/360012362193).

### Authorization timeout - Error code 6

This error can occur after a large amount of failed logins within a short period (lockout period). This lockout period isn't set/enforced by Handshake, but rather your local LDAP server, which causes an authorization timeout when trying to reach the LDAP server. It typically goes away after a set period of 15 - 30 minutes.

#### IT/SSO team Troubleshooting Steps

**If a small subset of users:**

1. Verify that you have adequate auth timeouts set for initial login, as heavy load may create a delay in auth, and timeouts, for large amounts of users.
2. Verify that your LDAP Base DN and Filter are specific enough to prevent timeouts in your Handshake SSO Preferences.
3. Verify that users reporting the issue are in the correct OU based on your Base DN.

**If all users:**

1. Verify that you have adequate local LDAP auth timeout set for initial login. Try increasing this by a few seconds.
2. Verify that your LDAP server and connection aren't having localized issues or outages.
3. Wait 30 minutes to an hour and verify that this persists.

![mceclip0.png](https://support.joinhandshake.com/hc/article_attachments/26001362631191)

### Failed to Validate the SAML/Invalid Signature - Error code 4

"Error 4: Failed to validate the SAML response. Errors:Invalid Signature on SAML Response"

This error indicates that the returned signature in your SAML response during authorization didn't match the **Fingerprint** (SHA-1 hash of your x.509 cert) value in your Handshake SSO Preferences.

This error commonly occurs**:**

- During initial setup and testing, if the wrong **Fingerprint** value was entered or left blank.
- Once or twice a year after launch, if you change or rotate your x.509 signing certificate, without updating the Fingerprint in Handshake SSO Preferences.

To fix this**:**

1. Login to your Handshake account
2. Navigate to your School Settings -> SSO Preferences section.
3. Scroll to the very bottom and update the 'Fingerprint' field with the new value. If you have your current Metadata URL you can import it in the indicated Metadata URL field and we will calculate the fingerprint fr you.
4. Click the green button **Update SSO Preferences** to save.

![mceclip0.png](https://support.joinhandshake.com/hc/article_attachments/26001385393943)

### Fields You Can Update Within the SSO Settings

- The fingerprint value when you roll over to a new x.509 certificate (SAML)
- The base URL if moving to a new CAS server (CAS)
- The bind username/password, BaseDN, or Search Filters for LDAPS
  - **Note**: if you're changing LDAPS IP's, we do need to unblock these on the backend **prior** to the change.  [SSO Setup Guides: LDAP Configuration](https://support.joinhandshake.com/hc/en-us/articles/360012362193).

### Additional Resources

- [SSO Setup Guides: In-App Setup and Testing](https://support.joinhandshake.com/hc/en-us/articles/360012363913)
- [SSO Setup Guides: SAML Configuration](sso-setup-guides-saml-configuration.md)
- [SSO Setup Guides: CAS Configuration](sso-setup-guides-cas-configuration.md)
- [SSO Setup Guides: LDAP Configuration](sso-setup-guides-ldap-configuration.md)