# Understanding options for end-user access and sign-in

Source: https://support.zendesk.com/hc/en-us/articles/4408887573274-Understanding-options-for-end-user-access-and-sign-in

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

One of the steps in setting up your Zendesk account is deciding how you want to
configure end-user access. Based on the type of support you provide, you may
allow anyone to submit support requests or limit it to a select group of
users. You can configure Zendesk Support for either scenario.

You'll need to configure end-user access, registration, and sign-in options.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/access_diagram.png)

This article covers the following topics:

- [Options for end-user access](#topic_dkn_nfk_v3)
- [Options for end-user registration](#topic_rdm_jkx_53)
- [Options for end-user sign-in](#topic_ry4_2hk_v3)

## Options for end-user access

You have internal and external users. Your agents and other support staff
are your internal users, also called *team members*. Your end
users, also called customers, are the people to whom you provide
support and whose tickets you manage in Zendesk Support. These are
your external users. While your support staff must sign in to your
Zendesk account, your end users may not have to, depending on how
you set up access to Zendesk Support.

You can use the [allowlist and
blocklist](https://support.zendesk.com/hc/en-us/articles/4408886840986) to restrict the external users who can
access your Zendesk Support instance. For example, you might want to
allow only end users from a specific email domain and reject all
others.

You can set up your Zendesk Support access to be completely open to all
users, restrict it to a specific group or groups of users, or close
your Zendesk Support instance and allow only the users you add to
your Zendesk account.

- **Open** means that everyone can see your help center
  and submit support requests. For example, you'd
  choose this configuration if you sell products and
  provide support to the general public. This option
  allows anyone to submit support requests. A new user
  account is then created in Zendesk for users who
  haven't submitted support requests before.
- **Closed** means your help center is visible to
  everyone, but only the users you add to your Zendesk
  account can sign in and submit support requests.
  Each user's account must be created before they can
  submit support requests, and signing in is required.
  This is typically how an in-house IT help desk would
  configure their Zendesk Support instance.
- **Restricted** means that your help center is visible
  to everyone, but only users with email addresses in
  domains you approve can submit support requests
  successfully. All other users' requests are
  rejected. This configuration allows you to restrict
  access to Zendesk Support but also allows your users
  to request support without first being added to your
  Zendesk account, as is the case with a closed
  Zendesk Support instance.

Setting up your Zendesk Support instance for all three options is
described in the following topics:

- [Enabling anyone to submit tickets
  (open)](https://support.zendesk.com/hc/en-us/articles/4408881989018)
- [Permitting only added users to
  submit tickets (closed)](https://support.zendesk.com/hc/en-us/articles/4408883658906)
- [Permitting only users with approved
  email addresses to submit tickets
  (restricted)](https://support.zendesk.com/hc/en-us/articles/4408893912986)

## Options for end-user registration

You can require that your end users register before they can begin a
conversation with your Zendesk instance. This means that users must
first register (sign up) by providing their name and email address.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/captcha_signin2.png)

The registration process starts when an end user does one of the
following:

- Visits your help center and clicks **Submit a
  request**
- Visits your help center and clicks **Sign in** for
  the first time and then **Sign up**
- Sends an email support request to your support email
  address for the first time

After signing up, users receive a welcome email message that prompts them
to verify their email address and create a password to sign in to
Zendesk.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/welcome_email.png)

Important: When you require your end users to register,
requests they submit to Zendesk Support before registering
are sent to the suspended tickets view; they are not added
as tickets in your Zendesk Support instance. When the end
user verifies their email address, their future requests
will create tickets. Their previous requests must be
recovered from the suspended tickets view.

Requiring your end users to register helps you ensure that the support
requests you receive are legitimate and not spam. Registration does
not guarantee that spam won't get through to your Zendesk account,
but other tools are provided to handle those that do manage to get
through. See [Understanding and managing suspended
tickets and spam](https://support.zendesk.com/hc/en-us/articles/4408889141146).

Registering and signing in to your Zendesk Support instance allows the
end user to do the following:

- Submit tickets in your help center without being
  prompted to provide their email address
- Track their tickets in your help center
- Comment on articles in your help center, participate in
  community discussions, and more. See [Getting started with your help
  center](https://support.zendesk.com/hc/en-us/articles/4408846795674-Getting-started-with-Help-Center#topic_p5y_31c_qk).
- Update their user profile and add additional contact
  information (email addresses and social media
  accounts) so that they can submit requests from any
  of these accounts, and Zendesk will pair them to
  their Zendesk user account

Note: End users must allow third-party cookies in their browser to be added as a new user when using
an incognito or private window.

### Allowing unregistered users to submit requests

You can still provide support to your end users without requiring
them to register and sign in. They lose the benefits that
registration provides, but the ticket workflow is the same
for your agents. Many companies provide email-only support
and never require their end users to register because they
don't want or need their end users to visit and use their
help center.

Note: You can actually do both: not require registration and
also allow your end users to use your help center.
You'd do this by hiding all the sign-in access
points into your knowledge base and providing
content anyone can see. For more information, see
[Setting up to provide email-only
support](https://support.zendesk.com/hc/en-us/articles/4408888722842).

Even when you don't require your end users to register, a user
account is created for each of them in your Zendesk account.
This is required because Zendesk (and you) need to
communicate with them via email. The user account contains
their email address and other personal data. These users
remain unverified in your Zendesk account, which is fine
because you don't require registration.

When unregistered users submit a support request, they receive an
email notification informing them that their request has
been received. They don't receive the new user welcome email
message. And, unlike when requiring registration, the ticket
is immediately added to your Zendesk Support instance.

See [Managing end user settings](https://support.zendesk.com/hc/en-us/articles/4408883052442)
for more information about setting up your Zendesk Support
instance to allow unregistered users.

### End user accounts created by agents

In addition to self-registration, your agents can manually add
end users. Administrators can bulk import a list of users
using a CSV file or add users via the Zendesk API.

If you require registration, you can [send a welcome
message](https://support.zendesk.com/hc/en-us/articles/4408824350746#topic_vcv_xqj_v1b) to the end users you've added. This
is an admin setting called **Also send a welcome email when
a new user is created by an agent or
administrator**. Choosing this setting prompts end
users to verify their email and choose a password just as if
they had created the user account themselves. If you don't
require registration, don't choose this option.

## Options for end-user sign-in

If you've decided that your end users must sign in to access Zendesk
Support, determine how you want to authenticate them so that you're
assured that they are who they say they are. You can use Zendesk's
user authentication (the standard sign-in process) or remotely
authenticate your end users outside of Zendesk and then seamlessly
sign them into your Zendesk Support instance. You can also allow
your end users to sign in using popular social media such as
Facebook and Google.

When discussing users that are authenticated outside of your Zendesk
account, you will see these terms: *single sign-on* (or SSO)
and *remote authentication*. *Single sign-on* is often
used interchangeably with *remote authentication*. For clarity,
it's best to think of *single sign-on* as allowing your users
to sign in to your Zendesk Support instance using a password from an
outside system. That's made possible by *remote
authentication*; users are authenticated outside of your Zendesk
account and then seamlessly sign in.

You can set one authentication method for end users and another for team
members (agents and admins). For example, you can specify stricter
password requirements for agents who have access to more sensitive
information. You can also provide different single sign-on options
for each set of users.

Zendesk provides a lot of flexibility regarding configuring sign-in
options for your users. You can offer multiple sign-in options and
let users choose how to sign in or require users to sign in using
SSO.

### Standard Zendesk sign-in

This is the user authentication that Zendesk provides. You set
your Zendesk account to require registration, and the end
user signs up (registers), verifies their email address, and
creates a password. They then sign in to your help center
using their email address and password. All user data is
contained and managed within your Zendesk account.

When you use the standard Zendesk sign-in process, you can
also:

- Set the security level for passwords, password
  expiration rules, and so on. See [Setting the
  password security level](https://support.zendesk.com/hc/en-us/articles/4408822149018#topic_tcn_ppr_2j).
- Turn on two-factor authentication for agents and
  administrators individually. After entering their
  password as usual, they'll be asked to enter a
  6-digit passcode. The passcodes can be received in
  text messages, or they can be generated by a
  two-factor authentication app installed on a
  mobile device. See [Managing two-factor
  authentication (2FA)](https://support.zendesk.com/hc/en-us/articles/4408826974874).

### Social and business SSO

In addition to the end user's Zendesk user account sign-in (email
address and password), you can allow your end users to sign
in to your Zendesk Support instance using their Facebook,
Google, and Microsoft accounts.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_security_end_user_login_no_X.png)

These social and business sign-in options are convenient for your
end users, so they don't need to remember another password
to sign in to your Zendesk account.

The social media account, rather than Zendesk, is authorized to
authenticate the end user. Zendesk trusts Facebook, for
example, to make sure that the user is who they say they
are.

Note: End users signing in to your Zendesk instance using
their personal Facebook account is different than
using the [Facebook
channel](https://support.zendesk.com/hc/en-us/articles/4408819897242) or [Facebook Messenger
channel](https://support.zendesk.com/hc/en-us/articles/4408835753370) in Zendesk. Facebook channels are
used to receive support requests and message
customers through Facebook.

For more information, see [Enabling social and business single
sign-on (SSO)](https://support.zendesk.com/hc/en-us/articles/4408885847962).

### Single sign-on with JSON Web Token (JWT)

You can also create a locally hosted custom remote authentication
script that connects to your external user management
system. This is possible using JSON Web Token (JWT). Single
sign-on is based on a shared secret between your local
authenticating script and Zendesk. This secret is used to
securely generate a hash (one-way encryption) that Zendesk
uses to ensure that users who sign in to your account using
remote authentication are who they claim to be and have been
pre-approved to do so by implicitly knowing the shared
secret.

For more information about JWT, see [Enabling JWT single sign-on](https://support.zendesk.com/hc/en-us/articles/4408845838874).

### Single sign-on with SAML

If you prefer to manage your users and their sign-in to your
Zendesk account yourself, you have the option of using
identity provider services such as OneLogin, Okta, and
PingIdentity. These use SAML (Secure Assertion Markup
Language) to store all your user data or connect to your
enterprise user management systems such as Active Directory
and LDAP.

You might set up your Zendesk sign-in this way if you're using
Zendesk Support as corporate IT help desk, for example. You
have complete control over your users; they don't need a
separate password to sign in to your Zendesk account.
Instead, when users visit your Zendesk Support instance and
attempt to sign in, they are seamlessly redirected to your
SAML server for authentication. When authenticated, users
are redirected back to your Zendesk Support instance and
automatically signed in.

The only user data in your Zendesk account is the user's email
address or an external ID you define.

For more information about setting up your Zendesk account to use
a SAML identity provider, see [Enabling SAML single
sign-on](https://support.zendesk.com/hc/en-us/articles/4408887505690).