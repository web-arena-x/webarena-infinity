# Giving users different ways to sign into Zendesk

Source: https://support.zendesk.com/hc/en-us/articles/5380943678106-Giving-users-different-ways-to-sign-into-Zendesk

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

As described in [Understanding options for end-user access and
sign-in](https://support.zendesk.com/hc/en-us/articles/4408887573274#topic_ry4_2hk_v3), Zendesk offers multiple ways to authenticate team members and end
users.

Because users may have different security requirements, Zendesk gives you the flexibility
to allow multiple authentication methods for each type of user. For example, if you
configured SAML SSO for team member sign-in, you can provide another authentication
mechanism (such as email and password) if you have a subset of users who can’t sign in
through SSO.

This article covers the following topics:

- [Understanding the sign-in options](#topic_srs_ysq_kwb)
- [Giving team members multiple ways to sign in](#topic_ydn_bvq_kwb)
- [Giving end users multiple ways to sign in](#topic_mmt_qtn_swb)

Related articles:

- [Managing single sign-on (SSO)
  configurations](https://support.zendesk.com/hc/en-us/articles/4408882188570)
- [Single sign-on (SSO) options in
  Zendesk](https://support.zendesk.com/hc/en-us/articles/4408883587226)
- [Understanding options for end-user access and
  sign-in](https://support.zendesk.com/hc/en-us/articles/4408887573274)

## Understanding the sign-in options

When multiple authentication methods are active, you can configure the sign-in
experience for each user type by selecting **Let them choose** or **Redirect to
SSO**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_security_choose-sign_in.png)

**Let them choose** allows the user to sign in using any active authentication
method.

**Redirect to SSO** only allows users to authenticate using the [primary SSO configuration](https://support.zendesk.com/hc/en-us/articles/4408882188570#topic_c55_3sf_vsb). Users don’t see
additional sign-in options, even if those authentication options are active.

## Giving team members multiple ways to sign in

You can configure the sign-in experience so team members can choose how to sign in.
For example, if you have two SSO configurations and Zendesk authentication active
for team members, they would see a sign-in screen similar to the one below if you
select **Let them choose**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_security_team_member_login_SSO.png)

**To give team members multiple ways to sign in**

1. To provide [JSON Web Token (JWT)](https://support.zendesk.com/hc/en-us/articles/4408845838874), [Secure Assertion Markup Language
   (SAML)](https://support.zendesk.com/hc/en-us/articles/4408887505690), or [OpenID Connect (OIDC)](https://support.zendesk.com/hc/en-us/articles/7957465432474) SSO as a sign-in
   option to team members, you must first add the SSO configuration to the Single
   sign-on page in Admin Center, making sure that **Show button when users sign
   in** is selected.
2. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > Team member
   authentication**.
3. To provide email address and password as a sign-in option to team members,
   select **Zendesk authentication**, then [set the password security level](https://support.zendesk.com/hc/en-us/articles/4408822149018).
4. To provide SSO as a sign-in option for team members:
   1. Select **External authentication**.
   2. Select the SSO configurations (that you set up in step 1).
   3. Select the business account logins you'd like to make available to team
      members: **Google** or **Microsoft**. You can select one or both
      options.
5. For **How team members sign in**, select **Let them choose**.
6. Click **Save**.

## Giving end users multiple ways to sign in

You can configure the sign-in experience so end users can choose how to sign in. For
example, if you activate one SSO configuration, Zendesk authentication, and social
sign-ins for end users, they would see a sign-in screen similar to the one below if
you select **Let them choose**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_security_end_user_login_no_X.png)

**To give end users multiple ways to sign in**

1. To provide [JSON Web Token (JWT)](https://support.zendesk.com/hc/en-us/articles/4408845838874), [Secure Assertion Markup Language
   (SAML)](https://support.zendesk.com/hc/en-us/articles/4408887505690), or [OpenID Connect (OIDC)](https://support.zendesk.com/hc/en-us/articles/7957465432474) SSO as a sign-in
   option for end users, you must first add the SSO configuration to the Single
   sign-on page in Admin Center, making sure that **Show button when users sign
   in** is selected.
2. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > End user
   authentication**.
3. To provide email address and password as a sign-in option to end users, select
   **Zendesk authentication** and [set the password security level](https://support.zendesk.com/hc/en-us/articles/4408822149018).
4. To provide SSO as a sign-in option for end users:
   1. Select **External authentication**.
   2. Select the SSO configurations (that you set up in step 1).
   3. Select one or more social logins you'd like to make available to end
      users: **Google**, **Microsoft**, or **Facebook**.
5. For **How end users sign in**, select **Let them choose**.
6. Click **Save**.