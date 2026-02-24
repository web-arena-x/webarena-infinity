# Connecting your email with Zendesk Sell

Source: https://support.zendesk.com/hc/en-us/articles/4408821242266-Connecting-your-email-with-Zendesk-Sell

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

Important: Enabling this functionality leverages Google API Services.
Zendesk’s use and transfer to any other app of information received through the
Google API Services connecting Zendesk Sell to your Gmail accounts will adhere to
Google's Limited Use Requirements described in the [Google API Services: User Data
Policy](https://developers.google.com/terms/api-services-user-data-policy).

The Sell email integration allows you to sync your existing email account to Sell, and
gives you greater visibility into your sales process. Other benefits include, for
example:

- Never missing a conversation with a prospect
- Knowing when your prospect opens, clicks and replies to emails in real-time
- Saves you time by auto-populating personalized emails

This article covers the following topics:

- [Connecting your Microsoft Office
  365 email](#topic_m1g_xgp_z4b)
- [Connecting your Google email
  (Gmail users)](#topic_kdp_wgp_z4b)
- [Connecting your email (other
  users)](#topic_dtp_xgp_z4b)
- [Troubleshooting email integration
  issues](#topic_jkd_ygp_z4b)
- [Next steps with your Sell
  email](#topic_vdq_ygp_z4b)

Related articles:

- [Sell email resource guide](https://support.zendesk.com/hc/en-us/articles/4627545703322)

## Connecting your Microsoft Office 365 email

The process for connecting your Microsoft Office 365 email account with
Sell is different depending on whether you have an existing connection or are
connecting your Microsoft Office 365 email account to Sell for the first time.
Everyone connecting their Microsoft Office 365 email account to Sell must follow
these instructions.

**Existing connections to Sell** - Use basic authentication to connect
your Microsoft Office 365 email account to Sell.

**New connections to Sell** - Use OAuth token-based authorization to connect
your Microsoft email account to Sell (by default).

Note: Make sure that SMTP protocol is enabled in your Microsoft Office 365 instance.

The benefits of using OAuth 2.0 token-based authorization:

- Users can enable multi-factor authentication in Microsoft Office 365 without
  any impact on their email connection
- Users can change their password in Microsoft Office 365 without any impact
  on their email connection, because Sell is authorized using tokens instead
  of passwords.

**To update your existing email connection with Sell from basic
authentication to OAuth token-based authorization**

Important: Do not disconnect and reconnect your existing basic
authentication email connection using the sign in with Microsoft option.

1. Sign in to Sell.
2. Sign in to Microsoft Office 365 on the same web browser you used to
   sign in to Sell.
3. Click the following link to create a private token and to sign in as
   per the standard OAuth2 flow. <https://app.futuresimple.com/apis/oauth2_connector/api/v1/oauth2/office365_mailman/authorize.json?reconnect=true>

Your email connection from Microsoft Office 365 to Sell is now updated to a
multi-factor connection.

**To connect your Microsoft email account to Sell for the first
time**

1. On the Sell sidebar, click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then click **[Communication Channels > Email](https://app.futuresimple.com/settings/email)**.
2. Click **Sign in with Microsoft**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_email_sign_in_microsoft.png)
3. If you've never signed in to your Microsoft account from your current browser or
   session, enter your Microsoft email address (your primary email address must be
   the same as your username) and your password, then click **Sign in**.
4. At the next prompt, select the email account you want to use with Sell.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_pick_user.png)
5. Click **Accept** to grant Sell permission to have offline access.

   The
   synchronization process starts and the following page
   displays:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_email_integrate.png)
6. If you have previously signed in to your Microsoft account from the browser and
   your session is still stored, click **Sign in with Microsoft**.
7. Enter your username and password (your primary email address must be the same as
   your username for Zendesk Sell to integrate).
8. Select the account you want to use to connect. You've now completed the first
   layer of authorization. Now, a similar account screen will **appear again**.
   Select the same account you previously selected.
9. Once again, click **Accept** to grant Sell permission to have offline access.

   The synchronization process starts and the Communication Center page is
   displayed again.

Depending on the size of your inbox, the initial sync with Sell can take some time.
You'll receive an email notification when your inbox sync completes. The initial
sync will retrieve up to 1,500 emails from your mailbox, (Inbox, Sent, Archived and
other default and custom folders).

Note: [Microsoft ended support for basic
authentication access](https://support.zendesk.com/hc/en-us/articles/4408883370010) on September 30, 2022.

## Connecting your Google email (Gmail users)

Connecting your email accounts to Sell is easy.

**To connect your Gmail account**

1. On the Sell sidebar, click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then click **[Communication Channels > Email](https://app.futuresimple.com/settings/email)**.
2. Click **Sign in with Google**. Select **Allow** to grant Zendesk Sell
   permission to have offline access.

   The synchronization process
   starts.

Depending on the size of your inbox, the initial sync with Sell can take some time.
You'll receive an email notification when your inbox sync completes. The initial
sync will retrieve up to 1,500 emails from your mailbox, (Inbox, Sent, Archived and
other default and custom folders).

## Connecting your email (other users)

If you have an email account with any other email provider, follow these steps.

**To connect your email account**

1. On the Sell sidebar, click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then click **[Communication Channels > Email](https://app.futuresimple.com/settings/email)**.
2. Enter your email address and password.
3. Click **Connect**. If you have an Exchange server or email under your own
   domain, you are prompted to enter your SMTP server, SMTP port, IMAP server, and
   IMAP port settings. For information about finding your SMTP and IMAP settings,
   see [Email troubleshooting: SMTP and IMAP
   Settings](https://support.zendesk.com/hc/en-us/articles/4408829062170-Email-troubleshooting-SMTP-and-IMAP-Settings). Complete all of the fields so Sell can connect to your
   email server.
4. If prompted, enter the SMTP server, SMTP port, IMAP server, and IMAP port, and
   click **Connect**. This information typically takes the following form:

   |  |  |  |  |
   | --- | --- | --- | --- |
   | Protocol | Server Name | Port | Encryption Method |
   | IMAP4 | imap.yourdomain.com | 993 | SSL |
   | SMTP | smtp.yourdomain.com | 465 | SSL |

   If you're unsure of this information, check with your email service
   provider to confirm the details.

   Your email servers must have a valid,
   third-party SSL certificate installed (or TLS). Sell requires this to
   preserve the security of your data, and we will not be able to connect to
   your email server using unsecured servers or ports.
5. The synchronization process starts.

Depending on the size of your inbox, the initial sync with Sell can take some time.
You'll receive an email notification when your inbox sync completes. The initial
sync will retrieve up to 1,500 emails from your mailbox (Inbox, Sent, Archived and
other default and custom folders).

## Troubleshooting email integration issues

If you are having trouble with integrating your email, see [Troubleshooting email integration errors](https://support.zendesk.com/hc/en-us/articles/4408829007514).

## Next steps with your Sell email

Use these articles to discover what you can do next with your email in Sell:

- [Sharing email conversations with your
  team](https://support.zendesk.com/hc/en-us/articles/4408834060186)
- [Sending bulk email messages](https://support.zendesk.com/hc/en-us/articles/4408828307226)
- [Managing your Sell email, phone calls,
  and text messages](https://support.zendesk.com/hc/en-us/articles/4408824369818)
- [Creating and editing email
  templates](https://support.zendesk.com/hc/en-us/articles/4408821812890)
- [Monitoring email open rate and link
  clicks](https://support.zendesk.com/hc/en-us/articles/4408832035866)
- [How do I update the email integration on
  my account?](https://support.zendesk.com/hc/en-us/articles/4408825434266)
- [Customizing your email
  signature](https://support.zendesk.com/hc/en-us/articles/4408832176666)