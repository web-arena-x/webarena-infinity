# Creating connections to integrate with external services

Source: https://support.zendesk.com/hc/en-us/articles/5040378297626-Creating-connections-to-integrate-with-external-services

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

Location: Admin Center > Apps and integrations > Connections >
Connections

A connection lets you safely store API credentials for a service or system, such as Slack or Shopify. You can use a connection to authenticate REST API calls in [auto assist actions](https://support.zendesk.com/hc/en-us/articles/8013439366810). You must be an admin to create connections.

Note: The instructions in this article also apply to accounts using using the legacy bot builder [Make API call](https://support.zendesk.com/hc/en-us/articles/4572971586586) step.

This article covers the following topics:

- [About connections](#topic_fyj_ply_rvb)
- [Creating a connection](#topic_wb5_txw_rvb)
- [Allowed domain](#topic_dmc_y23_fvb)
- [HTTP headers for API keys](#topic_u5k_qly_rvb)

## About connections

A connection supports one of the following API authentication methods:

- API key
- Basic authentication
- Bearer token
- OAuth 2.0

This authentication method determines the type of credentials the connection stores. For example, a basic authentication connection stores a username and password. After you create a connection, you can't change its authentication type.

Different APIs support different authentication methods. To determine the appropriate authentication method for an API call, consult the API's documentation.

### HTTP headers for authentication types

When you use a connection to authenticate an API call in an auto assist action, Zendesk passes the connection's credentials in an HTTP header. Zendesk determines this header based on the connection's authentication type.

| Authentication type | HTTP header |
| --- | --- |
| API key | Set when you create the connection. See [HTTP headers for API keys](#topic_u5k_qly_rvb) |
| Basic authentication | `Authorization: Basic` |
| Bearer token | `Authorization: Bearer` |
| OAuth 2.0 | Access token is sent to the service in `Authorization: Bearer` |

For more information about using a connection in an action, see [Creating and managing actions for auto assist](https://support.zendesk.com/hc/en-us/articles/8013439366810).

## Creating an OAuth client

An OAuth connection stores an OAuth 2.0 access token for a service or system, such as Slack, Shopify, or Zendesk.

Before creating a connection with the OAuth 2.0 authentication type, you must configure an OAuth client. When configuring the OAuth client, you need the client ID, client secret, authorization URL, token URL, and scopes from the external system's OAuth configuration interface or admin portal. These credentials are generated while registering your client application (such as Zendesk) with the external system. The exact steps vary based on the external service. If required, set the client's callback URL as "https://zis.zendesk.com/api/services/zis/connections/oauth/callback".

Note:
We only support connects with external systems that are compliant with the [OAuth 2.0 Authorization Framework](https://datatracker.ietf.org/doc/html/rfc6749).

You can create OAuth clients using the following OAuth 2.0 grant types:

- Authorization code
- Client credentials

The refresh token grant type is supported for OAuth 2.0 clients created using an authorization code grant type. If the system's access token response includes non-empty [`expires_in`and `refresh_token`](https://www.oauth.com/oauth2-servers/access-tokens/access-token-response/)
values, the access token is automatically refreshed using the refresh token.

OAuth 2.0 connections created with a client using the Clients credentials grant type may include a token expiry value. In these cases, when the token expires, a new access token is fetched using the same OAuth client.

Note:
In some cases, we may refresh the access token multiple times with a single refresh token. Because some systems implement mechanisms to prevent resuse of a refresh token, we recommend implementing a grace period if possible, or using the Client credentials grant type instead.

**To create an OAuth client**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Connections >
   Connections**.
2. Enter a name for the client. You cannot change this name after you create the client.
3. Enter the Client ID. This is a unique identifier assigned to your OAuth client, similar to a username for your client.
4. Enter the Client secret. This acts as a password for your client application and establishes trust between Zendesk and the external system.
5. (Authorization code grant type only) Enter the Authorization URL. This is the server URL used to receive an authorization code.
6. Enter the Token URL. This is the URL used to receive an access token.
7. Enter a space-separate list of default scopes. Scopes are permissions that represent what a client application can access on behalf of the user.
8. Click **Save** to create the client.

## Creating a connection

You can create a connection in Admin Center from the Connections page.

**To create a connection**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Connections > OAuth Clients**.
2. Click **Create connection**.
3. Select an authentication type.
4. Enter a name for the connection. You can't change this name after you create the connection.
5. Do one of the following:
   - (API Key, Basic authentication, Bearer token) Configure the connection's authentication credentials. The connection uses these details to authenticate REST API calls to the service or system.
   - (OAuth 2.0) Select the client to use and optionally enter a space-separated list of scopes. If you do not enter any scopes, the default ones specified in the OAuth client are used.
6. Enter an allowed domain for the connection. You can't change the allowed domain after you create the connection. For more information, see [Allowed domain](#topic_dmc_y23_fvb).
7. Click **Save** to create the connection.

After you've created the connection, you can view its details from the Connections page in Admin Center. See [Managing connections](https://support.zendesk.com/hc/en-us/articles/5174239310746).

Note:
When creating a connection with an OAuth 2.0 authentication type, the scopes included in the external system's access token response are stored, not the scopes defined when creating the connection. This value cannot be greater than 255 characters.

## Allowed domain

Each connection requires a URL hostname as an allowed domain. Zendesk only passes the connection's credentials in API calls to this hostname. Attempts to use the connection with other hostnames will fail. This helps prevent an accidental leak of the connection's credentials. After you create a connection, you can't change its allowed domain.

For example, you can only use a connection with an allowed domain of "api.example.com" to make API calls to the “https://api.example.com” hostname.

### Allowed domain requirements

A connection's allowed domain can't exceed 128 characters. A subdomain or domain in the value can't exceed 63 characters. The value must contain a valid domain name.

A connection always uses an `https`scheme. Other schemes, such as `ftps`, are not supported.

### Wildcards for allowed domain

A connection's allowed domain supports an optional wildcard (\*)
subdomain. This lets you use the connection with the bare domain and any subdomain. For example, you can use a connection with an allowed domain of `*.example.com`to authenticate API calls to "example.com" or any subdomain of "example.com".

To use a wildcard subdomain, the first two characters of the allowed domain must be `*.`. You can't use a wildcard in other parts of the hostname.
For example, you can't use a wildcard within a hostname, such as `exam*.com`or `my-*.example.com.`

You can't use a wildcard with only a [public domain suffix](https://publicsuffix.org/), such as `*.com`, `*.com.au`, or `*.myshopify.com`. For a list of public suffixes, see the [public suffix list](https://publicsuffix.org/list/public_suffix_list.dat)on publicsuffix.org.

## HTTP headers for API keys

When you create an API key connection, you must specify an HTTP header name. When the connection is used to make an API call, Zendesk passes the API key as the value for this header.

Many APIs use a custom header to accept API keys. To get the appropriate header name for an API call, consult the API's documentation.

### Header name requirements

An API key connection's header name can't exceed 128 characters. The header name can only contain letters, hyphens ( `-`), and underscores ( `_`).

You can't use the following HTTP header names:

- `accept`
- `accept-charset`
- `accept-encoding`
- `accept-language`
- `cache-control`
- `connection`
- `content-md5`
- `cookie`
- `date`
- `expect`
- `from`
- `host`
- `if-match`
- `if-modified-since`
- `if-none-match`
- `if-range`
- `if-unmodified-since`
- `max-forwards`
- `pragma`
- `proxy-authenticate`
- `proxy-authorization`
- `range`
- `server`
- `referer`
- `te`
- `trailer`
- `transfer-encoding`
- `upgrade`
- `user-agent`
- `via`
- `warning`
- `www-authenticate`
- Header names starting with:
 - `x-amz-`
 - `x-amzn-`
 - `x-forwarded-`
 - `x-zis-`