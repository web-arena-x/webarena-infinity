# Using restricted help center content with Web Widget (Classic)

Source: https://support.zendesk.com/hc/en-us/articles/4408843923610-Using-restricted-help-center-content-with-Web-Widget-Classic

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

You can configure your Web Widget (Classic) to embed content from a restricted help center (one
that requires users to sign in for access), or restricted knowledge base content (a public
help center with articles that are restricted to specific users).

When you configure Web Widget (Classic) to include restricted content:

- Visitors to your website who are logged in can read the restricted help center articles via Web
  Widget (Classic). Note that the customer site in which the widget is embedded is
  responsible for authentication of a users email.
- Visitors who are not logged in, however, see only public articles. If there are no public
  articles, the help center features do not appear in Web Widget (Classic).

This article includes the following topics:

- [Determining your help center security
  settings](#topic_wj4_kpz_pw)
- [Setting up Web Widget (Classic) to show restricted
  content](#topic_jxn_rpz_pw)
- [Code samples](#topic_u4v_lh1_qw)

Note: You do not need to have a single sign-on (SSO) connection between your site and your help
center to take advantage of this feature. However, having SSO will provide a more seamless
experience, for those users who want to “View Original Article” from Web Widget (Classic).
Please note that even if you already have SSO you will need to configure your Web Widget
(Classic) so that you can benefit from this feature.

For more information on Web Widget (Classic), see [Using Web
Widget (Classic) to embed customer service in your website](https://support.zendesk.com/hc/en-us/articles/4408836216218).

For information on restricted help centers and knowledge base content, see [Restricting your content to logged in users only](https://support.zendesk.com/hc/en-us/articles/4408883658906#topic_2kg_qct_f3) and [Restricting access to knowledge base content](https://support.zendesk.com/hc/en-us/articles/4408824005914).

## Determining your help center security settings

The Web Widget (Classic) allows you to display content from a help center with any of the
following security configurations. You may need to enable or disable the require sign in
option in your help center security settings, based on your type of help center.

| Type of help center | Enable "Require sign in"? |
| --- | --- |
| **A public help center**, where all content is available to the public. | Don't enable **Require sign in**. |
| **A restricted help center**, where users must be registered and signed in to view any content. | Enable **Require sign in**. |
| **A public help center with restricted content**, where some articles are only available to specific users, and others are available to all help center visitors. | Don't enable **Require sign in**. Everyone can see the unrestricted articles in your help center without logging in. However, only signed-in users with the correct permissions can see the restricted articles. |

**To check your help center security settings**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_settings.png)) in the sidebar.
2. In the **Security** section, enable or disable the **Require sign in** option, if
   needed, based on your type of help center.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_settings_security.png)
3. If you have a restricted help center or a public help center with restricted content,
   proceed to [Setting up Web Widget (Classic) to
   show restricted content](#topic_jxn_rpz_pw).

## Setting up Web Widget (Classic) to show restricted content

If you have a restricted help center or a public help center with restricted content that
means you have *restricted* articles (see [Determining your help center security settings](#topic_wj4_kpz_pw)). If you want restricted articles
to appear in Web Widget (Classic), you need to configure your Web Widget (Classic) settings
and add additional snippets to your website's code.

If you have a public help center, this task doesn't apply to you.

To get started, you need to check your Web Widget (Classic) settings and generate a shared
secret.

**To check your settings and generate a shared secret**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Classic > Web Widget**.
2. Click the **Basics** tab.
3. Make sure that the Help Center checkbox is selected.

   If you haven't already, enable
   or disable the **Require sign in** option, based on your type of help center (see
   [Determining your help center security
   settings](#topic_wj4_kpz_pw)).
4. Click the **Security** tab.
5. In the **Allowlist** box, enter the subdomains that contain Web
   Widget (Classic). This allows restricted help center content to display in the widget
   for authenticated users.

   For your security, we recommend adding subdomains to the
   allowlist. If you have specific reasons why restricting access to particular
   subdomains will not work, you may leave this box empty. Use spaces to separate
   subdomains.
6. Select **Allow agents to access restricted help center content**
   to allow restricted help center content to appear when agents and admins access Web
   Widget (Classic).

   If you have a restricted help center and agent access is *not*
   enabled, the help center features will not display in Web Widget (Classic) for agents
   and admins. If you have restricted articles and agent access is *not* enabled,
   agents will only encounter the public content.
7. Configure **Shared Secret**:
   - Create a shared secret by clicking the **Generate** button:

     Because it is a
     security setting, your shared secret is intended to be generated, copied and
     pasted into a communication with your engineering team or directly into your
     codebase in one sitting. It is not to be entered into a browser.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/SharedSecret2-2.png)

     Note: The shared secret is intended to remain secure. As a
     result, it will only appear in full one time. If you don’t have access to the
     shared secret and need the full secret to create your token, you can reset the
     secret by clicking **Reset**.
   - If you believe that your shared secret has been compromised, after you reset your
     shared secret you can **revoke all existing tokens**. This will invalidate the
     access of anyone that had authenticated previously and will not allow restricted
     content to be viewed until a new valid token has been issued.

Once you have generated the shared secret, use it to create a JWT token ([Learn more about JWT](https://jwt.io)) that
you'll add to your Web Widget (Classic) snippet.

**To create a JWT token and add the code to Web Widget (Classic) snippet**

1. Construct a server-side payload of data for the JWT token. This needs to have the
   following information:

   - **name**: Customer's name
   - **email**: Customer's email
   - **iat**: Integer value of the current timestamp, in seconds. Some functions
     in specific languages i.e. JavaScript's Date.now() return milliseconds, so please
     make sure you convert to seconds.

     Iat for Web Widget authentication permits up
     to two minutes clock skew.
   - **jti**: Unique identifier for this token. Cannot be the same as any other
     jwt tokens already sent through. A random 64 bit number for example.
2. Specify HS256 as the JWT algorithm in the header of your JWT
   payload:

   ```
   {
     "typ":"JWT",
     "alg":"HS256"
   }
   ```

   HS256 stands for
   HMAC SHA 256, a 256-bit encryption algorithm designed by the U.S. National Security
   Agency.

   Note: Zendesk does not support the RS256 and ES256 JWT
   algorithms.
3. Use the [code samples](#topic_u4v_lh1_qw) below to find
   a template that fits your language needs.
4. Add a function which fetches your JWT from your server, and makes a callback with the
   JWT value. Replace "YOUR\_JWT\_TOKEN" with the token you created. Make sure to put this
   code before the Web Widget (Classic) snippet:

   ```
   <script type="text/javascript">
   window.zESettings = {
       webWidget: {
         authenticate: {
           jwtFn: function(callback) {
             callback('YOUR_JWT_TOKEN');
               }
           }
       }
   };
   </script>
   ```

   Tokens expire after two hours. You can remove them from local storage sooner by
   adding the following API call when the user is logging out:

   ```
   <script type="text/javascript">
   zE(function() {
    zE.logout();
   });
   </script>
   ```

## Code samples

Your token needs to be dynamically generated from the server-side on page load. Find the
template below that fits your language needs. Customize the sample as needed, making sure to
replace the #{details} with your own information.

If none of these samples match your needs, JWT has a more extensive list of [JWT libraries](https://jwt.io/#libraries-io) to
explore.

- [Ruby](#topic_mkx_th1_qw)
- [NodeJS](#topic_h1r_th1_qw)
- [Python](#topic_cwk_th1_qw)
- [PHP](#topic_pxd_th1_qw)
- [Elixir](#topic_jhh_sh1_qw)

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
  :jti => "#{uniqueId}"
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
  jti: '#{uniqueId}'
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
  'jti': '#{uniqueId}'
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
  'jti' => '#{uniqueId}'
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
  jti: "#{uniqueId}"
}
options = %{ key: "#{yourSecret}" }
jwt = JsonWebToken.sign data, options
```