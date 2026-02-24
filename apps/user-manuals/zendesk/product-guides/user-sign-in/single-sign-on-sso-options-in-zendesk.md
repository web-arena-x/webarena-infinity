# Single sign-on (SSO) options in Zendesk

Source: https://support.zendesk.com/hc/en-us/articles/4408883587226-Single-sign-on-SSO-options-in-Zendesk

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Single sign-on (SSO) options let you authenticate users externally, enhancing security and user management. You can choose from social, business, or enterprise SSO methods like SAML, OIDC, or JWT. Ensure email verification with your identity provider. Configure multiple SSO setups for different user groups, and maintain access control even if your SSO service is down.

In addition to the user authentication provided by Zendesk, you can also use
single sign-on (SSO) to authenticate your users outside of Zendesk. There
are three types of SSO: social account, business account, and enterprise.

Zendesk recommends configuring and enforcing SSO for all admins and agents, if
possible. Email addresses are used as user IDs, so when using SSO, it is
critical that email addresses associated with users provisioned by the
identity provider are verified.

This article covers the following topics:

- [Essential facts for
  SSO](#topic_a5v_1pm_pz)
- [Social and business account
  SSO](#topic_v5q_hnm_yj)
- [Enterprise SSO](#topic_ftf_knm_yj)

Related articles:

- [Giving users
  different ways to sign into Zendesk](https://support.zendesk.com/hc/en-us/articles/5380943678106)
- [Enabling JWT single
  sign-on](https://support.zendesk.com/hc/en-us/articles/4408845838874)
- [Enabling SAML single
  sign-on](https://support.zendesk.com/hc/en-us/articles/4408887505690)
- [Setting up single
  sign-on with OpenID Connect (OIDC)](https://support.zendesk.com/hc/en-us/articles/7957465432474)

## Essential facts for SSO

Below are some essential facts about the available SSO options. These are
explained in greater detail in this article.

- Admins and agents can sign in with their Google,
  Microsoft, and Zendesk accounts, or can sign in
  directly by going to their Zendesk URL and entering
  their username and password. End users can sign in
  with social accounts and their Zendesk
  accounts.
- If your Zendesk account is closed or restricted, and a
  user tries to sign in with a different email than
  the one registered in Zendesk Support, their request
  will be rejected.
- You can have multiple active SAML, JWT, and OpenID
  Connect (OIDC) SSO configurations, which can be
  assigned to different collections of users. Each
  will have their own remote sign-in pages.
- No matter what authentication method you choose, Zendesk
  stores all users in the same database.
- If you're using a third-party identity provider to
  authenticate, you must configure the Zendesk app
  with the identity provider.
- It is not possible to apply different SSO options to
  individual brands, unless you use [a custom script for
  JWT](https://support.zendesk.com/hc/en-us/articles/4408886711066-Multibrand-Using-multiple-JWT-Single-Sign-on-URL-s-Professional-Add-on-and-Enterprise-).
- If you place a wildcard (\*) in the blocklist, users will
  no longer be able to authenticate or create an
  account with SSO. See [Using the allowlist and blocklist
  to control access to your
  Zendesk](https://support.zendesk.com/hc/en-us/articles/4408886840986).

## Social and business account SSO

Social and business account SSO are additional sign-in options you can
provide for your users' convenience. You can make these available on
your help center sign-in page so that users can authenticate with
their Zendesk Support account or a social or business account.

- Agents and admins can use Google and Microsoft
  (Microsoft Entra ID and Office 365) SSO methods to
  log into their *business* accounts.
- End users can use Facebook, Google, and Microsoft SSO
  methods using their *social/personal*
  accounts.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_security_end_user_login_no_X.png)

When using business account SSO, it's important to note that the Google
sign-in supports both Gmail and Google Workspace.

To add social and business account SSO to your sign-in page, see [Enabling social and business account single
sign-on](https://support.zendesk.com/hc/en-us/articles/4408885847962).

## Enterprise SSO

You can require users to sign in using enterprise SSO, or you can
activate multiple sign-in options (for example, enterprise SSO
*and* Zendesk authentication) and let users decide how
they want to sign in. (The word "enterprise" in this context doesn't
refer to Zendesk Enterprise plans.) See [Giving users different ways to sign into Zendesk](https://support.zendesk.com/hc/en-us/articles/5380943678106).

Important: When you use Enterprise SSO,
you are responsible for verifying your users' identities, including
their email addresses. If you don't verify your users and their
email addresses, your account is at risk of unauthorized access, and
Zendesk cannot guarantee or warrant the security of your account.

This section contains the following topics:

- [About
  enterprise SSO](#topic_n42_lph_4z)
- [Enterprise
  SSO options](#topic_ftf_knm_yj)

### About enterprise SSO

When you direct users to enterprise SSO, you're bypassing Zendesk
and authenticating your users externally. When users
navigate to your Zendesk sign-in page or click a link to
access your Zendesk account, they can authenticate by
signing into a corporate server or a third-party identity
provider, such as OneLogin or Okta. Enabling enterprise SSO
also affects the iOS and Android versions of the Zendesk
mobile app.

Note: It isn't possible to enable enterprise SSO for individual
brands, unless you use [a custom script for
JWT SSO](https://support.zendesk.com/hc/en-us/articles/4408886711066-Multibrand-Using-multiple-JWT-Single-Sign-on-URL-s-Professional-Add-on-and-Enterprise-).

If you're using enterprise SSO, your users' sign-in flow will
follow the sequence below:

1. Users navigate to a Zendesk page or
   subdomain.
2. If not already authenticated, users are
   redirected to your corporate server or third-party
   identity provider sign-in page, depending on the
   enterprise SSO option you selected.
3. Users enter their sign-in credentials.
4. If valid, users are redirected back to the
   original Zendesk page.

Note: Users can also start the sign-on process from
your corporate server or the third-party identity
provider sign-in page. They will then be
authenticated automatically when accessing Zendesk.

Both your end users and team members can sign in to your Zendesk
using enterprise SSO. You can configure enterprise SSO only
for end users, team members, or a mix of both. Users
authenticating through Zendesk end-user SSO are assigned the
role specified in Zendesk, which may include team member
access.

The advantage of using enterprise SSO is that you have complete
control over your users behind your firewall. You
authenticate your users once, against your own user
authentication system, and then grant them access to many
other resources both inside and outside of your firewall.
Your user management is performed outside of Zendesk, but
your corporate user authentication system is still synced
with Zendesk. When you add a user account for a new
employee, they will have immediate access to Zendesk, or if
you delete a user account, that employee will no longer have
access to Zendesk.

By default, the only data that Zendesk stores for each user is
their name and email address, but it's possible to sync more
user data to Zendesk, like the user's organization.

You have the option of keeping Zendesk authentication with your
enterprise SSO authentication. If you decide to turn off
Zendesk authentication, all Zendesk user passwords will be
permanently deleted within 24 hours.

If your SSO service is temporarily unavailable, you can still
access your Zendesk account. See [Accessing your
Zendesk account when your SSO service is
down](https://support.zendesk.com/hc/en-us/articles/4408882128666).

### Enterprise SSO options

There are three enterprise SSO options available in Zendesk:

- **Secure Assertion Markup Language (SAML)**:
  SAML is supported by many identity provider
  services, such as Okta, OneLogin, Active
  Directory, and LDAP. For information on
  configuring SAML SSO, see [Enabling SAML single
  sign-on](https://support.zendesk.com/hc/en-us/articles/4408887505690).
- **OpenID Connect (OIDC)**: Built on the OAuth
  2.0 framework, OIDC uses ID tokens to verify the
  identity of users based on the authentication
  performed by an authorization server. See [Setting up single
  sign-on with OpenID Connect (OIDC)](https://support.zendesk.com/hc/en-us/articles/7957465432474).
- **JSON Web Token (JWT)**: Credentials and
  user information is sent in JSON format encrypted
  using a Zendesk Shared Secret. For information on
  configuring JWT SSO, see [Enabling JWT single
  sign-on](https://support.zendesk.com/hc/en-us/articles/4408845838874).

You can use the same option for all users or different options
for different collections of users. This is ideal if you
have separate sets of users in different locations that you
don't want to merge. If you use more than one enterprise SSO
configuration, you can present users with multiple SSO
sign-in options on the Zendesk sign-in page or redirect
users to the primary SSO. See [Giving users
different ways to sign into Zendesk](https://support.zendesk.com/hc/en-us/articles/5380943678106).