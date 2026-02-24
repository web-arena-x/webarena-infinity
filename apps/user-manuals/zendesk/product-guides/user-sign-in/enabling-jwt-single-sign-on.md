# Enabling JWT single sign-on

Source: https://support.zendesk.com/hc/en-us/articles/4408845838874-Enabling-JWT-single-sign-on

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location:  Admin Center > Account > Security > Single sign-on

Single sign-on is a mechanism that allows you to authenticate users in your systems and subsequently tell Zendesk that the user has been authenticated. If you use single sign-on with JSON Web Token (JWT), a user is automatically verified with the identity provider when they sign in. The user is then allowed to access Zendesk without being prompted to enter separate sign-in credentials.

As a Zendesk admin, your role consists of enabling the SSO options. This article describes how to enable multiple JWT single sign-on configurations that can be used to authenticate team members (admins and agents, including light agents and contributors), end users, or both.

At the core of single sign-on is a security mechanism that allows Zendesk to trust the sign-in requests it gets from your systems. Zendesk only grants access to the users who have been authenticated by you. Zendesk SSO relies on JWT to secure the exchange of user authentication data.

Important: When you use JWT- or SAML-based SSO, you are responsible for verifying your users' identities, including their email addresses. If you don't verify your users and their email addresses, your account is at risk of unauthorized access, and Zendesk cannot guarantee or warrant the security of your account.

This article contains the following sections:

- [How JWT SSO for Zendesk works](#topic_xml_kdj_zj)
- [Requirements for enabling JWT SSO](#topic_u54_wc3_z2b)
- [Enabling JWT SSO](#topic_gds_ydj_zj)
- [Assigning JWT SSO to users](#topic_wgb_zsc_jhb)
- [Managing users in Zendesk after enabling JWT SSO](#topic_tbs_zmb_2lb)
- [Generating a new shared secret](#topic_bjn_hfd_vhb)
- [Switching authentication methods](#topic_qn4_tnb_2lb)
- [Additional information about JWT](#topic_15m_mfj_zj)

The IT team in a company is usually responsible for setting up and managing the company's JWT authentication system. Their role is to implement SSO for Zendesk on the system. Refer the team to the following topic in this article:

- [Technical implementation worksheet](#topic_wkt_3zg_3fb)

Related articles:

- [Single sign-on (SSO) options in Zendesk](https://support.zendesk.com/hc/en-us/articles/4408883587226)
- [Giving users different ways to sign into Zendesk](https://support.zendesk.com/hc/en-us/articles/5380943678106)
- [Accessing your Zendesk account when your SSO service is down](https://support.zendesk.com/hc/en-us/articles/4408882128666)

## How JWT SSO for Zendesk works

Once you enable SSO, sign-in requests are routed to a sign-in page external to Zendesk Support.

Steps of the JWT SSO authentication process:

1. An unauthenticated user navigates to your Zendesk Support URL. Example: **https://*yoursubdomain*.zendesk.com/**.
2. The Zendesk SSO mechanism recognizes that SSO is enabled and that the user is not authenticated.
3. Zendesk tries to determine whether the unauthenticated user is an end user or team member and redirects the user to your organization's appropriate remote sign-in page. Example: **https://*mycompany*.com/zendesk/sso**.
4. A script on the remote server authenticates the user using your organization's proprietary sign-in process.
5. The authentication system builds a JWT request that contains the relevant user data.
6. The authentication system redirects the user to the following Zendesk endpoint with the JWT payload:

   **https://*yoursubdomain*.zendesk.com/access/jwt**
7. Zendesk verifies the token and then parses the user details from the JWT payload and grants the user a session.

As you can see, this process relies on browser redirects and passing signed messages using JWT. The redirects happen entirely in the browser and there is no direct connection between Zendesk and your systems, so you can keep your authentication scripts safely behind your corporate firewall.

## Requirements for enabling JWT SSO

Meet with the team in your company responsible for the JWT authentication system (usually the IT team) to make sure that Zendesk-bound traffic is over HTTPS, not HTTP.

You'll need the following information to configure a JWT SSO method in Zendesk. Your IT team should be able to provide this to you.

- The remote login URL where Zendesk users should be redirected when they attempt to access Zendesk
- (Optional) The remote logout URL where Zendesk can redirect users after they sign out of Zendesk
- (Optional) A list of IP ranges to redirect users to the appropriate sign-in option. Users making requests from the specified IP ranges are routed to the remote JWT authentication sign-in form. Users making requests from IP addresses outside the ranges are routed to the normal Zendesk sign-in form. If you don't specify a range, all users are redirected to the remote authentication sign-in form.

The IT team may require additional information from Zendesk to configure the JWT implementation. Refer them to the [Technical implementation worksheet](#topic_wkt_3zg_3fb) in this article.

After you've confirmed that you meet the requirements and have all of the necessary information, you're ready to [enable JWT SSO](#topic_gds_ydj_zj).

## Enabling JWT SSO

Admins can enable JWT single sign-on only for end users, only for team members (including light agents and contributors), or for both groups. You can create multiple JWT SSO configurations. Before you start, obtain the required information from your company's IT team. See [Requirements for enabling JWT SSO](#topic_u54_wc3_z2b).

**To enable JWT single sign-on**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png) **Account** in the sidebar, then select **Security > Single sign-on**.
2. Click **Create SSO configuration** then select **JSON Web Token**.
3. Enter a unique **Configuration name**.
4. For **Remote Login URL**, enter the URL where your users should be redirected when they attempt to access your Zendesk URL.

   Zendesk automatically adds a **brand\_id** parameter to the URL. This is the Zendesk Support brand the user was on when they attempted to sign in.
5. (Optional) For **Remote Logout URL**, a logout URL where users should be redirected after they sign out of Zendesk.

   Zendesk automatically adds **email**, **external\_id**, and **brand\_id** parameters to the logout URL. If you prefer not to have email and external id information in the URL, specify blank parameters in the logout URL. Example:

   **https://www.xyz.com/user/signout/?email=&external\_id=**

   Note: If you're using an Ember.js application, you must amend the logout URL to use blank parameters before the hash. For example, `https://somedomain.com/?brand_id=&return_to=&email=#/zendesk-login/`.
6. (Optional) For **IP ranges**, enter a list of IP ranges if you want to redirect users to the appropriate sign-in option.

   Users making requests from the specified IP ranges are routed to the JWT authentication sign-in form. Users making requests from IP addresses outside the ranges are routed to the normal Zendesk sign-in form. Don't specify a range if you want all users to be redirected to the JWT authentication sign-in form.
7. If you use external IDs for your users, you can update these in Zendesk Support by selecting **On** for **Update of external ids?**.
8. Provide the **Shared secret** to your IT team. They'll need it for their JWT implementation.

   Important: Keep the shared secret safe. If it's compromised, all the data in your Support account is at risk.
9. Select **Show button when users sign in** to add a **Continue with SSO** button to the Zendesk sign-in page.

   You can customize the button label by entering a value in the **Button name** field. Custom button labels are useful if you add multiple SSO buttons to the sign-in page. See [Adding "Continue with SSO" buttons to the Zendesk sign-in page](https://support.zendesk.com/hc/en-us/articles/4408882188570#topic_rqg_yw4_2yb) for more information.
10. Click **Save**.

By default, enterprise SSO configurations are inactive. You must [assign the SSO configuration to users](#topic_wgb_zsc_jhb) to activate it.

## Assigning JWT SSO to users

After creating your JWT SSO configuration, you must activate it by assigning it to end users, team members, or both.

**To assign an SSO configuration to team members or end users**

1. Open the Security settings for team members or end users.
   - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png) **Account** in the sidebar, then select **Security > Team member authentication**.
   - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png) **Account** in the sidebar, then select **Security > End user authentication**.
2. Select **External authentication** to show the authentication options.
3. Select the name(s) of the SSO configuration(s) you want to use.

   Single sign-on might not cover all use cases, so Zendesk authentication remains active by default.
4. Select how you'd like to allow users to sign in.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_security_choose-sign_in.png)

   **Let them choose** allows users to sign in using any active authentication method. See [Giving users different ways to sign into Zendesk](https://support.zendesk.com/hc/en-us/articles/5380943678106).

   **Redirect to SSO** only allows users to authenticate using the [primary SSO configuration](https://support.zendesk.com/hc/en-us/articles/4408882188570#topic_c55_3sf_vsb). Users don’t see additional sign-in options, even if those authentication options are active. When you select **Redirect to SSO**, the **Primary SSO** field appears for you to select the primary SSO configuration.
5. Click **Save**.

## Managing users in Zendesk after enabling JWT SSO

After enabling JWT single sign-on in Zendesk, changes made to users outside Zendesk don't automatically sync to your Zendesk account. Users are updated in Zendesk at the point of authentication. For example, if a user is added to your internal system, the user is added to your Zendesk account when they sign in to Zendesk. If a user is deleted from your internal system, the user will no longer be able to sign in to Zendesk. However, their account will still exist in Zendesk.

By default, the only user data stored in Zendesk when single sign-on is enabled is the user's name and email address. Zendesk does not store passwords. As a result, you should turn off any automated email notifications from Zendesk about passwords.

To provide a better customer experience, you might want to store more than just the user's name and email address in Zendesk. You can do this using [additional JWT attributes](#topic_otw_jfh_3fb).

### Turning off password notification emails from Zendesk

A Zendesk user profile is created for any new user who accesses your Zendesk account through SAML, JWT, or OpenID Connect (OIDC) single sign-on. Because users are authenticated through an IdP with a non-Zendesk password, the profile is created without a password because they don't need to sign in to Zendesk directly.

Because new users who sign in to Zendesk through SSO are verified through an IdP, they don't receive email notifications to verify their account. However, it is still recommended to turn off these automated email notifications to prevent them from being sent if the IdP does not successfully verify the user. In the case of SSO, user verification must always occur through the IdP.

**To turn off password notification emails**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png) **People** in the sidebar, then select **Configuration > End users**.
2. In the **Account emails** section, deselect **Also send a welcome email when a new user is created by an agent or administrator**.
3. In **Allow users to change their password**, deselect this option.

## Generating a new shared secret

In some cases, like if your secret is compromised, you may need to issue a new JWT shared secret and provide it to your IT team or external identity provider. You can generate a new JWT shared secret from Zendesk Admin Center. This action will create a new secret and invalidate the old one. You'll need to inform your IT team or external identify provider of your new shared secret to keep Zendesk SSO account authentication working.

Important: Users cannot authenticate using JWT SSO until the new secret is in place. Make sure your users have a backup authentication method during this time.

**To generate a new shared secret**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png) **Account** in the sidebar, then select **Security > Single sign-on**.
2. Hover over the JWT configuration you want to create a new shared secret for, then click the option menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) and select **Edit**.
3. Scroll to **Shared secret** at the bottom of the configuration page and click **Reset secret**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_security_reset_secret.png)

   A confirmation message appears.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_security_reset_secret_conf.png)
4. Click **Reset secret** to confirm the reset.

   You should see a new **Shared secret** in plain text.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_security_reset_secret_copy.png)
5. Click **Copy** to make a copy of the new shared secret and give it to your IT team or your external identity provider.
6. **Save** your changes.

## Switching authentication methods

If you use a third-party SSO method to create and authenticate users in Zendesk and then switch to Zendesk authentication, these users will not have a password available for login. To gain access, ask these users to reset their passwords from the Zendesk sign-in page.

## Additional information about JWT

JWT is an open standard that is being driven by the international standards body [IETF](http://en.wikipedia.org/wiki/Internet_Engineering_Task_Force) and has top-level backers from the technology sector (for example, Microsoft, Facebook, and Google).

The fundamental building blocks of JWT are very well understood components and the result of this is a fairly simple spec, which is available here <http://tools.ietf.org/html/draft-jones-json-web-token-10>. There are a lot of open source implementations of the JWT spec that cover most modern technologies. This means that you can get JWT single sign-on set up without much difficulty.

One thing to be aware of is that the JWT payload is merely encoded and signed, not encrypted, so don't put any sensitive data in the hash table. JWT works by serializing the JSON that is being transmitted to a string. The string is Base64 encoded and then JWT makes an HMAC of the Base64 string which depends on the shared secret. This produces a signature that the recipient side can use to validate the user.

## Technical implementation worksheet

This section is for the team in the company responsible for the company's JWT authentication system. It provides details about the Zendesk JWT SSO implementation.

Note: If you're upgrading from an earlier version of Zendesk SSO (referred to as Zendesk Remote Authentication) to JWT, it's okay to have multiple SSO implementations enabled at the same time. Zendesk recognizes if a request is meant for JWT or another type of SSO and will handle the request accordingly. This means that you can enable and test JWT before deactivating your previous SSO implementation.

Topics covered:

- [JWT algorithm](#topic_bt2_x2h_3fb)
- [Zendesk JWT endpoint](#topic_w5x_1fh_3fb)
- [JWT attributes](#topic_otw_jfh_3fb)
- [Remote login URL parameter (return\_to)](#topic_hkm_kst_kk)
- [Error handling](#topic_cff_kst_kk)
- [Form submission examples](#topic_kqp_sps_d1c)
- [JWT generation examples](#topic_wjc_wdj_zj)

### JWT algorithm

Specify HS256 as the JWT algorithm in the header of your JWT payload:

```
{
  "typ":"JWT",
  "alg":"HS256"
}
```

HS256 stands for HMAC SHA 256, a 256-bit encryption algorithm designed by the U.S. National Security Agency.

Note: Zendesk does not support the RS256 and ES256 JWT algorithms.

### Zendesk JWT endpoint

Important: Using HTTP POST requests (instead of HTTP GET requests) is a best practice for your SSO security. Using HTTP POST, the user data is passed in the body of the request. With HTTP GET requests, data related to the user (like phone numbers or tags) are passed in the URL along with the JWT, which can be stored in a browser’s history or cache, putting it at risk for exposure.

After successfully authenticating the user, create the JWT payload and submit a POST request that contains the JWT payload to the following Zendesk endpoint:

**https://*yoursubdomain*.zendesk.com/access/jwt**

The payload must be base64-encoded and submitted via a form submission from a client. Submitting the payload with a client-side AJAX, fetch, or axios request won't work because the request will be blocked by the client's [same-origin policy](https://en.wikipedia.org/wiki/Same-origin_policy). Making a POST request from your server won't work either because it won't correctly set cookies used for authentication on the user's browser.

The JWT payload must be sent to your Zendesk Support subdomain using the https protocol. Example:

```
https://yoursubdomain.zendesk.com/access/jwt
```

If you have host mapping in place, you must send the JWT payload to your Zendesk Support subdomain using the HTTPS protocol, not the host-mapped domain.

### JWT attributes

Send JWT attributes using a hash (Ruby) or dictionary (Python). The JWT must be encoded as base64. Example using Ruby:

```
payload = JWT.encode({
   :email => "bob@example.com", :name => "Bob", :iat => Time.now.to_i, :jti => rand(2<<64).to_s
}, "Our shared secret")
```

Zendesk requires an email address to uniquely identify the user. Beyond the required attributes listed in the table below, you may optionally send additional user profile data. This data is synced between your user management system and Zendesk Support.

Attribute names are case sensitive, so you must match the exact casing shown in the tables below.

**Required attributes**

| Attribute name | Data type | Description |
| --- | --- | --- |
| iat | Numeric date | Issued At. The time the token was generated, this is used to help ensure that a given token gets used shortly after it's generated. The value must be the number of seconds since [UNIX epoch](http://en.wikipedia.org/wiki/Unix_time#Encoding_time_as_a_number). Zendesk allows up to three minutes clock skew, so make sure to configure NTP or similar on your servers. |
| jti | string | JSON Web Token ID. A unique id for the token, used by Zendesk to prevent token replay attacks. |
| email | string | Email of the user being signed in, used to uniquely identify the user record in Zendesk Support. |
| name | string | The name of this user. The user in Zendesk Support will be created or updated in accordance with this. |

**Optional user attributes**

| Attribute | Data type | Description |
| --- | --- | --- |
| external\_id | string | If your users are uniquely identified by something other than an email address, and their email addresses are subject to change, send the unique id from your system. Specify the id as a string. |
| locale (for end-users) locale\_id (for agents) | integer | The locale in Zendesk Support, specified as a number. |
| organization | string | The name of an organization to add the user to. If the organization doesn't exist in Zendesk, it won't be created. The user will still be created, but they won't be added to any organization. If [**Allow users to belong to multiple organizations**](https://support.zendesk.com/hc/en-us/articles/4408838140314) is turned on, additional organizations append the original organization and are considered secondary organizations. This does not delete the existing memberships.  If you'd like to pass multiple organization names at the same time, use the **organizations** attribute instead. Using the organizations attribute overwrites the existing list of organizations. The organization names must be passed in a string, separated by commas. |
| organization\_id | integer | The organization's [external ID](https://developer.zendesk.com/api-reference/ticketing/organizations/organizations/) in the Zendesk API. If both organization and organization\_id are supplied, organization is ignored. If the organization doesn't exist in Zendesk, it won't be created. The user will still be created, but they won't be added to any organization. If [**Allow users to belong to multiple organizations**](https://support.zendesk.com/hc/en-us/articles/4408838140314) is turned on, additional organizations append the original organization and are considered secondary organizations. This does not delete the existing memberships.  If you'd like to pass multiple organization IDs at the same time, use the **organization\_ids** attribute instead. Using the organization\_ids attribute overwrites the existing list of organizations. The organization IDs must be passed in a string, separated by commas. |
| phone | string | A phone number, specified as a string. The phone number should comply with the E.164 international [telephone numbering plan](https://en.wikipedia.org/wiki/E.164). Example: +15551234567.  E164 numbers are international numbers with a country dial prefix, usually an area code and a subscriber number. A valid E.164 phone number must include a [country calling code](https://en.wikipedia.org/wiki/List_of_country_calling_codes). |
| tags | array | This is a JSON array of tags to set on the user. These tags will *replace* any other tags that may exist in the user's profile. |
| remote\_photo\_url | string | URL for a photo to set on the user profile. |
| role | string | The user's role. This value can be set to **end\_user**, **agent**, or **admin**. The default is **end\_user**. If the user's role differs from the one in Zendesk Support, the role is changed in Zendesk Support. |
| custom\_role\_id | integer | Applicable only if the role of the user is agent. |
| user\_fields | object | A JSON hash of custom user field key and values to set on the user. The custom user field must exist in order to set the field value. Each custom user field is identified by its field key found in the user fields admin settings. The format of date values is yyyy-mm-dd.  If a custom user field key or value is invalid, updating the field will fail silently and the user will still log in successfully. For more information about custom user fields, see [Adding custom fields to users](https://support.zendesk.com/hc/en-us/articles/4408822051866). Note: Sending null values in the the user\_fields attribute will remove any existing values in the corresponding fields. |

### Remote login URL parameter (return\_to)

Whether you pass in the `return_to` parameter or not is optional, but we recommend it for the best user experience. When Zendesk redirects a user to your remote login page, it can pass a **return\_to** URL parameter. The parameter contains the page that Zendesk will return the user after your system has authenticated the user. Append the parameter name and value to the Zendesk JWT endpoint.

For example, suppose an agent who is signed out clicks the following link to open a ticket in Support: **https://mycompany.zendesk.com/tickets/1232**. The flow is as follows:

1. On click, Zendesk redirects the user to your remote login URL and appends the following `return_to` parameter to the URL:

   ```
   https://mycompany.com/zendesk/sso?return_to=https://mycompany.zendesk.com/tickets/123
   ```
2. Your authentication system takes the `return_to` parameter from the URL and, after successfully authenticating the user, appends it to the Zendesk JWT endpoint or adds it to the body of the request. Example:

   ```
   https://mycompany.zendesk.com/access/jwt?&return_to=https://mycompany.zendesk.com/tickets/123
   ```
3. Zendesk uses the parameter to open the ticket page for the agent.

The `return_to` parameter is an absolute URL for the agent interface, and a relative URL for Help Center.

Note: If your `return_to` address contains its own URL parameters, make sure that your script URI-encodes the entire return\_to value when submitting the JWT token.

### Error handling

If Zendesk encounters an error while processing a JWT login request, it sends a message that explains the issue. If you specified a remote logout URL when you configured the JWT integration, it redirects to that URL and passes a **message** and a **kind** parameter. In case of error, the **kind** parameter always has the value "error". Zendesk recommends specifying a remote logout URL, as well as logging messages from Zendesk alongside the type. Most of the errors that can happen are ones that you'll want to fix. Examples include clock drifts, rate limits being hit, and invalid tokens.

### Form submission examples

The JWT payload must be submitted using a form submission from a browser to the following Zendesk endpoint:

```
https://yoursubdomain.zendesk.com/access/jwt
```

Zendesk provides a series of examples for various technology stacks in the [Zendesk JWT SSO repository](https://github.com/zendesk/zendesk_jwt_sso_examples) on GitHub. You must submit the JWT payload using a form submission from a browser to ensure cookies can be set correctly on the browser and that the request isn’t blocked by CORS.

See the following form submission examples:

- [JavaScript example](https://github.com/zendesk/zendesk_jwt_sso_examples/blob/master/form_submission/javascript_jwt.html)
- [jQuery example](https://github.com/zendesk/zendesk_jwt_sso_examples/blob/master/form_submission/jquery_xhr_jwt.js)
- [Rails example](https://github.com/zendesk/zendesk_jwt_sso_examples/blob/master/form_submission/rails_html_erb_jwt.rb)
- [React example](https://github.com/zendesk/zendesk_jwt_sso_examples/blob/master/form_submission/react_jwt.jsx)

**Response**

The response should be HTML with a `200 OK` status. The response format is as follows:

```
<html><body>You are being <a href="">redirected</a>.</body></html>
```

If the `href` matches your `return_to` value, then the user was successfully authenticated and cookies should be set. If the `href` begins with `https://SUBDOMAIN.zendesk.com/access/unauthenticated`, then Zendesk was unable to authenticate the user.

### JWT generation examples

The actual JWT encoding is straightforward and most modern languages have libraries that support it. Zendesk provides a series of examples for various stacks in the JWT SSO GitHub repository:

- <https://github.com/zendesk/zendesk_jwt_sso_examples/tree/master/jwt_generation>

The JWT generation code is for your server implementation. You can pass the generated JWT back to your login page and then initiate the form submission from the browser.

If you implement JWT in any other stack, we would love to feature an example of that there as well. Add a comment to this article to share what you've implemented.

In case you run IIS/AD and don't want to build your own .NET solution, we provide a full implementation in classic ASP, which requires you to adjust only a couple of variables. [Download the ASP authentication script](https://github.com/zendesk/zendesk_jwt_sso_examples/tree/master/bundles) from Github.