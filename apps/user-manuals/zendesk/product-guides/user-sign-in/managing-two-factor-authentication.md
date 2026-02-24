# Managing two-factor authentication

Source: https://support.zendesk.com/hc/en-us/articles/4408826974874-Managing-two-factor-authentication

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Enhance security by enabling two-factor authentication, requiring users to verify their identity with a passcode. This feature reduces unauthorized access risks and is applicable to users signing in with email and password. You can track usage with a 2FA status report and have the option to turn it off if needed. Note that it doesn't affect API calls using an API token.

Location:  Admin Center > Account > Security >
Advanced

Two-factor authentication is an added security layer that requires users to verify their identity
after signing in using a passcode, reducing the risk of unauthorized access.
You can require two-factor authentication, or each user can set up
two-factor authentication for their own use.

Two-factor authentication applies to users who sign in to your Zendesk using Zendesk
authentication (email and password). It's not available for users who sign
in using third-party authentication, such as Google authentication services,
JWT, or SAML. However, these users might still be able to use third-party
two-factor authentication, such as Google 2-Step Verification, if you're
using Google authentication.

Zendesk recommends turning on two-factor authentication to help protect against
potential situations that could result in an admin or agent account being
compromised, such as a leaked password. If you require two-factor
authentication, it's a good idea to periodically generate a 2FA status
report to track who's using two-factor authentication to access their
Zendesk account.

This article covers the following topics:

- [Important considerations before turning on two-factor authentication](#topic_ebn_v44_hwb)
- [Requiring two-factor authentication on the account](#topic_mzk_l5b_dx)
- [Tracking who's using two-factor authentication](#topic_vjq_fgk_gs)
- [Turning off two-factor authentication](#topic_ryl_c5z_kgc)

Related articles:

- [Getting recovery codes for team members locked out of their accounts](https://support.zendesk.com/hc/en-us/articles/8197977742874)
- [Understanding options for end-user access and sign-in](https://support.zendesk.com/hc/en-us/articles/4408887573274)

## Important considerations before turning on two-factor authentication

Before turning on two-factor authentication, make sure you understand the
following important considerations:

- You can use two-factor authentication on the Zendesk
  website or with the Zendesk iOS or Android apps.
  However, the Zendesk REST API doesn't currently
  support two-factor authentication. See [Using the API when SSO or
  two-factor authentication is enabled](https://developer.zendesk.com/documentation/ticketing/using-the-zendesk-api/using-the-api-with-2-factor-authentication-enabled) in the
  developer documentation.
- Requiring two-factor authentication turns off
  password-based authentication to the Zendesk API.
  Zendesk recommends moving to another authentication
  method for API calls as soon as possible because
  password access [will be
  removed](https://support.zendesk.com/hc/en-us/articles/7386291855386) in January 2026.
- Requiring two-factor authentication does not impact API
  calls that are using an [API token](https://developer.zendesk.com/api-reference/introduction/security-and-auth/#api-token).

## Requiring two-factor authentication on the account

You can require two-factor authentication for all team members, all end users, or both user
types. Once this setting is turned on, users will be required to set
up two-factor authentication the next time they sign in. Users see
the following dialog after entering their email and password.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/2FA_start_setup.png)

The two-factor authentication wizard guides users through the process,
which includes options for how they'd like to receive a passcode:
authenticator app, email, or SMS.

You can optionally notify users of the change and include a link to an
article for more information about two-factor authentication:

- For admins and agents: [Using two-factor authentication
  to sign in to Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408829277466)
- For end users: [Accessing help
  center with two-factor authentication](https://support.zendesk.com/hc/en-us/articles/6429382053530)

When you require two-factor authentication, users are prompted for a
passcode every time they sign in.

**To require two-factor authentication**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > Advanced**.
2. Click the **Authentication** tab.
3. Select the options that apply:
   - **Require two-factor authentication (2FA) for
     team members**
   - **Require two-factor authentication (2FA) for
     end users**
4. Click **Save**.

## Tracking who's using two-factor authentication

You can generate a 2FA status report, in the form of a CSV spreadsheet, listing all the admins
and agents in your account and whether or not they're using
two-factor authentication. It's a good idea to do this periodically
if you require two-factor authentication. This option is not
available to track end users.

**To generate a 2FA status report**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > Advanced**.
2. Click the **Authentication** tab.
3. Click **Generate 2FA status report**.
4. Check your Zendesk email. You should get an email shortly with a link to download the spreadsheet.

## Turning off two-factor authentication

You can turn off two-factor authentication if you no longer want to
require it on your account. After you turn it off, users will no
longer be required to enter a passcode when signing in, unless they
have turned on two-factor authentication for themselves in their
profile.

If you turned off two-factor authentication but users are still being
prompted for a passcode, users can refer to the following resources
to turn it off:

- For agents: [Turning off
  two-factor authentication](https://support.zendesk.com/hc/en-us/articles/4408829277466#topic_p3p_zhk_gs)
- For end users: [Turning off
  two-factor authentication](https://support.zendesk.com/hc/en-us/articles/6429382053530)

**To turn off two-factor authentication**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > Advanced**.
2. Click the **Authentication** tab.
3. Deselect the options that apply:
   - **Require two-factor authentication (2FA) for
     team members**
   - **Require two-factor authentication (2FA) for
     end users**
4. Click **Save**.