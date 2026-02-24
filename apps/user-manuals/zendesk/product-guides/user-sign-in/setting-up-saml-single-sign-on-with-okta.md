# Setting up SAML single sign-on with Okta

Source: https://support.zendesk.com/hc/en-us/articles/4408821683738-Setting-up-SAML-single-sign-on-with-Okta

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Set up SAML single sign-on with Okta to streamline user authentication. Start by configuring SAML in Okta, then use the provided SAML SSO URL, Remote logout URL, and Certificate fingerprint to complete the setup. Assign SSO to users and manage authentication methods. Note: Switching from third-party SSO to native authentication requires users to reset their passwords.

Location: Admin Center > Account > Security > Single sign-on

Note: The tools described in this article were developed by a third party. Zendesk doesn't support the tools or guarantee results. For more information, see the [Okta documentation](https://www.okta.com/integrations/zendesk/).

Okta supports single sign-on with Zendesk using SAML (Security Assertion Markup Language).
For many of the settings used to configure single sign-on in Okta, you'll find much more detailed information in the Okta user interface. For more about Single sign-on using SAML support in Zendesk, see [Enabling SAML single sign-on](https://support.zendesk.com/hc/en-us/articles/4408887505690).

Configuring SAML must be done in both in your Okta account and in Zendesk. You start in Okta first and get the SAML information you'll need to complete the configuration in Zendesk.

This article includes the following topics:

- [Configuring SAML in Okta](#topic_ftq_dnq_l3)
- [Configuring SAML in Zendesk](#topic_1ms_gf3_l3)
- [Assign users to SAML single sign-on with Okta](#topic_jrq_mlr_jhb)
- [Switching authentication methods](#topic_xv5_sxq_j3b)

## Configuring SAML in Okta

Sign in to Okta as an administrator and then follow the steps below.

**To configure SAML for Zendesk in Okta**

1. In Okta, from the drop-down list in the upper-right corner, make sure you are using the **Classic UI** interface (not the **Developer Console**).
2. Select **Add Applications** from the dashboard.
3. Click **Add Application**, then search for and choose **Zendesk**. The Add Zendesk wizard appears.
4. On the first screen, **General Settings**, add a name for the application and your Zendesk subdomain. For example, if your Zendesk URL is *mycompany.zendesk.com*, enter *mycompany*). Click **Next**.
5. On the second screen, **Sign-On Options**, select **SAML 2.0**. This is where you'll find the **SAML SSO URL**, the **Remote logout URL**, and the **Certificate fingerprint (SHA2)**. You need this information to complete the SAML setup in Zendesk.
6. Click the **SAML 2.0 setup instructions for Zendesk** link.

   A page appears with instructions on how to configure SAML in Zendesk. See [Configuring SAML in Zendesk](#topic_1ms_gf3_l3) below for the latest information.
7. Copy the **SAML SSO URL**, the **Remote logout URL**, and the **Certificate fingerprint**.

   You need this information to configure SAML in Zendesk. When you've finished copying, close this window and return to your Okta dashboard.
8. (Optional) If you enable **User Management,** you'll be able to import users from Zendesk into your Okta account, provision new Zendesk accounts from Okta, and push Okta user profile updates and passwords to Zendesk.

   You'll find information about these Okta features in your Okta account and documentation.
9. (Optional) **People** allows you to select who in your Okta account has access to Zendesk. This step is not covered in this article. You'll find information about these Okta features in your Okta account and documentation.
10. When you've completed each step, click **Next** to complete and close the Zendesk configuration in Okta.

## Configuring SAML in Zendesk

When your Zendesk for Okta setup is complete and the information you need for setting up SAML in Zendesk is available, sign in to your Zendesk account as an admin and [enable SAML single sign-on](https://support.zendesk.com/hc/en-us/articles/4408887505690). You'll need the **SAML SSO URL**, the **Remote logout URL**, and the **Certificate fingerprint** from Okta to complete your set up.

Note: When you enable single sign-on via SAML or JWT, be aware that passwords do not expire even if your Zendesk password policy is set to high because passwords are not stored in Zendesk. Additionally, if agents manually add a Zendesk password to their account, these passwords will not expire.

## Assign users to SAML single sign-on with Okta

After configuring SAML single sign-on with Okta, assign this SSO option to end users, staff members (agents and administrators), or both. For more information, see [Assigning SAML SSO to users](https://support.zendesk.com/hc/en-us/articles/4408887505690-Using-SAML-for-single-sign-on-Plus-and-Enterprise-#topic_b15_1gd_jhb).

## Switching authentication methods

Important: If you use a third-party SSO method to create and authenticate users in Zendesk, then switch to Zendesk authentication, these users will not have a password available for login. To gain access, ask these users to reset their passwords from the Zendesk sign in page.