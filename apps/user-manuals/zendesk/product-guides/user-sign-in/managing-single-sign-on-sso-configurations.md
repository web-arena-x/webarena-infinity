# Managing single sign-on (SSO) configurations

Source: https://support.zendesk.com/hc/en-us/articles/4408882188570-Managing-single-sign-on-SSO-configurations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location: Admin Center > Account > Security > Single sign-on

Zendesk provides the ability to create multiple SSO authentication configurations for different collections of users. This could be as simple as one authentication policy for end users and another for team members, or as complex as different authentication policies for specific [groups and organizations](https://support.zendesk.com/hc/en-us/articles/4408886146842) of users.

See the following articles to learn how to create your SSO configurations, depending on the authentication protocols you're using:

- [Enabling SAML single sign-on](https://support.zendesk.com/hc/en-us/articles/4408887505690)
- [Setting up single sign-on with OpenID Connect (OIDC)](https://support.zendesk.com/hc/en-us/articles/7957465432474)
- [Enabling JWT single sign-on](https://support.zendesk.com/hc/en-us/articles/4408845838874)

After you've created your SSO configurations, you can view and manage them on the Single sign-on page in Admin Center.

This article covers the following topics:

- [Viewing your SSO configurations](#topic_jyz_2bz_5sb)
- [Editing SSO configurations](#topic_gz4_qbz_5sb)
- [Activating or deactivating SSO configurations](#topic_vzw_tbz_5sb)
- [Setting the primary SSO configuration](#topic_c55_3sf_vsb)
- [Adding "Continue with SSO" buttons to the Zendesk sign-in page](#topic_rqg_yw4_2yb)
- [Deleting SSO configurations](#topic_tq5_jvf_2yb)

## Viewing your SSO configurations

Your SSO configurations display on the Single sign-on page in Admin Center in a list sorted from newest to oldest. The list includes the configuration's name, the type of configuration (SAML, OIDC, or JWT), which types of users it's assigned to, and whether it's active or inactive.

**To view your SSO configurations**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
 **Account** in the sidebar, then select **Security > Single sign-on**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/auth_sso_configs.png)

## Editing SSO configurations

You may need to edit your SSO configurations after you create them. For example, you may need to create a new shared secret for a JWT configuration or update the remote login page URL.

**To edit an SSO configuration**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > Single sign-on**.
2. Click the option menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) and select **Edit** for the SSO configuration you want to edit.

## Activating or deactivating SSO configurations

SSO configurations are active when they are assigned to either team members or end users. To inactivate an SSO configuration, you must unassign it from both team members and end users, if applicable.

**To activate or deactivate an SSO configuration**

1. Open the Security settings for team members or end users:
   - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
     **Account** in the sidebar, then select **Security > Team member authentication**.
   - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
     **Account** in the sidebar, then select **Security > End user authentication**.
2. Under **External authentication** > **Single sign-on (SSO)**, select the configuration you want to activate. To inactivate a configuration, clear the check box.
3. Click **Save**.

## Setting the primary SSO configuration

Depending on how you require users to sign in, you might need to set an SSO configuration as the primary SSO method for team members or end users. As described in [Giving users different ways to sign into Zendesk](https://support.zendesk.com/hc/en-us/articles/5380943678106), you can configure the sign-in experience one of two ways:

- **Let them choose**: Display all active authentication options on the sign-in page and allow users to choose how they sign in, or
- **Redirect to SSO**: Require users to sign in using the primary SSO method.

You only have to set a primary SSO method if you redirect to SSO *and* have multiple SSO configurations active. Zendesk tries to determine whether an unauthenticated user is an end user or team member and routes them to the remote login page of the primary SSO.

**To set a primary SSO method**

1. Open the Security settings for team members or end users.
   - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
     **Account** in the sidebar, then select **Security > Team member authentication**.
   - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
     **Account** in the sidebar, then select **Security > End user authentication**.
2. For **Primary SSO**, select the name of the SSO configuration you want to send users to by default.

   The **Primary SSO** field is visible if you have multiple SSO configurations active and you've selected **Redirect to SSO**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/auth_primary_SSO_2.png)
3. Click **Save**.

## Adding "Continue with SSO" buttons to the Zendesk sign-in page

If you [let users choose how to sign in](https://support.zendesk.com/hc/en-us/articles/5380943678106), you can show a **Continue with SSO** button on the Zendesk sign-in page for each active SSO configuration. Customize the button labels so they are meaningful to your users.
If you offer multiple SSO sign-in methods, create unique labels so users know which option to choose.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_security_team_member_login_SSO.png)

You might not authenticate users this way. For example, if your users only sign in using an identity provider (Idp-initiated SSO), you don't have to add SSO buttons because your users don't use the Zendesk sign-in page.

**To add an SSO button to the Zendesk sign-in page**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > Single sign-on**.
2. Click the option menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) and select **Edit** for the SSO configuration you want to add to the sign-in page.
3. Scroll to the bottom of the page and select **Show button when users sign in**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/auth_show_sso_button.png)
4. In the **Button name** field, enter the text that should follow "Continue with."

   For example, typing **team member SSO** creates a button labeled **Continue with team member SSO**.
5. Click **Save**.
6. If the SSO configuration is inactive, [activate it](#topic_vzw_tbz_5sb) by assigning it to team members or end users.

## Deleting SSO configurations

You can delete inactive SSO configurations.

**To delete an SSO configuration**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > Single sign-on**.
2. If the configuration you want to delete is active, deactivate it first. See [Activating or deactivating SSO configurations](#topic_vzw_tbz_5sb).
3. Click the option menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) and select **Delete** for the SSO configuration you want to delete.