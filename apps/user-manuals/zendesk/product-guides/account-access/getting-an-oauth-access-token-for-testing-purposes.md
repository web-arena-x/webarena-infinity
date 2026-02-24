# Getting an OAuth access token for testing purposes

Source: https://support.zendesk.com/hc/en-us/articles/4408882184986-Getting-an-OAuth-access-token-for-testing-purposes

---

You can generate an OAuth access token for testing purposes. To test or build an internal application, avoid API requests that are associated with a specific user, as is the case with  [basic authentication](https://developer.zendesk.com/api-reference/introduction/security-and-auth/#basic-authentication), which requires a username and password, or [API token authentication](https://developer.zendesk.com/api-reference/introduction/security-and-auth/#api-token), which also requires a username. Instead, use an [OAuth access token](https://developer.zendesk.com/api-reference/introduction/security-and-auth/#oauth-access-token).

Important:  The technique described in this article consists of exchanging a Zendesk username and password for an access token. As a result, the token has the same security vulnerabilities as a password. Anybody with the token has access to the account. Keep the token in a safe place and don't hard-code it in your application code. Store it in an environment variable instead.

### Creating the OAuth client

Your first step is to create an OAuth client for testing.

1. In [Admin Center,](https://support.zendesk.com/hc/en-us/articles/4408838272410) click the **Apps and integrations** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)), then select **Connections >** **OAuth clients.**
2. Click **Add client**.

Note the following differences from creating a normal OAuth client:

- Your URLs needs to be valid HTTPS URLs, but they don't have to be a real website for this project. Example: <https://somesite.com>.
- **Unique identifier** is the name of your client for use in code. Get the client ID with the  [List Clients](https://developer.zendesk.com/rest_api/docs/core/oauth_clients#list-clients)  endpoint of the OAuth Client API.
- Copy your **Client Secret** for future reference. It won't be displayed again after you create it, and you'll need it build an OAuth web app or for other projects.
- All other fields can be filled out with dummy data.

![Add client.png](https://support.zendesk.com/hc/article_attachments/7457123228570)

### Creating the access token

Create a token with the  [OAuth Tokens API](https://developer.zendesk.com/rest_api/docs/core/oauth_tokens#create-token) by making the request with cURL:

```
 curl https://{subdomain}.zendesk.com/api/v2/oauth/tokens.json \
   -H "Content-Type: application/json" \
   -d '{"token": {"client_id": "your_client_id", "scopes": ["read", "write"]}}' \
   -X POST -v -u {email_address}:{password}
```

A few things to note about this code:

- Replace the subdomain placeholder with your own subdomain
- The value of "client\_id" is the number you copied from the OAuth Clients page
- Set your scopes to ["read", "write"] unless you're specifically testing read-only access to a resource
- If your organization uses [single sign-on](https://support.zendesk.com/hc/en-us/articles/4408883587226) (SSO) and the Zendesk passwords were deleted from the Zendesk account, use an API token to authenticate the request: `-u {email_address}/token:{api_token}`. See the [API token](https://developer.zendesk.com/rest_api/docs/support/introduction#api-token) in the Support API docs.

Run your cURL request. It should return a JSON package consisting of a token object with several properties:

![](https://support.zendesk.com/hc/article_attachments/7856552806938)

The value of **full\_token** is your access token. Copy it and keep it.

Note that the response's **expires\_at** property is **null**, which means the token won't stop working until you delete the client itself. Also, next time you visit the **OAuth Clients** list in Admin Center, your number of active tokens for your new client should increase by 1.

### Using your new access token

#### Using an access token to authenticate an API request

Any API call that requires authentication can be made with an OAuth access token. For example, a call to the **Ticket** endpoint looks like this:

```
curl https://{subdomain}.zendesk.com/api/v2/tickets.json \
   -u {email_address}:{password}
```

A call to the **Ticket** endpoint looks like this with an access token:

```
curl https://{subdomain}.zendesk.com/api/v2/tickets.json \
  -H "Authorization: Bearer {access_token}"
```

#### Using an access token in an API client

Use an OAuth access token in any of our  [API clients](https://developer.zendesk.com/rest_api/docs/api-clients/introduction). The  [Ruby client](https://github.com/zendesk/zendesk_api_client_rb), for example, requires authentication with a username and password (or API token):

```
  config.username = "user email"
  config.password = "user password"
```

Here's how it looks if you use an access token instead:

```
 config.access_token = "your OAuth access token"
```