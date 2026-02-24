# Setting up Single Sign On (SSO) for Sell accounts

Source: https://support.zendesk.com/hc/en-us/articles/4408833582746-Setting-up-Single-Sign-On-SSO-for-Sell-accounts

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

Single Sign On (SSO) is available across all Sell plans for Zendesk Sell accounts. If
your Sell account was created after January 7, 2020, or has been migrated to Zendesk,
then it is a Zendesk Sell account. If your account was created before January 7, 2020,
and has not yet been migrated, then it is a legacy Sell account.

This article covers the following topics:

- [Zendesk Sell accounts: Setting up
  SSO](#topic_lzr_xxc_qnb)
- [Legacy Sell accounts: Setting up
  SSO](#topic_a2w_fyc_qnb)
- [Logging in to Zendesk Sell with
  SSO enabled](#topic_ojq_gyc_qnb)

## Setting up SSO for Zendesk Sell accounts

For Zendesk accounts, all SSO settings are managed through the Zendesk Admin
Center.

**To set up SSO for a Zendesk Sell account**

1. If you have multiple Zendesk products, you can access the Admin Center directly
   from your [Product Tray](https://support.zendesk.com/hc/en-us/articles/4408839227290-Using-Zendesk-Admin-Center).

   Alternatively, in
   Sell, click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then select **[Integrations > Single Sign On](https://app.futuresimple.com/settings/sso)**.
2. Click **Configure**.

   A new window opens for the Zendesk Admin
   Center.
3. Follow the guidance in [Enabling SAML single sign-on](../user-sign-in/enabling-saml-single-sign-on.md#topic_1ms_gf3_l3) or [Enabling JWT single sign-on](https://support.zendesk.com/hc/en-us/articles/4408845838874) to set up
   SSO.

## Setting up SSO for legacy Sell accounts

For legacy Sell accounts, all SSO settings are managed
directly in Sell. You must have admin rights to set up SSO in Sell.

**To set up
SSO for a legacy Sell account**

1. In Sell, click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then select **[Integrations > Single Sign On](https://app.futuresimple.com/settings/sso)**.
2. Click **Configure**.

   You'll see the Zendesk Sell account UUID, Service
   Provider Issuer ID, and Service Provider Assertion Consumer Service URL
   information on this page. You'll need to provide this information to
   your identity provider.
3. Select **Automatic Setup** or **Manual Setup**.
4. If you select **Automatic Setup**, enter the metadata URL for your
   identity provider.

   Most identity providers offer one URL to transfer this
   information.
5. If your Identity Provider doesn't provide a single URL for configuration,
   select **Manual Setup**, then enter the following information:
   - Identity Provider Issuer ID, for example, <http://yourdomain/adfs/services/trust>.
   - Identity Provider SSO URL, for example, <https://yourdomain/adfs/ls>.
   - Identity Provider certificate fingerprint. This is the SHA-1
     fingerprint of the token signing certificate installed in the ADFS
     instance.
6. Click **Save**.

   You have now configured your SSO settings.

   The
   following table lists the parameter name, parameter value, and any
   comments about each SSO setting.

   |  |  |  |
   | --- | --- | --- |
   | **Parameter Name** | **Parameter Value** | **Comments** |
   | Single Sign On URL | Service Provider Assertion Consumer Service URL value from Zendesk Sell settings | This is a custom URL for each Zendesk Sell account, based on UUID generated during SSO configuration.  The same value should be used for Recipient URL and Destination URL if these are defined independently. |
   | Audience Restriction | Service Provider Issuer ID value from Zendesk Sell settings | This is a custom URL for each Zendesk Sell account, based on UUID generated during SSO configuration. |
   | NameID Format | EmailAddress |  |
   | Application Username | Email |  |
   | Response | Signed |  |
   | Assertion | Signed & Encrypted |  |
   | Signature Algorithm | RSA-SHA1 |  |
   | Digest Algorithm | SHA1 |  |
   | Single Log Out URL |  | Leave this empty, as it is not supported. |
   | Default RelayState |  | Leave this empty, as it is not supported. |

## Logging in to Zendesk Sell with SSO enabled

With SSO enabled, users continue to log in to Zendesk Sell from their default login
page, but you'll need to enter the email address registered to Sell, that is, your
login email.

Zendesk Sell automatically verifies the email address against your identity provider,
and if you're already logged in to your identity provider, you'll be automatically
logged into Sell.

If you're not already logged into your identity provider, you'll be redirected to
their login page to enter your login details. As soon as you're authenticated,
you'll be automatically logged into Zendesk Sell.

If you're logging in from a Sell mobile app, enter your Zendesk Sell email address in
order to begin the sign in process on your device. Depending on your device, you'll
be redirected to your browser or your identity provider's app to complete sign in.

If you're an administrator on your Zendesk Sell account, you'll be able to select an
option to log in with an email and password on the login page. All non-administrator
users will need to use SSO to log in.

You need administrator rights to change the email address registered to Sell.
Non-admin accounts won't be able to change the email address used to log in.