# Accessing your Zendesk account when your SSO service is down

Source: https://support.zendesk.com/hc/en-us/articles/4408882128666-Accessing-your-Zendesk-account-when-your-SSO-service-is-down

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

You can still access your account if your single sign-on (SSO) service goes down. The method
you use to regain access depends on whether Zendesk passwords are turned on.

For security reasons, Zendesk can't turn off SSO for your account to help you regain access.
However, the [account owner](https://support.zendesk.com/hc/en-us/articles/4408822084634) can always bypass SSO, and account
settings can be adjusted to allow all admins this capability.

This article covers the following topics:

- [Accessing the account if passwords are off](#topic_afy_4r3_4z)
- [Accessing the account if passwords are turned on](#topic_xtw_4r3_4z)

Related articles:

- [Enabling social and business SSO](https://support.zendesk.com/hc/en-us/articles/4408885847962#topic_nxw_j4m_h3)
- [Enabling JWT SSO](https://support.zendesk.com/hc/en-us/articles/4408845838874#topic_gds_ydj_zj)
- [Enabling SAML SSO](https://support.zendesk.com/hc/en-us/articles/4408887505690#topic_1ms_gf3_l3)

## Accessing the account if passwords are off

As described in [Giving users different ways to sign into Zendesk](https://support.zendesk.com/hc/en-us/articles/5380943678106),
you can turn off the email and password sign-in method (called *Zendesk
authentication*) when you turn on SSO for your account.

If Zendesk passwords are turned off and your SSO service is interrupted, you can still
access the account by using the SSO bypass feature to request a one-time access link. SSO
bypass is available only to the account owner or to the account owner and admins.

### Selecting which users can bypass SSO if passwords are turned off

The account owner can configure whether all admins or only the account owner can request
an email containing a one-time access link.

**To select the users who can bypass SSO**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > Advanced**.
2. Click the **Authentication** tab.
3. In the **SSO bypass** field, select whether the **Account owner** or all
   **Admins** (including the account owner) can gain access to the account if the
   external sign-in provider goes down.

   The **SSO bypass** field only displays for the
   account owner when Zendesk authentication is turned off for team members.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/admin_center_sso_bypass.png)
4. Click **Save**.

### Accessing the account by requesting a one-time access link

If Zendesk passwords are turned off and your SSO service is interrupted, admins or the
account owner can still access the account by requesting a one-time access link. Zendesk
sends the link in an email.

Clicking the link grants you access with no password required. The link only works once
and times out after 5 minutes.

Note: If your email address is protected by certain spam filters, the
filter may invalidate the access link by clicking it. If your spam filters perform this
kind of email link-checking, you may be unable to use this option.

**To receive a one-time access link**

1. Browse to `https://your_subdomain.zendesk.com/access/sso_bypass`, where
   **your\_subdomain** is your account name.
2. Enter and submit the email address associated with your Zendesk user profile.
3. Check your email, then click the link in the email to sign in.

## Accessing the account if passwords are turned on

If Zendesk passwords are turned on, agents and admins with a Zendesk username and password
can still access the account by browsing to a specific URL.

**To sign in**

1. Browse to `https://your_subdomain.zendesk.com/access/normal`, where
   **your\_subdomain** is your account name.
2. Enter the username and password associated with your Zendesk account.

If you're still having trouble signing in, consider the following:

- If your company uses SSO, the username and password you use for SSO may differ from
  the username and password stored in the backup Zendesk authentication system. Your
  Zendesk username is listed as the primary email address in your Zendesk user
  profile.
- If you remember your username but do not remember your Zendesk password, [reset your password](https://support.zendesk.com/hc/en-us/articles/4408843565722-How-do-I-reset-my-password-when-I-can-t-sign-in), then try signing in again.