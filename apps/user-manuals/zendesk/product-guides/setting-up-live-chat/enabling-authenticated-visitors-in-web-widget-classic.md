# Enabling authenticated visitors in Web Widget (Classic)

Source: https://support.zendesk.com/hc/en-us/articles/4408838925082-Enabling-authenticated-visitors-in-Web-Widget-Classic

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

If you are using Web Widget (Classic) with your Chat account, you can configure your widget
to authenticate visitors on every page load using the Javascript API and JWT token.

This article applies to customers using the following version of live chat:

- Zendesk Chat Phase 4 – Chat-only or with Support

For help identifying which version of Chat you're using, see [Determining your Zendesk Chat account version](https://support.zendesk.com/hc/en-us/articles/4408836197658).

This article includes the following topics:

- [Overview](#topic_isw_nry_4fb)
- [Generating a Chat shared
  secret](#topic_s5k_dvq_4fb)
- [Creating a JWT token](#topic_n3q_cvq_4fb)
- [Code samples](#topic_qbh_cvq_4fb)
- [Sign out](#topic_cd4_xnn_bhb)
- [About the agent experience with
  authenticated visitors](#topic_jsx_cvq_4fb)
- [About the Web Widget (Classic) experience
  for authenticated visitors](#topic_nj2_dvq_4fb)

## Overview

You can configure your widget to authenticate visitors on every page load using a
new Javascript API and JWT token.

When you configure the Web Widget (Classic) to use authenticated visitors, you
get the following benefits:

- Ability to have higher confidence and security that the visitor/customer you
  or your agents are talking to is the real deal
- Support for cross domain traffic. If you are embedding the widget on multiple
  domains or link to externally hosted services (ex. Shopify), authenticating the visitor
  will make it one visitor across the domains to the Chat platform which allows your agent
  to have more context
- Support for cross device/browser identification. The visitor can be viewed as
  the same person if or when they choose to use a different device or browser when the
  custom ID is specified in the authentication call.
- Ability to present past chat conversations to the visitor in the widget

## Generating a Chat shared secret

Note: This shared secret is different from the one available in the Web Widget (Classic)
settings for restricted help center content.

To generate a shared secret

1. From the Chat dashboard, go to **Settings > Widget > Widget Security
   tab**.
2. Click the **Generate** button underneath the Visitor Authentication
   section:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_visitor_auth_legacy.png)

Because it is a security setting, your shared secret is intended to be generated,
copied and pasted into a communication with your engineering team or directly into your
codebase in one sitting. It is not to be entered into a browser:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_shared_secret_LEGACY.png)

Note: The shared secret is intended to remain secure. As a result, it will only appear in full
one time. If you don’t have access to the shared secret and need the full secret to create
your token, you can reset the secret by clicking the **Regenerate** button.

Regenerating a new shared secret will revoke the previous token. If you have
concerns the shared secret has been compromised, you should regenerate a new one. If you
need to rotate the keys, you should schedule it when Chat is offline because regenerating
the secret may cause visitors to be disconnected from the widget for 5 minutes.

Once you have generated the shared secret, use it to create a JWT token ([Learn more about JWT](https://jwt.io/)) that
you'll add to your Web Widget snippet.

## Creating a JWT token

**To create a JWT token and add the code to the Chat standalone snippet**

1. Construct a server-side payload of data for the JWT token. This needs to have the
   following information:
   - **name**: Customer's name
   - **email**: Customer's email (note that accented characters cannot be used in
     email addresses)
   - **external\_id:** alphanumeric string, unique to identifying the customer. Once
     set for the customer, this value cannot be changed. We recommend that you use your
     system's unique user ID for this field. For example, user-123456.
   - **iat**: Integer value of the current timestamp, in seconds. Some functions in
     specific languages i.e. JavaScript's Date.now() return milliseconds, so please make
     sure you convert to seconds. Iat for Chat authentication permits up to two minutes
     clock skew.
   - **exp:** Integer value of the current timestamp, in seconds. This value indicates
     when this JWT token will expire. The value is permitted to be up to a maximum of 7
     minutes from the iat value.
2. Use the code samples below to find a template that fits your language needs.
3. Use the zESetting Javascript API with the key `webWidget.authentication.chat.jwtFn` to
   provide a function which supplies a fresh JWT every time it is invoked. Below is a code example:

   ```
   window.zESettings = {
    webWidget: {
      authenticate: {
        chat: {
          jwtFn: function(callback) { 
            fetch('JWT_TOKEN_ENDPOINT').then(function(res) {
               res.text().then(function(jwt) {
                callback(jwt);
               });
             });
           }
         } 
       }
     }
   };
   ```

   In the example above, JWT\_TOKEN\_ENDPOINT is an endpoint which can be implemented on
   your own server to obtain a fresh JWT.Note: The jwtFn can be called multiple times
   throughout a chat session to obtain a new JWT in order to validate the visitor’s identity
   over the session’s lifetime.

   Note: The jwtFn can be called multiple times throughout a chat
   session to obtain a new JWT in order to validate the visitor’s identity over the
   session’s lifetime.

## Code samples

Your token needs to be dynamically generated from the server-side on page load. Find the
template below that fits your language needs. Customize the sample as needed, making sure to
replace the #{details} with your own information.

If none of these samples match your needs, JWT has a more extensive list of [JWT libraries](https://jwt.io/#libraries-io) to
explore.

- [Ruby](#topic_cl2_nnn_bhb)
- [NodeJS](#topic_ocv_nnn_bhb)
- [Python](#topic_xbb_4nn_bhb)
- [PHP](#topic_ekv_4nn_bhb)
- [Elixir](#topic_r31_pnn_bhb)

### Ruby

First, install [ruby-jwt](https://github.com/jwt/ruby-jwt).

If you're using Rubygems:

```
gem install jwt
```

If you're using Bundler, add the following to your gem file:

```
gem 'jwt'
```

Next, generate a token using the shared secret:

```
require 'jwt'
payload = {
  :name => "#{customerName}",
  :email => "#{customerEmail}",
  :iat => timestamp,
  :external_id => "#{externalId}"
}
token = JWT.encode payload, "#{yourSecret}"
```

### NodeJS

Install [jsonwebtoken](https://github.com/auth0/node-jsonwebtoken):

```
npm install jsonwebtoken --save-dev
```

Then, generate a token using the shared secret:

```
var jwt = require('jsonwebtoken'); 
var payload = {
  name: '#{customerName}',
  email: '#{customerEmail}',
  iat: #{timestamp},
  external_id: '#{externalId}'
};
var token = jwt.sign(payload, '#{yourSecret}');
```

### Python

Install [python-jose](https://github.com/mpdavis/python-jose/):

```
pip install python-jose
```

Generate a token using the shared secret:

```
from jose import jwt
var payload = {
  'name': '#{customerName}',
  'email': '#{customerEmail}',
  'iat': #{timestamp}, 
  'external_id': '#{externalId}'
}
token = jwt.encode(payload, '#{yourSecret}'
```

### PHP

Download [PHP-JWT](https://github.com/firebase/php-jwt):

```
composer require firebase/php-jwt
```

Generate a token using the shared secret:

```
use \Firebase\JWT\JWT;
$payload = {
  'name' => '#{customerName}' ,
  'email' => '#{customerEmail}',
  'iat' => #{timestamp},
  'external_id' => '#{externalId}'
};
$token = JWT::encode($payload, '#{yourSecret}');
```

### Elixir

Add `json\_web\_token\_ex` to your `mix.exs` file:

```
defp deps do
  [{:json_web_token, "~> 0.2"}]
end
```

Generate a token using the shared secret:

```
data = %{
  name: "#{customerName}",
  email: "#{customerEmail}",
  iat: "#{timestamp}",
  external_id: "#{externalId}"
}
options = %{ key: "#{yourSecret}" }
jwt = JsonWebToken.sign data, options
```

## Sign out

If you want to sign out the authenticated visitor, see the [Web Widget (Classic) Settings reference](https://developer.zendesk.com/api-reference/widget/settings/#authenticate).

## About the agent experience with authenticated visitors

A few things are updated in the Chat dashboard when an agent starts chatting with an
authenticated visitor.

First, the agent will be able to tell the visitor is authenticated by the green
authenticated checkmark overlay on the visitor's avatar:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_user_avatar_check.png)

The agent will also notice that they cannot edit the visitor's name or email, since the
source of truth comes from the information that is being sent via the Javascript API.

Finally, banning an authenticated visitor will mean the visitor cannot access the Chat
widget across devices and browsers.

## About the Web Widget (Classic) experience for authenticated visitors

Authenticated visitors will also have a slightly different experience in the Chat widget.
First, their information is read-only and cannot be modified by them via the widget or
through the Javascript APIs.

Second, ongoing chat sessions are synced across devices when the visitor is authenticated.
This gives the visitor flexibility to switch computers/browsers and continue their ongoing
chat session, which is not possible today.

Third, the ability to have the chat in a popout is removed for authenticated visitors
because there is no way to verify their identity via the popout (as the experience is hosted
on our domain, zopim.com).

Finally, the authenticated visitor will have the ability to see their past conversations in
the widget by scrolling up in the chat log. To learn about conversation history support for
authenticated visitors, click [here](https://support.zendesk.com/hc/en-us/articles/4408821977114).