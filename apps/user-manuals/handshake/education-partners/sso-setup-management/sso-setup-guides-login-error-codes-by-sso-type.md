# SSO Setup Guides: Login Error Codes by SSO Type

Source: https://support.joinhandshake.com/hc/en-us/articles/360012284814-SSO-Setup-Guides-Login-Error-Codes-by-SSO-Type

---

**NOTE**: If your Handshake SSO setup was previously running without issue, you can also view the bottom of [this article](https://support.joinhandshake.com/hc/en-us/articles/360007797394) for additional reference, common issues, and next steps!

# SAML Error Codes

| | | | |
| --- | --- | --- | --- |
| **Error Code** | **Error Meaning** | **Test Mode Message** | **Next Steps** |
| 1 | SAML Response was somehow not included in the URL | Sorry, we couldn't find your school's system from your login. Please contact Support@"" Err 1 | Check your local SAML configuration and ensure that it matches your settings under Handshake SSO Preferences |
| 2 | SAML Validation (IdP does not know how to process the request as configured) – incorrect # or unsigned issuers in response or an incorrect nameID format specified | Sorry, we couldn't find your school's system from your login. Please contact Support@"" Err 2 | Verify your NameID format setting in Handshake SSO Preferences matches your local SAML configuration. If returning an attribute (such as urn:oid:1.3.6.1.4.1.5923.1.1.1.6 ), make sure you select "Attribute" for "Identifier Lookup Mode" and populate with the correct value. |
| 3 | No auth\_information was found matching the saml\_issuer. Seems likely the config has an incorrect value for that field | Sorry, we couldn't find your school's system from your login. Please contact Support@"" Err 3 | Verify that you have the correct "Issuer" value in Handshake SSO Preferences. If that is correct, make sure you don't have the NameID Format field populated if you selected "Attribute" for "Identifier Lookup Mode". |
| 4 | Failed to validate the SAML response This is likely due to a bad fingerprint/x509 cert. Please check your fingerprint and update accordingly. | Failed to validate the SAML response. Error: <error> | Verify that your "Fingerprint" value in Handshake SSO Preferences matches the x509 cert you are using. If this cert has changed at your local SAML setup, it must be updated in Handshake as well. |
| 5 | The saml response attributes don't contain an attribute matching the configured saml\_name\_identifier. Guessing the config most likely has an incorrect value for that field | Failed to find the expected attribute in the SAML Response. Expected #auth attribute identifer, Found these attributes in the response: <list parsed attributes found in response> | Check the NameID or attribute values you have in your Handshake SSO Preferences, and ensure that they match your local SAML configuration. |
| 6 | Failed to get successful response | Failed to get a successful SAML response. Got: <responder status> | Check your local SAML SSO setup and verify you are sending a valid response. |
| 7 | NameId not found and no saml\_name\_identifier is configured | NameId not found in the response. Check your Name ID Format setting, or configure SAML use an attribute instead | Check your NameID Format setting in Handshake SSO Preferences. If not using a NameID, switch "Identifier Lookup Mode" to Attribute and fill in the attribute value. |

- **Note**: Depending on the Identity Provider you are utilizing for SSO, you may receive the following error when attempting to log in (using SAML auth): 
 ![mceclip0.png](https://support.joinhandshake.com/hc/article_attachments/25995551492119)

This is related to your Identity Provider's '*requested authentication context*' which can be enabled/disabled under your SSO Preferences page: 
![](/attachments/token/mC2ZiiPnzrfmJQEIkoN5MPmZS/?name=inline-1485382199.png)

You'll need to disable this setting if you are using ADFS or Azure AD, but this should typically be enabled for most other Identity Providers.

# CAS Error Codes

| | | | |
| --- | --- | --- | --- |
| **Error Code** | **Error Meaning** | **Test Mode Message** | **Next steps** |
| 1 | School\_id param is missing or doesn't map to a school | Sorry, we had trouble finding your school. Please contact support | Not common, Handshake support must correct at this time. Please open support ticket. |
| 2 | validate\_service\_ticket through an exception | We failed to validate your ticket: #{exception class and message}. Please check your CAS Base URL and retry. | Update your CAS Base URL in Handshake SSO Preferences. This must match exact URL for your local CAS setup. |
| 3 | service\_ticket.is\_valid? returned false | We failed to validate your ticket. Code: #{failure\_code}. Message: #{failure\_message} | Check your local CAS configuration and test again. This indicates that we are unable to authenticate with your server. |

# 

# LDAP Error Codes

| | | | |
| --- | --- | --- | --- |
| **Error Code** | **Error Meaning** | **Test Mode Message** | **Next Steps** |
| 1 | Base bind method returned false: <https://github.com/ruby-ldap/ruby-net-ldap/blob/master/lib/net/ldap.rb#L813-L814> | Failed to connect to LDAP server: #{get\_operation\_result} | Verify your bind settings (host IP and credentials) in Handshake SSO Preferences. Make sure you also unblocked both of our IP's and have requested for us to unblock yours (see LDAP Setup Guide). If verified, try putting the DC value in front of the username with a slash between.(Example: DC=abc, username could be "abc/*username*") |
| 2 | Various exceptions thrown from base bind; mostly connection issues | Failed to connect to LDAP server: #{exception class + message} | Verify your bind settings (host IP and credentials) in Handshake SSO Preferences. Make sure you also unblocked both of our IP's and have requested for us to unblock yours (see LDAP Setup Guide). |
| 3 | Search failed with an error: <https://github.com/ruby-ldap/ruby-net-ldap/blob/master/lib/net/ldap.rb#L750-L751> | LDAP user search failed: #{get\_operation\_result} | Check your Username value in Handshake SSO Preferences. This must match your local LDAP configuration in order to auth with LDAP server before Base DN/Filter search. |
| 4 | Search found multiple users | LDAP user search found multiple users with the given username. | Check your Filter value in Handshake SSO preferences, and make sure that identifier being used is unique for each student. Adjust Base DN if looking in the wrong location. |
| 5 | Various exceptions thrown from client bind; mostly connection issues | LDAP user login failed: #{exception class + message} | Make sure you have unblocked both of our IP's and have requested for us to unblock yours (see LDAP Setup Guide). Also test your bind settings (Host IP, server username /password) outside of Handshake to track any local connection or configuration issues. |
| 6 | Likely cause is that auth took longer than client timeout | Authentication timed out. Is the LDAP server up and responding? | If only for a couple users, try again after a few moments as timeouts can be common with LDAP. If a large number of users, please have IT check health of local LDAP server. We usually see this if school's local LDAP server is under maintenance or having intermittent connection issues. |
| 7 | Token cookie not present | Background auth token not present | Not common, check your local LDAP server config. |
| 8 | Search returned an empty set | LDAP user search found no users; if this user should exist, check the filter setting on your Handshake SSO Preferences. | Student not found at the University based on username entered, so likely need to verify they are using correct ID format. If occurring for all users, adjust the Base DN and/or Filter setting in your Handshake SSO Preferences so that it looks in the correct place. |
| 9 | Client bind method returned false: <https://github.com/ruby-ldap/ruby-net-ldap/blob/master/lib/net/ldap.rb#L813-L814> | LDAP user login failed: #{get\_operation\_result} | Student was found at the school but their password was invalid. Please ensure they are using their local University/LDAP-managed password. |