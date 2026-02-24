# Enabling social and business single sign-on (SSO)

Source: https://support.zendesk.com/hc/en-us/articles/4408885847962-Enabling-social-and-business-single-sign-on-SSO

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location:  Admin Center > Account > Security

You can provide your users with more options for signing in to Zendesk Support by
allowing them to use their existing social and business accounts.

- Agents and admins can use Google and Microsoft (Microsoft Entra ID and Office 365)
  SSO methods to sign into their *business* accounts.
- End users can use Facebook, Google, and Microsoft SSO methods using their
  *social/personal* accounts.

Note: End users can only use Microsoft SSO if their Microsoft identity
is from a personal Microsoft account (services like Xbox, Teams for Life, or Outlook).
End users who attempt to sign in with a Microsoft Entra ID identity won't be able to
authenticate. You can enable [SAML-based SSO](https://support.zendesk.com/hc/en-us/articles/4408887505690) for your end users if you wish to allow that
option.

This article covers the following topics:

- [How social and business SSO works](#topic_5sh_rkg_fj)
- [Enabling social and business SSO](#topic_nxw_j4m_h3)
- [First authentication
  process](#topic_lmh_4vq_kxb)

Related articles:

- [Single sign-on (SSO) options in
  Zendesk](single-sign-on-sso-options-in-zendesk.md#topic_ftf_knm_yj)
- [Giving users different ways to sign into Zendesk](https://support.zendesk.com/hc/en-us/articles/5380943678106)

## How social and business SSO works

Social and business single sign-on allows team members to access Zendesk using their
Google and Microsoft business accounts, and end users to access Zendesk using their
personal Facebook, Google, or Microsoft accounts.

When you turn on these SSO methods and select **Let them choose** on the team
member or end user authentication page, sign-in buttons for each active SSO method
are added to your help center page. In the example below, the end user can log in
using any of their personal Facebook, Google, or Microsoft accounts.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_security_end_user_login_no_X.png)

If you select **Redirect to SSO**, users will be automatically redirected to the
[primary SSO](https://support.zendesk.com/hc/en-us/articles/4408882188570#topic_c55_3sf_vsb).

Your users' social and business account sign-in credentials (username and password)
are never shared with Zendesk. Only the primary email address contained in the
social and business account is shared.

## Enabling social and business SSO

You can enable social SSO (for end users) and business SSO (for team members) without
any custom configuration. To learn more about how the authentication process works
after you enable, see [First
authentication process](#topic_lmh_4vq_kxb).

If you use a third-party sign-in service, ensure you are verifying and managing user
identities in the external platform to prevent unauthorized access to your Zendesk
account.

**To enable business SSO for users**

1. Open the authentication page for either team members or end users:
   - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
     **Account** in the sidebar, then select **Security > Team member
     authentication**.
   - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
     **Account** in the sidebar, then select **Security > End user
     authentication**.

     End user options are not available until you [set up and activate your help
     center](https://support.zendesk.com/hc/en-us/articles/4408846795674).
2. Select **External authentication** to display options for
   third-party sign-in services.
3. Select each of the business/personal or social accounts you'd like to allow
   users to sign in with.

   For end users, if you select Microsoft, they can
   sign in with Microsoft identities managed through a personal Microsoft
   account (for instance, services like Xbox, Teams for Life, or
   Outlook).
4. (For team members only) If you selected Microsoft, you must provide the
   [tenant IDs](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-how-to-find-tenant) for the Microsoft Entra
   ID tenants that are permitted to access your Zendesk account (also required
   for Office 365) by entering them in the **Allowed tenant IDs** field,
   separated with spaces.
5. Select an option for **How team members sign in**:
   - **Let them choose** allows users to sign in using any active
     authentication method. If you select this option, the sign-in links
     for each option appear on your help center sign-in page.
   - **Redirect to SSO** only allows users to authenticate using the
     [primary SSO configuration](https://support.zendesk.com/hc/en-us/articles/4408882188570#topic_c55_3sf_vsb).
     If you select this option, and you have selected multiple
     third-party sign-in services, select the primary SSO configuration
     in the **Primary SSO** field that appears.
6. Click **Save**.

Note: If your SSO service goes down or you are locked out, you can
still access your account using the  [Zendesk SSO bypass functionality](https://support.zendesk.com/hc/en-us/articles/4408882128666).

## First authentication process

When you enable social and business SSO options and select **Let them choose**, a
user's first authentication process follows this sequence:

1. Users select one of the social or business sign-on options on your Zendesk
   account sign-in page.
2. Users will be redirected to their social or business sign-in page and must
   enter their credentials.
3. If the credentials are valid, users will be redirected back to your Zendesk
   Support account.

If the email address matches a user's email address in Zendesk, they are signed in.

If the email address does not match a user in Zendesk, a new user will be created,
and Zendesk will send a verification email. If the user is a duplicate of a
pre-existing Zendesk user, you can [merge the users](https://support.zendesk.com/hc/en-us/articles/4408887695898).

If your Zendesk account is closed or restricted and a user tries to sign in with a
business or social account email that does not exist in Zendesk, their request to
authenticate is rejected. To allow a user to sign in with a social or business
account that uses a different email, you must [add the account email](https://support.zendesk.com/hc/en-us/articles/4408822763546#topic_zb2_22c_ppb) to their user
profile.

After authenticating, the user is seamlessly signed in to Zendesk. On subsequent
visits, if the user is already signed in to their social or business account, they
are immediately signed in to Zendesk when they click the associated social or
business sign-on button. Otherwise, they are prompted to sign in to their social or
business account.