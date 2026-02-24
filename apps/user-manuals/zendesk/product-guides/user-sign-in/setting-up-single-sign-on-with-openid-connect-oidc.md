# Setting up single sign-on with OpenID Connect (OIDC)

Source: https://support.zendesk.com/hc/en-us/articles/7957465432474-Setting-up-single-sign-on-with-OpenID-Connect-OIDC

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Set up single sign-on (SSO) with OpenID Connect (OIDC) to simplify user authentication through a central identity provider like Google or Okta. This enhances security by using ID tokens for identity verification. Key steps include creating an OIDC SSO configuration, assigning it to users, and managing user data post-implementation. Remember to configure attributes and turn off password notifications for a seamless transition.

Location: Admin Center > Account > Security > Single sign-on

[OpenID Connect (OIDC)](https://openid.net/developers/how-connect-works/) is an authentication protocol built on the OAuth 2.0 framework. It enables developers to authenticate users and obtain basic profile information in a secure and standardized manner. OIDC uses ID tokens to verify the identity of users based on the authentication performed by an authorization server, simplifying the process of managing user identities and enhancing the security of interactions between users and applications.

OIDC single sign-on (SSO) with Zendesk streamlines the authentication process by allowing users to sign in using a central identity provider (IdP) like Google or Okta rather than managing separate login credentials for Zendesk.

This article contains the following topics:

- [How OIDC SSO for Zendesk works](#topic_dcx_h5m_pcc)
- [Important considerations](#topic_e5n_1ym_pcc)
- [Creating the OIDC SSO configuration](#topic_j1d_fym_pcc)
- [Assigning OIDC SSO to users](#topic_wxq_hym_pcc)
- [Managing users in Zendesk after turning on OIDC SSO](#topic_wb2_jym_pcc)
- [Switching authentication methods](#topic_m2g_lym_pcc)
- [Attributes supported by Zendesk](#topic_d1r_523_l3)

Related articles:

- [Managing single sign-on (SSO)
 configurations](https://support.zendesk.com/hc/en-us/articles/4408882188570)
- [Single sign-on (SSO) options in Zendesk](https://support.zendesk.com/hc/en-us/articles/4408883587226)
- [Giving users different ways to sign into Zendesk](https://support.zendesk.com/hc/en-us/articles/5380943678106)
- [Accessing your Zendesk account when your SSO service is down](https://support.zendesk.com/hc/en-us/articles/4408882128666)

## How OIDC SSO for Zendesk works

OIDC SSO allows a user to authenticate with an IdP using a standard protocol. Once authenticated, the IdP issues an ID token that is used to verify the user's identity and access permissions.

Steps of the Zendesk SSO process with OIDC:

1. An unauthenticated user navigates to your Zendesk Support URL. Example:
   **https://*yoursubdomain*.zendesk.com/**.
2. Depending on your sign-in workflow, the user clicks a button on the Zendesk sign-in page to sign in with SSO, directing them to your IdP, or is automatically redirected to your IdP to sign in.
3. After the user authenticates successfully, the IdP generates an ID token that contains user-specific information.
4. Zendesk receives the token at the callback URL:
   **https://*yoursubdomain*.zendesk.com/access/oidc/callback**.
   The token is validated against the configuration details shared between Zendesk and the IdP.
5. After successful validation, Zendesk grants the user access, leveraging the trust established by the IdP.

## Important considerations

- It's not possible to use OIDC to authenticate users in messaging.
- Zendesk requires all users to have an email address associated with their profile, but your users might try to sign in without having an email address. In this scenario, to prevent a loop where the authentication fails because of a missing email address, Zendesk will display an error message.
- RSA256 is the default JWT decoding algorithm. To use another algorithm (such as ES256), specify it in your OpenID provider discovery endpoint.
- If you want to use OIDC with Entra, a few specific requirements need to be configured.
 - The Authentication mode must be **PKCE**.
 - Add the callback URL on the Entra OIDC PKCE configuration form under **Mobile and desktop applications - Redirect URIs**.

## Creating the OIDC SSO configuration

Admins can enable OIDC single sign-on only for end users, only for team members (including light agents and contributors), or for both groups. You can create multiple OIDC SSO configurations.

The information needed for this step must come from the IdP you're using, so make sure your IdP is set up before you start. You may have to obtain the information from your company's IT team.

**To create the OIDC SSO configuration in Zendesk**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > Single sign-on**.
2. Click **Create SSO configuration**, then select **OpenID Connect**.
3. Enter a unique **Configuration name**.
4. (Optional) For **IP ranges**, enter a list of IP ranges if you want to redirect users to the appropriate sign-in option.

   Users making requests from the specified IP ranges are routed to the remote OIDC authentication sign-in form. Users making requests from IP addresses outside the ranges are routed to the standard Zendesk sign-in form.
   Don't specify a range if you want all users to be redirected to the remote authentication sign-in form.
5. In the **Client ID** field, enter the Client ID given to you by your IdP.
6. Enter the **Client secret** if your IdP requires it.

   Because the client secret must be kept confidential, you won't see the full secret again after you save the configuration. If you need to rotate the secret, edit this SSO configuration to enter and save a new secret.
7. In the **Scopes** field, list all the scopes you want to request from the IdP. At a minimum, you must add `openid` and `email`. Scopes are separated with spaces and no commas.
   For example: `openid email phone`

   Supported scopes within the OIDC standard include `openid`, `profile`, `email`, `address`, and `phone`. You can also list any custom scopes that have been configured in your IdP.

   Unaccepted scopes that your IdP rejects will cause sign-in to fail with the error `Unknown error during sign-in`.
   Zendesk doesn't validate any of the scopes in this field.
8. Select **Turn on auto discovery** if you only want to provide the Issuer URL. When this is turned on, Zendesk will automatically extract the configuration details from the OIDC Configuration Document. You only need to provide the Issuer URL and Authentication Mode.
9. Enter the required URLs.

   Check if your IdP requires a specific format for the URLs you are using. If the URLs are incorrectly formatted and rejected by your IdP, you may encounter a sign-in failure accompanied by the error message `Unknown error during sign-in`. Zendesk doesn't validate the URLs in these fields.

   - **Issuer URL** (also known as the issuer identifier): A unique identifier for the IdP that performs user authentication and delivers the ID tokens.
   - **UserInfo URL**: An endpoint provided by the IdP that, when accessed with a valid access token, returns attributes about the authenticated user.
   - **JWKs URL**: An endpoint provided by the IdP that allows Zendesk to retrieve the provider's public keys. These keys are used to verify the signature of JSON web tokens (JWTs) that the IdP issues.
   - **Authorization URL**: When users access this URL, they are prompted to sign in and consent to the requested scopes.
   - **Access URL** (also known as the token endpoint URL): Used to exchange an authorization code, client ID, and client secret for an access token.
10. Choose an **Authentication Mode**. **PKCE** is recommended.
    - Using **PKCE** to obtain the access token is best for public clients, like mobile or Javascript web apps, as it uses dynamically generated keys to prevent unauthorized token exchange without needing a client secret.
    - Choose **Authorization code flow** if you want the access token to be obtained using Authorization code flow. This is best for server-based apps with secure back-end storage that rely on a client secret to obtain tokens.
11. Select **Show button when users sign in** if you [let users choose how they sign in](https://support.zendesk.com/hc/en-us/articles/5380943678106)
    and want this configuration to be an option they can choose from. If you select this option, you also need [name the button](https://support.zendesk.com/hc/en-us/articles/4408882188570#topic_rqg_yw4_2yb) that will be shown on the Zendesk sign-in page.

    Clear this box if your users only sign in using an identity provider because they don't use the Zendesk sign-in page.
12. Click **Save**.

    By default, enterprise SSO configurations are inactive.
    You must [Assign OIDC SSO to users](#topic_wxq_hym_pcc) to activate it.

## Assigning OIDC SSO to users

After creating your OIDC SSO configuration, you must activate it by assigning it to end users, team members, or both.

**To assign an SSO configuration to team members or end users**

1. Open the Security settings for team members or end users.
   - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
     **Account** in the sidebar, then select **Security > Team member authentication**.
   - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
     **Account** in the sidebar, then select **Security > End user authentication**.
2. Select **External authentication** to show the authentication options.
3. Select the name(s) of the SSO configuration(s) you want to use.

   Single sign-on might not cover all use cases, so Zendesk authentication remains active by default.
4. Select how you'd like to allow users to sign in.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_security_choose-sign_in.png)

   **Let them choose** allows users to sign in using any active authentication method. See [Giving users different ways to sign into Zendesk](https://support.zendesk.com/hc/en-us/articles/5380943678106).

   **Redirect to SSO** only allows users to authenticate using the [primary SSO configuration](https://support.zendesk.com/hc/en-us/articles/4408882188570#topic_c55_3sf_vsb). Users don’t see additional sign-in options, even if those authentication options are active. When you select **Redirect to SSO**, the **Primary SSO** field appears for you to select the primary SSO configuration.
5. Click **Save**.

## Managing users in Zendesk after turning on OIDC SSO

After enabling OIDC single sign-on in Zendesk, changes made to users outside Zendesk don't automatically sync to your Zendesk account. Users are updated in Zendesk at the point of authentication. For example, if a user is added to your internal system, the user is added to your Zendesk account when they sign in to Zendesk. If a user is deleted from your internal system, the user will no longer be able to sign in to Zendesk. However, their account will still exist in Zendesk.

By default, the only user data stored in Zendesk when single sign-on is enabled is the user's name and email address. Zendesk does not store passwords. As a result, you should turn off any automated email notifications from Zendesk about passwords.

### Turning off password notification emails from Zendesk

A Zendesk user profile is created for any new user who accesses your Zendesk account through SAML, JWT, or OpenID Connect (OIDC) single sign-on.
Because users are authenticated through an IdP with a non-Zendesk password, the profile is created without a password because they don't need to sign in to Zendesk directly.

Because new users who sign in to Zendesk through SSO are verified through an IdP, they don't receive email notifications to verify their account.
However, it is still recommended to turn off these automated email notifications to prevent them from being sent if the IdP does not successfully verify the user. In the case of SSO, user verification must always occur through the IdP.

**To turn off password notification emails**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > End users**.
2. In the **Account emails** section, deselect **Also send a welcome email when a new user is created by an agent or administrator**.
3. In **Allow users to change their password**, deselect this option.

## Switching authentication methods

If you use a third-party SSO method to create and authenticate users in Zendesk and then switch to Zendesk authentication, these users will not have a password available for login. To gain access, ask these users to reset their passwords from the Zendesk sign-in page.

## Attributes supported by Zendesk

Zendesk supports standard and custom OIDC attributes.

- *Standard* attributes are predefined, widely accepted attributes specified by the OIDC protocol and ensure a uniform understanding of user identity across different systems. Zendesk supports the following standard attributes:
 - `sub`
 - `email`
 - `email_verified`
 - `locale`
 - `phone number` (maps to Zendesk user attribute `phone`)
 - `photo` (maps to Zendesk user attribute `remote_photo_url`)
 - `preferred_username` (maps to Zendesk user attribute `alias`)
 - `zoneinfo` (maps to Zendesk user attribute `time_zone`)
- *Custom* attributes are additional attributes that extend the standard set to meet Zendesk-specific requirements. You can pass custom attributes in the ID token or userinfo claims.

The table below is a complete list of standard and custom attributes supported by Zendesk. Attribute names are case sensitive, so you must match the exact casing shown in the table below.

| Attribute name | Description |
| --- | --- |
| name | The user's full name in displayable form including all name parts, possibly including titles and suffixes, ordered according to the end user's locale and preferences. If no name is present, this defaults to the user's primary email address. |
| email | The user's primary email address. |
| email\_verified | True if the user's email address has been verified; otherwise false. When this attribute value is true, this means that the OpenID Provider took affirmative steps to ensure that this email address was controlled by the user at the time the verification was performed. When you use SSO at Zendesk, it's your responsibility to verify your user's email addresses. |
| organization | Name or ID of an organization to add the user to. The external\_id attribute of an organization is not supported. If the organization doesn't exist in Zendesk, it won't be created. The user will still be created, but they won't be added to any organization. If [**Allow users to belong to multiple organizations**](https://support.zendesk.com/hc/en-us/articles/4408838140314) is turned on, additional organizations append the original organization and are considered secondary organizations. This does not delete the existing memberships. If you'd like to pass multiple organization names at the same time, use the **organizations** attribute instead. Using the organizations attribute overwrites the existing list of organizations. The organization names must be passed in a string, separated by commas. |
| organization\_id | The organization's [external ID](https://developer.zendesk.com/api-reference/ticketing/organizations/organizations/) in the Zendesk API. If both organization and organization\_id are supplied, organization is ignored. If the organization doesn't exist in Zendesk, it won't be created. The user will still be created, but they won't be added to any organization. If [**Allow users to belong to multiple organizations**](https://support.zendesk.com/hc/en-us/articles/4408838140314) is turned on, additional organizations append the original organization, and are considered secondary organizations. This does not delete the existing memberships. If you'd like to pass multiple organization IDs at the same time, use the **organization\_ids** attribute instead. Using the organization\_ids attribute overwrites the existing list of organizations. The organization IDs must be passed in a string, separated by commas. |
| phone | A phone number, specified as a string. |
| tags | Tags to set on the user. The tags will replace any other tags that may exist in the user's profile. |
| remote\_photo\_url | URL for a photo to set on the user profile. |
| locale (for agents) locale\_id (for end users) | The locale in Zendesk, specified as a number. To get a list of valid numbers, see [Locales](https://developer.zendesk.com/rest_api/docs/support/locales) in the API docs. |
| zendesk\_role | The user's role. Can be set to **end-user** , **agent**, or **admin**. If you don't pass a zendesk\_role, then Zendesk creates the user as an end user, unless they already exist with another role. |
| custom\_role\_id | Applicable only if the value of the **role** attribute above is **agent**. You can get the IDs of your custom roles with the [Custom Roles API](https://developer.zendesk.com/rest_api/docs/support/custom_roles). |
| external\_id | A user ID from your system if your users are identified by something other than an email address or if their email addresses are subject to change. Specified as a string. |
| user\_field\_<key> | A value for a custom user field in Zendesk Support. See [Adding custom fields to users](https://support.zendesk.com/hc/en-us/articles/4408822051866). The <key> is the field key assigned to the custom user field in Zendesk Support. Example: `user_field_employee_number` where `employee_number` is the field key in Zendesk. Sending a null value or an empty string in the attribute value will remove any custom field value set in Zendesk Support. |