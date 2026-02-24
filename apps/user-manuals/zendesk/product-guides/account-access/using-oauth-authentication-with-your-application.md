# Using OAuth authentication with your application

Source: https://support.zendesk.com/hc/en-us/articles/4408845965210-Using-OAuth-authentication-with-your-application

---

You can useOAuth 2to authenticate all your application's API requests to Zendesk. OAuth provides a secure way for your application to access Zendesk data without having to store and use the passwords of Zendesk users. For added security, OAuth tokens have expiration times, and Zendesk supports refresh tokens to renew access without requiring user re-authentication.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Use OAuth 2 for secure API authentication, allowing your application to access data without storing user passwords. Register your app, implement the authorization code flow, and handle token expiration with refresh tokens. Customize token lifespan and manage access with scopes. This setup enhances security and streamlines API interactions by reducing the need for user re-authentication.

Location: Admin Center > Apps and integrations > APIs > Oauth clients

You can use [OAuth 2](http://oauth.net/2/)
to authenticate all your application's API requests to Zendesk. OAuth provides a secure way for your application to access Zendesk data without having to store and use the passwords of Zendesk users. For added security, OAuth tokens have expiration times, and Zendesk supports refresh tokens to renew access without requiring user re-authentication.

To use OAuth authentication, you need to register your application with Zendesk. You also need to add some functionality to your application to support the OAuth authorization code flow and refreshing expired access tokens.

Zendesk also supports the client credentials grant type flow, which lets you create an access token using only an OAuth client’s secret. This grant type is intended for confidential clients only and is not covered in this article. For more information, see [Client credentials grant type](https://developer.zendesk.com/api-reference/ticketing/oauth/grant_type_tokens/#client-credentials-grant-type) in the API reference.

Topics covered in this article:

- [Registering your application with Zendesk](#topic_s21_lfs_qk)
- [Implementing an OAuth authorization flow in your application](#topic_jkc_dcm_dcc)
- [Replacing expired access tokens](#topic_p1c_xjf_52c)

Related topics:

- For a tutorial on building a web application that implements an OAuth authorization flow, see [Using OAuth to authenticate Zendesk API requests in a web app](https://developer.zendesk.com/documentation/api-basics/authentication/using-oauth-to-authenticate-zendesk-api-requests-in-a-web-app/).
- To implement an OAuth authorization flow in Zendesk apps, see [Adding third-party OAuth to a Support app](https://developer.zendesk.com/documentation/apps/build-an-app/adding-third-party-oauth-to-a-support-app/).
- If you don't need users to grant your application access to their accounts, you can still use OAuth tokens to authenticate API requests. See [Creating and using OAuth access tokens with the API](https://developer.zendesk.com/documentation/ticketing/working-with-oauth/creating-and-using-oauth-tokens-with-the-api).

## Registering your application with Zendesk

You must register your application to generate OAuth credentials that your application can use to authenticate API calls to Zendesk.

Note: This section describes how to set up an OAuth client for users of one Zendesk account.
If your application will interact not only with one Zendesk account but with lots of them, you can request a *global* OAuth client. A global OAuth client is a secure, cleaner way of doing API authentication with multiple Zendesk instances. For more information, see [Set up a global OAuth client](https://developer.zendesk.com/documentation/apps/publish-your-app-or-theme/global_oauth_intro/).

**To register your application**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **APIs > OAuth clients**.
2. Click **Add OAuth client** on the right side of the OAuth client list.
3. Complete the following fields to create a client:
   - **Name** - Enter a name for your app. This is the name that users will see when asked to grant access to your application, and when they check the list of third-party apps that have access to their Zendesk.
   - **Description** - Optional. This is a short description of your app that users will see when asked to grant access to it.
   - **Company** - Optional. This is the company name that users will see when asked to grant access to your application. The information can help them understand who they're granting access to.
   - **Logo** - Optional. This is the logo that users will see when asked to grant access to your application. The image can be a JPG, GIF, or PNG. For best results, upload a square image. It will be resized for the authorization page.
   - **Identifier** - The field is auto-populated with a reformatted version of the name you entered for your app. You can change it if you want.
   - **Client kind** - Public or Confidential. Public OAuth clients are applications that run in environments where credentials cannot be securely stored, such as mobile and web apps. These clients are required to use PKCE. Confidential OAuth clients run on secure servers where their credentials can be kept secure. These clients can use PKCE, client secret, or both. See [Understanding client kinds](#topic_ycb_ztl_m2c).
   - **Redirect URLs** - Enter the URL or URLs that Zendesk should use to send the user's decision to grant access to your application. The URLs must be absolute and not relative, https (unless localhost or 127.0.0.1), and newline-separated.
4. Click **Save**.

   After the page refreshes, a new pre-populated **Secret** field appears on the lower side. This is the "client\_secret" value specified in the [OAuth 2.0 spec](http://tools.ietf.org/html/rfc6749).
5. Copy the **Secret** value to your clipboard and save it somewhere safe. Note: The characters may extend past the width of the text box, so make sure to select everything before copying.

   Important: For security reasons, your secret is displayed fully only once. After clicking **Save**, you'll only have access to the first nine characters.
6. Click **Save**.

Use the unique identifier and the secret value in your application as described in this following topic.

### Understanding client kinds

OAuth clients have a `kind` property that can have one of the following values:

- Confidential: Confidential OAuth clients run on secure servers where their credentials can be kept secure. These clients can use PKCE, [client secret](https://developer.zendesk.com/api-reference/ticketing/oauth/grant_type_tokens/), or both.
- Public: Public OAuth clients are applications that run in environments where credentials cannot be securely stored, such as mobile and web apps. These clients must use [PKCE](https://developer.zendesk.com/documentation/ticketing/working-with-oauth/oauth-pkce/).

Examples of confidential clients include server-side web applications. Once the authorization server provides the tokens or the credentials to the web application, those credentials will not be exposed to the outside.

Examples for public clients include mobile applications and JavaScript applications that run on user-agent clients such as web browsers. Credentials are easily accessible (and often visible) in these clients.

Client kinds are also known as client types in the OAuth spec. For more information, see [Client Types](https://datatracker.ietf.org/doc/html/rfc6749#section-2.1) in the OAuth 2.0 spec.

This property applies only to the Zendesk Support ticketing system. It is not supported in Chat or Conversations.

Existing Zendesk OAuth clients currently have the `kind` property set to `unknown`. These clients remain unaffected until the `kind` property is updated to either `public` or `confidential`. New OAuth clients created in Admin Center must set the `kind` property during creation.

Note: If you are using an existing Zendesk OAuth client and plan to change the `kind` property to `public`, you must first implement PKCE. Failure to do so will result in the client not working, as PKCE will be immediately required.

Setting the `kind` property is mandatory for all new OAuth clients created in Admin Center. While the `kind` property is not required for OAuth clients created with the `api/v2/oauth/clients endpoint`, Zendesk recommends including it.

## **Implementing an OAuth authorization flow in your application**

Zendesk supports the authorization code grant flow to get access tokens. This flow is called the authorization code grant flow because you have to get an authorization code before you can request an access token.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/oauth_authorization_flow.png)

The flow uses refresh tokens, which allows you to generate new access tokens without requiring user re-authorization. The access token may expire if the API provides a valid `expires_in` parameter, indicating a specific lifespan for the token. In such cases, implement a mechanism to get a new access token when it expires using the provided refresh token.

Refresh tokens also expire, as indicated by the `refresh_token_expires_in` property. If a refresh token expires or is invalid, your app must send the user through the full OAuth authorization flow again.

You can customize how long tokens are valid by setting the `expires_in` and `refresh_token_expires_in` parameters in seconds when you request tokens.

To implement the authorization code grant flow, you need to add the following functionality to your application:

- [Step 1 - Send the user to the Zendesk authorization page](#topic_mkc_dcm_dcc)
- [Step 2 - Handle the user's authorization decision](#topic_ykc_dcm_dcc)
- [Step 3 - Get an access token from Zendesk](#topic_blc_dcm_dcc)
- [Step 4 - Use the access token in API calls](#topic_hlc_dcm_dcc)

For a tutorial on building a web application that implements an OAuth authorization code flow, see [Using OAuth to authenticate Zendesk API requests in a web app](https://developer.zendesk.com/documentation/api-basics/authentication/using-oauth-to-authenticate-zendesk-api-requests-in-a-web-app/).

The authorization code grant method supports [Proof Key for Code Exchange (PKCE)](https://www.oauth.com/oauth2-servers/pkce/), which adds an additional layer of security. For more information, see [Using PKCE to make Zendesk OAuth access tokens more secure](https://developer.zendesk.com/documentation/ticketing/working-with-oauth/oauth-pkce) in the developer documentation.

### Step 1 - Send the user to the Zendesk authorization page

First, your application has to send the user to the Zendesk authorization page. The page asks the user to authorize your application to access Zendesk on their behalf. After the user makes a choice, Zendesk sends the choice and a few other bits of information back to your application.

**To send the user to the Zendesk authorization page**

Add a link or button in your application that sends the user to the following URL:

```
https://{subdomain}.zendesk.com/oauth/authorizations/new
```

where `{subdomain}` is your Zendesk core subdomain, not a host-mapped subdomain.

You can use either a POST or a GET request. Include the following parameters:

- **response\_type** - Required. Zendesk returns an authorization code in the response, so specify `code` as the response type. Example:
 `response_type=code`.
- **redirect\_uri** - Required. The URL that Zendesk should use to send the user's decision to grant access to your application. The URL has to be absolute and not relative. It also has to be secure (https) unless you're using localhost or 127.0.0.1.
- **client\_id** - Required. The unique identifier you obtained when you registered your application with Zendesk. See the section above.
- **scope** - Required. A space-separated list of scopes that control access to the Zendesk resources. You can request *read*, *write*, or *impersonate* access to all resources or to specific resources. See [Setting the scope](#topic_qkc_dcm_dcc).
- **state** - An arbitrary string included in the response from Zendesk after the user decides whether or not to grant access. You can use the parameter to guard against cross-site request forgery ([CSRF](http://en.wikipedia.org/wiki/Cross-site_request_forgery)) attacks. In a CSRF attack, the end user is tricked into clicking a link that performs an action in a web application where the end user is still authenticated.
 To guard against this kind of attack, add some value to the `state` parameter and validate it when it comes back.
- **code\_challenge** - Required if using PKCE. A string representing a code challenge derived from a code verifier. See [Generating the code\_challenge value](https://developer.zendesk.com/documentation/ticketing/working-with-oauth/oauth-pkce#generating-the-code_challenge-value) in the developer documentation.
- **code\_challenge\_method** - Required if using PKCE. The method used to derive the code challenge. Specify **"S256"** as the value.

Make sure to URL-encode the parameters.

**Example GET request**

```
https://{subdomain}.zendesk.com/oauth/authorizations/new?response_type=code&redirect_uri={your_redirect_url}&client_id={your_unique_identifier}&scope=read%20write
```

The Zendesk authorization page opens in the end user's browser. After the user makes a decision, Zendesk sends the decision to the redirect URL you specified in the request.

#### Setting the scope

You must [specify a scope](#topic_qkc_dcm_dcc) to control the app's access to Zendesk resources. The  *read*  scope gives an app access to GET endpoints. It includes permission to sideload related resources. The *write*  scope gives an app access to POST, PUT, and DELETE endpoints for creating, updating, and deleting resources.

For more on the scope, see [OAuth Tokens for Grant Types](https://developer.zendesk.com/rest_api/docs/support/grant_type_tokens#scope).

The *impersonate* scope allows a Zendesk admin to make requests on behalf of end users. See [Making API requests on behalf of end users](https://developer.zendesk.com/documentation/ticketing/using-the-zendesk-api/making-api-requests-on-behalf-of-end-users).

For example, the following parameter gives an app read access to all resources:

```
"scope": "read"
```

The following parameter gives read and write access to all resources:

```
"scope": "read write"
```

You can fine-tune the scope to the following resources:

- tickets
- users
- auditlogs (read only)
- organizations
- hc
- apps
- triggers
- automations
- targets
- webhooks
- macros
- requests
- satisfaction\_ratings
- dynamic\_content
- any\_channel (write only)
- web\_widget (write only)
- zis

The syntax is as follows:

```
"scope": "resource:scope"
```

For example, the following parameter restricts an app to only reading tickets:

```
"scope": "tickets:read"
```

To give an app read and write access to a resource, specify both scopes:

```
"scope": "users:read users:write"
```

To give an app write access only to one resource, such as organizations, and read access to everything else:

```
"scope": "organizations:write read"
```

### Step 2 - Handle the user's authorization decision

Your application has to handle the response from Zendesk telling it what the user decided. The information is contained in URL parameters in the redirect URL.

If the user decided to grant access to the application, the redirect URL contains an authorization code. Example:

```
{redirect_url}?code=7xqwtlf3rrdj8uyeb1yf
```

The authorization code is only valid for 120 seconds.

If the user decided not to grant access to the application, the redirect URL contains `error` and `error_description` parameters that inform the app that the user denied access:

```
{redirect_url}?error=access_denied&error_description=The+end-user+or+authorization+server+denied+the+request
```

Use these values to control the flow of your application. If the URL contains a `code` parameter, get an access token from Zendesk as described in the following section. This is the token to include in API calls to Zendesk.

### Step 3 - Get an access token from Zendesk

If your application received an authorization code from Zendesk in response to the user granting access, your application can exchange it for an access token and a refresh token.
To get the tokens, make a POST request to the [Create Token Grant Type](https://developer.zendesk.com/api-reference/ticketing/oauth/grant_type_tokens/#create-token-for-grant-type) endpoint:

```
https://{subdomain}.zendesk.com/oauth/tokens
```

Note: Don't confuse this endpoint with the [Create Token](https://developer.zendesk.com/rest_api/docs/support/oauth_tokens#create-token) endpoint in the OAuth Tokens API.
Though both endpoints return valid OAuth access tokens, the endpoints don't share the same path, JSON format, or request parameters.

Include the following required parameters in the request:

- **grant\_type** - Specify **"authorization\_code"** as the value.
- **code** - Use the authorization code you received from Zendesk after the user granted access.
- **client\_id** - Use the unique identifier specified in an OAuth client in the Zendesk Admin Center (**Apps and integrations** > **APIs** > **OAuth Clients**). See [Registering your application with Zendesk](#topic_s21_lfs_qk).
- **client\_secret** - Use the secret specified in an OAuth client in the Zendesk Admin Center (**Apps and integrations** > **APIs** > **OAuth Clients**).
 See [Registering your application with Zendesk](#topic_s21_lfs_qk).

 If you use the PKCE `code_challenge` and `code_verifier` parameters, `client_secret` is not required. You can use this characteristic to migrate from the [implicit grant flow](https://oauth.net/2/grant-types/implicit/), which is no longer recommended because of security concerns. See [Using PKCE to migrate from the implicit grant flow](https://developer.zendesk.com/documentation/ticketing/working-with-oauth/oauth-pkce#using-pkce-to-migrate-from-the-implicit-grant-flow) in the developer documentation.
- **redirect\_uri** - The same redirect URL as in step 1. For ID purposes only.
- **scope** - See [Setting the scope](#topic_qkc_dcm_dcc).
- **code\_verifier** - Required if using PKCE. The string used to generate the `code_challenge` value. See [Generating the code\_challenge value](https://developer.zendesk.com/documentation/ticketing/working-with-oauth/oauth-pkce#generating-the-code_challenge-value) in the developer documentation.
- **expires\_in** - Number of seconds the access token is valid. Specify a value between 300 seconds (5 minutes) and 172,800 seconds (2 days).
- **refresh\_token\_expires\_in** - Number of seconds the refresh token is valid.
 Specify a value between 604,800 seconds (7 days) and 7,776,000 seconds (90 days).

See the [Create Token Grant Type](https://developer.zendesk.com/api-reference/ticketing/oauth/grant_type_tokens/#create-token-for-grant-type) endpoint in the API reference for more information.

The request must be over https and the properties must be formatted as JSON. If you use a custom or third-party application to make the API request, see its documentation for the proper format of property values.

**Using the Python requests library**

```
response = requests.post(
    f'https://{subdomain}.zendesk.com/oauth/tokens',
    data={
        'grant_type': 'authorization_code',
        'code': f'{your_code}',
        'client_id': f'{your_client_id}',
        'client_secret': f'{your_client_secret}',
        'redirect_uri': f'{your_redirect_url}',
        'scope': 'read',
        'expires in': 172800,
        'refresh_token_expires_in': 800000
    }
)
```

**Example response**

```
Status: 201 OK

{
 "access_token": "gErypPlm4dOVgGRvA1ZzMH5MQ3nLo8bo",
 "refresh_token": "31048ba4d7c601302f3173f243da835f",
 "token_type": "bearer",
 "scope":"read",
 "expires_in": 172800,
 "refresh_token_expires_in": 800000
}
```

Save both the access token and the refresh token in a secure data store to reuse them later.

### Step 4 - Use the access token in API calls

The app can use the access token to make API calls. Include the token in an HTTP Authorization header with the request, as follows:

`Authorization: Bearer {a_valid_access_token}`

For example, a curl request to list tickets would look as follows:

```
curl https://{subdomain}.zendesk.com/api/v2/tickets.json \
 -H "Authorization: Bearer gErypPlm4dOVgGRvA1ZzMH5MQ3nLo8bo"
```

## Replacing expired access tokens

Access tokens will expire after a set time. Use the refresh token you received with the access token to request a new access token. You don't need to use the authorization code flow to get the new token.

Your application should implement a fallback mechanism to handle expired access tokens and expired refresh tokens. For example, if the access token has expired or encountered an error, use a handler to refresh it. If the refresh process fails or there is no refresh token linked to the access token, redirect the user to `https://{subdomain}.zendesk.com/oauth/authorizations/new` to re-authorize your application.

### Detecting that an access token has expired

To determine if an access token has expired, instrument your code to look for a **401** response after making an API request with the token. The response will include the following JSON string:

```
{"error":"invalid_token","error_description":"The access token provided is expired, revoked, 
 malformed or invalid for other reasons."}
```

If you receive a 401 response, call a handler to refresh the access token using the refresh token you received with the access token.

Here's an example using the Python requests library:

```
url = f'https://{your_subdomain}.zendesk.com/{endpoint}'
headers = {'Authorization': f'Bearer {access_token}'}
response = requests.get(url, headers=headers)
if response.status_code == 401:     # if token has expired or is otherwise invalid
    access_token = refresh_access_token(refresh_token)
    headers['Authorization'] = f'Bearer {access_token}'
    response = requests.get(url, headers=headers)
```

### Refreshing an access token

To refresh an access token, make a POST request to the [Create Token Grant Type](https://developer.zendesk.com/api-reference/ticketing/oauth/grant_type_tokens/#create-token-for-grant-type) endpoint:

```
https://{subdomain}.zendesk.com/oauth/tokens
```

Include the following properties in the request body:

- **grant\_type** - Specify the string **"refresh token"** as the value.
- **refresh\_token** - Specify the value of the refresh token you received with the access token.
- **client\_id** - Use the identifier specified in the OAuth client in the Zendesk Admin Center (**Apps and integrations** > **APIs** > **OAuth clients**).
 See [Registering your application with Zendesk](#topic_s21_lfs_qk).
- **client\_secret** - Use the secret specified in the OAuth client in the Zendesk Admin Center (**Apps and integrations** > **APIs** > **OAuth Clients**).
 See [Registering your application with Zendesk](#topic_s21_lfs_qk).

 If you use the PKCE `code_challenge` and `code_verifier` parameters, `client_secret` is not required. You can use this characteristic to migrate from the [implicit grant flow](https://oauth.net/2/grant-types/implicit/), which is no longer recommended because of security concerns. See [Using PKCE to migrate from the implicit grant flow](https://developer.zendesk.com/documentation/ticketing/working-with-oauth/oauth-pkce#using-pkce-to-migrate-from-the-implicit-grant-flow) in the developer documentation.
- **scope** - See [Setting the scope](#topic_qkc_dcm_dcc).
- **expires\_in** - Number of seconds the access token is valid. Specify a value between 300 seconds (5 minutes) and 172,800 seconds (2 days).
- **refresh\_token\_expires\_in** - Number of seconds the refresh token is valid.
 Specify a value between 604,800 seconds (7 days) and 7,776,000 seconds (90 days).

See the [Create Token Grant Type](https://developer.zendesk.com/api-reference/ticketing/oauth/grant_type_tokens/#create-token-for-grant-type) endpoint in the API reference for more information.

Here's an example request using the Python requests library:

```
response = requests.post(
    f'https://{your_subdomain}.zendesk.com/oauth/tokens',
    data={
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': 'read',
        'expires in': 172800,
        'refresh_token_expires_in': 800000
    }
)
```

The request creates new access and refresh tokens while invalidating the previous ones.
Here's an example response:

```
Status: 201 OK

{
 "access_token": "gErypPlm4dOVgGRvA1ZzMH5MQ3nLo8bo",
 "refresh_token": "31048ba4d7c601302f3173f243da835f,
 "token_type": "bearer",
 "scope": "read",
 "expires_in": 172800,
 "refresh_token_expires_in": 80000
}
```

Save both tokens in a secure data store to reuse them later.